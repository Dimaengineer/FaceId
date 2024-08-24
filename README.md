---

# Face Recognition Attendance System

This project is ideal for companies with many employees. It uses Python's `face_recognition` and `OpenCV` to detect faces via a webcam, match them with a stored dataset, and automatically log attendance.

## Features
- **Face Recognition:** Identifies and matches faces against a known dataset.
- **Attendance Logging:** Records attendance with a timestamp.
- **Easy Dataset Management:** Add new individuals on the fly.

## How It Works
1. **Load Dataset:** Images in the `dataset` folder are used for recognition.
2. **Real-Time Recognition:** Detects and recognizes faces in live video.
3. **Mark Attendance:** Logs recognized faces with the current time in `Attendance.csv`.

## Project Structure
- **dataset/**: Holds images for recognition.
- **Attendance.csv**: Stores attendance records.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/DmitroKDS/FaceId.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python FaceId.py
   ```

## Requirements
- Python 3.x
- `face_recognition`
- `OpenCV`
- `Numpy`

---
