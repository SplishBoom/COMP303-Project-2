
from Constants import connect_pathes, STORE_DATA_OUTPUT_PATH

def create_svg_output(number_of_cities:int):
    
    gen_font_family = "Times New Roman"
    gen_font_size = 20
    gen_storke_width = 1
    gen_scheme_color = "black"
    gen_fill_color = "white"
    gen_stroke_style = "fill: rgb(255, 255, 255);"
    gen_text_style = "white-space: pre;"

    if number_of_cities % 2 == 0 :
        maxColNum = int(number_of_cities/2)
    else :
        maxColNum = int(number_of_cities/2) + 1

    if number_of_cities == 0 :
        maxRowNum = 0
    elif number_of_cities == 1 :
        maxRowNum = 1
    else :
        maxRowNum = 2

    circR = 30
    p = 10
    city_locs = []

    width = 2*p + (maxColNum-1)*7*circR + 2*circR
    height = 2*p + (maxRowNum-1)*8*circR + 2*circR

    for i in range(number_of_cities) :
        if i == 0 :
            x = circR+p
            y = circR+p
            loc = (x,y)
            city_locs.append(loc)
        else :
            if i % 2 == 0 :
                previousX = city_locs[i-2][0]
                x = previousX + 7*circR
                y = city_locs[i-2][1]
                loc = (x,y)
                city_locs.append(loc)
            else :
                previousX = city_locs[i-1][0]
                x = previousX
                y = city_locs[i-1][1] + 8*circR
                loc = (x,y)
                city_locs.append(loc)
                
    city_circles = ""
    for i in city_locs :
        str = f"    <ellipse stroke=\"black\" stroke-width=\"1\" cx=\"{i[0]}\" cy=\"{i[1]}\" rx=\"30\" ry=\"30\" style=\"fill: rgb(255, 255, 255);\"/>\n"
        city_circles += str

    city_labels = ""
    count = 1
    for i in city_locs :
        str = f"    <text x=\"{i[0]}\" y=\"{i[1]}\" font-family=\"Times New Roman\" font-size=\"20\" style=\"white-space: pre; text-anchor: middle; dominant-baseline: middle;\">{count}</text>\n"
        count += 1
        city_labels += str

    svgStart = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
    svgSetting = f"<svg width=\"{width}\" height=\"{height}\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\">"
    svgBorder = f"<rect x=\"0\" y=\"0\" width=\"{width}\" height=\"{height}\" style=\"fill: rgb(255, 255, 255); stroke: rgb(0, 0, 0); stroke-width: 1;\"/>"
    svgEnd = "</svg>"

    edges = ""
    for i in range(number_of_cities) :
        for j in range(number_of_cities) :
            if i != j :
                if abs(i-j) <= 3 :
                    x1 = city_locs[i][0]
                    y1 = city_locs[i][1]
                    x2 = city_locs[j][0]
                    y2 = city_locs[j][1]
                    str = f"    <line x1=\"{x1}\" y1=\"{y1}\" x2=\"{x2}\" y2=\"{y2}\" stroke=\"black\" stroke-width=\"1\"/>\n"
                    edges += str

    edge_labels = ""
    for i in range(number_of_cities) :
        for j in range(number_of_cities) :
            if i != j :
                if abs(i-j) <= 3 :
                    x1 = city_locs[i][0]
                    y1 = city_locs[i][1]
                    x2 = city_locs[j][0]
                    y2 = city_locs[j][1]
                    x = (x1+x2)/2
                    y = (y1+y2)/2
                    str = f"    <text x=\"{x}\" y=\"{y}\" font-family=\"Times New Roman\" font-size=\"20\" style=\"white-space: pre; text-anchor: middle; dominant-baseline: middle;\">{i+j+2}</text>\n"
                    edge_labels += str

    edge_label_circles = ""
    for i in range(number_of_cities) :
        for j in range(number_of_cities) :
            if i != j :
                if abs(i-j) <= 3 :
                    x1 = city_locs[i][0]
                    y1 = city_locs[i][1]
                    x2 = city_locs[j][0]
                    y2 = city_locs[j][1]
                    x = (x1+x2)/2
                    y = (y1+y2)/2

                    y -= 0.03*circR*1.2
                    
                    str = f"    <ellipse stroke=\"black\" stroke-width=\"1\" cx=\"{x}\" cy=\"{y}\" rx=\"15\" ry=\"15\" style=\"fill: rgb(255, 255, 255); stroke-dasharray: 2px;\"/>\n"
                    edge_label_circles += str

    def create_svg(args) :
        
        svg = ""

        for arg in args :
            svg += arg
            svg += "\n"

        return svg

    svg = create_svg([svgStart, svgSetting, svgBorder, edges, city_circles, city_labels, edge_label_circles, edge_labels, svgEnd])

    with open("index.svg", "w") as f :
        f.write(svg)


def colorize_svg_output():
    pass

create_svg_output(10)