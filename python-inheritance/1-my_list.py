#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements a sorted printing for the built in list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))