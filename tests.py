import pytest

def conjunction(A, B):
    return A and B

def disjunction(A, B):
    return A or B

def negation(A):
    return not A

def implication(A, B):
    return not A or B

def biconditional(A, B):
    return A == B

# Normal Test Cases
def test_case_1():
    A, B = True, True
    assert conjunction(A, B) == True
    assert disjunction(A, B) == True
    assert negation(A) == False
    assert negation(B) == False
    assert implication(A, B) == True
    assert biconditional(A, B) == True

def test_case_2():
    A, B = True, False
    assert conjunction(A, B) == False
    assert disjunction(A, B) == True
    assert negation(A) == False
    assert negation(B) == True
    assert implication(A, B) == False
    assert biconditional(A, B) == False

def test_case_3():
    A, B = False, True
    assert conjunction(A, B) == False
    assert disjunction(A, B) == True
    assert negation(A) == True
    assert negation(B) == False
    assert implication(A, B) == True
    assert biconditional(A, B) == False

# Edge Test Cases
def test_case_4():
    A, B = False, False
    assert conjunction(A, B) == False
    assert disjunction(A, B) == False
    assert negation(A) == True
    assert negation(B) == True
    assert implication(A, B) == True
    assert biconditional(A, B) == True

def test_invalid_input_non_boolean():
    A = 2
    B = -1
    with pytest.raises(ValueError):
        if A not in [0, 1] or B not in [0, 1]:
            raise ValueError("Invalid input. Please enter 1 or 0.")

def test_empty_input():
    A = ''
    B = ''
    with pytest.raises(ValueError):
        if not isinstance(A, int) or not isinstance(B, int):
            raise ValueError("Invalid input. Please enter numeric values (1 or 0).")
