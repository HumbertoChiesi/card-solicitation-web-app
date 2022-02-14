import random


def credit_approved(income) -> float:
    serasa_score = random.randint(1, 999)
    cc_limit = 0
    if serasa_score >= 951:
        cc_limit = 1000000
    elif serasa_score >= 800:
        cc_limit = income * 4
    elif serasa_score >= 600:
        cc_limit = income / 2
        if cc_limit < 1000:
            cc_limit = 1000
    elif serasa_score >= 300:
        cc_limit = 1000

    return cc_limit
