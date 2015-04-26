# MovieWatch app
This application was developed by ITESM CEM students as part of the
Advanced Databases class.

The application lets you to create a catalog of films and provide them to the
users so they can watch those films from a web browser.

## Running the applications
    # Setup database
    mysql -u root -p < all.sql

    # Install requirements
    pip install -r requirements.txt

    # Make migrations and create your admin user
    python manage.py migrate
    python manage.py createsuperuser

    # Run application
    python manage.py runserver

Once app is running you can access it from <http://localhost:8000/>

## Routes
So far the app has the next application and routes

+ /admin/

## TODO
We must implement the next apps and routes
+ / (index)
+ /signup (signup page)
+ /login (login page)
+ /movies/ (catalog of movies)
+ /movies/:movie (details for movie)


## Authors
- Fernando Gómez <gomezhyuuga@gmail.com>
- Rodolfo Ramírez <rodolfo@ramirezvalenzuela.com>
- Luis Ballinas <lu15bytes@gmail.com>


