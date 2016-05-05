# -*- coding:utf-8 -*-
# xml模块

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(' ', child.tag, child.attrib)
    for i in child:
        print('   ',i.tag,i.attrib)
        for x in i:
            print('     ',x.tag, x.attrib,x.text)

for node in root.iter('field'):
    print(node.tag,node.attrib ,node.text)


new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式