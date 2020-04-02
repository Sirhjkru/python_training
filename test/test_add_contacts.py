# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.company_details import CompanyDetails

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username='admin', password='secret')
    app.open_the_contact_creation_page()
    app.add_full_name(firstname='Nikita', middlename='Olegovich', lastname='Pavlov', nickname='NIKPAVLOV')
    app.add_photo()
    app.add_company(CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
    app.add_phone_number(mobile_num='786512', work_num='222', fax_num='125423')
    app.add_email(email_one='easdq@mail.ru', email2='testtest@yandex.ru', email3='asdasdqwe@google.com')
    app.add_homepage(homepage='vk.com')
    app.add_date_birth(day='12', month='July', year='1990')
    app.add_date_anniversary(a_day='23', a_month='April', a_year='2004')
    app.select_a_group()
    app.adding_secondary_data(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub')
    app.logout()

def test_add_contact2(app):
    app.open_home_page()
    app.login(username='admin', password='secret')
    app.open_the_contact_creation_page()
    app.add_full_name(firstname='Edward', middlename='Edward', lastname='Pavlov', nickname='Edward')
    app.add_photo()
    app.add_company(CompanyDetails(header='TEST', comName='New_comany', comAddress='yl.pysh', comHome='www.company.com'))
    app.add_phone_number(mobile_num='32131', work_num='111', fax_num='4232521')
    app.add_email(email_one='easdq@mail.ru', email2='testtest@yandex.ru', email3='asdasdqwe@google.com')
    app.add_homepage(homepage='vk.com')
    app.add_date_birth(day='1', month='July', year='1991')
    app.add_date_anniversary(a_day='14', a_month='April', a_year='2001')
    app.select_a_group()
    app.adding_secondary_data(address='Asdwqead', phone='342324', notes='fghrturturtuy ruub')
    app.logout()

