import re

def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()

    if phone_number.startswith('+'):
        phone_number = phone_number[1:]
    else:
        pass

    phone_number = re.sub('\D', '', phone_number)

    if len(phone_number) == 10:
        return '+38' + phone_number

    return '+' + phone_number
