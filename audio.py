import winsound
from winsound import Beep

def beep1():
    for i in range(1,11):
        Freq = i * 500  # Set Frequency To 2500 Hertzs
        Dur = 250 - (i + 10)  # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq, Dur)
        print "-" * i,

def march():
    Beep(440, 500)
    Beep(440, 500)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
    # Beep(659, 500)
    # Beep(659, 500)
    # Beep(659, 500)
    # Beep(698, 350)
    # Beep(523, 150)
    # Beep(415, 500)
    # Beep(349, 350)
    # Beep(523, 150)
    # Beep(440, 1000)