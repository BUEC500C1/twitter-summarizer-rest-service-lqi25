import pytest
from Twitter2Video import image2video,tweet2image

def test_result():
    assert tweet2image('') == "No tweet name entered!"
    # No twitter keys, can't test.
    '''
    assert tweet2image("BU_Tweets") == "Images created!"
    assert tweet2image("CNN") == "Images created!"
    assert tweet2image("Nike") == "Images created!"
    assert tweet2image("mfaboston") == "Images created!"
    assert tweet2image("CityOfBoston") == "Images created!"
    '''
    assert image2video("") == "No video name entered!"
    # No twitter keys, can't test.
    '''
    assert image2video("BU_Tweets") == "Video created!"
    assert image2video("CNN") == "Video created!"
    assert image2video("Nike") == "Video created!"
    assert image2video("mfaboston") == "Video created!"
    assert image2video("CityOfBoston") == "Video created!"
    '''

test_result()

