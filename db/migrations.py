
from pathlib import Path

from alembic.config import Config
from alembic import command


class AlembicMigration:
    def __init__(self, base_dir: str = ''):
        self._base_dir = Path(base_dir)
        self._alembic_ini_path = str(self._base_dir / 'alembic.ini')
        self._init_config()

    def _init_config(self) -> None:
        self._alembic_cfg = Config(self._alembic_ini_path)
        self._alembic_cfg.set_main_option('script_location', str(self._base_dir / 'alembic'))

    def create_revision(self, comment: str, autogenerate: bool):
        try:
            command.revision(self._alembic_cfg, comment, autogenerate)
        except Exception:
            pass

    def run_upgrade_db(self, revision: str = 'head'):
        try:
            command.upgrade(self._alembic_cfg, revision)
        except Exception:
            pass

    def run_downgrade_db(self, revision: str = 'base'):
        try:
            command.downgrade(self._alembic_cfg, revision)
        except Exception:
            pass
