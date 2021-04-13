# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', parent_link=True, primary_key=True, auto_created=True)),
                ('form_name', models.CharField(max_length=60, verbose_name='Form name', help_text='Used to distinguish multiple contact forms on the same site.', blank=True)),
                ('form_layout', models.CharField(choices=[('cmsplugin_contact.forms.ContactForm', 'default'), ('quomodusapp.forms.ContactForm', 'Quomodus contact form')], max_length=255, verbose_name='Form Layout', help_text='Choose the layout of contact form')),
                ('site_email', models.EmailField(max_length=254, verbose_name='Email recipient')),
                ('thanks', models.TextField(default='Thank you for your message.', max_length=200, verbose_name='Thanks message', help_text='Message displayed on successful submit')),
                ('submit_text', models.CharField(default='Submit', max_length=30, verbose_name='Submit button value')),
                ('spam_protection_method', models.SmallIntegerField(choices=[(0, 'Honeypot'), (1, 'Akismet'), (2, 'ReCAPTCHA')], default=0, verbose_name='Spam protection method')),
                ('akismet_api_key', models.CharField(max_length=255, blank=True)),
                ('recaptcha_public_key', models.CharField(max_length=255, blank=True)),
                ('recaptcha_private_key', models.CharField(max_length=255, blank=True)),
                ('recaptcha_theme', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=20, verbose_name='ReCAPTCHA theme')),
                ('recaptcha_size', models.CharField(choices=[('normal', 'Normal'), ('compact', 'Compact')], default='normal', max_length=20, verbose_name='ReCAPTCHA size')),
                ('redirect_url', models.URLField(verbose_name='URL Redirection', help_text='If it is set, the form redirect to url when the form is valid', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
