import pytest
import os
from gendiff import diff_builder


PATH_TO_FIXTURES = '/home/rockbiter/git/projects/python-project-lvl2/tests/fixtures/'
first_file = 'file1.json'
second_file = 'file2.json'


@pytest.mark.parametrize('path_to_first, path_to_second, expected_result', [
    pytest.param(
        'file1.json',
        'file2.json',
        'expect',
    )])
def test_generate_diff(path_to_first, path_to_second, expected_result):
    test_data = collect_data('expect')
    assert diff_builder.generate_diff(path_to_first, path_to_second) == test_data


def collect_data(path_to_file):
    with open(os.path.join(PATH_TO_FIXTURES, path_to_file), 'r') as fixture:
        return fixture.read()
