import  cv2
import numpy as np
import f2
#import gui
########################################################

path1="img1.jpg"
path2="img2.jpg"
path3="img3.jpg"
path4="img4.jpg"
path5="IMG20230724200337.jpg"
path6="IMG20230724200412.jpg"
w=720
h=720
clickpoints=[]

#path=str(input("ENTER PATH"))
#dans,cm,wm=f2.askanskey()
#dans={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1,17:1,18:1,19:1,20:1,21:1,22:1,23:1,24:1,25:1,26:1,27:1,28:1,29:1,30:1,31:1,32:1,33:1,34:1,35:1,36:1,37:1,38:1,39:1,40:1,41:1,42:1,43:1,44:1,45:1}
#f2.showall(l2)
########################################################
def crop():
    w, h = 720, 720
    points1 = np.array([clickpoints[0], clickpoints[1], clickpoints[2], clickpoints[3]], dtype="float32")
    points2 = np.array([clickpoints[4], clickpoints[5], clickpoints[6], clickpoints[7]], dtype="float32")
    points3 = np.array([clickpoints[8], clickpoints[9], clickpoints[10], clickpoints[11]], dtype="float32")
    pointsf = np.array([[0, 0], [w, 0], [0, h], [w, h]], dtype="float32")
    pers1 = cv2.getPerspectiveTransform(points1, pointsf)
    pers2 = cv2.getPerspectiveTransform(points2, pointsf)
    pers3 = cv2.getPerspectiveTransform(points3, pointsf)

    imgcrop1 = cv2.warpPerspective(imgtresh, pers1, (w, h))
    imgcrop2 = cv2.warpPerspective(imgtresh, pers2, (w, h))
    imgcrop3 = cv2.warpPerspective(imgtresh, pers3, (w, h))
    #cv2.imshow("croppedimage1",imgcrop1)
    #cv2.imshow("croppedimage2", imgcrop2)
    #cv2.imshow("croppedimage3", imgcrop3)
    parts = np.vstack((imgcrop1, imgcrop2, imgcrop3))


    l = f2.imgsplit(parts)


    print(l[2])
    d = f2.corrector(dans, l[2])
    print("marks:",d["marks"])


def click(event, x, y, flags, param):

    global clickpoints

    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        clickpoints.append([x, y])


        if len(clickpoints) == 12:
            crop()



"""img = cv2.imread(gui.root.filename)
img = cv2.resize(img, (w, h))
cv2.imshow("Mywindow", img)


imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgtresh = cv2.threshold(imggray, 100, 255, cv2.THRESH_BINARY_INV)[1]

cv2.setMouseCallback("Mywindow", click)

# f2.showall(l2)
cv2.waitKey(0)"""

