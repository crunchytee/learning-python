import sys

# Prints out the arguments passed when the file is run
# Example: python sys_example.py arg1
# Results: args: ["filename", "arg1"]
# arguments = sys.argv

#Split off the filename - the first argument is always the filename
arguments = sys.argv[1:]
print(f"We received these args: {arguments}")
print(f"we're currently running on a {sys.platform} machine")