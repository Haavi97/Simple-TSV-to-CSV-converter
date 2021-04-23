import os
from sys import argv

if __name__ == '__main__':
    try:
        if argv[1] == '--guided':
            fn = input('Please, provide the file name: ')
            enc = input('Please, provide file encoding: ')
        else:
            fn = argv[1]
            try:
                enc = argv[2]
                try:
                    sep = argv[3]
                except:
                    sep = ','
            except:
                enc = 'utf-8'
        cp = os.getcwd() + os.sep
        in_fn = cp + fn
        out_fn = cp + fn.split('.')[0] + '.csv'

        try:
            with open(in_fn, 'r', encoding=enc) as tsv, open(out_fn, 'w+', encoding=enc) as csv:
                str_file = tsv.read()
                csv.write(str_file.replace('\t', sep))
            print('Succesfully converted')
        except FileNotFoundError:
            print('File not found')
        except UnicodeEncodeError:
            print('Wrong encoding')
    except:
        print('Some error ocurred. Please, check input parameters')