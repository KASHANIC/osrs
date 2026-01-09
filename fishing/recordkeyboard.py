import keyboard
import os
import pickle
from datetime import datetime
import time

# Set the directory to save recordings
save_directory = r"C:\Users\SinaKashani\Desktop\python\fishing\left_rec"

# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    print(f"Directory created: {save_directory}")

print("The recording will start in 3 seconds")
time.sleep(1)
print("The recording will start in 2 seconds")
time.sleep(1)
print("...1 second")
time.sleep(1)
print("START!")

# List to store recorded events
events = []

def record_arrow_keys(event):
    """Capture arrow key presses and releases."""
    if event.name in ["up", "down", "left", "right"]:  # Filter only arrow keys
        print(f"Recorded: {event.name} ({event.event_type})")  # Debugging
        events.append(event)

# Start recording arrow key events
keyboard.hook(record_arrow_keys)
print("Recording started. Press 'a' to stop recording.")

# Wait for 'a' key press to stop the recording
keyboard.wait("a")
keyboard.unhook(record_arrow_keys)  # Stop recording
print("Recording stopped.")

# Save the recorded events to a file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"recording_{timestamp}.pkl"
file_path = os.path.join(save_directory, file_name)

with open(file_path, "wb") as f:
    pickle.dump(events, f)

print(f"Recording saved to: {file_path}")