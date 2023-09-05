from tkinter import *
root=Tk()
root.geometry("500x300")

def getvalue():
    print("Accepted the Details")

#Heading
Label(root,text="PYTHON REGISTRATION FORM",font="ar 10 bold").grid(row=0,column=3)

#Field Name
name=Label(root,text="Name")
name.grid(row=1,column=2)
phone=Label(root,text="Phone")
phone.grid(row=2,column=2)
gender=Label(root,text="Gender")
gender.grid(row=3,column=2)
emergency=Label(root,text="Emergency")
emergency.grid(row=4,column=2)
paymentmode=Label(root,text="Paymentmode")
paymentmode.grid(row=5,column=2)

#Variable For Storing Data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmodevalue=StringVar
checkvalue=IntVar

#Creating Entry Field
nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=1,column=3)
phoneentry=Entry(root,textvariable=phonevalue)
phoneentry.grid(row=2,column=3)
genderentry=Entry(root,textvariable=gendervalue)
genderentry.grid(row=3,column=3)
emergencyentry=Entry(root,textvariable=emergencyvalue)
emergencyentry.grid(row=4,column=3)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
paymentmodeentry.grid(row=5,column=3)

#Creating Checkbox()
checkbtn=Checkbutton(text="Remember me ?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit Button
Button(text="Submit",command=getvalue,bg="red").grid(row=7,column=3)

root.mainloop()
