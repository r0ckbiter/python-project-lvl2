from gendiff import generate_diff
import tests.expected as expected


def test_string():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           )
    assert actual == expected.SIMPLE_STRING
    assert actual == expected
