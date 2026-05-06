import cv2

img = cv2.imread("person.png")
grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(grey_image,(224,224))

cv2.imshow("processed image",resized_image)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("grey_scale_resized_image.jpg",resized_image)
    print("image saved as grey_scale_image.jpg")
else:
    print("image not saved")

cv2.destroyAllWindows()
print(f"processed image dimestions: {resized_image.shape}")