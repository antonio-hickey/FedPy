from util.date_handler import DatesHandler as datesHand

SOMA_HIST_BASE = "https://raw.githubusercontent.com/antonio-hickey/"
SOMA_HIST_END = "FedPy/main/FedPy/data/soma_historical.csv"
SOMA_HIST = SOMA_HIST_BASE + SOMA_HIST_END


class Create:
    """ Class to create different links for SOMA data"""

    def __init__(self):
        self.today = datesHand().today().date()
        self.link_base = "https://markets.newyorkfed.org/read?productCode=30&startDt="

    def summary(self) -> str:
        link_end = "&query=summary&format=xml"
        return self.current_handler(link_end)

    def current_holdings(self, type: str) -> str:
        link_end = f"&query=details&holdingTypes={type}&format=xml"
        return self.current_handler(link_end)

    def current_handler(self, link_end: str) -> str:
        """ Handle logic behind creating links
            current SOMA portfolio data. """
        # If today is before Thursday use last weeks URL
        if self.today.weekday() < 3:
            last_wednesday = datesHand().last_weekday(self.today, 2)
            return self.link_base + last_wednesday + "&endDt=" + last_wednesday + link_end

        # If today is Thursday
        elif self.today.weekday() == 3:
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand().time()[:2]) >= 17:
                this_wednesday = datesHand().this_weekday(self.today, 2)
                return self.link_base + this_wednesday + "&endDt=" + this_wednesday + link_end

            # Else before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand().last_weekday(self.today, 2)
                return self.link_base + last_wednesday + "&endDt=" + last_wednesday + link_end

        # Else today is past Thursday use this weeks URL
        else:
            this_wednesday = datesHand().this_weekday(self.today, 2)
            return self.link_base + this_wednesday + "&endDt=" + this_wednesday + link_end
