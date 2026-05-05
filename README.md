# ⛶ Face Recognition System
## 📄 Description
This project is a Python-based **Face Recognition system** designed to collect, store, and process facial data for identification purposes. It uses OpenCV for capturing real-time video feeds and face_recognition for processing facial encodings.     

---

## 🚀 Features
- **Real-time Capture**: Uses webcam input to detect and crop face images.

- **Data Collection**: Automatically saves processed facial data for model training.

- **Persistence**: Uses pickle to store names and face data efficiently.

- **Scalable**: Designed to handle multiple face entries.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- **Python** 3.12+

- **CMake**: Required for compiling dlib.

- **Visual Studio Build Tools**: (If you are on Windows) Ensure the "Desktop development with C++" workload is installed.

---

## 📦 Installation
#### Clone the repository: 
```bash
git clone https://github.com/Bruhrk42/Face_Recognition.git
cd Face_Recognition
```
#### Install the required dependencies:
```bash
pip install opencv-python numpy face_recognition
```
 **Note** : If you encounter issues installing dlib on Windows, it is recommended to install a pre-compiled 
 wheel for your specific Python version.

--- 
 
## ⚙️ How to Use
#### Run the script:
```bash
python final.py
```
#### Enter your name: 
When prompted, provide your name. The system will then open your webcam to capture 100 frames of your face.

#### Data Storage:
The script will automatically create a data/ directory to store your names.pkl and faces_data.pkl files.

--- 

## 📁 Project Structure
#### final.py
- The main script for capturing and processing facial data.
#### haarcascade_frontalface_default.xml
- The pre-trained classifier used for face detection.
#### data/
- Stores the generated .pkl files (created upon first run).

---

## ⚠️ Troubleshooting

#### ModuleNotFoundError
- Ensure your VS Code interpreter is set to the same environment where you installed the dependencies.
#### FileNotFoundError
- Verify that your image paths are correct and use raw strings (r"path") in your code if you are using full Windows file paths.
#### Invalid Escape Sequence
- Always use r"C:\path\to\file" when handling Windows directory strings.
