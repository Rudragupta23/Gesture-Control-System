import cv2
from config import FONT, FONT_SCALE, FONT_THICKNESS, TEXT_COLOR, TEXT_POSITION
from detection_utils import mp_draw, mp_hands

def draw_gesture_text(frame, text):
    """Draws the recognized gesture text onto the frame."""
    if text:
        cv2.putText(frame, text, TEXT_POSITION, FONT, FONT_SCALE, TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)
    return frame

def draw_hand_landmarks(frame, hand_landmarks):
    """Draws the hand skeleton on the frame."""
    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

def draw_face_detections(frame, detections):
    """Draws bounding boxes for detected faces."""
    if detections:
        for detection in detections:
            mp_draw.draw_detection(frame, detection)

