from core.pyttp import PyTTP

entrypoint = 'https://www.tutorialspoint.com/html/index.htm'

def run():
    PyTTP.createPDF(entrypoint)

if __name__ == "__main__":
    run()



