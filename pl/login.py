import webbrowser
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from customtkinter import *



from bll.blconselor import ConselorService
from bll.blvisitor import VisitorService
from bll.bladmin import AdminService

from be.visitor import conselor
from be.visitor import visitor
from be.admin import admin


class App(Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.Crearewidget()

    def Crearewidget(self):
        style = ttk.Style()
        style.theme_use("vista")


        # pictures
        self.IconHmoe= PhotoImage(file="pl/form/home2.png")
        self.IconEdit= PhotoImage(file="pl/form/edit.png")
        self.Icondelete= PhotoImage(file="pl/form/delete.png")
        self.Iconsetting= PhotoImage(file="pl/form/setting.png")
        self.IconConselor= PhotoImage(file="pl/form/doctor.png")
        self.IconClose= PhotoImage(file="pl/form/close.png")
        self.player_1=PhotoImage(file="pl/form/mngg.png")
        self.player_2 = PhotoImage(file="pl/form/lbll.png")
        self.player_3=PhotoImage(file="pl/form/lbll.png")
        self.bime1=PhotoImage(file="pl/form/niro.png")
        self.bime2=PhotoImage(file="pl/form/melat.png")
        self.bime3=PhotoImage(file="pl/form/salamat.png")
        self.bime4=PhotoImage(file="pl/form/pasargad.png")
        self.bime5=PhotoImage(file="pl/form/dana.png")



        self.layer_1=Frame(self.master,width=875,height=750,background="white")
        self.layer_1.place(x=0,y=0)
        self.lblimage1=Label(self.layer_1,image=self.player_1)
        self.lblimage1.place(x=0,y=0)



        #first page
        self.lblname=Label(self.layer_1,text=" مرکز مشاوره \n حس خوب",font="Calibri 40 bold")
        self.lblname.config(bg="#fdfce0")
        self.lblname.place(x=320, y=150)

        self.lblvsitor =Button(self.layer_1, text="مراجعین ",font="Calibri 30 bold",command=self.open_manager_page)
        self.lblvsitor.config(padx=50,pady=40,bg="#1c0275",fg="white")
        self.lblvsitor.place(x=150, y=400)

        self.lblconselor =Button(self.layer_1, text= "مشاوران",font="Calibri 30 bold",command=self.open_conselor_page)
        self.lblconselor.config(padx=50,pady=40,bg="#1c0275",fg="white")
        self.lblconselor.place(x=500, y=400)

        #settingFrame
        self.btn_setting=Button(self.layer_1,image=self.Iconsetting,command=self.ShowSetting)
        self.btn_setting.config(bg="#fdfce0")
        self.btn_setting.place(x=40,y=40)
        self.frm_setting=CTkFrame(self.layer_1,width=875,height=750)
        self.frm_setting.place(x=0,y=0)
        self.frm_setting.place_forget()
        self.imageSetting=Label(self.frm_setting, image=self.player_2)
        self.imageSetting.place(x=0,y=0)

        self.lbl_cons_title_name = Label(self.frm_setting, text="تنظیمات", font="calibri 20 bold")
        self.lbl_cons_title_name.config(bg="#fdfce0")
        self.lbl_cons_title_name.place(x=400, y=60)

        self.btn_home_setting = Button(self.frm_setting, image=self.IconHmoe,command=self.open_login_page_of_SettingPage)
        self.btn_home_setting.config( bg="#fdfce0")
        self.btn_home_setting.place(x=100, y=60)


#mainframeCons
        self.Conslayer = Frame(self.layer_1, width=875,height=750)
        self.Conslayer.place(x=0, y=0)
        self.Conslayer.place_forget()
        self.lblimage1 = Label(self.Conslayer, image=self.player_2)
        self.lblimage1.place(x=0, y=0)

        #conselorButton
        self.lbl_cons_title_name = Label(self.Conslayer, text="مشاوران", font="calibri 20 bold")
        self.lbl_cons_title_name.config(bg="#fdfce0")
        self.lbl_cons_title_name.place(x=400, y=60)

        self.btn_cons_sign = Button(self.Conslayer, text="ثبت مشاور \n جدید", font="Calibri 20 bold",command=self.onclick_show_cons_sign)
        self.btn_cons_sign.config(pady=10, padx=10, bg="#1c0275", fg="white")
        self.btn_cons_sign.place(x=600, y=100)

        self.btn_list_cons = Button(self.Conslayer, text="مشاهده ی \n لیست مشاوران", font="Calibri 20 bold", command=self.onclick_show_cons_list)
        self.btn_list_cons.config(pady=0, padx=0, bg="#1c0275", fg="white")
        self.btn_list_cons.place(x=590, y=250)

        self.btnAnjoman = Button(self.Conslayer, text="انجمن ها", font="Calibri 20 bold",command=self.onclick_show_Anjoman_list)
        self.btnAnjoman.config(pady=0, padx=0, bg="#1c0275", fg="white")
        self.btnAnjoman.place(x=620, y=380)

        self.btn_home = Button(self.Conslayer, image=self.IconHmoe,command=self.open_login_page_of_ConselorPage)
        self.btn_home.config( bg="#fdfce0")
        self.btn_home.place(x=100, y=60)

# mainframeVisitor
        self.Visitorlayer = Frame(self.layer_1,width=875,height=750)
        self.Visitorlayer.place(x=0, y=0)
        self.Visitorlayer.place_forget()
        self.lblimage2 = Label(self.Visitorlayer, image=self.player_3)
        self.lblimage2.place(x=0, y=0)

        # visirorButton
        self.lbl_visiror_title_name = Label(self.Visitorlayer, text="مراجعین", font="calibri 20 bold")
        self.lbl_visiror_title_name.config(bg="#fdfce0")
        self.lbl_visiror_title_name.place(x=400, y=60)

        self.btn_visiror_sign = Button(self.Visitorlayer, text="ثبت\n مراجعه کننده", font="Calibri 20 bold",command=self.onclick_show_visitor_sign)
        self.btn_visiror_sign.config(pady=10, padx=10, bg="#1c0275", fg="white")
        self.btn_visiror_sign.place(x=600, y=100)

        self.btn_list_visitor = Button(self.Visitorlayer, text="مشاهده ی \n وقت های ملاقات", font="Calibri 20 bold",command=self.onclick_show_visitor_list)
        self.btn_list_visitor.config(pady=0, padx=0, bg="#1c0275", fg="white")
        self.btn_list_visitor.place(x=590, y=250)

        self.btnBime = Button(self.Visitorlayer, text="بیمه ها", font="Calibri 20 bold",command=self.onclick_show_bime_list)
        self.btnBime.config(pady=0, padx=0, bg="#1c0275", fg="white")
        self.btnBime.place(x=650, y=380)

        self.btn_home = Button(self.Visitorlayer, image=self.IconHmoe, font="Calibri 10 bold",command=self.open_login_page_of_visitorPage)
        self.btn_home.config( bg="#fdfce0")
        self.btn_home.place(x=100, y=60)


#FrameLogin
        self.User=StringVar()
        self.Pass=StringVar()
        self.frmLogin = Frame(self.master, width=875,height=750, background="#fdfce0")
        self.frmLogin.place(x=0, y=0)
        self.lblimglog = Label(self.frmLogin, image=self.player_1).place(x=0, y=0)
        self.lblwellcome=Label(self.frmLogin,text="مرکز مشاوره حس خوب",background="#fdfce0",font="Calibri 40 bold").place(x=250,y=150)
        self.lblUser=Label(self.frmLogin,text="نام کاربری",background="#fdfce0",font="Calibri 20").place(x=550,y=340)
        self.lblPass=Label(self.frmLogin,text="رمز عبور",background="#fdfce0",font="Calibri 20").place(x=550,y=400)
        self.txtUser=Entry(self.frmLogin,textvariable=self.User,bg="white",fg="black",width=40)
        self.txtUser.place(x=250,y=355)
        self.txtPass = Entry(self.frmLogin, textvariable=self.Pass, bg="white",fg="black",show="*",width=40)
        self.txtPass.place(x=250, y=415)
        #دکمه مخفی سازی و نمایش پسورد هنگام ورود
        self.btnShowPass=Button(self.frmLogin,text="نمایش/پنهان رمز",command=self.ShowPass,font="Calibri 15",bg="#faf573")
        self.btnShowPass.place(x=390,y=500)
        self.btnLogin=Button(self.frmLogin,text="ورود",bg="#1c0275", fg="white",command=self.Login,font="Calibri 20")
        self.btnLogin.place(x=250,y=500)





#fram setting

        self.entry_admin_Id=StringVar()
        self.entry_admin_id=CTkEntry(self.frm_setting, textvariable=self.entry_admin_Id)
        self.entry_admin_id.place_forget()


        self.lnd_admin_name=Label(self.frm_setting,text="نام", font="Calibri 17 bold")
        self.lnd_admin_name.config(padx=10, pady=10, bg="#fdfce0",fg="black")
        self.lnd_admin_name.place(x=720, y=180)
        self.entry_admin_Name=StringVar()
        self.entry_admin_name=CTkEntry(self.frm_setting, textvariable=self.entry_admin_Name, bg_color="#fdfce0", justify=CENTER, corner_radius=20, border_color="#1c0275")
        self.entry_admin_name.place(x=390, y=160)

        self.lnd_admin_family=Label(self.frm_setting,text="نام\n خانوادگی", font="Calibri 17 bold")
        self.lnd_admin_family.config(padx=10, pady=10, bg="#fdfce0",fg="black")
        self.lnd_admin_family.place(x=700, y=230)
        self.entry_admin_Family=StringVar()
        self.entry_admin_family=CTkEntry(self.frm_setting, textvariable=self.entry_admin_Family,bg_color="#fdfce0",justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_admin_family.place(x=390, y=210)

        self.lnd_admin_username=Label(self.frm_setting,text="نام\n کاربری", font="Calibri 17 bold")
        self.lnd_admin_username.config(padx=10, pady=10, bg="#fdfce0",fg="black")
        self.lnd_admin_username.place(x=700, y=310)
        self.entry_admin_USERname=StringVar()
        self.entry_admin_username=CTkEntry(self.frm_setting, textvariable=self.entry_admin_USERname,bg_color="#fdfce0",justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_admin_username.place(x=390, y=270)

        self.lnd_admin_password=Label(self.frm_setting,text="رمز\n عبور", font="Calibri 17 bold")
        self.lnd_admin_password.config(padx=10, pady=10, bg="#fdfce0",fg="black")
        self.lnd_admin_password.place(x=700, y=380)
        self.entry_admin_Password=StringVar()
        self.entry_admin_password=CTkEntry(self.frm_setting, textvariable=self.entry_admin_Password,bg_color="#fdfce0",justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_admin_password.place(x=390, y=330)

        self.btn_admin_sabt=Button(self.frm_setting, text="ثبت", font="Calibri 17 bold", command=self.OnclickAdminSave)
        self.btn_admin_sabt.config(width=20,bg="#1c0275", fg="white")
        self.btn_admin_sabt.place(x=480, y=480)

        #tbl Admin
        self.tbl_list_admin=ttk.Treeview(self.frm_setting, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", height=20)
        self.tbl_list_admin.heading("# 1",text="رمز عبور")
        self.tbl_list_admin.column("# 1", width=100,anchor=E)
        self.tbl_list_admin.heading("# 2",text="نام کاربری")
        self.tbl_list_admin.column("# 2", width=80,anchor=E)
        self.tbl_list_admin.heading("# 3",text="نام خانوادگی")
        self.tbl_list_admin.column("# 3", width=90,anchor=E)
        self.tbl_list_admin.heading("# 4",text="نام")
        self.tbl_list_admin.column("# 4",width=60,anchor=E)
        self.tbl_list_admin.heading("# 5",text="شماره")
        self.tbl_list_admin.column("# 5",width=40,anchor=E)
        self.tbl_list_admin.bind("<Button-1>", self.GetAdminSelection)
        self.tbl_list_admin.place(x=100,y=120)

        self.btn_admin_edit = Button(self.frm_setting, image=self.IconEdit, command=self.EditDataInAdmin)
        self.btn_admin_edit.config(bg="green",width=30,height=30)
        self.btn_admin_edit.place(x=100, y=610)

        self.btn_admin_delete = Button(self.frm_setting, image=self.Icondelete,command=self.OnclickAdminDelete)
        self.btn_admin_delete.config(bg="yellow",width=30,height=30)
        self.btn_admin_delete.place(x=150, y=610)



#frameConselor
    #frame_cons_sign
        self.frame_cons_sign=Frame(self.Conslayer, width=400, height=550, background="white")
        self.frame_cons_sign.place(x=150, y=100)
        self.frame_cons_sign.place_forget()

        self.btn_close_cons_sign=Button(self.frame_cons_sign, image=self.IconClose, command=self.onclick_close_cons_sign)
        self.btn_close_cons_sign.config(bg="#ff0000",width=15,height=15)
        self.btn_close_cons_sign.place(x=0, y=0)

        #conselor_name
        self.lbl_cons_name_sign=Label(self.frame_cons_sign, text="نام", font="Calibri 17 bold")
        self.lbl_cons_name_sign.config(padx=10, pady=10, bg="white")
        self.lbl_cons_name_sign.place(x=325, y=60)
        self.entry_cons_Name_sign=StringVar()
        self.entry_cons_name_sign=CTkEntry(self.frame_cons_sign, textvariable=self.entry_cons_Name_sign, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_name_sign.place(x=90, y=60)

        #conselor_family
        self.lbl_cons_family_sign=Label(self.frame_cons_sign, text="نام\n خانوادگی", font="Calibri 17 bold")
        self.lbl_cons_family_sign.config(padx=10, pady=10, bg="white")
        self.lbl_cons_family_sign.place(x=310, y=120)
        self.entry_cons_Family_sign=StringVar()
        self.entry_cons_family_sign=CTkEntry(self.frame_cons_sign, textvariable=self.entry_cons_Family_sign, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_family_sign.place(x=90, y=120)

        #conselor_phone
        self.lbl_cons_phone_sign=Label(self.frame_cons_sign, text="شماره\n تماس", font="Calibri 17 bold")
        self.lbl_cons_phone_sign.config(padx=10, pady=10, bg="white")
        self.lbl_cons_phone_sign.place(x=315, y=200)
        self.entry_cons_Phone_sign=StringVar()
        self.entry_cons_phone_sign=CTkEntry(self.frame_cons_sign, textvariable=self.entry_cons_Phone_sign, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_phone_sign.place(x=90, y=180)

        #conselor_expertise
        self.lbl_cons_expertise_sign=Label(self.frame_cons_sign, text="تخصص", font="Calibri 17 bold")
        self.lbl_cons_expertise_sign.config(padx=10, pady=10, bg="white")
        self.lbl_cons_expertise_sign.place(x=310, y=300)
        self.combo_cons_Expertise_sign=StringVar()
        self.values=["مشاور کودک","مشاور تحصیلی","مشاور فردی","مشاور خانواده"]
        self.combo_cons_expertise_sign=CTkComboBox(self.frame_cons_sign, variable=self.combo_cons_Expertise_sign,values=self.values, state="readonly", justify=CENTER,dropdown_hover_color="red",border_color="#1c0275")
        self.combo_cons_expertise_sign.place(x=90, y=250)

        #btnsign
        self.btn_cons_sabt=Button(self.frame_cons_sign, text="ثبت", font="Calibri 17 bold", command=self.OnclickConsSave)
        self.btn_cons_sabt.config(width=20,bg="#1c0275", fg="white")
        self.btn_cons_sabt.place(x=80, y=420)


    #frame_cons_list
        self.frm_cons_list =Frame(self.Conslayer,width=400, height=550, background="white")
        self.frm_cons_list.place(x=150, y=100)
        self.frm_cons_list.place_forget()
        self.btn_close_cons_list = Button(self.frm_cons_list, image=self.IconClose, command=self.onclick_close_cons_list)
        self.btn_close_cons_list.config(bg="#ff0000",width=15,height=15)
        self.btn_close_cons_list.place(x=0, y=0)

        self.btn_cons_edit=Button(self.frm_cons_list, image=self.IconEdit, command=self.EditDataInConselor)
        self.btn_cons_edit.config(bg="green",width=30,height=30)
        self.btn_cons_edit.place(x=0, y=500)

        self.btn_cons_delete=Button(self.frm_cons_list, image=self.Icondelete, command=self.OnclickConsDelete)
        self.btn_cons_delete.config(bg="yellow",width=30,height=30)
        self.btn_cons_delete.place(x=70, y=500)

        #Table_cons_List
        self.tbl_list_cons=ttk.Treeview(self.frm_cons_list, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", height=20)
        self.tbl_list_cons.heading("# 1",text="تخصص")
        self.tbl_list_cons.column("# 1", width=100,anchor=E)
        self.tbl_list_cons.heading("# 2",text="شماره تماس")
        self.tbl_list_cons.column("# 2", width=90,anchor=E)
        self.tbl_list_cons.heading("# 3",text="نام خانوادگی")
        self.tbl_list_cons.column("# 3", width=90,anchor=E)
        self.tbl_list_cons.heading("# 4",text="نام")
        self.tbl_list_cons.column("# 4",width=70,anchor=E)
        self.tbl_list_cons.heading("# 5",text="شماره")
        self.tbl_list_cons.column("# 5",width=40,anchor=E)
        self.tbl_list_cons.bind("<Button-1>", self.GetConsSelection)
        self.tbl_list_cons.place(x=5,y=40)

        #freamecurdlist
        self.Crud_cons_List=Frame(self.Conslayer, width=200, height=280, background="white")
        self.Crud_cons_List.place(x=600, y=450)
        self.Crud_cons_List.place_forget()

        self.entry_cons_Id_crud=IntVar()
        self.entry_cons_id_crud=CTkEntry(self.Crud_cons_List, textvariable=self.entry_cons_Id_crud)
        self.entry_cons_id_crud.place_forget()

        self.lbl_cons_name_crud = Label(self.Crud_cons_List, text="نام", bg="white")
        self.lbl_cons_name_crud.pack()
        self.entry_cons_Name_crud=StringVar()
        self.entry_cons_name_crud=CTkEntry(self.Crud_cons_List, textvariable=self.entry_cons_Name_crud, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_name_crud.pack()

        self.lbl_cons_family_crud = Label(self.Crud_cons_List, text="نام خانوادگی", bg="white")
        self.lbl_cons_family_crud.pack()
        self.entry_cons_Family_crud=StringVar()
        self.entry_cons_family_crud = CTkEntry(self.Crud_cons_List, textvariable=self.entry_cons_Family_crud, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_family_crud.pack()

        self.lbl_cons_phone_crud = Label(self.Crud_cons_List, text="شماره تماس", bg="white")
        self.lbl_cons_phone_crud.pack()
        self.entry_cons_Phone_crud=StringVar()
        self.entry_cons_phone_crud = CTkEntry(self.Crud_cons_List, textvariable=self.entry_cons_Phone_crud, justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_cons_phone_crud.pack()

        self.lbl_cons_expertise_crud = Label(self.Crud_cons_List, text="تخصص", bg="white")
        self.lbl_cons_expertise_crud.pack()
        self.combo_cons_Expertise_crud=StringVar()
        self.values=["مشاور کودک","مشاور تحصیلی","مشاور فردی","مشاور خانواده"]
        self.combo_cons_expertise_crud = CTkComboBox(self.Crud_cons_List, variable=self.combo_cons_Expertise_crud,values=self.values, state="readonly", justify=CENTER,dropdown_hover_color="red",border_color="#1c0275")
        self.combo_cons_expertise_crud.pack()

        # FrameAnjoman
        self.frm_anjoman_list = Frame(self.Conslayer, width=400, height=550, background="#fdfce0")
        self.frm_anjoman_list.place(x=100, y=100)
        self.frm_anjoman_list.place_forget()
        self.btn_close_anjoman_list = Button(self.frm_anjoman_list, image=self.IconClose,command=self.onclick_close_Anjoman_list)
        self.btn_close_anjoman_list.config(bg="#ff0000",width=15,height=15)
        self.btn_close_anjoman_list.place(x=0, y=0)

        self.anjoman1=Button(self.frm_anjoman_list,text="انجمن \n روانشناسی \n  ایران ",font="Calibri 15 bold",command=self.ShowLinkanjoman1)
        self.anjoman1.config(pady=10, padx=10, bg="white", fg="black")
        self.anjoman1.place(x=90, y=10)

        self.anjoman2=Button(self.frm_anjoman_list,text=" انجمن \n روانشناسی \n سلامت",font="Calibri 15 bold",command=self.ShowLinkanjoman2)
        self.anjoman2.config(pady=10, padx=10, bg="white", fg="black")
        self.anjoman2.place(x=90, y=150)

        self.anjoman2=Button(self.frm_anjoman_list,text=" انجمن \n مشاوره \n ایران",font="Calibri 15 bold",command=self.ShowLinkanjoman3)
        self.anjoman2.config(pady=10, padx=10, bg="white", fg="black")
        self.anjoman2.place(x=103, y=290)


#frameVisitor
    # frame_visiror_sign
        self.visiror_frmsign = Frame(self.Visitorlayer, width=400, height=550, background="white")
        self.visiror_frmsign.place(x=100, y=100)
        self.visiror_frmsign.place_forget()

        self.btn_close_visiror_sign = Button(self.visiror_frmsign, image=self.IconClose,command=self.onclick_close_visitor_sign)
        self.btn_close_visiror_sign.config(bg="#ff0000",width=15,height=15)
        self.btn_close_visiror_sign.place(x=0, y=0)

        # visiror_name
        self.lbl_visiror_name_sign = Label(self.visiror_frmsign, text="نام", font="Calibri 17 bold")
        self.lbl_visiror_name_sign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_name_sign.place(x=320, y=40)
        self.entry_visiror_Name_sign = StringVar()
        self.entry_visiror_name_sign = CTkEntry(self.visiror_frmsign, textvariable=self.entry_visiror_Name_sign,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visiror_name_sign.place(x=90, y=40)

        # visiror_family
        self.lbl_visiror_family_sign = Label(self.visiror_frmsign, text="نام\n خانوادگی", font="Calibri 17 bold")
        self.lbl_visiror_family_sign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_family_sign.place(x=300, y=100)
        self.entry_visiror_Family_sign = StringVar()
        self.entry_visiror_family_sign = CTkEntry(self.visiror_frmsign, textvariable=self.entry_visiror_Family_sign,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visiror_family_sign.place(x=90, y=100)

        # visiror_phone
        self.lbl_visiror_phone_sign = Label(self.visiror_frmsign, text="شماره\n تماس", font="Calibri 17 bold")
        self.lbl_visiror_phone_sign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_phone_sign.place(x=310, y=170)
        self.entry_visiror_Phone_sign = StringVar()
        self.entry_visiror_phone_sign = CTkEntry(self.visiror_frmsign, textvariable=self.entry_visiror_Phone_sign,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visiror_phone_sign.place(x=90, y=160)


        #visiror_age
        self.lbl_visiror_age_sign = Label(self.visiror_frmsign, text="سن",font="Calibri 17 bold")
        self.lbl_visiror_age_sign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_age_sign.place(x=325, y=250)
        self.combo_visiror_Age_sign=IntVar()
        self.valuesage = self.GetAgeValue()
        self.combo_visiror_age_sign = CTkComboBox(self.visiror_frmsign,variable=self.combo_visiror_Age_sign ,values=self.valuesage,state="readonly", justify=CENTER,border_color="#1c0275",dropdown_hover_color="red")
        self.combo_visiror_age_sign.place(x=90, y=210)


        # visiror_nobat
        self.lbl_visiror_nobat_sign = Label(self.visiror_frmsign, text="نوبت", font="Calibri 17 bold")
        self.lbl_visiror_nobat_sign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_nobat_sign.place(x=320, y=320)
        self.entry_visiror_Nobat_sign = StringVar()
        self.entry_visiror_nobat_sign = CTkEntry(self.visiror_frmsign, textvariable=self.entry_visiror_Nobat_sign,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visiror_nobat_sign.place(x=90, y=265)

        self.lbl_visiror_conselorsign = Label(self.visiror_frmsign, text="مشاور", font="Calibri 17 bold")
        self.lbl_visiror_conselorsign.config(padx=10, pady=10, bg="white")
        self.lbl_visiror_conselorsign.place(x=320, y=380)
        self.combo_visiror_Conselorsign=IntVar()
        self.valuescons = self.LoadCnselorInComboCons()
        self.combo_visiror_conselorsign = CTkComboBox(self.visiror_frmsign,variable=self.combo_visiror_Conselorsign ,values=self.valuescons,state="readonly", justify=CENTER,border_color="#1c0275",dropdown_hover_color="red")
        self.combo_visiror_conselorsign.place(x=90, y=310)

        # frameshowconselortabke
        self.ShowTblConselorInVisitorSign = Frame(self.Visitorlayer, width=240, height=230, background="white")
        self.ShowTblConselorInVisitorSign.place(x=550, y=420)
        self.ShowTblConselorInVisitorSign.place_forget()

        self.btn_ShowTblConselorInVisitorSign = Button(self.visiror_frmsign,image=self.IconConselor , font="Calibri 12 bold",command=self.onclick_show_tblConselor_for_signVisitor)
        self.btn_ShowTblConselorInVisitorSign.config(bg="white",)
        self.btn_ShowTblConselorInVisitorSign.place(x=50, y=390)

        self.btn_close_TblConselorInVisitorSign = Button(self.ShowTblConselorInVisitorSign, image=self.IconClose,command=self.onclick_close_tblConselor_for_signVisitor)
        self.btn_close_TblConselorInVisitorSign.config(bg="#ff0000",width=15,height=15)
        self.btn_close_TblConselorInVisitorSign.place(x=0, y=10)

        # btn_visiror_sign
        self.btn_sabt = Button(self.visiror_frmsign, text="ثبت", font="Calibri 12 bold",command=self.OnclickVisirorSave)
        self.btn_sabt.config(width=30,bg="#1c0275", fg="white")
        self.btn_sabt.place(x=90, y=470)

        # frame_Visiror_list
        self.frm_visiror_list = Frame(self.Visitorlayer, width=680, height=550, background="white")
        self.frm_visiror_list.place(x=100, y=100)
        self.frm_visiror_list.place_forget()

        self.lbl_Caption1=Label(self.frm_visiror_list, text="جدول" ,font="Calibri 20 bold",background="white")
        self.lbl_Caption1.place(x=550,y=30)
        self.lbl_Caption2=Label(self.frm_visiror_list, text="مراجعه کنندگان" ,font="Calibri 20 bold",background="white")
        self.lbl_Caption2.place(x=500, y=80)
        self.lbl_Caption3=Label(self.frm_visiror_list, text="کلینیک" ,font="Calibri 20 bold",background="white")
        self.lbl_Caption3.place(x=550, y=140)
        self.lbl_Caption4=Label(self.frm_visiror_list, text="حس خوب" ,font="Calibri 20 bold",background="white")
        self.lbl_Caption4.place(x=525, y=200)

        self.btn_close_visiror_list = Button(self.frm_visiror_list, image=self.IconClose,command=self.onclick_close_visitor_list)
        self.btn_close_visiror_list.config(bg="#ff0000",width=15,height=15)
        self.btn_close_visiror_list.place(x=0, y=0)


        self.btn_visiror_edit = Button(self.frm_visiror_list, image=self.IconEdit, command=self.EditDataInVisitor)
        self.btn_visiror_edit.config(bg="green",width=30,height=30)
        self.btn_visiror_edit.place(x=0, y=410)

        self.btn_visiror_delete = Button(self.frm_visiror_list, image=self.Icondelete,command=self.OnclickVisitorDelete)
        self.btn_visiror_delete.config(bg="yellow",width=30,height=30)
        self.btn_visiror_delete.place(x=0, y=450)

        self.ShowTblConselorInVisitorCrud = Frame(self.frm_visiror_list, width=270, height=110, background="white")
        self.ShowTblConselorInVisitorCrud.place(x=20, y=270)
        self.ShowTblConselorInVisitorCrud.place_forget()

        self.btn_close_TblConselorInVisitorCrud = Button(self.ShowTblConselorInVisitorCrud, image=self.IconClose,command=self.onclick_close_tblConselor_for_CrudVisitor)
        self.btn_close_TblConselorInVisitorCrud.config(bg="#ff0000",width=15,height=15)
        self.btn_close_TblConselorInVisitorCrud.place(x=0, y=0)

        self.btn_ShowTblConselorInVisitorCrud = Button(self.frm_visiror_list,image=self.IconConselor,command=self.onclick_show_tblConselor_for_CrudVisitor)
        self.btn_ShowTblConselorInVisitorCrud.config(bg="white")
        self.btn_ShowTblConselorInVisitorCrud.place(x=0, y=500)


        # Table_visiror_List
        self.tbl_list_visitor = ttk.Treeview(self.frm_visiror_list, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),show="headings", height=10)
        self.tbl_list_visitor.heading("# 1", text="مشاور")
        self.tbl_list_visitor.column("# 1", width=40, anchor=E)
        self.tbl_list_visitor.heading("# 2", text="نوبت")
        self.tbl_list_visitor.column("# 2", width=100, anchor=E)
        self.tbl_list_visitor.heading("# 3", text="سن")
        self.tbl_list_visitor.column("# 3", width=30, anchor=E)
        self.tbl_list_visitor.heading("# 4", text="شماره تماس")
        self.tbl_list_visitor.column("# 4", width=100, anchor=E)
        self.tbl_list_visitor.heading("# 5", text="نام خانوادگی")
        self.tbl_list_visitor.column("# 5", width=100, anchor=E)
        self.tbl_list_visitor.heading("# 6", text="نام")
        self.tbl_list_visitor.column("# 6", width=50, anchor=E)
        self.tbl_list_visitor.heading("# 7", text="شماره")
        self.tbl_list_visitor.column("# 7", width=40, anchor=E)
        self.tbl_list_visitor.bind("<Button-1>", self.GetVisitorSelection)
        self.tbl_list_visitor.place(x=5, y=40)

        # table conseluor for sign
        self.tbl_list_conseluor_for_signVisitor = ttk.Treeview(self.ShowTblConselorInVisitorSign,columns=("c1", "c2", "c3", "c4"), show="headings",height=8)
        self.tbl_list_conseluor_for_signVisitor.heading("# 1", text="تخصص")
        self.tbl_list_conseluor_for_signVisitor.column("# 1", width=75, anchor=E)
        self.tbl_list_conseluor_for_signVisitor.heading("# 2", text="نام خانوادگی")
        self.tbl_list_conseluor_for_signVisitor.column("# 2", width=75, anchor=E)
        self.tbl_list_conseluor_for_signVisitor.heading("# 3", text="نام")
        self.tbl_list_conseluor_for_signVisitor.column("# 3", width=45, anchor=E)
        self.tbl_list_conseluor_for_signVisitor.heading("# 4", text="شماره")
        self.tbl_list_conseluor_for_signVisitor.column("# 4", width=40, anchor=E)
        self.tbl_list_conseluor_for_signVisitor.place(x=0, y=40)

        # table conseluor for crud
        self.tbl_list_conseluor_for_CrudVisitor = ttk.Treeview(self.ShowTblConselorInVisitorCrud,columns=("c1", "c2", "c3", "c4"), show="headings", height=4)
        self.tbl_list_conseluor_for_CrudVisitor.heading("# 1", text="تخصص")
        self.tbl_list_conseluor_for_CrudVisitor.column("# 1", width=75, anchor=E)
        self.tbl_list_conseluor_for_CrudVisitor.heading("# 2", text="نام خانوادگی")
        self.tbl_list_conseluor_for_CrudVisitor.column("# 2", width=75, anchor=E)
        self.tbl_list_conseluor_for_CrudVisitor.heading("# 3", text="نام")
        self.tbl_list_conseluor_for_CrudVisitor.column("# 3", width=45, anchor=E)
        self.tbl_list_conseluor_for_CrudVisitor.heading("# 4", text="شماره")
        self.tbl_list_conseluor_for_CrudVisitor.column("# 4", width=40, anchor=E)
        self.tbl_list_conseluor_for_CrudVisitor.place(x=27, y=0)
        # crud visitor

        self.entry_visitor_Id_crud = IntVar()
        self.entry_visitor_id_crud = Entry(self.frm_visiror_list, textvariable=self.entry_visitor_Id_crud)
        self.entry_visitor_id_crud.place_forget()

        self.lbl_visitor_name_crud = Label(self.frm_visiror_list, text="نام", bg="white", font="Calibri 17 bold")
        self.lbl_visitor_name_crud.place(x=620, y=380)
        self.entry_visitor_Name_crud = StringVar()
        self.entry_visitor_name_crud = CTkEntry(self.frm_visiror_list, textvariable=self.entry_visitor_Name_crud,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visitor_name_crud.place(x=320, y=305)

        self.lbl_visitor_family_crud = Label(self.frm_visiror_list, text="نام\n خانوادگی", bg="white", font="Calibri 17 bold")
        self.lbl_visitor_family_crud.place(x=600, y=430)
        self.entry_visitor_Family_crud = StringVar()
        self.entry_visitor_family_crud = CTkEntry(self.frm_visiror_list, textvariable=self.entry_visitor_Family_crud,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visitor_family_crud.place(x=320, y=360)

        self.lbl_visitor_phone_crud = Label(self.frm_visiror_list, text=" شماره\n تماس", bg="white", font="Calibri 17 bold")
        self.lbl_visitor_phone_crud.place(x=610, y=490)
        self.entry_visitor_Phone_crud = StringVar()
        self.entry_visitor_phone_crud = CTkEntry(self.frm_visiror_list, textvariable=self.entry_visitor_Phone_crud,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visitor_phone_crud.place(x=320, y=410)

        self.lbl_visitor_age_crud=Label(self.frm_visiror_list, text="سن", bg="white",font="Calibri 17 bold")
        self.lbl_visitor_age_crud.place(x=340,y=400)
        self.combo_visitor_Age_crud=IntVar()
        self.valuesage_crud = self.GetAgeValue()
        self.combo_visitor_age_crud=CTkComboBox(self.frm_visiror_list,variable=self.combo_visitor_Age_crud ,values=self.valuesage_crud,state="readonly", justify=CENTER,border_color="#1c0275",dropdown_hover_color="red")
        self.combo_visitor_age_crud.place(x=125,y=320)

        self.lbl_visitor_nobat_crud = Label(self.frm_visiror_list, text="نوبت", bg="white", font="Calibri 17 bold")
        self.lbl_visitor_nobat_crud.place(x=340, y=450)
        self.entry_visitor_Nobat_crud = StringVar()
        self.entry_visitor_nobat_crud = CTkEntry(self.frm_visiror_list, textvariable=self.entry_visitor_Nobat_crud,justify=CENTER,corner_radius=20,border_color="#1c0275")
        self.entry_visitor_nobat_crud.place(x=125, y=360)

        self.lbl_visitor_conselorcrud=Label(self.frm_visiror_list, text="مشاور", bg="white",font="Calibri 17 bold")
        self.lbl_visitor_conselorcrud.place(x=330,y=510)
        self.combo_visitor_Conselorcrud=IntVar()
        self.valuescons_crud = self.LoadCnselorInComboCons()
        self.combo_visitor_conselorcrud=CTkComboBox(self.frm_visiror_list,variable=self.combo_visitor_Conselorcrud ,values=self.valuescons_crud,state="readonly", justify=CENTER,border_color="#1c0275",dropdown_hover_color="red")
        self.combo_visitor_conselorcrud.place(x=120,y=405)

        #FrameBime
        self.frm_bime_list = Frame(self.Visitorlayer, width=400, height=550, background="#fdfce0")
        self.frm_bime_list.place(x=100, y=100)
        self.frm_bime_list.place_forget()
        self.btn_close_bime_list = Button(self.frm_bime_list, image=self.IconClose,command=self.onclick_close_bime_list)
        self.btn_close_bime_list.config(bg="#ff0000",width=15,height=15)
        self.btn_close_bime_list.place(x=0, y=0)

        self.bim1=Button(self.frm_bime_list,image=self.bime1,command=self.ShowLinkBime1)
        self.bim1.place(x=10, y=50)

        self.bim2=Button(self.frm_bime_list,image=self.bime2,command=self.ShowLinkBime2)
        self.bim2.place(x=150, y=30)

        self.bim3=Button(self.frm_bime_list,image=self.bime3,command=self.ShowLinkBime3)
        self.bim3.place(x=60, y=250)

        self.bim4=Button(self.frm_bime_list,image=self.bime4,command=self.ShowLinkBime4)
        self.bim4.place(x=10, y=140)

        self.bim5=Button(self.frm_bime_list,image=self.bime5,command=self.ShowLinkBime5)
        self.bim5.place(x=150, y=140)

        #tabedlsLoad
        self.LoadDataInVisitorTable()
        self.LoadConsolerInVisitorTableFor_sign()
        self.LoadConsolerInVisitorTableFor_Crud()
        self.LoadDataInConsTable()
        self.LoadDataInAdminTable()

    #function
    #Main_function
    def open_login_page_of_visitorPage(self):
        self.Visitorlayer.place_forget()
        self.layer_1.place(x=0, y=0)

    def open_login_page_of_ConselorPage(self):
        self.Conslayer.place_forget()
        self.layer_1.place(x=0, y=0)

    def open_conselor_page(self):
        self.Conslayer.place(x=0, y=0)

    def open_manager_page(self):
        self.Visitorlayer.place(x=0, y=0)



    #تابع نمایش پسورد
    def ShowPass(self):
        if self.txtPass['show']=='*':
            self.txtPass.config(show='')
        else:
            self.txtPass.config(show='*')
    #تابع ورود
    def Login(self):
        objL=admin("","",self.User.get(),self.Pass.get())
        objbl=AdminService()
        r=objbl.blExistLogin(admin,objL)
        if r==True:
            self.frmLogin.place_forget()
        else:
            messagebox.showerror("خطا","!نام کاربری یا رمز عبور اشتباه است")

#frmSetting
    #frmSetting_show
    def ShowSetting(self):
        self.frm_setting.place(x=0,y=0)

    def open_login_page_of_SettingPage(self):
        self.frm_setting.place_forget()
        self.layer_1.place(x=0, y=0)

    #frmSetting_table
    def GetAdminSelection(self,e):
        selection_row=self.tbl_list_admin.selection()
        if selection_row != ():
            self.entry_admin_Id.set(self.tbl_list_admin.item(selection_row)["values"][4])
            self.entry_admin_Name.set(self.tbl_list_admin.item(selection_row)["values"][3])
            self.entry_admin_Family.set(self.tbl_list_admin.item(selection_row)["values"][2])
            self.entry_admin_USERname.set(self.tbl_list_admin.item(selection_row)["values"][1])
            self.entry_admin_Password.set(self.tbl_list_admin.item(selection_row)["values"][0])
    #AdminSetting
    def OnclickAdminSave(self):
        if self.entry_admin_name.get()== "":
            messagebox.showerror("خطا", "نام را پر کنید")
            self.entry_admin_name.focus_set()

        elif self.entry_admin_family.get()== "":
            messagebox.showerror("خطا", "نام خانوادگی را پر کنید")
            self.entry_admin_family.focus_set()

        elif self.entry_admin_username.get()== "":
            messagebox.showerror("خطا", "نام کاربری را وارد کنید")
            self.entry_admin_username.focus_set()

        elif self.entry_admin_password.get()== "":
            messagebox.showerror("خطا", "رمز عبور را بنویسید")
            self.entry_admin_password.focus_set()

        else:
            objadmin=AdminService()
            result=objadmin.create_admin(self.entry_admin_name.get(), self.entry_admin_family.get(), self.entry_admin_username.get(), self.entry_admin_password.get())
            if result== True:
                listItemAdmin=[self.entry_admin_Name, self.entry_admin_Family, self.entry_admin_USERname, self.entry_admin_Password]
                self.cleareAdmin(listItemAdmin)
                messagebox.showinfo("خوش آمدید","همکار گرامی به کادر مدیریتی مرکز حس خوب اضافه شد")
                self.ReloadAdmin()
            else:
                messagebox.showerror("خطا","مشکلی در اجرای دستور پیش آمد")


    def OnclickAdminDelete(self):
        ressultAdminDelete=messagebox.askquestion("هشدار","آیا می خواهید حذف شود؟")
        if ressultAdminDelete=="yes":
            listItemAdminDelete=[self.entry_admin_Name, self.entry_admin_Family, self.entry_admin_USERname, self.entry_admin_Password]
            self.cleareAdmin(listItemAdminDelete)
            objblAdminDEL=AdminService()
            objblAdminDEL.delete_admin(self.entry_admin_Id.get())
            messagebox.showinfo("انجام شد","در کادر مدیریتی یک مورد با موفقیت حذف شد")
            self.ReloadAdmin()

    def EditDataInAdmin(self):
        ressultAdminEdit = AdminService()
        ressultAdminEdit.update_admin(admin, id=self.entry_admin_Id.get(), name=self.entry_admin_Name.get(), family=self.entry_admin_Family.get(), username=self.entry_admin_USERname.get(), password=self.entry_admin_Password.get())
        listItemAdminEdit = [self.entry_admin_Name, self.entry_admin_Family, self.entry_admin_USERname, self.entry_admin_Password]
        self.cleareAdmin(listItemAdminEdit)
        messagebox.showinfo("انجام شد","تغییرات مورد نظر با موفقیت اعمال شد")
        self.ReloadAdmin()



    def LoadDataInAdminTable(self):
        objAdminload=AdminService()
        listAdmins=objAdminload.read_admin()
        for item in listAdmins:
            self.tbl_list_admin.insert('',"end",text=item.id,values=[item.password,item.username,item.family,item.name,item.id])

    def ClearAdminTable(self):
        for item in self.tbl_list_admin.get_children():
            sel=(str(item),)
            self.tbl_list_admin.delete(sel)

    def ReloadAdmin(self):
        self.ClearAdminTable()
        self.LoadDataInAdminTable()

    def cleareAdmin(self,listval):
        for item in listval:
            item.set("")

    #conselorFunction_show
    def onclick_show_cons_sign(self):
        self.frame_cons_sign.place(x=150, y=100)


    def onclick_close_cons_sign(self):
        self.frame_cons_sign.place_forget()


    def onclick_show_cons_list(self):
        self.frm_cons_list.place(x=150, y=100)
        self.Crud_cons_List.place(x=600, y=450)


    def onclick_close_cons_list(self):
        self.frm_cons_list.place_forget()
        self.Crud_cons_List.place_forget()

    def onclick_show_Anjoman_list(self):
        self.frm_anjoman_list.place(x=150, y=100)

    def onclick_close_Anjoman_list(self):
        self.frm_anjoman_list.place_forget()

    #conselorFunction_show_tble
    def GetConsSelection(self,e):
        selection_row=self.tbl_list_cons.selection()
        if selection_row != ():
            self.entry_cons_Id_crud.set(self.tbl_list_cons.item(selection_row)["values"][4])
            self.entry_cons_Name_crud.set(self.tbl_list_cons.item(selection_row)["values"][3])
            self.entry_cons_Family_crud.set(self.tbl_list_cons.item(selection_row)["values"][2])
            self.entry_cons_Phone_crud.set(self.tbl_list_cons.item(selection_row)["values"][1])
            self.combo_cons_Expertise_crud.set(self.tbl_list_cons.item(selection_row)["values"][0])

    #conselorFunction_Crud
    def OnclickConsSave(self):
        if self.entry_cons_name_sign.get()== "":
            messagebox.showerror("خطا", "نام را پر کنید")
            self.entry_cons_name_sign.focus_set()

        elif self.entry_cons_family_sign.get()== "":
            messagebox.showerror("خطا", "نام خانوادگی را پر کنید")
            self.entry_cons_family_sign.focus_set()

        elif self.entry_cons_phone_sign.get()== "":
            messagebox.showerror("خطا", "شماره تماس را وارد کنید")
            self.entry_cons_phone_sign.focus_set()

        elif self.combo_cons_expertise_sign.get()== "":
            messagebox.showerror("خطا", "تخصص مورد نظر را انتخاب کنید")
            self.combo_cons_expertise_sign.focus_set()

        else:
            objconselor=ConselorService()
            result=objconselor.create_conselor(self.entry_cons_name_sign.get(), self.entry_cons_family_sign.get(), self.entry_cons_phone_sign.get(), self.combo_cons_expertise_sign.get())
            if result== True:
                listItem=[self.entry_cons_Name_sign, self.entry_cons_Family_sign, self.entry_cons_Phone_sign, self.combo_cons_Expertise_sign]
                self.cleareCons(listItem)
                messagebox.showinfo("خوش آمدید","مشاور مورد نظر با موفقیت یه مجموعه حس خوب اضافه شد")
                self.ReloadCons()
            else:
                messagebox.showerror("خطا","مشکلی در اجرای دستور پیش آمد")

    def OnclickConsDelete(self):
        ressult=messagebox.askquestion("هشدار","آیا می خواهید حذف شود؟")
        if ressult=="yes":
            listItem=[self.entry_cons_Name_crud, self.entry_cons_Family_crud, self.entry_cons_Phone_crud, self.combo_cons_Expertise_crud]
            self.cleareCons(listItem)
            objblcons=ConselorService()
            objblcons.delete_conselor(self.entry_cons_Id_crud.get())
            messagebox.showinfo("انجام شد","مشاوره مورد نظر با موفقیت حذف شد")
            self.ReloadCons()

    def EditDataInConselor(self):
        objblcons = ConselorService()
        objblcons.update_conselor(conselor, id=self.entry_cons_Id_crud.get(), name=self.entry_cons_Name_crud.get(), family=self.entry_cons_Family_crud.get(), phone=self.entry_cons_Phone_crud.get(), expertise=self.combo_cons_Expertise_crud.get())
        listItem = [self.entry_cons_Name_crud, self.entry_cons_Family_crud, self.entry_cons_Phone_crud, self.combo_cons_Expertise_crud]
        self.cleareCons(listItem)
        messagebox.showinfo("انجام شد","تغییرات مورد نظر با موفقیت اعمال شد")
        self.ReloadCons()

    def LoadDataInConsTable(self):
        objblcons=ConselorService()
        listConselor=objblcons.read_conselor()
        for item in listConselor:
            self.tbl_list_cons.insert('',"end",text=item.id,values=[item.expertise,item.phone,item.family,item.name,item.id])

    def ClearConselorTable(self):
        for item in self.tbl_list_cons.get_children():
            sel=(str(item),)
            self.tbl_list_cons.delete(sel)

    def ReloadCons(self):
        self.ClearConselorTable()
        self.LoadDataInConsTable()

    def cleareCons(self,listval):
        for item in listval:
            item.set("")

    #show link Anjoman

    def ShowLinkanjoman1(self,e=[]):
        webbrowser.open("https://www.iranpa.org/cgi-sys/suspendedpage.cgi")

    def ShowLinkanjoman2(self,e=[]):
        webbrowser.open("https://www.iranpa.org/cgi-sys/suspendedpage.cgi")

    def ShowLinkanjoman3(self,e=[]):
        webbrowser.open("https://irancounseling.ir/")

    #VisitorFunction_show
    def onclick_show_visitor_sign(self):
        self.visiror_frmsign.place(x=150, y=100)

    def onclick_close_visitor_sign(self):
        self.visiror_frmsign.place_forget()

    def onclick_show_visitor_list(self):
        self.frm_visiror_list.place(x=100, y=100)

    def onclick_close_visitor_list(self):
        self.frm_visiror_list.place_forget()

    def onclick_show_bime_list(self):
            self.frm_bime_list.place(x=150, y=100)

    def onclick_close_bime_list(self):
            self.frm_bime_list.place_forget()




    def onclick_show_bime_list(self):
        self.frm_bime_list.place(x=150, y=100)

    def onclick_close_bime_list(self):
        self.frm_bime_list.place_forget()

    def onclick_show_tblConselor_for_signVisitor(self):
        self.ShowTblConselorInVisitorSign.place(x=550, y=420)

    def onclick_close_tblConselor_for_signVisitor(self):
        self.ShowTblConselorInVisitorSign.place_forget()

    def onclick_show_tblConselor_for_CrudVisitor(self):
        self.ShowTblConselorInVisitorCrud.place(x=400, y=270)

    def onclick_close_tblConselor_for_CrudVisitor(self):
        self.ShowTblConselorInVisitorCrud.place_forget()

    #VisitorFunction_Tbleshow
    def GetVisitorSelection(self, e):
        selection_row = self.tbl_list_visitor.selection()
        if selection_row != ():
            self.entry_visitor_Id_crud.set(self.tbl_list_visitor.item(selection_row)["values"][6])
            self.entry_visitor_Name_crud.set(self.tbl_list_visitor.item(selection_row)["values"][5])
            self.entry_visitor_Family_crud.set(self.tbl_list_visitor.item(selection_row)["values"][4])
            self.entry_visitor_Phone_crud.set(self.tbl_list_visitor.item(selection_row)["values"][3])
            self.combo_visitor_Age_crud.set(self.tbl_list_visitor.item(selection_row)["values"][2])
            self.entry_visitor_Nobat_crud.set(self.tbl_list_visitor.item(selection_row)["values"][1])
            self.combo_visitor_Conselorcrud.set(self.tbl_list_visitor.item(selection_row)["values"][0])

    # VisitorFunction_Crud
    def OnclickVisirorSave(self):
        if self.entry_visiror_name_sign.get() == "":
            messagebox.showerror("خطا", "نام را پر کنید")
            self.entry_visiror_name_sign.focus_set()

        elif self.entry_visiror_family_sign.get() == "":
            messagebox.showerror("خطا", "نام خانوادگی را پر کنید")
            self.entry_visiror_family_sign.focus_set()

        elif self.entry_visiror_phone_sign.get() == "":
            messagebox.showerror("خطا", "شماره تماس را وارد کنید")
            self.entry_visiror_phone_sign.focus_set()

        elif self.combo_visiror_age_sign.get() == "":
            messagebox.showerror("خطا", "سن مورد نظر را انتخاب کنید")
            self.combo_visiror_age_sign.focus_set()

        elif self.entry_visiror_nobat_sign.get() == "":
            messagebox.showerror("خطا", "نوبت مورد نظر را انتخاب کنید")
            self.entry_visiror_nobat_sign.focus_set()

        elif not self.combo_visiror_conselorsign.get().isdigit():
            messagebox.showerror("خطا", "لطفا شناسه مشاور را وارد کنید")
            self.combo_visiror_conselorsign.focus_set()


        else:
            objvisitor = VisitorService()
            resultVisitor = objvisitor.create_visitor(self.entry_visiror_name_sign.get(),self.entry_visiror_family_sign.get(),self.entry_visiror_phone_sign.get(),int(self.combo_visiror_age_sign.get()),self.entry_visiror_nobat_sign.get(),int(self.combo_visiror_conselorsign.get()))
            if resultVisitor == True:
                messagebox.showerror("خطا", "مشکلی در اجرای دستور پیش آمد")
            else:
                listItemvisitorSighn = [self.entry_visiror_Name_sign, self.entry_visiror_Family_sign,self.entry_visiror_Phone_sign, self.combo_visiror_Age_sign,self.entry_visiror_Nobat_sign, self.combo_visiror_Conselorsign]
                self.cleareVisitor(listItemvisitorSighn)
                messagebox.showinfo("خوش آمدید", "مراجعه کننده  نظر با موفقیت یه مجموعه حس خوب اضافه شد")
                self.ReloadVisitor()

    def OnclickVisitorDelete(self):
        ressultt = messagebox.askquestion("هشدار", "آیا می خواهید خذف شود؟")
        if ressultt == "yes":
            listItemvisitor = [self.entry_visitor_Name_crud, self.entry_visitor_Family_crud,self.entry_visitor_Phone_crud, self.combo_visitor_Age_crud,self.entry_visitor_Nobat_crud, self.combo_visitor_Conselorcrud]
            self.cleareVisitor(listItemvisitor)
            objbvisitor = VisitorService()
            objbvisitor.delete_visitor(self.entry_visitor_Id_crud.get())
            messagebox.showinfo("انجام شد", "مراجعه کننده مورد نظر با موفقیت حذف شد")
            self.ReloadVisitor()

    def EditDataInVisitor(self):
        objbvisitors = VisitorService()
        objbvisitors.update_visitor(visitor, id=self.entry_visitor_Id_crud.get(),name=self.entry_visitor_Name_crud.get(),family=self.entry_visitor_Family_crud.get(),phone=self.entry_visitor_Phone_crud.get(), age=self.combo_visitor_Age_crud.get(),nobat=self.entry_visitor_Nobat_crud.get(),conselor_id=int(self.combo_visitor_Conselorcrud.get()))
        listItemvisitorEdit = [self.entry_visitor_Name_crud, self.entry_visitor_Family_crud,self.entry_visitor_Phone_crud, self.combo_visitor_Age_crud,self.entry_visitor_Nobat_crud, self.combo_visitor_Conselorcrud]
        self.cleareVisitor(listItemvisitorEdit)
        messagebox.showinfo("انجام شد", "تغییرات مورد نظر با موفقیت اعمال شد")
        self.ReloadVisitor()



    def LoadDataInVisitorTable(self):
        objblvisitor = VisitorService()
        listVisitor = objblvisitor.read_visitor()
        for item in listVisitor:
            self.tbl_list_visitor.insert('', "end", text=item.id,values=[item.conselor_id, item.nobat, item.age, item.phone, item.family,item.name, item.id])

    def LoadConsolerInVisitorTableFor_sign(self):
        objblcons = ConselorService()
        listConselor = objblcons.read_conselor()
        for item in listConselor:
            self.tbl_list_conseluor_for_signVisitor.insert('', "end", text=item.id,values=[item.expertise, item.family, item.name, item.id])

    def LoadConsolerInVisitorTableFor_Crud(self):
        objblcons = ConselorService()
        listConselor = objblcons.read_conselor()
        for item in listConselor:
            self.tbl_list_conseluor_for_CrudVisitor.insert('', "end", text=item.id,values=[item.expertise, item.family, item.name, item.id])


    def ClearVisitorTable(self):
        for item in self.tbl_list_visitor.get_children():
            rel = (str(item),)
            self.tbl_list_visitor.delete(rel)



    def ReloadVisitor(self):
        self.ClearVisitorTable()
        self.LoadDataInVisitorTable()

    def cleareVisitor(self, listval):
        for item in listval:
            item.set("")

    def GetAgeValue(self):
        counter = []
        for item in range(1, 100):
            counter.append(str(item))
        return counter

    def LoadCnselorInComboCons(self):
        objblcons = ConselorService()
        listfamily = objblcons.read_conselor()
        listt = []
        for item in listfamily:
            listt.append(str(item.id))
        return listt

    #show link bimw

    def ShowLinkBime1(self,e=[]):
        webbrowser.open("https://esata.ir/web/sata/clinic")

    def ShowLinkBime2(self,e=[]):
        webbrowser.open("https://darman.mellatyar.app/")

    def ShowLinkBime3(self,e=[]):
        webbrowser.open("https://eservices.ihio.gov.ir/erx/")

    def ShowLinkBime4(self,e=[]):
        webbrowser.open("http://life.pasargadinsurance.ir:2525/(S(rhuefsi4yid4iqlqm4nlvtxj))/Insur48/SYS_48.aspx")

    def ShowLinkBime5(self,e=[]):
        webbrowser.open("https://totalapp.dana-insurance.ir/subportal")





















