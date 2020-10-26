# import the aetest module
from pyats import aetest
import logging
import os

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    
    @aetest.subsection
    def connect_to_devices(self, testbed):
        
        for device in testbed:
            # don't do the default show version
            # don't do the default config
            device.connect(init_exec_commands=[],
                           init_config_commands=[],
                           log_stdout=False)
            
            logger.info('{device} connected'.format(device=device.alias))

class CheckVersion(aetest.Testcase):

    @aetest.test
    def check_current_version(self, testbed):

        # Local vars
        test_success = True
        xe_version = '16.9.3'
        xr_version = '6.5.3'
        fail_devices = []

        for device in testbed:
            
            #Learning platform information
            platform = device.learn('platform')

            # We use .lower() so we're not case sensitive
            if (platform.os.lower() == 'iosxe' and platform.version != xe_version): 
                test_success = False
                fail_devices.append(device.alias)

            # We use .lower() so we're not case sensitive
            if (platform.os.lower() == 'iosxr' and platform.version != xr_version): 
                test_success = False
                fail_devices.append(device.alias)

            logger.debug('{device} running {platformos} has OS: {os}'.format(device=device.alias, platformos=platform.os, os=platform.version))

        # If we have devices with the wrong OS, print their names
        assert test_success == True, 'List of fail devices: {list}'.format(list=fail_devices)

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        
        for device in testbed:
            device.disconnect()

if __name__ == '__main__':

    # local imports
    from genie.testbed import load
    import sys

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.INFO)

    # Loading device information
    # Take the testbed file in the same directory where the python file is executed.
    testbed = load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))

    aetest.main(testbed = testbed)