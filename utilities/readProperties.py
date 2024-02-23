import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get("commonInfo", "url")
        return url

    @staticmethod
    def setCouponcode():
        coupon = config.get("commonInfo", "coupon")
        return coupon

    @staticmethod
    def setMail():
        mail = config.get("commonInfo", "mail")
        return mail

    @staticmethod
    def setPassword():
        password = config.get("commonInfo", "password")
        return password


