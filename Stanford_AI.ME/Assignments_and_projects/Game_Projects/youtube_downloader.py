from tkinter import *
import pytube
from pytube import *

video = None

def window():
  global root
  root = Tk()
  root.geometry('500x300')
  root.resizable(0,0)
  root.title("YouTube Downloader")

  # YouTube label creation
  ytd = Label(root, text="YouTube Videos download for free", font=("TimesNewRoman", 20, "bold italic"))
  ytd.pack()

  # Link entry field
  link = StringVar()
  link_label = Label(root, text="Paste Link Here:", font="arial 20 bold")
  link_label.place(x=160, y=60)
  link_entry = Entry(root, width=70, textvariable=link)
  link_entry.place(x=32, y=90)

  # Download button
  download_button = Button(root, text="DOWNLOAD", font="arial 15 bold", bg="Blue", padx=2, command=lambda: Downloader(link.get()))
  download_button.place(x=180, y=150)

  # Downloaded label
  downloaded_label = Label(root, text="DOWNLOADED", font="arial 15")

def Downloader(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
      print("This download was completed successfully!. Youtube video thief!")
  except:
    
    print("There was an error downloading the youtube video, Please try again!")

if video is not None:
    video.Downloader()
    downloaded_label.pack()

window()
root.mainloop()

if __name__ == "__window__":
  main()
