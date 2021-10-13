from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # user.username = data.get('username')
        user.company = data.get('company')
        user.emissions_CO2e = data.get('emissions_CO2e')
        user.save()
        return user