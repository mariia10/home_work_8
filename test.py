from api import checkAnswer as check

def test(answer, number, foundation):
    c = check(answer, number, foundation)
    assert c is True


test(20)
