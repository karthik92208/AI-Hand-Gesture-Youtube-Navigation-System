🎮 Gesture Guide — AI Hand Gesture YouTube Navigation System

This document gives a clear visual explanation of every gesture supported by the system.
Each gesture includes:
- a hand emoji symbol,
- the finger pattern detected by MediaPipe,
- and the YouTube action it triggers.
- Use this as a quick reference while testing the project.

** Supported Gestures **

1. Play / Pause -> ☝️
Pattern: [0,1,0,0,0]
Action: Toggles Play/Pause (Space bar)

2. Mute -> 🤚
Pattern: [1,1,1,1,1]
Action: Mute/Unmute (M)

3. Volume Up -> 👉  
Pattern: [1,1,0,0,0]
Action: Volume Up (Arrow Up)

4. Volume Down -> 👆🖕
Pattern: [1,1,1,0,0]
Action: Volume Down (Arrow Down)

5. Skip Forward -> 🤘
Pattern: [0,1,0,0,1]
Action: Seek Forward (Arrow Right)

6. Skip Backward -> ☝️(little finger)
Pattern: [0,0,0,0,1]
Action: Seek Backward (Arrow Left)

7. Fullscreen -> 🤙
Pattern: [1,0,0,0,1]
Action: Enter Fullscreen (F)

8. Exit Fullscreen -> 🤙
Pattern: [1,0,0,0,1]
Action: Exit Fullscreen (ESC)

9. Next Video
Symbol: ✌️
Pattern: [0,1,1,0,0]
Action: Next Video (Shift + N)

10. Previous Video️ -> ✌️☝
Pattern: [0,1,1,1,0]
Action: Previous Video (Shift + P)

11. Toggle Captions -> 🖖
Pattern: [1,1,1,1,0]
Action: Toggle Captions (C)

12. Exit -> ✊
Pattern: [0,0,0,0,0]
Action: Exit application.

📌 Notes

Keep your hand within the green bounding box for best accuracy.
Gestures activate after 1.5 seconds unless rapid-fire is triggered.
Volume and skip gestures enter rapid mode after holding for 4+ seconds.
Only one hand is tracked at a time.
