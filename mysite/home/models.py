from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.models import Page

from website_blocks.blocks import hero, features, separators

from wagtailseo.models import SeoMixin, SeoType, TwitterCard

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtailyoast.edit_handlers import YoastPanel


class BasePage(SeoMixin, Page):

    # wagtailseo
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels

    content_panels = Page.content_panels

    # wagtailyoast
    keywords = models.CharField(default='', blank=True, max_length=100)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(promote_panels, heading=('Promotion')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])

    class Meta:
        abstract = True



class HomePage(BasePage):
    #templates = "home/home_page.html"


    body = StreamField([
        ('Hero1', hero.Hero1()),
        ('Features1', features.Feature1()),
        ('Features2', features.Feature2()),
        ('SeparatorTextDescription', separators.SeparatorTextDescription()),
    ])

    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]


