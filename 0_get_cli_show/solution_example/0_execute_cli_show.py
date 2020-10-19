from pyats.topology import loader
import os

# Loading device information. 
# Take the testbed file in the same directory where the python file is executed.
testbed = loader.load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))
csr1000v = testbed.devices["csr1000v"]

# Connect to the device
csr1000v.connect()

# Step 0: showing the output in the terminal output
csr1000v.execute('show ip interface brief')

# Step 1: saving the output in a variable
show_interface = csr1000v.execute('show ip interface brief')
print(show_interface)