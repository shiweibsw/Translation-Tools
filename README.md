# Translation-Tools
Android strings.xml 多语言文本翻译导入工具，解决多语种项目翻译逐条导入问题。
## 使用方式
#### 1 XML转XLS 
把待翻译的strings.xml文件放在xml转xls.exe同级目录下
![](https://user-gold-cdn.xitu.io/2018/7/2/1645991812bff5bd?w=579&h=186&f=jpeg&s=12247)
双击执行xml转xls.exe
![](https://user-gold-cdn.xitu.io/2018/7/2/1645992da64a072c?w=837&h=541&f=jpeg&s=33752)
输入你要转换的语种 ，比如 英文 日文 韩文（使用空格分割）回车，会在当前目录下生成一个strings.xls文件
![](https://user-gold-cdn.xitu.io/2018/7/2/164599806e024158?w=743&h=214&f=jpeg&s=16705)
打开格式如下
![](https://user-gold-cdn.xitu.io/2018/7/2/1645998dfd06a7ea?w=510&h=242&f=jpeg&s=22161)
这个文档就可以提供给翻译公司或者我们自己完成对应语种下的翻译了。
#### 2 XLS转XML
现在假如我们已经拿到了翻译好文档，就像这样

![](https://user-gold-cdn.xitu.io/2018/7/2/164599f426c54852?w=590&h=217&f=jpeg&s=33909)
现在我们把这个文档放在xls转xml.exe的同级目录下

__注意:文档名为strings.xls不能修改__

![](https://user-gold-cdn.xitu.io/2018/7/2/164599806e024158?w=743&h=214&f=jpeg&s=16705)
双击执行xls转xml.exe，执行完毕后你会发现目录下成了以下四个文件

![](https://user-gold-cdn.xitu.io/2018/7/2/16459a2bb97f8c23?w=611&h=206&f=jpeg&s=11201)
这些文件就是我们要放置到各个语种文件夹下的xml文件（中文的可以忽略）

任务完成！

#### 3 XLS转PLIST

##### Windows平台
同步骤2

##### Mac平台
strings.xls文件（名称不能改）放在xlstoplist.py同级目录下，打开python运行环境执行xlstoplist.py即可

## 注意事项
不要修改strings.xml及strings.xls文件名

windows平台下py脚本打包exe文件命令
pyinstaller -F -p F:\PythonWorkSpace\Translation-Tools\venv\Lib\site-packages xlstoplist.py
