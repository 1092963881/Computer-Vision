import cv2

cap = cv2.VideoCapture("444.mp4")#打开视频
while cap.isOpened():
    ret,fram = cap.read()#读取视频返回视频是否结束的bool值和每一帧的图像
    cv2.imshow('a',fram)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()