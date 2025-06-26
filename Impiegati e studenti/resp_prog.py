from classi import Impiegato, Progetto
from typing import Any


class Resp_Prog:
    impiegato: Impiegato
    _progetto: Progetto

    def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
        self._impiegato = impiegato
        self._progetto = progetto

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def progetto(self) -> Progetto:
        return self._progetto

    def __hash__(self)->int:
        return hash( (self.impiegato(), self.progetto()) )
    
    def __eq__(self, other:Any)->bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return ( self.impiegato(), self.progetto() ) == (other.impiegato(), other.progetto() )

'''class resp_prog:

    @classmethod
    def add(cls, impiegato: Impiegato, progetto:Progetto)->None:
        l = resp_prog._link(impiegato, progetto)
        l.impiegato()._add_link_resp(l)
        l.progetto()._add_link_resp(l)

    @classmethod
    def remove(cls, l:weakref[esame._link])->None:
        if l() is None:
            raise ValueError("l cannot be None")
        l().studente()._remove_link_esame(l())
        l().modulo()._remove_link_esame(l()) 
    class _link:
        _impiegato: Impiegato
        _progetto: Progetto

        def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
            self._impiegato = impiegato
            self._progetto = progetto

        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def progetto(self) -> Progetto:
            return self._progetto

        def __hash__(self)->int:
            return hash( (self.impiegato(), self.progetto()) )
        
        def __eq__(self, other:Any)->bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return ( self.impiegato(), self.progetto() ) == (other.impiegato(), other.progetto() )'''

