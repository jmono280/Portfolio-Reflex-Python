import reflex as rx
from portafolio.styles.styles import EmSize, Size
from portafolio.views.skills import skills
from portafolio import data


data = [
    {
        "subject": "Php",
        "A": 120,
        "fullMark": 100,
    },
    {
        "subject": "JS",
        "A": 98,
        "fullMark": 100,
    },
    {
        "subject": "Json",
        "A": 86,
        "fullMark": 100,
    },
    {
        "subject": "Python",
        "A": 99,
        "fullMark": 100,
    },
    {
        "subject": "Mysql",
        "A": 85,
        "fullMark": 100,
    },
    {
        "subject": "Java",
        "A": 65,
        "fullMark": 100,
    },
]


def radar_start_end() -> rx.Component:
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            dot=True,
            stroke="#8884d8",
            fill="#8884d8",
            fill_opacity=0.6,
            legend_type="line",
            animation_begin=0,
            animation_duration=8000,
            animation_easing="ease-in",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(angle=90, domain=[0, 100]),
        rx.recharts.legend(),
        data=data,
        width=200,
        height=200,
    )
