from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from data_extractor import Extractor
from tkinter import Tk
from  tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

extractor = Extractor()

# extractor.generate_csv()

Tk().withdraw()
song = askopenfilename()


test_data = extractor.extract_data_from_audio(song)

df = pd.read_csv("song_dataset.csv")
x = df.drop("label", axis=1)
labels = df.label.unique()
y = df.label.map(
    {
        "Sin-Bandera-Ahora-Se": 0,
        "Sin-Bandera-Cuando-Te-Vuelva-a-Ver": 1,
        "Sin-Bandera-Cuando-Ya-No-Te-Esperaba": 2,
        "Sin-Bandera-Dime-Que-Si": 3,
        "Sin-Bandera-En-Esta-No": 4,
        "Sin-Bandera-Entra-En-Mi-Vida": 5,
        "Sin-Bandera-Kilometros": 6,
        "Sin-Bandera-Mientes-Tan-Bien": 7,
        "Sin-Bandera-No-Veo-La-Hora": 8,
        "Sin-Bandera-Para-Siempre-Tal-Vez": 9,
        "Sin-Bandera-Que-Lloro": 10,
        "Sin-Bandera-Que-Me-Alcance-La-Vida": 11,
        "Sin-Bandera-Sera": 12,
        "Sin-Bandera-Si-Tu-No-Estas": 13,
        "Sin-Bandera-Suelta-Mi-Mano": 14,
        "Sin-Bandera-Te-Vi-Venir": 15,
        "Sin-Bandera-Ves": 16,
        "Sin-Bandera-y-llegaste-tu-sin-bandera": 17,
        "Sin-Bandera-Y-No-Fue-Suficiente": 18,
    }
)

classifier = RandomForestClassifier()
classifier.fit(x, y)
predicted = classifier.predict([test_data])
# print(labels[predicted[0]])

showinfo("Prediction", labels[predicted[0]])

