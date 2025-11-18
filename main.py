import cv2
import time
from utilities import hands, mp_drawing, mp_hands
from gesture_detector import detect_gesture
from gesture_handler import handle_gesture_trigger

# ---------------- Main ---------------- #
cap = cv2.VideoCapture(0)
p_time = 0
last_gesture = None
last_trigger_time = 0
gesture_start_time = None

log_file = open("gesture_log.txt", "a")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture_name = "Waiting..."

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        x_vals = [int(lm.x * w) for lm in hand_landmarks.landmark]
        y_vals = [int(lm.y * h) for lm in hand_landmarks.landmark]
        xmin, xmax = min(x_vals), max(x_vals)
        ymin, ymax = min(y_vals), max(y_vals)
        cv2.rectangle(frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

        if (xmax - xmin) < 80 or (ymax - ymin) < 80:
            cv2.putText(frame, "Hand too far", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        else:
            gesture_name = detect_gesture(hand_landmarks.landmark)
            current_time = time.time()

            if gesture_name:
                last_trigger_time, gesture_start_time, did_trigger = handle_gesture_trigger(
                    gesture_name, last_gesture, current_time, gesture_start_time, last_trigger_time, log_file
                )
                if did_trigger:
                    last_gesture = gesture_name

    if gesture_name:
        cv2.putText(frame, f'Gesture: {gesture_name}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    c_time = time.time()
    fps = 1 / (c_time - p_time) if c_time != p_time else 0
    p_time = c_time
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.imshow("AI Hand Gesture YouTube Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

log_file.close()
cap.release()
cv2.destroyAllWindows()
