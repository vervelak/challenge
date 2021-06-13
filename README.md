# challenge
## Coding part
Inside the "coding" folder there is a flask api with the following endpoint /api/v1/<int> that actions the requirements.
It also includes some pytest(s) as well :)
(parts that I wasn't able to complet in time: dockerfile, github pipeline, swagger file/endpoint)
steps to run/test:
```bash
cd coding
pip install -r requirements.txt
pytest
flask run
```
Navigate to http://127.0.0.1:5000/api/v1/14 in order to manual test the api.

## Architecture part
Inside the "arch" folder you will find a screenshot with my design for the cookie oven (I have some questions in order to make it production ready)