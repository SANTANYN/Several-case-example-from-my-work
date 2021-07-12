import time
import pytest
from selenium import webdriver
import os
import test_data
rand = test_data.rand
ip = test_data.ip
import datetime
time2 = datetime.datetime.now()
timedef = time2.strftime('%Y-%m-%d %H:%M:%S')
# Тут будет тест проверяющий загрузку отчетов

class TestDownloadHistory:

    # Проверка загрузки отчета в call history xlsx+csv
    def test_download_call_history_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/History']").click()
        driver.find_element_by_css_selector("a[href='/History/Calls']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='application']//main/div/div[1]/div[2]//button[1]").click()
        time.sleep(3)
        chek_text = driver.find_element_by_xpath("//*[@id='application']/div/main/div/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='application']//main/div/div[1]/div[2]//button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//*[@id='application']/div/main/div/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

    def test_download_massaging_history_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/History']").click()
        driver.find_element_by_css_selector("a[href='/History/Messages']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='application']//main/div/div[1]/div[1]/div[2]//button[1]").click()
        time.sleep(3)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/div/div[1]/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='application']//main/div/div[1]/div[1]/div[2]//button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/div/div[1]/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

class TestCampaignReport:

    # Загружаем стату по кампании.
    def test_download_campaign_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/Outbound/']").click()
        driver.find_element_by_css_selector("a[href='/Outbound/Campaigns']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//div[2]/div[1]/div[2]/ul/div/li[1]/div[2]/div[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//div[1]/div[2]/div[2]/div/div/div/button[1]").click()
        time.sleep(3)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main//div[1]/div[2]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//div[1]/div//div[1]/div[2]/div[2]/div/div/div/button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main//div[1]/div[2]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

class TestDownloadReport():
    # Стата по call report. Агенты
    def test_download_operator_call_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports']").click()
        time.sleep(1)
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(3)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

    # Загрузка call report по очередям
    def test_download_queue_call_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports/Queues']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

    # Загрузка репортов по соообщениям. Чаты операторов
    def test_download_agent_massaging_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[1]/div/div[2]/aside[2]/div[2]/ul/div[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

    def test_download_queue_massaging_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[1]/div/div[2]/aside[2]/div[2]/ul/div[2]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports/QueueMessaging']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."

    def test_download_channel_massaging_report(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        test_data.test_auth(driver)
        time.sleep(1)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[1]/div/div[2]/aside[2]/div[2]/ul/div[2]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a[href='/ccc/AgentReports/ChannelMessaging']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[1]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        time.sleep(2)
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("//div[1]/div//section/div[1]/div[2]/div/div/div/button[2]").click()
        time.sleep(5)
        chek_text = driver.find_element_by_xpath("//div[1]/div/main/section/div[1]/div[2]/div/div").text
        assert chek_text == "Загрузка файла начнется автоматически. Если этого не произошло, нажмите здесь."
