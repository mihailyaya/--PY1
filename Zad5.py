from random import sample


def get_random_password(n=8) -> str:
    str_ = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    password = "".join(sample(str_, n))
    return password


print(get_random_password())
