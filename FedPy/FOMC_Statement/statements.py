from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

class Transcripts:

    """
        Returns a Pandas DataFrame of historic FOMC statements    
    """
    def hist_fomc_statement():

        # Create pandas DataFrame of the dataset
        URL = "https://raw.githubusercontent.com/antonio-hickey/FedPy/main/FedPy/data/fomc_statement_historic.csv"
        df = pd.read_csv(URL)

        return df

    
    """
        Returns a string of the most recent FOMC statement
    """
    def fomc_statement():
        
        # Creatign soup of press release feed
        URL = "https://www.federalreserve.gov/feeds/press_all.xml"
        page = req.get(URL)
        content = bs(page.content,"xml")
        
        # Finding FOMC Statement link
        items = content.findAll("item")
        for item in items:
            title = item.find("title")
            if "Federal Reserve issues FOMC statement" in title:
                link = item.find("link")
                LINK = link.text

        # Statement page
        statement_page = req.get(LINK)
        statement_content = bs(statement_page.content,"lxml")
        paragraphs = statement_content.findAll("p")
        
        # Rendering dataset
        for i in enumerate(paragraphs):
            if 'For release' in i[1].text:
                start = i[0]+1
            if 'Implementation Note issued' in i[1].text:
                end = i[0]
        paragraph_list = paragraphs[start:end]
        date = paragraphs[start-2].text
        p_ = [i.text for i in paragraph_list]
        statement = ' '.join(map(str,p_))
        dict = {"Date": date, "Statement": statement}
        
        return dict
