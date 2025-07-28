import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()

def histogram_equalization(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    eq_image = cv2.equalizeHist(image)
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(eq_image, cmap='gray'), plt.title('Equalized')
    plt.show()

def non_linear_filtering(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    filtered_image = cv2.medianBlur(image, 5)
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered')
    plt.show()

def apply_2d_dft(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)
    plt.imshow(magnitude_spectrum, cmap='hot')
    plt.title('DFT Magnitude Spectrum')
    plt.show()

def apply_2d_dct(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.float32(image) / 255.0
    dct = cv2.dct(image)
    plt.imshow(dct, cmap='hot')
    plt.title('DCT Coefficients')
    plt.show()

def edge_detection(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection')
    plt.show()

def line_and_corner_detection(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    corners = cv2.goodFeaturesToTrack(image, 100, 0.01, 10)
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image_color, (x1, y1), (x2, y2), (0, 255, 0), 2)
    if corners is not None:
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image_color, (int(x), int(y)), 5, (0, 0, 255), -1)
    plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
    plt.title('Line and Corner Detection')
    plt.show()

def segmentation(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, segmented = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    plt.imshow(segmented, cmap='gray')
    plt.title('Segmentation')
    plt.show()

def compute_sift_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    image_sift = cv2.drawKeypoints(image, keypoints, None)
    plt.imshow(image_sift, cmap='gray')
    plt.title('SIFT Features')
    plt.show()

# Usage example:
# show_image_gray('image.jpg')
# histogram_equalization('image.jpg')
# non_linear_filtering('image.jpg')
# apply_2d_dft('image.jpg')
# apply_2d_dct('image.jpg')
# edge_detection('image.jpg')
# line_and_corner_detection('image.jpg')
# segmentation('image.jpg')
# compute_sift_features('image.jpg')
