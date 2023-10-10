import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("iabloki_krasnyj_frukt_188738_1280x720.jpg")

hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([20, 255, 255])

# Создайте маску для красного цвета
mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

# Примените маску к исходному изображению, чтобы оставить только красное яблоко в цвете
result = cv2.bitwise_and(src, src, mask=mask_red)

red_mask = cv2.bitwise_and(src, src, mask=mask_red)

# Создайте зеленый цвет (в HSV)
green_hue = 60  # Зеленый оттенок
green_saturation = 255  # Полная насыщенность
green_value = 255  # Максимальное значение яркости
green_color = np.array([green_hue, green_saturation, green_value])

# Создайте зеленую маску для изменения цвета
green_mask = np.zeros_like(src)
green_mask[mask_red != 0] = green_color

# Измените цвет предмета на зеленый
result1 = cv2.add(red_mask, green_mask)

while True:
  cv2.imshow("1", src)
  cv2.imshow("2", result)
  cv2.imshow("3", result1)
  key = cv2.waitKey(0) & 0xFF
  if key == 27:
      break
  
cv2.destroyAllWindows()
