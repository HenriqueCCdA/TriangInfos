import os

import pytest

from api.config import Settings


@pytest.fixture
def set_cors_env():
    os.environ["TRIANG_INFOS_API_CORS"] = "http://localhost:3000,https://localhost:3001"
    yield
    del os.environ["TRIANG_INFOS_API_CORS"]


def test_positive_env(set_cors_env):
    settings = Settings()

    assert settings.CORS == (
        "http://localhost:3000",
        "https://localhost:3001",
    )


def test_positive_dotenv():
    Settings.model_config["env_file"] = "tests/env_files/env1"

    settings = Settings()

    assert settings.CORS == ("http://localhost:8000",)


def test_positive_env_precedes_dotenv(set_cors_env):
    Settings.model_config["env_file"] = "tests/env_files/env1"

    settings = Settings()

    assert settings.CORS == (
        "http://localhost:3000",
        "https://localhost:3001",
    )
