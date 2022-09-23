import cv2
import numpy as np

def HSV_mask(img_hsv, lower):
    lower = np.array(lower)
    upper = np.array([255, 255, 255])
    return cv2.inRange(img_hsv, lower, upper)

ints = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in ints:  
    img = cv2.imread('./'+str(i)+'.jpg')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray[img_gray >= 24] = 255
    mask1 = HSV_mask(img_hsv, [0, 0, 155])[..., None].astype(np.float32)
    mask2 = HSV_mask(img_hsv, [0, 20, 0])
    masked = np.uint8((img + mask1) / (1 + mask1 / 255))
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    #gay sacale mayor a nuemro a eliminar
    gray[gray >= 24] = 255
    gray[mask2 == 0] = img_gray[mask2 == 0]
    cv2.imwrite('./'+str(i)+'.jpg', gray)

