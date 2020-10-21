# Importing a new library!
from genie.utils.diff import Diff
import json
import os

# Step 0: Opening the two files
with open('{cwd}/config_modified.json'.format(cwd=os.path.dirname(__file__)), 'r') as config_file:
    config_modified = json.load(config_file)

with open('{cwd}/config_original.json'.format(cwd=os.path.dirname(__file__)), 'r') as config_file:
    config_original = json.load(config_file)

# Step 1: Printting the differences
dd = Diff(config_modified, config_original)
dd.findDiff()

print(dd)