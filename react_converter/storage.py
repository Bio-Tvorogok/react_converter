import logging
import tarfile
from pathlib import Path

from react_converter.settings import settings

logger = logging.getLogger(__name__)


class TemplateStorage:
    def __init__(self, path: Path):
        self._files: dict[str, bytes | None] = {}
        self.path = path

    def start_up(self):
        logger.debug("Startup loading template")
        with tarfile.open(self.path, "r:gz") as file:
            for member in file:
                logger.debug(member.path)
                if member.isdir():
                    self._files[member.path] = None
                else:
                    self._files[member.path] = file.extractfile(
                        member.name
                    ).read()
        logger.debug("Finish loading template")

    @property
    def files(self) -> dict[str, bytes | None]:
        return self._files


template_storage = TemplateStorage(settings.TEMPLATE)
