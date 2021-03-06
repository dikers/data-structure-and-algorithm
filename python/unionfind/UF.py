from abc import abstractmethod


class UF:
    @abstractmethod
    def is_connected(self, p: int, q: int) -> bool:
        return False

    @abstractmethod
    def union_elements(self, p: int, q: int):
        pass

    @abstractmethod
    def get_size(self) -> int:
        return 0