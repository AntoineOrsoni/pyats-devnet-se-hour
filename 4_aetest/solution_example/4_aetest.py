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

        for device in testbed:
            
            # Checking the current version of the device
            platform = device.learn('platform')

            if platform.os == 'iosxe': assert platform.version == '16.9.3'
            elif platform.os == 'iosxr': assert platform.version == '6.5.3'

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