from pyats.topology import loader
import os

# Loading device information. 
# Take the testbed file in the same directory where the python file is executed.
testbed = loader.load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))
csr1000v = testbed.devices["csr1000v"]

# Connect to the device
csr1000v.connect()

# Step 0: saving the `show interface brief` output in a variable

# Step 1: pritting the `show interface brief` output
