from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    # file= forms.FileField()
    # name = forms.CharField(
    #     label="Full Name : ", 
    #     help_text="Total length must be within 70 characters",
    #     required=False, 
    #     error_messages={'required': 'Please enter your name.'},
    #     widget = forms.Textarea(attrs = {'id' : 'text_area',
    #                                      'class' : 'class1 class 2', 
    #                                      'placeholder' : 'Enter your name'},))
    # email = forms.EmailField(label = "User Email")
    # # age = forms.IntegerField()
    # # weight = forms.FloatField()
    # # balance = forms.DecimalField()
    # age = forms.CharField(widget=forms.NumberInput)
    # check = forms.BooleanField()
    # birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    # appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    # MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    message = forms.CharField(max_length = 10)
    first_name = forms.CharField(initial='Your name')
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    email = forms.EmailField()
    agree = forms.BooleanField()
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))



def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
    
class StudentData(forms.Form):
    name =forms.CharField(validators=[validators.MinLengthValidator(10, 
                          message='Enter a name with at least 10 characters')])
    
    text = forms.CharField(widget=forms.TextInput, 
                           validators=[len_check])
    
    email =forms.CharField(widget=forms.EmailInput, 
                           validators=[validators.EmailValidator(
                            message="Enter a valid Email")])
    
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, 
                            message="age must be maximum 34"),
                            validators.MinValueValidator(24, 
                            message="age must be at least 24")])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(
                            allowed_extensions=['pdf','png'], 
                            message = 'File Extension must be ended with .pdf')])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")
        

