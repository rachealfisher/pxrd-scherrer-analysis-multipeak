# -*- coding: utf-8 -*-
"""
Author: Racheal Fisher
"""
#import programs
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import math

# Create figure
plt.figure(figsize=(3,3), dpi=300)

# Create lists angle and intensity
angle = []
intensity = []

# Open file and read data
file = open('Audrey.txt')
data = file.readlines()
file.close()

# Divide text data into two lists, angle and intensity
for line in data[151:]:
    split = line.strip().split(',')
    angle.append(float(split[0]))
    intensity.append(float(split[1]))

# Find peaks in the intensity data. Adjust prominence to get more or less peaks.
peaks, _ = find_peaks(intensity, prominence=3)
print(peaks)

CrystalliteSizes = [] 

# Label Peaks
peakIndex = 0
for peak in peaks:
    peakAngle = angle[peak]
    peakIntensity = intensity[peak]
    print(peakIndex, peakAngle, peakIntensity)
    
    # Plot a dot at the peak's location
    plt.plot(peakAngle, peakIntensity, marker = "o", markersize=3, color="red",)
    
    # Add a label with the peak index near the point
    plt.annotate(peakIndex, (peakAngle, peakIntensity), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color="red")

    peakIndex += 1

# Create the figure
plt.plot(angle, intensity)
# Add x and y labels
plt.ylabel("Intensity (a.u.)")
plt.xlabel("2*theta (degrees)")

plt.show()

# Ask the user for peaks to remove
removePeaks = input("Which peaks would you like to remove? Please enter as a number with one space in between each peak. Recommended: noisy peaks.:")
print("\n")
peaksList = removePeaks.split()
print(peaksList)
# Add peaks to be removed to a list
selectedPeaks = []
for item in peaksList:
     peak = peaks[int(item)]
     selectedPeaks.append(peak)
print(selectedPeaks)

# Remove undesired peaks
keptPeaks = [x for x in peaks if x not in selectedPeaks]
print(keptPeaks)
oldpeaks = peaks
peaks = keptPeaks


for peak in peaks:
    ## Finding FWHM
    #Find half max peak intensity
    HalfMaxPeakIntensity = intensity[peak]/2
    print("peak:", list(oldpeaks).index(peak))
    print("Half Max Peak Intensity", HalfMaxPeakIntensity)

    #Find the x-intercepts
    x_intercepts = []  # To store the x-intercept angles
    peakAngle = angle[peak]

    # Iterate through the data to find x-intercepts
    for i in range(len(angle) - 1):
        if (intensity[i] - HalfMaxPeakIntensity) * (intensity[i + 1] - HalfMaxPeakIntensity) < 0:
            # Crossed the threshold between i and i+1
            x_intercept = angle[i] + (angle[i + 1] - angle[i]) * (HalfMaxPeakIntensity - intensity[i]) / (intensity[i + 1] - intensity[i])
            x_intercepts.append(x_intercept)
    
    #isolate only the x-intercepts of that peak
    target_value = peakAngle
    sorted_list = sorted(x_intercepts, key=lambda x: abs(target_value - x))
 
    intercept1 = sorted_list[0]
    intercept2 = sorted_list[1]
    
    x_intercepts = []
 
    print("intercepts", intercept1,intercept2)
    # print(f"X-intercepts for y = {HalfMaxPeakIntensity}: {x_intercepts}")

    #Full width at half maximum
    FWHM_angle = abs(intercept2 - intercept1)
    print('FWHM in angles', FWHM_angle)
    #Convert to radians
    FWHM = math.radians(FWHM_angle)
    print('FWHM in radians', FWHM)
    
    ##Create other scherrer variables
    #lambda = x-ray wavelength (nm)
    My_lambda = .154
    K = .89
    Bragg_angle = peakAngle
    print('peakAngle:', peakAngle)

    #Calculate the particle size in nm w/ Scherrer eqn.
    D = (K*My_lambda)/(FWHM*(math.cos(math.radians(Bragg_angle))))
    print("Average crystallite size:", D)
    
    CrystalliteSizes.append(D)

print("Total average:", sum(CrystalliteSizes)/len(CrystalliteSizes))


plt.savefig('Audrey.png')
plt.show()




""