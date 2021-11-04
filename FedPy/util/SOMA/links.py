from typing import Union

from ..date_handler import DatesHandler as datesHand


class Create:
    """Class to create links to SOMA data"""

    def __init__(self):
        self.today = datesHand().today().date()
        self.link_base = "https://markets.newyorkfed.org/read?productCode=30&startDt="

    def summary(self) -> str:
        """
        Method to get summary of
        current SOMA portfolio.
        """
        link_end = "&query=summary&format=json"
        return self.date_context() + link_end

    def holdings(self, security_type: Union[str, list[str]]) -> str:
        """
        Method to get holding details on specific types
        of securities in the SOMA portfolio.
        """
        if isinstance(security_type, str):
            return (self.date_context() + f"&query=details&holdingTypes={security_type}&format=json")
        else:
            security_types: str = ','.join(security_type)
            return (self.date_context() + f"&query=details&holdingTypes={security_types}&format=json")

    def date_context(self) -> str:
        """
        Method to handle logic behind creating
        links to current SOMA portfolio data.
        """

        # If today is before Thursday use last weeks URL
        if self.today.weekday() < 3:
            last_wednesday = datesHand().last_weekday(self.today, 2)
            return self.link_base + last_wednesday + "&endDt=" + last_wednesday

        # else If today is Thursday
        elif self.today.weekday() == 3:
            # If the time is past 5:00 pm use yesterday's URL
            if int(datesHand().time()[:2]) >= 17:
                this_wednesday = datesHand().this_weekday(self.today, 2)
                return self.link_base + this_wednesday + "&endDt=" + this_wednesday

            # Else before 5:00 pm use last weeks URL
            else:
                last_wednesday = datesHand().last_weekday(self.today, 2)
                return self.link_base + last_wednesday + "&endDt=" + last_wednesday

        # Else today is past Thursday use this weeks URL
        else:
            this_wednesday = datesHand().this_weekday(self.today, 2)
            return self.link_base + this_wednesday + "&endDt=" + this_wednesday
