# New module! Now using genie!
from genie.testbed import load

testbed = load(f"testbed.yaml")

# Step 0: Looping for all devices in the testbed
for device in testbed:
    # Step 1: Connect on the device and print its name
    device.connect(init_config_commands=[], log_stdout=False)

    print("-----------------------------------")
    print(f"-- Connected on device: {device.alias} --")
    print("-----------------------------------")

    # Step 2: Listing interfaces and IP addresses
    show_interface = device.learn("interface")

    for interface, info in show_interface.info.items():
        # Step 2 - Verify that the  'ipv4' key exist (= no assigned IPv4)?
        if "ipv4" in info:
            for ip, value in info["ipv4"].items():
                print(f'{interface} -- {value["ip"]}')
        # Step 2 Bonus - Print unassigned if the key 'ipv4' doesn't exist
        else:
            print(f"{interface} -- unassigned")

    print("")

    # Step 3: Disconnect from the device
    device.disconnect()
