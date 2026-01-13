import os

# 1. Căi de bază
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# 2. Fișierul de intrare (Cel existent deja)
INPUT_FILE = os.path.join(PROCESSED_DATA_DIR, 'full_dataset_synchronized.csv')

# 3. Parametrii Modelului
FEATURES = [
    'voltage_V', 
    'current_total_A', 
    'temperature_C', 
    'percentage_SoC', 
    'robot_speed_avg_rads'
]

TARGET = 'target_RUL_seconds'

# Setări antrenare
TEST_SIZE = 0.2
RANDOM_STATE = 42