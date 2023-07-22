#!/usr/bin/python3

import sys
import os

# Add the parent directory (which contains the 'models' package) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.engine.file_storage import FileStorage

# Instantiate the FileStorage class
storage = FileStorage()

# Load data from the JSON file
storage.reload()

# Now you can use 'storage' to access the data from the storage engine
# For example:
states = storage.all('State')
for state_id, state in states.items():
    print(state_id, state.name)

