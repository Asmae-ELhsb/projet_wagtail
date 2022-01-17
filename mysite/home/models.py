from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.models import Page

from website_blocks.blocks import hero, features, separators




class HomePage(Page):
    #templates = "home/home_page.html"


    body = StreamField([

        ('Hero1', hero.Hero1()),
        ('Features1', features.Feature1()),
        ('Features2', features.Feature2()),
        ('SeparatorTextDescription', separators.SeparatorTextDescription()),


    ])

    content_panels = Page.content_panels + [

        StreamFieldPanel('body'),
    ]

