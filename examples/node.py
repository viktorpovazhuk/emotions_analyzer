"""
File: node.py
Author: Ken Lambert
"""


class Node(object):
    """Nodes for singly linked structures."""

    def __init__(self, data, previous=None, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.previous = previous
        self.next = next
