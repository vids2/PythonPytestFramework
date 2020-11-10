'''
Created on 28 Oct 2020

@author: 612563313
'''

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
