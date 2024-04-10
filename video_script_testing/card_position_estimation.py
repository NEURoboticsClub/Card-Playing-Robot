import cv2
import numpy as np

# Function to calculate distance based on card size
def calculate_distance(known_width, known_height, per_width, per_height):
    focal_length = per_width  / known_width
    distance = (known_width * focal_length) / per_width
    return distance

# Constants for card size and known distance
known_width = 5.5  # Width of the playing card in centimeters
known_height = 8.6  # Height of the playing card in centimeters
known_ratio = known_width/known_height

# Function to detect cards in the frame
def detect_cards(frame):

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the frame
    frame_contours = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    # Loop through detected contours
    for contour in contours:
        # # Approximate the contour to a polygon
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if len(approx) == 4:
            # Compute the bounding box of the contour
            (x, y, w, h) = cv2.boundingRect(contour)

            # Calculate the aspect ratio of the bounding box
            if w > h:
                aspect_ratio = float(h) / float(w)
            else:
                aspect_ratio = float(w) / float(h)
            
            # If aspect ratio is within a certain range (to filter out non-card shapes)
            if aspect_ratio > (known_ratio-0.25) and aspect_ratio < (known_ratio+0.25):
                # Draw bounding box around the card
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                
                # Calculate the distance to the card
                distance = calculate_distance(known_width, known_height, w, h)

                # Display distance on the frame
                cv2.putText(frame, f" {approx} sides", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    return frame

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        break
    
    # Detect cards in the frame
    detected_frame = detect_cards(frame)
    
    # Display the resulting frame
    cv2.imshow('Card Detection', detected_frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
