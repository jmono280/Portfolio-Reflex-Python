import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Language
from portafolio.styles.styles import EmSize, Size


def lang(lang: list[Language]) -> rx.Component:
    return rx.vstack(
        rx.mobile_only(),
        rx.tablet_and_desktop(
            heading("Idiomas"),
            rx.flex(
                *[
                    rx.badge(
                        rx.text(lng.name),
                        rx.text(": "),
                        rx.text(lng.percentage),
                        size="2",
                    )
                    for lng in lang
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            ),
            spacing=Size.DEFAULT.value,
        ),
    )
