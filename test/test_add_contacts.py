# -*- coding: utf-8 -*-
from model.company_details import *



def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.open_the_contact_creation_page()
    app.contact.add_full_name(CompanyDetails(firstname='Nikita', middlename='Olegovich', lastname='Pavlov', nickname='NIKPAVLOV'))
    app.contact.add_photo(CompanyDetails(image_path=r'C:\Users\admin\Pictures\Screenshots\Снимок экрана (2).png'))
    app.contact.add_company(CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
    app.contact.add_phone_number(CompanyDetails(mobile_num='786512', work_num='222', fax_num='125423'))
    app.contact.add_email(CompanyDetails(email_1='easdq@mail.ru', email_2='testtest@yandex.ru', email_3='asdasdqwe@google.com'))
    app.contact.add_homepage(CompanyDetails(homepage='vk.com'))
    app.contact.add_date_birth(CompanyDetails(day='12', month='July', year='1990'))
    app.contact.add_date_anniversary(CompanyDetails(a_day='23', a_month='April', a_year='2004'))
    app.contact.select_a_group()
    app.contact.adding_secondary_data(CompanyDetails(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub'))
    app.session.logout()

def test_add_contact2(app):
    # app.session.login(username='admin', password='secret')
    app.contact.open_the_contact_creation_page()
    app.contact.add_full_name(CompanyDetails(firstname='Ivan', middlename='Nikitovich', lastname='Melnikov', nickname='Yragan'))
    app.contact.add_photo(CompanyDetails(image_path=r'C:\Users\admin\Pictures\Screenshots\Снимок экрана (2).png'))
    app.contact.add_company(CompanyDetails(header='TEST1', comName='New_comany1', comAddress='yl.pysh2', comHome='www.compan12312y.com'))
    app.contact.add_phone_number(CompanyDetails(mobile_num='7812312', work_num='22112', fax_num='1254124423'))
    app.contact.add_email(CompanyDetails(email_1='e234234asdq@mail.ru', email_2='test123123test@yandex.ru', email_3='asda34234sdqwe@google.com'))
    app.contact.add_homepage(CompanyDetails(homepage='v11312k.com'))
    app.contact.add_date_birth(CompanyDetails(day='13', month='July', year='1994'))
    app.contact.add_date_anniversary(CompanyDetails(a_day='25', a_month='April', a_year='2005'))
    app.contact.select_a_group()
    app.contact.adding_secondary_data(CompanyDetails(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub'))
    app.session.logout()

