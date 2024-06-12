from format_phone import RwandaPhoneFormat


def test_rwanda_phone_format_start_with_078():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("0788000000")
    assert formatted_phone == "250788000000"


def test_rwanda_phone_format_start_with_250():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("250788000000")
    assert formatted_phone == "250788000000"


def test_rwanda_phone_format_start_with_78():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("788000000")
    assert formatted_phone == "250788000000"


def test_rwanda_phone_format_start_with_plus_250():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("+250788000000")
    assert formatted_phone == "250788000000"


def test_rwanda_phone_format_with_invalid_phone():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("25078800000011")
    assert formatted_phone == "25078800000011"


def test_rwanda_phone_format_with_invalid_input():
    phone_format = RwandaPhoneFormat()
    formatted_phone = phone_format.format_phone("1")
    assert formatted_phone == "1"
