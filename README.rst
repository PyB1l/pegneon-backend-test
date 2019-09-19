Pegneon Backend Test
====================

Requirements
------------
1. python 3.6+

1. Postgresql DB (
    host: localhost,
    port: 5434,
    dbname: pegneon_db,
    user: pegneon_admin,
    password: 1234)

2. pip install requirements.txt (psycopg2-binary may requires external system libs)

3. python manage.py migrate --settings=config.settings.dev

4. python manage.py runserver


Notes
-----

1. Project is layout is scoped in 3 django Apps. **Core** which is the basic app for functionality, **Api** which
has it's own versions (i.e endpoints, Interface contracts, serializers ) and **Dashboard** as the actual app
that users interact.

2. Because it's a multi-tenant platform (in reality you would have many companies ) i used a Unique Field accross
all DB tables so we can create Postgresql sharding clusters with no problem. Additionally, i
de-normalized the "tenant" relationships for faster queries. I.E every Employee is related to Company
and Department although is not needed to find Employee records for a specific company.

3. I used DRF, mostly because you suggested it, and Django Filters for API filtering.
   I have enabled some extra features (search, ordering).

4. I avoided to overload serializer create methods for relations, by providing the ability to
   attach the company or department by id (only for write).

5. I used a free theme (Paper Kit 2) styles for the dashboard page for showcasing template,
    theming layout. I've override a few styles in templates.

6. For the demo i only needed on template ('/game'), but i extracted the base scaffold just
   in case.

7. Static folders per App, so **collectionstatic** will always work before deploy.

8. Authorization in implemented in API scope (at least that's what it seemed from specs),
    it's session-based (thus thread-safe) without involving DJANGO_AUTH_USER settings due to it's scale limitations.
    This way you can build complex auth backend (i.e company admin login that edits departments and employees)

9. In slug I choose to make it optional and use name (and Company.name and Department.name)
    as default although you can provide values.

10. Pytest for unit testing. I have setup pytest with factory_boy for DB fixtures.