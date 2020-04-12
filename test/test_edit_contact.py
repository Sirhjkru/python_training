from model.company_details import *


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact()
    app.contact.add_company(CompanyDetails(header='TEST21', comName='Comany', comAddress='yl.Yarl', comHome='www.dfgdfgd.com'))
    app.contact.add_phone_number(CompanyDetails(mobile_num='48954', work_num='2212', fax_num='86448652'))
    app.contact.add_email(CompanyDetails(email_1='eas123123q@mail.ru', email_2='testtest13133@yandex.ru', email_3='asdasdqwe13213@google.com'))
    app.contact.save_contact_update()
    app.session.logout()