import pyautogui
from datetime import datetime
from config import gesture_map, GESTURE_COOLDOWN, RAPID_FIRE_THRESHOLD, RAPID_FIRE_INTERVAL, rapid_fire_gestures

def handle_gesture_trigger(gesture, last_gesture, current_time, gesture_start_time, last_trigger_time, log_file):
    did_trigger = False

    if gesture == last_gesture:
        if gesture_start_time and (current_time - gesture_start_time) > RAPID_FIRE_THRESHOLD:
            if (current_time - last_trigger_time) >= RAPID_FIRE_INTERVAL and gesture in rapid_fire_gestures:
                did_trigger = True
        elif (current_time - last_trigger_time) >= GESTURE_COOLDOWN:
            did_trigger = True
    else:
        if (current_time - last_trigger_time) >= GESTURE_COOLDOWN:
            did_trigger = True
            gesture_start_time = current_time

    if did_trigger:
        key = gesture_map.get(gesture)
        if key:
            try:
                if "+" in key:
                    mod, main = key.split("+")
                    pyautogui.hotkey(mod, main)
                else:
                    pyautogui.press(key)
                tag = "(Rapid)" if (gesture == last_gesture and (current_time - gesture_start_time) > RAPID_FIRE_THRESHOLD) else ""
                log_file.write(f"{datetime.now()} - Gesture: {gesture} {tag}\n")
                log_file.flush()
            except:
                pass
        last_trigger_time = current_time

    return last_trigger_time, gesture_start_time, did_trigger
