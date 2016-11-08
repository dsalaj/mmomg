from allauth.account.views import SignupView, LoginView


class UserSignupView(SignupView):
    template_name = "account/signup.html"

    def dispatch(self, request, *args, **kwargs):
        print("dispatching UserSignupView")
        return super(UserSignupView, self).dispatch(request, *args, **kwargs)
signup = UserSignupView.as_view()


class UserLoginView(LoginView):
    template_name = "account/login.html"

    def dispatch(self, request, *args, **kwargs):
        print("dispatching UserLoginView")
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)
login = UserLoginView.as_view()
