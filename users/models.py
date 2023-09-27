from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext as _
from myapp.models import WorkPlace

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Telefon raqamini to'g'ri ko'rsating, masalan: +998901234567",
)

class AdminUser(AbstractUser):
    # USERNAME_FIELD = 'phone'
    phone = models.CharField(
        validators=[phone_regex],
        max_length=15,
        unique=True,
    )
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this admin user belongs to.'),
        related_name='admin_user_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this admin user.'),
        related_name='admin_user_permissions'
    )
    def __str__(self):
        return self.username








