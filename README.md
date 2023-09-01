# Utility Expenses Keeper
Monthly utility bookkeeping tool written in Python (Cli + GUI version). 
By default, this tool records the following entries as row in a csv file:
* Date
* Rent
* Parking
* Electricity
* Water
* Gas
* Internet
* Total

Each month's expenses will be appended and updated to the same csv file if you run the script again.

## Dependencies
0. `cd` into the directory
1. create and use virtual environment (optional) by typing the following in your terminal:
```bash
python -m venv .venv # Windows
python3 -m venv .venv #macOS/Linux
source .venv/bin/activate
```
2. install dependencies by typing the following in your terminal once inside venv:
```bash
pip -r requirements.txt
```

## Usage
Note that both version will generate an expenses.csv in local directory. If you wish to append future bill to the same csv, please do not delete as it will be read and then appended. 

### CLI version
1. run [bill_gen_cli.py](bill_gen_cli.py) by
```bash
python bill_gen_cli.py
```
2. follow the prompt to input your individual expense
3. Once finished, total amount and summary will be displayed. Your expense will be saved as a csv file inside of current directory.

### GUI version
0. Python [Tkinter](https://docs.python.org/3/library/tkinter.html) packages is required. On Windows, it is included when you installed Python. Here's how to install on [MacOs](https://www.geeksforgeeks.org/how-to-install-tkinter-on-macos/) and [Linux/Deb-based-distro](https://www.pythonguis.com/installation/install-tkinter-linux/).
1. run [bill_gen_gui.py](bill_gen_gui.py) by
```bash
python bill_gen_cli.py
```
2. input your expenses on the GUI
3. Once finished, your total expense will be calculated and expense will be saved as csv to local directory.