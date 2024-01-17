import cv2


#load th video
#cap actually has the video
cap = cv2.VideoCapture('vid.mp4')
cap_two = cv2.VideoCapture('vid.mp4')

#get the frame per second (FPS)
#from the video we are retrieving the fps
fps = cap.get(cv2.CAP_PROP_FPS)
fps_two = cap_two.get(cv2.CAP_PROP_FPS)

#prints the fps for the video
print("Frames Per Second for OrIginal VIDEO",round(fps))
#print(fps_two)


#DEFINIng the output file name
output_file_one = 'video_one_fast_motion.mp4'
output_file_two = 'video_two_slow_motion.mp4'

#increasing the fps
output_fps = fps * 2
output_fps_two = fps / 2

print("Output File 1, fps: ",round(output_fps))
print("Output File 2, fps: ",round(output_fps_two))



#create the video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fourcc_two = cv2.VideoWriter_fourcc(*'mp4v')

#out is the vidoe writer object
out = cv2.VideoWriter(output_file_one, fourcc, output_fps,(int(cap.get(3)), int(cap.get(4))))
out_slow = cv2.VideoWriter(output_file_two, fourcc_two, output_fps_two,(int(cap.get(3)), int(cap.get(4))))

#converting video FPS
while cap.isOpened():
    ret, frame = cap.read()
    #cv2.imshow('Frame',frame)
    #cv2.waitKey(200)
    if not ret:
        break
    out.write(frame)
    out_slow.write(frame)

#to destroy all the windows created by the program
#cv2.destroyAllWindows()


#to delay the destroying of windows
#cv2.waitKey(100)

