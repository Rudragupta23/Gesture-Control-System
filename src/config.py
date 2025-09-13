import cv2

# --- MediaPipe Detection Confidence ---
HAND_MIN_DETECTION_CONFIDENCE = 0.8
HAND_MIN_TRACKING_CONFIDENCE = 0.5
FACE_MIN_DETECTION_CONFIDENCE = 0.5

# --- Gesture Cooldown ---
GESTURE_COOLDOWN_TIME = 1.5  # seconds

# --- User Interface (UI) Constants ---
# Font settings for displaying text on the screen
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1
FONT_THICKNESS = 2
TEXT_COLOR = (0, 255, 255)  # Yellow
TEXT_POSITION = (50, 50)

# --- Landmark IDs for Finger Tips ---
# For Thumb, Index, Middle, Ring, Pinky
FINGER_TIP_IDS = [4, 8, 12, 16, 20]

