from typing import Any
from My_Types import IntGEZ

class Citta():
    _nome: str # certamente noto alla nascita
    _abitanti: IntGEZ

    def __init__(self, nome: str, abitanti: IntGEZ):
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def abitanti(self) -> IntGEZ:
        return self._abitanti
    
    def set_abitanti(self, abitanti: IntGEZ) -> None:
        self._abitanti = abitanti
   
    def __hash__(self) -> int:
        return hash((self.nome()))
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.nome()) == (other.nome())
    
    def __repr__(self) -> str:
        return self.nome()
    