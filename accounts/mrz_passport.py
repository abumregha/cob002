import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\Tesseract'
import numpy as np
import imutils


def test_call(img_path):
    print(img_path)


def read_passport_mrz(img_path):
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,5))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(21,21))
    img = cv2.imread(img_path)
    width,height = 600,400
    imgResize = cv2.resize(img, (width, height))
    imgCrop = imgResize[200:400,0:600]
    gray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    thresh = cv2.erode(thresh, None, iterations=4)
    # p = int(imgCrop.shape[1] * 0.0001)
    # thresh[:, 0:p] = 0
    # thresh[:, imgCrop.shape[1] - p:] = 0
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and use the contour to
        # compute the aspect ratio and coverage ratio of the bounding box
        # width to the width of the image
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        crWidth = w / float(gray.shape[1])
        # check to see if the aspect ratio and coverage width are within
        # acceptable criteria
        if ar > 5 and crWidth > 0.75:
            # pad the bounding box since we applied erosions and now need
            # to re-grow it
            pX = int((x + w) * 0.06)
            pY = int((y + h) * 0.06)
            (x, y) = (x - pX, y - pY)
            (w, h) = (w + (pX * 2), h + (pY * 2))
            # extract the ROI from the image and draw a bounding box
            # surrounding the MRZ
            roi = imgCrop[y:y + h, x:x + w].copy()
            cv2.rectangle(imgCrop, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break
    roi2 = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
    passport_data = pytesseract.image_to_string(roi)
    print(passport_data)
    split_Ppassport_data = [x.strip() for x in passport_data.split('<')]
    while ("" in split_Ppassport_data):
        split_Ppassport_data.remove("")
    print(split_Ppassport_data)
    print('Passport mrz fields: ' + len(split_Ppassport_data))
    print('Passport Number: ' + split_Ppassport_data[5])
    # show the output images
    # cv2.imshow("Image", imgResize)
    # cv2.imshow("ROI", roi)
    # cv2.waitKey(0)

