import random
import time
import keyboard
from sub import find_best_match, click_on_best_match, click_gauss, find_color
from testing_color import search_rgb_color_on_screen
import pyautogui

def banking():
    bank_color = (28, 153, 118)  # First color target
    range_color = (92, 7, 7)  # Second color target
    bankall_path = r"C:\Users\SinaKashani\Desktop\python\cooking\bankall"
    closebank_path = r"C:\Users\SinaKashani\Desktop\python\cooking\closebank"
    longbow_path = r"C:\Users\SinaKashani\Desktop\python\cooking\rawmonk"
    confidence_threshold = 0.80
    max_attempts = 3  # Number of retries before reverting to the previous step

    def click_color(target_color, step_name):
        """Attempts to find and click a color on screen, retrying up to max_attempts."""
        for attempt in range(max_attempts):
            matches = search_rgb_color_on_screen(target_color, tolerance=5)
            if matches:
                x, y = random.choice(matches)
                print(f"{step_name}: Match found. Clicking at ({x}, {y})")
                click_gauss((x, y), 1.0, 0, 0, 0, 0)
                return True
            print(f"{step_name}: No match found (Attempt {attempt+1}/{max_attempts}). Retrying...")
            time.sleep(1)
        print(f"{step_name}: Failed after {max_attempts} attempts. Going back to previous step...")
        return False

    def click_image(image_path, step_name):
        """Attempts to find and click the best-matching image, retrying up to max_attempts."""
        for attempt in range(max_attempts):
            best_match, confidence = find_best_match(image_path, confidence_threshold)
            if confidence >= confidence_threshold:
                print(f"{step_name}: Image found with {confidence:.2f} confidence. Clicking...")
                click_gauss(best_match, confidence, 0, 7, 0, 7)
                return True
            print(f"{step_name}: No image match found (Attempt {attempt+1}/{max_attempts}). Retrying...")
            time.sleep(1)
        print(f"{step_name}: Failed after {max_attempts} attempts. Going back to previous step...")
        return False


    # Step 1: Click first color (bank)
    while not click_color(bank_color, "Step 1 - Click Bank"):
        pass
    time.sleep(random.uniform(0.54, 0.95))

    if random.random() < 0.05:
        click_gauss((477, 156), 0.95, 0, 7, 0, 7)

    # Step 2: Click 'Bank All' image - double click
    while not click_image(bankall_path, "Step 2 - Click Bank All"):
        while not click_color(bank_color, "Step 1 - Click Bank"):
            pass
        time.sleep(2)
    time.sleep(random.uniform(0.2, 0.21))



    # Step 3: Click logs in bank (fixed coordinates as example)
    start_time = time.time()
    click_gauss((477, 156), 0.95, 0, 7, 0, 7)

    print(f"Step 3 Execution Time: {time.time() - start_time:.4f} seconds")
    if random.random() < 0.04:
        click_gauss((478, 155), 0.95, 0, 11, 0, 11)

    start_time = time.time()
    click_color(range_color, "Step 4 - Click fletching location")
    print(f"Step 4 Execution Time: {time.time() - start_time:.4f} seconds")

    time.sleep(random.uniform(1.93, 2.03))

    # Step 6: Click longbow image or press space
    if random.random() < 0.05:
        click_image(longbow_path, "Step 5 - Click Longbow")
    else:
        print("Step 7: No longbow image found, pressing SPACE instead.")
        keyboard.press_and_release('space')

    click_gauss((1464, 1059), 0.95, 0, 7, 0, 7)



while True:
    print("Starting to fletch...")
    banking()
    sleepy_time = random.uniform(66.4, 69.4)
    print(f"Sleeping for {sleepy_time:.2f} seconds...")
    time.sleep(sleepy_time)