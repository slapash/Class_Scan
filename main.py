import cv2
import numpy as np
from pyzbar.pyzbar import decode
from collections import Counter

# Initialize the counter for the QR codes
qr_counter = Counter()

# Initialize a set to store seen QR codes
seen_qr_codes = set()

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the video feed
    ret, frame = cap.read()
    
    # Process the video feed
    for barcode in decode(frame):
        # Get the QR code data
        data = barcode.data.decode('utf-8')
        
        # Check if the QR code contains "HCA1" or "HCA2"
        if "HCA1" in data or "HCA2" in data:
            # If this specific ID hasn't been seen before, update the counter
            if data not in seen_qr_codes:
                seen_qr_codes.add(data)
                if "HCA1" in data:
                    qr_counter.update(["HCA1"])
                else:
                    qr_counter.update(["HCA2"])
            
            # Draw the bounding box
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)

    # Display the count for HCA1 and HCA2
    text_y_pos = 50
    for key in ["HCA1", "HCA2"]:
        count = qr_counter[key]
        cv2.putText(frame, f'{key}: {count}', (50, text_y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        text_y_pos += 40  # Increment the y-position for the next text
    
    # Display the video feed
    cv2.imshow('QR Code Scanner', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
