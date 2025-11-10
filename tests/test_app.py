from app.main import square
def test_square_numeric():
    assert square(3)["x2"] == 9
