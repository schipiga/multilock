import threading
import weakref


__all__ = (
    'MultiLock',
    'MultiRLock',
)


class BaseLock:

    def __init__(self):
        self._locks = weakref.WeakKeyDictionary()

    def __call__(self, key):
        return self._locks[key]

    def add(self, key):
        raise NotImplementedError


class MultiLock(BaseLock):

    def add(self, key):
        self._locks[key] = threading.Lock()


class MultiRLock(BaseLock):

    def add(self, key):
        self._locks[key] = threading.RLock()
