# New module! Now using genie!
from genie.testbed import load
import os
import json

# Loading device information
cwd = os.path.dirname(__file__)

# If the python script is executed from the local directory, use local testbed
if cwd == '': testbed = load(f'./testbed.yaml')
# Else, the python script is executed from another directory, use testbed in the folder of the script
else: testbed = load(f'{cwd}/testbed.yaml')

# Looping for all devices in the testbed
for device in testbed:

    print('')

    device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

    # Step 0: Saying on which device we are currently connected
    print('-----------------------------------')
    print('-- Connected on device: {device} --'.format(device=device.alias))
    print('-----------------------------------')

    config = device.learn('config')

    # Step 1: Open the targeted file
    with open('{cwd}/config_modified.json'.format(cwd=os.path.dirname(__file__)), 'w') as config_file:

        # Step 2: Write the config
        json.dump(config, config_file, indent=4)
        print('config_modified of {device} has been written!'.format(device=device.alias))   

    # Step 3: Do the same operation for 
    with open('{cwd}/config_original.json'.format(cwd=os.path.dirname(__file__)), 'w') as config_file:

        json.dump(config, config_file, indent=4)
        print('config_original of {device} has been written!'.format(device=device.alias))  

    # Step 4: Disconnect from the device
    device.disconnect()