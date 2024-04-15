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
pydantic>=2.6.2
```

# Secrets file
```
# enviroment variables
key = key for hased passwords with Fernet
queries_path = 'static/queries'  # your folder queries path
utils_files = 'static/consume'  # your static files path
admin_contact = 'admin@admin.com'  # show contact if something went wrong 

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

[ENVIRONMENTS]
name.image = ''  # Some image to show for the environment
name.url = 'https://pokeapi.co'  # host url for request with different environments  

[REQUESTS]
get_pockemon.url = '/api/v2/berry/'
get_pockemon.method = 'get'
```

### Generate Passwords
To generate passwords use `Hasher` from `streamlit_authenticator`
```Hasher([password]).generate()[]```