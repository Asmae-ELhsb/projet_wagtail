from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from website_blocks.blocks import hero, separators, features

class AboutPage(Page):

    body = StreamField([

        ('Hero1', hero.Hero1()),
        # Feature des services
        ('Features', features.Feature1()),

    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    #template = "website_pages/about_page.html"