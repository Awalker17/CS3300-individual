# CS3300 individual

* [Environment setup](#django-setup)
* [Creating a Project](#project-setup)
* [Install Bootstrap](#installing-bootstap)

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