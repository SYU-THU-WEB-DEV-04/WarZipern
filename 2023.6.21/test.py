import re


def parse_display_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    color_pattern = r"\( display\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s*\)"
    colors = re.findall(color_pattern, data)

    color_dict = {}
    for color in colors:
        color_name, red, green, blue = color
        color_dict[color_name] = (int(red), int(green), int(blue))

    return color_dict


file_path = "E:\\EDA\\vue-project\\demo\\display.drf"
color_dict = parse_display_data(file_path)


for color_name, rgb in color_dict.items():
    print(f"Color: {color_name}, RGB: {rgb}")
