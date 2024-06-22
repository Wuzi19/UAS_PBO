from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #Variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        # 1st
        img=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\Robotika.jpg")
        img=img.resize((510,160),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root, command=self.open_img1,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)
        
         # 2nd
        img_2=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\Komputer.jpg")
        img_2=img_2.resize((510,160),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root, command=self.open_img2,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160)
        
         # 3st
        img_3=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\Sipil.jpg")
        img_3=img_3.resize((510,160),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        self.btn_3=Button(self.root, command=self.open_img3,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=160)
        
        
        #bg image    
        img_4=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\Rektorat.jpg")
        img_4=img_4.resize((1530,710),Image.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
      
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        
        
        lbl_title=Label(bg_lbl,text="Sistem Management Mahasiswa",font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        # manage Frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=25,y=55,width=1470,height=560)
        
        
        # left Frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Sistem Informasi",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=540)
        
        # img
        img_5=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\Rektorat.jpg")
        img_5=img_5.resize((650,120),Image.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)
      
        my_img= Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0, y=0, width=650, height=120)        
        
        # Current course LabelFrame Information
        std_lbl_info_frame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Informasi Pelajaran Saat Ini",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=10,y=120,width=660,height=115)
        
        # Labels and Combobox
        # department
        lbl_dep=Label(std_lbl_info_frame,text="Jurusan: ",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Pilih Jurusan","Computer","IT","Sipil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course
        course_std=Label(std_lbl_info_frame,text="Mata Kuliah:",font=("arial",12,"bold"),fg="black",bg="white")
        course_std.grid(row=1,column=0,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course, state="readonly",
                                                            font=("arial", 12, "bold"), width=17)
        com_txtcourse_std['value'] = ("Pilih Mata Kuliah", "FE", "SE", "TE", "BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=1, column=1, sticky=W, padx=2, pady=10)
        
        #year
        current_year=Label(std_lbl_info_frame,text="Tahun:",font=("arial",12,"bold"),fg="black",bg="white")
        current_year.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txt_current_year_std = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year, state="readonly",
                                                            font=("arial", 12, "bold"), width=17)
        com_txt_current_year_std['value'] = ("Pilih Tahun", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        com_txt_current_year_std.current(0)
        com_txt_current_year_std.grid(row=0, column=3, sticky=W, padx=2, pady=10)
        
        #semester
        label_Semester=Label(std_lbl_info_frame,text="Semester:",font=("arial",12,"bold"),fg="black",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        
        com_Semester = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester, state="readonly",
                                                            font=("arial", 12, "bold"), width=17)
        com_Semester['value'] = ("Pilih Semester", "Semester-1", "Semester-2")
        com_Semester.current(0)
        com_Semester.grid(row=1, column=3, sticky=W, padx=2, pady=10)
        
        # Student class LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Informasi Kelas Mata Kuliah",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=300)   
        
        #labels entry
        #ID
        lbl_id=Label(std_lbl_class_frame,text="ID Mahasiswa:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)     
        
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("arial",12,"bold"),width=17)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        #Name
        lbl_name=Label(std_lbl_class_frame,text="Nama Mahasiswa:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)     
        
        id_name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name,font=("arial",12,"bold"),width=17)
        id_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)    
        
        #Division
        lbl_div=Label(std_lbl_class_frame,text="Pembagian Kelas:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_div = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div, state="readonly",
                                                            font=("arial", 12, "bold"), width=15)
        com_txt_div['value'] = ("Pilih Kelas", "A", "B", "C", "D")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        
        #Roll
        lbl_roll=Label(std_lbl_class_frame,text="Roll No:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)     
        
        txt_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("arial",12,"bold"),width=17)
        txt_roll.grid(row=1,column=3,sticky=W,padx=2,pady=7)    
        
        #Gander
        lbl_gander=Label(std_lbl_class_frame,text="Jenis Kelamin:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_gander.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_gander = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, state="readonly",
                                                            font=("arial", 12, "bold"), width=15)
        com_txt_gander['value'] = ("Pilih Gender", "Pria", "Wanita")
        com_txt_gander.current(0)
        com_txt_gander.grid(row=2, column=1, sticky=W, padx=2, pady=7)
        
        #DOB
        lbl_dob=Label(std_lbl_class_frame,text="Tanggal Lahir",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)     
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=("arial",12,"bold"),width=17)
        txt_dob.grid(row=2,column=3,sticky=W,padx=2,pady=7)    
        
        #Email
        lbl_email=Label(std_lbl_class_frame,text="Email:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)     
        
        txt_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("arial",12,"bold"),width=17)
        txt_email.grid(row=3,column=1,sticky=W,padx=2,pady=7)    
        
        #Phone
        lbl_phone=Label(std_lbl_class_frame,text="No Telepon:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)     
        
        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,font=("arial",12,"bold"),width=17)
        txt_phone.grid(row=3,column=3,sticky=W,padx=2,pady=7) 
        
        #Address
        lbl_address=Label(std_lbl_class_frame,text="Alamat:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_address.grid(row=4,column=0,sticky=W,padx=2,pady=7)     
        
        txt_address=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=("arial",12,"bold"),width=17)
        txt_address.grid(row=4,column=1,sticky=W,padx=2,pady=7) 
        
        #Teacher
        lbl_teacher=Label(std_lbl_class_frame,text="Nama Pengajar:",font=("arial",12,"bold"),fg="black",bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)     
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,font=("arial",12,"bold"),width=17)
        txt_teacher.grid(row=4,column=3,sticky=W,padx=2,pady=7) 
        
        # Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)
        
        btn_add=Button(btn_frame, text="Save",command=self.add_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_add.grid(row=0,column=0, padx=1)
        
        btn_update=Button(btn_frame, text="Update",command=self.update_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_update.grid(row=0,column=1, padx=1)
        
        btn_delete=Button(btn_frame, text="Delete",command=self.delete_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_delete.grid(row=0,column=2, padx=1)
        
        btn_reset=Button(btn_frame, text="Reset",command=self.reset_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_reset.grid(row=0,column=3, padx=1)
        
        # right Frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Informasi Pelajaran Saat Ini", font=("times new roman", 12, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=670, y=10, width=900, height=540)
        
        #img1
        img_6=Image.open(r"C:\Users\zaini\Project PBO\student management system\college_images\college_images\DJulid.jpg")
        img_6=img_6.resize((780,200),Image.LANCZOS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)
      
        my_img= Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0, y=0, width=800, height=200)
        
        # right Frame
        Search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Cari Informasi Mahasiswa", font=("times new roman", 12, "bold"), fg="red", bg="white")
        Search_Frame.place(x=0, y=200, width=850, height=70)
        
        search_by=Label(Search_Frame,text="Cari Berdasarkan:",font=("arial",12,"bold"),fg="red",bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)     
        
        #Search
        self.var_com_search=StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, textvariable=self.var_com_search, state="readonly",
                                                            font=("arial", 12, "bold"), width=15)
        com_txt_search['value'] = ("Tentukan Pilihan", "Roll", "Phone", "id_mahasiswa")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame, textvariable=self.var_search,font=("arial",12,"bold"),width=15)
        txt_search.grid(row=0,column=2,padx=5)
        
        btn_search=Button(Search_Frame, command=self.search_data, text="Cari", font=("arial", 11, "bold"), width=12, bg="blue", fg="white")
        btn_search.grid(row=0,column=3, padx=5)
        
        btn_ShowA11=Button(Search_Frame, command=self.fetch_data, text="Tampilkan Semua", font=("arial", 11, "bold"), width=15, bg="blue", fg="white")
        btn_ShowA11.grid(row=0,column=4, padx=5)

        # =============================Student Table and Scroll bar======================================
        table_frame=Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=260, width=790, height=250)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Jurusan","Mata Kuliah","Tahun","Semester","Id","Nama","Kelas","Roll","Jenis Kelamin","Tanggal Lahir","Email","Phone","Alamat","Pengajar"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Jurusan",text="Jurusan")
        self.student_table.heading("Mata Kuliah",text="Mata Kuliah")
        self.student_table.heading("Tahun",text="Tahun")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Id",text="ID Mahasiswa")
        self.student_table.heading("Nama",text="Nama Mahasiswa")
        self.student_table.heading("Kelas",text="Kelas")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Jenis Kelamin",text="Jenis Kelamin")
        self.student_table.heading("Tanggal Lahir",text="Tanggal Lahir")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="No Telepon")
        self.student_table.heading("Alamat",text="Alamat")
        self.student_table.heading("Pengajar",text="Nama Pengajar")

        self.student_table["show"]="headings"

        self.student_table.column("Jurusan",width=100)
        self.student_table.column("Mata Kuliah",width=100)
        self.student_table.column("Tahun",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Nama",width=100)
        self.student_table.column("Kelas",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Jenis Kelamin",width=100)
        self.student_table.column("Tanggal Lahir",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Alamat",width=100)
        self.student_table.column("Pengajar",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() 


    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","Semua Bagian Diperlukan")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="zain",password="zain",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_dep.get(),
                                                                self.var_course.get(),
                                                                self.var_year.get(),
                                                                self.var_semester.get(),
                                                                self.var_std_id.get(),
                                                                self.var_std_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_email.get(),
                                                                self.var_phone.get(),
                                                                self.var_address.get(),
                                                                self.var_teacher.get()
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Berhasil","Mahasiswa telah ditambahkan!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Karena:{str(es)}",parent=self.root)

    #fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="zain",password="zain",database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student");
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","Semua Bagian diperlukan")
        else:
                try:
                    update=messagebox.askyesno("Update","Apakah anda yakin ingin memperbarui data mahasiswa ini?",parent=self.root)
                    if update>0:
                        conn=mysql.connector.connect(host="localhost",username="zain",password="zain",database="mydata")
                        my_cursur=conn.cursor()
                        my_cursur.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                self.var_dep.get(),
                                                                self.var_course.get(),
                                                                self.var_year.get(),
                                                                self.var_semester.get(),
                                                                self.var_std_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_email.get(),
                                                                self.var_phone.get(),
                                                                self.var_address.get(),
                                                                self.var_teacher.get(),
                                                                self.var_std_id.get()
                                                                ))
                    else:    
                        if not update:
                            return
                
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Berhasil","Mahasiswa Telah berhasil diperbaharui", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Karena:{str(es)}",parent=self.root)

    # delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Semua Bagian diperlukan")
        else:
            try:
                Delete=messagebox.askyesno("Hapus","Apakah Anda yakin ingin menghapus mahasiswa ini?",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="zain",password="zain",database="mydata")
                    my_cursur=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Hapus","Mahasiswamu telah dihapus!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Karena:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
            self.var_dep.set("Pilih Jurusan")
            self.var_course.set("Pilih Mata Kuliah")
            self.var_year.set("Pilih Tahun")
            self.var_semester.set("Pilih Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("Pilih Kelas")
            self.var_roll.set("")
            self.var_gender.set("Pilih Jenis Kelamin")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
    
    # Search Data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Tolong tentukan pilihan")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="zain",password="zain",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursur.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,value=i)


                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Karena:{str(es)}",parent=self.root)
        
    #open image
    def open_img1(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open image",filetype=(("JPG file","*.jpg"),("PNG file",".png"),("All files","*.*")))       
        img=Image.open(fln)
        img_browse=img.resize((510,160),Image.LANCZOS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)

    def open_img2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open image",filetype=(("JPG file","*.jpg"),("PNG file",".png"),("All files","*.*")))       
        img_2=Image.open(fln)
        img_browse_2=img_2.resize((510,160),Image.LANCZOS)
        self.photoimg_browse_2=ImageTk.PhotoImage(img_browse_2)
        self.btn_2.config(image=self.photoimg_browse_2)

    def open_img3(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open image",filetype=(("JPG file","*.jpg"),("PNG file",".png"),("All files","*.*")))       
        img_3=Image.open(fln)
        img_browse_3=img_3.resize((510,160),Image.LANCZOS)
        self.photoimg_browse_3=ImageTk.PhotoImage(img_browse_3)
        self.btn_3.config(image=self.photoimg_browse_3)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()


