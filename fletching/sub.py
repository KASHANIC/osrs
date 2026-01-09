import cv2
import os
from PIL import ImageGrab
import numpy as np
import pyautogui
import random
import time
from humancursor import SystemCursor
import math


def hex_to_bgr(hex_color):
    """ Convert a HEX color to BGR for OpenCV. """
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))  # Convert HEX to BGR


def find_color(hex_color, tolerance=100):
    """
    Scan the screen and find the given hex color.

    :param hex_color: HEX color to find (e.g., "#ff0000" for red).
    :param tolerance: Allowed variation in color detection.
    :return: List of (x, y) coordinates where the color is found.
    """
    bgr_target = np.array(hex_to_bgr(hex_color), dtype=np.uint8)  # Convert to BGR
    lower_bound = np.clip(bgr_target - tolerance, 0, 255)
    upper_bound = np.clip(bgr_target + tolerance, 0, 255)

    # Capture the screen
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Create a mask for the color
    mask = cv2.inRange(screenshot, lower_bound, upper_bound)

    # Find all pixel positions where the color is detected
    coords = np.column_stack(np.where(mask > 0))

    if len(coords) == 0:
        return None  # No color found

    return coords.tolist()  # Return list of (y, x) coordinates

def find_best_match(directory_path, threshold=0.6):
    """
    Compare multiple template images in the specified directory against the screen and return the best match.

    :param directory_path: Path to the directory containing template image files.
    :param threshold: Confidence threshold for template matching.
    :return: Coordinates (x, y) of the best match center and the match confidence.
    """
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    best_match = None
    highest_confidence = 0

    for filename in os.listdir(directory_path):
        template_path = os.path.join(directory_path, filename)
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Could not load template image from {template_path}")
            continue

        template_h, template_w = template.shape
        screenshot_h, screenshot_w = screenshot_gray.shape
        if template_h > screenshot_h or template_w > screenshot_w:
            scale = min(screenshot_h / template_h, screenshot_w / template_w)
            template = cv2.resize(template, (int(template_w * scale), int(template_h * scale)))

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > highest_confidence and max_val >= threshold:
            highest_confidence = max_val
            template_h, template_w = template.shape[:2]
            best_match = (max_loc[0] + template_w // 2, max_loc[1] + template_h // 2)

    return best_match, highest_confidence


def find_closest_match(directory_path, threshold=0.6, target_coords=(820, 530)):
    """
    Find all template matches above a given threshold and return the closest to the target coordinates.

    :param directory_path: Path to the directory containing template image files.
    :param threshold: Confidence threshold for template matching.
    :param target_coords: The target pixel coordinates (x, y) to find the closest match.
    :return: The closest match center (x, y) and its confidence.
    """
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    matches = []  # Store all matches above the threshold

    for filename in os.listdir(directory_path):
        template_path = os.path.join(directory_path, filename)
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Could not load template image from {template_path}")
            continue

        template_h, template_w = template.shape
        screenshot_h, screenshot_w = screenshot_gray.shape
        if template_h > screenshot_h or template_w > screenshot_w:
            scale = min(screenshot_h / template_h, screenshot_w / template_w)
            template = cv2.resize(template, (int(template_w * scale), int(template_h * scale)))

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            template_h, template_w = template.shape[:2]
            match_center = (max_loc[0] + template_w // 2, max_loc[1] + template_h // 2)
            matches.append((match_center, max_val))

    if matches:
        # Find the match closest to the target coordinates
        closest_match = min(matches, key=lambda match: math.sqrt(
            (match[0][0] - target_coords[0]) ** 2 + (match[0][1] - target_coords[1]) ** 2
        ))
        return closest_match
    else:
        return None, 0


def click_on_best_match(best_match, confidence, a, b, c, d):
    """
    Simulate human-like mouse movement to click on the best match if it exists.

    :param best_match: Tuple (x, y) of the best match center coordinates.
    :param confidence: Confidence score of the best match.
    :param a: Minimum x-offset for randomness.
    :param b: Maximum x-offset for randomness.
    :param c: Minimum y-offset for randomness.
    :param d: Maximum y-offset for randomness.
    """
    if best_match:
        print(f"Best match found at {best_match} with confidence {confidence:.2f}. Clicking...")

        # Introduce random offset to simulate human imprecision
        target_x = best_match[0] + random.randint(a, b)
        target_y = best_match[1] + random.randint(c, d)

        # Initialize HumanCursor's SystemCursor
        cursor = SystemCursor()

        # Move the mouse to the target position with human-like movement
        cursor.move_to([target_x, target_y])

        # Add a small delay before clicking to simulate hesitation
        time.sleep(random.uniform(0, 0.003))

        # Perform the click
        pyautogui.click()

    else:
        print("No suitable match found.")

import pyautogui
import random
import time

def click_on_best_match_bot(best_match, confidence, a, b, c, d):
    """
    Simulate human-like mouse movement to click on the best match if it exists.

    :param best_match: Tuple (x, y) of the best match center coordinates.
    :param confidence: Confidence score of the best match.
    :param a: Minimum x-offset for randomness.
    :param b: Maximum x-offset for randomness.
    :param c: Minimum y-offset for randomness.
    :param d: Maximum y-offset for randomness.
    """
    if best_match:
        print(f"Best match found at {best_match} with confidence {confidence:.2f}. Clicking...")

        # Introduce random offset to simulate human imprecision
        target_x = best_match[0] + random.randint(a, b)
        target_y = best_match[1] + random.randint(c, d)

        # Move the mouse to the target position with a smooth transition
        pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.3), tween=pyautogui.easeOutQuad)

        # Add a small delay before clicking to simulate hesitation
        time.sleep(random.uniform(0, 0.003))

        # Perform the click
        pyautogui.click()
    else:
        print("No suitable match found.")


