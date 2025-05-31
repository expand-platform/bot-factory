from dataclasses import dataclass


@dataclass
class Environment:
    development: str = "development"
    production: str = "production"

ENVIRONMENT = Environment()