# Pre-requisites

## Testbed

We're using the always-on DevNet sandboxes in the `testbed.yaml` file. More information about DevNet sandboxes here:

> http://devnetsandbox.cisco.com/RM/Topology

We will be using XE and XR sandboxes for the exercices attached. Feel free to use others.

## Dependances

To install the right packages, please run the command below:

```
pip install -r requirements.txt
```

## Supporter Python versions

You can find the list of supported Python versions for pyATS here:

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/prereqs/prerequisites.html

# Exercices

## 0. Get CLI show command output

In the first exercice, we will connect to the device and get an unstructued show command output (ex: `show ip interface brief`).

### Output example

```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES other  up                    up    
GigabitEthernet2       unassigned      YES NVRAM  administratively down down  
GigabitEthernet3       unassigned      YES NVRAM  up                    up    
Loopback11             1.2.3.1         YES other  up                    up  
```

### Complete instructions

[Complete instructions can be found here](0_get_cli_show/README.md)

## 1. Get structured show command output

In the second exercice, we will leverage Genie parsers to get a structured output (JSON). Complete list of interfaces.

### Output example

```
Loopback333 -- 3.3.3.3
Loopback99 -- 99.99.99.99
Loopback11 -- 1.2.3.1
GigabitEthernet2 -- Unassigned
GigabitEthernet1 -- 10.10.20.48
GigabitEthernet3 -- Unassigned
```

### Complete instructions

[Complete instructions can be found here](1_structured_output/README.md)

### Genie parsers documentation

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

## 2. Get structured show command output for multiple OS (XE and XR)

In the third exercice, we will connect on multiple devices of the same testbed. They are running different OS (XE and XR). We will see that we can get the same structured output with the same line of code.

### Output example

```
-----------------------------------
-- Connected on device: csr1000v --
-----------------------------------
Loopback333 -- 3.3.3.3
Loopback99 -- 99.99.99.99
Loopback11 -- 1.2.3.1
GigabitEthernet2 -- Unassigned
GigabitEthernet1 -- 10.10.20.48
GigabitEthernet3 -- Unassigned

-----------------------------------
-- Connected on device: iosxr1 --
-----------------------------------
Loopback200 -- 1.1.1.200
Loopback100 -- 1.1.1.100
GigabitEthernet0/0/0/1 -- Unassigned
GigabitEthernet0/0/0/0 -- Unassigned
MgmtEth0/RP0/CPU0/0 -- 10.10.20.175
Null0 -- Unassigned
```

### Complete instructions

[Complete instructions can be found here](2_multi_os/README.md)

### Genie supported models list

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models

## 3. Diff between two config files

In this fourth exercice, we will connect on the CSR1000v sandbox. We will `learn` the configuration of the device, and save it in two files.

We will manually modify one of them, and use the `Diff` capability of Genie to print the change.

### Output example

```
 interface Loopback2345:
- description Added via python Antoine script: 
+ description Added via python RESTCONF script: 
+ ip address 2.3.4.5 255.255.255.255: 
- ip address 2.3.4.6 255.255.255.255: 
```

### Learning the configuration of a device

To learn the configuration of a device, the below command can be used:

```python
device.learn('config')
```

### Complete instructions

[Complete instructions can be found here](3_config_diff/README.md)

### Genie diff documentation

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff

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

### Complete instructions

[Complete instructions can be found here](4_aetest/README.md)

### AEtest documentation

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html

# pyATS documentation

## Official documentation

pyATS documentation can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/getting_started/index.html

## List of supported platforms

The list of supported platforms can be found here:

> https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/supported_platforms.html

## Typical errors

Below a list of errors I encountered and the resolution. The list is not aimed to be exhaustive.

### Testbed file is not in the folder of execution

```
! output omitted
pyats.utils.yaml.exceptions.LoadError: Content of 'testbed.yaml' failed to load into a dict.
```

### Hostname and testbed mismatch

The name of the device in your testbed, and the hostname MUST match. It's case sensitive.

```
unicon.core.errors.TimeoutError: timeout occurred:
```

Otherwise, you can also set the `learn_hostname` argument to `True`.

```python
device.connect(learn_hostname=True)
```

More information in the documentation below:

> https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/connection.html

### Don't print the default commands

Don't print the `show version`, `show running-configuration` and the output.

```python
device.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)
```

### device.learn('platform')

`platform.os` has the following values for IOSXE and IOSXR:

- `iosxe` >> lower case
- `IOSXR` >> upper case

### diconnect() quickly

To avoid waiting ~10 seconds to disconnect on the device, you can edit your `testbed.yaml` file as such:

```yaml
    connections:
      cli:
        protocol: telnet
        ip: 10.1.1.1
        settings:
          GRACEFUL_DISCONNECT_WAIT_SEC: 0
          POST_DISCONNECT_WAIT_SEC: 0
```

More info here:

> https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/connection.html

### Parsing an already saved output

If you already have an output, and don't want to reconnect to the device to parse it, you can!

```python
output = device.execute('<show command>')
device.parse('<show command>', output=output)
```
