import codecs
import pygame, sys
import os
from scipy.misc import imread
from numpy import * 
chinese_dir = 'E:\Matvideo\chinese_fin'
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)
matrix=[]

start,end = (0x4E00, 0x9FA5) # 汉字编码范围
strH_gray=[]

for codepoint in range(int(start), int(end)):
    word = chr(codepoint)
    path2='E:\Matvideo\chinese'
    path1=os.path.join(path2,word+ ".png")
    strdata= imread(path1,mode = 'RGB')
    strdata1=strdata[:,:,1]
    strdata1=(strdata1!=255)
    nn=len(strdata1[:])
    sm=sum(strdata1[:])
    matrix.append(codepoint)
    strH_gray.append(sm/nn)
     
    
 

def findSmallest(arr):
    smallest = arr[0]#将第一个元素的值作为最小值赋给smallest
   
    
    smallest_index = 0#将第一个值的索引作为最小值的索引赋给smallest_index
    for i in range(1, len(arr)):
        
        if arr[i] < smallest:#对列表arr中的元素进行一一对比
            smallest = arr[i]
            
            smallest_index = i
    return smallest_index
def selectionSort(arr,cop):
    newArr = []
    newcop=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)#一共要调用5次findSmallest
        newArr.append(arr.pop(smallest))#每一次都把findSmallest里面的最小值删除并存放在新的数组newArr中
        newcop.append(cop.pop(smallest))
    return newcop
cop=selectionSort(strH_gray,matrix)
with codecs.open("E:\Matvideo\chinese2.txt", "wb", encoding="utf-8") as f:
 for codepoin in range(0,len(cop)-1):
  f.write(chr(cop[codepoin]))
