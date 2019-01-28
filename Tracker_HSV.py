import cv2
import numpy as np


def tracker(filename):

    if isinstance(filename,str):
        file_name=cv2.imread(filename)
    else:
        file_name=filename
        


    def Null_Value(x):
        return None

    cv2.namedWindow("Trackbars")
     
    cv2.createTrackbar("L - H", "Trackbars", 0, 179, Null_Value)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, Null_Value)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, Null_Value)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, Null_Value)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, Null_Value)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, Null_Value)
     
    while True:
        
        hsv = cv2.cvtColor(file_name, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])
        mask = cv2.inRange(hsv, lower, upper)
        

        result = cv2.bitwise_and(file_name, file_name, mask=mask)

        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame',(500,500))
        cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('mask',(500,500))
        cv2.namedWindow('result',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('result',(500,500))
        cv2.imshow("frame", file_name)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)
        key=cv2.waitKey(1)
        if key==27:
            lower_hue=l_h
            lower_sat=l_s
            lower_val=l_v
            upper_hue=u_h
            upper_sat=u_s
            upper_val=u_v
            break

    cv2.destroyAllWindows()
    return lower_hue,lower_sat,lower_val,upper_hue,upper_sat,upper_val


def help():
    print(""" For more information please visit
py2py: https://py2py.com/Tracker-for-HSV-model-Overview-and-Explanation
Github: https://github.com/Pushkar-Singh-14/Tracker_HSV
PyPI: https://pypi.org/project/Tracker-HSV/

""")
