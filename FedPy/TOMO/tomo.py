"""
tomo.py : Temporary Open Market Operations 

Sourced: New York Federal Reserve (https://markets.newyorkfed.org)

Output Data:
    - recent_rp():
        - {Date,OpType,OpId,Maturity,Method,Treasuries,Agencies,MortBack,Total}
    - recent_rrp():
        - {Date,OpType,OpId,Maturity,Method,TreasuryCollateral,Yield}
"""

# Import Modules
from .utils.date_handler import DatesHandler as datesHand
from bs4 import BeautifulSoup as bs
import requests as req

class TOMO:

    """
        Returns a dictionary with data on most recent
        repo operations by the Federal Reserve.
    """    
    def recent_rp():
        if (int(datesHand.time()[:2])) > 14:
            URL = "https://websvcgatewayx2.frbny.org/autorates_tomo_external/services/v1_0/tomo/retrieveXml"
        else:
            URL = "https://websvcgatewayx2.frbny.org/autorates_tomo_external/services/v1_0/tomo/retrieveXmlLastN?n=2"
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML
        
        # Types of operations inside group tag
        groups = soup.findAll("ns2:group")
        
        # Repo Operations
        RP = groups[0]
        op_id = RP['operationid']
        deal_date = RP['dealdate']
        maturity_date = RP['maturitydate']
        auction_method = RP['auctionmethod']
        sections = RP.findAll("ns2:section")
        treasury = sections[0].find("ns2:totalpropositionsaccepted")['value']
        agency = sections[1].find("ns2:totalpropositionsaccepted")['value']
        mort_back = sections[2].find("ns2:totalpropositionsaccepted")['value']
        total = sections[3].find("ns2:totalpropositionsaccepted")['value']

        # Render dictionary
        d = {
            'Deal Date': deal_date, 
            'Operation Type': "Repo",
            'Operation ID': op_id,
            'Maturity Date': maturity_date,
            'Auction Method': auction_method,
            'Treasuries': treasury,
            'Agencies': agency,
            'Mortgage Backed': mort_back,
            'Total': total,
        }

        # Return dictionary
        return d

    """
        Returns a dictionary of most
        recent Reverse Repo Operations.
    """
    def recent_rrp():
        if (int(datesHand.time()[:2])) > 14:
            URL = "https://websvcgatewayx2.frbny.org/autorates_tomo_external/services/v1_0/tomo/retrieveXml"
        else:
            URL = "https://websvcgatewayx2.frbny.org/autorates_tomo_external/services/v1_0/tomo/retrieveXmlLastN?n=2"
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML
        
        # Types of operations inside group tag
        groups = soup.findAll("ns2:group")
        
        # Reverse Repo Operations
        RRP = groups[1]
        op_id = RRP['operationid']
        deal_date = RRP['dealdate']
        maturity_date = RRP['maturitydate']
        auction_method = RRP['auctionmethod']
        sections = RRP.findAll('ns2:section')
        treasury_collateral = sections[0]
        value = treasury_collateral.find("ns2:totalpropositionsaccepted")['value']
        rate = treasury_collateral.find("ns2:awardrate")['value']

        # Render dictionary
        d = {
            'Deal Date': deal_date,
            'Operation Type': "Reverse Repo",
            'Operation ID': op_id,
            'Maturity Date': maturity_date,
            'Auction Method': auction_method,
            'Treasury Collateral': value,
            'Yield': rate,
        }
        
        # Return dictionary above
        return d 
