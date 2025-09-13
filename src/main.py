import cv2
from detection_utils import initialize_detectors, process_frame_for_detections
from ui_utils import draw_gesture_text, draw_hand_landmarks, draw_face_detections
from gesture_handler import recognize_and_perform_action

def main():
    """Main function to run the gesture control application."""
    # --- Initialization ---
    hands_detector, face_detector = initialize_detectors()
    video_cap = cv2.VideoCapture(0)

    if not video_cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # --- Main Application Loop ---
    while True:
        ret, frame = video_cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Flip for a mirror view and convert color for MediaPipe
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # --- Detection Processing ---
        hand_results, face_results = process_frame_for_detections(frame_rgb, hands_detector, face_detector)
        
        # --- Drawing Face Detections ---
        if face_results.detections:
            draw_face_detections(frame, face_results.detections)

        # --- Gesture Recognition and Action ---
        gesture_text = ""
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                draw_hand_landmarks(frame, hand_landmarks)
                gesture_text = recognize_and_perform_action(hand_landmarks, frame)

        # --- Displaying UI ---
        frame = draw_gesture_text(frame, gesture_text)
        cv2.imshow("AI Gesture Control", frame)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # --- Cleanup ---
    video_cap.release()
    cv2.destroyAllWindows()
    print("Application closed successfully.")

if __name__ == "__main__":
    main()

