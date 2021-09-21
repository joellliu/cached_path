import os
from os import PathLike
from pathlib import Path
from urllib.parse import urlparse
from typing import Union, Tuple

PathOrStr = Union[str, PathLike]

CACHE_DIRECTORY = Path(os.getenv("CACHED_PATH_CACHE_ROOT", Path.home() / ".cache" / "cached_path"))


def _split_cloud_path(url: str, provider: str) -> Tuple[str, str]:
    """Split a full s3 path into the bucket name and path."""
    parsed = urlparse(url)
    if not parsed.netloc or not parsed.path:
        raise ValueError("bad {} path {}".format(provider, url))
    bucket_name = parsed.netloc
    provider_path = parsed.path
    # Remove '/' at beginning of path.
    if provider_path.startswith("/"):
        provider_path = provider_path[1:]
    return bucket_name, provider_path