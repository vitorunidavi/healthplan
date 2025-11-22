from .base_observer import BaseObserver
from infra.logger_singleton import Logger

class QuotaObserver(BaseObserver):
    def update(self, plan, event: str, **data):
        logger = Logger()

        if event == 'quota_high':
            logger.warn(f"Uso acima de 80% no plano {plan.name}. Total: R${data.get('total'):.2f}")

        elif event == 'quota_exceeded':
            logger.warn(f"Cota excedida no plano {plan.name}! Total: R${data.get('total'):.2f}")
