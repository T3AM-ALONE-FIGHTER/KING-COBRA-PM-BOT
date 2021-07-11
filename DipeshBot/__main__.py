import glob
from pathlib import Path
from DipeshBot.utils import load_plugins
import logging
from . import Dipesh

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "DipeshBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @CoffinXsupport")

if __name__ == "__main__":
    Dipesh.run_until_disconnected()
