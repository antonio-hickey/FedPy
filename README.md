# FedPy
## _Everything Federal Reserve Related_

<img src=https://github.com/antonio-hickey/FedPy/blob/main/FedPy_logo.png/>

Open source python library for quickly and seamlessly pulling data related to the Federal Reserve.

## Installation:
Install using pip:


```sh
pip install FedPy
```


## [Documentation](https://antonio-hickey.github.io/FedPy.Docs/):
Check out the [Documentation](https://antonio-hickey.github.io/FedPy.Docs/) for more in depth usage!

## Basic Example Usage:
```
import FedPy
t_bill_holdings = FedPy.SOMA.holdings("bills")
```

### Output's a pandas DataFrame with the CUSIP as the column name:
```
                                9127964W6           912796N54           912796H51  ...           912796L64           912796M71           912796M89
asOfDate                       2021-11-03          2021-11-03          2021-11-03  ...          2021-11-03          2021-11-03          2021-11-03
maturityDate                   2021-11-04          2021-11-09          2021-11-12  ...          2022-08-11          2022-09-08          2022-10-06
issuer                                                                             ...
spread                                                                             ...
coupon                                                                             ...
parValue                      20426299000          4646453200         11769171200  ...          3847131500          3419277000          5630934600
inflationCompensation                                                              ...
percentOutstanding     0.1257560211293619  0.0583431654873188  0.0982657862288283  ...  0.1016500440616873  0.0913774993736779  0.1420853358794164
changeFromPriorWeek                     0                   0                   0  ...                   0                   0                   0
changeFromPriorYear                                                                ...
securityType                        Bills               Bills               Bills  ...               Bills               Bills               Bills
```
