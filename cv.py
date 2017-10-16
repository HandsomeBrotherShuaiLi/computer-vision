import cv2
import numpy as np
import time
cap=cv2.VideoCapture(0)
while(1):
    s,frame = cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l=np.array([110,50,50])
    u=np.array([130,255,255])
    mask=cv2.inRange(hsv,l,u)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k=cv2.waitKey(10)
    #按z退出
    if(k == ord("z")):
        break




# import time
# time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数
# i=0
# while i<100000000:
#     i+=1
# time_end=time.time()#time.time()为1970.1.1到当前时间的毫秒数
# print(time_end-time_start)
# print ("s")












