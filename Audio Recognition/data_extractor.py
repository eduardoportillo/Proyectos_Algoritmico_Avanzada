"""
Importamos las librerias
"""
from hashlib import new
import math
from random import sample
import librosa
from librosa.feature.spectral import (
    chroma_stft,
    spectral_bandwidth,
    spectral_centroid,
    rms,
    spectral_rolloff,
    zero_crossing_rate,
    mfcc,
)

import numpy as np
import csv
import os
import matplotlib.pyplot as plt
from traitlets import default


class Extractor:

    def generate_csv(self):
        # Agregamos la primera fila del archivo que corresponde al encabezado
        header = [
            "chroma_stft",
            "rms",
            "spectral_centroid",
            "spectral_bandwith",
            "rollof",
            "zero_crossing_rate",
        ]

        valor = 5

        for index in range(1, 21):
            header.append(f"mfcc{index}")
        header.append("label")
        # Generaremos el archivo csv con la cabecera
        file = open("song_dataset.csv", "w", newline="\n")
        with file:
            writer = csv.writer(file)
            writer.writerow(header)
        # Recorremos la carpeta generos y para cada archivo presente extraermeos info
        for root, folders, files in os.walk("songs"):
            for audio in files:
                path = os.path.join(root, audio)
                y, sr = librosa.load(path)
                duration = librosa.get_duration(y=y, sr=sr)
                sections = int(duration - 4)

                for section in range(sections):
                    data_x, sample_rate = librosa.load(
                        path, mono=True, offset=section, duration=valor)
                    chroma = chroma_stft(data_x, sr=sample_rate)
                    root_mean = rms(data_x)
                    centroid = spectral_centroid(data_x, sr=sample_rate)
                    bandwith = spectral_bandwidth(data_x, sr=sample_rate)
                    rollof = spectral_rolloff(data_x, sr=sample_rate)
                    zero_crossing = zero_crossing_rate(data_x)
                    mel_coef = mfcc(data_x, sr=sample_rate)
                    row = [
                        np.mean(chroma),
                        np.mean(root_mean),
                        np.mean(centroid),
                        np.mean(bandwith),
                        np.mean(rollof),
                        np.mean(zero_crossing),
                    ]
                    # Agregamos los coeficientes de MEL al arreglo
                    for coef in mel_coef:
                        row.append(np.mean(coef))
                    # Agregamos la etiqueta a la cual pertenece el audio estudiado
                    row.append(audio.split(".")[0])
                    file = open("song_dataset.csv", "a+", newline="\n")
                    with file:
                        writer = csv.writer(file)
                        writer.writerow(row)

    def extract_data_from_audio(self, path):

        valor = 5

        data_x, sample_rate = librosa.load(path, mono=True, duration=valor+1)
        chroma = chroma_stft(data_x, sr=sample_rate)
        root_mean = rms(data_x)
        centroid = spectral_centroid(data_x, sr=sample_rate)
        bandwith = spectral_bandwidth(data_x, sr=sample_rate)
        rollof = spectral_rolloff(data_x, sr=sample_rate)
        zero_crossing = zero_crossing_rate(data_x)
        mel_coef = mfcc(data_x, sr=sample_rate)
        data = [
            np.mean(chroma),
            np.mean(root_mean),
            np.mean(centroid),
            np.mean(bandwith),
            np.mean(rollof),
            np.mean(zero_crossing),
        ]
        # Agregamos los coeficientes de MEL al arreglo
        for coef in mel_coef:
            data.append(np.mean(coef))
        return data
