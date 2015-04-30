import os

from gather_metrics import DATA_ROOT_DIR, PROJECT_ROOT_DIR
import run_metrics

import flask_project as project

data_dir = os.path.join(DATA_ROOT_DIR, project.DIR)
project_dir = os.path.join(PROJECT_ROOT_DIR, project.DIR)
commit = '941e11e54d175f4ffc769852e5dd376ec1ba5239'

run_metrics.gather_metrics(commit, project_dir, data_dir)
