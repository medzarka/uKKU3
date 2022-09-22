
from shutil import copytree, ignore_patterns, copy
from pathlib import Path
import os

##### configuration:
PROJECT__NAME = 'uKKU3'


#################################################
############# Don not touch what follows :
HOME_DIR = Path(__file__).resolve().parent.parent.parent
REPOSITORY_DIR = os.path.join(HOME_DIR, 'repositories', PROJECT__NAME)
BASE_DIR = Path(__file__).resolve().parent.parent
passenger_template_file = os.path.join(BASE_DIR, PROJECT__NAME, 'passenger_wsgi.template.py')
passenger_real_file = os.path.join(BASE_DIR, 'passenger_wsgi.py')

try:
    print('copying the files from the Git local repository...')
    copytree(REPOSITORY_DIR, BASE_DIR, dirs_exist_ok=True, ignore=ignore_patterns('.git', ))
    print('Done.')

    print('Updating the passenger wsgi file...')
    f = open(passenger_real_file, mode='w', encoding='UTF-8')
    f.write('from uKKU3.wsgi import application \n' )
    f.close()
    #copy(passenger_template_file, passenger_real_file)
    print('Done.')


except Exception as e:
    print("Error in copying the files.")
    print(str(e))
