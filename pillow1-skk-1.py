# PIL 모듈에서 몇 개의 클래스를 포함시킨다. 
from PIL import Image, ImageTk 

# tkinter 모듈을 포함시킨다. 
import tkinter as tk

img = Image.open("lena.png")
#img = Image.open("c:\\temp\\lenna.png")
#img = Image.open("c:\\temp\\추.jpg")
#img = Image.open("c:/temp/chipmunk.png")

#console에 image 정보 출력
print (img.size, img.mode, img.format)
#img.size는 Tuple 형식 : 교재 p.264

# 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다. 
window = tk.Tk()
canvas = tk.Canvas(window, width=img.size[0], height=img.size[1])
canvas.pack()

# tk 형식으로 영상을 변환한다. 
tk_img = ImageTk.PhotoImage(img)

# tkinter의 캔버스에 영상을 표시한다. 

#canvas.create_image(img.size[0]/2, img.size[1]/2,  image=tk_img)
#canvas.create_image(img.size[0], img.size[1],  image=tk_img)
#canvas.create_image(0,0,  image=tk_img)
canvas.create_image(0,0, anchor=tk.NW,image=tk_img)
window.mainloop()
