# 0. Get CLI show command output

In the first exercice, we will connect to the device and get an unstructued show command output (ex: `show ip interface brief`).

## Output example

```
show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES other  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  up                    up      
Loopback11             1.2.3.1         YES other  up  
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps

The testbed is already loaded for you. Fore more information about the `topology.loader.load()` API, please refer to the documentation below:

https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file

The `connect()` method is explained here:

https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

### Step 0

Use the `execute()` method on the `csr1000v` object to send a CLI command to the device. Get the `show interface brief` output, and save it in a variable.

More information about the `execute()` method here:

https://pubhub.devnetcloud.com/media/pyats/docs/apidoc/connections/index.html#module-pyats.connections.bases

### Step 1

Print the output.