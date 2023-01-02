import  os
import  shutil
import json

from Constants import SAFE_CACHED_FOLDERS, SAFE_PRE_EXISTING_CHECKLIST, SAFE_UNNECESSARY_FOLDERS, RUN_CONFIG_FILE_PATH

def safe_start() :

    for path in SAFE_PRE_EXISTING_CHECKLIST :
        if not os.path.exists(path) :
            if os.path.splitext(path)[1] == "" :
                os.mkdir(path)
            else :
                with open(path, "w") as f :
                    f.write("")

    # Check if 
    try :
        with open (RUN_CONFIG_FILE_PATH, "r") as infile:
            configFile = json.load(infile)
        dummy = configFile["number_of_cities"], configFile["is_continuously_generated"], configFile["start_city"], configFile["destination_city"], configFile["will_save_data"], configFile["will_plot_data"]
    except :
        fixData = {
            "number_of_cities" : 1000,
            "is_continuously_generated" : False,
            "start_city" : 1,
            "destination_city" : 1000,
            "will_save_data" : True,
            "will_plot_data" : True
        }
        with open(RUN_CONFIG_FILE_PATH, "w") as f:
            json.dump(fixData, f, sort_keys=True, indent=4)

def safe_stop() :

    projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for folder in SAFE_CACHED_FOLDERS :
        folderPath = os.path.join(projectDir, folder)
        for root, dirs, files in os.walk(folderPath):
            for dir in dirs :
                if dir == "__pycache__" :
                    shutil.rmtree(os.path.join(root, dir))

    # clear SAFE_UNNECESSARY_FOLDERS
    for folder in SAFE_UNNECESSARY_FOLDERS :
        folderPath = os.path.join(projectDir, folder)
        shutil.rmtree(folderPath)

    exit()