from enum import StrEnum, auto
from typing import Any
import re


class IntGZ(int):
    def __new__(cls, n: int | float | str | bool):
        if n > 0:
            return int.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be greater than 0")



class IntGEZ(int):
    def __new__(cls, n: int | float | str | bool):
        if n >= 0:
            return int.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be greater or equal to 0")
    
class IntG1900(int):
    def __new__(cls, n: int | float | str):
        if n > 1900:
            return int.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be greater than 1900")
   


class FloatGZ(float):
    def __new__(cls, n: float | int | str | bool):
        if n > 0:
            return float.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be greater than 0")



class FloatGEZ(float):
    def __new__(cls, n: float | int | str | bool):
        if n >= 0:
            return float.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be greater or equal to 0")
   


class FloatBZO(float):
    '''Rappresenta un numero reale compreso tra 0 e 1'''
    def __new__(cls, n: float |int | str | bool):
        if 0 <= n <= 1:
            return float.__new__(cls, n)
        raise ValueError(f"Value n: {n} must be between 0 and 1")
   


class Genere(StrEnum):
    uomo = auto()
    donna = auto()



class IndirizzoMail(str):
    def __new__(cls, s: str):
        if re.fullmatch(r"[a-zA-Z0-9._-]+@\w+\.\w+", s):
            return str.__new__(cls, s)
        raise ValueError(f"Invalid Email format")
       


class Valuta(str):
    def __new__(cls, val: str):
        if len(val.upper()) == 3 and val.isalpha():
            return str.__new__(cls, val)
        raise ValueError(f"Invalid Valuta format")



class Denaro():
    _importo: float
    _valuta: Valuta


    def __init__(self, importo: float, valuta: Valuta) -> None:
        self._importo = float
        self._valuta = valuta
   
    def importo(self) -> float:
        return self._importo
   
    def valuta(self) -> Valuta:
        return self._valuta


    def __hash__(self) -> int:
        return hash( (self.importo(), self.valuta()) )
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.importo(), self.valuta() ) == (other.importo(), other.valuta())
   


class Telefono(str):
    def __new__(cls, s:str):
        if re.fullmatch(r"(?:\+39)?(?:0\d{1,3}\d{5,7}|3\d{2}\d{6,7})", s):
            return str.__new__(cls, s)
        raise ValueError(f"Invalid phone number format")



class Targa(str):
    def __new__(cls, s:str):
        if re.fullmatch(r"[A-Z]{2}\d{3}[A-Z]{2}"):
            return str.__new__(cls, s)
        raise ValueError(f"Invalid license plate format")
   


class Matricola(str):
    def __new__(cls, s:str):
        if s.isdigit():
            return str.__new__(cls,s)
        raise ValueError(f"Invalid ID number format")



'''class Nazione():
    _nome:str
    _regioni: list["Regione"]


    def __init__(self, nome: str, regioni = None, citta = None):
        self._nome = nome
        self._regioni = regioni if regioni else []


    def nome(self) -> str:
        return self._nome
   
    def regioni(self) -> list:
        return self._regioni
   
    def __hash__(self) -> int:
        return hash(self.nome())
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return self.name() == other.name()
       
   
class Regione():
    _nome: str
    _nazione: Nazione
    _citta: list["Citta"]


    def __init__(self, nome: str, nazione: Nazione, citta = None):
        self._nome = nome
        self._nazione = nazione
        self_citta = citta if citta else []


    def nome(self) -> str:
        return self._nome
   
    def nazione(self) -> Nazione:
        return self._nazione
   
    def citta(self) -> list:
        return self._citta
   
    def __hash__(self) -> int:
        return hash(self.nome(), self.nazione())
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.name(), self.nazione()) == (other.name(), other.nazione())
   


class Citta():
    _nome: str
    _regione: Regione


    def __init__(self, nome: str, regione: Regione):
        self._nome = nome
        self._regione = regione


    def nome(self) -> str:
        return self._nome
   
    def regione(self) -> Regione:
        return self._regione
   
    def nazione(self) -> Nazione:
        return self._regione.nazione()
   
    def __hash__(self) -> int:
        return hash(self.nome(), self.regione())
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.name(), self.regione()) == (other.name(), other.regione())
'''

class CAP(str):
    def __new__(cls, s: str):
        if re.fullmatch(r"\d{5}"):
            return super.__new__(cls, s)
        raise ValueError("Invalid CAP format")
class Indirizzo:
    _via: str
    _numero_civico: str
    _cap: str


    def __init__(self, via: str, numero_civico: str, cap: str) -> None:
        self._via = via
        self._numero_civico = numero_civico
        self._cap = cap


    def via(self) -> str:
        return self._via
   
    def numero_civico(self) -> str:
        return self._numero_civico


    def cap(self) -> str:
        return self._cap
   
    def __hash__(self) -> int:
        return hash( (self.via(), self.numero_civico(), self.cap()) )
   
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False    
        return (self.via(), self.numero_civico(), self.cap() ) == (other.via(), other.numero_civico(), other.cap())
   


class CodiceFiscale(str):
    def __new__(cls, s: str):
        if re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]", s.strip()):
            return str.__new__(cls, s)
        raise ValueError(f"Invalid Codice Fiscale format.")




class PartitaIva(str):
    def __new__(cls, s: str):
        if len(s) == 11 and s.isdigit():
            return str.__new__(cls, s)
        raise ValueError(f"Invalid Partita Iva format.")



if __name__ == "__main__":
    eur = Valuta.EUR
    usd = Valuta.USD
    d1 = Denaro(float(30), eur)
    d2 = Denaro(34, usd)
    eur2 = Valuta.EUR
    print(eur)
    print(eur == eur2)
    print(d1 == d2)
    d2 = Denaro(float(30), eur2)
    print(d1 == d2)
       
    d3 = Denaro(float(30), eur2)
    print(d1 == d3)


    i1 = Indirizzo("Viale Cesare Pavese", "666", "nonloso")
    i2 = Indirizzo("Viale Cesare Pavese", "666", "nonloso")
    print(id(i1), id(i2))
    print(hash(i1), hash(i2))
    print(i1 == i2)


    cf = CodiceFiscale("RSSRRT80L04F205H")
    print(cf)
    s = "RSSRRT80L04F205H"
    print(id(cf), id(s), hash(cf), hash(s))
    print(cf==s)