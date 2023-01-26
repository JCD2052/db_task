class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return MetaSingleton._instances[cls]
