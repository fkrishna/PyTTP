import core.config as config
from core.pyttp import PyTTP

def run():
    PyTTP.createPDF(entrypoint=config.DEFAULT_ENTRYPOINT, kind='html')

if __name__ == "__main__":
    run()



