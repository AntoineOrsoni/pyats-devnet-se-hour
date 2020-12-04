# import the aetest module
from pyats import aetest
import logging
import os

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    
    # Step 0: Use a loop to `connect()` to each device in the testbed.
    # Don't forget to remove the `pass`
    @aetest.subsection
    def connect_to_devices(self, testbed):
        pass

class CheckVersion(aetest.Testcase):

    # Step 1: Check the OS of the device.
    # xe should be 16.9.3
    # xr should be 6.5.3
    # Don't forget to remove the `pass`
    @aetest.test
    def check_current_version(self, testbed):

        # Local vars
        xe_version = '16.9.3'
        xr_version = '6.5.3'

        for device in testbed:
            pass 

            # Step 1.0: Learning platform information

            # Step 1.1: If the device is XE, check that its version complies with `xe_version`
            #           If the device is XR, check that its version complies with `xr_version`

            # Step 1.2 - Bonus: Change the `xe_version` to something else. 
            #                   If version is not compliant, fail the test

            # Step 1.3 - Bonus: What if the first device fails, but you want to test the others?
            #            Change your algo to all the devices are tested. At the end, fail the test if 
            #            one of them is not compliant.        

        
class CommonCleanup(aetest.CommonCleanup):

    # Step 2: Use a loop to `disconnect()` from each device in the testbed.
    # Don't forget to remove the `pass`
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        pass

if __name__ == '__main__':

    # local imports
    from genie.testbed import load
    import sys

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.INFO)

    # Loading device information
    cwd = os.path.dirname(__file__)

    # If the python script is executed from the local directory, use local testbed
    if cwd == '': testbed = load(f'./testbed.yaml')
    # Else, the python script is executed from another directory, use testbed in the folder of the script
    else: testbed = load(f'{cwd}/testbed.yaml')

    aetest.main(testbed = testbed)