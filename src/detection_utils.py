import mediapipe as mp
from config import (HAND_MIN_DETECTION_CONFIDENCE, HAND_MIN_TRACKING_CONFIDENCE,
                        FACE_MIN_DETECTION_CONFIDENCE)

mp_hands = mp.solutions.hands
mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

def initialize_detectors():
    """Initializes and returns the MediaPipe hand and face detectors."""
    hands = mp_hands.Hands(
        min_detection_confidence=HAND_MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=HAND_MIN_TRACKING_CONFIDENCE
    )
    face_detector = mp_face_detection.FaceDetection(
        min_detection_confidence=FACE_MIN_DETECTION_CONFIDENCE
    )
    return hands, face_detector

def process_frame_for_detections(frame_rgb, hands_detector, face_detector):
    """Processes a single frame to detect hands and faces."""
    hand_results = hands_detector.process(frame_rgb)
    face_results = face_detector.process(frame_rgb)
    return hand_results, face_results

