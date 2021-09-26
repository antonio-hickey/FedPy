import datetime as dt

class DatesHandler:

    def time() -> datetime.datetime:
        now = dt.datetime.now()
        return now.strftime('%H:%M')
        
    def today() -> datetime.datetime:
        return dt.datetime.today()

    def last_weekday(day: datetime.datetime, weekday: int) -> str:
        
        if day.weekday() > weekday:
            last_week = day - dt.timedelta(days=7) 
            offset = (last_week.weekday() - weekday) % 7

            return str(last_week - dt.timedelta(days=offset))
        
        else:
            offset = (day.weekday() - weekday) % 7

            return str(day - dt.timedelta(days=offset))
        
    def next_weekday(day: datetime.datetime, weekday: int) -> str:
        
        days_forward = weekday - day.weekday()
        if days_forward <= 0:
            days_forward += 7

        return str(day + dt.timedelta(days_forward))
    
    def this_weekday(day: dt.datetime, weekday: int) -> str:
        
        days_prev = weekday - day.weekday()
        
        return str(day + dt.timedelta(days_prev))
