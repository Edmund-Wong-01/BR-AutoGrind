# config.py

# Positions
awsWarningPos = (100, 200)  # Example coordinates

# Delays
creepForwardFromBrakeSec = 1  # Time to creep forward after braking

# RGB Values
throttleRedRGB = (255, 0, 0)  # Example RGB value
rgbTolerance = 10  
# Rates
decelRate = 1.2  

# Lengths
trainLength = 132  # Length of the train in meters

# Throttle and Brake Steps
throttleSteps = 7  # Steps from OFF (0) to FULL (6)
brakeSteps = 4     # Steps from OFF (0) to MAX (4)

# Portions for screenshots. X, Y, Width, Height 
distancePortion = (100, 100, 200, 200)  
currentSpeedPortion = (200, 200, 200, 200)
speedLimitPortion = (300, 300, 200, 200)

# Spacing
minsSpacing = 10  # Vertical spacing value between destination (menu.py)