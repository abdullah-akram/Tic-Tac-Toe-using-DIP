import cv2
import sys
import winsound
# to draw X on square
def drawXO(img_rgb,x,w,y,h):
    cv2.putText(img_rgb, 'X', (x + w // 2 - 30, y + h // 2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0,0), 3)

# to draw O on square
def drawO(img_rgb,x,w,y,h):
    cv2.putText(img_rgb, 'O', (x + w // 2 - 30, y + h // 2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)

    
#detects empty square and fills a value accordingly X
def detectEmptySquare(img,img_rgb,cnt,j,cc):
    x, y, w, h = cv2.boundingRect(cnt)
    sub_img = img[y:y+h, x:x+w]
    _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
    if cv2.sumElems(sub_thresh)[0] > 180000: # adjust threshold as needed
        # print("filled value:"+str(cv2.sumElems(sub_thresh)[0]))
        print("")
    else:
        # print("j = "+str(j))
        if j==(9-cc):
            winsound.Beep(1240, 400)
            drawXO(img_rgb,x,w,y,h)
            # print("X on "+str(cc))
            # print("empty value:"+str(cv2.sumElems(sub_thresh)[0]))
            
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
        # print("empty value:"+str(cv2.sumElems(sub_thresh)[0]))
        print("")
    else:
        # print("j = "+str(j))
        if j==(9-cc):
            winsound.Beep(1240, 400)
            drawO(img_rgb,x,w,y,h)
            # print("O on "+str(cc))
            # print("filled value:"+str(cv2.sumElems(sub_thresh)[0]))
            
            # moveAI(img,img_rgb,cnt,j,cc)
    j+=1
    return j



def checkresult(img,cntours):

    cntx = 0
    cnto=0
    xlist = []
    olist = []
    i=1
    for cnt in cntours:
        x, y, w, h = cv2.boundingRect(cnt)
        sub_img = img[y:y+h, x:x+w]
        _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
        j = 10-i
        if cv2.sumElems(sub_thresh)[0] > 183500 and cv2.sumElems(sub_thresh)[0] < 183700: # adjust threshold as needed
            # print("X detected on"+str(j))
            # cntx+=1
            xlist.append(j)

        elif cv2.sumElems(sub_thresh)[0] > 220800 and cv2.sumElems(sub_thresh)[0] < 220900: # adjust threshold as needed
            # print("0 detected on"+str(j))
            cnto+=1
            olist.append(j)
        i+=1    
            # moveAI(img,img_rgb,cnt,j,cc)
 
    checklist = [[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [1,5,9],
                 [3,5,7],
                 [2,5,8],
                 [1,4,7],
                 [3,6,9]]
    
    xset = set(xlist)
    for lst in checklist:
        if set(lst).issubset(xset):
            xshow = cv2.imread('xwon.png')
            cv2.namedWindow('Xwon', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Xwon",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow("Xwon", 525, 456)
            cv2.imshow("Xwon", xshow)
            cv2.moveWindow("Xwon", 21,128) 
            print(f"{lst} is a subset of {xlist}")
            return "x"

    oset = set(olist)
    for lst in checklist:
        if set(lst).issubset(oset):
            print(f"{lst} is a subset of {olist}")
            oshow = cv2.imread('owon.png')
            cv2.namedWindow('Owon', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Owon",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow("Owon", 525, 456)
            cv2.imshow("Owon", oshow)
            cv2.moveWindow("Owon", 21,128) 
            return "o"


    if len(xlist)+len(olist)>=9:
        draw = cv2.imread('draw.png')
        cv2.namedWindow('Draw', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Draw",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.resizeWindow("Draw", 525, 456)
        cv2.imshow("Draw", draw)
        cv2.moveWindow("Draw", 21,128) 
        return "d"
        # print(f"{lst} is a subset of {xlist}")


    print("cntx:"+str(xlist)+"\n cnto:"+str(olist))
    return "n"






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
    
    re = checkresult(img,contours)
    


  
    cv2.destroyWindow('Board')
#  Update the board
    cv2.imwrite('box1.png',img_rgb)
    # imgg= cv2.imread('box1.png')
    # cv2.imshow('Result', img_rgb)
    imS = cv2.resize(img_rgb, (530, 460)) 

    # cv2.imshow('Board', imS)

    # cv2.resizeWindow("Result", 520, 520)
    cv2.namedWindow('Board', cv2.WINDOW_NORMAL)
    cv2.moveWindow("Board", 775,130) 
    cv2.setWindowProperty("Board",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.resizeWindow('Board', 530, 460)
    cv2.moveWindow("Board", 775,130) 
    cv2.imshow('Board', imS)
    return bol,re