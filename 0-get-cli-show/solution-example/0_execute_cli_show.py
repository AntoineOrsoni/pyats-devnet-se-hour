from pyats.topology import loader

# Loading device information
testbed = loader.load('testbed.yaml')
csr1000v = testbed.devices["csr1000v"]

# Connect to the device
csr1000v.connect()

# Step 0: showing the output in the terminal output
csr1000v.execute('show ip interface brief')

# Step 1: saving the output in a variable
show_interface = csr1000v.execute('show ip interface brief')
print(show_interface)