from __future__ import print_function
if __name__ == '__main__':
    print("attempting to make an epic account fully automatically")
    print("made by Tyler!#9369 and The true forger#2137")
    import os
    import os.path
    import ctypes
    MB_OK = 0
    MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10
    MB_SYSTEMMODAL = 0x1000
    def MsgBox(text, style, title):
        return ctypes.windll.user32.MessageBoxW(None, text, title, style)
    try:
        import legendary;import undetected_chromedriver
    except:
        os.system('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org undetected_chromedriver');os.system('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org legendary-gl')
    try:
        open('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
    except:
        os.system('powershell -Command "(New-Object Net.WebClient).DownloadFile(\'https://referrals.brave.com/latest/BraveBrowserSetup.exe\', \'install_brave.exe\')"')
        os.system('install_brave.exe')
        os.remove('install_brave.exe')
    import random
    import string
    import sys
    import time
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    options = uc.ChromeOptions()
    if input('type "y" for custom username, ENTER key for random : ') == 'y': username = input('username : ')
    else: username = f"a{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}"
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    firstname = f"A{''.join(random.sample(string.ascii_lowercase + string.digits, 14))}"
    lastname = f"L{''.join(random.sample(string.ascii_lowercase + string.digits, 14))}"
    password = f"A{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}&*"
    email = f"{firstname}.{lastname}@interia.pl"
    def switch(x):
        windows = driver.window_handles
        driver.switch_to.window(windows[x])
    try:
        driver = uc.Chrome(options=options, service_log_path=os.devnull)
    except:
        os.system('ctypes.windll.user32.MessageBoxW(0, "Failed setting chromedriver. Make sure you have internet and have normal google chrome downloaded", 1)');exit()
    wait = WebDriverWait(driver, 3000)
    print("Cooking up an epic account 4u")
    print("1st- creating interia.pl account")
    print("waiting for browser to load give it a sec")
    driver.maximize_window()
    driver.get("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe")
    print("waiting for website to load give it a sec")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'rodo-popup-agree'))).click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[1]/input').send_keys(firstname)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(lastname)
    driver.find_element(By.ID, "birthdayDay").send_keys("04")
    driver.find_element(By.CLASS_NAME, 'icon-arrow-right-full').click()
    driver.find_element(By.CLASS_NAME, 'account-select__options__item').click()
    driver.find_element(By.ID, "birthdayYear").send_keys("2000")
    driver.find_element(By.XPATH, "//*[contains(text(), 'P??e??')]").click()
    time.sleep(.3)
    driver.find_element(By.CLASS_NAME, 'account-select__options__item').click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "rePassword").send_keys(password)
    driver.find_element(By.CLASS_NAME, 'checkbox-container').click()
    time.sleep(.6)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(.3)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(.3)
    print(f"2nd- creating epic games account with username {username}")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.epicgames.com/id/register/date-of-birth?redirect_uri=https%3A%2F%2Fwww.epicgames.com%2Fstore%2Fen-US%2Fp%2Ffortnite")
    print("typeing in birthday")
    wait.until(EC.visibility_of_element_located((By.ID, "month"))).click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Jan')]").click()
    driver.find_element(By.ID, "day").click()
    driver.find_element(By.TAG_NAME, "li").click()
    driver.find_element(By.ID, "year").send_keys("2000")
    driver.find_element(By.ID, "continue").click()
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(firstname)
    print("typeing in other info")
    driver.find_element(By.ID, "lastName").send_keys(lastname)
    driver.find_element(By.ID, "displayName").send_keys(username)
    driver.find_element(By.ID, "email").send_keys(email.lower())
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "tos").click()
    if __name__ == '__main__':
        print(MsgBox("It is Recommended to enable your VPN!", MB_ICONERROR | MB_OK | MB_SYSTEMMODAL, "Enable VPN"))
    print("3rd- user needs to (mabye) complete captcha")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify email')]")))
    print("verifying email address")
    switch(0)
    print("waiting to recieve verification email")
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Epic Games')]"))).click()
    print("getting verification code from email")
    time.sleep(5)
    switch(1)
    print("adding fortnite to your list of games")
    wait.until(EC.visibility_of_element_located([By.XPATH,'/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/div[2]/div[4]/div/aside/div/div/div[4]/div/button'])).click()
    wait.until(EC.visibility_of_element_located((By.ID, "agree"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div[2]/button'))).click()
    print(f"{email}:{password} Username:{username} FirstName:{firstname} LastName:{lastname}\n")
    with open("saved_accounts.txt", "a") as f:
        f.write(f"{email}:{password} Username:{username} FirstName:{firstname} LastName:{lastname}\n")
    print("Saved Account to saved_accounts.txt")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div[1]/span"))).click()
    def launch():
        driver.get("https://www.epicgames.com/id/api/redirect")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[style="word-wrap: break-word; white-space: pre-wrap;"]')))
        sid = driver.page_source[219:-22]
        print("deleting any old accounts if present")
        os.system('rmdir /q /s "C:\\Users\\%username%\\.config\\legendary"')
        os.system(f"legendary auth --sid {sid}")
        time.sleep(1)
        os.system('legendary import --disable-check Fortnite "C:\Program Files\Epic Games\Fortnite"')
        time.sleep(1)
        os.system(f"legendary launch fortnite")

    while True:
        input("press a key to launch fortnite")
        launch()
