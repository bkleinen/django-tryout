.PHONY : django
.RECIPEPREFIX = -


django:
- open http://127.0.0.1:8000/bib
- python3 manage.py runserver