# Python BINlist
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/86eb561a4ca74b038b058bc12e8e0409)](https://www.codacy.com/app/PatDuJour/python-binlist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PatDuJour/python-binlist&amp;utm_campaign=Badge_Grade)

The Python BIN-list library provides convinent PCI compliant methods to lookup credit card BIN/IIN to help you 
understand your credit card charges by enriching your customer's card data while maintaing (outside of) PCI compliance.
It includes a pre-defined set of classes that represents Card Issuing Networks(American Express, Visa, etc.) with the most up-to-date
pulished IIN rules.


## Installation
BINlist is distributed on PyPI. The best way to install it is with pip:

`pip install binlist`

If you want to contribute and need access to the source code, then install from source with:

`python setup.py install`

## Requirements
* Python 2.7+ or Python 3.4+ 

## Usage
```
from binlist import BIN

# lookup card number's issuing network
BIN("5454").lookup()
```

## Development
Show help message:

`make help`

Run tests the default Python

`make test`

Run all tests on all supported Python versions:

`make test-all`

Run linter(flake8) with

`make lint`

