import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

projectName = 'textSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{projectName}/__init__.py',
    f'src/{projectName}/components/__init__.py',
    f'src/{projectName}/utils/__init__.py',
    f'src/{projectName}/utils/common.py',
    f'src/{projectName}/logging/__init__.py',
    f'src/{projectName}/pipeline/__init__.py',
    f'src/{projectName}/config/__init__.py',
    f'src/{projectName}/config/configuration.py',
    f'src/{projectName}/entity/__init__.py',
    f'src/{projectName}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory {file_dir} for the file {file_name}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
            logging.info(f'Create the the file: {filepath}')
    else:
        logging.info(f'The file: {filepath} is already exists')
