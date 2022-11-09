from pydantic import BaseModel


class Country(BaseModel):
    name: str


class Network(BaseModel):
    name: str
    country: Country


class TvProgramModel(BaseModel):
    name: str
    network: Network
    summary: str
