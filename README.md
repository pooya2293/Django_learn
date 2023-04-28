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