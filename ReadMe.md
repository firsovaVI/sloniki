To get this project up and running locally on your computer:

1. Set up the Python development environment.
2. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):    ```
```bash
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

3. Open a browser to `http://127.0.0.1:8000` to see the main site.
4. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site.