def go_to_the_match(best_match, confidence, a, b, c, d):
    """
    Simulate human-like mouse movement to click on the best match if it exists.

    :param best_match: Tuple (x, y) of the best match center coordinates.
    :param confidence: Confidence score of the best match.
    :param a: Minimum x-offset for randomness.
    :param b: Maximum x-offset for randomness.
    :param c: Minimum y-offset for randomness.
    :param d: Maximum y-offset for randomness.
    """
    if best_match:
        print(f"Best match found at {best_match} with confidence {confidence:.2f}. Clicking...")

        # Introduce random offset to simulate human imprecision
        target_x = best_match[0] + random.randint(a, b)
        target_y = best_match[1] + random.randint(c, d)

        # Initialize HumanCursor's SystemCursor
        cursor = SystemCursor()

        # Move the mouse to the target position with human-like movement
        cursor.move_to([target_x, target_y])

        # Add a small delay before clicking to simulate hesitation
        time.sleep(random.uniform(0.001, 0.003))

    else:
        print("No suitable match found.")

def click_gauss(best_match, confidence, mean_x, stddev_x, mean_y, stddev_y):
    """
    Simulate human-like mouse movement to click on the best match if it exists.

    :param best_match: Tuple (x, y) of the best match center coordinates.
    :param confidence: Confidence score of the best match.
    :param mean_x: Mean x-offset for the Gaussian distribution.
    :param stddev_x: Standard deviation for the x-offset.
    :param mean_y: Mean y-offset for the Gaussian distribution.
    :param stddev_y: Standard deviation for the y-offset.
    """
    if best_match:
        print(f"Best match found at {best_match} with confidence {confidence:.2f}. Clicking...")

        # Introduce Gaussian offset to simulate human-like imprecision
        offset_x = int(random.gauss(mean_x, stddev_x))
        offset_y = int(random.gauss(mean_y, stddev_y))
        target_x = best_match[0] + offset_x
        target_y = best_match[1] + offset_y

        # Initialize HumanCursor's SystemCursor
        cursor = SystemCursor()

        # Move the mouse to the target position with human-like movement
        cursor.move_to([target_x, target_y])

        # Add a small delay before clicking to simulate hesitation
        time.sleep(random.uniform(0.001, 0.003))  # Adjust delay as needed

        # Perform the click
        pyautogui.click()

    else:
        print("No suitable match found.")


