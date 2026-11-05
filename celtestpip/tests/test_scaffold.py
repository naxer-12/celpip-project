import os

def test_directories_exist():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.isdir(os.path.join(base, "crawler"))
    assert os.path.isdir(os.path.join(base, "server"))
    assert os.path.isdir(os.path.join(base, "static"))
    assert os.path.isfile(os.path.join(base, "requirements.txt"))
