# New module! Now using genie!
from genie.testbed import load

testbed = load("./testbed.yaml")
cat8000v = testbed.devices["Cat8000V"]

# Connect to the device
cat8000v.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

# Step 0: showing the output in the terminal output
show_interface = cat8000v.parse("show ip interface brief")

# Step 1: For each interface, give the interface name + IP address
for interface in show_interface["interface"]:
    ip = show_interface["interface"][interface]["ip_address"]
    print(f"{interface} -- {ip}")

# Disconnect from the device
cat8000v.disconnect()
