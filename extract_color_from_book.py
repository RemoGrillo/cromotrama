import json

# 1. Read every word from the text file.
with open('orca.txt', 'r') as file:
    # Splitting by spaces to get individual words
    # We also strip punctuation to ensure a better match with dictionary keys
    words = [word.strip('.,!?;()[]{}"\'') for line in file for word in line.split()]

# 2. Load the colors.json file to check the words against.
with open('colors.json', 'r') as file:
    colors_dict = {key.lower(): value for key, value in json.load(file).items()}

# 3. For every word, check in "colors.json" if there's a key corresponding to that word.
found_words = [word for word in words if word.lower() in colors_dict]

# 4. Save the found words to "found_words.txt".
with open('found_words.txt', 'w') as file:
    for word in found_words:
        file.write(word + '\n')

# 5. Create a dictionary of found colors.
found_colors = {word.lower(): colors_dict[word.lower()] for word in found_words}

# 6. Save the found colors to "found_colors.json".
with open('found_colors.json', 'w') as file:
    json.dump(found_colors, file)

# 7. Create a colors.css stylesheet.
with open('colors.css', 'w') as css_file:
    for color, value in found_colors.items():
        css_file.write(f".{color} {{\n    color: {value};\n}}\n\n")
