from abc import ABC, abstractmethod

class Block:
    """
    Abstract class that defines the basic structure of a block.
    """
    def __init__(self):
        pass

    @abstractmethod
    def is_blocked(self) -> bool:
        pass