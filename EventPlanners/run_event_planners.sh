#!/bin/bash

# Number of times to run the Python script
count=300

# Loop to run the script
for ((i=1; i<=$count; i++))
do
    echo "Running iteration $i"
    python event_planners.py
done
