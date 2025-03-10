from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
        Return a list of users with congratulation dates, whose birthdays are in the next 7 days.

        Congratulation date is a date on a birthday date or the next Monday after birthday date,
        if birthday date is a weekend (Saturday or Sunday).

        Dates are parsed and formatted using this format: "%Y.%m.%d".

    :param users: list of dictionaries with keys "name" and "birthday"
    :return: list of dictionaries with keys "name" and "congratulation_date"
    """

    # results list
    users_to_greet: list[dict[str, str]] = list()

    today = datetime.now().date()

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # get the next birthday after today
        next_birthday = birthday_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday_date.replace(year=today.year + 1)

        # if next birthday is more than 7 days a week,
        # user is not added to the results list
        if (next_birthday - today).days > 7:
            continue

        congratulation_date = next_birthday

        weekday = next_birthday.weekday()

        if weekday > 4:
            # 1 for Sunday
            # 2 for Saturday
            days_to_add = 7 - weekday

            congratulation_date = next_birthday + timedelta(days=days_to_add)

        # adding user to set of results with correct congratulation date
        users_to_greet.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return users_to_greet
