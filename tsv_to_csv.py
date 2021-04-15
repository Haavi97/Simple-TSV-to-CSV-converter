import os

if __name__ == '__main__':
    fn = input('Please, provide the file name: ')
    enc = input('Please, provide file encoding: ')
    cp = os.getcwd() + os.sep
    in_fn = cp + fn
    out_fn = cp + fn.split('.')[0] + '.csv'

    try:
        with open(in_fn, 'r', encoding=enc) as tsv, open(out_fn, 'w+', encoding=enc) as csv:
            str_file = tsv.read()
            csv.write(str_file.replace('\t', ','))
    except FileNotFoundError:
        print('File not found')
    except UnicodeEncodeError:
        print('Wrong encoding')