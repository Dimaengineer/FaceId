---

# Face Recognition Attendance System

This project is a simple face recognition-based attendance system. It uses Python's `face_recognition` and `OpenCV` libraries to detect faces in real-time via a webcam, match them with pre-stored images, and mark attendance by recording the time of detection.

## Features
- **Face Detection & Recognition:** Identifies faces using a webcam and matches them against a dataset of known individuals.
- **Attendance Logging:** Automatically logs the attendance with the timestamp of recognition.
- **Dynamic Dataset Update:** Easily add new individuals to the dataset during runtime.

## How It Works
1. **Load Dataset:** The program loads images from the `dataset` folder. Each image file should be named in the format `NameType.jpg` (e.g., `JohnDoe_seller.jpg` or `JaneDoe_buyer.jpg`).
2. **Real-Time Recognition:** The webcam captures live video, detecting and recognizing faces from the dataset.
3. **Mark Attendance:** If a recognized face is detected, the system logs the name and timestamp in `Attendance.csv`.

## Project Structure
- **dataset/**: Contains the images used for face recognition.
- **Attendance.csv**: The file where attendance records are stored.

## Installation
1. **Clone the repository:**
   ```bash
   [git clone https://github.com/yourusername/face-recognition-attendance.git](https://github.com/Dimaengineer/FaceId.git)
   ```
2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python FaceId.py
   ```

## Screenshots
1. **Face Detection in Action:**
<img width="1044" alt="Screenshot 2024-08-18 at 22 19 01" src="https://github.com/user-attachments/assets/e30634e3-dfd1-4194-8ffe-eccf54db8151">
<img width="1373" alt="Screenshot 2024-08-18 at 22 19 24" src="https://github.com/user-attachments/assets/ba185ff0-d531-437c-8193-ffcc6e003214">


## Requirements
- Python 3.x
- `face_recognition`
- `OpenCV`
- `Numpy`

## Future Enhancements
- Implement a GUI for easier management.
- Support for different image formats.

---
