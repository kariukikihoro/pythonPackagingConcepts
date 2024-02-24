from mypackage import myModule

def test_top_n():
    """
    making sure the top n function works as intended
    :return:
    """

    assert myModule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], "incorrect"
    assert myModule.top_n([8, 9, 2, 4], 2) == [9, 8], "incorrect"
    assert myModule.top_n([6, 5, 4, 3 , 2, 1], 4) == [6, 5, 4, 3], "incorrect"