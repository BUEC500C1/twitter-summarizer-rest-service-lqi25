import pytest
from Twitter2Video import image2video,tweet2image
from queue_mul import Mul_Threads
import os
def test_result():
    item_list = ['BU_Tweets','CNN','Nike','mfaboston']
    assert Mul_Threads([],2) == "No twitter names entered"
    assert Mul_Threads(item_list,0) == "The num should be bigger than 0"
    # No twitter keys, can't test.
    '''
    Mul_Threads(item_list, 4)
    assert os.path.exists('BU_Tweets.avi') == True
    assert os.path.exists('CNN.avi') == True
    assert os.path.exists('Nike.avi') == True
    assert os.path.exists('mfaboston.avi') == True
    assert os.path.exists('celtics.avi') == False
    '''

#test_result()