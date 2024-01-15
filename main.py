from flet import *
from flet_route import Routing, path, Params, Basket
import time as stallion
from pathlib import Path
import selectors
import json
import os
import socket
import secrets
import io
import sys
import struct


class BChat():

    def __init__(self, **kwargs):
        super(BChat, self).__init__(**kwargs)
        app(target=self.main,assets_dir='assets',view=WEB_BROWSER,port=55001,web_renderer="html")

    def main(self,page: Page):
        page.title = "Container"
        page.vertical_alignment = MainAxisAlignment.CENTER
        page.horizontal_alignment = CrossAxisAlignment.CENTER
        page.theme_mode = 'Light'
        BG = '#041955'
        FWG = '#97b4ff'
        FG = '#3450a1'
        PINK = '#eb06ff'

        #page.window_maximized = True
        page.update()
        app_routes = [

            path(url='/',clear=False,view=self.my_prof),
            path(url='/authen',clear=False,view=self.my_hom),
            path(url='/reception',clear=False,view=self.start_page),
            path(url='/payments',clear=False,view=self.payment_page),
            path(url='/school',clear=False,view=self.school_page),
        ]
        Routing(page=page,app_routes=app_routes)
        page.go(page.route)

    def my_prof(self, page: Page, params: Params, basket: Basket):
        def process_clicked(e):
            '''
            Login processor
            '''
            page.go('/authen')
        self.chrook = 0
        benn = Column(horizontal_alignment = CrossAxisAlignment.CENTER,spacing=30,)
        decry_pemkey = 'Failed.'
        benn.controls.append(Container(width=400,height=20,
            content=Column(controls=[
            ])))
        benn.controls.append(Row(width=400,height=30,alignment = MainAxisAlignment.CENTER,controls=[Text("Smart Login",size=20,text_align=TextAlign.CENTER,style=TextThemeStyle.HEADLINE_SMALL)]))
        bill = Row(width=400,height=40,alignment = MainAxisAlignment.CENTER)
        self.username = TextField(helper_text="Username", hint_text="", max_lines=1, max_length=40,border=InputBorder.UNDERLINE) # NONE, OUTLINE
        bill.controls.append(self.username)
        self.username.value = 'Hie'
        benn.controls.append(bill)
        bill = Row(width=400,height=40,alignment = MainAxisAlignment.CENTER)
        self.password = TextField(helper_text="Password", hint_text="", max_lines=1, max_length=400,border=InputBorder.UNDERLINE, password=True, can_reveal_password=True)
        bill.controls.append(self.password)
        benn.controls.append(bill)
        lien = Row(width=400,height=30,
            alignment=MainAxisAlignment.END,
        )
        self.confirm = TextButton("Confirm",scale=1.25,on_click=process_clicked) # page.go('/authen'))
        lien.controls.append(self.confirm)
        lien.controls.append(Container(width=40))
        benn.controls.append(lien)
        benn.controls.append(Row(width=400,height=30,alignment = MainAxisAlignment.CENTER,controls=[Icon(icons.COPYRIGHT_ROUNDED),Text(stallion.strftime("%Y", stallion.localtime()))]))
        self.login = Card(
            width=500,
            height=400,
            color=colors.WHITE70,
            content=Container(
                content=benn,
                width=400,
                padding=10,
            )
        )
        self.login_page = View(
            route='/',
            vertical_alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls=[
                self.login
            ]
        )
        return self.login_page

    def my_hom(self, page: Page, params: Params, basket: Basket):
        def item_clicked(e):
            page.go('/reception')
        def get_field_two(e):
            self.autkey2.focus()
        def get_field_three(e):
            self.autkey3.focus()
        benn = Column(horizontal_alignment = CrossAxisAlignment.CENTER,spacing=30,)
        benn.controls.append(Container(width=400,height=20))
        benn.controls.append(Row(width=400,height=30,alignment = MainAxisAlignment.CENTER,controls=[Text("Authentication",size=20,text_align=TextAlign.CENTER,style=TextThemeStyle.HEADLINE_SMALL)]))
        benn.controls.append(Container(width=400,height=30))
        bill = Row(width=400,height=40,alignment = MainAxisAlignment.CENTER)
        self.autkey1 = TextField(helper_text="", hint_text="", max_lines=1, max_length=3,border=InputBorder.UNDERLINE, width=36,on_submit=get_field_two)
        bill.controls.append(self.autkey1)
        bill.controls.append(Container(width=30))
        self.autkey2 = TextField(helper_text="", hint_text="", max_lines=1, max_length=3,border=InputBorder.UNDERLINE, width=36,on_submit=get_field_three)
        bill.controls.append(self.autkey2)
        bill.controls.append(Container(width=30))
        self.autkey3 = TextField(helper_text="", hint_text="", max_lines=1, max_length=3,border=InputBorder.UNDERLINE, width=36)
        bill.controls.append(self.autkey3)
        benn.controls.append(bill)
        lien = Row(width=400,height=30,
            alignment=MainAxisAlignment.END,
        )
        self.authenbutt = TextButton("Confirm",scale=1.25, on_click=item_clicked)
        lien.controls.append(self.authenbutt)
        lien.controls.append(Container(width=40))
        benn.controls.append(lien)
        benn.controls.append(Row(width=400,height=30,alignment = MainAxisAlignment.CENTER,controls=[Icon(icons.COPYRIGHT_ROUNDED),Text(stallion.strftime("%Y", stallion.localtime()))]))
        self.authen = Card(
            width=500,
            height=400,
            color=colors.WHITE70,
            content=Container(
                content=benn,
                width=400,
                padding=10,
            )
        )
        self.authen_page = View(
            route='/authen',
            vertical_alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls=[
                self.authen
            ]
        )
        return self.authen_page

    def start_page(self, page: Page, params: Params, basket: Basket):
        page.vertical_alignment = MainAxisAlignment.NONE
        page.horizontal_alignment = CrossAxisAlignment.NONE

        def check_item_clicked(e):
            page.go('/'+e.control.text.lower())

        self.appbar = AppBar(
            leading=Container(
                content=Icon(icons.ARROW_CIRCLE_LEFT, size=40, color='blue600'),
                #width = 40,
                #height= 40,
                #on_click=,
            ),
            leading_width=20,
            title=ListTile(
                title=Text("Sangfroid Digital Card",size=32,weight=FontWeight.BOLD, color='blue600'),
                selected=True,
            ),
            center_title=False,
            toolbar_height=60,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(
                            text="Account", on_click=check_item_clicked
                        ),
                        PopupMenuItem(
                            text="Transfer", on_click=check_item_clicked
                        ),
                        PopupMenuItem(
                            text="Payments", on_click=check_item_clicked
                        ),
                        PopupMenuItem(
                            text="Airtime", on_click=check_item_clicked
                        ),
                        PopupMenuItem(
                            text="Card Management", on_click=check_item_clicked
                        ),
                        PopupMenuItem(
                            text="Analytics", on_click=check_item_clicked
                        ),
                    ]
                ),
            ],
        )
        self.main_box = Column(
            expand=1,
            height=500,
            visible=True,
            spacing=10,
            controls=[
                Row(height=300,alignment = MainAxisAlignment.CENTER,controls=[Container(
                    image_src=Path(__file__).joinpath("../assets").resolve().joinpath("user.png"),
                    image_fit=ImageFit.FILL,
                    width = 300,
                    border_radius=150,)]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Welcome',size=20,weight=FontWeight.BOLD,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Hwizah Timothy',size=24,italic=True,weight=FontWeight.BOLD,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Account ID:',italic=True,size=24,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('222222234588229944',size=20,weight=FontWeight.BOLD,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Academic Institute:',italic=True,size=24,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('University of Zimbabwe',size=20,weight=FontWeight.BOLD,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Student Classifier:',italic=True,size=24,color='blue600'),]),
                Row(height=30,alignment = MainAxisAlignment.CENTER,controls=[Text('Alumni',size=20,weight=FontWeight.BOLD,color='blue600'),]),
            ]
        )
        self.boris = Row(height=40,spacing=30,alignment = MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)
        self.homekey = Container(height=40,width=40,content=Icon(icons.HOME,color=colors.BLUE_800,tooltip="Home Page"))
        self.boris.controls.append(self.homekey)
        self.feedkey = Container(height=40,width=40,content=Icon(icons.FEEDBACK,color=colors.BLUE_800,tooltip="Give your Feedback"))
        self.boris.controls.append(self.feedkey)
        self.helpkey = Container(height=40,width=40,content=Icon(icons.HELP,color=colors.BLUE_800,tooltip="Get Help"))
        self.boris.controls.append(self.helpkey)
        self.mabena = BottomAppBar(
            bgcolor=colors.SURFACE_VARIANT,
            surface_tint_color=colors.BLUE_100,
            content= self.boris,
            height=60,
        )
        for i in range(0,60):
            berl = Container(
                border_radius=20,
                width = 100,
                padding = padding.only(top=0,bottom=20,right=10,left=10),
                content= Column(
                ),
            )
            self.main_box.controls.append(berl)
        self.reception_page = View(
            route='/reception',
            vertical_alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            scroll=ScrollMode.AUTO,
            controls=[
                self.appbar,
                Card(
                    #width=500,
                    height=650,
                    #color=colors.WHITE70,
                    content=Container(
                        content=self.main_box,
                        #width=400,
                        padding=10,
                    ),
                ),
                self.mabena,
            ]
        )
        return self.reception_page

    def payment_page(self, page: Page, params: Params, basket: Basket):
        page.vertical_alignment = MainAxisAlignment.NONE
        page.horizontal_alignment = CrossAxisAlignment.NONE

        def go_paging(e):
            page.go('/'+e.control.text.lower().replace(' ',''))

        def go_somewhere(e):
            page.go('/school')

        def check_item_clicked(e):
            self.payments_page.drawer.open = True
            self.payments_page.drawer.update()

        self.appbar = AppBar(
            leading=Container(
            image_src=Path(__file__).joinpath("../assets").resolve().joinpath("user.png"),
            image_fit=ImageFit.FILL,
            #width = 40,
            border_radius=30,
            #height= 40,
            on_click=check_item_clicked,
        ),
            leading_width=60,
            title=ListTile(
                title=Text("Hwizah Timothy",size=12,weight=FontWeight.BOLD),
                subtitle=Text("Tertiary",size=12),
                selected=True,
            ),
            center_title=False,
            toolbar_height=60,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(
                            text="UZ", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="HIT", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="GZU", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="Hre Poly", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="MSU", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="Msv Poly", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="Belv College", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="CUT", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="AU", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="ZOU", on_click=go_paging
                        ),
                        PopupMenuItem(
                            text="BUSE", on_click=go_paging
                        ),
                    ]
                ),
            ],
        )
        self.main_box = Column(
            expand=1,
            visible=True,
            spacing=10,
        )
        self.boris = Row(height=40,spacing=30,alignment = MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)
        self.homekey = Container(height=40,width=40,content=Icon(icons.HOME,color=colors.BLUE_800,tooltip="Home Page"))
        self.boris.controls.append(self.homekey)
        self.feedkey = Container(height=40,width=40,content=Icon(icons.FEEDBACK,color=colors.BLUE_800,tooltip="Give your Feedback"))
        self.boris.controls.append(self.feedkey)
        self.helpkey = Container(height=40,width=40,content=Icon(icons.HELP,color=colors.BLUE_800,tooltip="Get Help"))
        self.boris.controls.append(self.helpkey)
        self.mabena = BottomAppBar(
            bgcolor=colors.SURFACE_VARIANT,
            surface_tint_color=colors.BLUE_100,
            content= self.boris,
            height=60,
        )
        self.payments_page = View(
            route='/payments',
            vertical_alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls=[
                self.appbar,
                Container(
                    content=self.main_box,
                ),
                self.mabena,
            ],
            scroll= ScrollMode.AUTO,
        )
        self.payments_page.drawer = NavigationDrawer(
            elevation=40,
            indicator_color=colors.BLUE_200,
            indicator_shape=StadiumBorder(),
            shadow_color=colors.BLUE_900,
            surface_tint_color=colors.BLUE,
            #bgcolor=colors.BLUE,
            selected_index=-1,
            controls=[
                Container(height=12),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 100,
                    controls = [
                        Container(
                            image_src=Path(__file__).joinpath("../assets").resolve().joinpath("user.png"),
                            image_fit=ImageFit.FILL,
                            width = 100,
                            border_radius=50,
                            height= 100,
                        ),
                    ],
                ),
                Divider(thickness=2),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 30,
                    controls = [
                        Container(
                            content=Text('Tertiary',size=20,),
                            width = 150,
                            border_radius=7,
                            height= 30,
                        ),
                    ],
                ),
                Container(height=15),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 30,
                    controls = [
                        Container(
                            content=Text('School',size=20,),
                            width = 150,
                            border_radius=7,
                            height= 30,
                            on_click=go_somewhere,
                        ),
                    ],
                ),
            ],
        )
        return self.payments_page

    def school_page(self, page: Page, params: Params, basket: Basket):
        page.vertical_alignment = MainAxisAlignment.NONE
        page.horizontal_alignment = CrossAxisAlignment.NONE

        def check_item_clicked(e):
            self.school_page.drawer.open = True
            self.school_page.drawer.update()

        def go_somewhere(e):
            page.go('/payments')

        self.appbar = AppBar(
            leading=Container(
            image_src=Path(__file__).joinpath("../assets").resolve().joinpath("user.png"),
            image_fit=ImageFit.FILL,
            #width = 40,
            border_radius=30,
            #height= 40,
            on_click=check_item_clicked,
        ),
            leading_width=60,
            title=ListTile(
                title=Text("Hwizah Timothy",size=12,weight=FontWeight.BOLD),
                subtitle=Text("School",size=12),
                selected=True,
            ),
            center_title=False,
            toolbar_height=60,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
            ],
        )
        self.main_box = Column(
            expand=1,
            visible=True,
            spacing=10,
        )
        self.boris = Row(height=40,spacing=30,alignment = MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)
        self.homekey = Container(height=40,width=40,content=Icon(icons.HOME,color=colors.BLUE_800,tooltip="Home Page"))
        self.boris.controls.append(self.homekey)
        self.feedkey = Container(height=40,width=40,content=Icon(icons.FEEDBACK,color=colors.BLUE_800,tooltip="Give your Feedback"))
        self.boris.controls.append(self.feedkey)
        self.helpkey = Container(height=40,width=40,content=Icon(icons.HELP,color=colors.BLUE_800,tooltip="Get Help"))
        self.boris.controls.append(self.helpkey)
        self.mabena = BottomAppBar(
            bgcolor=colors.SURFACE_VARIANT,
            surface_tint_color=colors.BLUE_100,
            content= self.boris,
            height=60,
        )
        self.school_page = View(
            route='/school',
            vertical_alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls=[
                self.appbar,
                Container(
                    content=self.main_box,
                ),
                self.mabena,
            ],
            scroll= ScrollMode.AUTO,
        )
        self.school_page.drawer = NavigationDrawer(
            elevation=40,
            indicator_color=colors.BLUE_200,
            indicator_shape=StadiumBorder(),
            shadow_color=colors.BLUE_900,
            #bgcolor=colors.BLUE,
            surface_tint_color=colors.BLUE,
            selected_index=-1,
            controls=[
                Container(height=12),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 100,
                    controls = [
                        Container(
                            image_src=Path(__file__).joinpath("../assets").resolve().joinpath("user.png"),
                            image_fit=ImageFit.FILL,
                            width = 100,
                            border_radius=50,
                            height= 100,
                        ),
                    ],
                ),
                Divider(thickness=2),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 30,
                    controls = [
                        Container(
                            content=Text('Tertiary',size=20,),
                            width = 150,
                            border_radius=7,
                            height= 30,
                            on_click=go_somewhere,
                        ),
                    ],
                ),
                Container(height=15),
                Row(
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    height = 30,
                    controls = [
                        Container(
                            content=Text('School',size=20,),
                            width = 150,
                            border_radius=7,
                            height= 30,
                        ),
                    ],
                ),
            ],
        )
        return self.school_page

    def chatbox(self):
        lotus = Column(expand=True,col=1)
        berl = Container(
            width=500,
            bgcolor=colors.BLUE,
            content=lotus,
            alignment=CrossAxisAlignment.END
        )
        self.add_widget(lotus,Text('This is awesome'))
        self.add_widget(self.main_box,berl)

    def add_widget(self,parent,child):
        parent.controls.append(child)
        #page.update()

    def remove_widget(self,parent,child):
        parent.controls.remove(child)

BChat()