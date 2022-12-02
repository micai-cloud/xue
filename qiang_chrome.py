# _*_ coding: utf-8 _*_

from selenium import webdriver
import time
import datetime
import json
import random
import sys
# import configparser
from urllib.request import Request, urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
# from 中转.inform import send_email
from sendemil import send


# path_profile = "C:/Users/admin/AppData/Roaming/Mozilla/Firefox/Profiles/899nu40m.default-esr"

# 全局url
HOME_PAGE = 'https://www.xuexi.cn/'  # 学习强国官方url
LOGIN_LINK = 'https://pc.xuexi.cn/points/login.html'  # 登录url
SCORES_LINK = 'https://pc.xuexi.cn/points/my-points.html'  # 分数url
zhuan_link = 'https://pc.xuexi.cn/points/exam-paper-detail.html?id='
week_link = 'https://pc.xuexi.cn/points/exam-weekly-detail.html?id='

test_Link = 'https://www.xuexi.cn/lgpage/detail/index.html?id=9145579201389915752&item_id=9145579201389915752'
# zhuan_answer_link =
day_answer_link = 'https://pc.xuexi.cn/points/exam-practice.html'
# 浏览器驱动
# profile = webdriver.FirefoxProfile(path_profile)

# 控制台打印
# print("开始执行你的测试用例！")


# 第二个输入这个：隐藏式启动谷歌浏览器执行UI测试用例
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r'./chrome.exe'
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--mute-audio")  # 静音
chrome_options.add_argument('log-level=3')


chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

# old_time=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
# zhuan_id = "71"
# week_id  = "68"
browser.implicitly_wait(60)
js = """(function() {

    function doit()
    {
        var nextAll=document.querySelectorAll(".ant-btn");

        var next=nextAll[0];

        if(nextAll.length==2)
        {
            next=nextAll[1];
        }
        if(next.disabled)
        {
            document.querySelector(".tips").click();            
            var allTips=document.querySelectorAll("font[color=red]");         
            var buttons=document.querySelectorAll(".q-answer");           
            var textboxs=document.querySelectorAll("input");          
            var qType= document.querySelector(".q-header").textContent;
            qType=qType.substr(0,3);
            switch(qType)
            {
                case"填空题":                   
                    var mevent=new Event('input',{bubbles:true});
                    if( textboxs.length>1)
                    {                       
                        if(allTips.length==textboxs.length)
                        {
                            for(let i=0;i< allTips.length;i++)
                            {
                                let tip=allTips[i];
                                let tipText=tip.textContent;
                                if(tipText.length>0)
                                {                                    
                                    textboxs[i].setAttribute("value",tipText);
                                    textboxs[i] .dispatchEvent(mevent);                                 
                                }
                            }
                        }
                        else
                        {                            
                            if(allTips.length>textboxs.length)
                            {
                                var lineFeed=document.querySelector('.line-feed').textContent;
                                let n=0;
                                for(let j=0;j<textboxs.length;j++)//多个填空
                                {
                                    let tipText=allTips[n].textContent;
                                    let nextTipText="";
                                    do{
                                     tipText+=nextTipText;
                                        if(n<textboxs.length-1)
                                        {
                                            n++;
                                            nextTipText=allTips[n].textContent;
                                        }
                                        else
                                        {
                                            nextTipText="结束了，没有了。";
                                        }
                                    }
                                    while(lineFeed.indexOf(tipText+nextTipText));

                                    textboxs[j].setAttribute("value",tipText);
                                    textboxs[j] .dispatchEvent(mevent);
                                }
                            }

                        }
                    }
                    else if(textboxs.length==1)
                    {
                        let tipText="";
                        for(let i=0;i< allTips.length;i++)
                        {
                            tipText += allTips[i].textContent;
                        }
                        textboxs[0].setAttribute("value",tipText);
                        textboxs[0] .dispatchEvent(mevent);

                    }
                    let flag = 1//
                    for(let i=0;i< textboxs.length;i++) {
                    flag = flag&&textboxs[i].value ==""//
                    }
                    if (flag ==1)
                    {
                    for(let i=0;i< textboxs.length;i++)
                    {
                    textboxs[i].setAttribute("value","aaa");//
                    textboxs[i] .dispatchEvent(mevent); }//

                    }

                    break;
                case "多选题":
                    let clickNum = 0
                    for(let js=0;js<buttons.length;js++)
                    {
                        let cButton=buttons[js];
                        for(let i=0;i< allTips.length;i++)
                        {
                            let tip=allTips[i];
                            let tipText=tip.textContent;
                            if(tipText.length>0)
                            {
                                let cButtonText=cButton.textContent;

                                if(cButtonText.indexOf(tipText)>-1||tipText.indexOf(cButtonText)>-1)
                                {
                                    cButton.click();
                                    clickNum++;
                                    break;
                                }

                            }
                        }

                    }
                    if(clickNum  == 0)//
                        {

                       for(let js=0;js<buttons.length;js++)//
                       {
                       let cButton=buttons[js];//
                       cButton.click();//
                       }
                    }
                    break;

                case "单选题":
                    if(true)
                    {                      
                        let tipText="";
                        for(let i=0;i< allTips.length;i++)
                        {
                            tipText += allTips[i].textContent;
                        }

                        if(tipText.length>0)
                        {

                            for(let js=0;js<buttons.length;js++)
                            {
                                let cButton=buttons[js];
                                let cButtonText=cButton.textContent;                               
                                if(cButtonText.indexOf(tipText)>-1||tipText.indexOf(cButtonText)>-1)
                                {
                                    cButton.click();
                                    break;
                                }
                                else
                                {
                                buttons[0].click();//
                                }
                            }
                        }
                    }

                    break;
                default:
                    break;
            }
            document.querySelector(".tips").click();
        }
        else
        {
            if(next.textContent!="再练一次"&&next.textContent!="再来一组"&&next.textContent!="查看解析"){
                next.click();
            }
        }

    };

    window.setInterval(doit, 3000);
})();"""


