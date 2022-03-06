from .types import GenomeSize, PathLike, BedFile, BdgFile, BdgEntry, BedEntry
from typing import Union, List, Dict, Generator, Tuple, Optional

def map_bdg_on_bed(bed_file: BedFile, bdg_file: BdgFile, genome_size: GenomeSize=None) -> BdgFile:
    """
    :param bed_file: a bed file (in fact no need to be a "file", just need to be a bed entry generator)
    :param bdg_file: a bdg file
    :param genome_size: a dictionary of chr: size
    :return: a bdg file, but the region is the provided bed file, and score is the mean of the bdg score in the bed region
    """
    for bed_entry in bed_file:
        for bdg_entry in BdgFile:
            if bed_entry[0] != bdg_entry[0]:
                break

            