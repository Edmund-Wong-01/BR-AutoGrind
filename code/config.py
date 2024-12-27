# Configuration file for settings and parameters

# RGB values with tolerance
TOOL_RGB_TOLERANCE = 5
THROTTLE_RED_RGB = (255, 0, 0)  # Throttle red RGB value

# Pixel positions (x, y)
drivePos = (100, 200)  # Example positions
loadConsistPos = (150, 250)
consistPos = (200, 300)
continuePos = (250, 350)
mainRoutePortion = (300, 400, 100, 100)  # (x, y, width, height)
secondaryRoutePortion = (400, 500, 100, 100)
distancePortion = (500, 600, 100, 50)
currentSpeedPortion = (600, 700, 100, 50)
speedLimitPortion = (700, 800, 100, 50)
throttleRedPos = (800, 900)

# Control parameters
accelRate = 0.5  # m/s²
deccelRate = 1.0  # m/s²
trainLength = 200  # meters
trainTopSpeed = 100  # kph
creepForwardFromBrakeSec = 2  # seconds
