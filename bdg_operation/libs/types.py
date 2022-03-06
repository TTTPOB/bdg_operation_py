import os
from typing import List, Dict, Union, Generator, Tuple, Optional

PathLike = Union[str, os.PathLike]
BedEntry = Tuple[str, int,int, Optional[str], Optional[int], Optional[str]]
BdgEntry = Tuple[str, int, int, float]
BedFile = Generator[BedEntry, None, None]
BdgFile = Generator[BdgEntry, None, None]
GenomeSize = Dict[str, int]