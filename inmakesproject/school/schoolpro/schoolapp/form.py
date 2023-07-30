from.models import Student,Course,Department
from django import forms
from tempus_dominus.widgets import DatePicker

class StudentForm(forms.ModelForm):

      dob=forms.DateField(widget=forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control','type': 'date','style':'width:400px'}))
      # notebook=forms.BooleanField()

      class Meta:
          model= Student
          # fields = '__all__'
          fields = ['name', 'department', 'course', 'age', 'dob', 'address', 'email', 'gender', 'purpose',
                    'notebook','pen','exampaper']

          widgets = {'name': forms.TextInput(attrs={'class': 'form-control','style':'width:400px'}),
                     'department': forms.Select(attrs={'class': 'form-control','style':'width:400px'}),
                     'course': forms.Select(attrs={'class': 'form-control','style':'width:400px'}),
                     'age': forms.NumberInput(attrs={'class': 'form-control','style':'width:400px'}),

                     'address': forms.TextInput(attrs={'class': 'form-control','style':'width:400px'}),
                     'email': forms.EmailInput(attrs={'class': 'form-control','style':'width:400px'}),
                     'gender': forms.Select(attrs={'class': 'form-control','style':'width:400px'}),
                     'purpose': forms.Select(attrs={'class': 'form-control','style':'width:400px'}),

                     }
      def __init__(self,*args,**kwargs):
          super().__init__(*args,**kwargs)
          self.fields['course'].queryset =Course.objects.none()

          if 'department' in self.data:
              try:
                  department_id=int(self.data.get('department'))

                  self.fields['course'].queryset =Course.objects.filter(department_id=department_id).all()
              except(ValueError,TypeError):
                  pass


# class StudentForm(forms.Form):
#     department = forms.Select(choices=Department.objects.all().values_list('name', flat=True))
#     course = forms.Select(choices=[])
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].choices = []
#
#         if self.cleaned_data['department']:
#             courses = Course.objects.filter(department=self.cleaned_data['department']).values_list('name', flat=True)
#             self.fields['course'].choices = courses

# class StudentForm(forms.Form):
#       department = forms.ModelChoiceField(queryset=Department.objects.all())
#       courses = forms.ModelMultipleChoiceField(queryset=Course.objects.none())