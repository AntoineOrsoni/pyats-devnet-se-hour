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


# Exercices
## Get CLI show command output

In the first exercice, we will connect to the device and get an unstructued show command output (ex: `show ip interface brief`).

## GET structured show command output

In the second exercice, we will leverage Genie parsers to get a structured output (JSON). Complete list of Genie parsers can be found here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers



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

### Don't print the default commands

Don't print the `show version`, `show running-configuration` and the output.

```python
device.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)
```