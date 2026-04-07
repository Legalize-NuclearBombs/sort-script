from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def calculate(self, data: list[dict]):
        pass
