import sys
import argparse

import cv2

# save video frames to list
def extractImages(pathIn):
    frames = []
    cap = cv2.VideoCapture(pathIn)
    ret = True
    
    while ret:
      ret, img = cap.read() # read one frame from the 'capture' object; img is (H, W, C)
      if ret:
        frames.append(img)
    return frames



def analyzeVideoFrmaes(frames):
    return 0
    

if __name__ == "__main__":
    
    #a = argparse.ArgumentParser()
    #a.add_argument("--pathIn", help="path to video")
    #args = a.parse_args()
    #print(args)

    
    # videos to list
    videoframes = extractImages('test.mp4')

    # analyze video
    #analyzeVideoFrmaes(videofrmaes)
