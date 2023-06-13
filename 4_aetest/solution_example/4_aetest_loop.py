# import the aetest module
from pyats import aetest
import logging
import os

logger = logging.getLogger(__name__)


class CommonSetup(aetest.CommonSetup):
    # Mark the subsection to loop over a list of static devices
    @aetest.loop(device_name=["Cat8000V", "iosxr1"])
    @aetest.subsection
    def connect_to_devices(self, device_name):
        device = testbed.devices[device_name]
        device.connect(init_config_commands=[], log_stdout=False)
        logger.info(f"{device.alias} connected")


class CheckVersion(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        # Mark dynamically the test function to loop over the devices in the testbed
        aetest.loop.mark(
            self.check_current_version, device=list(testbed.devices.values())
        )

    @aetest.test
    def check_current_version(self, device):
        # Local vars
        xe_version = "17.9.2a"
        xr_version = "7.3.2"

        # Learning platform information
        platform = device.learn("platform")
        expected_version = None

        # We use .lower() so we're not case-sensitive
        if platform.os.lower() == "iosxe":
            expected_version = xe_version

        # We use .lower() so we're not case-sensitive
        if platform.os.lower() == "iosxr":
            expected_version = xr_version

        logger.debug(f"{device.alias} ({platform.os}) is in version {platform.version}")
        if platform.version != expected_version:
            self.failed(
                f"{device.alias} ({platform.os}) has an unexpected version: {platform.version} (expected: {expected_version})"
            )


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        # Disconnect all devices from testbed
        testbed.disconnect()


if __name__ == "__main__":
    # local imports
    from genie.testbed import load
    import sys

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.DEBUG)

    testbed = load(f"testbed.yaml")

    aetest.main(testbed=testbed)
