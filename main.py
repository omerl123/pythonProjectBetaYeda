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


def logs(T, A ):
    # Receives a string and a double and puts it in a text file
    with open('BetaLogs.txt', 'a') as f:
        f.write("The Login success to email:" + Email + "\n" + "The time it took to " + A + ":" + str(T) + " seconds.\n")

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
        # Takes 5 seconds and checks if the argument it receives exists
    Search_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/login']"))
    )


    # Click on this variable
    Search_element.click()

    # Takes 5 seconds and checks if the argument it receives exists
    UserExist_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "link"))
    )

    # Click on this variable
    UserExist_element.click()

    # Takes 5 seconds and checks if the argument it receives exists
    input_Email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )


    #Send the String To Element
    input_Email_element.send_keys(Email)


    # Takes 5 seconds and checks if the argument it receives exists
    input_Password_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    #Send the String To Element
    input_Password_element.send_keys(Password)

    try:
        # Searches for the element and if it finds it, it records in the file a tex that the user failed to connect
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "mat-error-0"))
        )
        print("The email not contains @ ")
        with open('BetaLogs.txt', 'a') as f:
            f.write("The Login to " + Email + " Fail. \n")
        driver.quit()
        raise SystemExit(1)
    except TimeoutException:
        print("The email contains @")


        # Waits for the login button element to be present for up to 5 seconds
        LogIn_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-btn"))
        )




    # Click on this variable
    LogIn_element.click()

    # start to counting time
    start_time = time.time()

    try:
        # Takes 10 seconds and checks if the argument it receives exists
        Skill_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "skill-image-container"))
        )
        # end to counting time
        end_time = time.time()
        # how much time take to login
        taken_time = end_time - start_time

        # move elements to logs function
        logs(taken_time, "Moving from the login to the home page")

    except TimeoutException:
        # If not successful it means that the user failed to connect
        with open('BetaLogs.txt', 'a') as f:
            f.write("The Login to " + Email + " Fail. \n")

    # end to counting time

    # start to counting time
    start_time = time.time()

    # Click on this variable
    Skill_element.click()

    # end to counting time
    end_time = time.time()


    # how much time take to open skill
    taken_time = end_time-start_time

    logs(taken_time , "open the skill")


    Next_Run = True
    # Run While the Next Button is Clickable
    time.sleep(10)


    while Next_Run:
        try:
            time.sleep(5)
            # Check if you finish skill if you finish its write this to .txt file
            Skill_element = driver.find_element(By.CLASS_NAME, "skill-image-container")
            if Skill_element is not None:
                with open('BetaLogs.txt', 'a') as f:
                    f.write(Email + " complete the skill. \n")
        except NoSuchElementException:
            print(Email + "Couldn't finish the skill")
        try:
            # Checks if the button exists on the page
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "button.mat-raised-button.mat-button-base.app-button.round.medium.ng-star-inserted"))
            )
        except NoSuchElementException:
            print("The Button dont Exsit")
        # If the button is found and clickable, click it
        if next_button.is_enabled():
            time.sleep(4)
            next_button.click()

        else:
            try:
                # Checks if the checkbox is found, if it exists, click it
                CheckBox = driver.find_element(By.CLASS_NAME, "checkbox")
                if CheckBox is not None:
                    time.sleep(4)
                    CheckBox.click()
                    time.sleep(2)
            except NoSuchElementException:
                print("Checkbox not found")

            try:
                # Checks if the input line exists, if it exists, write in the input line
                Input_fill = driver.find_element(By.XPATH , "//input[@formcontrolname='data']")
                if Input_fill is not None:
                    time.sleep(4)
                    Input_fill.send_keys("dsagsg")
                    time.sleep(2)
            except NoSuchElementException:
                print("Input field not found")
            try:
                # Checks if there are several questions and if the array is larger than 1, mark the third element in the array
                buttons = driver.find_elements(By.CSS_SELECTOR,
                                           "app-radio-list[formcontrolname='data'] .learner-choose-one-group .learner-item .learner-task-name span")
                if len(buttons) >= 1:
                    time.sleep(4)
                    buttons[2].click()
                    time.sleep(2)
            except NoSuchElementException:
                print("Buttons not found")






# Take delay
time.sleep(10)


# close the test program
driver.quit()