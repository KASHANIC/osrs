

import random
import time
import keyboard
from sub import find_best_match, click_on_best_match, click_gauss, find_color, find_closest_match, go_to_the_match, go_gauss
from testing_color import search_rgb_color_on_screen
import pyautogui

ore_color = (28, 153, 118)  # First color target
hopper_color = (92, 7, 7)  # Second color target
inv_path = r"C:\Users\SinaKashani\Desktop\python\mining\full_inventory"
mining_icon_2 = r"C:\Users\SinaKashani\Desktop\python\mining\mining_icon_2"
#longbow_path = r"C:\Users\SinaKashani\Desktop\python\cooking\rawmonk"
confidence_threshold = 0.80
max_attempts = 3  # Number of retries before reverting to the previous step
spec_directory = r"C:\Users\SinaKashani\Desktop\python\mining\special_att"
fullhopper = r"C:\Users\SinaKashani\Desktop\python\mining\hopper_full"
gorest =r"C:\Users\SinaKashani\Desktop\python\mining\go_rest"
stats_icon = r"C:\Users\SinaKashani\Desktop\python\mining\stats_icon"
mining_icon = r"C:\Users\SinaKashani\Desktop\python\mining\mining_icon"
inventory_icon = r"C:\Users\SinaKashani\Desktop\python\mining\inventory_icon"

def click_color(target_color, step_name):
    """Attempts to find and click a cclick_color(target_color, step_name)olor on screen, retrying up to max_attempts."""
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


def go_image(image_path, step_name):
    """Attempts to find and click the best-matching image, retrying up to max_attempts."""
    for attempt in range(max_attempts):
        best_match, confidence = find_best_match(image_path, confidence_threshold)
        if confidence >= confidence_threshold:
            print(f"{step_name}: Image found with {confidence:.2f} confidence. Clicking...")
            go_gauss(best_match, confidence, 0, 7, 0, 7)
            return True
        print(f"{step_name}: No image match found (Attempt {attempt+1}/{max_attempts}). Retrying...")
        time.sleep(1)
    print(f"{step_name}: Failed after {max_attempts} attempts. Going back to previous step...")
    return False


def periodic_check():

    mining_yes=r"C:\Users\SinaKashani\Desktop\python\mining\mining_yes"
    full_inventory=r"C:\Users\SinaKashani\Desktop\python\mining\full_inventory"


    print("Starting periodic check...")
    time_begin = time.time()
    count = int(input("How many times did you use the hopper? "))
    while True:
        print(f"Checking if we are performing fishing activity...")
        best_match, confidence = find_best_match(mining_yes, threshold=0.9)

        if best_match:
            print(f"Mining activity detected...")
            if random.randint(1, 300) == 1:
                print("Check xp!")
                click_image(stats_icon, "1")
                time.sleep(random.uniform(1.45, 1.92))
                go_image(mining_icon,"2")
                time.sleep(random.uniform(7.95, 11.4))
                click_image(inventory_icon, "3")
            else:
                print("...congratulations!")
        else:
            print("We are not mining? Hopper time...")
            best_match, confidence = find_best_match(full_inventory, threshold=0.97)
            if best_match:
                print("We do indeed need to use the hopper.")
                click_color(hopper_color, "step 2")
                time.sleep(random.uniform(2.95, 3.4))
                best_match, confidence = find_best_match(fullhopper, threshold=0.97)
                count = count + 1
                print(count)
                if count == 7:
                    print(((time.time() - time_begin) / 60), "min")
                    exit(1)

                if best_match:
                    print(((time.time() - time_begin) / 60), "min")
                    exit(20)
                else:
                    best_match, confidence = find_closest_match(mining_icon_2, threshold=0.8)
                    click_on_best_match(best_match, confidence, -3, 2, -3, 2)
            else:
                print("No need to hopper. Searching for a mining spot...")
                best_match, confidence = find_closest_match(spec_directory, threshold=0.80)
                click_gauss(best_match, confidence, 0, 13, 0, 10)
                best_match, confidence = find_closest_match(mining_icon_2, threshold=0.8)
                if best_match:
                    if random.random() < 0.2:
                        click_on_best_match(best_match, confidence, -7, 6, -7, 6)
                    else:
                        click_gauss(best_match, confidence, 0, 5, 0, 5)
                else:
                    print("nothing")
            click_gauss((1464, 1059), 0.95, 0, 7, 0, 7)
            best_match, confidence = find_best_match(fullhopper, threshold=0.9)
            if best_match:
                print(((time.time() - time_begin) / 60), "min")
                quit(21)
            print(((time.time() - time_begin) / 60), "min")
        time.sleep(random.uniform(3.95, 8.4))

    # # Step 1: Click first color (bank)
    # while not click_color(bank_color, "Step 1 - Click Bank"):
    #     pass
    # time.sleep(random.uniform(0.54, 0.95))
    #
    # if random.random() < 0.05:
    #     click_gauss((477, 156), 0.95, 0, 7, 0, 7)
    #
    # # Step 2: Click 'Bank All' image - double click
    # while not click_image(bankall_path, "Step 2 - Click Bank All"):
    #     while not click_color(bank_color, "Step 1 - Click Bank"):
    #         pass
    #     time.sleep(2)
    # time.sleep(random.uniform(0.2, 0.21))
    #
    # # Step 3: Click logs in bank (fixed coordinates as example)
    # start_time = time.time()
    # click_gauss((477, 156), 0.95, 0, 7, 0, 7)
    # print(f"Step 3 Execution Time: {time.time() - start_time:.4f} seconds")
    #
    # start_time = time.time()
    # click_color(range_color, "Step 4 - Click fletching location")
    # print(f"Step 4 Execution Time: {time.time() - start_time:.4f} seconds")
    #
    # time.sleep(random.uniform(1.81, 2.03))
    #
    # # Step 6: Click longbow image or press space
    # if random.random() < 0.05:
    #     click_image(longbow_path, "Step 5 - Click Longbow")
    # else:
    #     print("Step 7: No longbow image found, pressing SPACE instead.")
    #     keyboard.press_and_release('space')



periodic_check()
