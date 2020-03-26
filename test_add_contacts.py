# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, os
from company_details import CompanyDetails

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_the_contact_creation_page(wd)
        self.add_full_name(wd, firstname='Nikita', middlename='Olegovich', lastname='Pavlov', nickname='NIKPAVLOV')
        self.add_photo(wd)
        self.add_company(wd, CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
        self.add_phone_number(wd, mobile_num='786512', work_num='222', fax_num='125423')
        self.add_email(wd, email_one='easdq@mail.ru', email2='testtest@yandex.ru', email3='asdasdqwe@google.com')
        self.add_homepage(wd, homepage='vk.com')
        self.add_date_birth(wd, day='12', month='July', year='1990')
        self.add_date_anniversary(wd, a_day='23', a_month='April', a_year='2004')
        self.select_a_group(wd)
        self.adding_secondary_data(wd, address='Asdwqead', phone='342324', notes='fghrturturtuy ruub')
        self.logout(wd)

    def test_add_contact2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_the_contact_creation_page(wd)
        self.add_full_name(wd, firstname='Edward', middlename='Edward', lastname='Pavlov', nickname='Edward')
        self.add_photo(wd)
        self.add_company(wd, CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
        self.add_phone_number(wd, mobile_num='32131', work_num='111', fax_num='4232521')
        self.add_email(wd, email_one='easdq@mail.ru', email2='testtest@yandex.ru', email3='asdasdqwe@google.com')
        self.add_homepage(wd, homepage='vk.com')
        self.add_date_birth(wd, day='1', month='July', year='1991')
        self.add_date_anniversary(wd, a_day='14', a_month='April', a_year='2001')
        self.select_a_group(wd)
        self.adding_secondary_data(wd, address='Asdwqead', phone='342324', notes='fghrturturtuy ruub')
        self.logout(wd)

    def adding_secondary_data(self, wd, address="address", phone="home", notes="notes"):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def select_a_group(self, wd):
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("New_group")
        wd.find_element_by_xpath("(//option[@value='12'])[3]").click()

    def add_date_anniversary(self, wd, a_day="8", a_month="August", a_year="1996"):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(a_day)
        wd.find_element_by_xpath("(//option[@value='8'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(a_month)
        wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(a_year)

    def add_date_birth(self, wd, day="3", month="July", year="1997"):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(day)
        wd.find_element_by_xpath("//option[@value='9']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(month)
        wd.find_element_by_xpath("//option[@value='July']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)

    def add_homepage(self, wd, homepage="vk.ru"):
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)

    def add_email(self, wd, email_one="asdfq@gmail.com", email2="cgetzdbf@yandex.com", email3="cvntxdvrc@mail.com"):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email_one)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)

    def add_phone_number(self, wd, mobile_num="5476981465", work_num="3333", fax_num="4521754"):
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile_num)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_num)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax_num)

    def add_company(self, wd, company_details):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(company_details.header)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company_details.comName)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(company_details.comAddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(company_details.comHome)

    def add_photo(self, wd):
        wd.find_element_by_xpath("/html/body/div/div[4]/form/input[7]").send_keys(image_path)

    def add_full_name(self, wd, firstname="ivan", middlename="ivanovich", lastname="raduk", nickname="irad"):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

    def open_the_contact_creation_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/?group=")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()


image_path = os.path.abspath(r'C:\Users\admin\Pictures\Screenshots\Снимок экрана (2).png')

if __name__ == "__main__":
    unittest.main()
