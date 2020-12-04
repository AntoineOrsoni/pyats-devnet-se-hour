from pyats.topology import loader
import os

# Step 0: load the testbed
cwd = cwd=os.path.dirname(__file__)

# If the python script is executed from the local directory, use local testbed
if cwd == '': testbed = loader.load(f'./testbed.yaml')
# Else, the python script is executed from another directory, use testbed in the folder of the script
else: testbed = loader.load(f'{cwd}/testbed.yaml')

# Step 1: testbed is a dictionnary. Extract the device csr1000v
csr1000v = testbed.devices["csr1000v"]

# Step2: Connect to the device
csr1000v.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

# Step 3: saving the `show interface brief` output in a variable
show_interface = csr1000v.execute('show ip interface brief')

# Step 4: pritting the `show interface brief` output
print(show_interface)

# Disconnect from the device
csr1000v.disconnect()