import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("5181.jpg")

hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([20, 255, 255])

mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

result = cv2.bitwise_and(src, src, mask=mask_red)

y_hue = 120  # Желтый оттенок
y_saturation = 255  # Полная насыщенность
y_value = 255  # Максимальное значение яркости
y_color = np.array([y_hue, y_saturation, y_value])

y_mask = np.zeros_like(src)
y_mask[mask_red != 0] = y_color

result1 = cv2.add(result, y_mask)

while True:
  cv2.imshow("1", src)
  cv2.imshow("2", result)
  cv2.imshow("3", result1)
  key = cv2.waitKey(0) & 0xFF
  if key == 27:
      break
  
cv2.destroyAllWindows()

