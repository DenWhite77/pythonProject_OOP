from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Абстрактный базовый класс для всех моделей."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        pass
