class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def info(self, message):
        self.logs.append(f"[INFO] {message}")
        print(f"[INFO] {message}")

    def warn(self, message):
        self.logs.append(f"[WARN] {message}")
        print(f"[WARN] {message}")
