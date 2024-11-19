import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from sample import *
from io import StringIO

def test_answer():
    assert func(3) == 5

def test_double(monkeypatch):
    number_inputs = StringIO('joelbolduc\njoelbolduc@hotmail.fr\nabc123!')
    monkeypatch.setattr('sys.stdin', number_inputs)
    a,b=input_credentials()
    assert (a==True and b==[])