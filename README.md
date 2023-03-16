# PlayArena

### Initialize database

Before initializing database make sure to run 
```
python manage.py migrate
```

Then just run 
```
python manage.py load_initial_data
```

You can check user logins in **fixtures/user.json**. Password to each of them is "haslo123"
