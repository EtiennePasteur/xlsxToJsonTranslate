#!/usr/bin/env python3

import sys, getopt
import xlrd
from collections import OrderedDict
from unflatten import unflatten
from deepmerge import always_merger
import simplejson as json

def createJSON(inputfile, outputfile, lang, keyColumn):
    wb = xlrd.open_workbook(inputfile)
    sh = wb.sheet_by_index(0)
    translation = {}

    translationColumn = sh.row_values(0).index(lang)

    for rownum in range(1, sh.nrows):
        data = OrderedDict()
        row_values = sh.row_values(rownum)
        data['translate_key'] = row_values[keyColumn]
        data['translation'] = row_values[translationColumn]
        
        t = unflatten({data['translate_key']: data['translation']})
        translation = always_merger.merge(translation, t)

    j = json.dumps(translation)

    with open(outputfile, 'w') as f:
        f.write(j)
    print('\nSuccess, output written in ->', outputfile)


def main(argv):
    inputfile = 'translate-file.xlsx'
    outputfile = 'fr.json'
    lang = 'fr'
    keyColumn = 1
    try:
        opts, args = getopt.getopt(argv,"hi:o:l:k",["ifile=","ofile=","lang=","keycolumn="])
    except getopt.GetoptError:
        print('xlsxToJsonTranslate -i <inputfile> -o <outputfile> -l <lang> -k <keycolumn>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('xlsxToJsonTranslate -i <inputfile> -o <outputfile> -l <lang> -k <keycolumn>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-l", "--lang"):
            lang = arg
        elif opt in ("-k", "--keycolumn"):
            keyColumn = arg
    print('Input file is :', inputfile)
    print('Output file is :', outputfile)
    print('Lang is :', lang)
    print('KeyColumn is :', keyColumn)
    createJSON(inputfile, outputfile, lang, keyColumn)

if __name__ == "__main__":
    main(sys.argv[1:])
