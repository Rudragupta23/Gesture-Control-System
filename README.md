# AI Gesture Control System ✨

An advanced Python application that transforms your webcam into a futuristic gesture-based remote control for your computer. Control volume, media, mouse clicks, and more, all with simple hand signs. Built with OpenCV and Google's MediaPipe.


## Features 🚀

-   **Volume Control**: Raise a thumbs-up to increase volume or show an open palm to decrease it.
-   **Media Control**: Make a fist to instantly play or pause your video or music.
-   **Mouse Control**: Point your index finger to perform a left mouse click.
-   **Take Photos**: Show a peace sign to capture and save a photo from your webcam
-   **Capture Your Screen:**: Show a pinky finger to take a screenshot of your entire display.
-   **Real-time Detection**: Smooth and responsive face and hand tracking.

| Gesture | Action |
| :--- | :--- |
| 👍 Thumbs Up | Volume Up |
| 🖐️ Open Palm | Volume Down |
| ✊ Fist | Play / Pause Media |
| ✌️ Peace Sign | Take a Photo |
| 🤙 Pinky Up | Take Screenshot |
| ☝️ Pointing Up | Left Mouse Click |

## Project Structure 📂

The project is organized into logical modules for better readability and maintenance.

```
Gesture-Control-System
├── src/
│   ├── main.py             
│   ├── config.py         
│   ├── detection_utils.py  
│   ├── gesture_handler.py  
│   └── ui_utils.py
├── requirements.txt        
└── README.md               
```

## Installation ⚙️

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Rudragupta23/Gesture-Control-System.git](https://github.com/Rudragupta23/Gesture-Control-System.git)
    cd GestureControlProject
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage ▶️

To run the application, make sure you are inside the src directory, then execute the main.py script:

```bash
python main.py
```

-   Press the **'q'** key to close the application window.