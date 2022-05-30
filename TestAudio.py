#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pydub import AudioSegment
from pydub.playback import play
import time
import random
background = AudioSegment.from_file("194235__cosmician__background-noise-jet-city-birds.wav") #your first audio file
birds = AudioSegment.from_file("416529__inspectorj__bird-whistling-single-robin-a.wav") #your second audio file
car = AudioSegment.from_file("522222__nox-sound__car-passby-exterior-mono.wav") #your third audio file
cat = AudioSegment.from_file("415209__inspectorj__cat-screaming-a.wav")
pBirds = 5
pCar = 10


backDuration = len(background)
numAppearencesBirds = backDuration % pBirds
numAppearencesCar = backDuration % pCar

print(backDuration)
print(numAppearencesBirds)
print(numAppearencesCar)

mixed = background

for i in range(numAppearencesBirds):
    
    startIndex = random.randint(0,backDuration)
    panRandom = random.uniform(-1,1)
    
    mixed = mixed.overlay(birds.pan(panRandom), position = startIndex )

for i in range(numAppearencesCar):
    
    startIndex = random.randint(0,backDuration)
    
    car = car.fade(from_gain=-120.0, start=0, duration=2000)
    car = car.fade(to_gain=-120.0, end=0, duration=2000)
    car = car.apply_gain(-6)
    
    mixed = mixed.overlay(car, position = startIndex)

startIndex = random.randint(0,backDuration)
panRandom = random.uniform(-1,1)
cat = cat.apply_gain(-10)
mixed = mixed.overlay(cat.pan(panRandom), position = startIndex)

mixed.export("mixed.wav", format = 'wav')


# In[ ]:




