import os
import glob
from . import config

def list_ebooks():
    if not os.path.exists(config.EBOOK_DIR):
        os.makedirs(config.EBOOK_DIR)
        print(f"Created eBook directory: {config.EBOOK_DIR}")

    ebooks = []
    for ext in config.SUPPORTED_FORMATS:
        pattern = os.path.join(config.EBOOK_DIR, f"*{ext}")
        ebooks.extend(glob.glob(pattern))
    return ebooks
