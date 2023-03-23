
import cv2

# Load the original image
img = cv2.imread("input_image.jpg")

# Resize the image to half its size
img = cv2.resize(img, (img.shape[1]//8, img.shape[0]//8))

## Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter
bilateral = cv2.bilateralFilter(gray, 11, 17, 17)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Create cartoon-like effect using bitwise_and() function
cartoon = cv2.bitwise_and(img, img, mask=thresh)


# Apply the cartoon effect to the image
# (insert the cartoonization code here)

# Resize the cartoon image to match the original image size
cartoon = cv2.resize(cartoon, (img.shape[1], img.shape[0]))

# Blend the cartoon image with the original image
alpha = 0.4  # adjust the blending ratio as desired
blend = cv2.addWeighted(cartoon, alpha, img, 1-alpha, 0)

# Concatenate the original and blended images horizontally
side_by_side = cv2.hconcat([img, blend])

# Display the original and blended images side-by-side
cv2.imshow("Original vs Processed Images", side_by_side)
cv2.waitKey(0)
cv2.destroyAllWindows()