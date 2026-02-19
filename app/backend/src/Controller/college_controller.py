import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
college_view_path = BASE_DIR.parent.parent.parent / 'frontend' / 'src' / 'views' / 'panels'
college_view_path = BASE_DIR.parent / 'Model' 
sys.path.insert(0, str(college_view_path))
sys.path.insert(0, str(college_view_path))

from college_model import CollegeModel
class CollegeController:
    def __init__(self, views):
        self.model = CollegeModel()
        self.views = views