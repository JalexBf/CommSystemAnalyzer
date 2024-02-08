Those repositoty provides tools for analyzing PAM systems and generating PPM signals.


PAM_analysis.py
Includes functionality for calculating the required signal-to-noise ratio (SNR) for a given PAM system, plotting the relationship between SNR and the order of the PAM system,

PPM_generator.py
Includes functionality for generating PPM signals for a given name encoded in binary ASCII format.

PPM_test.py
Unit tests for the PPM_generator.


Author: 
	Jason Alexander Karafotias
	

Github repository:
	https://github.com/JalexBf/CommSystemAnalyzer.git


Prerequisites:
	-Python 3.6 or later
	-Necessary libraries: numpy, scipy and matplotlib


Use:
	For the SNR calculation and plotting:
	
		python PAM_analysis.py
	
	
	For the PPM signal generator:
	
		python PPM_generator.py
	
	
