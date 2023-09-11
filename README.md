# pxrd-scherrer-analysis-multipeak

## Usage
1. Save the PXRD output as a text file, and move into the same directory as this program (or include directory in next step.)
2. Replace `Audrey.txt` in line 18 with the name of your text file.
3. Replace `Audrey.png` in line 136 with the name you would like to save your figure under.
4. When you run the program, `peaks, _ = find_peaks(intensity, prominence=3)` will detect the peaks present in your code. Modifying the prominence will change the number of peaks detected.
5. When you run the program, a figure will appear with the peaks in your code labeled with numbers. You will be prompted to list the codes you would like to exclude from your analysis. Exclude all noisy or overlapping peaks for a better analysis. Indicate peaks to be excluded by typing the number corresponding to each peak with a space in between.

## Output
The code will give the analysis for each peak as it iterates through them, and then an average size at the end. The units of the crystallite size are nm. For each peak, it will display average crystal size, FWHM, x-intercepts, and Bragg angle. The total average size will only display size in nm. 

## Errors
If you are getting a sherrer analysis indicating a size that is unexpected, especially overly large, look through the individual peak outputs. One or two of the peaks may be giving innacurate sizes due to noise. Rerun the code removing those peaks, and see if your result is more accurate. 

Otherwise contact me and I will fix:) ty