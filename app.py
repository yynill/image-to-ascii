from PIL import Image
import os


def convert(image_name, new_width=500):
    # Correct path handling
    image_path = os.path.join('img', image_name)
    img = Image.open(image_path)

    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)

    img = img.resize((new_width, new_height))

    # Access resized image's pixels
    pixels = img.load()

    # ASCII characters from 'darkest' to 'lightest'
    ascii_chars = "@%#*+=-:. "

    # Calculate the scale for each brightness level to ASCII character mapping
    # 765 = 255 * 3 (max RGB value times three channels)
    scale_factor = 765 / len(ascii_chars)

    board = []
    for y in range(0, new_height, 2):
        row = []
        for x in range(new_width):
            # Calculate the brightness of the pixel
            brightness = sum(pixels[x, y])
            # Find the appropriate character
            char_index = int(brightness / scale_factor)
            row.append(ascii_chars[char_index])
        board.append(row)

    # Save the ASCII art to a text file
    ascii_file_path = image_name + "_ascii.txt"
    with open(ascii_file_path, 'w') as file:
        for row in board:
            file.write("".join(row) + "\n")


if __name__ == '__main__':
    convert('dune.jpg')
