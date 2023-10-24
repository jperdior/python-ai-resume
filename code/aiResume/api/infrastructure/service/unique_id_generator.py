import ulid
from api.domain.service.unique_id_generator import UniqueIdGeneratorInterface


class UniqueIdGeneratorService(UniqueIdGeneratorInterface):
    def generateUlid(self) -> str:
        return str(ulid.new())
