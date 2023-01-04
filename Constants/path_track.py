import os

def connect_pathes(*pathes):
    return os.path.join(*pathes)

SAFE_PRE_EXISTING_CHECKLIST = ["Data Export"]

RUN_CONFIG_FILE_PATH = "run_config.json"

STORE_DATA_OUTPUT_PATH = "Data Export"

VISUAL_SVG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Graph_SVG.svg")
VISUAL_PNG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Graph_PNG.png")

SAVE_TIME_PLOT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Plot_Time.png")
SAVE_ITERATIONS_PLOT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Plot_Iterations.png")
SAVE_COST_PLOT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Plot_Cost.png")