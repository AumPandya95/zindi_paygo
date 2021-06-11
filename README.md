# SFC PAYGo Solar Credit Repayment
[![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

The objective of this competition was to provide methods for automatically detecting abnormal energy consumption in buildings.

<i>Follow the instructions listed below to get started with the setup of this project on your local system.</i>

### Requirements
You need Python 3.5 or later, preferably `Python 3.9` to run the project to avoid any package resolution issues.  
You can have multiple Python versions (2.x and 3.x) installed on the same system.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

or you can build python from source by following steps listed on 
[this](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/#installing-python-39-on-ubuntu-with-apt) 
website. For CentOS, you can visit [this](https://computingforgeeks.com/install-latest-python-on-centos-linux/) website.

### Installation
* Create a virtual environment and activate the same
    ```bash
    virtualenv -p python3.9 venv
    source venv/bin/activate
    ```
* Specify the python location in place of `python3.9`.
* You can find the location of your specific python version by using this command (shown for python3.9)
    ```bash
    which python3.9
    ```

### Setup
* After activating the environment, update setuptools and install the requirements for the project,
    ```bash
    pip install -U setuptools
    pip install -r requirements.txt
    ```
* Run the following command to make shell scripts executable,
    ```bash
    chmod -x process_data.sh
    ```

### Data Setup
* Next up, we need to extract data files and save the processed files to the `./data/processed/` directory. For that
run the following command in the terminal,
    * Instructions/ information will be given once you run the following script
    ```bash
    ./process_data.sh
    ```
