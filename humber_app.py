from tkinter import *
from tkinter import messagebox
from humber_database import*
from tkinter import ttk
from datetime import datetime
import tkinter as tk

create_table()

win=Tk()
win.state("zoomed")
win.configure(bg="green")
win.title("Humber North Campus Center")
win.resizable(width=False ,height=False)

lbl_title=Label(win,text="Humber Student Registration Portal",font=('',35,'bold'),bg='green',fg='orange')
lbl_title.pack()

loggedUserName = "Admin"
class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas.
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))

        (x0, y0, x1, y1) = self.bbox("text")

        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height, bg="yellow")

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)

def Homescreen():
    frm=Frame(win,bg='olive')
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    marquee = Marquee(frm, text="Welcome to Humber College portal for the upcoming January 2022 intake. Important COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!", borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)

    lbl_user = Label(frm, text='Welcome to the Humber College Course Registration System', font=('', 20, 'bold'), bg='olive', fg='blue').place(x=400,y=50)

    lbl_user=Label(frm,text='Username:',font=('',20,'bold'),bg='olive',fg='red')
    lbl_user.place(x=400,y=100)

    lbl_pass=Label(frm,text='Password:',font=('',20,'bold'),bg='olive',fg='red')
    lbl_pass.place(x=400,y=160)

    entry_user=Entry(frm,font=('',15,'bold'),bg='yellow')
    entry_user.place(x=560,y=100)
    entry_user.focus()

    entry_pass=Entry(frm,font=('',15,'bold'),show='*',bg='yellow')
    entry_pass.place(x=560,y=160)

    btn_login = Button(frm, text='Sign-up', command=lambda: signup(frm, 0), font=('', 15, 'bold'), width=6, bd=1, bg='magenta', fg='magenta')
    btn_login.place(x=500, y=240)

    btn_login=Button(frm,text='Login',command=lambda:login(frm,entry_user,entry_pass),font=('',15,'bold'),width=6,bd=1,bg='magenta',fg='magenta')
    btn_login.place(x=610,y=240)

    btn_reset=Button(frm,text='Reset',command=lambda:reset(frm,entry_user,entry_pass),font=('',15,'bold'),width=6,bd=1,bg='magenta',fg='magenta')
    btn_reset.place(x=720,y=240)

