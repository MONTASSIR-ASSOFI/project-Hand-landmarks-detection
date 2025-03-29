import cv2 as vesion
import mediapipe as media
import serial

serial_Communication = serial.Serial("COM2",9600)

camera = vesion.VideoCapture(0)

hand_solution = media.solutions.hands
hand = hand_solution.Hands()
drawing = media.solutions.drawing_utils

while True :
    return_ , frame = camera.read()

    processing = hand.process(frame)
    
    if processing.multi_hand_landmarks :
        height , width ,_ = frame.shape
        for hand_landmark in processing.multi_hand_landmarks :

            x8,y8 = int(hand_landmark.landmark[8].x *width) , int(hand_landmark.landmark[8].y*height)
            x7,y7 = int(hand_landmark.landmark[7].x *width), int(hand_landmark.landmark[7].y*height)
             if y8 < y7 :
                 message = "ON"
             elif  y8 > y7 :
                 message = "OFF"
    
                serial_Communication.write(message.encode())
                vesion.putText(frame,message,(50,50),vesion.FONT_HERSHEY_COMPLEX,3,(0,0,255)) 
              
        vesion.circle(frame,(x8,y8),2,(0,255,0))
        vesion.circle(frame,(x7,y7),2,(0,255,0))

    vesion.imshow("video" , frame)
    vesion.waitKey(1)



