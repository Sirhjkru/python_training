class CompanyDetails:
    def __init__(self, header, comName, comAddress, comHome):
        self.header = header
        self.comName = comName
        self.comAddress = comAddress
        self.comHome = comHome


class SecondaryData:
    def __init__(self, address, phone, notes):
        self.address = address
        self.phone = phone
        self.notes = notes


class AnniversaryDate:
    def __init__(self, a_day, a_month, a_year):
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year


class BirthDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Homepage:
    def __init__(self, homepage):
        self.homepage = homepage


class Email:
    def __init__(self, email_1, email_2, email_3):
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3

class PhoneNomber:
    def __init__(self, mobile_num, work_num, fax_num):
        self.mobile_num = mobile_num
        self.work_num = work_num
        self.fax_num = fax_num


class Image:
    def __init__(self, image_path):
        self.image_path = image_path


class FullName:
    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname