# 1. Get structured show command output

In the second exercise, we will leverage Genie parsers to get a structured output (JSON) of a list of interfaces.

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

The loader is now testbed loader is now imported from the Genie library. 

The testbed and devices objects returned by the loader are the sames as with the pyATS. However, additional methods are added by Genie.

### Step 0

Use the `parse()` method on the `cat8000v` object to get a structured output of the `show ip interface brief` command. Save it to a variable.

Documentation can be found here:

> https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/explore.html?highlight=parse#

Available parsers can be found here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

### Step 1

Use a loop to iterate through your list of `interfaces`. Print each interface name and its IP address. Refer to the output example, above.

*You may print the parsed output first in order to understand the structure of the return object.*

You can also find the schema of the return object in the genie documentation

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers/show%2520ip%2520interface%2520brief%2520%257Binterface%257D