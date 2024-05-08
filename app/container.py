from dependency_injector import containers, providers
from app.services.config_service import AppConfig
import os
from app.api.api__handler import ConverterHandler


class Container(containers.DeclarativeContainer):
    config = providers.Factory(AppConfig, env=os.environ)
    handler = providers.Singleton(ConverterHandler)
