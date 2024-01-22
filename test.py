from api import checkAnswer as check

def testMod(answer, number, foundation):
    c = check(answer, number, foundation)
    assert c is True

def testValidation(answer, number, foundation):
    c = check(answer, number, foundation)
    assert c is False

testMod("2", 16, 7)
testValidation("hhdehdh2", 16, 7)
