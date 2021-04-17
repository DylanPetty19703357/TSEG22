import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import csv

#//PLEASE READ//
#This program looks for a file in the same directory named 'sample.ogg'
#and requires a premade csv file in the same directory in order to print results

#note current use of csv print has no use in providing csv that can be fed in to ml, for now copy paste data in to another csv
#-----------------------------------------------------------------------------------------------------------------------------

#Load file
FilePath = "sample.ogg"
AudioSample, sr= librosa.load(FilePath)

#Number of samples in file
AudioSample.size
print("Number of samples in the audio signal is:", AudioSample.size," samples")

#Duration of each sample
AudioSample_SampleDuration = 1/sr
print(f"Duration of each sample is: {AudioSample_SampleDuration:.6f} Seconds")

#Duration of file
AudioSample_Duration = AudioSample_SampleDuration * AudioSample.size
print(f"Duration of audio signal is: {AudioSample_Duration:.2f} Seconds")

#Set size
FrameLength = 1024
HopLength = 512

#Calculate amplitude for each frame
def amplitude_envelope(Audio_Signal, FrameLength, HopLength):
    amplitude_envelope = []
    for i in range(0, len(Audio_Signal), HopLength):
        Current_Frame_AE = max(Audio_Signal[i:i+FrameLength])
        amplitude_envelope.append(Current_Frame_AE)
        
    return np.array(amplitude_envelope)

#Calculate Root-Mean Square energy
def root_mean_square(AudioSample, FrameLength, HopLength):
	root_mean_square = []
	for i in range(0, len(AudioSample), HopLength):
		Current_Frame_RMS = np.sqrt(np.sum(AudioSample[i:i+FrameLength]**2) / FrameLength)
		root_mean_square.append(Current_Frame_RMS)
	
	return np.array(root_mean_square)

#Calculate Zero-Crossing Rate

#___________________________________________________________

#Calling each function
AE_AudioSample = amplitude_envelope(AudioSample, FrameLength, HopLength)#Amplitude envelope/AE
len(AE_AudioSample)

RMS_AudioSample = root_mean_square(AudioSample, FrameLength, HopLength)#Root Mean Square energy/RMSe
RMS_AudioSample.shape

ZCR_AudioSample = librosa.feature.zero_crossing_rate(AudioSample, FrameLength, HopLength)[0]#Zero Crossing Rate/ZCR

#Plot audio signal of file and amplitude envelope
frames = range(0, AE_AudioSample.size)
t = librosa.frames_to_time(frames, hop_length = HopLength)

plt.figure(figsize=(15, 15))
plt.subplot(3, 1, 1)
librosa.display.waveplot(AudioSample, alpha = 0.5)
plt.plot(t, AE_AudioSample, color = "r")
plt.ylim((-1, 1))

#Plot audio signal of file and Root-Mean Square energy
frames = range(0, RMS_AudioSample.size)

plt.figure(figsize=(15, 15))
plt.subplot(3, 1, 1)
librosa.display.waveplot(AudioSample, alpha = 0.5)
plt.plot(t, RMS_AudioSample, color = "r")
plt.ylim((-1, 1))

#Plot audio signal of file and Zero Crossing Rate
frames = range(0, ZCR_AudioSample.size)

plt.figure(figsize=(15, 15))
plt.subplot(3, 1, 1)
librosa.display.waveplot(AudioSample, alpha = 0.5)
plt.plot(t, ZCR_AudioSample, color = "r")
plt.ylim((0, 1))

#Output each feature as suitable value
AE_AudioSample = np.mean(AE_AudioSample)
AE_AudioSample = round(AE_AudioSample, 6)
print("\nAmplitude Envelope =", AE_AudioSample)

RMS_AudioSample = np.mean(RMS_AudioSample)
RMS_AudioSample = round(RMS_AudioSample, 6)
print("Root-Mean Square energy =", RMS_AudioSample)

Min_ZCR_AudioSample = np.min(ZCR_AudioSample)
Max_ZCR_AudioSample = np.max(ZCR_AudioSample)
Min_ZCR_AudioSample = round(Min_ZCR_AudioSample, 6)
Max_ZCR_AudioSample = round(Max_ZCR_AudioSample, 6)
print("Minimum Zero Crossing Rate Minimum =", Min_ZCR_AudioSample)
print("Maximum Zero Crossing Rate =", Max_ZCR_AudioSample)

#Print Values to suitable CSV format
file = open('extract_audio_features.csv')
csv_reader = csv.reader(file)
next(csv_reader, None)
with open('extract_audio_features.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	
	#writer.writerow(['AE', 'RMS', 'ZCR', 'Target'])
	writer.writerow([AE_AudioSample, RMS_AudioSample, Min_ZCR_AudioSample, Max_ZCR_AudioSample])

plt.show()

