import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime


class ferry:
  def __init__(self,root):
    self.root=root
    self.root.title("FERRY MANAGEMENT SYSTEM")
    self.root.geometry("1400x500+0+0")

    self.FerryId = StringVar()
    self.Ferryname=StringVar()
    self.Seat = IntVar()
    self.From = StringVar()
    self.To = StringVar()
    self.Type = StringVar()
    self.Slot = IntVar()


    lbltitle=Label(self.root,bd=20,relief=RIDGE,text="FERRY MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold"))
    lbltitle.pack(side=TOP,fill=X)

    ##DATAFRAME

    Dataframe=Frame(self.root,bd=20,relief=RIDGE)
    Dataframe.place(x=0,y=130,width=1400,height=250)

    DataframeLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                font=("times new roman",12,"bold"),text="Ferry Infromation")
    
    DataframeLeft.place(x=0,y=5,width=800,height=200)

    DataframeRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                font=("times new roman",12,"bold"),text="Route Infromation")
    
    DataframeRight.place(x=810,y=5,width=500,height=200)

    ##BUTTON FRAME

    Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
    Buttonframe.place(x=0,y=400,width=1400,height=70)

    ##DETAILS FRAME

    Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
    Detailsframe.place(x=0,y=480,width=1400,height=180)

    ##DATA FRAME LEFT

    lblferryid = Label(DataframeLeft,text="Ferry ID",font=("times new roman",12,"bold"),padx=2,pady=6)
    lblferryid.grid(row=0,column=0,sticky=W)
    txt1 = Entry(DataframeLeft, textvariable=self.FerryId,font=("times new roman", 12, "bold"), width=25)
    txt1.grid(row=0, column=1)

    lblfname=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Ferry Name",padx=2,pady=6)
    lblfname.grid(row=1,column=0,sticky=W)
    txt2=Entry(DataframeLeft,textvariable=self.Ferryname,font=("times new roman",12,"bold"),width=25)
    txt2.grid(row=1,column=1)

    lblseat = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Seat Availability", padx=2, pady=6)
    lblseat.grid(row=2, column=0, sticky=W)
    txt3 = Entry(DataframeLeft, textvariable=self.Seat, font=("times new roman", 12, "bold"), width=25)
    txt3.grid(row=2, column=1)

    lblfrom = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="From", padx=2, pady=6)
    lblfrom.grid(row=3, column=0, sticky=W)
    txt4 = Entry(DataframeLeft, textvariable=self.From, font=("times new roman", 12, "bold"), width=25)
    txt4.grid(row=3, column=1)

    lblto = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="To", padx=2, pady=6)
    lblto.grid(row=4, column=0, sticky=W)
    txt5 = Entry(DataframeLeft, textvariable=self.To, font=("times new roman", 12, "bold"), width=25)
    txt5.grid(row=4, column=1)

    lbltype = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Type", padx=2, pady=6)
    lbltype.grid(row=0, column=30, sticky=W)
    txt6 = Entry(DataframeLeft, textvariable=self.Type, font=("times new roman", 12, "bold"), width=25)
    txt6.grid(row=0, column=31)

    lblslot = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Vehicle Slots", padx=2, pady=6)
    lblslot.grid(row=1, column=30, sticky=W)
    txt7 = Entry(DataframeLeft, textvariable=self.Slot, font=("times new roman", 12, "bold"), width=25)
    txt7.grid(row=1, column=31)



    ##DATAFRAME RIGHT

    self.txtInformation=Text(DataframeRight,font=("times new roman",12,"bold"),width=50,padx=2,pady=6)
    self.txtInformation.grid(row=0,column=0)

    ##BUTTONS

    btninfo=Button(Buttonframe,text="Display details",command=self.display,bg="green",fg="white",font=("times new roman",12,"bold"),width=15,height=1,padx=2,pady=6)
    btninfo.grid(row=0,column=0)

    btninsert = Button(Buttonframe, text="Insert",command=self.insert, bg="green", fg="white", font=("times new roman", 12, "bold"),width=15, height=1, padx=2, pady=6)
    btninsert.grid(row=0, column=2)

    btnupdate = Button(Buttonframe, text="Update",command=self.update, bg="green", fg="white", font=("times new roman", 12, "bold"),width=15, height=1, padx=2, pady=6)
    btnupdate.grid(row=0, column=4)

    btnroute = Button(Buttonframe,text="Route Info",command=self.information, bg="green", fg="white", font=("times new roman", 12, "bold"),width=15, height=1, padx=2, pady=6)
    btnroute.grid(row=0, column=6)

    btndelete = Button(Buttonframe, text="Delete", command=self.delete, bg="green", fg="white",
                      font=("times new roman", 12, "bold"), width=15, height=1, padx=2, pady=6)
    btndelete.grid(row=0, column=8)

    btnclear = Button(Buttonframe, text="Clear", command=self.clear, bg="green", fg="white",
                      font=("times new roman", 12, "bold"), width=15, height=1, padx=2, pady=6)
    btnclear.grid(row=0, column=10)

    btnexit = Button(Buttonframe, text="Exit", command=self.exit, bg="green", fg="white",
                      font=("times new roman", 12, "bold"), width=15, height=1, padx=2, pady=6)
    btnexit.grid(row=0, column=12)

    ##TABLE
    ##SCROLLBAR
    scroll_x=Scrollbar(Detailsframe,orient=HORIZONTAL)
    scroll_y = Scrollbar(Detailsframe,orient=VERTICAL)
    self.ferry_table=ttk.Treeview(Detailsframe,column=("FerryID","FerryName","SeatAvailability","From","To","VehicleSpots","Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=self.ferry_table.xview)
    scroll_y = ttk.Scrollbar(command=self.ferry_table.yview)

    self.ferry_table.heading("FerryID", text="Ferry ID")
    self.ferry_table.heading("FerryName",text="Ferry name")
    self.ferry_table.heading("SeatAvailability", text="Seat availability")
    self.ferry_table.heading("From", text="From")
    self.ferry_table.heading("To", text="To")
    self.ferry_table.heading("VehicleSpots", text="Vehicle spots")
    self.ferry_table.heading("Type", text="Type")


    self.ferry_table["show"]="headings"

    self.ferry_table.column("FerryID", width=60)
    self.ferry_table.column("FerryName", width=60)
    self.ferry_table.column("SeatAvailability", width=60)
    self.ferry_table.column("From", width=60)
    self.ferry_table.column("To", width=60)
    self.ferry_table.column("Type", width=60)
    self.ferry_table.column("VehicleSpots", width=60)

    self.ferry_table.pack(fill=BOTH,expand=1)

    self.ferry_table.bind("<ButtonRelease-1>", self.get_cursor)

    self.display()



##FUNCTIONALITY DECLARATION

  def update(self):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="pes2ug20cs334",
      database="proj"
    )

    mycursor = mydb.cursor()
    mycursor.execute("UPDATE FERRY_INFO SET Ferry_id=%s,Ferry_name=%s, Seat_availability=%s, source=%s , dest=%s, Type_of_ferry=%s, Vehicle_spots=%s ",
                     (self.FerryId.get(), self.Ferryname.get(),
                      self.Seat.get(), self.From.get(), self.To.get(),
                      self.Type.get(), self.Slot.get())
                     )
    mydb.commit()
    self.display()
    mydb.close()
    messagebox.showinfo("Success", "Record has been updated!")

  def insert(self):
    if self.FerryId.get()=="":
      messagebox.showerror("Error","FerryId is required!!")
    else:
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pes2ug20cs334",
        database="proj"
      )

      mycursor = mydb.cursor()

      mycursor.execute("INSERT INTO FERRY_INFO(Ferry_id,Ferry_name, Seat_availability, source , dest , Type_of_ferry, Vehicle_spots) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (self.FerryId.get(),self.Ferryname.get(),
                        self.Seat.get(),self.From.get(),self.To.get(),
                        self.Type.get(),self.Slot.get()))
      mydb.commit()
      self.display()
      mydb.close()
      messagebox.showinfo("Success","Record has been inserted!")



  def information(self):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="pes2ug20cs334",
      database="proj"
    )

    mycursor = mydb.cursor()
    self.txtInformation.insert(END,"Ferry ID:\t\t\t" + self.FerryId.get() + "\n")
    self.txtInformation.insert(END, "Ferry Name:\t\t\t" + self.Ferryname.get() + "\n")
    self.txtInformation.insert(END, "Source:\t\t\t" + self.From.get() + "\n")
    self.txtInformation.insert(END, "Destination:\t\t\t" + self.To.get() + "\n")
    query = "SELECT Travel_time FROM ROUTE_INFO WHERE Ferry_id = %s"
    value=(self.FerryId.get(),)
    mycursor.execute(query,value)
    res=mycursor.fetchall()
    self.txtInformation.insert(END, "Travel time:\t\t\t" ,res , "\n")
    mydb.commit()
    mydb.close()


  def display(self):
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pes2ug20cs334",
        database="proj"
      )

      mycursor = mydb.cursor()
      query = "SELECT * FROM FERRY_INFO WHERE Ferry_id = %s"
      value = (self.FerryId.get(),)
      mycursor.execute(query, value)
      res = mycursor.fetchall()
      if len(res) != 0:
        self.ferry_table.delete(*self.ferry_table.get_children())
        for i in res:
          self.ferry_table.insert("", END, values=i)
        mydb.commit()
      mydb.close()

  def delete(self):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="pes2ug20cs334",
      database="proj"
    )

    mycursor = mydb.cursor()
    query = "DELETE  FROM FERRY_INFO WHERE Ferry_id = %s"
    value = (self.FerryId.get(),)
    mycursor.execute(query,value)
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Delete", "Record has been Deleted!")




  def exit(self):
    exit=messagebox.askyesno("Ferry Management System","Do you want to exit?")
    if exit>0:
      root.destroy()
      return


  def clear(self):
    self.FerryId.set("")
    self.Ferryname.set("")
    self.Seat.set("")
    self.From.set("")
    self.To.set("")
    self.Type.set("")
    self.Slot.set("")
    self.txtInformation.delete("1.0",END)


  def get_cursor(self,event=""):
    cursor_row=self.ferry_table.focus()
    content=self.ferry_table.item(cursor_row)
    row=content["values"]
    self.FerryId.set(row[0])
    self.Ferryname.set(row[1])
    self.Seat.set(row[2])
    self.From.set(row[3])
    self.To.set(row[4])
    self.Type.set(row[5])
    self.Slot.set(row[6])



root=Tk()
ob=ferry(root)
root.mainloop()
