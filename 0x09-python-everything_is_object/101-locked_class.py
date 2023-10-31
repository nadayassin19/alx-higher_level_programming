#!/usr/bin/python3
"""A module of a locked class"""


class LockedClass:
    """that prevents the user from dynamically
    creating new instance attributes,
    except if the new instance attribute
    is called first_name.
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """init method
        """
        pass
