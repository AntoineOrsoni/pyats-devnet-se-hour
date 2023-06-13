# New module! Now using genie!
from genie.testbed import load
import os

testbed = load(f'testbed.yaml')

# Step 0: Looping for all devices in the testbed

    # Step 1: Connect on the device and print its name

    # Step 2: Listing interfaces and IP addresses

    # Step 2 - Verify that the 'ipv4' key exist (= no assigned IPv4)?

    # Step 2 Bonus - Print unassigned if the key 'ipv4' doesn't exist

    # Step 3: Disconnect from the device