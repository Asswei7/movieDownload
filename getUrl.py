import subprocess

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from tqdm import tqdm


# 获取cdn网址的过程
def getMovieUrl(_wholeUrl):
    chrome_options = Options()  # 以后就可以设置无界面
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    chromedriverPath = "F:\\Git\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriverPath)
    driver.get(_wholeUrl)
    iframe = driver.find_elements_by_tag_name('iframe')[0].get_attribute('src')

    movieUrl = iframe.split("=")[1]
    print(movieUrl)
    return movieUrl


def downloadMovie(_wholeUrl, filename):
    _movieUrl = getMovieUrl(_wholeUrl)
    dirName = "D:\\Download\\"
    filePath = dirName + filename + ".mp4"
    cmd = "ffmpeg -i {} -c copy {}".format(_movieUrl, filePath)
    print(cmd)

    process = subprocess.Popen(
        cmd,  # cmd特定的查询空间的命令
        stdin=None,  # 标准输入 键盘
        stdout=subprocess.PIPE,  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
        stderr=subprocess.PIPE,  # 标准错误，保存到管道
        shell=True)

    outInfo, errInfo = process.communicate()  # 获取输出和错误信息


# cmd命令
# ffmpeg -i https://cdn20.vip-yzzyonline.com/20231006/238_3bd7457a/index.m3u8 -c copy bbbbb.mp4
# movieUrl = "https://cdn16.vip-vip-yzzy.com/20231208/27653_68306657/index.m3u8"
wholeUrl = "https://www.dyttcn.com/dongzuopian/44558.html"
downloadMovie(wholeUrl, "movieName")
