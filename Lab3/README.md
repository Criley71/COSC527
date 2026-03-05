# Set Up

First make and activate the virtual environment, then install requirements.
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


# Required Packages
The requirements are listed and installable via the requirements.txt file but if a technical issue arises the needed packages are:
```
matplotlib==3.10.8
numpy==2.4.2
```

# Usage
Its a Jupyter Notebook file so the kernel may need to be selected but the project should be able to be ran fully now. The user will be asked for input to set the bipolar vector size, number of patterns and number of experiemental runs. Leaving the input empty will set the values to 100, 50 and 5 respectively.