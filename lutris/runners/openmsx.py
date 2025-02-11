# Standard Library
from gettext import gettext as _

from lutris.exceptions import MissingGameExecutableError
# Lutris Modules
from lutris.runners.runner import Runner
from lutris.util import system


class openmsx(Runner):
    human_name = _("openMSX")
    description = _("MSX computer emulator")
    platforms = [_("MSX, MSX2, MSX2+, MSX turboR")]
    flatpak_id = "org.openmsx.openMSX"
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "label": _("ROM file"),
            "help": _("The game data, commonly called a ROM image."),
        }
    ]

    def play(self):
        rom = self.game_config.get("main_file") or ""
        if not system.path_exists(rom):
            raise MissingGameExecutableError(filename=rom)
        return {"command": self.get_command() + [rom]}
