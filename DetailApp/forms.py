from DetailApp.models import ClientApp
from django.forms import PasswordInput, ModelForm, CharField

class FormAppDetail(ModelForm):
    # PASSWORD_SERVER = CharField(widget=PasswordInput)

    # class Meta:
    #     model = ClientApp

    class Meta:
        fields = [ 'App','name', 'version', 'Description', 'Active', 'Server_Address', 'send_port', 'DataBase_Address', 'DataBase_Name', 'DatabasePort', 'PASSWORD_SERVER', 'USER_SERVER', 'BarcodeRestart', 'BarcodeShutdown']
        model = ClientApp
        widgets = {
            'PASSWORD_SERVER':PasswordInput(),
        }

