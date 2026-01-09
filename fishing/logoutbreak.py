import cv2
import os
from PIL import ImageGrab
import numpy as np
import pyautogui
import random
import time
from sub import find_best_match, go_to_the_match, click_on_best_match

directory_first = [
    r"C:\Users\SinaKashani\Desktop\python\fishing\logout1",
    r"C:\Users\SinaKashani\Desktop\python\fishing\logout2",
    r"C:\Users\SinaKashani\Desktop\python\fishing\login1",
    r"C:\Users\SinaKashani\Desktop\python\fishing\login2"
]

# Define custom offsets for each step
offsets = {
    1: (-8, 8, -13, 13),  # Coordinates for step 1
    2: (-69, 69, -69, 69),  # Coordinates for step 2
    3: (-15, 15, -15, 15),  # Coordinates for step 3
    4: (-20, 20, -20, 20),  # Coordinates for step 4
}

def process_step(directory_path, step, threshold=0.9, max_retries=5):
    """
    Process a single step by searching for the best match in a directory and clicking on it.

    :param directory_path: Directory to search for template images.
    :param step: The current step number.
    :param threshold: Confidence threshold for template matching.
    :param max_retries: Maximum number of retries if no match is found.
    :return: True if a match was found and clicked; False otherwise.
    """
    retries = 0
    while retries < max_retries:
        best_match, confidence = find_best_match(directory_path, threshold)
        if best_match:
            # Use offsets specific to the current step
            a, b, c, d = offsets.get(step, (-3, 3, -3, 3))  # Default to step 1 offsets if step is not found
            click_on_best_match(best_match, confidence, a, b, c, d)
            return True
        else:
            print(f"No match found in {directory_path}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(random.uniform(3, 4))
            if retries == 4:
                antiban2()
    print(f"Failed to find a match in {directory_path} after {max_retries} retries.")
    return False


def logout():
    previous_step = None
    current_step = 1
    while current_step <= len(directory_first):
        directory = directory_first[current_step - 1]
        print(f"Starting step {current_step}: Searching in {directory}")

        if current_step == 3:
            # Add a significant break before the second step
            print("Pausing before the second step...")
            time.sleep(random.uniform(967,1684))  # Adjust this duration as needed

        if process_step(directory, threshold=0.9):
            print(f"Step {current_step} completed successfully. Moving to the next step.")
            previous_step = directory  # Remember the last successful step
            current_step += 1  # Move to the next step
        else:
            print(f"Step {current_step} failed. Attempting the previous step...")
            if previous_step and process_step(previous_step, threshold=0.9):
                print(f"Recovered by redoing the previous step: {previous_step}. Retrying step {current_step}.")
                continue  # Retry the same step
            else:
                print(f"Previous step also failed. Exiting script.")
                break