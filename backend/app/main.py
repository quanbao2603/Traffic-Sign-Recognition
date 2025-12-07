import cv2
import numpy as np

img = cv2.imread("D:/HCMUTE/Digital_Image/homework/tuan03/download.jpg", cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(img, (5, 5), 1.2)
lap = cv2.Laplacian(blur, cv2.CV_32F, ksize=3)

added = cv2.add(img.astype("float32"), lap)
added = cv2.normalize(added, None, 0, 255, cv2.NORM_MINMAX).astype("uint8")

gamma = 1.5
out = np.power(added / 255.0, gamma)
out = (out * 255).astype("uint8")

cv2.imshow("Original", img)
cv2.imshow("After Pipeline", out)
cv2.waitKey(0)
cv2.destroyAllWindows()