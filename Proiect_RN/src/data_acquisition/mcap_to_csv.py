import rclpy
from rclpy.serialization import deserialize_message
# Am corectat importurile eliminând 'rosbag2_py.' din interiorul funcției și asigurând clasele necesare
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions 
import pandas as pd
from collections import defaultdict
import os
import sys
import importlib 
# --- Configurarea ---
# ATENȚIE: Verifică dacă acest nume este exact cel al folderului din data/raw/
BAG_FOLDER_NAME = "rosbag2_2025_11_27-13_07_52_0" 

# Deoarece rulăm din /ws/project_data, BASE_DIR devine /ws/project_data/data/raw
BASE_DIR = os.path.join(os.getcwd(), "data", "raw")

# Calea completă catre directorul ROS Bag, necesară pentru StorageOptions(uri=...)
FULL_BAG_URI = os.path.join(BASE_DIR, BAG_FOLDER_NAME)

OUTPUT_DIR = BASE_DIR

TOPICS_TO_EXTRACT = ['/front_battery_state', '/rear_battery_state', '/joint_states']
# --------------------

def convert_bag_to_csv(bag_uri, output_dir, topics_to_extract):
    """
    Citeste ROS bag-ul dintr-un URI (cale) specificat si extrage datele in fisiere CSV separate.
    
    Args:
        bag_uri (str): Calea completă către directorul ROS Bag.
    """
    
    data_by_topic = defaultdict(list)
    reader = SequentialReader()
    
    # 1. Deschiderea bag-ului (Corecția finală a apelului StorageOptions)
    try:
        reader.open(
            # Utilizam calea completă (uri) și specificăm tipul de stocare
            StorageOptions(uri=bag_uri, storage_id='mcap'),
            # Opțiuni standard de conversie
            ConverterOptions(input_serialization_format='cdr', output_serialization_format='cdr') 
        )
    except Exception as e:
        print(f"[EROARE FATALĂ] Eroare la deschiderea bag-ului: {e}")
        print(f"Calea încercată (URI): {bag_uri}")
        print("Asigura-te ca directorul ROS Bag este complet si CALEA ABSOLUTĂ este corectă.")
        sys.exit(1)

    # 2. Obtinerea informatiilor despre topicuri (necesar pentru deserializare)
    topic_types = reader.get_all_topics_and_types()
    type_map = {topic_meta.name: topic_meta.type for topic_meta in topic_types}
    
    # 3. Citirea si Extragerea Mesajelor
    while reader.has_next():
        topic, data, t = reader.read_next()
        
        if topic in topics_to_extract:
            
            # Obținem numele tipului de mesaj (Ex: sensor_msgs/msg/BatteryState)
            msg_typename = type_map[topic]
            try:
                
                pkg_name, _, class_name = msg_typename.replace("/", ".").rpartition(".")
                pkg_module = importlib.import_module(pkg_name)
                msg_type = getattr(pkg_module, class_name)
                msg = deserialize_message(data, msg_type)
                row = extract_fields(topic, msg)
                data_by_topic[topic].append(row)
                
            except Exception as e:
                print(f"Avertisment: Eroare la deserializarea mesajului pe topicul {topic}. Eroare: {e}")
                continue 

    # 4. Salvarea in CSV
    for topic_name, data_list in data_by_topic.items():
        if not data_list:
            continue
            
        safe_name = topic_name.replace("/", "_").strip("_")
        output_file = os.path.join(output_dir, f"{safe_name}.csv")
        
        # Incarcarea in DataFrame si scrierea in CSV
        df = pd.DataFrame(data_list)
        df.to_csv(output_file, index=False)
        print(f"✅ Salvare reusita: {output_file} ({len(df)} randuri)")

def extract_fields(topic, msg):
    """Functie auxiliara pentru a extrage campurile specifice per tip de mesaj."""
    
    # Timestamp in format float (secunde + nanosecunde)
    ts_sec = msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9

    if "battery_state" in topic:
        # Mesaje BatteryState (pentru front si rear)
        return {
            'timestamp': ts_sec,
            'voltage': msg.voltage,
            'current': msg.current,
            'temperature': msg.temperature,
            'percentage': msg.percentage,
        }
    
    elif "joint_states" in topic:
        # Mesaje JointState (Extragerea vectorilor)
        data = {'timestamp': ts_sec}
        
        # Presupunem ca ordinea numelor (names) este constanta
        for i, name in enumerate(msg.name):
            # Extragerea vitezei si pozitiei individuale pe roata
            # Verificam daca vectorul de viteze are dimensiunea corecta inainte de a accesa
            if i < len(msg.velocity):
                data[f'velocity_{name}'] = msg.velocity[i]
            if i < len(msg.position):
                data[f'position_{name}'] = msg.position[i]
        return data

    # Mesaje necunoscute
    return {'timestamp': ts_sec, 'error': f"Unknown topic type for {topic}"}


if __name__ == '__main__':
    # Initializarea ROS 2 este necesara
    rclpy.init() 
    
    # Ruleaza functia principala, folosind calea completă (FULL_BAG_URI)
    convert_bag_to_csv(FULL_BAG_URI, OUTPUT_DIR, TOPICS_TO_EXTRACT)
    
    # Incheierea ROS 2
    rclpy.shutdown()