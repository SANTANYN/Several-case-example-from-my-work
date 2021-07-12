import time
import pytest
import requests
from selenium import webdriver
import os
import test_data
rand = test_data.rand
ip = test_data.ip


'''class with all  integrations unit test'''
class Testvoxintegration():
    '''test for create api token'''

    def test_apitoken(self):
        # auth in system
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        # Create APIkey
        driver.find_element_by_css_selector("a[href='/Integrations']").click()
        driver.find_element_by_css_selector("a[href='/Integrations/ApiTokens']").click()
        driver.find_element_by_css_selector("div > button.sc-btn.is-default.is-primary.is-medium ").click()
        driver.find_element_by_css_selector("div.simple-dialog__input input").send_keys(f"{rand}")
        save = driver.find_element_by_css_selector(" div.sc-modal__footer button.sc-btn.is-default.is-primary.is-big")
        webdriver.ActionChains(driver).move_to_element(save).click(save).perform()
        time.sleep(2)
        apikey1 = driver.find_element_by_xpath("//section/div[2]//div[2]/div[1]/div[1]/div[2]/div[1]").text
        assert float(apikey1) == rand, print("все верно")
        '''Next step is delete created in previous step api key'''
        time.sleep(1)
        delete = driver.find_element_by_css_selector("div.uniq-table__body > div:nth-child(1) div:nth-child(4) button")
        webdriver.ActionChains(driver).move_to_element(delete).click(delete).perform()
        time.sleep(1)
        delete2 = driver.find_element_by_css_selector("div > div.sc-remove-popover__btns > button:nth-child(1)")
        webdriver.ActionChains(driver).move_to_element(delete2).click(delete2).perform()
        time.sleep(1)
        apikey2 = driver.find_element_by_xpath("//main//section//div[2]/div[1]/div[1]/div[2]/div[1]").text
        assert apikey2 != str(rand), print("все верно")


    ''' test for create Global Variables'''
    def test_global_var(self):
        # auth in system
        driver = webdriver.Chrome()
        test_data.test_auth(driver)
        # Next step is create global variables
        driver.find_element_by_css_selector("a[href='/Integrations']").click()
        driver.find_element_by_css_selector("a[href='/Integrations/GlobalVariables']").click()
        gb_ul_lenBefore = driver.find_elements_by_xpath("//main//section/div[2]/div[1]//div/ul/li")
        driver.find_element_by_xpath("//main//section/div[2]/div[2]/div/ul/li[2]").click()
        time.sleep(1)
        gb_ul_lenBefore2 = driver.find_elements_by_xpath("//main//section/div[2]/div[1]//div/ul/li")
        driver.find_element_by_xpath("//main//section/div[2]/div[2]/div/ul/li[1]").click()
        gbb = len(gb_ul_lenBefore2) + len(gb_ul_lenBefore)
        time.sleep(1)
        driver.find_element_by_xpath("//main//section//button").click()
        rand_name1 = f'"string"+{rand}'
        driver.find_element_by_xpath("// form/div[1]//div[1]/input").send_keys(f'{rand_name1}')
        driver.find_element_by_xpath("// form/div[2]//div[1]/input").send_keys(f'{rand_name1}')
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='sc-btn is-default is-primary is-big']").click()
        time.sleep(1)
        gb_ul_lenAfter = driver.find_elements_by_xpath("//main//section/div[2]/div[1]//div/ul/li")
        driver.find_element_by_xpath("//main//section/div[2]/div[2]/div/ul/li[2]").click()
        time.sleep(2)
        gb_ul_lenAfter2 = driver.find_elements_by_xpath("//main//section/div[2]/div[1]//div/ul/li")
        gb = len(gb_ul_lenAfter) + len(gb_ul_lenAfter2)
        assert gbb + 1 == gb, "все верно"
        '''Ждем реализацию сортировки, без нее данный ассерт является серьезным костылём'''

    def test_SIPWhitelist(self):
        driver = webdriver.Chrome()
        test_data.test_auth(driver)
        driver.find_element_by_xpath("//*[@id='application']//div/ul/a[6]").click()
        driver.find_element_by_xpath("//*[@href='/Integrations/SIPWhitelist']").click()
        driver.find_element_by_xpath("//main//section//div[2]/button").click()
        new_ip = ip
        driver.find_element_by_xpath("//form//div[1]/div[1]/input").send_keys(new_ip)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]//div[3]//div/button[1]").click()
        time.sleep(1)
        ip_text = driver.find_element_by_xpath("//main//section//ul/li/div[1]//div[2]/div[1]").text
        assert new_ip == ip_text, "все верно"


    def test_dialogflow(self):
        # auth in system
        driver = webdriver.Chrome()
        test_data.test_auth(driver)
        # Next step is download dialogflow agent
        driver.find_element_by_xpath("//*[@id='application']//div/ul/a[6]").click()
        driver.find_element_by_xpath("//*[@href='/Integrations/Dialogflow']").click()
        name = driver.find_element_by_xpath("//main//div[2]/div[1]//div/ul/li[1]/div[1]/div[1]/div[2]/div[1]").text
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'some_dialogflow_agent')
        driver.find_element_by_xpath("//main//section/div[1]/div[2]/div[2]/input").send_keys(file_path)
        time.sleep(2)
        # delete agent
        driver.find_element_by_xpath("//main//section/div[2]/div[1]//ul/li[1]/div[1]/div[2]/div/div").click()
        driver.find_element_by_xpath("//div[4]/div[1]//ul/li[2]").click()
        driver.find_element_by_xpath("//div[5]/div[1]/div[2]/button[1]").click()
        time.sleep(1)
        name3 = driver.find_element_by_xpath("//main//div[2]/div[1]//div/ul/li[1]/div[1]/div[1]/div[2]/div[1]").text
        assert name == name3

''' Тут важно чтобы небыло дублей агента перед стартом теста'''