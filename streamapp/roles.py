"""Custom Snowflake connector for Streamlit.

This custom connector tries to ease the use of Jinja templates to generate
queries, it supports direct queries, template queries, template queries
with Jinja formating, inside Jinja template you can use loops, conditionals
and define variables.
Jinja details go to: https://jinja.palletsprojects.com/en/3.1.x/
it must be used carefully to prevent SQLinjection.

Usage:
    conn = st.connection('snow', tye=SnowConnection)
    df1 = conn.query('select * from table')
    df2 = conn.query('select * from table wheer column1 = "{{name}}"',
                     params={'name': 'John'})
    df3 = conn.query_template('path/to/query.sql')
    df4 = conn.query_template('path/to/query.sql',
                              params={'name': 'John', 'last_name': 'Doe'})
"""

from streamlit import secrets, session_state, markdown, warning, stop
from typing import Optional


class Roles:
    admin_contact = secrets.get('admin_contact', '')
    no_acces = f'⛔ You don\'t have access to this page \
    contact your admin for more info {admin_contact}'

    def __init__(self, roles: list):
        self.roles = set(roles)
        self.roles.add('admin')

    # def __call__(self, func) -> Callable:
    #     if self.roles.intersection(session_state.roles):
    #         def wrapper(*args, **kwargs):
    #             return func(*args, **kwargs)
    #         return wrapper
    #     else:
    #         return lambda: toast(Roles.no_acces)

    @classmethod
    def allow_acces(cls, roles: Optional[list] = None):
        if 'dev' in session_state.get('roles', []):
            warning('Be carefull in development speace', icon='🤖')
        elif roles is None or 'admin' in session_state.get('roles', []):
            return
        elif not set(roles).intersection(session_state.get('roles', [])):
            markdown('#### ' + cls.no_acces)
            stop()
        return
