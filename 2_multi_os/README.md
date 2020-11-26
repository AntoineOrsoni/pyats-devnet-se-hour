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

## File 0 - Noob version

On this first file, for each device in the testbed, we are going to use a Genie Parser to get the IP address on all interfaces.

### Step 0

Create a loop: we are going to print details for each `device` in the `testbed`.

### Step 1

Use the `connect()` method to connect on the device. See the above documentation. The `connect()` method is explained here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

Use one of the device attribute to print the name of the device.

### Step 2

Use Genie Parser to parse `show ip interface brief` command. Parsers allows you to parse show commands into structured output (JSON/Dictionary).

Navigate through the dictionnary. Extract each interface name, and its IP address.

Genie `parse()` method documentation can be found here:

> https://developer.cisco.com/docs/genie-docs/

Genie available parsers can be found here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models

## File 1 - Pro version

### Step 0 Step 1

You can reuse the code you did for `File 0`.

### Step 1

You can reuse the code you did for `File 0`.

### Step 2

Instead of learning a few cli at the time, you can learn the whole feature and have it into 1 structured output (JSON/Dictionary). This structure is agnostic between all OS (i.e. identical between all the OS).

You can read about the Genie `parse()` method here:

> https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/explore.html?highlight=genie%20testbed#learn-devices-features-into-structured-output

You can find all Genie supported models here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models

### Step 2 - Bonus

What if the key `ipv4` doesn't exist (no assigned IPv4 address). For such interface, print `unassigned` instead of the empty address.