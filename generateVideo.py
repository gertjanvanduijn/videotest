import cv2
import time
from apscheduler.schedulers.background import BackgroundScheduler

def capture_video():
    # specify the name of the output file
    filename = "video_" + time.strftime("%Y%m%d-%H%M%S") + ".avi"
    
    # specify video codec
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # specify output video settings
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    # start the camera
    cap = cv2.VideoCapture(0)

    # capture 10 seconds of video
    start_time = time.time()
    while(int(time.time() - start_time) < 10):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    # close the output file
    out.release()

    # close the camera
    cap.release()

# create a scheduling job that runs every 15 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(capture_video, 'interval', minutes=15)

# start the scheduler
scheduler.start()

# to keep the script running
while True:
    time.sleep(1)