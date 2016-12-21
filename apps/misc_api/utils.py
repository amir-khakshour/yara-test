import re
import datetime

from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from rest_framework import throttling


phone_regx = re.compile(r'''
    ^           # start of the string
    (\d{2,4})   # area code is 3 digits (e.g. '800')
    -?          # optional dash separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of the string
    ''', re.VERBOSE)


class PhoneValidator(RegexValidator):
    regex = phone_regx
    message = _('Invalid Phone Number, please use a phone number with this format: 21-77363735 or 0915-1177495')


class JokingThrottling(throttling.BaseThrottle):
    """
    A dummy Throttler for test only!
    """
    def allow_request(self, request, view):
        return datetime.datetime.now().second % 2 == 0
