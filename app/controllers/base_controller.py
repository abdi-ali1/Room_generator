# app/controllers/base_controller.py
from fastapi import APIRouter
from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self, router_prefix: str) -> None:
        self.router = APIRouter(prefix=router_prefix)

    @abstractmethod
    def register_routes(self) -> None:
        pass
