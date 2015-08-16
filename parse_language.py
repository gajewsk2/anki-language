import os
from os import listdir
from os.path import isfile, join
from lxml import etree

from unicode_writer import UnicodeWriter

def get_files(folder):
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    return files

def get_tags(input):
    doc = etree.parse(input)
    tags = doc.findall('*')
    return tags


def sanitize(text):
    if text is not None:
        return text.strip(' \t\n\r')
    return ''
def parse_xml(target, source, output):
    target_tags = get_tags(target)
    source_tags = get_tags(source)

    # with open(output, 'a+') as csv_file:
    with open(output, 'a+') as fout:
        for t, s in zip(target_tags, source_tags):
            if t.get('name') == s.get('name'):
                    t_text = sanitize(t.text)
                    s_text = sanitize(s.text)
                    if t_text != '' and s_text != ''\
                            and t_text != s_text:
                        writer = UnicodeWriter(fout)
                        writer.writerow([t_text, s_text])


def parse_folder(target, source, output):
    target_files = get_files(target)
    for t in target_files:
        parse_xml(target + t, source + t, output)


def remove_file(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


def main():
    output = 'output/2.csv'
    remove_file(output)
    parse_folder('ja/', 'eu/', output)
    

if __name__ == '__main__':
    main()
