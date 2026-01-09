import random
import time
from sub import find_best_match, click_on_best_match, go_to_the_match,click_gauss
import os
import keyboard
import pickle


def process_step(directory_path, threshold, max_retries):
    """
    Process a single step by searching for the best match in a directory and clicking on it.

    :param directory_path: Directory to search for template images.
    :param threshold: Confidence threshold for template matching.
    :param max_retries: Maximum number of retries if no match is found.
    :return: True if a match was found and clicked; False otherwise.
    """
    retries = 0
    while retries < max_retries:
        best_match, confidence = find_best_match(directory_path, threshold)
        if best_match:
            # 50% chance to pick one of the two options
            if random.random() < 0.5:
                click_on_best_match(best_match, confidence, -11, 12, -12, 10)
            else:
                click_gauss(best_match, confidence, 0, 5, 0, 5)
            return True
        else:
            print(f"No match found in {directory_path}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(random.uniform(3, 4))
    print(f"Failed to find a match in {directory_path} after {max_retries} retries.")
    return False

def process_step_2(directory_path, threshold, max_retries):
    """
    Process a single step by searching for the best match in a directory and clicking on it.

    :param directory_path: Directory to search for template images.
    :param threshold: Confidence threshold for template matching.
    :param max_retries: Maximum number of retries if no match is found.
    :return: True if a match was found and clicked; False otherwise.
    """
    retries = 0
    while retries < max_retries:
        best_match, confidence = find_best_match(directory_path, threshold)
        if best_match:
            go_to_the_match(best_match, confidence, -11, 35, -11,11)
            return True
        else:
            print(f"No match found in {directory_path}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(random.uniform(3, 4))
    print(f"Failed to find a match in {directory_path} after {max_retries} retries.")
    return False

def antiban():
    process_step("iconskills", 0.9,2)
    process_step_2("iconwc",0.9,2)
    time.sleep(random.uniform(7,12))
    if random.random() >= 0.8:
        process_step("iconskills_2", 0.9, 2)

def antiban2(directory_path):
    time.sleep(2)
    # Directory containing the recordings
    directory_path = r"C:\Users\SinaKashani\Desktop\python\fishing\recordings"

    # Get a list of all `.pkl` files in the directory
    recording_files = [f for f in os.listdir(directory_path) if f.endswith(".pkl")]

    # Check if there are any recordings
    if not recording_files:
        print("No recordings found in the directory.")
    else:
        # Choose a random file
        random_file = random.choice(recording_files)
        file_path = os.path.join(directory_path, random_file)
        print(f"Playing random recording: {random_file}")

        # Load the chosen recording
        with open(file_path, "rb") as f:
            events = pickle.load(f)

        # Replay the recorded events
        print("Replaying recorded events...")
        last_time = events[0].time if events else None

        for event in events:
            if last_time is not None:
                delay = event.time - last_time
                if delay > 0:
                    time.sleep(delay)  # Maintain recorded timing
            last_time = event.time

            if event.event_type == "down":
                keyboard.press(event.name)
            elif event.event_type == "up":
                keyboard.release(event.name)

        print("Playback finished.")
        time.sleep(2)


