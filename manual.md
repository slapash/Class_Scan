# QR Code Scanner

This application is designed to scan QR codes in real-time using a webcam. It is capable of identifying two specific QR codes: 'hca1' and 'hca2', representing choices 1 and 2 respectively. The live camera feed is displayed, with bounding boxes highlighting the detected QR codes. The application also keeps a count of the number of times each QR code is scanned. The count for 'hca1' is displayed on the right side of the screen and the count for 'hca2' on the left.

## Quick Install

Before running the application, you need to install the required Python libraries. You can do this by running the following command in your terminal:

```
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```
opencv-python==4.5.3.56
numpy==1.21.2
pyzbar==0.1.8
```

## How to Use

To start the application, run the `main.py` script. This will initialize the webcam and start processing the video feed. The application will display the live camera feed and highlight any detected QR codes with a bounding box.

The count for each QR code is displayed next to the bounding box. The count for 'hca1' is displayed on the right side of the screen and the count for 'hca2' on the left.

To stop the application, press the 'q' key.

## Troubleshooting

If you encounter any issues while using the application, please check the following:

- Make sure your webcam is properly connected and working.
- Ensure that the required Python libraries are correctly installed.
- If the application is not correctly identifying the QR codes, make sure the QR codes are not damaged or obscured.

## Feedback and Support

We value your feedback and are here to help if you encounter any issues. Please contact us at support@chatdev.com for any questions or concerns.