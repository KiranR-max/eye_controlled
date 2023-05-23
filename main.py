import cv2
import mediapipe as mp
import PyAutoGUI as pyautogui #lets control mouse ,keybord...
# to check the version of opencv installed
# print(cv2.__version__)
cam=cv2.VideoCapture(0)#index 0
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmarks_points=output.multi_face_landmarks
    (frame_h,frame_w,_)=frame.shape #frame width height and depth
    #we included only h,w as it is 2D 
   # print(landmarks_points)#prints the coordinates of the eye
    if landmarks_points:
        landmarks=landmarks_points[0].landmark
        for landmark in enumerate(landmarks[474:478]):#4 diffent landmarks on your face
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))#3 is the radius
            if id==1:
                pyautogui.moveTO(x,y)
           # print(x,y)#position in 2 dimension
    cv2.imshow("eye contoleed mouse",frame)
    cv2.waitKey(1)