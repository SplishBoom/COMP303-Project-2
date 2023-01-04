"""
This script is used to make sure that the program is safe to start and end.
"""


from Constants import (
    SAFE_PRE_EXISTING_CHECKLIST,
    RUN_CONFIG_FILE_PATH,
)
import json
import  os

def safe_start() :
    """
    Makes sure that the program is safe to start.
    """

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
        dummy = configFile["number_of_cities"], configFile["is_continuously_generated"], configFile["start_city"], configFile["destination_city"], configFile["will_visualize_data"], configFile["will_plot_data"]
    except :
        fixData = {
            "number_of_cities" : 20,
            "is_continuously_generated" : False,
            "start_city" : 1,
            "destination_city" : 20,
            "will_visualize_data" : True,
            "will_plot_data" : True
        }
        with open(RUN_CONFIG_FILE_PATH, "w") as f:
            json.dump(fixData, f, sort_keys=True, indent=4)

def safe_stop() :
    """
    Makes sure that the program is safe to end.
    """

    # CACHE CLEANUP, TEMP DELETIONS ARE REMOVED. THIS FUNCTION IS DUMMY. BUT CAN BE USED IF NEEDED.

    exit()