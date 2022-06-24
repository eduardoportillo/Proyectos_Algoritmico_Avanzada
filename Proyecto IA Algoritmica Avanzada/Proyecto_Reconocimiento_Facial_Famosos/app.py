from recognition_methods import RecognitionMethods
from colorama import init, Fore, Style

recognizer = RecognitionMethods()
while True:
    print(Fore.YELLOW + "Oprime el numero de la Opción deseada:")
    print("1.- Renderizar dataset.")
    print("2.- Entrenar Modelo.")
    print("3.- Que el modelo te diga a que famoso Te pareces.")
    print("4.- Salir.")
    in_key = input()
    
    if in_key.isnumeric():
        in_key=int(in_key)
        if in_key == 1:
            recognizer.image_filter_by_folder()
        if in_key == 2:
            recognizer.fit()
        if in_key == 3:
            recognizer.predict()
        if in_key == 4:
            quit()
    else:
        print(Fore.RED + "Ingrese un numero.")