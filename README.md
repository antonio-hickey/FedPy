# FedPy
### _Everything Federal Reserve Related_

<img src="https://github.com/antonio-hickey/image-bucket/blob/master/Logo_FedPy.png?raw=true"/>

Open source python library for quickly and seamlessly pulling data related to the Federal Reserve.

## Installation:
Install using pip:

```sh
pip install FedPy
```



## Basic Example Usage:

Check out the [Documentation](https://antonio-hickey.github.io/FedPy.Docs/) for more in depth usage!


- Pull all the U.S Treasury Bills currently held in the Federal Reserve's System Open Market Account (SOMA) portfolio.
    - ```python
        import FedPy
        
        t_bill_holdings = FedPy.SOMA().holdings("bills")

- Pull Temporary Open Market Operations (TOMO) conducted by the Federal Reserve.

    - ```python 
        import FedPy
        
        repo_ops = FedPy.TOMO().repo()
        rev_repo_ops = FedPy.TOMO().reverse_repo()
