import cv2
import math
import argparse

def DetectarRostro(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes

def preparar_rostro():
    parser=argparse.ArgumentParser()
    parser.add_argument('--image')
    args=parser.parse_args()

    modelo_cara1="opencv_face_detector.pbtxt" 
    modelo_cara2="opencv_face_detector_uint8.pb"
    modelo_edad1="age_deploy.prototxt"
    modelo_edad2="age_net.caffemodel"

    MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)

    Lista_edades=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(20-30)', '(30-45)', '(45-60)', '(60-100)']

    red_rostro=cv2.dnn.readNet(modelo_cara2,modelo_cara1)
    red_edad=cv2.dnn.readNet(modelo_edad2,modelo_edad1)

    video=cv2.VideoCapture(args.image if args.image else 0)
    padding=20
    while cv2.waitKey(1)<0:
        hasFrame,frame=video.read()
    #if not hasFrame:
        #cv2.waitKey()
        #break

        resultImg,faceBoxes=DetectarRostro(red_rostro,frame)

        for faceBox in faceBoxes:
            rostro=frame[max(0,faceBox[1]-padding):
                min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                :min(faceBox[2]+padding, frame.shape[1]-1)]

            edad_blob=cv2.dnn.blobFromImage(rostro, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            red_edad.setInput(edad_blob)
            predict_edad=red_edad.forward()
            Edad=Lista_edades[predict_edad[0].argmax()]

            cv2.putText(resultImg, f'{Edad}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
            cv2.imshow("Detector Edad", resultImg)