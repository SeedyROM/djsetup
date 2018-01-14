"""A commandline interface to create simple django boilerplate projects.

Usage:
    djsetup <project_name> [<destination>] [options]

Options:
    -v --verbose    Log all setup information.
"""
import subprocess
import sys
import os

from docopt import docopt

def eval_setup_script(project_name, destination):
    try:
        script = os.path.join(os.path.dirname(__file__), 'setup.sh')
        subprocess.run(['sh', script, project_name, destination])
    except BaseException as e:
        print(e)
        print('Something fucked up.')
        sys.exit(-1)

def create_project(*args):
    eval_setup_script(*args)

def main():
    """Our programs main entry point, using docopt to parse CLI arguments.
    """
    args = docopt(__doc__)
    args['<destination>'] = args.get('<destination>') or '.'

    create_project(args['<project_name>'], args['<destination>'])

if __name__ == '__main__':
    main()