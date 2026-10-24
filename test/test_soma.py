from main import soma, diminuir 

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_diminuir():
    assert diminuir(2, 3) == -1
    assert diminuir(-1, 1) == -2
    assert diminuir(2, -1) == 3
