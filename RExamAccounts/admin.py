from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from RExamAccounts.models import UserProfile, StudyGroup


class UserProfileChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserProfileAdmin(UserAdmin):
    form = UserProfileChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'middle_name', 'study_group', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


# Перерегистрируем модель User
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(StudyGroup)
