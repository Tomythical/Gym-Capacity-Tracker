import datetime
import requests
import os
import pytesseract
import cv2
from csv import DictWriter, writer
import re

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'



def tracker():
    url = "https://covid.fortx.com/embed/1/UsAY4g-iMCongGOQAcoWFoqQDa6X8cnaoGA61obCfzDT8ogjQOO2akKoPkuWDMaclT2e00sBxYgOOLjziEct5EAIFgvPcaSMIF1HOFCE2IOQ3V798hVSmI4dqYta7x-_615lKuxr65b-GDVGpssUCrxKH-9SX6p29w05pwqvVLQijp0zhA3rajM=.png"

    save_path = '/Users/ThomasMatheickal/Projects/Gym_Tracking/Images'
    file_name = "img2.jpg"

    completeName = os.path.join(save_path, file_name)

    r = requests.get(url)
    with open(completeName, "wb") as f:
        f.write(r.content)

    img = cv2.imread(completeName)
    cropped_img = img[60:220, 80:350]

    gray=cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray,9,75,75)
    otsu_threshold,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresh = cv2.bitwise_not(thresh)

    morph_img = thresh.copy()   
    element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(5, 5))
    cv2.morphologyEx(src=thresh, op=cv2.MORPH_OPEN, kernel=element, dst=morph_img)

    text = pytesseract.image_to_string(morph_img, config ='--psm 13')
    digit = re.sub("[^0-9]", "", text)
    # print(digit)
    times = datetime.datetime.now()
    # print(percent)
    # print(times)
    with open("/Users/ThomasMatheickal/Projects/Gym_Tracking/Data/Capacity2.csv", 'a+') as output:
        csv_writer = writer(output)
        csv_writer.writerow([times ,digit])

# while True:
#     minute = ['00','10','20','30','40','50']
#     # minute = ['04','05','06','07','40','50']
#     x = time.strftime('%M')
#     if x in minute:
#         tracker()
#         time.sleep(60)
#     if time.strftime('%H:%M') == '12:04':
#         np.savetxt(f"/Users/ThomasMatheickal/Projects/Gym Tracking/Data/{time.strftime('Data:%d-%m-%y')}.dat", percent)
#         with open(f"/Users/ThomasMatheickal/Projects/Gym Tracking/Data/{time.strftime('Times:%d-%m-%y')}.txt", "w") as output:
#             output.write(str(times))
#         break

tracker()
# x = np.loadtxt(f"/Users/ThomasMatheickal/Projects/Gym_Tracking/Data/{time.strftime('%d-%m-%y')}.dat")
# print(x)


