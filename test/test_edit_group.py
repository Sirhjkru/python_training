from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.group.create(Group(name="New11_group11", header="group111", footer="group111"))
    app.session.logout()
