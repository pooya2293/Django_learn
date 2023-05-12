# Django_learn

# when you whant to instal django on your comuter first

pip install django

# instal virtualenv wrapper on your comuter first

pip install virtualenvwrapper-win

# instal virtualenv in your project

E:\code\python\learning\your project path > mkvirtualenv myapp

# when you make virtualenv in your project in cmd you shuold see this befor your cmd path shell

For EX:(myapp)E:\code\python\learning\your project path >

# when you can't see (myapp) run this

E:\code\python\learning\your project path >workon myapp

# when you whant Exit from virtualenv run this

E:\code\python\learning\your project path >deactivate

# now when you whant to intsal django on your project run this

# -(you should in your virtualenv mode run this)

(myapp)E:\code\python\learning\your project path >pip instal django

# then finally u should run this to start yuor django project

(myapp)E:\code\python\learning\your project path >django-admin startproject popoProject

# when we whant creat app after that run this

# -(we dont want manage.py actually)

(myapp)E:\code\python\learning\your project path\popoProject >python manage.py startapp myapp

# when we whant run our project

(myapp) E:\code\python\learning\Django_learn\popoProject>python manage.py runserver

# when we whant save chnage in models

E:\code\python\learning\Django_learn\popoProject>python manage.py makemigrations

# when we whant to migrate (load) an models

E:\code\python\learning\Django_learn\popoProject>python manage.py migrate

# create Admin user

E:\code\python\learning\Django_learn\popoProject>python manage.py createsuperuser

# link postgresql to your Django project

first download postgresql and next run PgAdmin ->
1-write click in ui Databases in PgAdmin -> create -> database...
2-write database name and -> save in here: pooryaProject
note:in here when you go to ->Databases->pooryaProject->Schemas->Tables
you do not see any tabel from your project
3-edite some info in setting.py that you can see
4-install tow pip package
first: E:\code\python\learning\Django_learn\popoProject>pip install psycopg2
second: E:\code\python\learning\Django_learn\popoProject>pip install pillow
5-E:\code\python\learning\Django_learn\popoProject>python manage.py makemigrations
6-E:\code\python\learning\Django_learn\popoProject>python manage.py migrate
7- then in here when you go to ->Databases->pooryaProject->Schemas->Tables
Now you can see yor tabels and now you can go to ->
8-myapp_feature -> riteClick -> view/Edit Data -> All Rows :now you can Add row in Data Output
