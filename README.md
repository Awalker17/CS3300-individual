# CS3300 individual

* [Environment setup](#django-setup)
* [Creating a Project](#project-setup)
* [Install Bootstrap](#installing-bootstap)
* [Ready Django](#change-settings-make-app-and-edit-app-urls-and-views)
* [Making Models](#models)
* [SuperUser](#making-a-superuser)
* [Detail views and List views](#detail-views-and-list-views)
* [How to make a link to another internal page](#linking-to-another-page)
* [How to create a model create page](#new-modelshow-create-page)
* [How to create a model update page](#update-modelshow-page)
* [How to create a model delete page](#delete-modelshow-page)
* [Bootstrap](/Bootstrap.md)
* [How to make the dropdown menu on details page](#in-page-form)
    * [Here for views.py changes (see UserDetailView function)](#viewspy)
* [Users](#making-users)

# Setting up the envirnonment

# Django Setup

For this setup you may be intrested in fallowing this [page](https://docs.djangoproject.com/en/4.0/howto/windows/) instead.
I found the most sucsess using powershell but if you find CMD works for you go for it!

Start by seting up your virtual environment.
> [!IMPORTANT]
> Remember to replace the project Name with what you want the project to be called for the entirety of this guide.

```
py -3 -m venv Individual
```
Now you can activate the virtual environment
```
Individual\Scripts\activate
```

Now that the venv is active you can install django.
``` 
py -3 -m pip install Django
```
> [!IMPORTANT]
> if that command doesnt seem to be working try
```
pip install Django
```

You may want to upgrade pip at this time.
```
py -3 -m pip install --upgrade pip
```

For Help on creating a project go [here](#Project-Setup)

To deactivate your virtual environment run Ctrl-C (if you have a django project running) then enter deactivate.

# Project Setup

Once you have django installed and your vertual environment running you can fallow these instuctions. Remember to change the project name to your own.
```
django-admin startproject Individual_project
```
If you want to be able to activate your project from the same place you controll your virual environment go ahead and do this. (I beleive this is optional just makes your life a little easier in the long run)
```
mv Individual_project/manage.py ./ 
mv Individual_project/Individual_project/* Individual_project
rm -r Individual_project/Individual_project/
```
You can run your server now with the command. Remember if you skiped the last step you will need to modify this command path for manage.py or navigate to the folder containing manage.py
```
python manage.py runserver
```
Now you Have started the server go to [http://localhost:8000/](http://localhost:8000/) to se if its working. Use (on windows)ctrl+C to stop the server.

# Installing Bootstap

With the server deactivated but inside the environment run
```
pip install django_bootstrap5
```

# Change settings make app and edit app urls and views

There are several thing to change in Indvidula_project./settings.py

Include at the top
```
import os
```

change Installed_apps to

```
INSTALLED_APPS = [
# ...
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
# Add your app name here
'Website_app',
'django_bootstrap5'
]
```

and add
```
# Add support for authenticating users
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',]
```

at the bottom of the page after STATIC_URL include
```
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/images/'
```

run in command line 
```
django-admin startapp Website_app
```

In Website_app/views.py

```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'Website_app/index.html')
```

inside of Website_app/ create urls.py and put

```
from django.urls import path
from . import views
urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
]
```

Next You will need to create a base template and index.html

Inside of Website_app make the folders

Template and inside that make a folder named Website_app

inside that folder make base_template.html and include
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
<title>UCCS CS Students</title>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
{% load django_bootstrap5 %} 
{% bootstrap_css %}
{% bootstrap_javascript %}
</head>


<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" 
    data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
    <li class="nav-item">
    <a class="nav-link" href="{% url 'index' %}">Home</a>
    </li>
    <li class="nav-item">
    </li>
    <li class="nav-item">
    <a class="nav-link" href="#">Menu 2</a>
    </li>
    </ul>
    </div>
    </div>
    </nav>


<!-- add block content from html template -->
{% block content %}


{% endblock %}
</body>
</html>
```

next make another page index.html

```
<!-- inherit from base.html -->
{% extends 'Website_app/base_template.html' %}


<!-- Replace block content in base_template.html -->
{% block content %}


{% endblock %}
```

# models

inside models.py
You can add any model you want in Individual_project we made a show model

```
from django.urls import reverse

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('show-detail', args = [str(self.id)])
    
```

title and description are feilds

__str__ and get_absolute_url will be used for linking to the url and displaying the name of the show.

if you need to view these models inside the admin make a [superuser](#making-a-superuser) and put this code into the admin.py

```
from .models import *

# Register your models here.

admin.site.register(Show)
```

any model you need to register just add a line replacing `Show` with the name of the model


## updating your model

When updating your models it is very important to clear the database first... or else your gonna run into problems.

1) Clear your data base you don't want to forget this so do it fisrt

2) Make changes to your model

3) run 

```
python manage.py makemigrations
python manage.py migrate
```

If you get this issue:
It is impossible to add a non-nullable field 'episode' to show without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.

 type `1` then type `None`

 That should fix the issue

4) Run your server and check your work.

Remember to update any views as nessisary

### I forgot to clear the database

Heres how to fix it.

1) manualy delete the db.sqlite3 file in your website
2) run
```
python manage.py flush
```
answer `yes`
3) remake [superuser](#making-a-superuser)
4) repopulate models with test data
5) and go back to [step 3 in updating model](#updating-your-model)


# Making a superuser

inside the console run

```
python manage.py createsuperuser
```
then fallow the instructions.

# Detail views and List views

Making these two types of pages is easy but there are alot of places to go wrong.

## Detail View

Start with making the html page. Under templates then Website_app make a new file named `model_detail.html` mine is called `show_deltai.html`

Next move to the views. Add a class for the view like:

```
class ShowDetailView(generic.DetailView):
    model = Show
```
if you havent already go ahead and import the models by `from .models import *` you can replace * with a specific model name if you want.

next go into your urls.py and add

```
path('show/<int:pk>', views.ShowDetailView.as_view(), name = 'show-detail')
```

Now you can make your webpage. Go back to your `model_detail.html` page and add a few things.

```
<!-- inherit from base.html -->
{% extends 'Website_app/base_template.html' %}


<!-- Replace block content in base_template.html -->
{% block content %}

<!-- Your webpage content goes here -->

{% endblock %}
```

Populate the page with whatever you need. Note if you need to add details for a model that isn't in the models feilds you will need to do extra steps. In the mean time you can add things like

```
<p><strong>Show: {{show.title}}</strong></p>
<p>Current episode: {{show.season}}:{{show.episode}} </p>
<p>{{show.description}}</p>
```
this looks like

<p><strong>Show: NAME</strong></p>
<p>Current episode: #:# </p>
<p>Donec ipsum purus, consequat id libero suscipit, convallis pellentesque erat. Donec sit amet metus tempus, dictum erat vitae, tempus velit. Curabitur sit amet turpis lacus. Quisque egestas, sem nec efficitur ornare, tortor eros bibendum mauris, eu scelerisque elit ex quis enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>

## List View
Start with making the html page. Under templates then Website_app make a new file named `model_list.html` mine is called `show_list.html`

Next move to the views. Add a class for the view like:

```
class ShowListView(generic.ListView):
    model = Show
```

if you havent already go ahead and import the models by `from .models import *` you can replace * with a specific model name if you want.

next go into your urls.py and add

```
path('show', views.ShowListView.as_view(), name= "show-list"),
```

Now you can make your webpage. Go back to your `model_detail.html` page and add a few things.

```
<!-- inherit from base.html -->
{% extends 'Website_app/base_template.html' %}


<!-- Replace block content in base_template.html -->
{% block content %}

<h1>All shows inputed</h1>

<ul class="list-group">

{% if show_list %}
<ul>
{% for show in show_list %}
<li>
    <a href="{{ show.get_absolute_url }}">{{ show.title }}</a>
    </li>
{% endfor %}
</ul>
{% else %}
<p>There are no shows registered.</p>
{% endif %}

{% endblock %}

```

# Linking to another page

Go to urls.py and double check what the name is for the path you intend to fallow. Lets pretend we want to go to show_list.html.
```
path('show', views.ShowListView.as_view(), name= "show-list")
```
the path you want to use is `show-list`. Now got to the html page you want to have this link to.
```
<a href = "{% url 'show-list' %}">Here</a>
```
reconize these key elements:`<a></a>` link is used, `href= "{% url '' %}"` is the link format, then inside the '' your path name is used.

# New Model/show create page

## Step 1 
Make a new file named forms.py inside of the Website_app

add the fallowing code:
```
from django.forms import ModelForm
from .models import *

class ShowForm(ModelForm):
     class Meta:
        model = Show
        fields =('title', 'description')
```

For different models replace the `model = show ` with the apropiete model. To change the form fields you can add any of the fields from the model or use `'__all__'` to simply put in all of them.

## Step 2
Make a file named 'show_form.html' inside your templates/Website_app folder.

```
<!-- inherit from base.html -->
{% extends 'Website_app/base_template.html' %}


<!-- Replace block content in base_template.html -->
{% block content %}


<form action="" method="POST">


{% csrf_token %}
<table>
{{ form.as_table }}
</table>
<input type="submit" name="Submit">
</form>


{% endblock %}
```

## Step 3
Inside your views add the fallowing

```
from django.shortcuts import redirect, render
```

```
def createShow(request):
    form = ShowForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and show_id
        show_data = request.POST.copy()
        
        form = ShowForm(show_data)
        if form.is_valid():
            # Save the form without committing to the database
            show = form.save(commit=False)
            
            show.save()

            # Redirect back to the show detail page
            return redirect('show-list')

    context = {'form':form}
    return render(request, 'Website_app\show_form.html', context)
```

This is code for a model with no relations. If their are relations you will need to modify it a bit.

Inside the def line add your id's as nessisary in the format `request, modelname_id` and as you need more relationships add more `, modelname_id`.
Make sure they are clear and distinct.

After `form = Showform()` aprox. line 2 add.
```
modelname = Modelname.objects.get(pk=modelname_id)
```
pay attention to the capitalization.

After the if statement beteen `show_data = ...` and `form = ...` add `show_data['modelname_id'] = madelname_id` this will set the id of the apropriet data feild. 
Remember i'm useing show_data but you will need to replace all the shows with the name of the model your making a form for.

Next up after `show = form.save(commit=False)` add `show.modelname = modelname` this will make sure to add all the data for your model as apropriet.

Last in `return redirect('show-list')`  after `'show_list'` add  modelname_id

> [!IMPORTANT] 
> You need to update your url to include `<int:modelname_id>`, and if you have any links to the page remember to add `'modelname.id'` as nessissary. 
> if you have any views to this page you will also need to add to the redirect as nessisary

## Step 4 

Now head into the urls.py and add your path

```
path('show/create_show', views.createShow, name='create_show'),
```
In this case the show list contains the new button (for now this might change later) so using the show-list path add `/create-show` then the name of your view method and then name your path.

## Step 5

Add your button. You can put them in a few places or just one but don't forget to add it. Style as needed. In this case I put the button in `show_list.html` towards the top.
<a href = "{% url 'create_show' %}">New</a>

Give it ago! And remember if its not compleatly working try checking that you spell everything correctly didn't miss a step and change ALL the names of the models from the example.

# Update model/show page

If you've already made a Create model page then you wont need to do much if you haven't fallow steps 1 and 2 in the [New model](#new-modelshow-create-page) section.

## Step 1

In Views.py add the fallowing code

```
from django.shortcuts import redirect, render
```

```
def updateShow(request, show_id):
    show = Show.objects.get(id = show_id)
    form = ShowForm(instance=show)

    if request.method == 'POST':
        # Retrieve the show based on the show_id
        print('printing POST:', request.POST)
        print('Show id:', show_id)
        form = ShowForm(request.POST, instance=show)
        
        if form.is_valid():
            # Save the form without committing to the database
            show = form.save(commit=False)

            show.save()
            # Redirect back to the show detail page
            return redirect('show-detail', show_id)


    context = {'form': form}
    return render(request, 'Website_app/Show_form.html',context )
```
To add relationship to this code do the fallowing for each relationship.

In `def updateShow(request, show_id):` add your `modelname_id` simular to show_id.

After `form = ShowForm(instance = show)` add `modelname = Modelname.objects.get(id = modelname_id)`
Pay attention to the capitiziation.

Bewteen `show = ...` and `show.save()` add `show.modelname = modelname`

## Step 2

Add your path 
```
path('show/<int:show_id>/update_show', views.updateShow, name='update_show'),
```
> [!IMPORTANT] 
> You need to update your url to include `<int:modelname_id>`, and if you have any links to the page remember to add `'modelname.id'` as nessissary. 
> if you have any views to this page you will also need to add to the redirect as nessisary

# Delete Model/show page

If you have yet to do Step 1 from [New Model](#new-modelshow-create-page) go ahead and do that now.

## Step 1 
Make a new file in templates\Website_app called `show_delete.html` and put the fallowing into the file

```
{% extends 'Website_app/base_template.html' %}


{% block content %}


<p>Are you sure you want to delete "{{show}}"?</p>

<form method="POST" action="{% url 'delete_show' show.id %}">

{% csrf_token %}
<a href="{% url 'show-list' %}">Cancel</a>
<input type="submit" name="Confirm">

</form>


{% endblock %}
```
if you add relations you will need to change the `action = ""` url

## Step 2

Inside of the view.py page add

```
from django.contrib import messages
```

```
def deleteShow(request, show_id):
    show = Show.objects.get(id = show_id)

    if request.method == "POST":
        show.delete()
        messages.success(request, "The show has been deleted.")
        
        return redirect('show-list')

    context = {"show": show}
    return render(request, 'Website_app/show_delete.html',context )

```

If you need to add a relation change the fallowing:

In `def deleteShow(request, show_id):` add `modelname_id` for each relation

In ` context = {"show": show}` add a second dictionary key named modelname_id with modelname_id as the value


## Step 3 

Move to the urls.py page and add:
```
path('show/<int:show_id>/delete_show', views.deleteShow, name='delete_show'),
```
Remember if you need to add relations add another `<int:modelname_id>`

## Step 4

In the page you want to have the delete button add:

```
<a class="btn btn-danger" role="button" href = "{% url 'delete_show' show.id %}">Delete</a>
```
Remember if you need to add relations be sure to add the id here aswell.




# In page form
Here I have a select form that is named `Show_types`
This is in the main html page.
```
<form method="GET" style="padding: 10px;">
<select class="form-select form-select-sm w-25" name = "Show_types">
    <option value = "All Shows">All Shows</option>
    <option value = "Unfinished">Unfinished</option>
    <option value = "Finished">Finished</option>
</select>
<input type="submit" value="Search">
</form>
```
Then in the views.py I have a search function for what do for each selection

```
shows = None
    if request.GET.get("Show_types"):
        results = request.GET.get("Show_types")
        shows = Show.objects.all()
        print(results)
        if results == "Unfinished":
            shows = shows.filter(finished = False)
        elif results == "Finished":
            shows = shows.filter(finished = True)
```
# Making Users 

[Video Guide- Django Authentication & User Management - Full Tutorial](https://www.youtube.com/watch?v=WuyKxdLcw3w)
^ this video is an excelent visual guide for how to makeing users and their permissions

Things to install inside your virtual environment
```
python -m pip install crispy-bootstrap5
python -m pip install django-crispy-forms
```
For assistance in crispy bootstrap5 go [here](https://pypi.org/project/crispy-bootstrap5/)

For assistance in crispy forms go [here](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

in your setting.py add:
```
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
)
```
And you may need to add:

```
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
```

While your in setting.py there are a few the video did not cover that I had issues in.

where I could not move from the login or sign-up page to another. Consider including the fallowing line.
```
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000/sign-up', 'http://localhost:8000/login']
```

## detail and list veiws
In the views.py page, forms.py page, models.py page and the urls.py page you aka anywhere you use User include
```
from django.contrib.auth.models import User
```
The list views was not particularly unique and didn't have any issues.
```
class UserListView(generic.ListView):
    model = User
```
However the standard detail veiw was causing issues because I wanted to include a form.
```
def UserDetailView(request, user_id):

    shows = None
    shows = Show.objects.all().filter(user = user_id)
    if request.GET.get("Show_types"):
        results = request.GET.get("Show_types")
        print(results)
        if results == "Unfinished":
            shows = shows.filter(finished = False)
        elif results == "Finished":
            shows = shows.filter(finished = True)

    user = User.objects.get(id = user_id)
    return render( request, 'Website_app/user_detail.html', {'otheruser': user, 'shows':shows})

```

Notice I rename the context from just user to `otheruser` This was to fix an issue with the logged in user and the user for the current page were conflicting. 

For the fallowing sections remeber to change all show urls and functions and classes to reflect the fact that shows now rely on users.

## urls.py User paths

The main paths I wrote were

```
path('user/<int:user_id>', views.UserDetailView, name = 'user_detail'),

path('user/<int:user_id>/create_show', views.createShow, name='create_show'),

path('user', views.UserListView.as_view(), name = 'user-list'),

path('user/create_user', views.createUser, name='create_user'),

path('user/<int:user_id>/delete_user', views.deleteUser, name='delete_user'),
```

## models.py
Be sure to include 
```
from django.contrib.auth.models import User
```
and add the user feild to the show model.

```
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```

The forien key here will be used to identfy who wrote what shows.

## forms.py
Be sure to include
```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
```

the create_user form uses the UserCreationForm a pre setup type of form to use.
```
class RegisterForm(UserCreationForm):
   email = forms.EmailField(required = True)
   class Meta:
      model = User
      fields =["username", "email", "password1", "password2"]
```

## views.py

3 views writen to support user creation and deletion

```
class UserListView(generic.ListView):
    model = User

def createUser(request):
    form = UserForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and user_id
        user_data = request.POST.copy()
        
        form = UserForm(user_data)
        if form.is_valid():
            # Save the form without committing to the database
            user = form.save(commit=False)
            
            user.save()

            # Redirect back to the user detail page
            return redirect('user-list')

    context = {'form':form}
    return render(request, 'Website_app/user_form.html', context)

def deleteUser(request, user_id):
    user= User.objects.get(id = user_id)

    if request.method == "POST":
        user.delete()
        messages.success(request, "The user has been deleted.")
        
        return redirect('user-list')

    context = {"user": user}
    return render(request, 'Website_app/user_delete.html',context )

def sign_up(request):
    print("hello from signup")
    if request.method == "POST":
        print("hello form post")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(user.id)
            return redirect('user_detail', user.id)

    else:
        print("hello form else")
        form = RegisterForm()
    return render(request, 'registration\sign-up.html', {"form": form})
```

The create show function must be updated to:
```
def createShow(request, user_id):
    form = ShowForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and show_id
        show_data = request.POST.copy()
        
        form = ShowForm(show_data)
        if form.is_valid():
            # Save the form without committing to the database
            show = form.save(commit=False)
            show.user = User.objects.get(id = user_id)

            show.save()

            # Redirect back to the show detail page
            return redirect('user_detail', user_id)

    context = {'form':form}
    return render(request, 'Website_app\show_form.html', context)
```
I had some major issues when making these changes: flushing the database fixed it.
## HTML pages

Inside of the templates folder include:
`registration` and `auth`
After encountering an error Django was looking for user_list.html in a folder called `auth`, after creating the folder simply move user_list.html into that folder.
>[!NOTE!]
>This may not be nesassary for you.

Inside of `registration` make two html files: `login.html` and `sign-up.html` 
These contain very simular code.


Sign-up
```
{% extends 'Website_app/base_template.html' %}
{%load crispy_forms_tags%}
{% block content%}


<form method = 'post'>
    {% csrf_token %}
    {{form|crispy}}

<p>Have an accont? Sign in <a href="/login">Here</a>!</p>
<button type="submit" class="btn btn-primary">Login</button>
</form>

{% endblock %}
```
Login
```
{% extends 'Website_app/base_template.html' %}
{%load crispy_forms_tags%}
{% block content%}


<form method = 'post'>
    {% csrf_token %}
    {{form|crispy}}

<p>Don't have an accont? Create one <a href="/sign-up">Here</a>!</p>
<button type="submit" class="btn btn-primary">Login</button>
</form>

{% endblock %}
```
`{{form|crispy}}` is a bootstrap form for your use.

# User permisions and control