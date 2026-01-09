import tkinter as tk
from tkinter import messagebox

def select_area():
    """
    Allows the user to draw a rectangle to select an area on the screen.
    Prints the top-left and bottom-right coordinates of the rectangle.
    """
    def on_mouse_down(event):
        # Record the starting coordinates
        global start_x, start_y
        start_x, start_y = event.x, event.y

    def on_mouse_drag(event):
        # Update the rectangle as the mouse is dragged
        canvas.delete("rectangle")
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tags="rectangle")

    def on_mouse_up(event):
        # Record the ending coordinates and close the selection window
        global end_x, end_y
        end_x, end_y = event.x, event.y
        root.destroy()

    # Create a full-screen transparent window
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.config(bg="black")

    # Create a canvas to draw the rectangle
    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Bind mouse events
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    # Run the Tkinter main loop
    root.mainloop()

    # Print the coordinates of the selected area
    global start_x, start_y, end_x, end_y
    if start_x > end_x:
        start_x, end_x = end_x, start_x
    if start_y > end_y:
        start_y, end_y = end_y, start_y
    messagebox.showinfo("Selected Area", f"Top-left: ({start_x}, {start_y})\nBottom-right: ({end_x}, {end_y})")
    print(f"Top-left: ({start_x}, {start_y}), Bottom-right: ({end_x}, {end_y})")

select_area()