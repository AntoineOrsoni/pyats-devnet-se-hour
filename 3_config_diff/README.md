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

## File 0

**There is no work to be done in this file. It's mostly what we've done in the previous part.**

The file 0 will get the configuration from the device, and save it into two files:
* `config_original.json` which contains the original (unchanged) configuration.
* `config_modified.json` which contains the modified configuration. A changed has already been made. Feel free to add more.

### Learning the configuration of a device

To learn the configuration of a device, the below command can be used:

```python
device.learn('config')
```

## File 1

### Step 0

Open the two files, in `read` mode. The documentation can be found here:

> https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

For each of them, save its output in a variable. As-is, these two variables will be type `_io.TextIOWrapper`. Use the `json` library to transform them to `dict`. The documentation can be found here:

> https://docs.python.org/3/library/json.html

Hint: method to be used is `json.load()` (because we're a loading a file). If we were loading a **s**tring, methold would be `json.loads()` (with an `s`).

### Step 1

Use Genie `Diff` documentation to print the differences between the two dictionnaries: `config_original` and `config_modified`. It can be found here:

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff