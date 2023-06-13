# New module! Now using genie!
from genie.testbed import load

testbed = load("./testbed.yaml")
cat8000v = testbed.devices["Cat8000V"]

# Connect to the device

# Step 0: showing the output in the terminal output

# Step 1: For each interface, give the interface name + IP address

# Disconnect from the device
cat8000v.disconnect()