def click_gauss_bot(best_match, confidence, mean_x, stddev_x, mean_y, stddev_y):
    """
    Simulate human-like mouse movement to click on the best match if it exists.

    :param best_match: Tuple (x, y) of the best match center coordinates.
    :param confidence: Confidence score of the best match.
    :param mean_x: Mean x-offset for the Gaussian distribution.
    :param stddev_x: Standard deviation for the x-offset.
    :param mean_y: Mean y-offset for the Gaussian distribution.
    :param stddev_y: Standard deviation for the y-offset.
    """
    if best_match:
        print(f"Best match found at {best_match} with confidence {confidence:.2f}. Clicking...")

        # Introduce Gaussian offset to simulate human-like imprecision
        offset_x = int(random.gauss(mean_x, stddev_x))
        offset_y = int(random.gauss(mean_y, stddev_y))
        target_x = best_match[0] + offset_x
        target_y = best_match[1] + offset_y

        # Move the mouse to the target position with a very fast transition
        pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.002, 0.008), tween=pyautogui.easeOutQuad)

        # Add a small delay before clicking to simulate hesitation
        time.sleep(random.uniform(0, 0.002))

        # Perform the click
        pyautogui.click()

    else:
        print("No suitable match found.")

def click_gauss_closest(matches, confidence_scores, mean_x, stddev_x, mean_y, stddev_y, target_coords=(823, 517)):
    """
    Click on the match closest to a target coordinate (default: 823,517) with human-like mouse movement.

    :param matches: List of tuples [(x, y), (x, y), ...] representing match center coordinates.
    :param confidence_scores: List of confidence scores corresponding to each match.
    :param mean_x: Mean x-offset for Gaussian distribution.
    :param stddev_x: Standard deviation for x-offset.
    :param mean_y: Mean y-offset for Gaussian distribution.
    :param stddev_y: Standard deviation for y-offset.
    :param target_coords: Tuple (x, y) of the desired closest position.
    """
    if not matches:
        print("No matches found.")
        return

    # Find the closest match based on Euclidean distance
    closest_match = min(matches, key=lambda match: math.dist(match, target_coords))
    closest_confidence = confidence_scores[matches.index(closest_match)]

    print(f"Closest match found at {closest_match} with confidence {closest_confidence:.2f}. Clicking...")

    # Introduce Gaussian offset to simulate human-like imprecision
    offset_x = int(random.gauss(mean_x, stddev_x))
    offset_y = int(random.gauss(mean_y, stddev_y))
    target_x = closest_match[0] + offset_x
    target_y = closest_match[1] + offset_y

    # Initialize HumanCursor's SystemCursor
    cursor = SystemCursor()

    # Move the mouse to the target position with human-like movement
    cursor.move_to([target_x, target_y])

    # Add a small delay before clicking to simulate hesitation
    time.sleep(random.uniform(0.001, 0.003))  # Adjust delay as needed

    # Perform the click
    pyautogui.click()


def find_random_match(directory_path, threshold=0.6):
    """
    Find all template matches above a given threshold and return one randomly.

    :param directory_path: Path to the directory containing template image files.
    :param threshold: Confidence threshold for template matching.
    :return: Randomly selected match center (x, y) and its confidence.
    """
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    matches = []  # Store all matches above the threshold

    for filename in os.listdir(directory_path):
        template_path = os.path.join(directory_path, filename)
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Could not load template image from {template_path}")
            continue

        template_h, template_w = template.shape
        screenshot_h, screenshot_w = screenshot_gray.shape
        if template_h > screenshot_h or template_w > screenshot_w:
            scale = min(screenshot_h / template_h, screenshot_w / template_w)
            template = cv2.resize(template, (int(template_w * scale), int(template_h * scale)))

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            template_h, template_w = template.shape[:2]
            match_center = (max_loc[0] + template_w // 2, max_loc[1] + template_h // 2)
            matches.append((match_center, max_val))

    if matches:
        # Randomly choose one match from the list
        chosen_match = random.choice(matches)
        return chosen_match
    else:
        return None, 0


