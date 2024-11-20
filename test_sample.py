import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from sample import *
from io import StringIO
from unittest.mock import patch

def test_answer():
    assert func(3) == 5

def test_input_credentials_good_input(monkeypatch):
    inputs = iter(['joel', 'joelbolduc@hotmail.fr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==True and b==[])

def test_input_credentials_space_username(monkeypatch):
    inputs = iter(['jo el', 'joelbolduc@hotmail.fr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.'])


def test_input_credentials_empty_username(monkeypatch):
    inputs = iter(['', 'joelbolduc@hotmail.fr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.'])

def test_input_credentials_email_no_at(monkeypatch):
    inputs = iter(['joel', 'joelbolduchotmail.fr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['email should contain both a . and an @ character.'])

def test_input_credentials_email_no_dot(monkeypatch):
    inputs = iter(['joel', 'joelbolduc@hotmailfr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['email should contain both a . and an @ character.'])

def test_input_credentials_email_no_at_or_dot(monkeypatch):
    inputs = iter(['joel', 'joelbolduchotmailfr','abc123!!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['email should contain both a . and an @ character.'])

def test_input_credentials_empty_username_email_no_at_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduchotmail.fr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_dot_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduc@hotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_at_or_dot_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduchotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_at_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmail.fr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_dot_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduc@hotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_at_or_dot_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_at_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduchotmail.fr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_dot_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduc@hotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_at_or_dot_password_too_short(monkeypatch):
    inputs = iter(['', 'joelbolduchotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_at_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmail.fr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_dot_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduc@hotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_space_username_email_no_at_or_dot_password_too_short(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmailfr','abc123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.'])

def test_input_credentials_empty_username_email_no_at_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduchotmail.fr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_empty_username_email_no_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduc@hotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_empty_username_email_no_at_or_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduchotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_at_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmail.fr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduc@hotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_at_or_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_empty_username_email_no_at_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduchotmail.fr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_empty_username_email_no_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduc@hotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_empty_username_email_no_at_or_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['', 'joelbolduchotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot be empty.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_at_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmail.fr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduc@hotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_space_username_email_no_at_or_dot_password_too_short_no_letters_in_password(monkeypatch):
    inputs = iter(['jo el', 'joelbolduchotmailfr','!!!123!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['username cannot contain whitespaces.','email should contain both a . and an @ character.','password should contain at least 8 characters.','password must contain a letter'])

def test_input_credentials_no_numbers_in_password(monkeypatch):
    inputs = iter(['joel', 'joelbolduc@hotmail.fr','aaabbb!!'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['password must contain a number'])

def test_input_credentials_no_special_characters_in_password(monkeypatch):
    inputs = iter(['joel', 'joelbolduc@hotmail.fr','aaabbbo1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    a,b=input_credentials()
    assert (a==False and b==['password must contain a special character'])