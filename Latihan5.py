from PIL import Image, ImageEnhance
import numpy as np


img = Image.open('Ahmad.jpg')
print(img.format)
print(img.size)
print(img.mode)

arr = np.array(img.copy())
print(type(arr))
print(arr.shape)

arrFactor1 = arr.copy()
arrFactor2 = arr.copy()
arrFactor3 = arr.copy()
arrFactor4 = arr.copy()

for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
        arrFactor1[y, x] = [max(int(arr[y, x, 0]-40),0),
                            max(int(arr[y, x, 1]-40),0),
                            max(int(arr[y, x, 2]-40),0)]
        arrFactor2[y, x] = [max(int(arr[y, x, 0]-20),0),
                            max(int(arr[y, x, 1]-20),0),
                            max(int(arr[y, x, 2]-20),0)]
        arrFactor3[y, x] = [min(int(arr[y, x, 0]+20),255),
                            min(int(arr[y, x, 1]+20),255),
                            min(int(arr[y, x, 2]+20),255)]
        arrFactor4[y, x] = [min(int(arr[y, x, 0]+20),255),
                            min(int(arr[y, x, 1]+20),255),
                            min(int(arr[y, x, 2]+20),255)]
        
Image.fromarray(np.hstack((arrFactor1, arrFactor2,arr,arrFactor3, arrFactor4))).show()