# shell
- `python manage.py debugsqlshell`

- Jos halutaan tiedot `json muodossa` kirjoitetaan seuraavat comentit:
`python manage.py dumpdata goods.Category > fixtures/goods/categories.json`
`python manage.py dumpdata goods.Category > fixtures/goods/products.json`

- Django dokumentation mukaan `pip install psycopg2` 
- Uudestaan luodaan django admin- `python manage.py createsuperuser`
- categories.json sekä products.json:sta laitetaan data admin:lle:
* `python manage.py loaddata fixtures/goods/products.json`
* `python manage.py loaddata fixtures/goods/categories.json` 
- Django dokumentaatiossa etsimällä `Full text search` voidaan lisätä etsimään muutamia parametria : => utils.py:

```
Product.objects.annotate(
    search=SearchVector("name", "description"),).filter(search=query)

```


