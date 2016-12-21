from django.db import models
from django.conf import settings
from django.utils.translation import ugettext
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinLengthValidator

from apps.misc_api.utils import PhoneValidator


@python_2_unicode_compatible
class UserPurchaseHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(max_length=255)
    purchase = models.CharField(max_length=150, default=None, validators=[MinLengthValidator(2)])
    purchase_id = models.IntegerField()
    name = models.CharField(max_length=150, default=None, validators=[MinLengthValidator(2)])
    phone_number = models.CharField(
        validators=[
            PhoneValidator,
            MinLengthValidator(10)
        ],
        default=None,
        max_length=20
    )
    address = models.TextField()

    def __str__(self):
        return ugettext('UserPurchaseHistory<%d:%s:%s:>') % (
            self.user.pk,
            self.date,
            self.purchase,
        )
