import sys
import os
import random
# 引入 tkinter 模組
import tkinter as tk

def OpenVideo():
	Path = PathString.get()
	List = os.listdir(Path)
	r = random.randint(0, len(List))
	fName = List[r]

	if fName[-3:].lower() in ('mp4','avi','flv','rmbv','wmv'):
		os.system( '"' + Path + '\\' + List[r] + '"')
	else:
		print('非影片')	
		

window = tk.Tk()
window.title('Hello World')
window.geometry("300x100+250+150")

labelPath = tk.Label(window,
                    text = "Path")
labelPath.pack()
PathString = tk.Entry(window)
PathString.pack()

button = tk.Button(window,         
                   text = '隨機撥放',  
				   command = OpenVideo)
#button.pack()
button.pack()  
window.mainloop()