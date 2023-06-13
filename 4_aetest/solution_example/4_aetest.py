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
            device.connect(init_config_commands=[], log_stdout=False)

            logger.info(f"{device.alias} connected")


class CheckVersion(aetest.Testcase):
    @aetest.test
    def check_current_version(self, testbed):
        # Local vars
        test_success = True
        xe_version = "17.9.2a"
        xr_version = "7.3.2"
        fail_devices = []

        for device in testbed:
            # Learning platform information
            platform = device.learn("platform")

            # We use .lower() so we're not case-sensitive
            if platform.os.lower() == "iosxe" and platform.version != xe_version:
                test_success = False
                fail_devices.append(device.alias)

            # We use .lower() so we're not case-sensitive
            if platform.os.lower() == "iosxr" and platform.version != xr_version:
                test_success = False
                fail_devices.append(device.alias)

            logger.debug(
                f"{device.alias} running {platform.os} has OS: {platform.version}"
            )

        # If we have devices with the wrong OS, print their names
        assert test_success == True, f"List of fail devices: {fail_devices}"


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        for device in testbed:
            device.disconnect()


if __name__ == "__main__":
    # local imports
    from genie.testbed import load
    import sys

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.INFO)

    testbed = load(f"./testbed.yaml")

    aetest.main(testbed=testbed)
