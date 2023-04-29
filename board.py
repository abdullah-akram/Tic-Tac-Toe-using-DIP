import cv2
import sys

# to draw X on square
def drawXO(img_rgb,x,w,y,h):
    cv2.putText(img_rgb, 'X', (x + w // 2 - 30, y + h // 2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0,0), 3)

# to draw O on square
def drawO(img_rgb,x,w,y,h):
    cv2.putText(img_rgb, 'O', (x + w // 2 - 30, y + h // 2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)

# def moveAI(img,img_rgb,cnt,k,cc):
#     x, y, w, h = cv2.boundingRect(cnt)
#     sub_img = img[y:y+h, x:x+w]
#     _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#     print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
#     if cv2.sumElems(sub_thresh)[0] > 180000: # adjust threshold as needed
#         # cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 0, 255), 2)
#         print("no")
#     else:
    
#         drawO(img_rgb,x,w,y,h)
        
#     k+=1
#     return k
    
    
#detects empty square and fills a value accordingly X
def detectEmptySquare(img,img_rgb,cnt,j,cc):
    x, y, w, h = cv2.boundingRect(cnt)
    sub_img = img[y:y+h, x:x+w]
    _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
    if cv2.sumElems(sub_thresh)[0] > 180000: # adjust threshold as needed
        print("empty value:"+str(cv2.sumElems(sub_thresh)[0]))
    else:
        # print("j = "+str(j))
        if j==(9-cc):
            drawXO(img_rgb,x,w,y,h)
            print("filled value:"+str(cv2.sumElems(sub_thresh)[0]))
            
            # moveAI(img,img_rgb,cnt,j,cc)
    j+=1
    return j

#detects empty square and fills a value accordingly O
def detectOSquare(img,img_rgb,cnt,j,cc):
    x, y, w, h = cv2.boundingRect(cnt)
    sub_img = img[y:y+h, x:x+w]
    _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
    if cv2.sumElems(sub_thresh)[0] > 180000: # adjust threshold as needed
        print("empty value:"+str(cv2.sumElems(sub_thresh)[0]))
    else:
        # print("j = "+str(j))
        if j==(9-cc):
            drawO(img_rgb,x,w,y,h)
            print("filled value:"+str(cv2.sumElems(sub_thresh)[0]))
            
            # moveAI(img,img_rgb,cnt,j,cc)
    j+=1
    return j

#Takes in input as the count of fingers and fills the box accordingly
def callbox(cc,key,bol):
    if key == ord('q'):
        sys.exit()
    j=0
    k=0
    img = cv2.imread('box1.png', cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    # Draw bounding box around each contour and check for text
 
#  Check to maintain alternating turns
    if bol:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300: # Filter out small contours
                j = detectEmptySquare(img,img_rgb,cnt,j,cc)
        bol = False   
    else:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300: # Filter out small contours
                j = detectOSquare(img,img_rgb,cnt,j,cc)
        bol = True   


  
    cv2.destroyWindow('Board')
#  Update the board
    cv2.imwrite('box1.png',img_rgb)
    # imgg= cv2.imread('box1.png')
    # cv2.imshow('Result', img_rgb)
    imS = cv2.resize(img_rgb, (560, 450)) 

    # cv2.imshow('Board', imS)

    # cv2.resizeWindow("Result", 520, 520)
    cv2.namedWindow('Board', cv2.WINDOW_NORMAL)

    cv2.moveWindow("Board", 775,130) 



    cv2.setWindowProperty("Board",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.resizeWindow('Board', 530, 460)
    cv2.moveWindow("Board", 775,130) 

    cv2.imshow('Board', imS)
    return bol