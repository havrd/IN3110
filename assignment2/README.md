# README.md Assignment2 

## Task 2.1

### Prerequisites

Both source and destination directory must exist

### Functionality

Move files from one directory to another

### Missing Functionality

Moves all files, cannot decide which files to move

### Usage

./move \<source directory\> \<destination directory\>

## Task 2.2 & 2.3

### Prerequisites

~/.local/share directory must exist

### Functionality

Can start, name and stop tasks which will be timed

### Missing Functionality

Can not have multiple running tasks in parallel

### Usage

source ./track.sh

    To start tracking a new task, enter:            'track start <label>' 
    To finish tracking current task, enter:         'track stop'
    To get info on current task, enter:             'track status'
    To see time used on all previous tasks, enter:  'track log'
