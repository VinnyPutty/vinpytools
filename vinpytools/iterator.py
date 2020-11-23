from typing import Iterable, Sized, Iterator, Tuple, Reversible


def reverse_enumerate(collection: [Iterable, Sized, Reversible], start_index: int = None) -> Iterator[Tuple]:
    """
    Iterator form of reverse_enumerate.
    :param collection:
    :param start_index:
    :return: Iterator populated with tuples of (index, item) for each item in collection and its associated index
    :rtype: Iterator
    """
    # TODO: implement start_index functionality that mirrors enumerate builtin
    return zip(reversed(range(len(collection))), reversed(collection))
