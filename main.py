import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
import Write
import Read





Run_Web = False
Next_Run = False
# Check the current stage
count = 0
expect_step = 8

# Reads the file "Details.txt" and takes the URL, e-mail and password from it
url,Email,Password=Read.ReadDetails()

if Email is not None and Password is not None:
    Run_Web = True
if Run_Web:
    start_script = time.time()
    service = Service(executable_path="chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.service = service

    # use with the recommendation options to run this program on chrome
    driver = webdriver.Chrome(options=options)



    # Check for 503 error from 22:00 to 07:00
    response = requests.get(url)
    if response.status_code == 503:
        print("Error 503. Please try tomorrow at 07:00 o'clock")
        driver.quit()
        exit()

    driver.get(url)

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
        Write.Fail(Email)
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
        # Increase the step count by 1
        count+=1

        # move elements to logs function
        Write.logs(taken_time, "Moving from the login to the home page",count,Email)

    except TimeoutException:
        # If not successful it means that the user failed to connect
        Write.Fail(Email)

    # end to counting time

    # start to counting time
    start_time = time.time()

    # Click on this variable
    Skill_element.click()

    # end to counting time
    end_time = time.time()


    # how much time take to open skill
    taken_time = end_time-start_time
    # take the name of skill
    skill_element = driver.find_element(By.CSS_SELECTOR, ".skill-name")

    skill_name = skill_element.text

    info = "skill: " + skill_name

    count+=1
    # add the skill name t log
    Write.logs(taken_time, info, count,Email)


    Next_Run = True
    # Run While the Next Button is Clickable
    time.sleep(10)

    while Next_Run:
        try:
            time.sleep(4)
            # Check if you finish skill if you finish its write this to .txt file
            Skill_element = driver.find_element(By.CLASS_NAME, "skill-image-container")
            if Skill_element is not None:
                # Makes a calculation of the running time of the script, some percentages of completion and enters into the log
                finish_script = time.time()
                total_time = finish_script - start_script
                total = count/expect_step
                minuts = total_time//60
                seconds = total_time - (minuts * 60)
                Write.CalcStep(Email, minuts, seconds, total)

                driver.quit()
        except NoSuchElementException:
            print(Email + " Couldn't finish the skill")
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
            time.sleep(1)
            next_button.click()

        else:

            try:
                # Checks if the checkbox is found, if it exists, click it
                CheckBox = driver.find_element(By.CLASS_NAME, "checkbox")
                if CheckBox is not None:
                    # Calculates some percentages and enters the log of the percentage of success so far and also the name of the stage
                    count += 1
                    total = count / expect_step
                    CheckBox.click()
                    Write.logs(total, "Checkbox", count, Email)

            except NoSuchElementException:
                print("Checkbox not found")

            try:
                # Checks if the input line exists, if it exists, write in the input line
                Input_fill = driver.find_element(By.XPATH , "//input[@formcontrolname='data']")
                if Input_fill is not None:
                    # Calculates some percentages and enters the log of the percentage of success so far and also the name of the stage
                    count += 1
                    total = count / expect_step
                    Input_fill.send_keys("dsagsg")
                    Write.logs(total, "open question", count, Email)
            except NoSuchElementException:
                print("Input field not found")
            try:
                # Checks if there are several questions and if the array is larger than 1, mark the third element in the array
                buttons = driver.find_elements(By.CSS_SELECTOR,
                                       "app-radio-list[formcontrolname='data'] .learner-choose-one-group .learner-item .learner-task-name span")
                if len(buttons) >= 1:
                    # Calculates some percentages and enters the log of the percentage of success so far and also the name of the stage
                    count += 1
                    total = count / expect_step
                    buttons[2].click()
                    Write.logs(total, "Choose one", count, Email)
            except NoSuchElementException:
                print("Buttons not found")







# Take delay
time.sleep(10)



# close the test program
driver.quit()