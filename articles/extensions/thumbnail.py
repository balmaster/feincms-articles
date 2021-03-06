import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms import settings

def register(cls, admin_cls):
    cls.add_to_class('thumbnail', models.ImageField(_('thumbnail'), max_length=250, upload_to=os.path.join(settings.FEINCMS_UPLOAD_PREFIX, 'articles/thumbnails'), null=True, blank=True))
    if admin_cls:
        admin_cls.add_extension_options(_('Thumbnail'), {
            'fields': ('thumbnail',),
        })


