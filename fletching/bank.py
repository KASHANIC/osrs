import random
import time
import keyboard
from sub import find_best_match, click_on_best_match, click_gauss, find_color, click_gauss_bot
from testing_color import search_rgb_color_on_screen

def banking():
    bank_color = (28, 153, 118)  # First color target
    tree_color = (105, 60, 104)  # Second color target
    bankall_path = r"C:\Users\SinaKashani\Desktop\python\fletching\bankall"
    closebank_path = r"C:\Users\SinaKashani\Desktop\python\fletching\closebank"
    longbow_path = r"C:\Users\SinaKashani\Desktop\python\fletching\longbow"
    confidence_threshold = 0.80
    max_attempts = 3  # Number of retries before reverting to the previous step

    def click_color(target_color, step_name):
        """Attempts to find and click a color on screen, retrying up to max_attempts."""
        for attempt in range(max_attempts):
            matches = search_rgb_color_on_screen(target_color, tolerance=5)
            if matches:
                x, y = random.choice(matches)
                print(f"{step_name}: Match found. Clicking at ({x}, {y})")
                click_gauss((x, y), 1.0, 0, 1, 0, 1)
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

    def click_image_bot(image_path, step_name):
        """Attempts to find and click the best-matching image, retrying up to max_attempts."""
        for attempt in range(max_attempts):
            best_match, confidence = find_best_match(image_path, confidence_threshold)
            if confidence >= confidence_threshold:
                print(f"{step_name}: Image found with {confidence:.2f} confidence. Clicking...")
                click_gauss_bot(best_match, confidence, 0, 7, 0, 7)
                return True
            print(f"{step_name}: No image match found (Attempt {attempt+1}/{max_attempts}). Retrying...")
            time.sleep(1)
        print(f"{step_name}: Failed after {max_attempts} attempts. Going back to previous step...")
        return False



    # Step 1: Click first color (bank)
    while not click_color(bank_color, "Step 1 - Click Bank"):
        pass
    time.sleep(random.uniform(0.54, 0.87))

    # Step 2: Click 'Bank All' image
    while not click_image(bankall_path, "Step 2 - Click Bank All"):
        while not click_color(bank_color, "Step 1 - Click Bank"):
            pass
        time.sleep(2)
    time.sleep(random.uniform(0.4, 1.7))

    # Step 3: Click logs in bank (fixed coordinates as example)
    click_gauss((477, 156), 0.95, 0, 7, 0, 7)
    time.sleep(random.uniform(0.6, 1.7))

    # Step 4: Close bank (either by clicking image or pressing ESC)
    if random.random() < 0.01:
        click_image(closebank_path, "Step 4 - Close Bank")
    else:
        print("Step 4: No close button found, pressing ESC instead.")
        keyboard.press_and_release('esc')
    time.sleep(random.uniform(0.7, 1.3))

    # Step 5: Click fletching location
    click_gauss((1387, 648), 0.95, 0, 5, 0, 5)
    time.sleep(random.uniform(0.1, 0.5))

    # Step 6: Click the correct fletching button with a randomized choice
    if random.random() < 0.31:
        click_gauss_bot((1447, 647), 0.95, 0, 5, 0, 7)
    else:
        click_gauss_bot((1387, 699), 0.95, 0, 7, 0, 6)
    time.sleep(random.uniform(0.59, 0.91))

    # Step 7: Click longbow image or press space
    if random.random() < 0.09:
        click_image(longbow_path, "Step 7 - Click Longbow")
    else:
        print("Step 7: No longbow image found, pressing SPACE instead.")
        keyboard.press_and_release('space')

while True:
    print("Starting to fletch...")
    banking()
    sleepy_time = random.uniform(49, 55)
    print(f"Sleeping for {sleepy_time:.2f} seconds...")
    click_gauss((1464, 1059), 0.95, 0, 7, 0, 7)
    time.sleep(sleepy_time)