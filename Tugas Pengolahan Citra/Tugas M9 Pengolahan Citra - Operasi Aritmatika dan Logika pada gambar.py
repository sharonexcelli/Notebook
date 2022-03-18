import cv2
import numpy as np

img1 = cv2.imread('gambar1.jpg')
img2 = cv2.imread('gambar2.jpg')

tambah = img1 + img2
kurang = img1 - img2
dan = img1 & img2
atau = img1 | img2

cv2.imshow('Tambah',tambah)
cv2.imshow('Kurang',kurang)
cv2.imshow('And',dan)
cv2.imshow('Or',atau)
cv2.waitKey(0)
cv2.destroyAllWindows()