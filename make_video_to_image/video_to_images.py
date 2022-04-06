from __future__ import unicode_literals
import cv2
import os

import youtube_dl

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

if __name__ == '__main__':

  #!pip install youtube_dl

  #ここを書き換える
  URL = "https://youtu.be/PwhBA7J-Q2E"

  ydl_opts = {}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([f'{URL}'])#, 'https://youtu.be/qkDux-jahOk', 'https://youtu.be/PwhBA7J-Q2E'])
  os.makedirs('./images', exist_ok=True)

  files=os.listdir('./')
  print(files)
  for i in files:
    if (".py" not in i) and ("images" not in i):
      file_name=i
      print(file_name)
  filename = URL.split('=')[-1]
  
  save_all_frames(file_name,
                'images', 
                filename)