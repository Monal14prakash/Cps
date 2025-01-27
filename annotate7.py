import cv2
img_path='capturedimg.jpg'
cam=cv2.VideoCapture(0)
def capture_image():
    print("capturing image..")
    ret,frame=cam.read()
    cam.release()
    cv2.destroyAllWindows()
    if ret:
        cv2.imwrite(img_path,frame)
        print("image saved at",img_path)
        return frame
    else:
        print("image not captured!")
        return None
    
def annotate_image(frame):
    print("annotating image...")
    if frame is None:
        print("image not available to annotate")
        return
    height,width,_=frame.shape
    print("height:",height)
    print("width:",width)
    start=(100,100)
    end=(400,400)
    cv2.rectangle(frame,start,end,(0,255,0),3)
    cv2.putText(frame,"ROI",(start[0],start[1]-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow("annotated image",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

frame=capture_image()
annotate_image(frame)

