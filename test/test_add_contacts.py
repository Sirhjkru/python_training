# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.company_details import *

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username='admin', password='secret')
    app.open_the_contact_creation_page()
    app.add_full_name(FullName(firstname='Nikita', middlename='Olegovich', lastname='Pavlov', nickname='NIKPAVLOV'))
    app.add_photo(Image(image_path=r'C:\Users\admin\Pictures\Screenshots\Снимок экрана (2).png'))
    app.add_company(CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
    app.add_phone_number(PhoneNomber(mobile_num='786512', work_num='222', fax_num='125423'))
    app.add_email(Email(email_1='easdq@mail.ru', email_2='testtest@yandex.ru', email_3='asdasdqwe@google.com'))
    app.add_homepage(Homepage(homepage='vk.com'))
    app.add_date_birth(BirthDate(day='12', month='July', year='1990'))
    app.add_date_anniversary(AnniversaryDate(a_day='23', a_month='April', a_year='2004'))
    app.select_a_group()
    app.adding_secondary_data(SecondaryData(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub'))
    app.logout()

def test_add_contact2(app):
    app.login(username='admin', password='secret')
    app.open_the_contact_creation_page()
    app.add_full_name(FullName(firstname='Ivan', middlename='Nikitovich', lastname='Melnikov', nickname='Yragan'))
    app.add_photo(Image(image_path=r'C:\Users\admin\Pictures\Screenshots\Снимок экрана (2).png'))
    app.add_company(CompanyDetails(header='TEST1', comName='New_comany1', comAddress='yl.pysh2', comHome='www.compan12312y.com'))
    app.add_phone_number(PhoneNomber(mobile_num='7812312', work_num='22112', fax_num='1254124423'))
    app.add_email(Email(email_1='e234234asdq@mail.ru', email_2='test123123test@yandex.ru', email_3='asda34234sdqwe@google.com'))
    app.add_homepage(Homepage(homepage='v11312k.com'))
    app.add_date_birth(BirthDate(day='13', month='July', year='1994'))
    app.add_date_anniversary(AnniversaryDate(a_day='25', a_month='April', a_year='2005'))
    app.select_a_group()
    app.adding_secondary_data(SecondaryData(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub'))
    app.logout()

