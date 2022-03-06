from email.generator import Generator
from pathlib import Path
from .types import GenomeSize, PathLike, BedFile, BdgFile
from typing import Union
import gzip

BED_COLNAMES = ["chr", "start", "end", "name", "score", "strand"]
BDG_COLNAMES = ["chr", "start", "end", "score"]

def read_tsv(path: PathLike) -> Union[BedFile, BdgFile]:
    """
    :param path: path to a bed file
    :return: a bed file generator
    """
    if Path(path).suffix == ".gz":
        handle = gzip.open(path, "rt")
    else:
        handle = open(path, "r")
    for line in handle:
        if line.startswith("#"):
            continue
        line = line.strip().split("\t")
        yield tuple(line)
    handle.close()

def read_genome_size(path: PathLike) -> GenomeSize:
    """
    :param path: path to a bed file
    :return: a dictionary of chr: size
    """
    genome_size = {}
    if Path(path).suffix == ".gz":
        handle = gzip.open(path, "rt")
    else:
        handle = open(path, "r")
    for line in handle:
        if line.startswith("#"):
            continue
        line = line.strip().split("\t")
        genome_size[line[0]] = int(line[1])
    handle.close()
    return genome_size