from allauth.account.views import SignupView


class UserSignupView(SignupView):
    template_name = "account/signup.html"

    def dispatch(self, request, *args, **kwargs):
        print("I am really here!")
        return super(UserSignupView, self).dispatch(request, *args, **kwargs)
signup = UserSignupView.as_view()
