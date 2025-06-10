from __future__ import annotations
from datetime import date
from My_Types import CodiceFiscale, IntG1088, IntGEZ

class Citta():
    _nome: str # certamente noto alla nascita
    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome



class Nazione():
    _nome: str # certamente noto alla nascita
    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome


class Studente():
    _nome: str # certamente noto alla nascita
    _codice_fiscale: CodiceFiscale # certamente noto alla nascita
    _matricola: str # <<immutabile>> certamente noto alla nascita
    _data_nascita: date # <<immutabile>> certamente noto alla nascita
    _citta: Citta # <<immutabile>> certamente noto alla nascita

    def __init__(self, nome: str, codice: CodiceFiscale, matricola: str, data: date, citta: Citta) -> None:
        self.set_nome(nome)
        self.set_codice_fiscale(codice)
        self._matricola = matricola
        self._data_nascita = data
        self._citta = citta

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def set_codice_fiscale(self, codice: CodiceFiscale) -> None:
        self._codice_fiscale = codice

    def matricola(self) -> str:
        return self._matricola
    
    def data_nascita(self) -> date:
        return self._data_nascita
    
    def citta(self) -> Citta:
        return self._citta
    


class Professore():
    _nome: str # certamente noto alla nascita
    _data_nascita: date # <<immutabile>> certamente noto alla nascita
    _codice_fiscale: CodiceFiscale # certamente noto alla nascita
    _citta: Citta # <<immutabile>> certamente noto alla nascita

    def __init__(self, nome: str, codice: CodiceFiscale, data: date, citta: Citta) -> None:
        self.set_nome(nome)
        self._data_nascita = data
        self.set_codice_fiscale(codice)
        self._citta = citta

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def data_nascita(self) -> date:
        return self._data_nascita

    def codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def set_codice_fiscale(self, codice: CodiceFiscale) -> None:
        self._codice_fiscale = codice
    
    def citta(self) -> Citta:
        return self._citta



class Corso():
    _codice: str # <<immutabile>> certamente noto alla nascita
    _nome: str # certamente noto alla nasctia
    _numero_ore: IntGEZ # certamente noto alla nascita

    def __init__(self, codice: str, nome: str, ore: IntGEZ) -> None:
        self._codice = codice
        self.set_nome(nome)
        self.set_numero_ore(ore)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def numero_ore(self) -> IntGEZ:
        return self._numero_ore
    
    def set_numero_ore(self, ore: IntGEZ) -> None:
        self._numero_ore = ore

    def codice(self) -> str:
        return self._codice



class Facolta():
    _nome: str # certamente noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
    
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome



class Tipo():
    _tipo: str # <<immutabile>> certamente noto alla nascita
    
    def __init__(self, tipo: str) -> None:
        self._tipo = tipo

    def tipo(self) -> str:
        return self._tipo


class Studente_Facolta():
    _anno_iscrizione: IntG1088 # <<immutabile>> certamente noto alla nascita

    def __init__(self, anno: IntG1088) -> None:
        self._anno_iscrizione = anno

    def anno_iscrizione(self) -> IntG1088:
        return self._anno_iscrizione