def mask_security_number(security_number):
    return security_number[:len(security_number) - 4] + "****"

print(mask_security_number("880720-1234567"))