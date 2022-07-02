# pace
Next tarantino is a simple app. Just need to develop some endpoints. There are four endpoints.
I am used Django for this project. Django enforces MVT structure, so I have used that. 
I have also used django-tables2 and django-filter for table and filtering. There is only
one model class needed for this project which is `Movie`. 

## Prepare Environment
* ``git clone https://github.com/nahidsaikat/pace.git``
* ``cd pace``
* ``virtualenv .venv``
* ``source .venv/bin/activate``

## Run the projeect
* ``cd next_tarantino``
* ``python manage.py migrate``
* ``python manage.py runserver``

## List of URLs
* localhost:8000/movies/
* localhost:8000/movies/create/
* localhost:8000/movies/{pk}/
* localhost:8000/movies/{pk}/favorite/

