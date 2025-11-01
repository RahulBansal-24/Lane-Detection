# 🚗 Lane Detection using OpenCV

Real-time **frame-by-frame lane detection** from road videos using **OpenCV** and **NumPy** — detects and highlights lane lines using edge detection and Hough transforms. ⚙️🎥  

---

## 📸 Overview
This project demonstrates **lane detection** on road videos using computer vision techniques.  
It processes each video frame in real time to identify and visualize lane markings.  
A simple **Tkinter file dialog** lets you select any `.mp4`, `.avi`, `.mov`, or `.mkv` file for detection.

---

## ✨ Features
- 🛣️ Detects lane lines from any road video.  
- ⚙️ Uses **Canny edge detection** and **Hough Line Transform**.  
- 🎯 Applies a **region of interest (ROI)** to focus on the road area.  
- 🪟 Simple **file selector GUI** for quick input.  
- 🕹️ Real-time visualization — press **`q`** to quit anytime.  

---

## 📂 Repository Structure
  
📦 lane-detection  
┣ 📜 lane detection.py # Main Python script  
┣ 📜 README.md # Project documentation  
┗ 📜 LICENSE # MIT License


---

## 🧠 How It Works
1. **Grayscale & Blur:** Converts frames to grayscale and applies Gaussian blur to reduce noise.  
2. **Edge Detection:** Uses the Canny algorithm to find lane edges.  
3. **ROI Masking:** Focuses only on the lower trapezoidal area (where lanes typically appear).  
4. **Line Detection:** Finds straight lane lines using the Probabilistic Hough Transform.  
5. **Overlay:** Draws detected lines back onto the original frame for clear visualization.

---

## 🧩 Tech Stack
- 🐍 **Python 3.x**
- 📷 **OpenCV**
- 🔢 **NumPy**
- 🪟 **Tkinter**

---

## ⚙️ Installation

Make sure Python is installed on your system, then install the dependencies:

```bash
pip install opencv-python numpy
```

---

## 🚀 Usage

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/lane-detection.git
cd lane-detection
```

2. Run the script:
```bash
python "lane detection.py"
```
3. Select a road video file when prompted.

4. The program will process each frame and display detected lanes in real time.

5. Press q to exit the window at any time.


---

## ⚠️ Known Limitations
- May occasionally detect **extra or incorrect lines** under poor lighting, shadows, or rainy conditions.  
- Optimized primarily for **daytime driving videos** with clear lane markings.  
- Does not currently handle **curved lanes** or **complex multi-lane highways** accurately.

---

## 🧭 Future Improvements
- 🎨 Add **color-based filtering** to improve accuracy under varying light conditions.  
- 🧮 Implement **curve fitting** for smoother lane tracking.  
- 🧠 Explore **deep learning-based segmentation models** for more robust detection.  
- 🎥 Add support for **live camera input** to make it truly real-time.

---

## 🪪 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project with proper attribution.  
See the [LICENSE](./LICENSE) file for full details.

---

## 👨‍💻 Author
**Rahul Bansal**  
💻 Python & OpenCV Enthusiast | 🧠 Computer Vision Learner  
📷 *Lane Detection using OpenCV — built for practice, performance, and precision.*

---

## 🌟 Support the Project

If you found this project useful or learned something from it, consider giving it a **⭐ on GitHub**!  
Your support helps others discover the project and motivates continued improvements. 🚀💡