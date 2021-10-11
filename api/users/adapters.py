from allauth.account.adapter import DefaultAccountAdapter


class UserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'username', request.data.get('name', ''))
        user_field(user, 'email', request.data.get('email', ''))
        user_field(user, 'company', request.data.get('company', ''))
        user_field(user, 'password', request.data.get('password', ''))
        user.save()
        return user
