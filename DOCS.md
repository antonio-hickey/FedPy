## Commands:

 - #### FRED Commmands:
    - `FedPy.FRED(api_key, series_id, *start, *end)`: Returns Pandas Dataframe
                                                      of any FRED dataset, but requires
                                                      the inputs of data series id and api key.
                                                      (API Key is free @ https://research.stlouisfed.org/useraccount/apikeys)

 - #### FOMC Statement Command:
    - `FedPy.Transcripts().historic()`: Returns Pandas DataFrame of historic
                                        FOMC statements from 2006 to today.
    
    - `FedPy.Transcripts().latest()`: Returns Pandas Series of the latest
                                      FOMC statement.
    
    - `FedPy.Transcripts().previous()`: Returns Pandas Series of the previous
                                        FOMC statement.

 - #### SOMA Commands:
    - `FedPy.SOMA().hist()`: Returns Pandas DataFrame of
                             historical SOMA portfolio Summary.

    - `FedPy.SOMA().summary()`: Returns pandas DataFrame of
                                current SOMA portfolio Summary.

    - `FedPy.SOMA().total()`: Returns a float of the total
                              current value of the SOMA portfolio.

    - `FedPy.SOMA().bills()`: Returns a Pandas DataFrame of
                              current bills in SOMA portfolio.

    - `FedPy.soma().notes_bonds()`: Returns a Pandas DataFrame of
                                 current Notes & Bonds in SOMA portfolio.

    - `FedPy.SOMA().tips()`: Returns a Pandas DataFrame of
                             current TIPS in SOMA portfolio.

    - `FedPy.SOMA().frn()`: Returns a Pandas DataFrame of
                            current FRNs in SOMA portfolio.

    - `FedPy.SOMA().agency_debts()`: Returns a Pandas DataFrame of
                                     current Agency Debts in SOMA portfolio.

    - `FedPy.SOMA().cmbs()`: Returns a Pandas DataFrame of
                             current CMBS in SOMA portfolio.

 - #### TOMO Commands:
    - `FedPy.TOMO().repo()`: Returns a dictionary of data on
                             most recent Repo Operation.
    
    -  `FedPy.TOMO().reverse_repo()`: Returns a dictionary of data on
                                      most recent Reverse Repo Operation.
