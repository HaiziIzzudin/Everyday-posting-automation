from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
  capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Android",
    "language": "en",
    "locale": "US"
  }


  with open('text.txt', 'r', encoding='utf-8') as file:
    fulltext = file.read()

  appium_server_url = 'http://localhost:4723'

  options = UiAutomator2Options().load_capabilities(capabilities)
  driver = webdriver.Remote(appium_server_url, options=options)


  #################
  ### Instagram ###
  #################

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Instagram").click()

  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create"))
  )
  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create").click()

  sleep(0.5)

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "STORY").click()

  sleep(0.5)

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Gallery").click()

  sleep(2)

  driver.find_element(AppiumBy.XPATH, '//android.widget.GridView[@resource-id="com.instagram.android:id/gallery_recycler_view"]/android.view.ViewGroup[1]').click()

  sleep(1)

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add text").click()

  driver.find_element(AppiumBy.ID, "com.instagram.android:id/text_overlay_edit_text").send_keys(fulltext) # input the text

  driver.swipe(32, 480, 32, 751, 200) # smallen text

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text alignment center").click()

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text color").click()

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Black color").click()

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Done").click()

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Your story").click() # click to post to your story
  sleep(5)

  driver.press_keycode(3)  # Keycode for HOME button

  sleep(1)



  ################
  ### Telegram ###
  ################

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Telegram").click()

  GROUPS = [
    "NR Kampus Puncak Alam",
    "NR Kampus Puncak Perdana",
    "NR Puncak Alam ZON 1",
    "NR Puncak Alam ZON 2",
    "NR Puncak Alam ZON 3",
    "NR Puncak Alam ZON 4",
    "NR Puncak Alam ZON 5",
    "NR Puncak Alam ZON 6",
    "NR Puncak Perdana ZON 7",
  ]

  for groupName in GROUPS:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search"))
    )
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search").click()
    sleep(0.5)


    # clear recent searches
    if len(driver.find_elements(AppiumBy.XPATH, f'//android.widget.TextView[@text="Clear All"]')) > 0:
      driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="Clear All"]').click()
      driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="Clear All"]').click() # confirm clear all
    

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Search"]').send_keys(f"{groupName}")
    driver.find_element(AppiumBy.XPATH, f'//android.view.ViewGroup[contains(@text, "{groupName}")]').click()
    sleep(0.5)

    try: # if input field is Message
      driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Message"]').click()
      driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Message"]').send_keys(fulltext)
    except: # if input field is Send anonymously
      driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Send anonymously"]').click()
      driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Send anonymously"]').send_keys(fulltext)

    sleep(0.5)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send").click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Go back").click()

  driver.press_keycode(3)  # Keycode for HOME button
  sleep(1)




  ################
  ### Whatsapp ###
  ################

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WhatsApp").click()

  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search"))
  )
  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search").click()
  sleep(0.5)

  driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.whatsapp:id/search_input"]').send_keys(f"INFO RASMI JPNR")
  driver.find_element(AppiumBy.XPATH, f'(//android.widget.RelativeLayout[@resource-id="com.whatsapp:id/contact_row_container"])[4]').click()
  sleep(0.5)

  driver.find_element(AppiumBy.ID, f'com.whatsapp:id/entry').click()
  sleep(0.5)

  driver.find_element(AppiumBy.ID, f'com.whatsapp:id/entry').send_keys(fulltext)
  sleep(0.5)

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send").click()
  sleep(10)

  driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up").click()

  driver.press_keycode(3)  # Keycode for HOME button
  sleep(1)




  ###############
  ### Closing ###
  ###############


  driver.press_keycode(187)  # Keycode for RECENTS button
  driver.swipe(100, 500, 1500, 500, 200) # reveals clear all button
  driver.find_element(AppiumBy.ID, "com.google.android.apps.nexuslauncher:id/clear_all").click()


  driver.quit()