import cv2 


img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun", (20,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))

cv2.putText(img,"Mercury", (105,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Venus", (190,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Earth", (280,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Mars", (380,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Jupiter", (490,190), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Saturn", (720,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img,"Uranus", (950,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


cv2.imshow("output",img)

cv2.waitKey(0)



