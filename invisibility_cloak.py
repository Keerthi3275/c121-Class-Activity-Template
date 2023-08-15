

#To save the output in a file output.avi

#Starting the webcam


#Allowing the webcam to start by making the code sleep for 2 seconds


#Capturing background for 60 frames

#Flipping the background


#Reading the captured frame until the camera is open
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Flipping the image for consistency
    

    #Converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Generating mask to detect red colour(values can be changed)
    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask_1 = mask_1 + mask_2

    cv2.imshow("mask_1", mask_1)


    #Open and expand the image where there is mask 1 (color)
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    #Selecting only the part that does not have mask one and saving in mask 2
    mask_2 = cv2.bitwise_not(mask_1)

    #Keeping only the part of the images without the red color 
    #(or any other color you may choose)
    res_1 = cv2.bitwise_and(img, img, mask=mask_2)

    #Keeping only the part of the images with the red color
    res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)

    #Generating the final output by merging res_1 and res_2
    
    #Displaying the output to the user
   



