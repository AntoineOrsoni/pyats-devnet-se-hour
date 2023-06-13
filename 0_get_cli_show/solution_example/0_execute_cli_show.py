from pyats.topology import loader

# Step 0: load the testbed
testbed = loader.load(f"./testbed.yaml")

# Step 1: testbed.devices is a dictionary. Extract the device Cat8000v
cat8000v = testbed.devices["Cat8000V"]

# Step2: Connect to the device
cat8000v.connect(init_config_commands=[], log_stdout=False)

# Step 3: Save the `show ip interface brief` output in a variable
show_interface = cat8000v.execute("show ip interface brief")

# Step 4: Print the `show interface brief` output
print(show_interface)

# Step 5: Disconnect from the device
cat8000v.disconnect()
