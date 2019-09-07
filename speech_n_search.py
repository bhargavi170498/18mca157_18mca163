# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:01:36 2019

@author: HP
"""

import speech_recognition as sr
import matplotlib.pyplot as plt
import sounddevice as sd
import webbrowser

sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=1000
Fs=16000;
d=2;

with sr.Microphone() as source:
    print('Speak!')
    audio=r.listen(source)
    audio1=sd.rec(int(d*Fs),Fs,1)
    sd.wait()
    try:
        plt.plot(audio1)
        text=r.recognize_google(audio)
        print("You said: {}".format(text))
        url='https://www.google.co.in/search?q='
        search=url+text
        webbrowser.open(search)
        
    except:
        print("Can't Recognize! ")