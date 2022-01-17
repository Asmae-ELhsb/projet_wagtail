from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from website_blocks.blocks.links import Link


class Feature1(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Dimensions minimum: 450x475px")
    title1 = blocks.CharBlock(default="Title 1", required=False)

    title2 = blocks.CharBlock(default="Title 2", required=False)
    our_link = Link(help_text="Enter a link or select a page", required=False)

    # ListBlock = Enables creation of the same block multiple times
    features = blocks.ListBlock(
        # StructBlock = Constructing 1 block from multiple Blocks
        blocks.StructBlock([
            ('text', blocks.CharBlock(default="Feature text", required=False)),
        ])
    )

    class Meta:
        template = 'features/feature1.html'
        icon = 'image'


class Feature2(blocks.StructBlock):
    # image = ImageChooserBlock(help_text="Dimensions minimum: 200x200px")
    # title = blocks.CharBlock(default="Title", required=False)
    # description = blocks.RichTextBlock(default="RichText", required=False)

    ###########################################################
    title1 = blocks.CharBlock(default="Title 1", required=False)
    # ListBlock = Enables creation of the same block multiple times
    services = blocks.ListBlock(
        # StructBlock = Constructing 1 block from multiple Blocks
        blocks.StructBlock([
            ('image', ImageChooserBlock(help_text="Dimensions minimum: 200x200px")),
            ('title', blocks.CharBlock(default="Title", required=False)),
            ('description', blocks.RichTextBlock(default="RichText", required=False)),
        ])
    )

    class Meta:
        template = 'features/feature2.html'
        icon = 'image'

