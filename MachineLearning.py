import pandas as pd
from tabulate import tabulate as tb
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing

import time
import librosa
import librosa.display
import numpy
import matplotlib.pyplot as spectoplot

### source = https://www.datacamp.com/community/tutorials/decision-tree-classification-python

FilePath = "sample.ogg" #Same file as this script
TimeSeries, SampleRate = librosa.load(FilePath)

# LIBROSA OUPUT #

def GetDuration():
    print("Duration of Song:", librosa.get_duration(TimeSeries, SampleRate))


def STFT():
    S = numpy.abs(librosa.stft(TimeSeries))
    print(S)
    fig, ax = spectoplot.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=numpy.max), y_axis='log', x_axis='time', ax=ax)

    ax.set_title('Short-time Fourier transformation spectogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    fig.show()


# MACHINE LEARNING #
def ML():

    # READS FILE

    with open(r"C:\Users\Student\Documents\Uni\Year 2\Team Software Engineering (CMP2804M)\Assessment 3\audio_features.csv") as f:

        data = pd.read_csv(f, header=0, encoding="utf-8-sig", engine="python")

        data.columns = [x.encode("utf-8").decode("ascii", "ignore") for x in data.columns]

        features = ['Genre', 'Amplitude Envelope', 'Root Square Mean', 'Min Zero Crossing Rate', 'Max Zero Crossing Rate']

        print(tb(data, headers=features))
        print()

    # SPLITS DATA INTO TESTING AND TRAINING DATA #

    X = data[features]

    Y = data.Genre

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

    print("X_test: ", X_test)
    #print("X_train:", X_train)
    #print("Y_test:", Y_test)
    #print("Y_train:", Y_train)

    # MACHINE LEARNING

    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)

    clf = clf.fit(X_train, Y_train)
    

    y_pred = clf.predict(X_test) 
    print(y_pred)

    print("Accuracy:", metrics.accuracy_score(Y_test, y_pred))


if __name__ == "__main__":
    #data = GetDuration()
    #print()
    #print("STFT:")
    #STFT()
    ML()




