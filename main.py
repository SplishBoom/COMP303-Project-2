from Utilities import safe_start, safe_stop, visualize
from Algorithms import AStar, Dijkstra, MyGraph
import timeit
from Constants import RUN_CONFIG_FILE_PATH, SAVE_TIME_PLOT_PATH, SAVE_ITERATIONS_PLOT_PATH
import argparse
import json
import keyboard
from matplotlib import pyplot as plt

def execute(number_of_cities:int, start_city:int, destination_city:int) -> dict:
    """
    Function, executes one times for a given case, and returns the results.
    @params :
        number_of_cities    -   Required    :   The number of cities. (int)
        start_city          -   Required    :   The start city. (int)
        destination_city    -   Required    :   The destination city. (int)
    @return :
        A dictionary, containing the results of the execution. (dict)
    """

    graph_object = MyGraph(number_of_cities)
    graph_object.generate_graph()
    graph = graph_object.graph

    dijkstra_object = Dijkstra()
    start_of_dijkstra = timeit.default_timer()
    dijkstra_result = dijkstra_object.solve(graph, start_city, destination_city)
    end_of_dijkstra = timeit.default_timer()
    dijkstra_time = (round((end_of_dijkstra - start_of_dijkstra) * 10 ** 6, 3))

    a_star_object = AStar()
    start_of_a_star = timeit.default_timer()
    a_star_result = a_star_object.solve(graph, start_city, destination_city)
    end_of_a_star = timeit.default_timer()
    a_star_time = (round((end_of_a_star - start_of_a_star) * 10 ** 6, 3))

    state = (dijkstra_result[0] == a_star_result[0])

    return {
        "number_of_cities" : number_of_cities,
        "start_city" : start_city,
        "destination_city" : destination_city,
        "simulate_correct" : state,

        "DIJKSTRA" : {
            "time" : dijkstra_time,
            "path" : dijkstra_result[0],
            "cost" : dijkstra_result[1],
            "iterations" : dijkstra_result[2],
        },

        "ASTAR" : {
            "time" : a_star_time,
            "path" : a_star_result[0],
            "cost" : a_star_result[1],
            "iterations" : a_star_result[2],
        },
    }

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r") -> None:
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  :   iterable object (Iterable)
        prefix      - Optional  :   prefix string (Str)
        suffix      - Optional  :   suffix string (Str)
        decimals    - Optional  :   positive number of decimals in percent complete (Int)
        length      - Optional  :   character length of bar (Int)
        fill        - Optional  :   bar fill character (Str)
        printEnd    - Optional  :   end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

def simulate(number_of_cities:int, is_continuously_generated:bool, start_city:int, destination_city:int) -> list:
    """
    Function, simulates the execution of the script for a given case.
    @params :
        number_of_cities            -   Required    :   The number of cities. (int)
        is_continuously_generated   -   Required    :   If this flag is set, the script will generate test cases continuously from 1 to N. (bool)
        start_city                  -   Required    :   The start city. (int)
        destination_city            -   Required    :   The destination city. (int)
    @return : 
        data                        -   Required    :   The result of the simulation. (list)
    """

    print("\n*** Simulation started.")
    data = []

    if not is_continuously_generated:
        data.append(execute(number_of_cities, start_city, destination_city))
    else:
        iterable = [i for i in range(1, number_of_cities + 1, 1)]
        for number_of_cities in progressBar(iterable, prefix = 'Simulating:', suffix = 'Complete', length = 50):
            try :
                data.append(execute(number_of_cities, 1, number_of_cities))
            except :
                print(f"** Error occured while generating test case {number_of_cities}. Program will skip this amount.")
            if keyboard.is_pressed("ESC") and keyboard.is_pressed("C") and keyboard.is_pressed("L") and keyboard.is_pressed("S") :
                print("** User stopped generating test cases. Program will now continue by results.")
                break

    return data

def visualize_data(result:list, will_visualize_data:bool) -> str:
    """
    Method, visualizes the given data.
    @params :
        result                  -   Required    :   The result of the simulation. (dict)
        will_visualize_data     -   Required    :   If this flag is set, the script will visualize the data. (bool)
    @return :
        None
    """

    if (not will_visualize_data) or (not result["simulate_correct"]):
        return
    
    dijkstra_path = result["DIJKSTRA"]["path"]
    astar_path = result["ASTAR"]["path"]

    number_of_cities = result["number_of_cities"]

    visualize(number_of_cities, dijkstra_path)

