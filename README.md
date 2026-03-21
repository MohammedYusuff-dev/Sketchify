# ✏️ Sketchify – Adaptive Graphite Sketch Generator

Turn any image into a clean, realistic pencil sketch using advanced image processing techniques.

This project goes beyond basic sketch filters by combining tone mapping, local contrast enhancement, and intelligent edge blending to produce a more natural graphite look.

----

## ⚡ Features

* 🎯 Adaptive tone mapping for better shading control
* 🧩 CLAHE-based local contrast enhancement
* 🧠 Edge-preserving smoothing (bilateral filter)
* ✏️ Pencil sketch generation using division blending
* 🔍 Subtle edge enhancement for realistic outlines
* 🎚️ Shadow depth control for a graphite feel
* ⚡ Final sharpening for crisp output

---

## 🛠️ Tech Stack

* Python
* OpenCV (`cv2`)
* NumPy

---

## 📸 How It Works

1. Resize image for consistent processing
2. Convert to grayscale
3. Apply gamma correction for tone control
4. Enhance contrast using CLAHE
5. Generate pencil base using Gaussian blur + division
6. Preserve structure with bilateral filtering
7. Extract edges using Canny
8. Blend base + edges intelligently
9. Adjust shadows and highlights
10. Apply sharpening for final output

---

## ▶️ Usage

```bash
pip install opencv-python numpy
```

Update the image path in the script:

```python
img_path = "your_image_path_here"
```

Run the script:

```bash
python sketchify.py
```

---

## 📷 Output

The program displays:

* Original Image
* Generated Sketch

---

## 🎯 Goal

To create a more **realistic and visually appealing sketch effect**, instead of the typical overexposed or low-detail filters.

---

## 🚧 Future Improvements

* GUI interface (Tkinter or PyQt)
* Batch image processing
* Adjustable sketch intensity sliders
* Color sketch mode
* Web version (Flask / Streamlit)

---

## 🤝 Contributing

Pull requests are welcome. If you have ideas to improve the sketch realism or performance, feel free to contribute.

---

## 📄 License

Open-source for learning and experimentation.

---

## 💡 Author

Built by Yusuff — focused on mastering AI, cybersecurity, and creative tech.
