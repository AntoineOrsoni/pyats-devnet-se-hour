# New module! Now using genie!
from genie.testbed import load
import os

# Loading device information
cwd = os.path.dirname(__file__)

# If the python script is executed from the local directory, use local testbed
if cwd == '': testbed = load(f'./testbed.yaml')
# Else, the python script is executed from another directory, use testbed in the folder of the script
else: testbed = load(f'{cwd}/testbed.yaml')

# Step 0: Looping for all devices in the testbed

# Step 1: Connect on the device and print its name

# Step 2: Listing interfaces and IP addresses

# Step 2 - Bonus: What if the key 'ipv4' doesn't exist (= no assigned IPv4)?

# Step 3: Disconnect from the device