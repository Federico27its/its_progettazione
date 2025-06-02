from My_Types import IntGZ
from typing import Any

class Volo():
    _codice: str # <<imm>> certamente noto alla nascita
    _durata_min: IntGZ # certamente noto alla nascita

    def __init__(self, codice: str, durata: IntGZ):
        self._codice = codice
        self.set_durata_min(durata)

        self._compagnia = None
        self._partenza = None
        self._arrivo = None

    def codice(self) -> str:
        return self._codice
    
    def set_codice(self, codice: str) -> None:
        self._codice = codice

    def durata_min(self) -> IntGZ:
        return self._durata_min
    
    def set_durata_min(self, durata_min: IntGZ) -> None:
        self._durata_min = durata_min

    def __hash__(self) -> int:
        return hash(self.codice())
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.codice(), self.durata_min()) == (other.codice(), other.durata_min())