# Virtual Enviroment Setup \& Installing Dependencies

## Prerequisites
|Packages  |Version|
|----------|-------|
|`python3` | 3.11+ |
|`pip`     | 23.0+ |
|`venv`    | 3.11+ |

### Installing the prerequisites
- On Debian-based distributions:
 
`$ apt install python3 python3-pip python3-venv`
 
- On Windows:
    - Use the Microsoft Store to download Python **or**
    - Download the 'Full Installer' from 
    [python.org](https://www.python.org/downloads)
        - To ensure `pip` is installed, run the following command on your 
        prefered terminal emulator:  
    `C:> py -m ensurepip --upgrade`  
    *For more information on installing `pip` on Windows follow this [link](https://pip.pypa.io/en/stable/installation/)*

## Setup `venv`
- On Linux-based machines:
    - Open up a terminal emulator and run:  
    `$ python3 -m venv venv/`
    - After `venv` is done with setting up your virtual enviroment, run the 
    following command to install the required packages for the Qiskit SDK:  
    `$ python3 -m pip install -r requirements.txt`
- On Windows machines:
    - Open up a terminal emulator and run:  
    `C:> py -m pip install -r requirements.txt`