def time_now():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime('%Y-%m-%d %H:%M')
    return time_str


def login_simulation():
    """模拟登录"""
    # 方式一：使用cookies方式
    # 先自己登录，然后复制token值覆盖
    # cookies = {'name': 'token', 'value': ''}
    # browser.add_cookie(cookies)

    # 方式二：自己扫码登录
    browser.get(LOGIN_LINK)
    browser.execute_script("var q=document.documentElement.scrollTop=1200")

    time.sleep(5)
    browser.get(HOME_PAGE)
    print("login ok\n")





def day_answer():
    global js
    print("day_answer\n")
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined}'''
    })



    browser.get(day_answer_link)
    browser.execute_script(js)
    sour = browser.find_element(By.CSS_SELECTOR,'#nc_1_n1z')
    # 获取滑条
    time.sleep(0.2)
    ele = browser.find_element(By.CSS_SELECTOR,"#nc_1__scale_text > span")
    # 拖动滑块滑条末尾

    ActionChains(browser).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()

    print(time_now())
    time.sleep(60)


def read_arts():
    """阅读文章"""
    print("readarts\n")
    # 通过分析，找到栏目url，拿到类似channelNames=学习时评这个栏目下的所有文章信息
    url = "https://www.xuexi.cn/lgdata/1ap1igfgdn2.json?_st=26593106"  # 获取文章Api
    firefox_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}  # 包装头部
    request = Request(url, headers=firefox_headers)  # 构建请求
    html = urlopen(request)  # 打开网页
    data = html.read()  # 读取网页内容，是json数据
    hjson = json.loads(data)  # json解析响应文本
    # print('响应解析后的类型：',type(hjson))     # 解析后是dict（字典）类型
    # print('响应解析后的键值对个数：',len(hjson))   # 字典键值对个数
    # 循环读取响应内容中“url”对应的值，设置“循环次数”=7
    length = len(hjson)
    for j in range(0, 7, 1):
        article = hjson[random.randint(1, length - 1)]['url']  # 取url对应的值
        print(j)
        print(article)
        time.sleep(5)
        browser.get(article)
        #  滚动条
        for i in range(0, 2000, 500):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(10)
        for i in range(2000, 0, -500):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(10)
    print("readarts over\n")


def watch_videos():
    """观看视频"""
    print("watch \n")
    url = 'https://www.xuexi.cn/lgdata/1novbsbi47k.json?_st=27497305&js_v=1648112787678'  # 获取视频Api
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    request = Request(url, headers=firefox_headers)
    html = urlopen(request)
    data = html.read()  # 获取数据
    hjson = json.loads(data)  # json解析响应文本
    length = len(hjson)
    for j in range(0, 9, 1):
        video_url = hjson[random.randint(1, length - 1)]['url']  # 取url对应的值
        print(j)
        print(video_url)

        # WebDriverWait(browser,60).until(EC.visibility_of(browser.find_element_by_xpath("//div[@class='outter']"))).click()

        browser.get(video_url)  # 打开浏览器
        time.sleep(5)
        browser.find_element(By.XPATH, "//div[@class='outter']").click()

        for i in range(0, 2000, 500):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(10)
        for i in range(2000, 0, -500):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(10)
    print("watch over\n")


def get_scores():
    """获取当前积分"""
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined}'''
    })
    browser.get(SCORES_LINK)
    time.sleep(2)
    gross_score = browser.find_element(By.XPATH, "//div[@class='my-points-block']/span[1]").get_attribute('innerText')
    today_score = browser.find_element(By.XPATH, "//div[@class='my-points-block']/span[3]").get_attribute('innerText')
    print("total" + str(gross_score))

    print("today" + str(today_score))
    # print("获取积分完毕。\n")
    return str(today_score)

