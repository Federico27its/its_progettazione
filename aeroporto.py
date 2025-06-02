from typing import Any

class Aeroporto():
    _codice: str # <<imm>> certamente noto alla nascita
    _nome: str # certamente noto alla nascita

    def __init__(self, codice: str, nome: str):
        self._codice = codice
        self.set_nome(nome)

    def codice(self) -> str:
        return self._codice

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def __hash__(self) -> int:
        return hash(self.codice())
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.codice(), self.nome()) == (other.codice(), other.nome())
    
    def __repr__(self) -> str:
        return self.nome()