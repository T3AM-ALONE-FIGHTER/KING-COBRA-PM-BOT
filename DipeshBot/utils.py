import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"DipeshBot/plugins/{plugin_name}.py")
    name = "DipeshBot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["DipeshBot.plugins." + plugin_name] = load
    print("DipeshBot has Imported " + plugin_name)
