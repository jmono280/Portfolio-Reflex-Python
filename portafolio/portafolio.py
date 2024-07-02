import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.skills import skills
from portafolio.views.lang import lang
from portafolio.views.tech_stack import tech_stack
from portafolio.views.chart import radar_start_end

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.hstack(
            rx.vstack(
                rx.box(
                    rx.card(skills(DATA.skills)),
                    spacing="4",
                ),
                rx.box(
                    rx.card(lang(DATA.lang)),
                    spacing="4",
                ),
                width="20%",
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.BIG.value,
            ),
            rx.vstack(
                header(DATA),
                about(DATA.about),
                rx.divider(),
                tech_stack(DATA.technologies),
                info("Experiencia", DATA.experience),
                # info("Proyectos", DATA.projects),
                info("Formación", DATA.training),
                extra(DATA.extras),
                rx.divider(),
                footer(DATA.media),
                spacing=Size.DEFAULT.value,
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.BIG.value,
                width="80%",
            ),
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", radius="medium", accentColor="bronze", grayColor="slate"
    ),
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
)
app.add_page(index)
