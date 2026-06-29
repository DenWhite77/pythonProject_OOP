class LogMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print("!!! ЛОГИРУЕМ СОЗДАНИЕ ОБЪЕКТА !!!")
        # Вызываем следующий конструктор в цепочке наследования
        self._log_params = {
            'args': args,
            'kwargs': kwargs
        }
        super().__init__()
        # Печатаем информацию о созданном объекте
        print(self.__repr__())

    def __repr__(self):
        """Возвращает строку с именем класса и параметрами."""
        # Получаем имя класса
        class_name = self.__class__.__name__
        # Если есть сохранённые параметры — используем их
        if hasattr(self, '_log_params'):
            args = self._log_params.get('args', ())
            kwargs = self._log_params.get('kwargs', {})
            # Формируем строку параметров
            params = ', '.join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
            return f"{class_name}({params})"
        # Если параметров нет — выводим атрибуты
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        # Формируем строку в формате ClassName(attr1=value1, attr2=value2, ...)
        params = ', '.join(f"{k}={v!r}" for k, v in attrs.items())
        return f"{class_name}({params})"
