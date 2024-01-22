from api import checkAnswer as check
from api import random_number as number
from api import random_foundation as foundation

def test(answer, number, foundation):
    number = 0
    foundation = 0

    c = check(answer)

    assert c is True


test(20)
