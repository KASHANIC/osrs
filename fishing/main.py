import random
import time
from banking import process_step, banking, banking_2
from antiban import antiban, antiban2
from logoutbreak import logout
from sub import find_best_match, click_on_best_match, go_to_the_match, find_closest_match, click_gauss

save_directory = r"C:\Users\SinaKashani\Desktop\python\fishing\recordings"
directory_path_wc = r"C:\Users\SinaKashani\Desktop\python\fishing\tree"
directory_path_non_wc = r"C:\Users\SinaKashani\Desktop\python\fishing\not_wc_image"
directory_path_inv = r"C:\Users\SinaKashani\Desktop\python\fishing\inventory_check"
spec_directory = r"C:\Users\SinaKashani\Desktop\python\fishing\special_att"


def periodic_check(directory_path_wc, directory_path_non_wc, directory_path_inv, spec_directory):
    """
    Periodically check for woodcutting and act accordingly.

    :param directory_path_wc: Path to the woodcutting template directory.
    :param directory_path_non_wc: Path to the non-woodcutting template directory.
    :param directory_path_inv: Path to the inventory check template directory.
    :param threshold_wc: Confidence threshold for woodcutting image matching.
    :param threshold_non_wc: Confidence threshold for non-woodcutting image matching.
    :param threshold_inv: Confidence threshold for inventory check image matching.
    """
    print("Starting periodic check...")
    next_break_time = time.time() + random.uniform(7200, 14400)  # Random time between 2-4 hours
    print(((next_break_time - time.time())/60)/60, "hours")

    while True:
        print(f"Checking if we are performing fishing activity...")
        best_match, confidence = find_best_match(directory_path_non_wc, threshold=0.9)

        if best_match:
            print(f"Fishing activity detected...")
            if random.randint(1, 60) == 1:
                print("Check xp!")
                antiban()
            elif random.randint(1, 60) == 1:
                print("Wollahi, let's move the screen")
                antiban2(antiban2(directory_path=r"C:\Users\SinaKashani\Desktop\python\fishing\recordings"))
            elif time.time() >= next_break_time:
                print('Mashallah you played enough, time for a break dadash!')
                logout()
                next_break_time = time.time() + random.uniform(7200, 14400)  # Reset the break timer
                print(((next_break_time - time.time())/60)/60)
            else:
                print("...congratulations!")
        else:
            print("We are not fishing? Checking if we need to bank...")
            best_match, confidence = find_best_match(directory_path_inv, threshold=0.97)
            if best_match:
                print("We do indeed need to bank.")
                exit(1)
                time.sleep(random.uniform(10.11, 10.58))
            else:
                print("No need to bank. Searching for a fishing spot...")
                best_match, confidence = find_best_match(spec_directory, threshold=0.80)
                click_gauss(best_match, confidence, 0, 2, 0, 3)
                best_match, confidence = find_closest_match(directory_path_wc, threshold=0.8)
                if best_match:
                    if random.random() < 0.2:
                        click_on_best_match(best_match, confidence, -3, 2, -3, 2)
                        click_gauss((1464, 1059), 0.95, 0, 10, 0, 10)
                    else:
                        click_gauss(best_match, confidence, 0,2,0,2)
                        click_gauss((1464, 1059), 0.95, 0, 10, 0, 10)
                else:
                    exit(2)

        time.sleep(random.uniform(5.85, 20.4))


if __name__ == "__main__":
    periodic_check(directory_path_wc, directory_path_non_wc, directory_path_inv, spec_directory)
