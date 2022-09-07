import pytest
import os
from gendiff import diff_builder


PATH = 'tests/fixtures/'


@pytest.mark.parametrize('path_to_first, path_to_second, expected_result', [
        ('file1.json', 'file2.json', 'expect'),
        ('file1.yml', 'file2.yml', 'expect'),
        ])
def test_generate_diff(path_to_first, path_to_second, expected_result):
    test_data = collect_data('expect')
    assert diff_builder.generate_diff(path_to_first, path_to_second) == test_data


def collect_data(filename):
    with open(os.path.join(PATH, filename), 'r') as fixture:
        return fixture.read()
