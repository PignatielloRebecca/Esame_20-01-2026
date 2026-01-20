from dataclasses import dataclass

@dataclass
class Generi:
    id : int
    name : str
    genere:str

    def __str__(self):
        return f"{self.id}, {self.name}, {self.genere}"

    def __hash__(self):
        return hash(self.id)