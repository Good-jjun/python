# PIL 모듈에서 몇 개의 클래스를 포함시킨다. 
from PIL import Image, ImageTk 

# tkinter 모듈을 포함시킨다. 
import tkinter as tk
import numpy as np

#img = Image.open("c:\\temp\\lenna.png")
img = Image.open("lenna.png")
#img = Image.open("chipmunk.png")

#console에 image 정보 출력
print (img.size, img.mode, img.format)

# 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다. 
window = tk.Tk()
canvas = tk.Canvas(window, width=img.size[0], height=img.size[1])
canvas.pack()


# im_array = np.asarray(img)   # ValueError: assignment destination is read-only
im_array = np.asarray(img).copy()

for i in range(len(im_array)):
    for j in range(len(im_array[0])):
        #mean=im_array[i][j][0]/3+im_array[i][j][1]/3+im_array[i][j][2]/3
        #mean=(im_array[i][j][0]+im_array[i][j][1]+im_array[i][j][2])/3  #오류 byte overflow
        mean=(int(im_array[i][j][0])+int(im_array[i][j][1])+int(im_array[i][j][2]))/3
        im_array[i][j][1]=im_array[i][j][2]=0


img_mean = Image.fromarray(im_array)

# tk 형식으로 영상을 변환한다. 
tk_img = ImageTk.PhotoImage(img_mean)

# tkinter의 캔버스에 영상을 표시한다. 
canvas.create_image(0,0, anchor=tk.NW,image=tk_img)

window.mainloop()


