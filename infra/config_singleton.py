class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._init_defaults()
        return cls._instance

    def _init_defaults(self):
        self.environment = "dev"
        self.database_url = "sqlite://memory"
        self.version = "1.0.0"

    def set(self, key: str, value):
        setattr(self, key, value)

    def get(self, key: str):
        return getattr(self, key, None)
