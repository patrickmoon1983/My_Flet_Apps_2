import datetime

import flet
import requests
from flet import *

API_key = '8dd96e2ae1fe585f16864b32dae6eee3'
lat = 43.6534817
lon = -79.3839347
part = 'daily'

city_name = 'Moscow'

_current = requests.get(f'https://api.weatherapi.com/v1/current.json?key=527252564787419c94e153304242609&q={city_name}')
icon_name = ''

days = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun'
]


def main(page: Page):
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 700
    page.theme_mode = ThemeMode.LIGHT

    def _expand(e):
        if e.data == 'true':
            _c.content.controls[1].height = 600
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.40
            _c.content.controls[1].update()

    def _current_temp():
        try:
            _current_temp = round(_current.json()['current']['temp_c'])
            _current_weather = _current.json()['current']['condition']['text']
            _current_description = _current.json()['current']['condition']['text']
            _current_wind = round(_current.json()['current']['wind_kph'])
            _current_humidity = round(_current.json()['current']['humidity'])
            _current_feels = round(_current.json()['current']['feelslike_c'])
            _current_icon = _current.json()['current']['condition']['icon']
            return [
                _current_temp,
                _current_weather,
                _current_description,
                _current_wind,
                _current_humidity,
                _current_feels,
                _current_icon
            ]
        except:
            pass

    def _current_extra():

        _extra_info = []

        _extra = [
            [
                round(_current.json()['current']['condition']['code'] / 1000),
                'km',
                'visibility',
                'https://cdn-icons-png.freepik.com/256/531/531708.png?ga=GA1.1.1967550842.1730282326&semt=ais_hybrid'
            ],
            [
                round(_current.json()['current']['pressure_mb'] * 0.001, 2),
                'bar',
                'Pressure',
                'https://cdn-icons-png.freepik.com/256/4117/4117400.png?ga=GA1.1.1967550842.1730282326&semt=ais_hybrid'
            ],
            [
                '18:00',
                'PM',
                'Sunset',
                'https://cdn-icons-png.freepik.com/256/3266/3266245.png?ga=GA1.1.1967550842.1730282326'
            ],
            [
                '06:00',
                'AM',
                'Sunrise',
                'https://cdn-icons-png.freepik.com/256/1582/1582750.png?ga=GA1.1.1967550842.1730282326&semt=ais_hybrid'
            ],

        ]

        for data in _extra:
            _extra_info.append(
                Container(
                    bgcolor=Colors.WHITE10,
                    border_radius=12,
                    alignment=alignment.center,
                    content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Image(
                                    src=data[3],
                                    # color=Colors.WHITE,
                                ),
                                width=32,
                                height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    spacing=0,
                                    controls=[
                                        Text(
                                            str(data[0]) + ' ' + data[1],
                                            size=14,
                                            color=Colors.WHITE,
                                        ),
                                        Text(
                                            data[2],
                                            size=11,
                                            color=Colors.WHITE54,
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
        return _extra_info

        pass

    def _top():
        _today = _current_temp()
        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in _current_extra():
            _today_extra.controls.append(info)
        print(_today)
        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600', 'lightblue900']
            ),
            border_radius=35,
            animate=animation.Animation(450, AnimationCurve.DECELERATE),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment=MainAxisAlignment.START,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value='Toronto. CA',
                                 size=16,
                                 weight=FontWeight.W_500,
                                 color=Colors.WHITE)
                        ]
                    ),
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src=f'https:{_today[6]}'

                                    )
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(value='Today',
                                         size=12,
                                         text_align=TextAlign.CENTER,
                                         color=Colors.WHITE),
                                    Row(
                                        vertical_alignment=CrossAxisAlignment.START,
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Row([
                                                    Text(
                                                        _today[0],
                                                        size=52,
                                                    ),
                                                    Text(
                                                        value='°',
                                                        size=40
                                                    )
                                                ],
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN)

                                            ),

                                        ]
                                    ),
                                    Text(
                                        _today[1] + '\n- Overcast',
                                        size=10,
                                        color=Colors.WHITE54,
                                        text_align=TextAlign.CENTER,
                                    ),
                                    Column(
                                        spacing=5,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Text(value=f'Localtime :',
                                                 size=11,
                                                 text_align=TextAlign.CENTER,
                                                 color=Colors.WHITE54),
                                            Text(
                                                value=str(''.join(list(_current.json()["location"]["localtime"])[11:])),
                                                size=14,
                                                text_align=TextAlign.CENTER,
                                                color=Colors.WHITE),
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    Divider(height=8,
                            thickness=1,
                            color=Colors.WHITE10),
                    Row(
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    spacing=2,
                                    controls=[
                                        Container(
                                            width=35,
                                            height=35,
                                            image_src='https://cdn-icons-png.freepik.com/256/4662/4662681.png?uid'
                                                      '=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid',
                                            alignment=alignment.center,

                                        ),
                                        Text(
                                            value=f'{_today[3]} km/h',
                                            size=11,
                                        ),
                                        Text(
                                            value='Wind',
                                            size=9,
                                            color=Colors.WHITE54
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    spacing=2,
                                    controls=[
                                        Container(
                                            width=35,
                                            height=35,
                                            image_src='https://cdn-icons-png.freepik.com/256/9047/9047829.png?uid'
                                                      '=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid',
                                            alignment=alignment.center,
                                        ),
                                        Text(
                                            value=f'{_today[4]} %',
                                            size=11,
                                        ),
                                        Text(
                                            value='Humidity',
                                            size=9,
                                            color=Colors.WHITE54
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    spacing=2,
                                    controls=[
                                        Container(
                                            width=35,
                                            height=35,
                                            image_src='https://cdn-icons-png.freepik.com/256/4963/4963155.png?'
                                                      'ga=GA1.1.1967550842.1730282326&semt=ais_hybrid',
                                            alignment=alignment.center,
                                        ),
                                        Text(
                                            value=f'{_today[5]} ° ',
                                            size=11,
                                        ),
                                        Text(
                                            value='Feels like',
                                            size=9,
                                            color=Colors.WHITE54
                                        )
                                    ]
                                )
                            ),

                        ]
                    ),
                    _today_extra,
                ]
            )
        )
        return top

    def _bot_data():
        try:
            _bot_data = []
            for index in range(1, 8):
                _bot_data.append(
                    Row(
                        spacing=5,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                expand=1,
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        content=Text(
                                            days[
                                                datetime.datetime.weekday(
                                                    datetime.datetime.fromtimestamp(
                                                        _current.json()['location']['localtime_epoch']
                                                    )
                                                )
                                            ],
                                            color=Colors.WHITE
                                        )
                                    )
                                ]
                            ),
                            Row(
                                expand=1,
                                controls=[
                                    Container(
                                        content=Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                Container(
                                                    width=20,
                                                    height=20,
                                                    alignment=alignment.center_left,
                                                    content=Image(
                                                        src=f'https:{_current.json()["current"]["condition"]["icon"]}'
                                                    )
                                                ),
                                                Text(
                                                    _current.json()['current']['condition']['text'][:9],
                                                    size=11,
                                                    color=Colors.WHITE54,
                                                    text_align=TextAlign.CENTER
                                                )
                                            ],
                                        )

                                    )
                                ]

                            ),
                            Row(
                                expand=1,
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        content=Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=5,
                                            controls=[
                                                Container(
                                                    width=20,
                                                    content=Text(
                                                        round(_current.json()['current']['temp_c']),
                                                        color=Colors.WHITE,
                                                        size=11,
                                                        text_align=TextAlign.START
                                                    )
                                                ),
                                                Container(
                                                    width=20,
                                                    content=Text(
                                                        -round(_current.json()['current']['temp_c']),
                                                        color=Colors.WHITE,
                                                        size=11,
                                                        text_align=TextAlign.END
                                                    )
                                                ),
                                            ]
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                )
            return _bot_data
        except:
            pass

    def _bottom():
        try:
            _bot_column = Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=25
            )
            for data in _bot_data():
                _bot_column.controls.append(data)

            bottom = Container(
                padding=padding.only(top=280,
                                     left=20,
                                     right=20,
                                     bottom=20),
                content=_bot_column,
            )
            return bottom
        except:
            pass

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor=Colors.BLACK,
        padding=10,
        content=Stack(
            width=210,
            height=550,
            controls=[
                _bottom(),
                _top()
            ]
        )

    )
    page.add(_c)


if __name__ == '__main__':
    flet.app(target=main)
