import numpy as np
import cv2 as cv
import os

def main():
    # 1. Load calibration data
    file_path = 'calibration_result.npz'
    if not os.path.exists(file_path):
        print("Error: Calibration data not found.")
        return

    data = np.load(file_path)
    K = data['mtx']
    dist_coeff = data['dist']

    # 2. Open input video
    video_file = 'data.MOV'
    video = cv.VideoCapture(video_file)
    
    # 3. VideoWriter Configuration
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc(*'mp4v') # Codec for .mp4 on macOS
    
    # Initialize VideoWriter to save the result
    out = cv.VideoWriter('corrected_result.mp4', fourcc, fps, (width, height))

    map1, map2 = None, None

    print("Processing and saving video... Press 'q' to stop.")

    while video.isOpened():
        valid, img = video.read()
        if not valid:
            break

        # 4. Generate rectification maps (only once)
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (width, height), cv.CV_32FC1)
        
        # 5. Apply remap to correct distortion
        rectified_img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)

        # 6. Write corrected frame to output file
        out.write(rectified_img)

        # 7. Display live preview
        cv.imshow('Saving Corrected Video...', rectified_img)
        if cv.waitKey(1) == ord('q'):
            break

    # 8. Release all resources
    video.release()
    out.release() 
    cv.destroyAllWindows()
    print("Success! Result saved as 'corrected_result.mp4'")

if __name__ == '__main__':
    main()