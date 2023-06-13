# New module! Now using genie!
from genie.testbed import load

testbed = load(f"testbed.yaml")

# Step 0: Looping through each device in the testbed
for device in testbed:
    # Step 1: Connect on the device and print its name
    device.connect(init_config_commands=[], log_stdout=False)

    print("-----------------------------------")
    print(f"-- Connected on device: {device.name} --")
    print("-----------------------------------")

    # Step 2: Listing interfaces and IP addresses
    show_interface = device.parse("show ip interface brief")

    for interface in show_interface["interface"]:
        ip = show_interface["interface"][interface]["ip_address"]
        print(f"{interface} -- {ip}")

    print("")

    # Step 3: Disconnect from the device
    device.disconnect()
