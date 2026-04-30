# src/metrics/base.py

from abc import ABC, abstractmethod

class Metric(ABC):
    
    @abstractmethod
    def compute(self, df, schema):
        pass