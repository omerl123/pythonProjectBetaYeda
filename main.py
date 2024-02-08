from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait




Run_Web = False
Next_Run = False
Email = input(str("Enter Your Email: "))
Password = input("Enter Your Password: ")
if Email is not None and Password is not None:
    Run_Web = True
if Run_Web:
    service = Service(executable_path="chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.service = service

    # use with the recommendation options to run this program on chrome
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://web-stg.betayeda.dev/pokemontcgtutorial/signup/53399de4-67a6-4e2a-b29e-5f85ef61c37a")
    except TimeoutException:
        print("Page load timed out. The website may not be available.")
    try:
        # Takes 5 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/login']"))
        )
        # create variable from element in page
        Search_element = driver.find_element(By.XPATH, "//a[@routerlink='/login']")

        # Take delay to do action on element
        time.sleep(2)

        # Click on this variable
        Search_element.click()

        # Takes 5 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "link"))
        )
        # create variable from element in page
        UserExist_element = driver.find_element(By.CLASS_NAME, "link")

        # Take delay to do action on element
        time.sleep(2)

        # Click on this variable
        UserExist_element.click()

        # Takes 5 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.NAME, "username"))
        )
        # create variable from element in page
        input_Email_element = driver.find_element(By.NAME, "username")

        # Take delay to do action on element
        time.sleep(2)

        #Send the String To Element
        input_Email_element.send_keys(Email)

        # Takes 5 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.NAME, "password"))
        )
        # create variable from element in page
        input_Password_element = driver.find_element(By.NAME, "password")

        # Take delay to do action on element
        time.sleep(2)

        #Send the String To Element
        input_Password_element.send_keys(Password)

        #Check if this Element was displayed
        #if yes-print error indicating the stage at which it stopped
        #else continue to test
        try:
            time.sleep(4)
            if driver.find_element(By.ID , "mat-error-0").is_displayed():
                print("The Email not include @\n"
                      "--Login Phase")
                driver.quit()
                raise SystemExit(1)
        except NoSuchElementException:
            pass


        # Takes 5 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-btn"))
        )
        # create variable from element in page
        LogIn_element = driver.find_element(By.CLASS_NAME, "login-btn")

        # Take delay to do action on element
        time.sleep(2)

        # Click on this variable
        LogIn_element.click()

        #Check if this Element was displayed
        #if yes-print error indicating the stage at which it stopped
        #else continue to test
        try:
            time.sleep(5)
            error_element = driver.find_element(By.ID, "mat-error-2")
            if error_element.is_displayed():
                print("Email Or Password Wrong\n"
                      "--Login Phase")
                driver.quit()
                raise SystemExit(1)
        except NoSuchElementException:
            pass

        # Takes 10 seconds and checks if the argument it receives exists
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "skill-image-container"))
        )
        # create variable from element in page
        Skill_element = driver.find_element(By.CLASS_NAME, "skill-image-container")

        # Take delay to do action on element
        time.sleep(2)

        # Click on this variable
        Skill_element.click()

        Next_Run = True
        # Run While the Next Button is Clickable
        while Next_Run:
            # check if Next Button is Clickable
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            ".mat-focus-indicator.mat-raised-button.mat-button-base.app-button.round.medium.ng-star-inserted:not([disabled])"))
            )
            #Create new element
            Next_Button_Element = driver.find_element(By.CSS_SELECTOR,
                                                      ".mat-focus-indicator.mat-raised-button.mat-button-base.app-button.round.medium.ng-star-inserted:not([disabled])")
            #take delya before click
            time.sleep(4)

            #Click on the Button
            Next_Button_Element.click()

            #Check if Button not Clickable
            if not Next_Button_Element.is_enabled():
                Next_Run = False



    except Exception as e:
        print("An error occurred:", e)
        # close the test program
        driver.quit()
        raise SystemExit(1)

    # Take delay
    time.sleep(10)


    # close the test program
    driver.quit()








