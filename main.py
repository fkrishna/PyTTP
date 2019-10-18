import argparse
import config as config
from core.pyttp import PyTTP

ENV = 'prod'

dev_config = {
    'entrypoint': config.ENTRYPOINT,
    'dest': config.DEST,
    'ext': config.DEF_FILE_FORMAT, 
    'debug': True
}

prod_config = {
    'entrypoint':'',
    'dest':'',
    'ext':'',
    'debug': False
}

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
        default=config.DEST,
        type=str,
        help='Overwrite default destination source',
    )

    parser.add_argument(
        '-f',
        '--format',
        metavar='format',
        default=config.DEF_FILE_FORMAT,
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
    
    args = cli_init()
    
    if ENV == 'prod':
        prod_config['entrypoint'] = args.entrypoint
        prod_config['dest'] = args.dest
        prod_config['ext'] = args.format
        config = prod_config
    else:
        config = dev_config 
    
    status = PyTTP.execute(**config)
    print(status)
    


