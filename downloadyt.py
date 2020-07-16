import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
root= tk.Tk()
root.title("Youtube Video Downloader")
canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(350, 100, window=entry1 , width = 500)

entry2 = tk.Entry (root) 
canvas1.create_window(350, 150, window=entry2 , width = 500)


label0 = tk.Label(root, text='DOWNLOAD YOUTUBE')
label0.config(font=('helvetica', 14,'bold'))
canvas1.create_window(300, 40, window=label0)

label1 = tk.Label(root, text='Input URL:')
label1.config(font=('helvetica', 10,'bold'))
canvas1.create_window(60, 100, window=label1)

label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10,'bold'))
canvas1.create_window(70, 150, window=label1)

label1 = tk.Label(root, text='Create by: Fakhril AK')
label1.config(font=('helvetica', 10,'bold'))
canvas1.create_window(510, 280, window=label1)


def Download():
     try:
          link = entry1.get()
          yt = YouTube(link).streams.first().download(output_path='C:/Users/FAKHRIL AK/Downloads',filename=entry2.get())
          info = "Saved Using Name" + entry2.get()
          messagebox.showinfo("Success", info)
     except:
          messagebox.showinfo("Success","Connection Error")
      
buttonAdd = tk.Button(text='DOWNLOAD', command=Download, bg='green', fg='Black', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 190, window=buttonAdd)


root.mainloop()
