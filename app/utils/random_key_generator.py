#pylint: disable=missing-final-newline
""" Random key generator"""
import random
import string

def generate_key(length):
    """
    Generates a Random String for utility purpose

    Args:
        length (Int): Length of the random string

    Returns:
        [String]: Returns a random string of the given length
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))