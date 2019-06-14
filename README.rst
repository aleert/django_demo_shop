This is a small demo shop made with django. It has fancy and useful Cart class
to store carts in sessions, supports different categories of products and have
custom user model (that have urls to register, edit etc, but not really used anywhere).

Setup
-----

There are several steps to run this project.

1. Install dependencies with ``pip install -r requirements.txt`` or ``poetry install``.

2. Make some database setup:

    2.1  Install postgresql if you havent already.

    2.2 Run following commands in ``psql`` shell to create database and user:

.. code-block:: sql

    CREATE DATABASE myshop;
    CREATE USER myshop;
    GRANT ALL ON DATABASE myshop to myshop;
    ALTER USER myshop PASSWORD 'development';
    ALTER USER myshop CREATEDB;
    \q

3. Navigate to ``shop_demo/`` and run migrations with ``python manage.py migrate``

4. Load data with ``python manage.py loaddata fixtures``

5. Optionally, you can collect static files ``python manage.py collectstatic``, but everything
   should work without it.

6. Create superuser to acess ``admin/`` part of the site: ``python manage.py createsuperuser``

7. Run ``python manage.py runserver`` and explore

NB: there are also user related parts that are not available as links on pages, but rather by a direct url.
Those are start with 'user/' and you can find them all in ``user/urls.py``. Those urls are irrelevant for
this version of a project but you can extend it to say add possibility for user to check out all of his orders etc.
