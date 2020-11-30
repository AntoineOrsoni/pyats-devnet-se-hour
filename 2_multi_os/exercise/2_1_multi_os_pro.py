# New module! Now using genie!
from genie.testbed import load
import os

# Loading device information
# Take the testbed file in the same directory where the python file is executed.
testbed = load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))

# Step 0: Looping for all devices in the testbed

# Step 1: Connect on the device and print its name

# Step 2: Listing interfaces and IP addresses

# Step 2 - Bonus: What if the key 'ipv4' doesn't exist (= no assigned IPv4)?

# Step 3: Disconnect from the device