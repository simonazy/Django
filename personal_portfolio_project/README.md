Steps:
1. Create folder personal_portfolio `cd personal_portfolio`
2. Use `django-admin startproject personal_portfolio` to create a subfolder and manage.py file 
3. Rename the main directory to  `personal_portfolio_project` for a clearer structure.
4. Create 2 apps for this site: `python manage.py startapp blog`, `python manage.py startapp portfolio`
5. Generate the db.sqlite3: `python manage.py migrate` and make migrations `python manage.py makemigrations`
6. Create an admin in admin page: `python manage.py createsuperuser`
7. Manipulate models, views, urls, templates(learned to extend base html), and static to create the sites. 
