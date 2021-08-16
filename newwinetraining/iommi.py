#Overrides for base iommi classes. Allows for inserting project-wide customizations
#In views, urls, etc, use `from project.iommi (newwinetrainig.iommi) import Page, Form, Table` instead of
#from iommi import Page.....

import iommi

class Page(iommi.Page):
    pass


class Action(iommi.Action):
    pass


class Field(iommi.Field):
    pass


class Form(iommi.Form):
    class Meta:
        member_class = Field
        page_class = Page
        action_class = Action


class Filter(iommi.Filter):
    pass


class Query(iommi.Query):
    class Meta:
        member_class = Filter
        form_class = Form


class Column(iommi.Column):
    pass


class Table(iommi.Table):
    class Meta:
        member_class = Column
        form_class = Form
        query_class = Query
        page_class = Page
        action_class = Action


class Menu(iommi.Menu):
    pass


class MenuItem(iommi.MenuItem):
    pass
