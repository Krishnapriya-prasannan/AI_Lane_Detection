
### **Day 10 - Lane Detection**  
This is part of my **#100DaysOfAI** challenge.  
On **Day 10**, I implemented a basic **lane detection system** using **Computer Vision techniques** to identify road lane markings from a driving video — a key part of autonomous vehicle perception.

---

### **Goal**  
Detect lane lines from a front-facing camera feed in a driving scenario using classical CV methods like **Canny edge detection** and **Hough Transform**.

---

### **Technologies Used**

| Tool     | Purpose                                           |
|----------|---------------------------------------------------|
| Python   | Main programming language                         |
| OpenCV   | Image and video processing, edge & line detection |
| NumPy    | Numerical operations and matrix manipulation      |
| Matplotlib | Optional visualization for testing             |
| VS Code  | Code editor                                       |

---

### **How It Works**

1. **Video Frame Extraction**
   - Captured individual frames from the driving video using OpenCV.

2. **Canny Edge Detection**
   - Converted frames to grayscale.
   - Applied Gaussian blur to reduce noise.
   - Used Canny edge detector to highlight lane-like edges.

3. **Region of Interest Mask**
   - Defined a polygonal mask to focus only on the region of the road (where lanes are expected).

4. **Hough Line Transform**
   - Detected straight lines in the masked edge image.
   - Separated left and right lanes based on slope and position.

5. **Lane Overlay**
   - Averaged the detected line segments for stability.
   - Overlaid the detected lanes back onto the original frame.

6. **Output Video**
   - Compiled the processed frames into an output video with highlighted lanes.

---

### **Highlights**

- Understood and applied **classical computer vision** concepts.
- Developed a real-time **lane detection pipeline**.
- Learned to work with **video I/O**, frame-wise processing, and overlay rendering.
- Hands-on practice with **Canny + Hough Transform combo**.
- Built a visual foundation for more advanced AI-driven self-driving tasks.

---

### **What I Learned**

- How Canny edge detection and Hough transform can work together for line detection.
- Importance of preprocessing and ROI selection in CV tasks.
- OpenCV functions for frame capture, display, and writing output videos.
- Foundations of lane detection, which is a core module in autonomous driving systems.
- How to pipeline real-time vision tasks for self-driving scenarios.

---

