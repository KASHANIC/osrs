from sub import click_gauss
import time

time.sleep(100)

for i in range(100):
    print(i)
    click_gauss(
        best_match=(895, 439),  # Example coordinates
        confidence=0.95,
        mean_x=0,  # Centered on the match
        stddev_x=5,  # Standard deviation for x-offset 99% (-15,15)
        mean_y=0,  # Centered on the match
        stddev_y=5   # Standard deviation for y-offset 99 (-15,15)
    )




