import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import sys


def handsTimer(video, detector,bg,key):
	
	cnt = 0
	timer = 0
	initialTime = time.time()
	while True:
		if key == ord('q'):
			sys.exit()
		(text_w, text_h), _ = cv2.getTextSize(str(int(timer)), cv2.FONT_HERSHEY_PLAIN, 6, 4)
		bg[425-text_h-6:425+4, 710:710+text_w] = (0,0,0)
    
		timer = time.time() - initialTime
		down = 3-int(timer)
		# cv2.putText(bg, str(int(timer)), (625, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
		cv2.putText(bg, str(int(down)), (710, 425), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
		# print("timer:"+str(int(timer)))
		cv2.imshow('Tic_Tac_Toe',bg)

		if timer<3:
			key = cv2.waitKey(1)
			if key == ord('q'):
				sys.exit()
			
			cnt = 0
			_, img = video.read()
			
		
			img = cv2.flip(img, 1)
			
			hand = detector.findHands(img, draw=False)
			# print("0 up")
			if len(hand)>=1:
				lmlist = hand[0]
				
				if lmlist:
					fingerup = detector.fingersUp(lmlist)
					if fingerup == [0, 1, 0, 0, 0]:
						print("1 up")
						cnt=1
					if fingerup == [0, 1, 1, 0, 0]:
						print("2 up")
						cnt=2
					if fingerup == [0, 1, 1, 1, 0]:
						print("3 up")
						cnt=3
					if fingerup == [0, 1, 1, 1, 1]:
						print("4 up")
						cnt=4
					if fingerup == [1, 1, 1, 1, 1]:
						print("5 up")
						cnt = 5
				if len(hand)==2:
					# Checks if two hands
					lmlist2 = hand[1]			
					if lmlist2:
						fingerup = detector.fingersUp(lmlist2)
						if fingerup == [0, 1, 0, 0, 0]:
							print("1 up------------")
							cnt += 1
						if fingerup == [0, 1, 1, 0, 0]:
							print("2 up------------")
							cnt += 2
						if fingerup == [0, 1, 1, 1, 0]:
							print("3 up------------")
							cnt += 3
						if fingerup == [0, 1, 1, 1, 1]:
							print("4 up------------")
							cnt += 4
						if fingerup == [1, 1, 1, 1, 1]:
							print("5 up------------") 
							cnt += 5

			cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

			cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

			cv2.resizeWindow("Video", 525, 456)
			cv2.imshow("Video", img)

			cv2.moveWindow("Video", 21,128) 
			# print("----------------- "+str(cnt)+"-------------------")
			if cv2.waitKey(1) & 0xFF == ord('p'):
				break

		else:
			# Prints the final value to return the number of fingers
			print("THE FINAL VALUE = "+str(cnt)+"")
			break	

	return cnt

