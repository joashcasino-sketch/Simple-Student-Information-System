import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
program_view_path = BASE_DIR.parent.parent.parent / 'frontend' / 'src' / 'views' / 'panels'
program_model_path = BASE_DIR.parent / 'Model' 
sys.path.insert(0, str(program_view_path))
sys.path.insert(0, str(program_model_path))

from program_model import ProgramModel
class ProgramController:
    def __init__(self, views):
        self.model = ProgramModel()
        self.views = views