# Generated by Django 2.2.6 on 2020-01-08 20:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20200108_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rows', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock(help_text='This will set the background image of the row.', required=False)), ('padding', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a padding size'), ('none', 'None'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Select how much top and bottom padding you would like on the row.', required=False)), ('content', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('width', wagtail.core.blocks.IntegerBlock(blank=True, default=12, help_text='Select the width of the column, max of 12.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('carousel', wagtail.core.blocks.StreamBlock([('carousel_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('quote', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a blockquote size'), ('short', 'Short'), ('long', 'Long')], required=False)), ('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))]))], help_text='Add content to column.'))]))], help_text='Add column to row.'))]))], blank=True, verbose_name='Page body'),
        ),
    ]
