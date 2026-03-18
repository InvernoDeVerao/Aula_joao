def validate_email (email):
    if email.count('@') != 1 or email.count('.com') != 1:
        return False
    return True
