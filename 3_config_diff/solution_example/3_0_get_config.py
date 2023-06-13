# New module! Now using genie!
from genie.testbed import load
import os
import json

testbed = load(f"testbed.yaml")

# Looping for all devices in the testbed
for device in testbed:
    device.connect(init_config_commands=[], log_stdout=False)

    # Step 0: Saying on which device we are currently connected
    print("-----------------------------------")
    print(f"-- Connected on device: {device.alias} --")
    print("-----------------------------------")

    config = device.learn("config")

    # Step 1: Open the targeted file
    with open("config_modified.json", "w") as config_file:
        # Step 2: Write the config
        json.dump(config, config_file, indent=4)
        print(f"config_modified of {device.alias} has been written!")

    # Step 3: Do the same operation for
    with open("config_original.json", "w") as config_file:
        json.dump(config, config_file, indent=4)
        print(f"config_original of {device.alias} has been written!")

    # Step 4: Disconnect from the device
    device.disconnect()
