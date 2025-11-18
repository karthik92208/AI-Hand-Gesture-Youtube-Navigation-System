# AI-Hand-Gesture-Youtube-Navigation-System

An intelligent, real-time hand-gesture recognition system that lets you control YouTube using simple gestures — no keyboard, no mouse, just vibes + machine learning.
This project uses MediaPipe, OpenCV, and PyAutoGUI to track your hand, detect gestures, and trigger YouTube actions like play, pause, volume control, mute, fullscreen, skip, and more.
Designed for speed, accuracy, and smooth usability — with gesture cooldowns, rapid-fire logic, distance validation, FPS tracking, a bounding box overlay, gesture logs, and modular architecture.

🚀 Features

🔹 Real-Time Gesture Recognition
- Tracks only one hand — the first detected hand.
- Built using MediaPipe Hands for reliable landmark extraction.

🔹 Gesture-Controlled YouTube Actions
Supports:
1. Play
2. Pause
3. Mute (Five-fingers 🖐️)
4. Volume Up / Down
5. Skip Forward / Backward
6. Fullscreen / Exit Fullscreen
7. Next Video / Previous Video
8. Toggle Captions
All mapped through a clean gesture → key press system.

🔹 Smart Trigger Logic
- 1.5-sec delay before a gesture fires.
- Rapid-fire mode after holding volume/skip gestures for 4+ seconds.
- Prevents double triggers or accidental spam.
- Seamlessly switches actions without delay.

🔹 Performance Enhancements
- FPS display
- Bounding box drawn around detected hand
- Tracks optimal hand distance (warns if too far)
- Landmark drawing for visual debugging

🔹 Logging
Every triggered gesture (with timestamp & rapid-fire tags) is saved in:
"gesture_log.txt"

🧠 Project Architecture

AI-Hand-Gesture-YouTube-Navigation/
│── config.py              # All configuration, cooldowns, rapid-fire, key mappings
│── gesture_detector.py    # Detects gestures from MediaPipe landmarks
│── gesture_handler.py     # Applies cooldown, rapid-fire, triggers key events
│── utilities.py           # MediaPipe & CV utilities setup
│── main.py                # Main video loop, FPS, bounding box, gesture pipeline
│── gesture_log.txt        # Auto-generated gesture log file

🎯 How It Works (Flow)

1. Camera captures frame
2. Frame → MediaPipe → extract 21 hand landmarks
3. Landmarks → gesture_detector.py
4. Detected gesture → gesture_handler.py
5. Handler checks:
   - Is it same gesture?
   - Has cooldown passed?
   - Did we cross rapid-fire threshold?
6. If allowed → triggers mapped hotkey
7. Logs the gesture
8. UI overlays bounding box + gesture name + FPS

✋ Gestures List :

To know about the gestures and detailed user guide please refer to the "Gestures.md" file.

🛠️ Tech Stack used :

Python
OpenCV
MediaPipe
PyAutoGUI
Time & Datetime modules

💻 How to Run

1. Install Dependencies
"pip install opencv-python mediapipe pyautogui"

2. Run the App
"python main.py"

3. Controls
- Ensure YouTube tab is active.
- Keep your hand within the camera’s detection box.
- Perform gestures smoothly for best results.

🌈 Future Enhancements

- Modern GUI with live preview, logs viewer, and gesture icons
- Customizable gesture sensitivity & cooldown settings
- User-defined gesture-to-key bindings
- Cross-platform support
- Better distance estimation via depth-based logic

📝 Author

Built with patience, late-night caffeine, and stubborn passion ✨
Created by Karthik, 2025.

⭐ Support

If this project helped you or inspired you, drop a ⭐ on the repo — it keeps the grind alive.
