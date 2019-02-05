from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import re
import time


def get_qq(element):
    """
    :param element: relevant element
    :return: I'd like to get child elements of the element which I pass in.
            And the function will return QQ number hidden in each child element's attribute.
    """
    return re.search('\d+', element.get_attribute('href')).group()


def mail(to):
    """
    :param to: The parameter 'to' is each one's qq mail's address.
    :return: The function has no return. Sending email is its work.
    """
    msg = MIMEMultipart("related")
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = "Happy New Year!"
    msgAlternative = MIMEMultipart("alternative")
    mail_content = """
    <p>HappyNewYear!</p>
    <br/>
    <img src='cid:image1'></img>
    """
    msgAlternative.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msg.attach(msgAlternative)
    with open(r'C:\Users\24312\Desktop\NewYear.jpg', 'rb') as file:
        img = MIMEImage(file.read())
    img.add_header('Content-ID', '<image1>')
    msg.attach(img)
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, t_password)
    server.sendmail(sender, [to, ], msg.as_string())
    server.quit()


# If today is the 5th day, execute the script.
# Notice the 5th day is the 2019 Lunar New Year's first day.
# You can change it whenever you want.
while time.localtime().tm_mday == 5:
    # Initialize
    browser = webdriver.Firefox()
    browser.get('https://user.qzone.qq.com')
    # Of couse I won't tell you what my qq number and my password are.
    # You can change them into your own qq number and password if necessary.
    username = "1234567"
    password = "666666666"

    # Login
    browser.switch_to.frame('login_frame')
    log = browser.find_element_by_id("switcher_plogin")
    log.click()
    time.sleep(0.5)
    uname = browser.find_element_by_id('u')
    uname.send_keys(username)
    ps = browser.find_element_by_id('p')
    ps.send_keys(password)
    btn = browser.find_element_by_id('login_button')
    time.sleep(0.5)
    btn.click()
    time.sleep(0.5)

    # Get the so-called like list
    qq_list = []
    browser.get("https://user.qzone.qq.com/1234567/main")
    browser.switch_to.frame('QM_Feeds_Iframe')
    # Get first list
    li = browser.find_element_by_class_name('user-list')
    user_list = li.find_elements_by_tag_name('a')
    for user in user_list:
        qq_list.append(get_qq(user))

    # Send mail to everyone
    sender = '1234567@qq.com'
    # It was the third party password
    t_password = '66666666'
    for qq in qq_list:
        mail(qq + '@qq.com')
    # All done!
    print("All done!")
    break
    
