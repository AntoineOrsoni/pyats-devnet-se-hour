# New module! Now using genie!
from genie.testbed import load
import os

# Loading device information
# Take the testbed file in the same directory where the python file is executed.
testbed = load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))

# Step 0: Looping for all devices in the testbed
for device in testbed:

    print('')

    # Step 1: Connect on the device and print its name
    device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
    
    print('-----------------------------------')
    print('-- Connected on device: {device} --'.format(device=device.alias))
    print('-----------------------------------')

    # Step 2: Listing interfaces and IP addresses
    show_interface = device.learn('interface')

    for interface, info in show_interface.info.items():

        # Step 2: What if the key 'ipv4' doesn't exist (= no assigned IPv4)?
        if 'ipv4' in info:
            for ip, value in info['ipv4'].items():
                print('{interface} -- {ip}'.format(interface=interface, ip=value['ip']))
        else:
            print('{interface} -- Unassigned'.format(interface=interface))
    
    print('')

    # Step 3: Disconnect from the device
    device.disconnect()