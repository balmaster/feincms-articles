from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms import settings as feincms_settings
from django.conf import settings as django_settings

def register(cls, admin_cls):
    cls.add_to_class('thumbnail', models.ImageField(_('thumbnail'), max_length=250, upload_to=os.path.join(django_settings.MEDIA_URL,feincms_settings.FEINCMS_UPLOAD_PREFIX, 'articles/thumbnails'), null=True, blank=True))
    if admin_cls:
        if admin_cls.fieldsets:
            admin_cls.fieldsets[0][1]['fields'].append('thumbnail')


