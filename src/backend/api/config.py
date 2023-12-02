from typing import Any

from pydantic.fields import FieldInfo
from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class TupleParseMixin:
    def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
        if field_name == "CORS" and value is not None:
            return tuple(s.strip() for s in value.split(","))

        return value


class MyEnvSettingsSource(TupleParseMixin, EnvSettingsSource):
    ...


class MyDotEnvSettingsSource(TupleParseMixin, DotEnvSettingsSource):
    ...


class Settings(BaseSettings):
    CORS: tuple[str, ...] = ("",)

    model_config = SettingsConfigDict(
        env_prefix="TRIANG_INFOS_API_",
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            MyEnvSettingsSource(settings_cls),
            MyDotEnvSettingsSource(settings_cls),
        )


settings = Settings()
