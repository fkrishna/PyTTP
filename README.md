# PyTTP

CLI application that generate a pdf or html document of any readable tutorials from https://www.tutorialspoint.com

# Environment

- python v3.6
- Pipenv for managing package dependencies.

# Lib Dependencies

- weasyprint
- requests
- beautifulsoup4

# Parameters

| Args            | Description                                 | Type                                              |
| --------------- | ------------------------------------------- | ------------------------------------------------- |
| entrypoint      | url of any readable tutorial                | positional                                        |
| -d or --dest    | Overwrite the default destination path      | optional: default is set to the working directory |
| --f or --format | Overwrite the default format of thedocument | optional: default is pdf                          |
| -v or --version | show program version number                 | optional                                          |

# How To Use

this command will generate a pdf document of the Data structure tutorial in the current working directory

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm
```

this command will generate an html document of the Data structure tutorial in the current working directory

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm --format=html
```

this command will generate an html document of the Data structure tutorial in the home

```
python3 main.py https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm -d=/home -f=html
```
