## Commands:

 - #### FRED Commmands:
    - `FedPy.fred(api_key, series_id, *start, *end)`: Returns Pandas Dataframe
                                                   of any FRED dataset, but requires
                                                   the inputs of data series id and api key.
                                                

 - #### SOMA Commands:
    - `FedPy.soma_hist()`: Returns Pandas DataFrame of
                  historical SOMA portfolio Summary.
                  
    - `FedPy.soma()`: Returns pandas DataFrame of
            current SOMA portfolio Summary.
            
    - `FedPy.soma_total()`: Returns a float of the total
                   current SOMA portfolio.
                   
    - `soma_bills()`: Returns a Pandas DataFrame of
                   current bills in SOMA portfolio.
                   
    - `FedPy.soma_notesbonds()`: Returns a Pandas DataFrame of
                        current Notes & Bonds in SOMA portfolio.
                        
    - `FedPy.soma_tips()`: Returns a Pandas DataFrame of 
                  current TIPS in SOMA portfolio.
                  
    - `FedPy.soma_frn()`: Returns a Pandas DataFrame of
                  current FRNs in SOMA portfolio.
                  
    - `FedPy.soma_agencies()`: Returns a Pandas DataFrame of
                      current Agency Debts in SOMA portfolio.
                      
    - `FedPy.soma_cmbs()`: Returns a Pandas DataFrame of
                  current CMBS in SOMA portfolio.

 - #### TOMO Commands:
    - `FedPy.tomo_rp()`: Returns a dictionary of data on
                   most recent Repo Operation.
    -  `FedPy.tomo_rrp()`: Returns a dictionary of data on
                   most recent Reverse Repo Operation.