def signup(wfrm, isAdmin):
    wfrm.destroy()
    frm = Frame(win, bg='olive')
    frm.place(x=0, y=100, relwidth=1, relheight=1)
    marquee = Marquee(frm,text="Welcome:User. Register student information on this Humber portal for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)
    if(isAdmin):
        lbl_tab = Label(frm, text='Signup New Admin Account', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=45)
        btn_back = Button(frm, text='Back', command=lambda: back(frm), font=('', 14, 'bold'), bg='green', fg='magenta', bd=5, width=5)
        btn_back.place(relx=0.91, y=50)
    else:
        lbl_tab = Label(frm, text='Signup New Student Account', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=45)
        btn_back = Button(frm, text='Back', command=lambda: back_to_login(frm), font=('', 14, 'bold'), bg='green', fg='magenta', bd=5, width=5)
        btn_back.place(relx=0.91, y=50)

    lbl_name = Label(frm, text='Full Name:', font=('', 20, 'bold'), bg='olive')
    lbl_name.place(relx=0.3, rely=0.2)
    entry_name = Entry(frm, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_name.place(relx=0.47, rely=0.2)
    entry_name.focus()

    lbl_age = Label(frm, text='Age:', font=('', 20, 'bold'), bg='olive')
    lbl_age.place(relx=0.3, rely=0.3)
    entry_age = Entry(frm, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_age.place(relx=0.47, rely=0.3)

    lbl_gender = Label(frm, text='Gender:', font=('', 20, 'bold'), bg='olive')
    lbl_gender.place(relx=0.3, rely=0.4)
    entry_gender = ttk.Combobox(frm, values=["Male", "Female"], font=('', 14, 'bold'))
    entry_gender.place(relx=0.47, rely=0.4)
    entry_gender.set("Select a Gender")

    lbl_username = Label(frm, text='Username:', font=('', 20, 'bold'), bg='olive')
    lbl_username.place(relx=0.3, rely=0.5)
    entry_username = Entry(frm, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_username.place(relx=0.47, rely=0.5)

    lbl_passwd = Label(frm, text='Password:', font=('', 20, 'bold'), bg='olive')
    lbl_passwd.place(relx=0.3, rely=0.6)
    entry_passwd = Entry(frm, font=('', 15, 'bold'),show='*', bd=5, bg='yellow')
    entry_passwd.place(relx=0.47, rely=0.6)

    btn_reg = Button(frm, text='Create Account', command=lambda: create_account_db(entry_name, entry_age, entry_gender, entry_username, entry_passwd, isAdmin), font=('', 15, 'bold'), bd=5, width=9, bg='green', fg='magenta')
    btn_reg.place(relx=0.45, rely=0.68)

    btn_reset = Button(frm, text='Reset', command=lambda: reset(frm, entry_name, entry_age, entry_gender, entry_username, entry_passwd), font=('', 15, 'bold'), bd=5, width=7, bg='green', fg='magenta')
    btn_reset.place(relx=0.57, rely=0.68)

def create_account_db(entry_name, entry_age, entry_gender, entry_username, entry_passwd, isAdmin):
    fullname = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    uname = entry_username.get()

    passwd = entry_passwd.get()
    dt = datetime.now().date()
    con = getcon()
    cur = con.cursor()

    # check if user name already exists
    cur.execute("select Username from tbl_login_credentials")
    rows = cur.fetchall()
    uname_already_exists = False
    try:
        for row in rows:
            print(row[0])
            if row[0] == uname:
                uname_already_exists = True
                break
    except:
        uname_already_exists = False

    if (uname_already_exists):
        messagebox.showinfo('Username not available', f'Choosen Username already being used by another account. Please change username to continue.')
    else:
        loginid = getnextcredentialsid()
        cur.execute("insert into tbl_login_credentials values(%s,%s,%s,%s,%s,%s,%s,%s)",(loginid,uname, passwd, isAdmin, fullname, age, gender, dt))
        con.commit()
        messagebox.showinfo('Account Created', f'Account Created Successfully.')
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_gender.delete(0, END)
        entry_username.delete(0, END)
        entry_passwd.delete(0, END)
        global loggedUserName
        loggedUserName = fullname
        if(isAdmin == 0):
            Student_welcome_screen(loggedUserName, loginid)
        elif(isAdmin == 1):
            Admin_welcome_screen(loggedUserName)

def back_to_login(wfrm):
    wfrm.destroy()
    loggedUserName = "Student"
    Homescreen()

def back(frm,loggedinUserId = None):
    frm.destroy()
    if (loggedinUserId != None):
        Student_welcome_screen(loggedUserName, loggedinUserId)
    else:
        Admin_welcome_screen(loggedUserName)

def reset(frm,x1,x2=None,x3=None,x4=None,x5=None,x6=None, screen=None):
    x1.delete(0,END)
    if(x2 != None):
        x2.delete(0,END)
    if (x3 != None):
        x3.delete(0,END)
    if(x4 != None):
        x4.delete(0,END)
    if(x5 != None):
        if(screen == "reg_screen"):
            x5.config(state=NORMAL)
            x5.delete(0,END)
            x5.config(state=DISABLED)
        else:
            x5.delete(0, END)
    if(x6 != None):
        x6.delete(0,END)
    x1.focus()

def login(frm,x1,x2):
    u=x1.get()
    p=x2.get()
    if (len(u)==0 or len(p)==0):
        messagebox.showwarning('Warning','User name and Pasword can not be empty.')
    else:
        con = getcon()
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_login_credentials;")
        rows = cur.fetchall()
        if (rows == None):
            messagebox.showwarning("None account set-up yet", "Student's and Admin's are NOT registered, yet!")
        else:
            print(rows)
            i = len(rows)
            global loggedUserName
            for idx, account in enumerate(rows):
                if(account[1] == u.lower() and account[2] == p.lower() and account[3] == 1):
                    messagebox.showinfo('Sucessfully Logged-in','Welcome Admin')
                    frm.destroy()
                    #win.configure(bg="green")
                    loggedUserName = account[4]
                    Admin_welcome_screen(loggedUserName)
                    return
                elif(account[1] == u.lower() and account[2] == p.lower() and account[3] == 0):
                    messagebox.showinfo('Sucessfully Logged-in', 'Welcome Student')
                    frm.destroy()
                    #win.configure(bg="green")
                    loggedUserName =  account[4]
                    loggedinUserId = account[0]
                    Student_welcome_screen(loggedUserName, loggedinUserId)
                    return
                elif(i == idx+1):
                    messagebox.showerror('Error','Invalid user name or password. Please try again.')

def logout(frm):
    frm.destroy()
    Homescreen()

def Admin_welcome_screen(loggedUserName):
    frm=Frame(win,bg='olive')
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    marquee = Marquee(frm, text="Welcome:Admin. Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!", borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)

    #lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='olive',fg='blue')
    #lbl_welcome.place(x=10,y=10)

    lbl_tab = Label(frm, text='', font=('', 20, 'bold'), bg='olive', fg='aqua')
    lbl_tab.place(relx=0.01, y=45)
    lbl_tab.configure(text="Hello Admin, '" + loggedUserName + "'!")

    btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',15,'bold'),bg='green',fg='magenta',bd=5,width=6)
    btn_logout.place(relx=0.9,y=50)

    btn_reg=Button(frm,text="Register Student Course",command=lambda:registerscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_reg.place(relx=0.4,y=70)

    btn_search=Button(frm,text="Search Student",command=lambda:searchscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_search.place(relx=0.4,y=140)

    btn_due = Button(frm, text="Check Due Amount", command=lambda: dueamountscreen(frm), font=('', 20, 'bold'),bg='green', bd=6, width=18)
    btn_due.place(relx=0.4, y=210)

    btn_update=Button(frm,text="Deposit Fee",command=lambda:depositscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_update.place(relx=0.4,y=280)

    btn_display = Button(frm, text="Display All Students", command=lambda: display_registered_data_screen(frm, loggedUserName), font=('', 20, 'bold'), bg='green',bd=6, width=18)
    btn_display.place(relx=0.4, y=350)

    btn_login = Button(frm, text='Add New Admin', command=lambda: signup(frm, 1), font=('', 20, 'bold'), width=18, bd=6, bg='green')
    btn_login.place(relx=0.4, y=420)

    btn_admin_scholarship = Button(frm, text="Approve Scholarships",command=lambda: display_Admin_Scholarship_screen(frm, loggedUserName), font=('', 20, 'bold'),bg='green', bd=6, width=18)
    btn_admin_scholarship.place(relx=0.4, y=490)

def Student_welcome_screen(loggedUserName, loggedinUserId):
    frm = Frame(win, bg='olive')
    frm.place(x=0, y=100, relwidth=1, relheight=1)
    marquee = Marquee(frm, text="Welcome:Student. Apply and Register any course via Humber portal. Search programs for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                      borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)

    lbl_tab = Label(frm, text='', font=('', 20, 'bold'), bg='olive', fg='aqua')
    lbl_tab.place(relx=0.01, y=45)
    lbl_tab.configure(text="Hello Student, '" + loggedUserName + "'!")

    btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 15, 'bold'), bg='green',
                        fg='magenta', bd=5, width=6)
    btn_logout.place(relx=0.9, y=50)

    btn_reg = Button(frm, text="Add Course", command=lambda: registerscreen(frm, loggedinUserId), font=('', 20, 'bold'),
                     bg='green', bd=6, width=18)
    btn_reg.place(relx=0.4, y=90)

    btn_search = Button(frm, text="Search saved Courses", command=lambda: searchscreen(frm, loggedinUserId), font=('', 20, 'bold'),
                        bg='green', bd=6, width=18)
    btn_search.place(relx=0.4, y=180)

    btn_due = Button(frm, text="Check Due Amount", command=lambda: dueamountscreen(frm, loggedinUserId),
                     font=('', 20, 'bold'), bg='green',
                     bd=6, width=18)
    btn_due.place(relx=0.4, y=270)

    btn_update = Button(frm, text="Deposit Fee Amount", command=lambda: depositscreen(frm, loggedinUserId), font=('', 20, 'bold'), bg='green',
                        bd=6, width=18)
    btn_update.place(relx=0.4, y=360)

    btn_display = Button(frm, text="View Registered Courses", command=lambda: display_registered_data_screen(frm,loggedUserName, loggedinUserId),
                         font=('', 20, 'bold'), bg='green', bd=6, width=18)
    btn_display.place(relx=0.4, y=450)

    btn_student_scholarship = Button(frm, text="Apply For Scholarships",command=lambda: display_Student_Scholarship_screen(frm, loggedUserName, loggedinUserId),
                         font=('', 20, 'bold'), bg='green', bd=6, width=18)
    btn_student_scholarship.place(relx=0.4, y=540)

def registerscreen(wfrm, loggedinUserId=None):
        wfrm.destroy()
        frm=Frame(win,bg='olive')
        frm.place(x=0,y=100,relwidth=1,relheight=1)

        marquee = Marquee(frm,text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                          borderwidth=1, relief="sunken")
        marquee.pack(side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

        if (loggedinUserId == None):
            lbl_tab = Label(frm, text='Register New Student', font=('', 35, 'bold'), bg='olive', fg='aqua')
            lbl_tab.place(relx=0.35, y=45)
        else:
            lbl_tab = Label(frm, text='Register New Course', font=('', 35, 'bold'), bg='olive', fg='aqua')
            lbl_tab.place(relx=0.35, y=45)
        btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',14,'bold'),bg='green',fg='magenta',bd=5,width=5)
        btn_logout.place(relx=0.92,y=50)

        btn_back=Button(frm,text='Back',command=lambda:back(frm,loggedinUserId),font=('',14,'bold'),bg='green',fg='magenta',bd=5,width=5)
        btn_back.place(relx=0.83,y=50)

        lbl_name=Label(frm,text='Student Name:',font=('',20,'bold'),bg='olive')
        lbl_name.place(relx=0.3,rely=0.2)
        entry_name=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_name.place(relx=0.47,rely=0.2)
        entry_name.focus()

        lbl_mob=Label(frm,text='Student Phone No:',font=('',20,'bold'),bg='olive')
        lbl_mob.place(relx=0.3,rely=0.3)
        entry_mob=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_mob.place(relx=0.47,rely=0.3)

        lbl_email=Label(frm,text='Student Email:',font=('',20,'bold'),bg='olive')
        lbl_email.place(relx=0.3,rely=0.4)
        entry_email=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_email.place(relx=0.47,rely=0.4)

        lbl_course=Label(frm,text='Course Name:',font=('',20,'bold'),bg='olive')
        lbl_course.place(relx=0.3,rely=0.5)

        availablecourses, course_details = getAvailableCourses()
        entry_course = ttk.Combobox(frm, values=availablecourses,font=('', 14, 'bold'))
        entry_course.place(relx=0.47,rely=0.5)
        entry_course.set("Pick a course")

        lbl_fee=Label(frm,text='Course Fee:',font=('',20,'bold'),bg='olive')
        lbl_fee.place(relx=0.3,rely=0.6)
        entry_fee=Entry(frm,textvariable=var4, font=('',15,'bold'),bd=5,bg='yellow')
        entry_fee.place(relx=0.47,rely=0.6)
        entry_fee.config(state=DISABLED)

        def fn_update_screen_fee(event):
            choosen_course = entry_course.get()
            print("combo value: "+choosen_course)
            print(course_details)
            try:
                for course in course_details:
                    print(course_details[course])
                    if(course_details[course][0] == choosen_course):
                        print("course" + course_details[course][0])
                        print("fee"+str(course_details[course][1]))
                        print(entry_fee.get())
                        var4.set(str(course_details[course][1]))
                        break
            except:
                print("Unexpected error occured while updating screen course fee!!")

        entry_course.bind("<<ComboboxSelected>>", fn_update_screen_fee)

        lbl_amt=Label(frm,text='Amount Paid:',font=('',20,'bold'),bg='olive')
        lbl_amt.place(relx=0.3,rely=0.7)
        entry_amt=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_amt.place(relx=0.47,rely=0.7)

        btn_reg=Button(frm,text='Register',command=lambda:reg_db(entry_name,entry_mob,entry_email,entry_course,entry_fee,entry_amt, None, loggedinUserId),font=('',15,'bold'),bd=5,width=7,bg='green',fg='magenta')
        btn_reg.place(relx=0.45,rely=0.78)

        btn_reset=Button(frm,text='Reset',command=lambda: reset(frm, entry_name, entry_mob,entry_email, entry_course, entry_fee, entry_amt, "reg_screen"),font=('',15,'bold'),bd=5,width=7,bg='green',fg='magenta')
        btn_reset.place(relx=0.57,rely=0.78)

boolRecordUpdated = True
def reg_db(e1, e2, e3, e4, e5, e6, sid=None, loggedinUserId=None):
    global boolRecordUpdated
    name = e1.get()
    mob = e2.get()
    email = e3.get()
    course = e4.get()
    fee = int(e5.get())
    amount = int(e6.get())
    dt = datetime.now().date()
    created_by_id = 0
    if (loggedinUserId != None):
        created_by_id = loggedinUserId

    if(boolRecordUpdated == False):
        con = getcon()
        cur = con.cursor()
        cur.execute("update tbl_students_details set stu_name='%s', stu_mob='%s', stu_email='%s', stu_course='%s', reg_date='%s', course_fee='%s', amount='%s', created_by ='%s' WHERE stu_id='%s'" % (name, mob, email, course, dt, fee, amount,created_by_id, sid))
        con.commit()
        messagebox.showinfo('Student Updated', f'Student course information Updated Successfully With Id:{sid} ')
        sid= -1
        boolRecordUpdated = True
        print(sid)
    else:
        sid=getnextid()
        con=getcon()
        cur=con.cursor()
        cur.execute("insert into tbl_students_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sid,name,mob,email,course,dt,fee,amount,created_by_id, 1))
        con.commit()
        messagebox.showinfo('Student Course Registered',f'Student selected course Registered Successfully With Id:{sid} ')

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.config(state=NORMAL)
    e5.delete(0, END)
    e5.config(state=DISABLED)
    e6.delete(0,END)
    e1.focus()

def getAvailableCourses():
    con = getcon()
    cur = con.cursor()
    cur.execute("SELECT * FROM tbl_course_details;")
    rows = cur.fetchall()
    print(rows)
    availablecourses = []
    course_details = {}
    count = 0
    try:
        for row in rows:
            course_details[count] = ([row[1], row[2]])
            count = count + 1;
            availablecourses.append(row[1])
        return availablecourses, course_details
    except:
        print("Unexpected error occured while fetching course names")

def searchscreen(wfrm,loggedinUserId = None):
    wfrm.destroy()
    frm=Frame(win,bg='olive')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    marquee = Marquee(frm,text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                      borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

    #lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='olive',fg='yellow')
    #lbl_welcome.place(x=10,y=10)
    if (loggedinUserId == None):
        lbl_tab = Label(frm, text='Search Registered Student', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    else:
        lbl_tab = Label(frm, text='Search Registered Course', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    btn_logout=Button(frm,command=lambda:logout(frm),text='Logout',font=('',15,'bold'),bg='green',fg='magenta',bd=5,width=6)
    btn_logout.place(relx=0.91,y=50)

    btn_back=Button(frm,command=lambda:back(frm,loggedinUserId),text='Back',font=('',15,'bold'),bg='green',fg='magenta',bd=5,width=5)
    btn_back.place(relx=0.83,y=50)

    lbl_name=Label(frm,text='Course Id:',font=('',20,'bold'),bg='olive')
    lbl_name.place(relx=.3,rely=.2)
    entry_sid=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
    entry_sid.place(relx=.42,rely=.2)
    entry_sid.focus()

    btn_sear=Button(frm,text='Search',command=lambda:search_stu_db(frm,entry_sid, loggedinUserId),font=('',15,'bold'),bg='green',fg='magenta',bd=5,width=8)
    btn_sear.place(relx=.4,rely=.3)

    btn_reset=Button(frm,text='Reset',command=lambda: reset(frm, entry_sid),font=('',15,'bold'),bd=5,width=8,bg='green',fg='magenta')
    btn_reset.place(relx=.51,rely=.3)

def search_stu_db(frm,e, loggedinUserId=None):
    sid=int(e.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select stu_name,stu_course,course_fee, amount, created_by from tbl_students_details where stu_id=%s and IsActive=1",(sid))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("Student Search","Student Id does not exist.")
    elif(loggedinUserId != None and loggedinUserId != row[4]):
        messagebox.showwarning("Student Search", "Selected course id is not your course id. You are not allowed to view other student course information. Please provide your course id to view details.")
    else:
        details = "Name:\t\t\t" + f"{str(row[0])}\n"
        details = details + "Course:\t\t\t" + f"{str(row[1])}\n"
        details = details + "Course Fee:\t\t" + f"{str(row[2])}\n"
        details = details + "Amount Paid:\t" + f"{str(row[3])}\n"

        messagebox.showinfo("Student Search",details)
        option=messagebox.askyesno("Update Student", message="Do you want to update student?")
        if(option==True):
            print(loggedinUserId)
            boolRecordUpdated = False
            updatescreen(frm,sid, loggedinUserId)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

def updatescreen(wfrm, sid,loggedinUserId = None):
    wfrm.destroy()
    frm = Frame(win, bg='olive')
    frm.place(x=0, y=100, relwidth=1, relheight=1)

    marquee = Marquee(frm,text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                      borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

    if (loggedinUserId == None):
        lbl_tab = Label(frm, text='Update Registered Student', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    else:
        lbl_tab = Label(frm, text='Update Registered Course', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 14, 'bold'), bg='green',
                        fg='magenta', bd=5, width=5)
    btn_logout.place(relx=0.92, y=50)

    btn_back = Button(frm, text='Back', command=lambda: back(frm,loggedinUserId), font=('', 14, 'bold'), bg='green', fg='magenta',
                      bd=5, width=5)
    btn_back.place(relx=0.83, y=50)

    lbl_name = Label(frm, text='Student Name:', font=('', 20, 'bold'), bg='olive')
    lbl_name.place(relx=0.3, rely=0.2)
    entry_name = Entry(frm, textvariable=var1, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_name.place(relx=0.47, rely=0.2)
    entry_name.focus()

    lbl_mob = Label(frm, text='Student Phone No:', font=('', 20, 'bold'), bg='olive')
    lbl_mob.place(relx=0.3, rely=0.3)
    entry_mob = Entry(frm, textvariable=var2, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_mob.place(relx=0.47, rely=0.3)

    lbl_email = Label(frm, text='Student Email:', font=('', 20, 'bold'), bg='olive')
    lbl_email.place(relx=0.3, rely=0.4)
    entry_email = Entry(frm, textvariable=var3, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_email.place(relx=0.47, rely=0.4)

    availablecourses, course_details = getAvailableCourses()

    lbl_course = Label(frm, text='Course Name:', font=('', 20, 'bold'), bg='olive')
    lbl_course.place(relx=0.3, rely=0.5)
    entry_course = ttk.Combobox(frm, textvariable=var4, values=availablecourses,font=('', 14, 'bold'))
    entry_course.place(relx=0.47, rely=0.5)

    lbl_fee = Label(frm, text='Course Fee:', font=('', 20, 'bold'), bg='olive')
    lbl_fee.place(relx=0.3, rely=0.6)
    entry_fee = Entry(frm, textvariable=var5, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_fee.place(relx=0.47, rely=0.6)
    entry_fee.config(state=DISABLED)

    def fn_update_fee_screen(event):
        choosen_course = entry_course.get()
        print("combo value: " + choosen_course)
        print(course_details)
        try:
            for course in course_details:
                print(course_details[course])
                if (course_details[course][0] == choosen_course):
                    print("course" + course_details[course][0])
                    print("fee" + str(course_details[course][1]))
                    print(entry_fee.get())
                    var5.set(str(course_details[course][1]))
                    break
        except:
            print("Unexpected error occured while updating course fee screen!!")

    entry_course.bind("<<ComboboxSelected>>", fn_update_fee_screen)

    lbl_amt = Label(frm, text='Amount Paid:', font=('', 20, 'bold'), bg='olive')
    lbl_amt.place(relx=0.3, rely=0.7)
    entry_amt = Entry(frm, textvariable=var6, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_amt.place(relx=0.47, rely=0.7)
    global boolRecordUpdated
    boolRecordUpdated = False
    btn_reg = Button(frm, text='Register',command=lambda: reg_db(entry_name, entry_mob, entry_email, entry_course, entry_fee, entry_amt,sid,loggedinUserId), font=('', 15, 'bold'), bd=5, width=7, bg='green', fg='magenta')
    btn_reg.place(relx=0.45, rely=0.78)

    btn_reset = Button(frm, text='Reset',command=lambda: reset(frm, entry_name, entry_mob,entry_email, entry_course, entry_fee, entry_amt, "reg_screen"), font=('', 15, 'bold'), bd=5, width=7, bg='green', fg='magenta')
    btn_reset.place(relx=0.57, rely=0.78)

    if (sid):
        con = getcon()
        cur = con.cursor()
        cur.execute("select stu_name,stu_mob,stu_email, stu_course, course_fee, amount from tbl_students_details where stu_id=%s and IsActive=1",(sid))
        row = cur.fetchone()
        if (row == None):
            messagebox.showwarning("Student Search", "Student Id does not exit")
        else:
            var1.set(str(row[0]))
            var2.set(row[1])
            var3.set(row[2])
            var4.set(row[3])
            var5.set(row[4])
            var6.set(row[5])

def update_stu_db(e1,e2,e3,e4,e5):
    sid=e1.get()
    name=e2.get()
    mob=e3.get()
    email=e4.get()
    course=e5.get()
    print(sid,name,mob,email,course)
    con=getcon()
    cur=con.cursor()
    cur.execute("""update tbl_students_details set stu_name=%s, stu_mob=%s, stu_email=%s, stu_course=%s where stu_id=%s""",(name,mob,email,course,sid))
    con.commit()
    con.close()
    messagebox.showinfo("Update Student","Student Record Updated...")

def dueamountscreen(wfrm,loggedinUserId = None):
    wfrm.destroy()
    frm=Frame(win,bg='olive')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    marquee = Marquee(frm, text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                      borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

    #lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='olive',fg='yellow')
    #lbl_welcome.place(x=10,y=10)

    lbl_tab = Label(frm, text='Check Due Amount', font=('', 35, 'bold'), bg='olive', fg='aqua')
    lbl_tab.place(relx=0.35, y=50)

    btn_logout=Button(frm,command=lambda:logout(frm),text='Logout',font=('',15,'bold'),bd=5,bg='green',fg='magenta',width=6)
    btn_logout.place(relx=.91,y=50)

    btn_back=Button(frm,command=lambda:back(frm,loggedinUserId),text='Back',font=('',15,'bold'),bd=5,bg='green',fg='magenta',width=5)
    btn_back.place(relx=0.83, y=50)

    lbl_name=Label(frm,text='Course Id:',font=('',20,'bold'),bg='olive')
    lbl_name.place(relx=.3,rely=.2)
    entry_sid=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
    entry_sid.place(relx=.47,rely=.2)
    entry_sid.focus()
   
    btn_sub=Button(frm,text='Submit',command=lambda:due_amt_db(entry_sid),font=('',15,'bold'),bd=5,bg='green',fg='magenta',width=8)
    btn_sub.place(relx=.45,rely=.3)

    btn_reset=Button(frm,text='Reset',command=lambda: reset(frm, entry_sid), font=('',15,'bold'),bd=5,bg='green',fg='magenta',width=8)
    btn_reset.place(relx=.56,rely=.3)

def due_amt_db(e):
    sid=int(e.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select course_fee,amount from tbl_students_details where stu_id=%a and IsActive=1",(sid,))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("balance","Student does not exist on this id")
    else:
        messagebox.showinfo("Balance",f"Balanced Due Amount : {row[0]-row[1]}")
    con.close()

def depositscreen(wfrm,loggedinUserId = None):
    wfrm.destroy()
    frm = Frame(win, bg='olive')
    frm.place(x=0, y=100, relwidth=1, relheight=1)

    marquee = Marquee(frm,text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important  COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!",
                      borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

    if (loggedinUserId == None):
        lbl_tab = Label(frm, text='Deposit Registered Student Fee', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    else:
        lbl_tab = Label(frm, text='Deposit Registered course Fee', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.35, y=50)
    btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 14, 'bold'), bg='green',
                        fg='magenta', bd=5, width=6)
    btn_logout.place(relx=0.91, y=50)

    btn_back = Button(frm, text='Back', command=lambda: back(frm,loggedinUserId), font=('', 14, 'bold'), bg='green', fg='magenta',
                      bd=5, width=5)
    btn_back.place(relx=0.83, y=50)

    lbl_sid = Label(frm, text='Student Id:', font=('', 20, 'bold'), bg='olive')
    lbl_sid.place(relx=0.3, rely=0.2)
    entry_sid = Entry(frm, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_sid.place(relx=0.47, rely=0.2)
    entry_sid.focus()

    lbl_amt = Label(frm, text='Amount:', font=('', 20, 'bold'), bg='olive')
    lbl_amt.place(relx=0.3, rely=0.3)
    entry_amt = Entry(frm, font=('', 15, 'bold'), bd=5, bg='yellow')
    entry_amt.place(relx=0.47, rely=0.3)

    btn_dep = Button(frm, text='Deposit', command=lambda: deposit_fee_db(entry_sid, entry_amt),
                     font=('', 15, 'bold'), bd=5, width=7, bg='green', fg='magenta')
    btn_dep.place(relx=0.45, rely=0.4)

    btn_reset = Button(frm, text='Reset', command=lambda: reset(frm, entry_sid, entry_amt), font=('', 15, 'bold'),
                       bd=5, bg='green', fg='magenta', width=8)
    btn_reset.place(relx=0.56, rely=0.4)

def deposit_fee_db(e1,e2):
    sid=int(e1.get())
    amt=int(e2.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select course_fee,amount from tbl_students_details where stu_id=%s and IsActive=1",(sid,))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("Fee Deposit",'Student does not exist on this id')
    else:
        if(row[1]<row[0]):
            if(row[0]>=(amt+row[1])):
                cur.execute("update tbl_students_details set amount=amount+%s where stu_id=%s",(amt,sid))
                messagebox.showinfo("Fee Deposit",'Fee Deposited')
                con.commit()
            else:
                messagebox.showinfo("Fee Deposit",'Deposited amount is not valid.')
        else:
            messagebox.showwarning("Fee Deposit",'Already fullpaid')
    con.close()

def display_registered_data_screen(wfrm, loggedUserName, loggedinUserId=None):
    con = getcon()
    cur = con.cursor()
    if (loggedinUserId != None):
        cur.execute("select stu_id, stu_name,stu_mob,stu_email,stu_course,reg_date,course_fee,amount from tbl_students_details where IsActive=1 and created_by=" + str(loggedinUserId))
    else:
        cur.execute("select stu_id, stu_name,stu_mob,stu_email,stu_course,reg_date,course_fee,amount from tbl_students_details  where IsActive=1")
    rows = cur.fetchall()

    if (rows == None):
        messagebox.showwarning("No One Registered", "Student are NOT registered, yet!")
    else:
        print(rows)
        wfrm.destroy()
        frm = Frame(win, bg='olive')
        frm.place(x=0, y=100, relwidth=1, relheight=1)

        #marquee = Marquee(frm,text="Welcome, Find enrolled students information on this Humber portal. Search programs/students for the upcoming January 2022 intake. Important COVID-19 Humber Updates: Please take vaccination before accessing the Humber campus, Make sure you have downloaded Humber Guardian app in your phone and upload self-assessment status before visiting us. Thank you!!", borderwidth=1, relief="sunken")
        #marquee.grid(side="top", padx=10, pady=10)#side="top", fill="x", pady=10)  # , bg='green',fg='magenta')

        if (loggedinUserId == None):
            lbl_welcome = Label(frm, text='Welcome:Admin', font=('', 20, 'bold'), bg='olive', fg='blue')
            lbl_welcome.place(x=10, y=10)

            lbl_tab = Label(frm, text='Display All Registered Students', font=('', 35, 'bold'), bg='olive', fg='aqua')
            lbl_tab.place(relx=0.35, y=11)
        else:
            lbl_tab = Label(frm, text='Display All the Registered Courses of you', font=('', 35, 'bold'), bg='olive', fg='aqua')
            lbl_tab.place(relx=0.25, y=11)
        btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=5)
        btn_logout.place(relx=0.92, y=11)

        btn_back = Button(frm, text='Back', command=lambda: back(frm,loggedinUserId), font=('', 14, 'bold'), bg='green', fg='magenta',bd=5, width=5)
        btn_back.place(relx=0.83, y=11)

        if (loggedinUserId == None):
            e = Label(frm, width=22, text='Admin: '+ loggedUserName, borderwidth=2, relief='ridge', anchor='w', bg='orange')
            e.grid(row=5, column=0, padx=(405, 10), pady=(65,2), columnspan=7)
            e = Label(frm, width=10, text='N01526516', borderwidth=2, relief='ridge', anchor='w', bg='orange')
            e.grid(row=6, column=0, padx=(300, 10), pady=(2, 10), columnspan=7)
        else:
            e = Label(frm, width=22, text='Student: '+ loggedUserName, borderwidth=2, relief='ridge', anchor='w',bg='orange')
            e.grid(row=5, column=0, padx=(405, 10), pady=(65, 2), columnspan=7)
            e = Label(frm, width=10, text=loggedinUserId, borderwidth=2, relief='ridge', anchor='w', bg='orange')
            e.grid(row=6, column=0, padx=(300, 10), pady=(2, 10), columnspan=7)

        e = Label(frm, width=5, text='Select', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=0, padx=(150, 10))
        e = Label(frm, width=12, text='Course ID', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=1)
        e = Label(frm, width=16, text='Student Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=2)
        e = Label(frm, width=12, text='Student Mobile', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=3)
        e = Label(frm, width=16, text='Email ID', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=4)
        e = Label(frm, width=12, text='Course', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=5)
        e = Label(frm, width=12, text='Registered Date', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=6)
        e = Label(frm, width=12, text='Course Fee', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=7)
        e = Label(frm, width=12, text='Amount Paid', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=8)

        del_rec = IntVar()

        i = 8
        for student in rows:
            for j in range(len(student)):
                if(j == 0):
                    Radiobutton(frm, width=5, variable=del_rec, value=student[j]).grid(row=i, column=j,padx=(150, 10))
                    e = Entry(frm, width=12, fg='blue')
                elif (j == 1 or j == 3):
                    e = Entry(frm, width=16, fg='blue')
                else:
                    e = Entry(frm, width=12, fg='blue')
                e.grid(row=i, column=j+1)
                e.insert(END, student[j])
                e["state"] = 'readonly'
            i = i + 1

        btn_del = Button(frm, text='Delete Record', command=lambda: delete_student_db(frm, del_rec, loggedUserName, loggedinUserId), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=8)
        btn_del.place(relx=0.45, y=490)

        if (loggedinUserId == None):
            btn_del_all = Button(frm, text='Delete All', command=lambda: delete_all_student_db(frm,loggedUserName, loggedinUserId),
                             font=('', 14, 'bold'), bg='green', fg='magenta', bd=5, width=8)
            btn_del_all.place(relx=0.58, y=490)

def delete_student_db(frm, del_rec, loggedUserName, loggedinUserId):
    del_stu_id = del_rec.get()
    print(del_stu_id)
    if(del_stu_id > 0):
        con = getcon()
        cur = con.cursor()
        #"DELETE FROM tbl_students_details WHERE stu_id=%s",(del_stu_id)
        cur.execute("update tbl_students_details set IsActive='%s' WHERE stu_id='%s'" % (0, del_stu_id))
        con.commit()
        cur.execute("update tbl_scholarship_status set IsActive='%s' WHERE student_id='%s'" % (0, del_stu_id))
        con.commit()
        con.close()
        messagebox.showinfo("Deleted Student", "Student record information removed successfully.")
        display_registered_data_screen(frm,loggedUserName, loggedinUserId)
    else:
        messagebox.showinfo("No student selected", "Please select one Student Record to remove.")

def delete_all_student_db(frm,loggedUserName, loggedinUserId):
    option = messagebox.askyesno("Delete All Students", message="Are you sure you want to delete all students information from the table?")
    if (option == True):
        con = getcon()
        cur = con.cursor()
        cur.execute("select * from tbl_students_details where IsActive=1")
        row = cur.fetchone()
        if (row != None):
            #"TRUNCATE TABLE tbl_students_details"
            cur.execute("update tbl_students_details set IsActive='%s'" % (0))
            con.commit()
            con.close()
            messagebox.showinfo("All Students Records Deleted", "All Students information removed successfully.")
            display_registered_data_screen(frm,loggedUserName, loggedinUserId)
        else:
            messagebox.showinfo("No student saved yet!", "Please register atleast one Student Record to perforn delete operation.")

def getScholarships(loggedinUserId=None):
    con = getcon()
    cur = con.cursor()
    cur.execute("SELECT * FROM tbl_scholarships_details;")
    scholarship_details = cur.fetchall()
    print(scholarship_details)
    try:
        if (loggedinUserId != None):
            cur.execute("SELECT stu_id, stu_course FROM tbl_students_details where IsActive=1 and created_by = "+ str(loggedinUserId))
            registered_courses = cur.fetchall()
            con.commit()
            print(registered_courses)
            availablecourses = []
            courses_registered = {}
            count = 0
            try:
                for row in registered_courses:
                    courses_registered[count] = ([row[0], row[1]])
                    count = count + 1;
                    availablecourses.append(row[1])
                return scholarship_details, availablecourses, courses_registered
            except:
                print("Unexpected error occured while fetching scholarship details for the student")
        else:
            cur.execute(
                "select tss.status_id, tsd2.scholarship_name,tsd2.award, tsd.stu_name, tss.scholarship_status, tsd.stu_course\
                FROM tbl_scholarship_status AS tss JOIN tbl_students_details AS tsd \
                ON tss.student_id = tsd.stu_id and tsd.IsActive = 1 and tss.IsActive = 1\
                JOIN tbl_scholarships_details AS tsd2 ON tss.scholarship_id = tsd2.scholarship_id;")
            rows = cur.fetchall()
            print(rows)
            if (rows != None):
                return scholarship_details, rows
        return scholarship_details, None
    except:
        print("Unexpected error occured while fetching scholarship names.!!")

def display_Admin_Scholarship_screen(wfrm, loggedUserName, loggedinUserId=None):
    con = getcon()
    cur = con.cursor()

    scholarship_details, applied_scholarship = getScholarships(None)

    if (applied_scholarship == None):
        messagebox.showwarning("No One Requested the scholarship yet", "Student have NOT requested for scholarship, yet!")
    else:
        print(applied_scholarship)
        wfrm.destroy()
        frm = Frame(win, bg='olive')
        frm.place(x=0, y=100, relwidth=1, relheight=1)

        lbl_welcome = Label(frm, text="Welcome:Admin, '"+loggedUserName+"!'", font=('', 20, 'bold'), bg='olive', fg='blue')
        lbl_welcome.place(x=10, y=10)

        lbl_tab = Label(frm, text='Applied Students Scholarship Status', font=('', 35, 'bold'), bg='olive', fg='aqua')
        lbl_tab.place(relx=0.32, y=20)

        btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=5)
        btn_logout.place(relx=0.92, y=11)

        btn_back = Button(frm, text='Back', command=lambda: back(frm,loggedinUserId), font=('', 14, 'bold'), bg='green', fg='magenta',bd=5, width=5)
        btn_back.place(relx=0.83, y=11)

        e = Label(frm, width=22, text='Admin: '+ loggedUserName, borderwidth=2, relief='ridge', anchor='w', bg='orange')
        e.grid(row=5, column=0, padx=(300, 10), pady=(65,2), columnspan=7)
        e = Label(frm, width=10, text='N01526516', borderwidth=2, relief='ridge', anchor='w', bg='orange')
        e.grid(row=6, column=0, padx=(300, 10), pady=(2, 10), columnspan=7)

        e = Label(frm, width=5, text='Select', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=0, padx=(100, 10))
        e = Label(frm, width=8, text='Status ID', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=1)
        e = Label(frm, width=28, text='Scholarship Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=2)
        e = Label(frm, width=8, text='Award', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=3)
        e = Label(frm, width=18, text='Student Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=4)
        e = Label(frm, width=15, text='Student Status', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=5)
        e = Label(frm, width=18, text='Course Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=6)
        #e = Label(frm, width=10, text='Amount Paid', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        #e.grid(row=7, column=7)

        def approve_scholarship_db():
            con = getcon()
            cur = con.cursor()
            cur.execute("SELECT status_id FROM tbl_scholarship_status where IsActive = 1;")
            status_ids = cur.fetchall()
            con.commit()
            con.close()
            print(status_ids)
            counter = 0
            checkboxes = [(variables, var.get()) for variables, var in checkbox_list.items()]
            con = getcon()
            cur = con.cursor()
            for checkbox in checkboxes:
                print(checkbox[1])
                print(status_ids[counter][0])
                #"SELECT stu_id, stu_course FROM tbl_students_details where IsActive=1 and created_by = "+ str(loggedinUserId)
                #cur.execute("select award from tbl_scholarships_details where scholarship_id = (select scholarship_id from tbl_scholarship_status where status_id = " + str(status_ids[counter][0]) + ")")
                #award = cur.fetchone()
                #print(award)
                #cur.execute("select student_id from tbl_scholarship_status where status_id = '%s'"%(str(status_ids[counter][0])))
                #stu_id = cur.fetchone()
                #print(stu_id)
                #cur.execute("select amount from tbl_students_details where stu_id = '%s'"%(str(stu_id[0])))
                #amount = cur.fetchone()
                #print(amount[0])
                #if (checkbox[1] == 1):
                    #then add award amount to the amount paid fee
                 #   amount = amount[0] + award[0]
                #elif (checkbox[1] == 0):
                    #else deduct awarded amount from the amount paid fee
                 #   amount = amount[0] - award[0]
                #cur.execute("UPDATE tbl_students_details SET amount = '%s' WHERE stu_id = '%s'" % (str(amount), str(stu_id[0])))
                cur.execute("UPDATE tbl_scholarship_status SET scholarship_status = '%s' WHERE status_id = '%s'" % ( str(checkbox[1]), str(status_ids[counter][0])))
                counter = counter + 1

            con.commit()
            con.close()
            messagebox.showinfo("Admin Updated Scholarship", "Scholarship updated successfully.")
            display_Admin_Scholarship_screen(wfrm, loggedUserName, loggedinUserId)
        checkboxState={}
        def checkbox_changed(status_id):
            if(not status_id in checkboxState):
                checkboxState[status_id] = True
            else:
                checkboxState[status_id] = False
            #filtered = [v for v in checkboxState.values() if v[True]]
            #print(filtered)
            print(checkboxState)
            print("checkbox" + str(status_id))

            print([k for k, v in checkboxState.items() if bool(v) == True])


        i = 8
        count = 0
        checkbox_list = {}  # dictionary to store all the IntVars

        for scholarship in applied_scholarship:
            for j in range(len(scholarship)):
                if(j == 0):
                    var = IntVar()
                    Checkbutton(frm,command=lambda:checkbox_changed(scholarship[0]), text=scholarship[j], width=5, variable=var).grid(row=i, column=j,padx=(100, 10))
                    checkbox_list[count] = var
                    var.set(scholarship[4])
                    count = count + 1
                    e = Entry(frm, width=8, fg='blue')
                elif (j == 1):
                    e = Entry(frm, width=28, fg='blue')
                elif (j == 2):
                    e = Entry(frm, width=8, fg='blue')
                elif (j == 4):
                    e = Entry(frm, width=15, fg='blue')
                #elif (j == 6):
                    #e = Entry(frm, width=10, fg='blue')
                else:
                    e = Entry(frm, width=18, fg='blue')
                e.grid(row=i, column=j+1)
                if(j == 4):
                    if(scholarship[j]==0):
                        e.insert(END, "Not Approved yet!!")
                    else:
                        e.insert(END, "Approved!!")
                else:
                    e.insert(END, scholarship[j])
                e["state"] = 'readonly'
            i = i + 1

        btn_Update_Scholarship = Button(frm, text='Approve/Disapprove Scholarship', command=lambda: approve_scholarship_db(), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=20)
        btn_Update_Scholarship.place(relx=0.45, rely=0.7)

def display_Student_Scholarship_screen(wfrm, loggedUserName, loggedinUserId=None):
    con = getcon()
    cur = con.cursor()
    if (loggedinUserId != None):
        scholarship_details,availablecourses, courses_registered = getScholarships(loggedinUserId)

        print(scholarship_details)
        wfrm.destroy()
        frm = Frame(win, bg='olive')
        frm.place(x=0, y=100, relwidth=1, relheight=1)

        lbl_welcome = Label(frm, text="Welcome:Student, '"+loggedUserName+"!'", font=('', 20, 'bold'), bg='olive', fg='blue')
        lbl_welcome.place(x=5, y=10)

        lbl_tab = Label(frm, text='Opened Scholarship Fall 2021', font=('', 35, 'bold'), bg='olive',fg='aqua')
        lbl_tab.place(relx=0.35, y=11)

        btn_logout = Button(frm, text='Logout', command=lambda: logout(frm), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=5)
        btn_logout.place(relx=0.92, y=11)

        btn_back = Button(frm, text='Back', command=lambda: back(frm,loggedinUserId), font=('', 14, 'bold'), bg='green', fg='magenta',bd=5, width=5)
        btn_back.place(relx=0.83, y=11)

        e = Label(frm, width=22, text='Student: '+ loggedUserName, borderwidth=2, relief='ridge', anchor='w',bg='orange')
        e.grid(row=5, column=0, padx=(405, 10), pady=(65, 2), columnspan=7)
        e = Label(frm, width=10, text=loggedinUserId, borderwidth=2, relief='ridge', anchor='w', bg='orange')
        e.grid(row=6, column=0, padx=(300, 10), pady=(2, 10), columnspan=7)

        entry_course = ttk.Combobox(frm, values=availablecourses, font=('', 14, 'bold'))
        entry_course.place(relx=0.45, rely=0.5)
        entry_course.set("Pick a registered course")

        e = Label(frm, width=5, text='Select', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=0, padx=(350, 10))
        e = Label(frm, width=12, text='Scholarship ID', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=1)
        e = Label(frm, width=40, text='Scholarship Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=2)
        e = Label(frm, width=12, text='Award', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=7, column=3)

        scholarship_rec = IntVar()
        i = 8
        for scholarship in scholarship_details:
            for j in range(len(scholarship)):
                if(j == 0):
                    Radiobutton(frm, width=5, variable=scholarship_rec, value=scholarship[j]).grid(row=i, column=j,padx=(350, 10))
                    e = Entry(frm, width=12, fg='blue')
                elif (j == 1):
                    e = Entry(frm, width=40, fg='blue')
                else:
                    e = Entry(frm, width=12, fg='blue')
                e.grid(row=i, column=j+1)
                e.insert(END, scholarship[j])
                e["state"] = 'readonly'
            i = i + 1

        def apply_scholarship_db(scholarship_rec):
            choosen_course = entry_course.get()
            print("combo value: " + choosen_course)
            print(courses_registered)
            student_id = 0
            try:
                for course in courses_registered:
                    print(courses_registered[course])
                    if (courses_registered[course][1] == choosen_course):
                        print("course" + courses_registered[course][1])
                        print("id" + str(courses_registered[course][0]))
                        student_id = courses_registered[course][0]
                        break
            except:
                print("Unexpected error occured while updating screen course fee!!")

            selected_scholarship_id = scholarship_rec.get()
            if (selected_scholarship_id > 0 and student_id > 0):
                con = getcon()
                cur = con.cursor()
                cur.execute("SELECT * FROM tbl_scholarship_status where student_id = " + str(student_id))
                row = cur.fetchone()
                print(row)
                if (row != None):
                    cur.execute("UPDATE tbl_scholarship_status SET scholarship_id ='%s' WHERE student_id = '%s'" % (
                    selected_scholarship_id, str(student_id)))
                    messagebox.showinfo("Updated Scholarship", "Scholarship updated successfully.")
                else:
                    cur.execute("insert into tbl_scholarship_status (scholarship_status,scholarship_id,student_id) values(%s,%s,%s)",
                        (0, str(selected_scholarship_id), str(student_id)))
                    messagebox.showinfo("Applied Scholarship", "Scholarship applied successfully.")
                con.commit()
                con.close()
            else:
                messagebox.showinfo("No scholarship or Course is selected", "Please make sure you have select one scholarship and one course to apply for.")

        def get_scholarship_status(event):
            choosen_course = entry_course.get()
            print("combo value: " + choosen_course)
            print(courses_registered)
            student_id = 0
            try:
                for course in courses_registered:
                    print(courses_registered[course])
                    if (courses_registered[course][1] == choosen_course):
                        print("course" + courses_registered[course][1])
                        print("id" + str(courses_registered[course][0]))
                        student_id = courses_registered[course][0]
                        break
            except:
                print("Unexpected error occured while updating screen course fee!!")

            if (student_id > 0):
                con = getcon()
                cur = con.cursor()
                cur.execute("SELECT scholarship_status FROM tbl_scholarship_status where student_id = " + str(student_id))
                scholarship_status = cur.fetchone()
                cur.execute("SELECT scholarship_id FROM tbl_scholarship_status where student_id = " + str(student_id))
                scholarship_id = cur.fetchone()
                con.commit()
                print(scholarship_status)
                con.commit()
                con.close()
                print(scholarship_id)
                scholarship_rec.set(scholarship_id)
                if (scholarship_status == None):
                    messagebox.showwarning("You have not applied for scholarship yet", "Hurry-up Grab the chances to secure a scholarship, apply early for Awards for the selected course!!")
                    scholarship_rec.set(0)
                elif (scholarship_status == (0,)):
                    messagebox.showwarning("Your scholarship is not approved yet","Please wait for the Awards, committee is reviewing your case for the selected course!! You could change the applied scholarship if you want.")
                else:
                    messagebox.showwarning("Scholarship approved","Congratulations Your scholarship has been approved for the selected course!!")

            else:
                messagebox.showinfo("No Course is selected", "Please make sure you have select a course to check status.")

        entry_course.bind("<<ComboboxSelected>>", get_scholarship_status)

        btn_apply_scholarship = Button(frm, text='Apply Scholarship', command=lambda: apply_scholarship_db(scholarship_rec), font=('', 14, 'bold'), bg='green',fg='magenta', bd=5, width=15)
        btn_apply_scholarship.place(relx=0.45, rely=0.7)

Admin_welcome_screen("Gursewak Singh Sidhu")
#Student_welcome_screen("Ikhlas Haniff", 1)
#Homescreen()
win.mainloop()