import core.config as config
from core.pyttp import PyTTP

def run():
    PyTTP.createPDF(config.DEFAULT_ENTRYPOINT)

if __name__ == "__main__":
    run()



