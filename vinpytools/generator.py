import inspect
from typing import Iterable, Sized, Generator, Tuple, Collection, Dict, Coroutine, Reversible, Union, List

from vinpytools.iterator import reverse_enumerate as reverse_enumerate_iterator


def reverse_enumerate(collection: [Iterable, Sized, Reversible], start_index: int = None) -> Generator:
    """
    Generator form of reverse_enumerate. Uses the iterator from the iterator version to procedurally generate and yield
        tuples. Exists only to mirror the functionality of the enumerate builtin, as it returns a generator object.
    :param collection:
    :param start_index:
    """
    # TODO: implement start_index functionality that mirrors enumerate builtin
    yield from reverse_enumerate_iterator(collection, start_index=start_index)


def array_traversal(coordinates: Union[List, Tuple], collection: Union[List, Tuple] = None,
                    valid_orientations: Tuple = None, custom_conditions: List = None):
    """

    :param coordinates:
    :param collection:
    :param valid_orientations: either a list of tuples
    :param custom_conditions: a list of single parameter functions that accept the index and return a boolean that
    determines whether or not the coordinate is valid
    :return
    :rtype: Generator
    """
    # TODO handle n-dimensional arrays without hard-coding

    # FIXME refactor function name
    def _33_axis_len():
        next_axis = collection
        for depth in range(len(coordinates)):
            yield len(next_axis)
            next_axis = next_axis[0]

    axis_len_gen = _33_axis_len()

    # Hard-coded default conditions for valid coordinate tuples
    if collection:
        default_conditions = {
            0: lambda index: 0 <= index < len(collection),
            1: lambda index: 0 <= index < len(collection[0]),
            2: lambda index: 0 <= index < len(collection[0][0]),
            3: lambda index: 0 <= index < len(collection[0][0][0]),
            4: lambda index: 0 <= index < len(collection[0][0][0][0]),
        }

    if not custom_conditions:
        custom_conditions = [None] * len(coordinates)

    if len(custom_conditions) < len(coordinates):
        custom_conditions.extend([None] * (len(coordinates) - len(custom_conditions)))

    for condition_index, custom_condition in enumerate(custom_conditions[:len(coordinates)]):
        next_axis_length = next(axis_len_gen)
        if not custom_condition:
            custom_conditions[condition_index] = \
                lambda index: 0 <= index < next_axis_length

    print(f'Populated conditions: {[inspect.getsource(func) for func in custom_conditions]}')

    # TODO generate and yield next valid coordinates (adjacent for uni-dimensional array, clockwise for bi-dimensional
    #   array, etc.)


if __name__ == '__main__':
    pass
