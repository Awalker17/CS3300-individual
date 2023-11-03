# CS3300 individual

* [Environment setup](#django-setup)
* [Creating a Project](#project-setup)
* [Install Bootstrap](#installing-bootstap)
* [Ready Django](#change-settings-make-app-and-edit-app-urls-and-views)
* [Making Models](#models)
* [SuperUser](#making-a-superuser)
* [Detail views and List views](#detail-views-and-list-views)
* [How to make a link to another internal page](#linking-to-another-page)

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
