import cv2
import numpy as np

# ---------- READ IMAGE ----------
img_path = r"Your File Path Here"
img = cv2.imread(img_path)

if img is None:
    print("Image not found")
    exit()

# ---------- RESIZE ----------
max_width = 600
h, w = img.shape[:2]
scale = max_width / w
img = cv2.resize(img, (max_width, int(h * scale)))

# ---------- GRAYSCALE ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------- TONE ANALYSIS ----------
# Normalize for consistent tone mapping
gray_float = gray.astype(np.float32) / 255.0

# Gamma correction (adaptive feel)
gamma = 0.9
tone = np.power(gray_float, gamma)

# ---------- LOCAL CONTRAST ENHANCEMENT ----------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
tone = (tone * 255).astype(np.uint8)
tone = clahe.apply(tone)

# ---------- PENCIL BASE ----------
blur = cv2.GaussianBlur(tone, (0, 0), sigmaX=20)
base = cv2.divide(tone, blur, scale=256)

# ---------- STRUCTURE PRESERVATION ----------
# Bilateral filter keeps edges but smooths noise
smooth = cv2.bilateralFilter(tone, d=9, sigmaColor=75, sigmaSpace=75)

# Subtle edge extraction
edges = cv2.Canny(smooth, 50, 120)
edges = cv2.GaussianBlur(edges, (3,3), 0)

# ---------- BLEND INTELLIGENTLY ----------
# Keep base shading dominant, edges secondary
sketch = cv2.addWeighted(base, 0.85, edges, 0.15, 0)

# ---------- SHADOW DEPTH CONTROL ----------
# Compress highlights, deepen midtones
sketch = sketch.astype(np.float32) / 255.0
sketch = np.power(sketch, 0.85)
sketch = np.clip(sketch * 1.2 - 0.05, 0, 1)

sketch = (sketch * 255).astype(np.uint8)

# ---------- FINAL SHARPEN ----------
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
sketch = cv2.filter2D(sketch, -1, kernel)

# ---------- DISPLAY ----------
sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
combined = np.hstack((img, sketch_bgr))

cv2.imshow("Original | Adaptive Graphite Sketch", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
