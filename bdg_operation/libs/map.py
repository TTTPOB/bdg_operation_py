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
                # here is a problem need to be done, chromosome switching, I need to find a way to switch chromosomes
                # maybe I can let the two loop compare with their last entry
                # here is two situations:
                # 1. bedgraph on chr2, but bed has no chr2, in this case I need to make bdg loop(inner loop) "continue"
                # 2. bed on chr2, but bedgraph has no chr2, if I let bedgraph continue directly, bed will stuck on this entry
                # oh I think I figured it out, the goal is the map bedgraph scores to bed, so I need only to consider bed entry
                # when they have different chromosomes, I can "compare" them using the default sort method, and determine if I
                # should score this region as 0
                break

            