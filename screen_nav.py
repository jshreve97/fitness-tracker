# second file is imported to main file to keep code clean
# screen manager allows for multiple screens to be used
# < > creates individual screen

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    ChestScreen:
    ArmsScreen:
    ShouldersScreen:
    BackScreen:
    LegsScreen:
    AbsScreen:
    ChestData:
    ArmsData:
    ShouldersData:
    BackData:
    LegsData:
    AbsData:

    

           
<ChestData>:
    name: 'chestdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'chest'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"

<ArmsData>:
    name: 'armsdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'arms'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
        
<ShouldersData>:
    name: 'shouldersdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'shoulders'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
        
<BackData>:
    name: 'backdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'back'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"

<LegsData>:
    name: 'legsdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'legs'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
        
<AbsData>:
    name: 'absdata'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.4,'center_y':0.075}
        on_press: root.manager.current = 'abs'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.6,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"





<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'Time to workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.65}
        font_style: 'H4'



    MDBottomAppBar:

        MDTopAppBar:
            title: ""
            icon: "arm-flex-outline"
            type: "bottom"
            on_action_button: root.manager.current = 'profile'
        
    
 

    

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Choose a body part'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDBottomAppBar:

        MDTopAppBar:
            title: ""
            icon: "home"
            type: "bottom"
            on_action_button: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Chest'
        pos_hint: {'center_x':0.5,'center_y':0.700}
        on_press: root.manager.current = 'chest'
        size_hint: (0.4,0.05)
    MDRectangleFlatButton:
        text: 'Arms'
        pos_hint: {'center_x':0.5,'center_y':0.625}
        on_press: root.manager.current = 'arms'
        size_hint: (0.4,0.05)
    MDRectangleFlatButton:
        text: 'Shoulders'
        pos_hint: {'center_x':0.5,'center_y':0.550}
        on_press: root.manager.current = 'shoulders'
        size_hint: (0.4,0.05)
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.475}
        on_press: root.manager.current = 'back'
        size_hint: (0.4,0.05)
    MDRectangleFlatButton:
        text: 'Legs'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'legs'
        size_hint: (0.4,0.05)
    MDRectangleFlatButton:
        text: 'Abs'
        pos_hint: {'center_x':0.5,'center_y':0.325}
        on_press: root.manager.current = 'abs'
        size_hint: (0.4,0.05)


<ChestScreen>:
    name: 'chest'
    MDLabel:
        text: 'Choose a workout to UPDATE'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDLabel:
        text: 'Sets/Reps/Weight'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.9}  
        size_hint: (0.5,0.05)
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'chestdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: bbpress
        hint_text: 'Update Barbell Press'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: dbpress
        hint_text: 'Update Dumbbell Press'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: chestflys
        hint_text: 'chestflys'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: dips
        hint_text: 'Update dips'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_chest()

        
  

<ArmsScreen>:
    name: 'arms'
    MDLabel:
        text: 'Choose an ARM workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}  
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'armsdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: bbcurl
        hint_text: 'Update Barbell Curl'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: dbcurl
        hint_text: 'Update Dumbbell Curl'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: preachercurls
        hint_text: 'Update Preacher Curls'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: hammercurls
        hint_text: 'Update Hammer Curls'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_arms()



<ShouldersScreen>:
    name: 'shoulders'
    MDLabel:
        text: 'Choose a SHOULDER workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'shouldersdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: shoulderpress
        hint_text: 'Update shoulder press'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: lateralraise
        hint_text: 'Update lateral raise'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: reardeltflys
        hint_text: 'Update rear delt flys'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: frontraises
        hint_text: 'Update Front raise'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_shoulders()



<BackScreen>:
    name: 'back'
    MDLabel:
        text: 'Choose a BACK workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'backdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: pullups
        hint_text: 'Update pullups'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: deadlifts
        hint_text: 'Update deadlifts'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: cablerows
        hint_text: 'Update cable rows'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: latpulldown
        hint_text: 'Update lat pull down'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_back()  



<LegsScreen>:
    name: 'legs'
    MDLabel:
        text: 'Choose a LEG workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'legsdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: squats
        hint_text: 'Update squats'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: rdls
        hint_text: 'Update rdls'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: lunges
        hint_text: 'Update lunges'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: hipthrust
        hint_text: 'Update hip thrust'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_legs() 
     


<AbsScreen>:
    name: 'abs'
    MDLabel:
        text: 'Choose an AB workout'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.950}
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'profile'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.075}
        on_press: root.manager.current = 'menu'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDIconButton:
        icon: 'calculator'
        pos_hint: {'center_x':0.8,'center_y':0.075}
        on_press: root.manager.current = 'absdata'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
    MDTextField:
        id: planks
        hint_text: 'Update planks'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: legraises
        hint_text: 'Update leg raises'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: russiantwist
        hint_text: 'Update russian twists'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
        multiline: False
    MDTextField:
        id: crunches
        hint_text: 'Update crunches'
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:200
        multiline: False
    MDRectangleFlatButton:
        text: 'Update'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: (0.4,0.05)
        on_release: app.on_enter_abs() """
