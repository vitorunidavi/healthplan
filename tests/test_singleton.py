from infra.config_singleton import Config
from infra.logger_singleton import Logger


def test_config_singleton_uniqueness():
    c1 = Config()
    c2 = Config()

    assert c1 is c2
    assert c1.get("environment") == c2.get("environment")

    c1.set("environment", "production")
    assert c2.get("environment") == "production"


def test_logger_singleton_uniqueness():
    l1 = Logger()
    l2 = Logger()

    assert l1 is l2

    # test shared state
    l1.info("Test message")
    assert len(l2.logs) > 0
