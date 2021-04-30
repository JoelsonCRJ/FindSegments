import cv2
import numpy as np

img = cv2.imread('01_escritorio_2solve_teste.pgm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,10,0.01,10)

corners = np.int0(corners)
corners_list=[]
j=0
for corner in corners:
    x,y = corner.ravel()
    corners_list.append([x,y,j])
    cv2.circle(img,(x,y),3,255,-1)
    string = '({})'.format(j)
    position = (x,y)
    cv2.putText(img,string,position,cv2.FONT_HERSHEY_SIMPLEX,0.3,(209, 10, 0, 255), #font color
     1) #font stroke)
    j=j+1

print(corners_list)
 
segments = ['A']
distances =[0]
# print(corners_list[77])
# print(corners_list[34])

distances[0] = np.sqrt(pow((corners_list[5][0]-corners_list[9][0]),2) + pow((corners_list[5][1]-corners_list[9][1]),2))
# distances[1] = np.sqrt(pow((corners_list[8][0]-corners_list[5][0]),2) + pow((corners_list[8][1]-corners_list[5][1]),2))
# distances[2] = np.sqrt(pow((corners_list[8][0]-corners_list[12][0]),2) + pow((corners_list[8][1]-corners_list[12][1]),2))
# distances[3] = np.sqrt(pow((corners_list[6][0]-corners_list[13][0]),2) + pow((corners_list[6][1]-corners_list[13][1]),2))
# distances[4] = np.sqrt(pow((corners_list[4][0]-corners_list[2][0]),2) + pow((corners_list[4][1]-corners_list[2][1]),2))

for i in range (0,len(distances)):
    print('{} : {} m'.format(segments[i],distances[i]*0.05))
    print('{} : {} px'.format(segments[i],distances[i]))
cv2.imshow('Corner',img)
cv2.imwrite('01_escritorio_2solve_saved.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()