def get_day_score():
    browser.get(SCORES_LINK)
    time.sleep(2)
    titles = browser.find_elements(By.XPATH, "//p[@class='my-points-card-title']")
    scores = browser.find_elements(By.XPATH, "//div[@class='my-points-card-text']")
    zhuan_index = scores[5].get_attribute('innerText').find("分")
    zhuan_score = int(scores[5].get_attribute('innerText')[0:zhuan_index])
    week_score = int(scores[6].get_attribute('innerText')[0:1])
    return zhuan_score, week_score


def start_learn():
    login_simulation()
    print('forward')
    get_scores()  # 获得今日积分
    day_answer()
    zhuan_week_learn()

    read_arts()
    #print(time_now())

    watch_videos()  # 观看视频
    #print(time_now())

    #print(time_now())



def zhuan_week_learn():
    zhuan_score, week_score = get_day_score()
    if zhuan_score == 0 or week_score == 0:
        fo = open('id.txt', 'r+')
        str_ID = fo.read()
        zhuan_id = str_ID.split()[0]
        week_id = str_ID.split()[1]

        while zhuan_score == 0 and int(zhuan_id) < 604:
            browser.get(zhuan_link + zhuan_id)
            print(zhuan_link + zhuan_id)
            time.sleep(5)
            print("zhuan_answer() is doing.zhuan_id=" + zhuan_id)
            browser.execute_script(js)
            print('zhuan ing')
            time.sleep(90)
            zhuan_score, week_score = get_day_score()
            print("zhuan_score:" + str(zhuan_score))
            print(zhuan_score)
            zhuan_id = str(int(zhuan_id) + 1)
            if zhuan_score >= 2:
                break


        position = fo.seek(0, 0)
        fo.write(zhuan_id)
        fo.close()  # 保存zhuan_id

        fo = open('id.txt', 'r+')

        while week_score == 0 and int(week_id) < 274:
            browser.get(week_link + week_id)
            time.sleep(5)
            print("week_answer() is doing.week_id=" + week_id)
            browser.execute_script(js)
            time.sleep(90)
            zhuan_score, week_score = get_day_score()
            print("week_score:" + str(week_score))
            week_id = str(int(week_id) + 1)
            if week_score >= 2:
                break

    print(time_now())


def pho():
    browser.get(LOGIN_LINK)
    browser.execute_script("var q=document.documentElement.scrollTop=1300")
    # a = browser.find_element_by_xpath("//div[@class='login_qrcode_content']")
    # WebDriverWait(browser,60).until(EC.visibility_of(browser.find_element_by_xpath("//span[@class='refresh']")))
    time.sleep(10)
    browser.get_screenshot_as_file("photo.png")
    # print("二维码图片已保存。")
    send('')


def photo_test():
    pho()
    time.sleep(60)
    while len(browser.find_elements(By.CLASS_NAME, 'ddlogintext')) != 0:
        pho()
        time.sleep(60)
    print('login ok')


if __name__ == '__main__':
    photo_test()


    start_learn()

    send('success  ' + get_scores() + 'score  ')

    browser.quit()
# python 3.7.1
