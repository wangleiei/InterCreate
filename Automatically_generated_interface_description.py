#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

path = '''C:/Users/Administrator/Desktop/I2Cslave'''


# dirs = os.listdir( path )
# # file,filetype = os.path.splitext(path)
# # print(filetype)
# # 输出所有文件和文件夹
# for file in dirs:

# 	# file,filetype = os.path.splitext(path+'\\'+file)
# 	# print(filetype)

# 	with open(path+'\\'+file, "r") as f:
# 		f.readlines()
# 		# f.write('\n\n')
# 		# print("adll new line ",file)
def getStraft(splittext,rawtex):
	end_index = rawtex.find(splittext)
	if end_index != -1:
		return rawtex[end_index+len(splittext):len(rawtex)-1]
	return ''

# 将# 函数名，说明，参数，返回值 写入pdf
def WritePDF(pdfpath,funcname,description,parma,returnval):

	pass
def ReadCfile(Cpath):
	with open(Cpath, "r",encoding="utf8") as f:
		filelist = f.readlines()
		reslist = []
		for x in range(len(filelist)):
			if filelist[x].startswith('*'):
				try:
					temp = list()
					funcname = getStraft("函 数 名:",filelist[x])
					temp.append(funcname)
					description = getStraft("功能说明:",filelist[x+1])
					temp.append(description)
					parma = getStraft("传    参:",filelist[x+2])
					temp.append(parma)
					returnval = getStraft("返 回 值:",filelist[x+3])
					temp.append(returnval)
					
					temp.append(getStraft("说    明:",filelist[x+4])	)
					# print(funcname,description,parma,returnval)
					reslist.append(temp)
					pass
				except Exception as e:
					raise e
			pass
	return reslist
# print(getStraft("函 数 名:","*	函 数 名: 6548sdaf3sad8f1\n"))
print( ReadCfile('''C:/Users/Administrator/Desktop/I2Cslave/I2C_SLAVE.c'''))
