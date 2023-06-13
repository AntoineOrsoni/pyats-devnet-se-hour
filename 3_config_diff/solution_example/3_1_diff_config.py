# Importing a new library!
from genie.utils.diff import Diff
import json

# Step 0: Opening the two files
with open("./config_modified.json", "r") as config_file:
    config_modified = json.load(config_file)

with open("./config_original.json", "r") as config_file:
    config_original = json.load(config_file)

# Step 1: Printing the differences
dd = Diff(config_original, config_modified)
dd.findDiff()

print(dd)
