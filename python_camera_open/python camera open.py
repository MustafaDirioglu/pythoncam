import cv2
def camera():

  '''
  Here we write 0 to get images from the main camera.
  If you want to get images from other cameras, you need to change this number.
  '''

  camera = cv2.VideoCapture(0) 
  
  while True:
    ret, frame = camera.read()
    cv2.imshow('Video', frame) # 'Video' is used here to specify the name of the popup

    if cv2.waitKey(1) == 27: #It shows '(1)' 1msec output, because it is very fast, the image that is perceived as continuous video is obtained.
      exit(0)
    
camera()