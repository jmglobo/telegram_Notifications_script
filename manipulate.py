
# Metodo para dar la fecha actual
def date():
    from datetime import datetime 
    dt = datetime.now()
    date = "{:02}/{:02}/{}".format(dt.day,dt.month,dt.year)
    return date


# Metodo para dar la hora actual
def hour():
    from datetime import datetime 
    dt = datetime.now()
    hour = "{:02}:{:02}".format(dt.hour,dt.minute)
    return hour





