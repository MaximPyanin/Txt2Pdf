from dependency_injector.wiring import inject, Provide
from dotenv import load_dotenv

from app.container import Container
from app.api.api__handler import ConverterHandler


@inject
def main(handler: ConverterHandler = Provide[Container.handler]):
    return handler.app


load_dotenv()
container = Container()
container.init_resources()
container.wire(modules=[__name__])
app = main()
