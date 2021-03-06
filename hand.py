import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            print("Couldn't access camera")
            break

        results = hands.process(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                     frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
        cv2.imshow("Hands", frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows() 
