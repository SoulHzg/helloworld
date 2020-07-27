import sys
import numpy
import cv2
import os
import imageio
import time

charList = "@$&%#?abcdefghijklmnopqrstuvwxyz987654321!|:{}()<>/\*^+=~-_      "
comments = []


# 根据灰度值取特定的字符
def getStr(grayValue):
    return charList[int(grayValue * (len(charList) - 1) / 255)]


# 把原始图像矩阵转成字符矩阵
def arrayToStr(array):
    str = ""
    [rows, cols] = array.shape
    index = 0
    for rowItem in array:
        index += 1
        if index < 20 or index > (rows - 30):  # 忽略到边缘的部分
            continue
        for columnItem in rowItem:
            str += columnItem + ' '
        str += '\n'
    return str


# 读取原始图片，返回转换后的字符矩阵列表，scalingRatio指定缩放比例
def createCommentList(img_path, scalingRatio=1):
    originalImgs = imageio.mimread(img_path)
    length = len(originalImgs)
    for i, img in enumerate(originalImgs):
        print('{}%'.format(int((i + 1) * 100 / length)))
        img = numpy.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, dsize=(0, 0), fx=scalingRatio, fy=scalingRatio)
        [rows, cols] = img.shape
        comment = numpy.zeros((rows, cols), dtype=numpy.str)
        for i in range(rows - 1):
            for j in range(cols - 1):
                comment[i][j] = getStr(img[i][j])
        comments.append(arrayToStr(comment))


# 显示转换好的字符矩阵列表，loopTime指定循环显示次数
def showComments(loopTime=1):
    stop = False
    index = 0
    while stop is False:
        index += 1
        for comment in comments:
            os.system('cls')
            print(comment)
            time.sleep(1 / 20)
            if index > loopTime:
                stop = True
                break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Wrong input')
    elif len(sys.argv) == 2:
        img_path = sys.argv[1]
        createCommentList(img_path)
        showComments()
    elif len(sys.argv) == 3:
        img_path = sys.argv[1]
        scalingRatio = float(sys.argv[2])
        createCommentList(img_path, scalingRatio)
        showComments()
    elif len(sys.argv) == 4:
        img_path = sys.argv[1]
        scalingRatio = float(sys.argv[2])
        loopTimes = int(sys.argv[3])
        createCommentList(img_path, scalingRatio)
        showComments(loopTimes)
