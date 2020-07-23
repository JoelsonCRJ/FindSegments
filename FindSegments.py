import cv2
import numpy as np
img = cv2.imread('test_map5.pgm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,14,0.01,10)

corners = np.int0(corners)
corners_list=[]
j=0
for corner in corners:
    x,y = corner.ravel()
    corners_list.append([x,y,j])
    cv2.circle(img,(x,y),3,255,-1)
    string = '({},{})'.format(x,y)
    position = (x,y)
    cv2.putText(img,string,position,cv2.FONT_HERSHEY_SIMPLEX,0.3,(209, 80, 0, 255), #font color
     1) #font stroke)
    j=j+1

print(corners_list)
 
segments = ['A','B','C','D','E']
distances =[0,0,0,0,0]

distances[0] = np.sqrt(pow((corners_list[11][0]-corners_list[9][0]),2) + pow((corners_list[11][1]-corners_list[9][1]),2))
distances[1] = np.sqrt(pow((corners_list[8][0]-corners_list[5][0]),2) + pow((corners_list[8][1]-corners_list[5][1]),2))
distances[2] = np.sqrt(pow((corners_list[8][0]-corners_list[12][0]),2) + pow((corners_list[8][1]-corners_list[12][1]),2))
distances[3] = np.sqrt(pow((corners_list[6][0]-corners_list[13][0]),2) + pow((corners_list[6][1]-corners_list[13][1]),2))
distances[4] = np.sqrt(pow((corners_list[4][0]-corners_list[2][0]),2) + pow((corners_list[4][1]-corners_list[2][1]),2))

for i in range (0,5):
    print('{} : {}'.format(segments[i],distances[i]*0.05))
cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()