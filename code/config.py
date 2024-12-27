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
