from lxml import etree
import csv
from unicode_writer import UnicodeWriter

def get_tags(input):
    doc = etree.parse(input)
    tags = doc.findall('*')
    return tags


def parse_xml(primary, source, output):
    primary_tags = get_tags(primary)
    source_tags = get_tags(source)

    # with open(output, 'a+') as csv_file:
    with open(output, 'wb') as fout:
        for p, s in zip(primary_tags, source_tags):
            if p.get('name') == s.get('name'):

                # reader = UnicodeReader(fin)
                writer = UnicodeWriter(fout)
                writer.writerow([p.text, s.text])
                # w = csv.writer(utf_8_encoder(csv_file))
                # w.writerow([p.text, s.text])


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def main():
    parse_xml("ja/01-core.xml", "eu/01-core.xml", "output/1.csv")

if __name__ == '__main__':
    main()
