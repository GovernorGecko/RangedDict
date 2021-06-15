"""
    rangeddict.py
"""

from .RedBlackTree.src.redblacktree import RedBlackTree


class RangedDict(RedBlackTree):
    """
    By using RedBlackTree, we create a Ranged Dictionary.
    """

    # Valid instances of data
    __valid_instances = (int, float)

    __slots__ = []

    def __init__(self):
        super(RangedDict, self).__init__(
            self.__ranged_dict_comparator,
            self.__ranged_dict_equals,
            self.__ranged_dict_validator
        )

    def __getitem__(self, key):
        """
        parameters:
            int
        returns:
            var
        """
        node, _ = self.find_node(key)
        return node._values[0]

    def __ranged_dict_comparator(self, key_one, key_two):
        """
        < or >
        parameters:
            tuple, int, or float
            tuple, int, or float
        returns
            bool or None
        """

        if isinstance(key_one, tuple):
            if key_one[1] < key_two[0]:
                return True
            elif key_one[0] > key_two[1]:
                return False
            else:
                raise Exception(
                    f"Overlap! {key_one} already exists in some form!"
                )
        elif isinstance(key_one, self.__valid_instances):
            if key_one < key_two[0]:
                return True
            return False
        return None

    def __ranged_dict_equals(self, key_one, key_two):
        """
        =
        parameters:
            tuple, int, or float
            tuple, int, or float
        returns:
            bool or None
        """

        if (
            isinstance(key_one, self.__valid_instances) and
            key_one >= key_two[0] and key_one <= key_two[1]
        ):
            return True
        elif isinstance(key_one, tuple) and key_one == key_two:
            return True
        return False

    def __ranged_dict_validator(self, key):
        """
        Valid key data?
        parameters:
            tuple
            tuple
        returns:
            bool
        Returns if the given key is valid for our RBTree
        """

        if isinstance(key, tuple):
            for k in key:
                if not isinstance(k, self.__valid_instances):
                    return False
            return True
        return False
