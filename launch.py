import subprocess
import os

subprocess.run(['python', 'manage.py', 'migrate'])
os.chdir('tracking/fixtures') 
subprocess.run(['python', 'load_data.py'])
os.chdir('/code')
subprocess.run(['python', 'manage.py', 'loaddata', 'tracking/fixtures/ships.json'])
subprocess.run(['python', 'manage.py', 'loaddata', 'tracking/fixtures/position.json'])
os.remove('tracking/fixtures/ships.json')
os.remove('tracking/fixtures/position.json')

