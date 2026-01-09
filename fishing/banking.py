import random
import time
from antiban import antiban2, antiban
from sub import find_best_match, click_on_best_match, go_to_the_match, click_gauss

extra_inv = r"C:\Users\SinaKashani\Desktop\python\fishing\extra_inv_check"

directory_first = [
    r"C:\Users\SinaKashani\Desktop\python\fishing\1",
    r"C:\Users\SinaKashani\Desktop\python\fishing\2",
    r"C:\Users\SinaKashani\Desktop\python\fishing\3",
    r"C:\Users\SinaKashani\Desktop\python\fishing\4"
]

directory_second = [
    r"C:\Users\SinaKashani\Desktop\python\fishing\5",
    r"C:\Users\SinaKashani\Desktop\python\fishing\6",
    r"C:\Users\SinaKashani\Desktop\python\fishing\7",
    r"C:\Users\SinaKashani\Desktop\python\fishing\8"
]

# Define custom offsets for each step
offsets = {
    1: (-1, 2, -3, 2),  # Coordinates for step 1    x positief rechts y positief beneden
    2: (-0, 4, 0, 3),  # Coordinates for step 2
    3: (-0, 4, 0, 3),  # Coordinates for step 3
    4: (0, 1, 15, 3),  # Coordinates for step 4
}



def process_step(directory_path, step, threshold=0.8, max_retries=40):
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
        # Find the best match
        best_match, confidence = find_best_match(directory_path, threshold)

        if best_match:
            # Retrieve offsets specific to the current step
            a, b, c, d = offsets.get(step, (-3, 3, -3, 3))  # Default offsets if step is not in the offsets dictionary

            print(f"Match found at {best_match} with confidence {confidence:.2f}. Proceeding to click...")
            click_gauss(best_match, confidence, a, b, c, d)
            return True
        else:
            # Log retry and add delay
            print(f"No match found in {directory_path}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1

            if step == 4 and retries in {3,4}:
                print("Say Less")
                antiban2(directory_path=r"C:\Users\SinaKashani\Desktop\python\fishing\recordings")

            # Execute antiban2 after a specific retry count
            if random.random() <= 0.3:
                if retries == 3:
                    print("Triggering antiban2 for safety.")
                    antiban2(directory_path=r"C:\Users\SinaKashani\Desktop\python\fishing\left_rec")
            else:
                print("No antiban")

    print(f"Failed to find a match in {directory_path} after {max_retries} retries.")
    return False

def banking():
    previous_step = None
    current_step = 1

    # Check if a 99% confidence match is found in directory 2 to skip to step 2
    best_match, confidence = find_best_match(r"C:\Users\SinaKashani\Desktop\python\fishing\2", 0.80)
    if confidence >= 0.80:
        print("High-confidence match found for step 2. Skipping to step 2...")
        click_on_best_match(best_match, confidence, a=-5, b=5, c=-5, d=5)
        current_step = 3
    else:
        print("No high-confidence match found. Starting from step 1.")

    while current_step <= len(directory_first):
        time.sleep(random.uniform(2, 3))
        directory = directory_first[current_step - 1]
        print(f"Starting step {current_step}: Searching in {directory}")

        if current_step == 2:
            # Add a significant break before the second step
            print("Pausing before the second step...")
            time.sleep(random.uniform(6, 8))  # Adjust this duration as needed

        if process_step(directory, current_step, threshold=0.8):
            print(f"Step {current_step} completed successfully. Moving to the next step.")
            previous_step = directory  # Remember the last successful step
            current_step += 1  # Move to the next step
        else:
            print(f"Step {current_step} failed. Attempting the previous step...")
            if previous_step and process_step(previous_step, current_step - 1, threshold=0.8):
                print(f"Recovered by redoing the previous step: {previous_step}. Retrying step {current_step}.")
                continue  # Retry the same step
            else:
                print(f"Previous step also failed. Exiting script.")
                exit(20)
    #time.sleep(random.uniform(0,1 ))

def banking_2():
        previous_step = None
        current_step = 1
        while current_step <= len(directory_first):
            time.sleep(random.uniform(2, 3))
            directory = directory_second[current_step - 1]
            print(f"Starting step {current_step}: Searching in {directory}")

            if current_step == 2:
                # Add a significant break before the second step
                print("Pausing before the second step...")
                time.sleep(random.uniform(4, 6))  # Adjust this duration as needed

            if current_step == 3:
                time.sleep(random.uniform(1.25, 1.88))
                retry_attempts = 3  # Maximum number of retries
                for attempt in range(retry_attempts):
                    if find_best_match(extra_inv, 0.5):
                        print("Inventory clean process successful.")
                        break
                    else:
                        print(f"Step 3 attempt {attempt + 1} failed. Retrying...")
                        time.sleep(random.uniform(1, 2))  # Pause before retrying
                else:
                    print("All retry attempts for step 3 failed. Fixing step 3 and retrying...")
                    continue  # Retry step 3 from the top of the loop

            if process_step(directory, current_step, threshold=0.8):
                print(f"Step {current_step} completed successfully. Moving to the next step.")
                previous_step = directory  # Remember the last successful step
                current_step += 1  # Move to the next step
            else:
                print(f"Step {current_step} failed. Attempting the previous step...")
                if previous_step and process_step(previous_step, current_step - 1, threshold=0.8):
                    print(f"Recovered by redoing the previous step: {previous_step}. Retrying step {current_step}.")
                    continue  # Retry the same step
                else:
                    print(f"Previous step also failed. Exiting script.")
                    exit(20)
        time.sleep(random.uniform(2, 3))

