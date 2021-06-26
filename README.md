# FedPy
## _Everything Federal Reserve Related_

Open source python package for seamlessly extracting data 
related to Federal Reserve and integrating for your own use.

Depending on the data you're trying to access FedPy will
return a `pandas DataFrame` or a `Dictionary`.

## Installation
Install using pip:


```sh
pip install FedPy
```

## Basic Usage
```
import FedPy
soma_bill_holdings = FedPy.soma_hist()
soma_bill_holdings.tail()
```
##### This returns:

```
Date        MBS           CMBS        ...    Notes & Bonds  Bills         Agencies      Total
2021-05-05  2.181449e+12  9.876134e+09  ...  4306171560100  326044000000  2.347000e+09  7.185813e+12
2021-05-12  2.181449e+12  9.876134e+09  ...  4315773560100  326044000000  2.347000e+09  7.199017e+12
2021-05-19  2.267736e+12  9.825699e+09  ...  4331310560100  326044000000  2.347000e+09  7.301989e+12
2021-05-26  2.234442e+12  9.823153e+09  ...  4343914560100  326044000000  2.347000e+09  7.283298e+12
2021-06-02  2.234447e+12  9.823153e+09  ...  4375118560100  326044000000  2.347000e+09  7.314507e+12
```



## For more information check out the [Documentation](https://github.com/antonio-hickey/FedPy/blob/main/DOCS.md).. 
