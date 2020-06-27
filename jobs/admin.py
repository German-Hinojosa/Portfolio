from django.contrib import admin


# Register your models here.

#first we're trying to import the model, so we're gonna type (line below)
from .models import Job
#"from .models" is just referencing
#the models.py file (the . means the current directory)
#"import Job" which is the name of the model

#after we do that, we can say
admin.site.register(Job)
#admin as imported from the first line, and then continue
# .site.register() and in the parenthesis we're going
#to pass our model, which is Job
