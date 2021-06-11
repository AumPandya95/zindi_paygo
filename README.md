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

### Project Structure

```markdown
.
├── data
│   ├── metadata.csv
│   ├── SampleSubmission.csv
│   ├── Test.csv
│   ├── Train.csv
│   └── VariablesDefinition.txt
├── models
├── notebooks
│   ├── exploratory_data_analysis
│   │   └── eda.ipynb
│   └── StarterNotebook.ipynb
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── src
    ├── data
    │   └── __init__.py
    ├── features
    └── model
        └── __init__.py
```

### Requirements

You need `Python 3.9` to run the project to avoid any package resolution issues.  
You can have multiple Python versions (2.x and 3.x) installed on the same system.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

or you can build python from source by following steps listed on
[this](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/#installing-python-39-on-ubuntu-with-apt)
website. For CentOS, you can visit [this](https://computingforgeeks.com/install-latest-python-on-centos-linux/) website.

### Installation

* This project requires `pipenv` to install dependencies
  * Install `pipenv` using the following command for `Ubuntu`:
    ```bash
    sudo pip install pipenv
    ```
    
  * Install `pipenv` using the following command for `Windows`:
    ```bash
    pip install --user pipenv
    
    # Set Path | Replace "$user_name" with your user name
    set PATH=%PATH%;set PATH=%PATH%;'c:\users\$user_name\appdata\local\programs\python\python39-32\Scripts'
    ```
  
* In the sources root of the directory, run the following command to install dependencies from the `Pipfile.lock` file
  ```bash
  pipenv install --ignore-pipfile
  ```
* You can find the location of your specific python version by using this command (shown for python3.9)
    ```bash
    which python3.9
    ```

### Additional

* After activating the environment, if you want to locate the project,
    ```bash
    pipenv--where
    ```
* Locate the virtualenv,
    ```bash
    pipenv --venv
    ```
* Locate the Python interpreter,
  ```bash
  pipenv --py
   ```
* To activate this project's virtualenv, run the following,
  ```bash
  pipenv shell
  ```
* Install a dev dependency,
  ```bash
  pipenv install <package_name> --dev
  ```
* To run a jupyter notebook, run the following,
  ```bash
  pipenv run jupyter notebook
  ```

