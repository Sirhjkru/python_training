class ContactHelper:
    def __init__(self, app):
        self.app = app

    def adding_secondary_data(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(company_details.address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(company_details.phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(company_details.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def select_a_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new_group").click()
        self.app.pick(wd.find_element_by_name("new_group")).select_by_visible_text("New_group")
        wd.find_element_by_xpath("(//option[@value='12'])[3]").click()

    def add_date_anniversary(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        self.app.pick(wd.find_element_by_name("aday")).select_by_visible_text(company_details.a_day)
        wd.find_element_by_xpath("(//option[@value='8'])[2]").click()
        wd.find_element_by_name("amonth").click()
        self.app.pick(wd.find_element_by_name("amonth")).select_by_visible_text(company_details.a_month)
        wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(company_details.a_year)

    def add_date_birth(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        self.app.pick(wd.find_element_by_name("bday")).select_by_visible_text(company_details.day)
        wd.find_element_by_xpath("//option[@value='9']").click()
        wd.find_element_by_name("bmonth").click()
        self.app.pick(wd.find_element_by_name("bmonth")).select_by_visible_text(company_details.month)
        wd.find_element_by_xpath("//option[@value='July']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(company_details.year)

    def add_homepage(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(company_details.homepage)

    def add_email(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(company_details.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(company_details.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(company_details.email_3)

    def add_phone_number(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(company_details.mobile_num)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(company_details.work_num)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(company_details.fax_num)

    def add_company(self, company_details):
        wd = self.app.wd
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

    def add_photo(self, company_details):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form/input[7]").send_keys(company_details.image_path)

    def add_full_name(self, company_details):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(company_details.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(company_details.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(company_details.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(company_details.nickname)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def open_the_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()