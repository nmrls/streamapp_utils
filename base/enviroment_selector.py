from streamlit import (
    session_state, secrets, container, image, columns, selectbox, button
)
from .utils import page_selector


class EnviromentSelector:
    enviroments = dict(secrets.enviromentselector)

    def __init__(self):
        session_state.enviroment = session_state.get(
            'enviroment',
            list(self.enviroments.keys())[0]
        )
        col1, col2 = container().columns([3, 1])
        col1.selectbox(
            'Enviroment Select',
            self.enviroments.keys(),
            key='EnviromentSelect',
            placeholder='Select Enviroment',
            on_change=self.change_enviroment(),
            label_visibility='collapsed',
            index=list(self.enviroments.keys()).index(
                session_state.get(
                    'EnviromentSelect',
                    list(self.enviroments.keys())[0]
                )
            )
        )
        with col2:
            self.show_image()
        return

    @staticmethod
    def change_enviroment():
        session_state.enviroment = session_state.get(
            'EnviromentSelect'
        )

    @staticmethod
    def set_options(key, option):
        session_state[key] = option

    @classmethod
    def show_image(cls, width: int = 40):
        if session_state.enviroment is not None:
            return image(
                cls.enviroments.get(session_state.enviroment, ''),
                width=width
            )
        return

    @classmethod
    def change_options(cls, key: str, page_options: dict,
                       include_pages: bool = False,
                       place_holder: str = 'Expander'):
        col1, col2 = columns([7, 1])
        with col1.expander(place_holder, expanded=False):
            selectbox(
                'Options',
                key=f'{key}_selected',
                options=page_options.keys(),
                label_visibility='hidden',
                placeholder=place_holder
            )
            button(
                'Select Option',
                on_click=cls.set_options,
                kwargs={
                    'key': key,
                    'option': session_state.get(f'{key}_selected')
                },
                type='primary'
            )
        with col2:
            cls.show_image()

        if include_pages:
            page_selector(session_state, key, page_options)
