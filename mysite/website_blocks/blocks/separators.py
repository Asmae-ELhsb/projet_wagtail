from django.db import models
from wagtail.core import blocks
from wagtail_color_panel.blocks import NativeColorBlock



class SeparatorTextDescription(blocks.StructBlock):
    title = blocks.CharBlock(default="Title 1", required=False)
    description = blocks.RichTextBlock(default="RichText", required=False)
    background_color = NativeColorBlock(required=True)

    class Meta:
        template = 'separators/separator1.html'
