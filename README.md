# PHSX815_Project3
## Electricity Use Analysis in my apartment.
In this experiment we simulated the electricity consumption using parabolic distribution for given difference in outside temperature and the temperature set on thermostat.
- The main code is in the folder python. Which is named as ElectricityUse.py.
- We can simulate the data using 
- python3 ElectricityUse.py -npar <number of paramters> -Nexp <number of experiments> -Nmeas <number of measurements> -seed <seed for random numbers> -output <name of output file>. This code also utilize the Random.py to simulate random parabolic distribution for the range of x value and provided temperature as parameter. It calculates the temperature and save the calculated temperature and true temperature in two separate files. 
- The code that reads the the data and plot the final histograms is analyzer.py 
- We can run this using python3 analyzer.py (you need to set the number of experiment , parameters and name of output files in the code)
