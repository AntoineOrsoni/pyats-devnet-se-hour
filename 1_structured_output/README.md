# 1. Get structured show command output

In the second exercice, we will leverage Genie parsers to get a structured output (JSON). Complete list of interfaces.

## Output example

```
Loopback333 -- 3.3.3.3
Loopback99 -- 99.99.99.99
Loopback11 -- 1.2.3.1
GigabitEthernet2 -- Unassigned
GigabitEthernet1 -- 10.10.20.48
GigabitEthernet3 -- Unassigned
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps

**Please note that we are now using the `Genie` library!**

The testbed is already loaded for you. Fore more information about the `topology.loader.load()` API, please refer to the documentation below:

https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file

The `connect()` method is explained here:

https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

Don't print the `show version`, `show running-configuration` and the output.

```python
device.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)
```

### Step 0

Use the `parse()` method on the `csr1000v` object to get a structured output of the `show ip interface brief` command. Save it to a variable.

Documentation can be found here:

https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/explore.html?highlight=parse#

Available parsers can be found here:

https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

### Step 1

Use a loop to iterate through your list of `interfaces`. Print each interface name and its IP address. Refer to the output example, above.