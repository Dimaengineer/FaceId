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

## Images
- **Registration** <img width="1044" alt="Screenshot 2024-08-18 at 22 19 01" src="https://github.com/user-attachments/assets/aae7e270-d7a2-4149-a7fd-64e9c8971693">

- **Detection** ![Screenshot 2024-08-18 at 22 19 24-2-2](https://github.com/user-attachments/assets/57ad43a4-e518-4cc2-a24e-8f31c1587d6f)


---
