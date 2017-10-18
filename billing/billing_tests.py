# -*- coding: utf-8 -*-

import pytest
from subprocess import Popen, PIPE
from tests_common import tests_common


@pytest.mark.parametrize(('task_file', 'answer_file'), tests_common.get_filenames("./tests_data/", 1, 23))
def test_simple_assume(task_file, answer_file):

    answer = open(answer_file, "r").readline().strip('\n')
    proc = Popen(["python", "./billing.py"], stdout=PIPE, stdin=PIPE)
    superline = ""
    for line in open(task_file, "r"):
        superline += line
        proc.stdin.write(str.encode(line))
    response = proc.communicate()

    assert response[0].decode() == answer
