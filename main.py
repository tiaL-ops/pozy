import cv2

cam= cv2.VideoCapture(0)

frame_wifth= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height= int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


#codec?? coder-decoder
fourcc= cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_wifth, frame_height))


while True:
    ret, frame = cam.read()

    out.write(frame)

    cv2.imshow('Camera',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.realease()
out.release()
cv2.destroyAllWindows()