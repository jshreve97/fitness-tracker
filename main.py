from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav import screen_helper
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout

# opens window in mobile screen size
Window.size = (300, 500)


# creating Screen classes
class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class ChestScreen(Screen):
    pass


class ArmsScreen(Screen):
    pass


class ShouldersScreen(Screen):
    pass


class BackScreen(Screen):
    pass


class LegsScreen(Screen):
    pass


class AbsScreen(Screen):
    pass


class DemoScreen(Screen):
    pass


# lists to hold exercise data

chest_data = ['', '', '', '']
arms_data = ['', '', '', '']
shoulders_data = ['', '', '', '']
legs_data = ['', '', '', '']
back_data = ['', '', '', '']
abs_data = ['', '', '', '']


# creating a class that loads data tables for each exercise
class ChestData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Barbell Press", dp(45)),
                ("Dumbbell Press", dp(45)),
                ("Chest Flys", dp(45)),
                ("Dips", dp(45)), ],
            row_data=[
                chest_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class ArmsData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Barbell Curl", dp(45)),
                ("Dumbbell Curl", dp(45)),
                ("Preacher Curl", dp(45)),
                ("Hammer Curl", dp(45)), ],
            row_data=[
                arms_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class ShouldersData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Shoulder press", dp(45)),
                ("Lateral Raises", dp(45)),
                ("rear delt flys", dp(45)),
                ("front raise", dp(45)), ],
            row_data=[
                shoulders_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class BackData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Pull-ups", dp(45)),
                ("Deadlift", dp(45)),
                ("Cable rows", dp(45)),
                ("Lat Pulldown", dp(45)), ],
            row_data=[
                back_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class LegsData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Squats", dp(45)),
                ("RDLs", dp(45)),
                ("Lunges", dp(45)),
                ("Hip Thrust", dp(45)), ],
            row_data=[
                legs_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class AbsData(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Planks", dp(45)),
                ("leg raises", dp(45)),
                ("russian twist", dp(45)),
                ("crunches", dp(45)), ],
            row_data=[
                abs_data
            ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


# adding widgets to the screen
sm = ScreenManager()
sm.add_widget(MenuScreen(name='workout'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ChestScreen(name='chest'))
sm.add_widget(ArmsScreen(name='arms'))
sm.add_widget(ShouldersScreen(name='shoulders'))
sm.add_widget(BackScreen(name='back'))
sm.add_widget(LegsScreen(name='legs'))
sm.add_widget(AbsScreen(name='abs'))
sm.add_widget(ChestData(name='chestdata'))
sm.add_widget(ArmsData(name='armsdata'))
sm.add_widget(ShouldersData(name='shouldersdata'))
sm.add_widget(BackData(name='backdata'))
sm.add_widget(LegsData(name='legsdata'))
sm.add_widget(AbsData(name='absdata'))


# building the app
class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Light'
        self.screen = Builder.load_string(screen_helper)

        return self.screen

    # on_enter updates the data to tables
    def on_enter_chest(self):
        bbpress = self.root.get_screen('chest').ids.bbpress.text
        dbpress = self.root.get_screen('chest').ids.dbpress.text
        chestflys = self.root.get_screen('chest').ids.chestflys.text
        dips = self.root.get_screen('chest').ids.dips.text

        chest_data[0] = bbpress
        chest_data[1] = dbpress
        chest_data[2] = chestflys
        chest_data[3] = dips

    def on_enter_arms(self):
        bbcurl = self.root.get_screen('arms').ids.bbcurl.text
        dbcurl = self.root.get_screen('arms').ids.dbcurl.text
        preachercurls = self.root.get_screen('arms').ids.preachercurls.text
        hammercurls = self.root.get_screen('arms').ids.hammercurls.text

        arms_data[0] = bbcurl
        arms_data[1] = dbcurl
        arms_data[2] = preachercurls
        arms_data[3] = hammercurls

    def on_enter_shoulders(self):
        shoulderpress = self.root.get_screen('shoulders').ids.shoulderpress.text
        lateralraise = self.root.get_screen('shoulders').ids.lateralraise.text
        reardeltflys = self.root.get_screen('shoulders').ids.reardeltflys.text
        frontraise = self.root.get_screen('shoulders').ids.frontraises.text

        shoulders_data[0] = shoulderpress
        shoulders_data[1] = lateralraise
        shoulders_data[2] = reardeltflys
        shoulders_data[3] = frontraise

    def on_enter_back(self):
        pullups = self.root.get_screen('back').ids.pullups.text
        deadlifts = self.root.get_screen('back').ids.deadlifts.text
        cablerow = self.root.get_screen('back').ids.cablerows.text
        latpulldown = self.root.get_screen('back').ids.latpulldown.text

        back_data[0] = pullups
        back_data[1] = deadlifts
        back_data[2] = cablerow
        back_data[3] = latpulldown

    def on_enter_legs(self):
        squats = self.root.get_screen('legs').ids.squats.text
        rdls = self.root.get_screen('legs').ids.rdls.text
        lunges = self.root.get_screen('legs').ids.lunges.text
        hipthrust = self.root.get_screen('legs').ids.hipthrust.text

        legs_data[0] = squats
        legs_data[1] = rdls
        legs_data[2] = lunges
        legs_data[3] = hipthrust

    def on_enter_abs(self):
        planks = self.root.get_screen('abs').ids.planks.text
        legraises = self.root.get_screen('abs').ids.legraises.text
        russiantwist = self.root.get_screen('abs').ids.russiantwist.text
        crunches = self.root.get_screen('abs').ids.crunches.text

        abs_data[0] = planks
        abs_data[1] = legraises
        abs_data[2] = russiantwist
        abs_data[3] = crunches


# runs the app
DemoApp().run()
