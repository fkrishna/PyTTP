# PyTTP

CLI application that generate a pdf or html document of any readable tutorials from https://www.tutorialspoint.com

# Stack

- weasyprint
- requests
- beautifulsoup4
- python 3

# Installation

...

# Parameters

| Params          | Description                              | Type                                                |
| --------------- | ---------------------------------------- | --------------------------------------------------- |
| entrypoint      | url of any readable tutorial             | (positional)                                        |
| -d or --dest    | Overwrite the default destination path   | (optional): default is set to the working directory |
| --f or --format | Overwrite the default format of document | (optional): default is pdf                          |
| -v or --version | 'show program\'s version number          | (positional)                                        |

# How To Use

Running this command will generate a pdf document of the data structure tutorial from the host server in the current working directory

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm
```

Running this command will generate a pdf document of the data structure tutorial from the host server in the home directory

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm -d=/home
```

Running this command will generate an html document of the data structure tutorial from the host server in the current working directory

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm --format=html
```

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm -d=/home -f=html
```
