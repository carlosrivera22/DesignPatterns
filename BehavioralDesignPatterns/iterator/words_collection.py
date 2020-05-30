from order_iterator import OrderIterator
from collections.abc import Iterable
from typing import Any, List
class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self):
   
        return OrderIterator(self._collection)

    def get_reverse_iterator(self):
        return OrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)
