from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from website_blocks.blocks.links import Link


class Hero1(blocks.StructBlock):
    title1 = blocks.CharBlock(default="Title 1", required=False)
    title2 = blocks.CharBlock(default="Title 2", required=False)

    button = Link(help_text="Enter a link or select a page", required=False)
    background_image = ImageChooserBlock(help_text="Dimensions minimum: 1920x1280px")

    class Meta:
        template = 'hero/hero1.html'
       # D:\projet_wagtail\mysite\website_blocks\templates\hero\hero1.html
        icon = 'image'