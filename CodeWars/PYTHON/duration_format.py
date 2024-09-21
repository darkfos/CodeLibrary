"""
    Your task in order to complete this Kata is to write a function which formats
    a duration, given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer. If it is zero, it just returns
    "now". Otherwise, the duration is expressed as a combination of years, days, hours,
    minutes and seconds.

    Different components have different unit of times. So there is not repeated units
    like in 5 seconds and 1 second.
    A component will not appear at all if its value happens to be zero. Hence, 1 minute
    and 0 seconds is not valid, but it should be just 1 minute.
    A unit of time must be used "as much as possible". It means that the function should
    not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified
    by of a component must not be greater than any valid more significant unit of time.
"""

def format_duration(seconds):
    #4 kyu

    if seconds:
        minutes: float = seconds / 60
        seconds = seconds - int(minutes) * 60
        minutes = int(minutes)
        hour = days = years = 0

        if minutes >= 60:
            hour: float = minutes / 60
            minutes = minutes - int(hour) * 60
            hour = int(hour)
        if hour >= 24:
            days: float = hour / 24
            hour = hour - int(days) * 24
            days = int(days)
        
        if days >= 365:
            years: float = days / 365
            days = days - int(years) * 365
            years = int(years)
        
        result = (
            (str(years) + " year" if years < 2 else str(years) + " years") if years else "",
            (str(days) + " day" if days < 2 else str(days) + " days") if days else "",
            (str(hour) + " hour" if hour < 2 else str(hour) + " hours") if hour else "",
            (str(minutes) + " minute" if minutes < 2 else str(minutes) + " minutes") if minutes else "",
            (str(seconds) + " second" if seconds < 2 else str(seconds) + " seconds") if seconds else ""
        )

        result: str = ", ".join(filter(lambda x: x != "", result))
        result = result[::-1].replace(",", "dna ", 1)
        return result[::-1]
    return "now"