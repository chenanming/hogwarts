#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging
from appium_po.utils.read_ini import ReadInit
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.element = ReadInit()