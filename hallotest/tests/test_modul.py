from hallotest import hallo, gruesse

def test_hallo_default():
    assert hallo() == "Hallo, Welt!"

def test_hallo_name():
    assert hallo("Luis") == "Hallo, Luis!"

def test_gruesse_returns_string():
    result = gruesse("Luis")
    assert isinstance(result, str)
    assert "Luis" in result

def test_gruesse_random():
    results = {gruesse("Test") for _ in range(20)}
    assert len(results) > 1