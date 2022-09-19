# README.md Assignment4

## Task 4.1 & 4.2

### Prerequisites

See dependecies in requirements.txt

### Functionality

Can apply greyscale and sepia filter to an image. The sepia filter can be applied in varying intensity

### Missing Functionality

1. Hardcoded filename for image
2. All .txt files are manually tested and written

### Usage

Run .py programs using python3

example:
>python3 python_color2grey.py

## Task 4.3 & 4.4 & 4.5

### Prerequisites

See dependecies in requirements.txt

### Functionality

Can apply greyscale and sepia filter to an image. The sepia filter can be applied in varying intensity

### Missing Functionality

No automated reports

### Usage

Inside the top directory i.e. Assignment4, run:
>pip install instapy/

Then you can run 'instapy' as a command in bash with the following flags:

    -h, --help: helpful message showing flags and usage of instapy
    -f FILE, --file FILE: The filename of file to apply filter to
    -se, --sepia: Select sepia filter
    -st STEP, --step STEP: Intensity of sepia-filter, from 0.0-1.0
    -r, --runtime: Prints average runtime of chosen implementation over three runs, defaults to numpy
    -g, --gray: Select gray filter
    -sc SCALE, --scale SCALE: Scale factor to resize image
    -i {python, numba, numpy}, --implement{python, numba, numpy}: Choose the implementation
    -o OUT, --out OUT: The output filename

Tests can be run using the command 'pytest'. Make sure to be located in the top directory where 'test_instapy.py' is.
