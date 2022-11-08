pip install -r requirements.txt
python manage.py makemigrations pullgerAccountManager
python manage.py makemigrations com_linkedin
python manage.py makemigrations com_linkedin__TT
python manage.py makemigrations djTaskBrocker
python manage.py migrate
python manage.py createsuperuser