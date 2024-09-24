# main.py
from fastapi import FastAPI
import os
import importlib
import inspect
import uvicorn
from contextlib import asynccontextmanager

# Create a lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up the API...")
    yield
    print("Shutting down the API...")

# Initialize the FastAPI application with the lifespan context manager
app = FastAPI(lifespan=lifespan)

# Directory containing controllers
controllers_path = os.path.join(os.path.dirname(__file__), "app", "controllers")

# Loop through all the files in the controllers directory
for filename in os.listdir(controllers_path):
    if filename.endswith(".py") and filename not in ["__init__.py", "base_controller.py"]:
        module_name = f"app.controllers.{filename[:-3]}"
        module = importlib.import_module(module_name)

        # Zoek naar alle klassen die afstammen van de BaseController
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ == module_name and hasattr(obj, 'register_routes'):
                # Instantiateer de controller
                controller_instance = obj()
                app.include_router(controller_instance.router)

# Als dit bestand direct wordt uitgevoerd, start de Uvicorn-server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
