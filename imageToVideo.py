import json
import cv2

with open("./photos.json", "r") as f:
    data = f.read()


images = json.loads(data)
videoName = "./hayasakaBlow.avi"
width = 1200
height = 960
fps = 30

fourcc = cv2.VideoWriter.fourcc(*'DIVX')
video = cv2.VideoWriter(videoName, fourcc, fps, (width, height))

for i in images:
    frame = cv2.imread(i)
    video.write(frame)
    
video.release()
cv2.destroyAllWindows()