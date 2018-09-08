from xml.dom import minidom
from xlrd import open_workbook
import codecs

# 打开excel
workbook = open_workbook('strings.xls')

# 新建xml
doc = minidom.Document()
doc.encoding='utf-8'
# 添加字符串
for sheet in workbook.sheets():
    for col in range(1,sheet.ncols):
        # 添加plist节点
        plistNode = doc.createElement('plist')
        plistNode.setAttribute('version','1.0')
        doc.appendChild(plistNode)
        # 添加dict节点
        dictNode=doc.createElement('dict')
        plistNode.appendChild(dictNode)
        for row_index in range(1,sheet.nrows):
            result_placeholder = sheet.cell(row_index, 0).value
            result_content = sheet.cell(row_index, col).value
            element_key = doc.createElement('key')
            element_key.appendChild(doc.createTextNode(result_placeholder))
            dictNode.appendChild(element_key)
            element_content = doc.createElement('string')
            element_content.appendChild(doc.createTextNode(result_content))
            dictNode.appendChild(element_content)
        result_content = sheet.cell(0, col).value
        f = codecs.open(result_content+'_new_strings.plist', 'w', encoding='utf-8')
        f.write(doc.toprettyxml(indent='    '))
        doc.removeChild(plistNode)

