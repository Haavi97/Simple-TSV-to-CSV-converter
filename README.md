# Simple TSV to CSV converter
> CLI app to convert TSV files to CSV files

## Requirements
Python
## Simple usage

Simplest usage is to run directly with the file name from the CLI:
```bash
python tsv_to_csv.py file_name
```

## Usage adding encoding and separator
If you want to add the encoding you can add an additional encoding (by default is utf-8) and separator (by default is ,) parameters:
```bash
python tsv_to_csv.py file_name encoding separator
```

## Guided usage
If you want a guided step by step just set the ```guided``` parameter:
```bash
python tsv_to_csv.py --guided
```
and you will be prompted something like:
```console
foo@bar:~$ python tsv_to_csv.py --guided
Please, provide the file name: filename.tsv
Please, provide file encoding: utf-8
Succesfully converted
foo@bar:~$ 
```