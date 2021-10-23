from ..date_handler import DatesHandler as datesHand


class Create:
    """ Class to create diff links for TOMO data """

    def __init__(self) -> None:
        self.link_base = "https://markets.newyorkfed.org/read?productCode=70&startDt=2000-07-01"
        self.today = datesHand().today().date()
        self.link_base = self.link_base + f"&endDt={self.today}&operationTypes="

    def rp_link(self) -> str:
        return self.link_base + "Repo&eventCodes=730"

    def rrp_link(self) -> str:
        return self.link_base + "Reverse Repo&eventCodes=730"
