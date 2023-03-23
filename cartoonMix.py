import cv2

# Load the image
img = cv2.imread("input_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter
bilateral = cv2.bilateralFilter(gray, 11, 17, 17)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Increase contrast
equalized = cv2.equalizeHist(thresh)

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Increase saturation and value channels
hsv[:,:,1] += 50
hsv[:,:,2] += 50

# Convert back to BGR color space
colorized = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Apply Canny edge detection
edges = cv2.Canny(colorized, 100, 200)

# Dilate edges to thicken them
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilated = cv2.dilate(edges, kernel)

# Combine cartoon and edges
cartoon = cv2.bitwise_and(colorized, colorized, mask=thresh)
final = cv2.bitwise_or(cartoon, cartoon, mask=dilated)

# Display the output
cv2.imshow("Anime Style", final)
cv2.waitKey(0)
cv2.destroyAllWindows()