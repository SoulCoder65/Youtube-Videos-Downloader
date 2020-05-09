from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import showerror,showinfo
from threading import *

# VARIABLES
font=('verdana',15,'bold')
def progress_bar(stream,chunk,file_handle,remaining):
    print("1")
    download_file=(file_size-remaining)
    percent=(download_file/file_size)*100
    print(percent)
    print("1")
    down_per.config(text="{:00.0f} % Downloaded".format(percent))
def threadcall():
    thread=Thread(target=video_down)
    thread.start()

file_size=0
def video_down():
    global file_size
    try:
        url=url_field.get()
        if url=="":
            showerror("URL Required","Provide Url")
        else:
            download_path=askdirectory()

            down_btn.config(state=DISABLED)
            youtube=YouTube(url,on_progress_callback=progress_bar)
            str_obj=youtube.streams.first()
            str_obj.download(download_path)
            showinfo("Downloaded","Video Downloaded Successfully!!")
            down_btn.config(text='Download')
            down_btn.config(state=ACTIVE)
            file_size=str_obj.filesize
    except Exception as e:
        showerror("Download Error","Cannot Download this video!!")
# GUI FOR YOUTUBE DOWNLOADER
window=Tk()
window.title("Youtube Downloader By Akshay")
window.geometry("450x500")
img=PhotoImage(file='/home/akshay/Desktop/python/youtube_downloader/photos/icons8-youtube-128.png')
youtube_img=Label(window,image=img)
youtube_img.pack(side=TOP)
url_field=Entry(window,font=font,justify=CENTER)
url_field.pack(side=TOP,padx=5)
down_btn=Button(window,text='Download',font=font,activebackground='blue',activeforeground='white',relief='solid',command=threadcall)
down_btn.pack(side=TOP,pady=10)
down_per=Entry(window,font=font)
down_per.pack(side=TOP,pady=10)
window.mainloop()
