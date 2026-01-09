import random
import time
from antiban import antiban2
from sub import find_best_match, click_on_best_match, go_to_the_match

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
    1: (-2, 2, 2, 4),  # Coordinates for step 1
    2: (-16, 16, -12, 12),  # Coordinates for step 2
    3: (-14, 13, -13, 14),  # Coordinates for step 3
    4: (-3, 3, 10, 14),  # Coordinates for step 4
}

hoffsets = {
    1: (0, 1, 0, 1),  # Coordinates for step 1
    2: (-0, 4, 0, 3),  # Coordinates for step 2
    3: (-0, 4, 0, 3),  # Coordinates for step 3
    4: (0, 1, 12, 2),  # Coordinates for step 4
}



def process_step(directory_path, step, threshold=0.7, max_retries=5):
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
            click_on_best_match(best_match, confidence, a, b, c, d)
            return True
        else:
            # Log retry and add delay
            print(f"No match found in {directory_path}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(random.uniform(3, 4))

            # Execute antiban2 after a specific retry count
            if retries == 4:
                print("Triggering antiban2 for safety.")
                antiban2()

    print(f"Failed to find a match in {directory_path} after {max_retries} retries.")
    return False

def banking():
    previous_step = None
    current_step = 1
    while current_step <= len(directory_first):
        time.sleep(random.uniform(2, 3))
        directory = directory_first[current_step - 1]
        print(f"Starting step {current_step}: Searching in {directory}")

        if current_step == 2:
            # Add a significant break before the second step
            print("Pausing before the second step...")
            time.sleep(random.uniform(4, 6))  # Adjust this duration as needed

        if current_step == 3:
            time.sleep(random.uniform(1.25,1.88))
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

        if process_step(directory, current_step, threshold=0.7):
            print(f"Step {current_step} completed successfully. Moving to the next step.")
            previous_step = directory  # Remember the last successful step
            current_step += 1  # Move to the next step
        else:
            print(f"Step {current_step} failed. Attempting the previous step...")
            if previous_step and process_step(previous_step, current_step - 1, threshold=0.7):
                print(f"Recovered by redoing the previous step: {previous_step}. Retrying step {current_step}.")
                continue  # Retry the same step
            else:
                print(f"Previous step also failed. Exiting script.")
                exit(20)
    time.sleep(random.uniform(2, 3))

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

            if process_step(directory, current_step, threshold=0.7):
                print(f"Step {current_step} completed successfully. Moving to the next step.")
                previous_step = directory  # Remember the last successful step
                current_step += 1  # Move to the next step
            else:
                print(f"Step {current_step} failed. Attempting the previous step...")
                if previous_step and process_step(previous_step, current_step - 1, threshold=0.7):
                    print(f"Recovered by redoing the previous step: {previous_step}. Retrying step {current_step}.")
                    continue  # Retry the same step
                else:
                    print(f"Previous step also failed. Exiting script.")
                    exit(20)
        time.sleep(random.uniform(2, 3))
