from abc import abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Metric:
    title: str
    metric_type: Optional[str]
    brief: Optional[str]
    description: str


class Fetcher:
    @abstractmethod
    def list(self) -> List[str]:
        pass

    @abstractmethod
    def get(self, id) -> List[Metric]:
        pass
