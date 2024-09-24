import os
import importlib
import inspect

controllers_path = os.path.dirname(__file__)
routers = []

for filename in os.listdir(controllers_path):
    if filename.endswith(".py") and filename not in ["__init__.py", "base_controller.py"]:
        module_name = f"app.controllers.{filename[:-3]}"
        module = importlib.import_module(module_name)

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ == module_name and hasattr(obj, 'register_routes'):
                controller_instance = obj()
                routers.append(controller_instance.router)
