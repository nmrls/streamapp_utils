# streamapp

Base modules to use in a Streamlit project.

- Snowflake connection with templates
- Cards generator for landing page
- Environment selector if needed
- Auth module to login users and grant roles
- Report generator for .xlsx files and templates
- Request handler to integrate with .secrets
- Subpages selector

## Requirements

```
streamlit>=1.30.0
streamlit-authenticator==0.2.2
snowflake-connector-python>=3.0.4
openpyxl==3.1.2
pydantic>=2.5.3
pymongo==4.6.3
twine>=4.0.2
```

# Secrets file
Create a in ./.streamlit folder a secrets.toml file for app configuration
```
# environment variables
key = streamlit cookies key for auth module
snow_key = key for hased snowflake password with Fernet
queries_path = 'static/queries'  # your folder queries path
utils_files = 'static/consume'  # your static files path
admin_contact = 'admin@admin.com'  # show contact if something went wrong
dev = false  # sert true to see a detailed error in development
allowed_roles = ['analysts', 'support', 'guess', 'admin']  # roles for UI interface

# snowflake credentials
# see snowflake documentation
[SNOW_SERVER]
account = '************'
database = '*********'
warehouse = '******'
role = '*********'
user = '**********'
password = '***********'

# see streamlit authenticator documentation
[credentials.usernames]
Pepe.name = '**********'
Pepe.roles = ['admin', 'dev', 'other]
Pepe.password = 'password hash'

# if you prefer user credentials in an Mongo DDBB
[mongo_auth]
host = 'localhost'
port = 27017
username = 'root'
password = 'example'

[mongo_conf]  # Optional if you prefer set up an specific database and collection
database = 'credentials_test'  # Mongo database name, default credentials
collection = 'users_test'  # Mongo database collection, default users

[auth_cookie]
cookie_name = 'cookie'
cookie_key = 'INTJB0EvLz1PzeEVp...'
cookie_expiry_days = 1

[ENVIRONMENTS]
name.image = ''  # Some image to show for the environment
name.url = 'https://pokeapi.co'  # host url for request with different environments  

[REQUESTS]
get_pockemon.url = '/api/v2/berry/'
get_pockemon.method = 'get'
```

# Config file
Create a in ./.streamlit folder a config.yaml file for user credentials and cookkie management, see streamlit authenticator documentation
*Users only if you are using local credentials instead of mongo credentials*
```
credentials:
  usernames:
    Pepe:
      name: 'pepe@mail.com'
      roles: ['admin', 'user', 'service']
      password: '$2b$12$6E4nrCcqAheeU9OE3zSQWeJjpEiJ6HL1AdXgo5vmE1yJ9z1XnqLq'
cookie:
  name: 'my_cookie_name'
  key: 'INTJB0EvLz1PzeEVp...'
  expiry_days: 1
```

### Generate Passwords
To generate passwords use `Hasher` from `streamlit_authenticator`
```Hasher([password]).generate()[0]```
