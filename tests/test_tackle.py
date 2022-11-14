import pytest
from tackle import tackle
import os
import shutil

LICENSE = [
    'apache',
    'mit',
    'gpl-v3',
    'bsd',
    'closed-source',
]

@pytest.mark.parametrize("license", LICENSE)
def test_all(change_base_dir, license):
    tackle(**{
        "output": "output",
        "license_type": license,
        "author": 'Foo',
        "start_date": 2022,
        "end_date": 2022,
    }, no_input=True)
    assert os.path.exists(os.path.join('output', 'LICENSE'))
    shutil.rmtree("output")
