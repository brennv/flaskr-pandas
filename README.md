![travisCI](https://travis-ci.org/brennan-v-/flaskr-sqlalchemy.svg) [![codecov.io](https://codecov.io/github/brennan-v-/flaskr-sqlalchemy/coverage.svg?branch=master)](https://codecov.io/github/brennan-v-/flaskr-sqlalchemy?branch=master)
 ![pythons](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.5--dev-blue.svg)

                         / flaskr-sqlalchemy /

                 a minimal blog application


    ~ What is flaskr-sqlalchemy?

      An sqlalchemy powered thumble blog application

    ~ How do I use it?

      1. clone the repo and step into it

          git clone git@github.com:brennan-v-/flaskr-sqlalchemy.git
          cd flaskr-sqlalchemy

      2. create a virtual environment and install packages

          virtualenv venv
          source venv/bin/activate

          pip install -r requirements.txt

            or
            
          pip install flask
          pip install flask-sqlalchemy

      3. start the application

          python flaskr.py

         the application will greet you on
         http://localhost:5000/

    ~ Attributions:

[mitsuhiko/flask/examples/flaskr](https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/)
      
[mitsuhiko/flask-sqlalchemy](https://github.com/mitsuhiko/flask-sqlalchemy)

[SQLAlchemy](http://www.sqlalchemy.org/)
