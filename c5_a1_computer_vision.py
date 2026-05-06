import cv2

img = cv2.imread("person.png")
cv2.namedWindow("loaded image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("loaded image",800,500)

cv2.imshow("loaded image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"image dimention: {img.shape}")