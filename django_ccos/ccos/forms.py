from django import forms


class RegisterForm(forms.Form):
    user_id = forms.CharField(label="账号", max_length=128,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': "Userid", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': "Password"}))
    user_name = forms.CharField(label="用户名", max_length=128,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': "Username"}))
    address = forms.CharField(label="地址", max_length=128,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': "Address"}))
    contact_name = forms.CharField(label="联系名称", max_length=128,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': "Contact name"}))
    phone_number = forms.CharField(label="电话号码", max_length=128,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': "Phone number"}))


class LoginForm(forms.Form):
    user_id = forms.CharField(label="账号", max_length=128,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': "Userid", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': "Password"}))
