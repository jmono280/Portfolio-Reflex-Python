import reflex as rx
from portafolio.components.heading import heading


def about(description: str) -> rx.Component:
    return rx.vstack(heading("About"), rx.text(description))
