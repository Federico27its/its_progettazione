from __future__ import annotations
from custom_types import *
from My_Types import IntGZ, Ruolo


class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo

    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, pos: PosizioneMilitare|None=None) -> None:
        self._nome = nome
        self._cognome = cognome
        self._genere = None
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")
        self._cf = cf

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)

        if genere == Genere.uomo:
            if pos is None:
                raise ValueError("È obbligatorio fornire la posizione militare per gli uomini")
            self.diventa_uomo(pos)


    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()


    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None


    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")
        self._maternita = maternita
        

    def diventa_uomo(self, pos: PosizioneMilitare) -> None:
        if self._genere == Genere.uomo:
            raise RuntimeError("La persona era già un uomo!")
        self._genere = Genere.uomo
        self.set_posizione_mil(pos)
        self.__dimentica_donna()


    def __dimentica_donna(self) -> None:
        self._maternita = None


    def set_posizione_mil(self, pos: PosizioneMilitare) -> None:
        if not self._genere == Genere.uomo:
            raise RuntimeError("Le donne non hanno la posizione militare!")
        self._posizione_mil = pos

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def cf(self) -> CodiceFiscale:
        return self._cf
    
    def genere(self) -> Genere:
        return self._genere
    
    def maternita(self) -> IntGEZ:
        return self._maternita
    
    def pos_mil(self) -> PosizioneMilitare:
        return self._posizione_mil



class Impiegato(Persona):
    _stipendio: RealGEZ
    _ruolo: Ruolo
    _is_responsabile: bool
    _resp_prog: dict['Progetto': 'Resp_prog']
    
    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, 
               pos: PosizioneMilitare|None=None, stipendio: RealGEZ, ruolo: Ruolo) -> None:
        super().__init__(nome = nome, cognome = cognome, cf = cf, genere = genere, maternita = maternita, pos = pos)
        from resp_prog import Resp_Prog
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        if ruolo == Ruolo.progettista:
            self._is_responsabile = False
        else:
            self._is_responsabile = None
        self._resp_prog = {}

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def set_ruolo(self, ruolo: Ruolo) -> None:
        self._ruolo = ruolo

    def set_responsabile(self, resp: bool) -> None:
        self._is_responsabile = resp

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def is_responsabile(self) -> bool:
        return self._is_responsabile
    
    def progetti(self) -> dict['Progetto', 'Resp_Prog']:
        return self._resp_prog
    
    def __repr__(self) -> str:
        return self.nome()


class Studente(Persona):
    _matricola: IntGZ
    _matricole: set[IntGZ] = set()
    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, pos: PosizioneMilitare|None=None, matricola: IntGZ) -> None:
        if matricola in self._matricole:
            raise ValueError("Esiste già uno studente con questo numero di matricola!")
        super().__init__(nome, cognome, cf, genere, maternita, pos)
        self._matricola = matricola
        self._matricole.add(matricola)

    def matricola(self) -> IntGZ:
        return self._matricola

class Progetto:
    _nome: str
    _resp_prog: dict[Impiegato, 'Resp_Prog']
    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._resp_prog = {}

    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def nome(self) -> str:
        return self._nome
    
    def add_responsabile(self, impiegato: 'Impiegato') -> None:
        from resp_prog import Resp_Prog
        if impiegato.ruolo() != Ruolo.progettista:
            raise ValueError("L'impiegato non è un progettista!")
        if impiegato not in self._resp_prog:
            resp: 'Resp_Prog' = Resp_Prog(self, impiegato)
            self._resp_prog[impiegato] = resp
            impiegato._resp_prog[self] = resp
            impiegato.set_responsabile(True)
        else:
            raise ValueError("L'impiegato è già responsabile del progetto!")
        
    def remove_responsabile(self, impiegato:'Impiegato') -> None:
        if impiegato in self._resp_prog:
            self._resp_prog.pop(impiegato)
            impiegato._resp_prog = None
        else:
            raise ValueError("L'impiegato non è responsabile del progetto!")
        
    def responsabili(self) -> dict['Impiegato', 'Resp_Prog']:
        return self._resp_prog
    
    def __repr__(self) -> str:
        return self.nome()

class PosizioneMilitare:
    _posizioni_militari: set[str] = set()
    _nome: str # <<imm>> 
    
    def __init__(self, nome: str) -> None:
        if nome in PosizioneMilitare._posizioni_militari:
            raise ValueError("Posizione militare già esistente!")
        self._nome = nome
        PosizioneMilitare._posizioni_militari.add(nome)

    def nome(self) -> str:
        return self._nome

if __name__ == "__main__":

    p1 = Persona(nome="Alice", cognome = "Alice", cf = CodiceFiscale("A"*16), genere = Genere.donna, maternita = IntGEZ(150))
    print(p1.nome(), p1.cognome(),p1.cf(),p1.genere(),p1.maternita(), p1.pos_mil())

    p1 = Impiegato(nome="Alice", cognome = "Alice", cf = CodiceFiscale("A"*16), genere = Genere.donna, maternita = IntGEZ(150), stipendio = RealGEZ(0.00000001), ruolo = Ruolo.progettista)

    print(p1.nome(), p1.cognome(),p1.cf(),p1.genere(),p1.maternita(), p1.pos_mil(), p1.stipendio(), p1.ruolo(), p1.is_responsabile())

    prog = Progetto("progettone")
    print(prog.nome())
    prog.add_responsabile(p1)
    print(prog.responsabili())
    print(p1.progetti())
    prog.remove_responsabile(p1)
    print(prog.responsabili())
    print(p1.progetti())
