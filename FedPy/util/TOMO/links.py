from util.date_handler import DatesHandler as datesHand

LINK_BASE = "https://markets.newyorkfed.org/read?productCode=70&startDt=2000-07-01"


class Create:
    """ Class to create diff links for TOMO data """

    def __init__(self) -> None:
        self.today = datesHand().today().date()
        self.link_base = LINK_BASE

    def rp_link(self) -> str:
        link_end = f"&endDt={self.today}&operationTypes=Repo&eventCodes=730"
        return self.link_base + link_end

    def rrp_link(self) -> str:
        link_end = f"&endDt={self.today}&operationTypes=Reverse Repo&eventCodes=730"
        return self.link_base + link_end
