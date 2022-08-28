import pytest
from gendiff import diff_builder


expected = '/home/rockbiter/git/projects/python-project-lvl2/tests/fixtures/expect'
first_file = '/home/rockbiter/git/projects/python-project-lvl2/tests/fixtures/file1.json'
second_file = '/home/rockbiter/git/projects/python-project-lvl2/tests/fixtures/file2.json'


def test_generate_diff():
    result = diff_builder.generate_diff(first_file, second_file)
    with open(expected, 'r') as expect_file:
        expect_result = expect_file.read()
        assert result == expect_result
