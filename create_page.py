import json

def get_colors_from_txt(filename):
    """Read colors from a txt file."""
    with open(filename, 'r') as file:
        colors = [line.strip().lower() for line in file]  # Convert to lowercase
    return colors

def get_color_dict_from_json(filename):
    """Read color dictionary from a JSON file and make it case-insensitive."""
    with open(filename, 'r') as file:
        color_dict = json.load(file)
    # Convert keys to lowercase for case-insensitive matching
    return {key.lower(): value for key, value in color_dict.items()}

def append_colors_to_html(colors, color_dict, output_filename, blacklist):
    """Create a new HTML page with colors."""
    html_content = []

    # Begin HTML content with a dark background and a web-friendly font
    html_content.append('<html><head>'
                        '<link href="colors.css" rel="stylesheet">'
                        '</head><body>\n')

    # Append colors
    for color in colors:
        if color not in blacklist:
            hex_value = color_dict.get(color, '#FFFFFF')  # Default to white if not found
            html_content.append(f'<span class="colorword {color}">{color}, </span> ')

    html_content.append('<style>body {'
                        'background-color: #191919;'
                        'color: #fff;'
                        '}'
                        '.colorword{'
                        'font-weight: bolder;'
                        'font-size:13pt;'
                        'font-family: Arial;'  # added Arial font here
                        '}'
                        '</style>\n')
    html_content.append('</body></html>\n')

    # Write the generated content
    with open(output_filename, 'w') as file:
        file.writelines(html_content)

def main():
    txt_filename = 'found_words.txt'
    json_filename = 'found_colors.json'
    output_filename = 'output2.html'

    colors = get_colors_from_txt(txt_filename)
    color_dict = get_color_dict_from_json(json_filename)

    # Define your blacklist here. Remember to keep it lowercase for case-insensitive matching.
    blacklist = ["sabbia", "conchiglia","tronco", "biscottino", "green", "limone", "kaki", "prugna", "cioccolato","isabella","argentino","argentina","pesca","biscotto"]  # Add colors you want to exclude

    append_colors_to_html(colors, color_dict, output_filename, blacklist)

if __name__ == '__main__':
    main()
