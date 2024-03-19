from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the function and verify that it returns a string.
    full_name = make_full_name("Sally","Brown")
    assert isinstance(full_name,str)  #must return a string
    
    #Test some names
    assert make_full_name("Sally","Brown") == "Brown; Sally"
    assert make_full_name("Don Tom","Juan III") == "Juan III; Don Tom"
    return

def test_extract_family_name():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the function and verify that it returns a string.
    fam_name = extract_family_name("Brown; Sally")
    assert isinstance(fam_name,str)

    #Test out some names
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Juan III; Don Tom") == "Juan III"
    return

def test_extract_given_name():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the function and verify that it returns a string.
    giv_name = extract_given_name("Brown; Sally")
    assert isinstance(giv_name,str)

    #Test some names
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Juan III; Don Tom") == "Don Tom"
    return

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])