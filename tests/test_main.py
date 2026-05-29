import pytest
import os

def test_yangi_fayl_yaratish():
    import tempfile
    from pathlib import Path

    def yarat_fayl():
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            f.close()
            return Path(f.name)

    fayl = yarat_fayl()
    assert fayl.exists()
    os.remove(fayl)
