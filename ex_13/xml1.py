import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Osama</name>
    <phone type="intl"> +46 768316075 </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
