class BaseObserver:
    def update(self, plan, event: str, **data):
        raise NotImplementedError
