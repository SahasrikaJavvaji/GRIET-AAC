import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\sahasrika\OneDrive\Pictures\Screenshots\AAC score card.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Original Image with Coordinates")
plt.show()
cropped = img[470:875, 0:725]
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
saved=cv2.imwrite(r'C:\Users\sahasrika\OneDrive\Pictures\Screenshots\croppedimage.png',cropped)