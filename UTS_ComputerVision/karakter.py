import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)

canvas = np.full((400, 400, 3), (255, 255, 255), dtype=np.uint8)

cv2.circle(canvas, (200, 200), 100, (0, 0, 255), -1)
cv2.circle(canvas, (160, 170), 20, (255, 255, 255), -1)
cv2.circle(canvas, (240, 170), 20, (255, 255, 255), -1)
cv2.circle(canvas, (160, 170), 10, (0, 0, 0), -1)
cv2.circle(canvas, (240, 170), 10, (0, 0, 0), -1)
cv2.rectangle(canvas, (160, 230), (240, 250), (0, 0, 0), -1)
cv2.line(canvas, (200, 100), (200, 50), (0, 0, 0), 3)
cv2.circle(canvas, (200, 45), 8, (0, 255, 0), -1)
cv2.putText(canvas, "BotRen", (150, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2)

cv2.imwrite("output/karakter.png", canvas)

M_trans = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(canvas, M_trans, (400, 400))
cv2.imwrite("output/translate.png", translated)

M_rotate = cv2.getRotationMatrix2D((200, 200), 45, 1)
rotated = cv2.warpAffine(canvas, M_rotate, (400, 400))
cv2.imwrite("output/rotate.png", rotated)

resized = cv2.resize(canvas, None, fx=0.5, fy=0.5)
cv2.imwrite("output/resize.png", resized)

crop = canvas[100:300, 100:300]
cv2.imwrite("output/crop.png", crop)

background = np.full((400, 400, 3), (255, 200, 100), dtype=np.uint8)
bitwise_and = cv2.bitwise_and(canvas, background)
cv2.imwrite("output/bitwise.png", bitwise_and)

brighter = cv2.add(canvas, (50, 50, 50, 0))
cv2.imwrite("output/final.png", brighter)

cv2.imshow("karakter", canvas)
waitkey(1000)

print("Semua gambar berhasil disimpan ke folder output/")
