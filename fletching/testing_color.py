import time
import pyautogui
from PIL import Image


def get_pixel_color(x, y):
    """
    Get the color of a specific pixel on the screen.

    :param x: The x-coordinate of the pixel.
    :param y: The y-coordinate of the pixel.
    :return: The RGB color of the pixel.
    """
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert('RGB')

    # Get the color of the pixel at (x, y)
    pixel_color = screenshot.getpixel((x, y))
    return pixel_color

#time.sleep(3)
#print(get_pixel_color(1007, 476))


def search_rgb_color_on_screen(target_color, tolerance=10):
    """
    Search the screen for a specific RGB color with a tolerance for slight variations.

    :param target_color: The RGB color to search for (e.g., (105, 60, 104)).
    :param tolerance: The allowed difference in RGB values (default is 10).
    :return: A list of positions (x, y) where the color was found.
    """
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert('RGB')

    # Get the dimensions of the screen
    width, height = screenshot.size

    # List to store matches
    matches = []

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            # Check if the pixel color is within the tolerance range
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                matches.append((x, y))  # Store the position of the match

    return matches
