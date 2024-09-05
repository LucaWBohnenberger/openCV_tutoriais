import cv2

img = cv2.imread('assets/map.jpg', -1)
img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
img = cv2.rotate(img, cv2.ROTATE_180)

# cv2.imwrite('new_image.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()