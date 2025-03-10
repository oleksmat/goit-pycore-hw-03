import re

def normalize_phone(phone_number: str) -> str:
    """
        Normalizes phone number string passed in the argument

        Normalization operations:
        - Remove any non-number values (except a leading `+` symbol)
        - Add default country code (`+38`) if phone number length is 10
    :param phone_number: phone number string
    :return: normalized number
    """

    # we remove all symbols except digits and `+` symbol
    phone_number = re.sub('(\\D|\\+)', '', phone_number)

    # we assume that after that we are left with these options:
    # +\\d{12}
    # 380\\d{9}
    # 0\\d{9}
    # so we add required prefixes

    if phone_number.startswith('+'):
        return phone_number

    if phone_number.startswith('380'):
        return '+' + phone_number

    return '+38' + phone_number