from pathlib import Path
from nacl.utils import random
from appdirs import user_cache_dir, user_data_dir, user_config_dir


def shred_file(path: Path):
    """Shreds a file by first overwriting it with random data of same size so that it cannot be recovered"""

    # Check if file exists
    if not (path.exists() or path.is_file()):
        raise FileNotFoundError("File does not exist")

    # Overwrite file with random data
    size = path.stat().st_size
    random_bits = random(size)
    with open(path, "wb") as file:
        file.write(random_bits)

    # Delete file
    path.unlink()


def write_chunks(chunks, path: Path):
    """Writes chunks (list of bytes) to a binary file"""
    with open(path, "wb") as outfile:
        for chunk in chunks:
            outfile.write(chunk)


def write_bytes(data: bytes, path: Path):
    """Writes bytes to a binary file"""
    with open(path, "wb") as file:
        file.write(data)


class Directories:
    """A class that contains the directories used by cryptbuddy"""

    def __init__(self):
        self.cache_dir = Path(user_cache_dir("cryptbuddy"))
        self.data_dir = Path(user_data_dir("cryptbuddy"))
        self.config_dir = Path(user_config_dir("cryptbuddy"))

    def __repr__(self):
        return f"<Directories {self.cache_dir} {self.data_dir} {self.config_dir}>"

    def __str__(self):
        return f"<Directories {self.cache_dir} {self.data_dir} {self.config_dir}>"

    @staticmethod
    def create_directories():
        """Creates the directories used by cryptbuddy"""
        Directories().cache_dir.mkdir(parents=True, exist_ok=True)
        Directories().data_dir.mkdir(parents=True, exist_ok=True)
        Directories().config_dir.mkdir(parents=True, exist_ok=True)