from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Returns amount of days between passed date and today

    If date string passed in is invalid (does not match format `'%Y-%m-%d'`),
    function throws `ValueError`

    :param date: string representing date to compare to
    :return: amount of days
    """

    try:
        date_in = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid date format") from e

    date_now = datetime.now()

    return (date_now - date_in).days
