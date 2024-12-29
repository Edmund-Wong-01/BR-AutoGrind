# Configurations and customizable settings

# RGB Tolerance
RGB_TOLERANCE = 5

# Pixel positions
DrivePos = (x1, y1)
LoadConsistPos = (x2, y2)
ConsistPos = (x3, y3)
ContinuePos = (x4, y4)
ThrottleRedPos = (x5, y5)
AWSWarningPos = (x6, y6)

DESTINATION_PORTION = (100, 200, 300, 400)  # (x, y, width, height)

# Screen portion for routes
ROUTE_PORTION = (500, 200, 300, 400)  # (x, y, width, height)

# Spacing between occurrences of "mins"
MINS_SPACING = 30  # Adjust based on your screen layout

# Sleep time between actions
SLEEP_TIME = 1  # seconds

# Define pixel positions for various actions
drivePos = (100, 150)          # Coordinates for Drive button
loadConsistPos = (200, 150)   # Coordinates for Load Consist button
consistPos = (300, 150)       # Coordinates for Consist button
continuePos = (400, 150)      # Coordinates for Continue button
throttleRedPos = (500, 150)   # Coordinates for Throttle Red indicator
throttleRedRGB = (255, 0, 0)  # RGB values for the Throttle Red indicator

# Screenshot portions
# Start at top left corner, adjust width and height for screenshot size
MainRoutePortion = (x_start, y_start, width, height)
SecondaryRoutePortion = (x_start2, y_start2, width2, height2)
DistancePortion = (x_start3, y_start3, width3, height3)
CurrentSpeedPortion = (x_start4, y_start4, width4, height4)
SpeedLimitPortion = (x_start5, y_start5, width5, height5)

# Train specifications
# Find at BR Wiki for that train (currently set to class 800)
AccelRate = 0.7 # m/s²
DecelRate = 1.2 # m/s²
TrainLength = 132.0  # meters
TrainTopSpeed = 201 # kph
# Maximum throttle and brake values
MAX_THROTTLE = 100  # Maximum throttle level (0-100)
MAX_BRAKE = 100     # Maximum brake level (0-100)

# Acceleration and deceleration rates (units per second)
accelRate = 5       # Rate at which the train accelerates (units/s)
decelRate = 10      # Rate at which the train decelerates (units/s)
