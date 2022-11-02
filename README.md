# panda_learn
![输入图片说明](assets/panda2.png)
#### 介绍
学习强国软件-------每天学习积分：45分

#### 软件架构
使用python selenium chrome


#### 安装教程

1.  下载chrome和chromedriver;注意版本对应关系;参考链接
https://chromedriver.chromium.org/downloads
2.  安装python 3.7.1版本（本地环境使用anaconda 4.5.12）和selenium3.8.1（使用pip install selenium==3.8.1)
3.  将qiangguo_chrome.py和id.txt安放在同一文件夹
4.  修改qiangguo_chrome.py中webdriver.Chrome参数executable_path="xxx"
5.  在命令窗口进入目录，输入python qiangguo_chrome.py
6.  在同目录下生成photo.png，打开这个图形，通过学习强国手机端扫码登录（每次运行都将更新photo.png图片)

#### 使用说明

1.  使用chrome无头模式
2.  自动阅读文章和观看视频
3.  js自动实现每日答题、每周答题、专项答题；答题时结果可能有误；所以可能总分少于45分
4.  id.txt分别记录专项答题的id与第周答题的id
5.  如何使用chrome有头模式，不能将chrome最小化，否则阅读文章，无法积分。



#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


