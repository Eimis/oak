# oak

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

Create `.env` file near settings.py file in 'oak' app and set dabatase settings
in that file:

```
DB_NAME=your_db_name
DB_USER=db_user
DB_PASSWORD=db_password
```

`./manage.py migrate`

`./manage.py runserver`

Congratulations, API server is running!