def plot_data(data:list, will_plot_data:bool) -> None:
    """
    Method, that takes the dict results of executions. And creates two plots about Dijkstra VS AStar. In case of aXb, where a is y axis, and b is x axis.
    First, it plots : time X number of cities.
    Second, it plots : iterations X number of cities.
    After that, it saves the plots.
    @params :
        data                -   Required    :   The result of the simulation. (list)
        will_plot_data      -   Required    :   If this flag is set, the script will plot the data. (bool)
    @return :
        None
    """

    if not will_plot_data:
        return

    # timeXcities
    plt.figure(figsize=(10, 10))
    plt.plot([i["number_of_cities"] for i in data], [i["DIJKSTRA"]["time"] for i in data], label="Dijkstra")
    plt.plot([i["number_of_cities"] for i in data], [i["ASTAR"]["time"] for i in data], label="AStar")
    plt.xlabel("Number of Cities")
    plt.ylabel("Time (s)")
    plt.title("Time X Number of Cities")
    plt.legend()
    plt.tight_layout()
    plt.savefig(SAVE_TIME_PLOT_PATH)
    plt.close()

    # iterationsXcities
    plt.figure(figsize=(10, 10))
    plt.plot([i["number_of_cities"] for i in data], [max(i["DIJKSTRA"]["iterations"].values()) for i in data], label="Dijkstra")
    plt.plot([i["number_of_cities"] for i in data], [max(i["ASTAR"]["iterations"].values()) for i in data], label="AStar")
    plt.xlabel("Number of Cities")
    plt.ylabel("Iterations")
    plt.title("Iterations X Number of Cities")
    plt.legend()
    plt.tight_layout()
    plt.savefig(SAVE_ITERATIONS_PLOT_PATH)
    plt.close()


def main(number_of_cities:int, is_continuously_generated:bool, start_city:int, destination_city:int, will_visualize_data:bool, will_plot_data:bool) -> None:
    """
    Main function of the script, IT drives through thw the program acording to the given parameters.
    @params :
        number_of_cities            -   Required    :   The number of cities. (int)
        is_continuously_generated   -   Required    :   If this flag is set, the script will generate test cases continuously from 1 to N. (bool)
        start_city                  -   Required    :   The start city. (int)
        destination_city            -   Required    :   The destination city. (int)
        will_visualize_data         -   Required    :   If this flag is set, the script will visualize the results. (bool)
        will_plot_data              -   Required    :   If this flag is set, the script will plot the results. (bool)
    @return : 
        None
    """

    simulation_results = simulate(number_of_cities, is_continuously_generated, start_city, destination_city)

    plot_data(simulation_results, will_plot_data)

    visualize_data(simulation_results[-1], will_visualize_data)


def get_arguments() -> tuple:
    """
    Method, that takes arguments and lines up the program.
    @returns:
    (
        number_of_cities : int -> The number of cities.
        is_continuously_generated : bool -> If this flag is set, the script will generate test cases continuously from 1 to N.
        start_city : int -> The start city.
        destination_city : int -> The destination city.
        will_visualize_data : bool -> If this flag is set, the script will visualize the data.
        will_plot_data : bool -> If this flag is set, the script will plot the data.
    )
    """

    parser = argparse.ArgumentParser(description="This script is used to compare the performance of the two well-known shortest path finder algorithms.")
    parser.add_argument("-n", "--number-of-cities", type=int, help="The number of cities in the graph.", required=False)
    parser.add_argument("-c", "--continuously-generate", type=int, help="If this flag is set, the script will generate test cases continuously from 1 to N.", required=False, default=False)
    parser.add_argument("-st", "--start-city", type=int, help="The start city.", required=False)
    parser.add_argument("-dt", "--destination-city", type=int, help="The destination city.", required=False)
    parser.add_argument("-v", "--visualize-results", type=int, help="If this flag is set, the results will be visualized.", required=False, default=False)
    parser.add_argument("-p", "--plot-results", type=int, help="If this flag is set, the results will be plotted.", required=False, default=False)
    args = parser.parse_args()

    number_of_cities = args.number_of_cities
    is_continuously_generated = args.continuously_generate
    start_city = args.start_city
    destination_city = args.destination_city
    will_visualize_data = args.visualize_results
    will_plot_data = args.plot_results

    if number_of_cities is None:
        with open(RUN_CONFIG_FILE_PATH, "r") as infile:
            configFile = json.load(infile)
        number_of_cities = configFile["number_of_cities"]
        is_continuously_generated = configFile["is_continuously_generated"]
        start_city = configFile["start_city"]
        destination_city = configFile["destination_city"]
        will_visualize_data = configFile["will_visualize_data"]
        will_plot_data = configFile["will_plot_data"]
    else:
        fixData = {
            "number_of_cities" : number_of_cities,
            "is_continuously_generated" : is_continuously_generated,
            "start_city" : start_city,
            "destination_city" : destination_city,
            "will_visualize_data" : will_visualize_data,
            "will_plot_data" : will_plot_data
        }
        with open(RUN_CONFIG_FILE_PATH, "w") as f:
            json.dump(fixData, f, sort_keys=True, indent=4)

    return (
        int(number_of_cities),
        bool(is_continuously_generated),
        int(start_city),
        int(destination_city),
        bool(will_visualize_data),
        bool(will_plot_data)
    )

if __name__ == "__main__":
    
    safe_start()

    args = get_arguments()

    main(*args)

    safe_stop()