# -*- coding: utf-8 -*-

import pytest
from subprocess import Popen, PIPE
from tests_common import tests_common


@pytest.mark.parametrize(('f1', 'f2'), tests_common.get_filenames("./concat/tests_data/", 1, 15))
def test_simple_assume(f1, f2):
    
    test = open(f1, "r").readline().strip('\n')
    answer = open(f2, "r").readline().strip('\n')
        
    proc = Popen(["python", "./concat/concat.py"], stdout=PIPE, stdin=PIPE)
    response = proc.communicate(input=str.encode(test))

    assert response[0].decode() == answer
