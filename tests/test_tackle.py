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
    create = tackle(**{
        "output": "test-output",
        "license_type": license,
    }, no_input=True)
    assert os.path.exists(os.path.join(create["output"], 'LICENSE'))
    shutil.rmtree("test-output")
