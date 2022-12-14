import os

def connect_pathes(*pathes):
    return os.path.join(*pathes)

SAFE_CACHED_FOLDERS = ["App", "Constants", "Utilities"]
SAFE_PRE_EXISTING_CHECKLIST = ["Data Export"]

STORE_DATA_OUTPUT_PATH = "Data Export"

