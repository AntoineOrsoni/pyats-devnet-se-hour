## 4. AEtest: Automated Easy Testing

In this fifth exercice, we will use AEtest to define and execute test cases. In our example, we will:

1. Connect to the devices (IOS XE, IOS XR),
2. Assert their current OS version,
3. Disconnect from the devices.

### Output example

```
2020-10-21T11:05:39: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:39: %AETEST-INFO: |                            Starting common setup                             |
2020-10-21T11:05:39: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:39: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:39: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2020-10-21T11:05:39: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:40: %SCRIPT-INFO: csr1000v connected
2020-10-21T11:05:42: %SCRIPT-INFO: iosxr1 connected
2020-10-21T11:05:42: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2020-10-21T11:05:42: %AETEST-INFO: The result of common setup is => PASSED
2020-10-21T11:05:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:42: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2020-10-21T11:05:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:05:42: %AETEST-INFO: |                    Starting section check_current_version                    |
2020-10-21T11:05:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:01: %AETEST-INFO: The result of section check_current_version is => PASSED
2020-10-21T11:06:01: %AETEST-INFO: The result of testcase CheckVersion is => PASSED
2020-10-21T11:06:01: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:01: %AETEST-INFO: |                           Starting common cleanup                            |
2020-10-21T11:06:01: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:01: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:01: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2020-10-21T11:06:01: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:27: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2020-10-21T11:06:27: %AETEST-INFO: The result of common cleanup is => PASSED
2020-10-21T11:06:27: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:27: %AETEST-INFO: |                               Detailed Results                               |
2020-10-21T11:06:27: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:27: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2020-10-21T11:06:27: %AETEST-INFO: --------------------------------------------------------------------------------
2020-10-21T11:06:27: %AETEST-INFO: .
2020-10-21T11:06:27: %AETEST-INFO: |-- common_setup                                                          PASSED
2020-10-21T11:06:27: %AETEST-INFO: |   `-- connect_to_devices                                                PASSED
2020-10-21T11:06:27: %AETEST-INFO: |-- CheckVersion                                                          PASSED
2020-10-21T11:06:27: %AETEST-INFO: |   `-- check_current_version                                             PASSED
2020-10-21T11:06:27: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2020-10-21T11:06:27: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2020-10-21T11:06:27: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:27: %AETEST-INFO: |                                   Summary                                    |
2020-10-21T11:06:27: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-10-21T11:06:27: %AETEST-INFO:  Number of ABORTED                                                            0 
2020-10-21T11:06:27: %AETEST-INFO:  Number of BLOCKED                                                            0 
2020-10-21T11:06:27: %AETEST-INFO:  Number of ERRORED                                                            0 
2020-10-21T11:06:27: %AETEST-INFO:  Number of FAILED                                                             0 
2020-10-21T11:06:27: %AETEST-INFO:  Number of PASSED                                                             3 
2020-10-21T11:06:27: %AETEST-INFO:  Number of PASSX                                                              0 
2020-10-21T11:06:27: %AETEST-INFO:  Number of SKIPPED                                                            0 
2020-10-21T11:06:27: %AETEST-INFO:  Total Number                                                                 3 
2020-10-21T11:06:27: %AETEST-INFO:  Success Rate                                                            100.0% 
2020-10-21T11:06:27: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

# Steps

**Please note that we are now using the `Genie` library!**

The testbed is already loaded for you. Fore more information about the `topology.loader.load()` API, please refer to the documentation below:

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file


The below arguments avoid pritting the `show version`, `show running-configuration` and the output.

```python
device.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)
```

To send information inline, in the ouput of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('csr1000v connected')`

```
2020-10-21T11:05:40: %SCRIPT-INFO: csr1000v connected
```

## Step 0

In the `CommonSetup` section, use a loop to `connect()` to each device of the testbed. Don't forget to remove the `pass`.

## Step 1

In this step, we will check the OS version of the devices in the testbed.
* XE should be `16.9.3`
* XR should be `6.5.3`

### Step 1.0

For each device in the testbed, we first need to learn about the platform information. You can use Genie. Refer to the documentation below:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/

### Step 1.1

Use a condition to check if the platform is XE or XR. Depending of the OS, check that the device has the right `os`.

For each device that passes the test, print a message such as `Device {name} passed. Running version {os}`. You can use `logger.info('Your message')` to do so.

### Step 1.2 - Bonus

Now, make the test fail. You could for instance change `xe_version` to something else (ex: `16.12.4`).
If the version is not compliant, use the `self.failed()` method to fail the test. 

```python
@aetest.test
def test(self):
    self.failed('This is a failure message')
```

### Step 1.3 - Bonus

What if the first device fails, but you want to test the others? Change your algo to all the devices are tested. At the end, fail the test if one of them is not compliant.

## Step 2

In the `CommonCleanup` section, use a loop to `disconnect()` to each device of the testbed. Don't forget to remove the `pass`.

# AEtest documentation

The AEtest documentation can be found below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html

## Main sections

AEtest is composed of 3 main sections:
* `CommonSetup` with Subsections
* `Testcases` with setup/tests/cleanup
* `CommonCleanup` with Subsections

`CommonSetup` is where all the common configurations, prerequisites and initializations shared between the script’s testcases should be performed.

`Testcase` is a container/collection of smaller tests. Testcases are the workhorse of every testscript, carrying out the assessments that determines the quality of the product under scrutiny.

`CommonCleanup` is the last section to run within each testscript. Any configurations, initializations and environment changes that occured during this script run should be cleaned up (removed) here.

More information about each part, in the documentation below:

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html

## AEtest python examples

Examples can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/examples.html#feature-usage

## Passing a test without checking

If your test is not yet coded, but you would like it to pass so your whole code doesn't fail, you can use `pass` as below. Anything below `pass` will not be executed. Once you have coded your test, do not forget to remove it.

```python
def connect_to_devices(self, testbed):
    pass
```