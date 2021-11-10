from pyats.topology import loader

# Step 0: load the testbed
testbed = loader.load(f'./testbed.yaml')

# Step 1: testbed is a dictionnary. Extract the device csr1000v
csr1000v = testbed.devices["csr1000v-1"]

# Step2: Connect to the device
csr1000v.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

# Step 3: saving the `show ip interface brief` output in a variable
show_interface = csr1000v.execute('show ip interface brief')

# Step 4: pritting the `show interface brief` output
print(show_interface)

# Disconnect from the device
csr1000v.disconnect()