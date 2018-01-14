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
    base_directory = os.path.dirname(__file__)
    try:
        script = os.path.join(base_directory, 'setup.sh')
        subprocess.run(['sh', script, project_name, destination])
    except BaseException as e:
        print('Something broke:\n {}'.format(e))
        subprocess.run(['rm', '-rf', os.path.join(os.getcwd(), destination)])
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