import cv2
import pyautogui
import time
from datetime import datetime
from config import FINGER_TIP_IDS, GESTURE_COOLDOWN_TIME

# --- State for Cooldown ---
last_gesture_time = 0

def recognize_and_perform_action(hand_landmarks, frame):
    """
    Recognizes a gesture from hand landmarks and performs the associated action.
    Returns the name of the gesture detected.
    """
    global last_gesture_time
    gesture_text = ""
    
    try:
        landmarks = hand_landmarks.landmark
        fingers_up = []

        # Check Thumb
        if landmarks[FINGER_TIP_IDS[0]].x < landmarks[FINGER_TIP_IDS[0] - 1].x:
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Check other four fingers
        for i in range(1, 5):
            if landmarks[FINGER_TIP_IDS[i]].y < landmarks[FINGER_TIP_IDS[i] - 2].y:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

        # Cooldown check
        current_time = time.time()
        if current_time - last_gesture_time > GESTURE_COOLDOWN_TIME:
            
            # Thumbs Up: Increase Volume
            if fingers_up == [1, 0, 0, 0, 0]:
                gesture_text = "Volume Up"
                pyautogui.press('volumeup')
                last_gesture_time = current_time

            # Open Palm: Decrease Volume
            elif fingers_up == [1, 1, 1, 1, 1]:
                gesture_text = "Volume Down"
                pyautogui.press('volumedown')
                last_gesture_time = current_time

            # Fist: Play/Pause Media
            elif sum(fingers_up) == 0:
                gesture_text = "Play/Pause"
                pyautogui.press('playpause')
                last_gesture_time = current_time
                
            # Peace Sign: Take a Photo
            elif fingers_up == [0, 1, 1, 0, 0]:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"photo_{timestamp}.jpg"
                cv2.imwrite(filename, cv2.flip(frame, 1)) 
                gesture_text = "Photo Saved!"
                last_gesture_time = current_time

            # Pinky Up: Take Screenshot
            elif fingers_up == [0, 0, 0, 0, 1]:
                gesture_text = "Screenshot!"
                pyautogui.screenshot(f"screenshot_{int(time.time())}.png")
                last_gesture_time = current_time
            
            # Pointing Up: Left Mouse Click
            elif fingers_up == [0, 1, 0, 0, 0]:
                gesture_text = "Mouse Click!"
                pyautogui.click()
                last_gesture_time = current_time

    except Exception as e:
        print(f"Error in gesture recognition: {e}")
        pass

    return gesture_text

