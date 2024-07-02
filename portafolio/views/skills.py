import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Skills
from portafolio.styles.styles import EmSize, Size


def skills(skill: list[Skills]) -> rx.Component:
    return rx.vstack(
        rx.mobile_only(),
        rx.tablet_and_desktop(
            heading("Skills"),
            rx.flex(
                *[
                    rx.badge(
                        rx.box(class_name=skill.icon, font_size="20px"),
                        rx.text(skill.name),
                        rx.text(": "),
                        rx.text(skill.percentage),
                        size="2",
                    )
                    for skill in skill
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            ),
            spacing=Size.DEFAULT.value,
        ),
    )
