# New module! Now using genie!
from genie.testbed import load
import os

# Loading device information
# Take the testbed file in the same directory where the python file is executed.
testbed = load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))

# Step 0: Looping through each device in the testbed

# Step 1: Connect on the device and print its name

# Step 2: Listing interfaces and IP addresses.

# Step 3: Disconnect from the device