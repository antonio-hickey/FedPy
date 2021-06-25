"""
soma.py : System Open Market Operations portfolio

Sourced: New York Federal Reserve (https://markets.newyorkfed.org)

Output Data:
    - Total Current SOMA Holdings
        - Bill holdings
        - Note & Bond holdings
        - TIPS holdings
        - FRN holdings
        - Agency Debts holdings
        - CMBS holdings
    - Historical SOMA Holdings
        - Bill holdings
        - Note & Bond holdings
        - TIPS holdings
        - FRN holdings
        - Agency Debts holdings
        - CMBS holdings
 
"""

# Import Modules
from .utils.date_handler import DatesHandler as datesHand
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

class SOMA:
    
    """
       Output's a dictionary summary
       of the current SOMA portfolio.
    """
    def Summary():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=summary&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=summary&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=summary&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=summary&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        date = []
        mbs = []
        cmbs = []
        tips = []
        frn = []
        tips_infcomp = []
        nb = []
        bills = []
        agencies = []
        total = []


        summary = soup.find("summary")    
        date = summary.find("asofdate").text
        mbs = summary.find("mbs").text
        cmbs = summary.find("cmbs").text
        tips = summary.find("tips").text
        frn = summary.find("frn").text
        tips_infcomp = summary.find("tipsinflationcompensation").text
        notes_bonds = summary.find("notesbonds").text
        bills = summary.find("bills").text
        agencies = summary.find("agencies").text
        total = summary.find("total").text

        d = {
            'Date': date,
            'Total': total,
            'Bills': bills,
            'Notes & Bonds': notes_bonds,
            'TIPS': tips,
            'FRNs': frn,
            'CMBS': cmbs,
            'MBS': mbs,
            'Agencies': agencies,
        }

        return d

    """
       Output's a float of the
       total current SOMA portfolio. 
    """
    def Total():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=summary&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=summary&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=summary&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=summary&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        summary = soup.find("summary")    
        total = summary.find("total").text

        return float(total)


        
    """
       Outputs a DataFrame of 
       current SOMA bill holdings.
    """
    def Bills():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        b_date = []
        b_maturity = []
        b_cusip = []
        b_percout = []
        b_parvalue = []
        b_cfpw = []
        b_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "Bills":
                b_date.append(holdings[i].find("asofdate").text)
                b_maturity.append(holdings[i].find("maturitydate").text)
                b_cusip.append(holdings[i].find("cusip").text)
                b_percout.append(holdings[i].find("percentoutstanding").text)
                b_parvalue.append(holdings[i].find("parvalue").text)
                b_cfpw.append(holdings[i].find("changefrompriorweek").text) 
                b_sectype.append("Bills")
            

        # Bills Dictionary
        bills_d = {
            'date': b_date,
            'security type': b_sectype,
            'maturity date': b_maturity,
            'cusip': b_cusip,
            'percent outstanding': b_percout,
            'change from prior week': b_cfpw, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(bills_d)

        # Return the DataFrame
        return df

    """
       Outputs a DataFrame of current 
       SOMA notes & bobnds holdings.
    """
    def NotesBonds():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        nb_date = []
        nb_maturity = []
        nb_cusip = []
        nb_coupon = []
        nb_percout = []
        nb_parvalue = []
        nb_cfpw = []
        nb_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "NotesBonds":
                nb_date.append(holdings[i].find("asofdate").text)
                nb_maturity.append(holdings[i].find("maturitydate").text)
                nb_cusip.append(holdings[i].find("cusip").text)
                nb_coupon.append(holdings[i].find("coupon").text)
                nb_percout.append(holdings[i].find("percentoutstanding").text)
                nb_parvalue.append(holdings[i].find("parvalue").text)
                nb_cfpw.append(holdings[i].find("changefrompriorweek").text) 
                nb_sectype.append("Notes & Bonds")
            

        # Bills Dictionary
        nb_d = {
            'date': nb_date,
            'security type': nb_sectype,
            'maturity date': nb_maturity,
            'cusip': nb_cusip,
            'coupon': nb_coupon,
            'percent outstanding': nb_percout,
            'change from prior week': nb_cfpw, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(nb_d)

        # Return the DataFrame
        return df

    """
       Outputs a DataFrame of current 
       SOMA TIPS holdings.
    """
    def TIPS():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        tips_date = []
        tips_maturity = []
        tips_cusip = []
        tips_coupon = []
        tips_percout = []
        tips_parvalue = []
        tips_infcomp = []
        tips_cfpw = []
        tips_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "TIPS":
                tips_date.append(holdings[i].find("asofdate").text)
                tips_maturity.append(holdings[i].find("maturitydate").text)
                tips_cusip.append(holdings[i].find("cusip").text)
                tips_coupon.append(holdings[i].find("coupon").text)
                tips_percout.append(holdings[i].find("percentoutstanding").text)
                tips_infcomp.append(holdings[i].find("inflationcompensation").text)
                tips_parvalue.append(holdings[i].find("parvalue").text)
                tips_cfpw.append(holdings[i].find("changefrompriorweek").text) 
                tips_sectype.append("TIPS")
            

        # Bills Dictionary
        tips_d = {
            'date': tips_date,
            'security type': tips_sectype,
            'maturity date': tips_maturity,
            'cusip': tips_cusip,
            'coupon': tips_coupon,
            'percent outstanding': tips_percout,
            'inflation compensation': tips_infcomp,
            'change from prior week': tips_cfpw, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(tips_d)

        # Return the DataFrame
        return df

    """
       Outputs a DataFrame of current 
       SOMA FRNs holdings.
    """
    def FRNs():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        frn_date = []
        frn_maturity = []
        frn_cusip = []
        frn_spread = []
        frn_percout = []
        frn_parvalue = []
        frn_cfpw = []
        frn_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "FRNs":
                frn_date.append(holdings[i].find("asofdate").text)
                frn_maturity.append(holdings[i].find("maturitydate").text)
                frn_cusip.append(holdings[i].find("cusip").text)
                frn_spread.append(holdings[i].find("spread").text)
                frn_percout.append(holdings[i].find("percentoutstanding").text)
                frn_parvalue.append(holdings[i].find("parvalue").text)
                frn_cfpw.append(holdings[i].find("changefrompriorweek").text) 
                frn_sectype.append("FRNs")
            

        # Bills Dictionary
        frn_d = {
            'date': frn_date,
            'security type': frn_sectype,
            'maturity date': frn_maturity,
            'cusip': frn_cusip,
            'spread': frn_spread,
            'percent outstanding': frn_percout,
            'change from prior week': frn_cfpw, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(frn_d)

        # Return the DataFrame
        return df

    """
       Outputs a DataFrame of current 
       SOMA Agency Debts holdings.
    """
    def AgencyDebts():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        ad_date = []
        ad_maturity = []
        ad_cusip = []
        ad_issuer = []
        ad_coupon = []
        ad_parvalue = []
        ad_cfpw = []
        ad_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "Agency Debts":
                ad_date.append(holdings[i].find("asofdate").text)
                ad_maturity.append(holdings[i].find("maturitydate").text)
                ad_cusip.append(holdings[i].find("cusip").text)
                ad_issuer.append(holdings[i].find("issuer").text)
                ad_coupon.append(holdings[i].find("coupon").text)
                ad_parvalue.append(holdings[i].find("parvalue").text)
                ad_cfpw.append(holdings[i].find("changefrompriorweek").text) 
                ad_sectype.append("Agency Debts")
            

        # Bills Dictionary
        ad_d = {
            'date': ad_date,
            'security type': ad_sectype,
            'maturity date': ad_maturity,
            'cusip': ad_cusip,
            'issuer': ad_issuer,
            'coupon': ad_coupon,
            'par value': ad_parvalue,
            'change from prior week': ad_cfpw, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(ad_d)

        # Return the DataFrame
        return df

    """
       Outputs a DataFrame of current 
       SOMA Agency Debts holdings.
    """
    def CMBS():

        """ 
            Dynamic URL to always get most recent data
        """
        today = datesHand.today().date()
        
        # If today is before Thursday use last weeks URL
        if today.weekday() < 3:
            last_wednesday = datesHand.last_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"

        
        # If today is Thursday
        if today.weekday() == 3:
            
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand.time()[:2]) >= 17:
                this_wednesday = datesHand.this_weekday(today,2)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
            
            # If before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand.last_weekday(today,2)
                print(last_wednesday)
                URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={last_wednesday}&endDt={last_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
        
        # If today is past Thursday use this weeks URL
        if today.weekday() > 3:
            this_wednesday = datesHand.this_weekday(today,2)
            URL = f"https://markets.newyorkfed.org/read?productCode=30&startDt={this_wednesday}&endDt={this_wednesday}&query=details&holdingTypes=bills,notesbonds,frn,tips,cmbs,agency%20debts&format=xml"
 
        
        # Making Soup
        page = req.get(URL) # Request Page
        soup = bs(page.content,"lxml") # Parse page as XML

        # Null Lists
        cmbs_date = []
        cmbs_cusip = []
        cmbs_secdescrip = []
        cmbs_facevalue = []
        cmbs_sectype = []

        # Each Holding in portfolio
        holdings = soup.findAll("holding")
        
        # For each holding in holdings
        for i in range(len(holdings)):

            # Define what type of security it is
            security = holdings[i].find("securitytype").text
            
            # If security is a bill then...
            if security == "CMBS":
                cmbs_date.append(holdings[i].find("asofdate").text)
                cmbs_cusip.append(holdings[i].find("cusip").text)
                cmbs_secdescrip.append(holdings[i].find("securitydescription").text)
                cmbs_facevalue.append(holdings[i].find("currentfacevalue").text)
                cmbs_sectype.append("CMBS")
            

        # Bills Dictionary
        cmbs_d = {
            'date': cmbs_date,
            'security type': cmbs_sectype,
            'security description': cmbs_secdescrip,
            'cusip': cmbs_cusip,
            'par value': cmbs_facevalue, 
        }

        # Render Pandas DataFrame
        df = pd.DataFrame(cmbs_d)

        # Return the DataFrame
        return df

    def Hist():
        df = pd.read_csv('https://raw.githubusercontent.com/antonio-hickey/FedPy/main/FedPy/data/soma_historical.csv')
        return df

    
