# SFC PAYGo Solar Credit Repayment

[![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

It is estimated that 592 million people in Africa are living without access to electricity. Most of these people live
outside of urban centers, and therefore out of reach of the continent’s electricity grid. And as many of us have
experienced, the existing systems in many African countries even struggle to supply enough energy to the homes and
businesses that are on the grid.

Pay-as-you-go (PAYGo) solar technology has become Africa’s most promising approach to handling the continent’s growing
energy problems. PAYGo users pay a small downpayment for a solar kit that provides up to eight hours of emission-free
lighting every day, as well as enough energy to charge mobile phones and other devices. With PayGo solar, residents are
able to reduce their energy spending by up to 50%.

PAYGo is a pioneering, game-changing credit system that removes the initial financial barrier to solar energy access by
allowing consumers to make a series of modest payments to purchase time units (or tokens) for using solar electricity
instead of paying upfront for the entire solar lighting system. After the payments are complete, the customer then owns
the solar power device, which they can use at no additional cost.

The objective of this challenge is to help predict the next six months of payments for different customers. This will
allow PAYGo distributors to provide appropriate services and customer support, ensuring that they can continue to
provide these important devices affordably and efficiently to the benefit of people all over Africa.

<i>Follow the instructions listed below to get started with the setup of this project on your local system.</i>

### Requirements

You need `Python 3.9` to run the project to avoid any package resolution issues.  
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

* Next up, we need to extract data files and save the processed files to the `./data/processed/` directory. For that run
  the following command in the terminal,
    * Instructions/ information will be given once you run the following script
    ```bash
    ./process_data.sh
    ```
