import cv2
import mediapipe
import pyautogui
#Step 1 : Capture video by assigning cv2.method and initializing it to 0 to capture from start
#Step 2 : detect hand, first import mediapipe
#Step 3 : distinguish the pointer finger by determining its landmark indexes, landmark indexes start from 0 of palm, there are 21 landmark indexes in a hand in total
#Step 4 : Move mouse pointer using finger
#Step 5 : Make the mouse functional
cap = cv2.VideoCapture(0)
hand_detector = mediapipe.solutions.hands.Hands()
drawing_utils = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
#Run the video continuously using a while loop
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(57, 255, 20))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(57, 255, 20))
                    thumb_x = screen_width / frame_width*x
                    thumb_y = screen_height / frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('AI Mouse', frame)
    cv2.waitKey(1)






















