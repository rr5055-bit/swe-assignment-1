# Loads the CV content from data.json
import json
from functools import lru_cache
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


@lru_cache(maxsize=1)
def load_cv():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))
