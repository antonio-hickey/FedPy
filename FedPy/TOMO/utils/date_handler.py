import datetime as dt

class DatesHandler:

    def time():
        now = dt.datetime.now()
        return now.strftime('%H:%M')
        
    def today():
        return dt.datetime.today()

    def last_weekday(d,weekday):
        
        if d.weekday() > weekday:
            last_week = d - dt.timedelta(days=7) 
            offset = (last_week.weekday() - weekday) % 7

            return last_week - dt.timedelta(days=offset)
        
        else:
            offset = (d.weekday() - weekday) % 7

            return d - dt.timedelta(days=offset)
        
    def next_weekday(d, weekday):
        
        days_forward = weekday - d.weekday()
        if days_forward <= 0:
            days_forward += 7

        return d + dt.timedelta(days_forward)
    
    def this_weekday(d, weekday):
        
        days_prev = weekday - d.weekday()
        
        return d + dt.timedelta(days_prev)
