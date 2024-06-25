import cv2
import numpy as np
import tkinter as tk

# Get the screen size using tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Define the size of the image and stripes
height, width = screen_height, screen_width
stripe_width = width // 6

# Initialize the position and direction of the stripes
green_x = 0
blue_x = width - stripe_width
direction = 2  # Increase the step size to make it faster

# Create a window to display the image in full screen
cv2.namedWindow('Stripes Animation', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Stripes Animation', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Create an empty image
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw the green stripe
    green_stripe = np.zeros((height, width, 3), dtype=np.uint8)
    green_stripe[:, green_x:green_x + stripe_width] = [0, 255, 0]
    image = cv2.addWeighted(image, 1.0, green_stripe, 1.0, 0)

    # Draw the red stripe in the center
    red_stripe = np.zeros((height, width, 3), dtype=np.uint8)
    center_x = (width - stripe_width) // 2
    red_stripe[:, center_x:center_x + stripe_width] = [0, 0, 255]
    image = cv2.addWeighted(image, 1.0, red_stripe, 1.0, 0)

    # Draw the blue stripe
    blue_stripe = np.zeros((height, width, 3), dtype=np.uint8)
    blue_stripe[:, blue_x:blue_x + stripe_width] = [255, 0, 0]
    image = cv2.addWeighted(image, 1.0, blue_stripe, 1.0, 0)

    # Display the image
    cv2.imshow('Stripes Animation', image)

    # Update the positions of the stripes
    green_x += direction
    blue_x -= direction

    # Reverse direction if stripes reach the opposite edges
    if green_x >= width - stripe_width or green_x <= 0:
        direction = -direction

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(20) & 0xFF == ord('q'):  # Reduced delay to 20 ms
        break

# Release resources and close the window
cv2.destroyAllWindows()
