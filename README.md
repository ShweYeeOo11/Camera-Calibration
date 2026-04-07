# Camera Calibration and Lens Distortion Correction

This project demonstrates the process of **Camera Calibration** to calculate intrinsic parameters and **Geometric Distortion Correction** for a wide-angle lens using Python and OpenCV.

---

## 1. Project Overview
Most camera lenses are prone to **Geometric Distortion**, where straight lines in the real world appear curved in the captured image. This project demonstrates a standard **Camera Calibration** workflow to mathematically calculate the camera's intrinsic parameters and rectify these optical distortions. 

By using a chessboard-based calibration method, we can accurately estimate the camera matrix and distortion coefficients, ensuring geometric consistency and spatial accuracy for high-level computer vision applications.

---

## 2. Calibration Results
The following parameters were obtained using a 8 x 6 (inner corners) chessboard pattern:

### Root Mean Square Error (RMSE)
* **RMSE:** 1.150194673247331

### Camera Matrix (K)
The intrinsic matrix representing focal length (fx, fy) and principal point (cx, cy):
```python
[[3.19401902e+03, 0.00000000e+00, 1.08432504e+03],
 [0.00000000e+00, 3.19039532e+03, 1.92592461e+03],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]
```
### 🔧 Distortion Coefficients (`dist`)

These coefficients correct radial and tangential distortion:

| Coefficient | Value |
|-------------|-------|
| **k1** (Radial) | `2.66674803e-01` |
| **k2** (Radial) | `-1.59792785e+00` |
| **p1** (Tangential) | `8.62949902e-04` |
| **p2** (Tangential) | `1.05856853e-03` |
| **k3** (Radial) | `3.01521579e+00` |

**Full array format:**

```python
[[ 2.66674803e-01, -1.59792785e+00,  8.62949902e-04,  1.05856853e-03, 3.01521579e+00]]
```
## 3. Implementation Workflow

### Step 1: Image Selection and Calibration
Run the calibration script to extract frames from the input video (`data.MOV`). 
* The script detects chessboard corners and draws "rainbow lines" when a complete pattern is found.
* Press **Space** to save a frame (at least 10-15 frames recommended for better accuracy).
* Press **Enter** to calculate parameters and save them to `calibration_result.npz`.

**Command:**
```bash
python3 icamera_calibration.py
```
### Step 2: Video Rectification
Run the correction script to apply the calculated parameters to the video stream and generate the output.
* Press **'r'** to toggle between **Original** and **Rectified** views.
* The script automatically saves the output as `corrected_result.mp4`.

**Command:**
```bash
python3 distortion_correction.py
```
## 4. Visual Comparison

The following table compares the raw input video frames with the rectified output using the calculated distortion coefficients.

| Original (Distorted) | Rectified (Corrected) |
| :---: | :---: |
| ![Original Frame](data.gif) | ![Rectified Frame](corrected_result.gif) |
| **Problem:** Straight edges of the chessboard appear curved due to Barrel Distortion. | **Solution:** Lines are mathematically straightened using the $K$ matrix and $dist$ coefficients. |

### Observation:
* With an **RMSE of 1.150194673247331**, the geometric projection is highly accurate.
* The $k_1$ ($2.666e-01$) and $k_2$ ($-1.597e+00$) values effectively counteract the wide-angle lens "bulge" effect.

*(Note: To make this section professional, replace the placeholder links above with actual screenshots from your `corrected_result.mp4`.)*

## 5. Requirements

The project is developed using **Python 3.x** and relies on the following key computer vision libraries:

* **OpenCV (opencv-python):** Used for chessboard corner detection, camera matrix calculation (`calibrateCamera`), and image remapping (`undistort`).
* **NumPy:** Used for high-performance matrix operations and handling 3D point coordinates.

### Installation
To install the necessary dependencies, run the following command in your terminal:

```bash
pip install opencv-python numpy
```
## 6. Project Structure

The repository is organized as follows to ensure a clear calibration workflow and easy navigation through the source files:

| File Name | Description |
| :--- | :--- |
| `icamera_calibration.py` | Main script for frame extraction, chessboard corner detection, and calculating the $K$ matrix & $dist$ coefficients. |
| `distortion_correction.py` | Script to apply saved calibration data to the video stream for real-time correction and undistortion. |
| `calibration_result.npz` | Compressed NumPy file containing the saved `K` (camera matrix), `dist` (coefficients), `rvecs`, and `tvecs`. |
| `data.mp4` | The raw input video containing the wide-angle lens footage used for the calibration process. |
| `corrected_result.mp4` | The final rectified output video with the geometric lens distortion removed. |
| `README.md` | Project documentation, technical results (RMSE: 1.15), and implementation guide. |

---
