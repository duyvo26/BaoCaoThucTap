import os
import subprocess
import sys

def get_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files



args = sys.argv

python_files = get_python_files(str(args[1]))

with open('requirements.txt', 'w') as f:
    for file in python_files:
        result = subprocess.run(['pip', 'freeze', '-r', file], stdout=subprocess.PIPE)
        f.write(result.stdout.decode('utf-8'))
