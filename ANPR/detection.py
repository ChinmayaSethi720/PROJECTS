import cv2
import pytesseract
import os

harcascade = "model/haarcascade_russian_plate_number.xml"

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract installation path

cap = cv2.VideoCapture(0)
cap.set(3, 900)  # width
cap.set(4, 500)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img_roi = img[y: y + h, x:x + w]

            # Save the full image
            cv2.imwrite("plates/full_img_" + str(count) + ".jpg", img)

            # Process the saved full image to detect ROI
            img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
            roi_plates = plate_cascade.detectMultiScale(img_roi_gray, 1.1, 4)

            for (roi_x, roi_y, roi_w, roi_h) in roi_plates:
                roi_area = roi_w * roi_h

                if roi_area > min_area:
                    roi = img_roi[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]
                    cv2.imshow("ROI", roi)

                    # Save the ROI
                    cv2.imwrite("plates/scanned_roi_" + str(count) + ".jpg", roi)

            count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
