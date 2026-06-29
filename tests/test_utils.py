import json
import sys
import tempfile
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'src'))

from utils import load_data_from_json  # noqa: E402


def test_load_data_from_json_success():
    data = [{"name": "Cat1", "description": "Desc1", "products": []}]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f)
        f.flush()
        result = load_data_from_json(f.name)
        assert len(result) == 1
        assert result[0].name == "Cat1"
    Path(f.name).unlink()


def test_load_data_from_json_file_not_found():
    result = load_data_from_json("non_existent.json")
    assert result == []


def test_load_data_from_json_invalid_json():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write("{invalid json}")
        f.flush()
        result = load_data_from_json(f.name)
        assert result == []
    Path(f.name).unlink()
