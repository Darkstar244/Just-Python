#encoding: utf-8
import os
import pygame

chinese_dir = 'E:\Matvideo\chinese'
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)

pygame.init()
start,end = (0x4E00, 0x9FA5) # 汉字编码范围
for codepoint in range(int(start), int(end)):
    word = chr(codepoint)
    font = pygame.font.Font("E:\Matvideo\SourceHanSansCN-Heavy.otf", 64)
    # 当前目录下要有思源黑体的字体文件SourceHanSansCN-Heavy.otf,或者去c:\Windows\Fonts目录下找，没有的自行百度下载
    # 64是生成汉字的字体大小
    rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, os.path.join(chinese_dir, word + ".png"))

