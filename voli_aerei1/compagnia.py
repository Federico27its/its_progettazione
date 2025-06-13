from My_Types import IntG1900
from typing import Any
from citta import Citta

class Compagnia():
    _nome: str # certamente noto alla nascita
    _anno_nascita: IntG1900 # <<imm>> certamente noto alla nascita

    def __init__(self, nome: str, anno: IntG1900, citta: Citta):
        self.set_nome(nome)
        self._anno_nascita = anno
        self.set_citta(citta)
 

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def anno_nascita(self) -> IntG1900:
        return self._anno_nascita
    
    def citta(self) -> Citta:
        return self._citta
    
    def set_citta(self, c: Citta) -> None:
        self._citta = c

    def __hash__(self) -> int:
        return hash((self.nome(), self.anno_nascita()))
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.nome(), self.anno_nascita()) == (other.nome(), other.anno_nascita())
    
    def __repr__(self) -> str:
        return self.nome()
    
