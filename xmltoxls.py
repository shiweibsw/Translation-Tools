import xml.dom.minidom
from xlwt import Workbook

# 新建一个workbook
book = Workbook(encoding='utf-8')
sheet = book.add_sheet('Android')

# 打开xml
xmldoc = xml.dom.minidom.parse('strings.xml')
code = xmldoc.getElementsByTagName('string')

sheet.write(0, 0, "键")
sheet.write(0, 1, "中文")
col=2
languages = input("请输入目标语言（空格分割）:")
lan_arr=languages.split()
for lan in lan_arr:
    sheet.write(0, col, lan)
    col = col + 1

row = 1
for node in code:
    for item in node.childNodes:
        sheet.write(row, 0, node.getAttribute('name'))
        sheet.write(row, 1, item.nodeValue)
    row = row + 1
# 保存workbook
book.save('strings.xls')