import os

def connect_pathes(*pathes):
    return os.path.join(*pathes)

RUN_CONFIG_FILE_PATH = connect_pathes("Constants", "run_config.json")

SAFE_CACHED_FOLDERS = ["Algorithms", "Constants", "Utilities"]
SAFE_UNNECESSARY_FOLDERS = ["Temp"]
SAFE_PRE_EXISTING_CHECKLIST = ["Data Export", "Temp"]

STORE_DATA_OUTPUT_PATH = "Data Export"
STORE_TEMP_OUTPUT_PATH = "Temp"

VISUAL_DIJKSTRA_SVG_OUTPUT_PATH = connect_pathes(STORE_TEMP_OUTPUT_PATH , "Dijkstra.svg")
VISUAL_ASTAR_SVG_OUTPUT_PATH = connect_pathes(STORE_TEMP_OUTPUT_PATH , "AStar.svg")
VISUAL_DIJKSTRA_PNG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Dijkstra.png")
VISUAL_ASTAR_PNG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "AStar.png")

SAVE_TIME_PLOT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Time_Plot.png")
SAVE_ITER_PLOT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Iter_Plot.png")