from email.mime import image
import cv2
import os

from PIL import Image
import pickle as pc
import numpy as np

from colorama import init, Fore

class RecognitionMethods:
    def __init__(self):
        self.IMAGE_DIR = "images/"
        self.NATIVE_CAMERA = 0
        self.AUXILIAR_CAMERA = 1

    def image_filter_by_folder(self):
        dir_image_main = os.listdir(self.IMAGE_DIR)

        for varFile in dir_image_main:
            output_images_path = self.IMAGE_DIR + varFile + "/output_image_filter_"+varFile
            if not os.path.exists(output_images_path):
                os.makedirs(output_images_path)
                print(Fore.GREEN + "created directory: " + output_images_path)

            origin_image_path = self.IMAGE_DIR + varFile + "/origin_image"
            if not os.path.exists(origin_image_path):
                os.makedirs(origin_image_path)
                print(Fore.GREEN + "created directory: " + origin_image_path)

            origin_image_list = os.listdir(origin_image_path)

            for image_file in origin_image_list:
                if image_file.split(".")[-1] not in ["jpg", "png", "jpeg"]:
                    continue

                image_path = origin_image_path + "/"+image_file
                image = cv2.imread(image_path)

                if image is None:
                    print(Fore.RED + "image is None")
                    continue

                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)

                cv2.imwrite(output_images_path + "/" +
                            "withFilter_" + image_file, image)
        print(Fore.GREEN + "DataSet Renderizado Con Exito.")

    def fit(self):
        cascade_classifier = cv2.CascadeClassifier(
            'cascades/haarcascade_frontalface_alt2.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_position = -1
        x_train = []
        y_train = []
        labels = {}

        dir_image_main = os.listdir(self.IMAGE_DIR)
        for varFile in dir_image_main:
            output_image_list = os.listdir(
                self.IMAGE_DIR + varFile + "/output_image_filter_"+varFile)
            for image_file in output_image_list:
                if image_file.endswith('jpg') or image_file.endswith('png') or image_file.endswith('gif') or image_file.endswith('jpeg'):

                    path = self.IMAGE_DIR + varFile + "/output_image_filter_"+varFile + "/" + image_file
                    label = os.path.basename(varFile).replace(' ', '').upper()

                    if label not in labels:
                        current_position += 1
                        labels[label] = current_position

                    image_pil = Image.open(path).convert('L')
                    image_bytes = image_pil.resize((500, 500), Image.ANTIALIAS)

                    image_np = np.array(image_bytes, 'uint8')

                    face_detector = cascade_classifier.detectMultiScale(
                        image_np, scaleFactor=1.5, minNeighbors=8)
                    for (x, y, width, height) in face_detector:
                        roi = image_np[y: y + height, x: x + width]
                        x_train.append(roi)
                        y_train.append(current_position)
        # Serializamos
        with open('pickles/face-labels.pickle', 'wb') as file:
            pc.dump(labels, file)

        recognizer.train(x_train, np.array(y_train))
        recognizer.save('training/face-training.yml')

        print(Fore.GREEN + "Entrenamiento Finalizados.")

    def predict(self, camera=0):
        cascade_classifier = cv2.CascadeClassifier(
            'cascades/haarcascade_frontalface_alt2.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()

        recognizer.read('training/face-training.yml')

        labels = {}

        with open('pickles/face-labels.pickle', 'rb') as file:
            labels_bytes = pc.load(file)
            labels = {value: key for key, value in labels_bytes.items()}

        catcher = cv2.VideoCapture(camera)
        font = cv2.QT_FONT_DEMIBOLD
        color_line = (255, 0, 0)
        stroke = 1

        while (True):
            state, frame = catcher.read()
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_detector = cascade_classifier.detectMultiScale(
                gray_scale, scaleFactor=1.5, minNeighbors=8)
            for (x, y, width, height) in face_detector:
                roi = gray_scale[y: y + height, x: x + width]
                label_position, accuracy = recognizer.predict(roi)
                if accuracy >= 80 and accuracy <= 100:
                    name = labels[label_position]
                    cv2.putText(frame, name, (x, y), font, stroke, (0, 0, 255))
                cv2.rectangle(frame, (x, y), ((x + width), (y + height)), color_line, stroke)
            cv2.imshow('Detector Facial Casero', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        cv2.destroyAllWindows()