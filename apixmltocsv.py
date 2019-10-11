import csv
from xml.etree import ElementTree
tree = ElementTree.parse('E:\\aaa imp dox\\csvtoxml.xml')
root = tree.getroot()
count = 0
with open('E:\\aaa imp dox\\test.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    for att in root:
        first = att.find('attval').text
        
        for subatt in att.find('children'):
                second = subatt.find('attval').text
                print('{},{},{}'.format(count, first, second))
                writer.writerow([count, first, second])
                count = count+1
