import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_validator(phone: str):
    pattern = r"^(09)([0-9]{9})$"

    if not re.search(pattern, phone):
        raise ValidationError(_("Phone number length is 11 and must starts with 09"))
