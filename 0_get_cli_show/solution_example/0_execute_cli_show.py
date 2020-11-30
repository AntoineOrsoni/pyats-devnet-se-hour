from pyats.topology import loader
import os

# Loading device information. 
# Take the testbed file in the same directory where the python file is executed.
testbed = loader.load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))
csr1000v = testbed.devices["csr1000v"]

# Connect to the device
csr1000v.connect(init_exec_commands=[],
                init_config_commands=[],
                log_stdout=False)

# Step 0: saving the `show interface brief` output in a variable
show_interface = csr1000v.execute('show ip interface brief')

# Step 1: pritting the `show interface brief` output
print(show_interface)