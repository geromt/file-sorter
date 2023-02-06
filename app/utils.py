import math
import os
from typing import Iterable

import click


def separate_by_number(number: int):
    buckets_dir = {}
    count = key = 0
    for entry in os.scandir():
        if entry.is_dir():
            continue

        if key in buckets_dir:
            buckets_dir[key].append(entry.name)
        else:
            buckets_dir[key] = [entry.name]

        count = (count + 1) % number
        if count == 0:
            key += 1

    return buckets_dir

            
def create_dirs(buckets_dir: dict, prefix: str = "", are_keys_int: bool = True,
                verbose: bool = False):
    """Given a dictionary of key:list_of_filename pairs, creates a directory
    for each key and move the files in the list to that directory. If the keys
    are strings you must pass the are_keys_int=False value

    Args:
        buckets_dir: Dictionary of key:list_of_filenames pairs
        prefix (optional): Prefix to name the directories that will be created
        are_keys_int (optional): Indicates if the keys are of int type. If the
            value is False, the keys are taken as strings and the directories
            are named as them.
        verbose (optional): If True, prints more information in the stdout.
    """
    for k in buckets_dir:
        if are_keys_int:
            dir_name = _form_name(k, len(buckets_dir), prefix)
        else:
            dir_name = prefix + k
        os.mkdir(dir_name)
        if verbose:
            click.echo(f"Create directory: {dir_name}")
        for f in buckets_dir[k]:
            os.rename("./" + f, "./" + dir_name + "/" + f)
            if verbose:
                click.echo(f"Move file: {f} -> {dir_name + '/' + f}")


def _form_name(index: int, total: int, prefix="") -> str:
    """Auxiliary private function. Form a string with the same number of
    digits as total. If prefix is passed, it is added at the beginning of the
    string"""
    if total != 0:
        digits = math.floor(math.log10(total)) + 1
    else:
        digits = 1

    if index != 0:
        index_digits = math.floor(math.log10(index)) + 1
    else:
        index_digits = 1

    zeros = digits - index_digits
    return prefix + ("0" * zeros) + str(index)