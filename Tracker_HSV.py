import cv2
import numpy as np


def tracker(filename):

    if isinstance(filename,str):
        file_name=cv2.imread(filename)
    else:
        file_name=filename
        

    def nothing(x):
        pass
     

    cv2.namedWindow("Trackbars")
     
    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
     
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
            x=l_h
            y=l_s
            z=l_v
            a=u_h
            b=u_s
            c=u_v
            break

    cv2.destroyAllWindows()
    return x,y,z,a,b,c


##tracker('rubix.png')
