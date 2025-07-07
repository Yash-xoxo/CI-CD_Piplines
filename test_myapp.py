from first import lw_sum, lw_mul

def test_sum():
    assert lw_sum(2, 3) == 5
    assert lw_sum(3, 3) == 6
    

def test_mul():
    assert lw_mul(2, 3) == 6
    assert lw_mul(5, 6) == 30

def test_sub():
    assert lw_mul(2, 8) == -6
    assert lw_mul(13, 4) == 9

def test_div():
    assert lw_mul(9, 3) == 3
    assert lw_mul(45, 9) == 5


