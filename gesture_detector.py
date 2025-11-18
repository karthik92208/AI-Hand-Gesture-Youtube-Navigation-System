def detect_gesture(landmarks):
    fingers = []
    tip_ids = [4, 8, 12, 16, 20]

    for i in range(1, 5):
        fingers.append(1 if landmarks[tip_ids[i]].y < landmarks[tip_ids[i] - 2].y else 0)

    fingers.insert(0, 1 if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x else 0)

    if fingers == [0, 1, 0, 0, 0]: return "play"
    elif fingers == [0, 1, 0, 0, 0]: return "pause"
    elif fingers == [1, 1, 1, 1, 1]: return "mute"
    elif fingers == [1, 1, 0, 0, 0]: return "volume_up"
    elif fingers == [1, 1, 1, 0, 0]: return "volume_down"
    elif fingers == [0, 1, 0, 0, 1]: return "skip_forward"
    elif fingers == [0, 0, 0, 0, 1]: return "skip_backward"
    elif fingers == [1, 0, 0, 0, 1]: return "fullscreen"
    elif fingers == [1, 0, 0, 0, 1]: return "exit_fullscreen"
    elif fingers == [1, 1, 1, 1, 0]: return "toggle_captions"
    elif fingers == [0, 1, 1, 0, 0]: return "next_video"
    elif fingers == [0, 1, 1, 1, 0]: return "previous_video"
    else:
        return None
