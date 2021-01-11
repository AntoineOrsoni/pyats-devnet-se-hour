# 0. Get CLI show command output

In the first exercice, we will connect to the device and get an unstructued show command output (ex: `show ip interface brief`).

## Output example

```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES other  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  up                    up      
Loopback11             1.2.3.1         YES other  up                    up
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps

### Step 0

Load the testbed. Use the `loader.load()` API. Fore more information about the `topology.loader.load()` API, please refer to the documentation below:

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file

### Step 1

A `testbed` is a `pyats.topology.testbed.Testbed` object. It has a `devices` attribute, which is a dictionnary of all devices in the testbed. 
* Try to print it.
* Extract the `csr1000v` device. 

### Step 2

Connect to the device. Use the `connect()` method to do so. It's explained here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

The below arguments avoid pritting the `show version`, `show running-configuration` and the output.

```python
device.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)
```

### Step 3

Use the `execute()` method on the `csr1000v` object to send a CLI command to the device. Get the `show interface brief` output, and save it in a variable.

More information about the `execute()` method here:

> https://pubhub.devnetcloud.com/media/pyats/docs/apidoc/connections/index.html#module-pyats.connections.bases

### Step 4

Print the output.