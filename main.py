import argparse
import config as config
from core.pyttp import PyTTP

ENV = 'dev'

def cli_init():
    parser = argparse.ArgumentParser(
        prog=config.APP_NAME.lower(), 
        description=config.APP_DESCRIPTION, 
        allow_abbrev=False
    )

    parser.add_argument(
        'entrypoint', 
        metavar='entrypoint',
        type=str, 
        help='Entry point tutorial'
    )

    parser.add_argument(
        '-d',
        '--dest',
        metavar='dest',
        default=f'{config.DEF_DEST_SRC}',
        type=str,
        help='Overwrite default destination source',
    )

    parser.add_argument(
        '-e',
        '--exp',
        metavar='export',
        default=f'{config.DOC_EXTS[0]}',
        type=str,
        help='format of the document to be exported',
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='show program\'s version number and exit',
    )

    return parser.parse_args()

if __name__ == "__main__":
    #args = cli_init()

    dev_config = {
        'entrypoint': config.ENTRYPOINT,
        'dest': '/vagrant/lab/PYTTP/',
        'ext':'pdf', 
        'debug': True
    }

    prod_config = {
        'entrypoint': '',
        'dest': '',
        'ext':'pdf',
        'debug': False
    }

    if ENV == 'prod':
        config = prod_config
    else:
        config = dev_config 
    
    PyTTP.execute(**config)
    


    



