# Configuration Parameters
GESTURE_COOLDOWN = 1.5  # Delay before allowing same or new gesture
RAPID_FIRE_THRESHOLD = 4.0  # Time to activate rapid fire mode
RAPID_FIRE_INTERVAL = 0.3  # Interval between triggers in rapid fire
rapid_fire_gestures = {"volume_up", "volume_down", "skip_forward", "skip_backward"}

# Gesture to Key Mapping
gesture_map = {
    "play": "space",
    "pause": "space",
    "mute": "m",
    "volume_up": "up",
    "volume_down": "down",
    "skip_forward": "right",
    "skip_backward": "left",
    "fullscreen": "f",
    "exit_fullscreen": "esc",
    "next_video": "shift+n",
    "previous_video": "shift+p",
    "toggle_captions": "c"
}
