from tkinter import *
from tkinter import ttk
from datetime import datetime

# المنتجات: رقم - [اسم, سعر]
products = {
    
    0: ['saw', 10],
    1: ['drill', 30],
    2: ['hammer', 15],

}

    


# إنشاء نافذة البرنامج
window = Tk()
window.title("برنامج بيع الأدوات")
window.geometry("1000x700")
window.config(bg="white")
#
iop=PhotoImage(file="download.png",height=50*3,width=40*5)
iol=PhotoImage(file="images.png",height=50*3,width=50*5)


oa=Button(relief=SOLID,cursor="hand2",image=iop,width=170,height=150)
oa.place(y=110,x=50)
ob=Button(relief=SOLID,cursor="hand2",image=iol,width=170,height=150)
ob.place(x=300,y=110)





ioy=PhotoImage(file="imagess.png",height=50*4,width=50*4)
oe=Button(relief=SOLID,cursor="hand2",image=ioy,width=170,height=150)
oe.place(y=110,x=550)



# عنوان البرنامج
title = Label(window, text="برنامج بيع الأدوات", font=("Arial", 18, "bold"), bg="black", fg="gold", height=2, width=110)
title.pack()

# حاوية المنتجات
product_frame = Frame(window, bg="white")
product_frame.place(x=25, y=300)

# تخزين الـ Spinbox لكل منتج
spinboxes = []

# إنشاء الحقول لكل منتج

for i in range(len(products)):
    name, price = products[i]
    Label(product_frame, text=f"{name} - {price} ريال", font=("Arial", 12), bg="white").grid(row=0, column=i, padx=20)
    
    var = IntVar()
    spin = Spinbox(product_frame, from_=0, to=20, width=7*2, textvariable=var, font=("Arial", 12))
    spin.grid(row=1, column=i, padx=50)
    spinboxes.append(spin)
   

# حاوية الجدول
tree_frame = Frame(window)
tree_frame.place(x=266*3, y=90)

# جدول الفاتورة
tree = ttk.Treeview(tree_frame, columns=("item", "price", "qty", "total"), show='headings', height=149)
tree.heading("item", text="المنتج")
tree.heading("price", text="السعر")
tree.heading("qty", text="الكمية")
tree.heading("total", text="الإجمالي")

tree.column("item", anchor="center", width=150)
tree.column("price", anchor="center", width=100)
tree.column("qty", anchor="center", width=100)
tree.column("total", anchor="center", width=150)

tree.pack()

# دالة إنشاء الفاتورة

def fatora():
    global p
    tree.delete(*tree.get_children())  # مسح الجدول السابق
    total_all = 0

    for i in range(len(products)):
        qty = int(spinboxes[i].get())
        if qty > 0:
            name, price = products[i]
            total = qty * price
            po=qty
            total_all += total
            t=total_all+price
            tree.insert("", "end", values=(name, price, qty, total))

    p=bo_Entry.config(text=f"الإجمالي الكلي: {total_all} ريال")
    
    
    o=datetime.now()
    ti=o.strftime('%d -%m-%y')
    bo_Entry.insert("1",f"total={total_all}")
    co_Entry.insert("2",str(ti))
    pass
    
        



    pass


    

    

    
        
    
def delete():
    for item in tree.get_children(): 
        tree.delete(item)  
        bo_Entry.delete('0',END)
        co_Entry.delete('0',END)
        print(123456789)
        pass

     
yu=Frame(window, bg='gray',width=250,height=700)
yu.place(x=1300,y=90)
total_labe = Label(window,font=("Arial", 18),fg='green',text='name',height=1,width=10,bg='white')
total_labe.place(x=1420, y=90)

to = Label(window,font=("Arial", 18),fg='green',text='phone  ',height=1,width=10,bg='white')
to.place(x=1420, y=255)

total_label = Label(window,font=("Arial", 18),fg='green',text='total',height=1,width=10,bg='white')
total_label.place(x=1430, y=370)

total_label = Label(window,font=("Arial", 18),fg='green',text='history',height=1,width=10,bg='white')
total_label.place(x=1420, y=470)




# inbut
bo_Entry=Entry(window,text='p', font=("Arial", 14), bg="white", fg="black")
bo_Entry.place(x=1320, y=400)
time_label=Label(window,font=("Arial", 12),fg='black',text='time',height=15,width=10)

co_Entry=Entry(window, font=("Arial", 14), bg="white", fg="black")
co_Entry.place(x=1320, y=500)

cn_Entry=Entry(window, font=("Arial", 14), bg="white", fg="black")
cn_Entry.place(x=1320, y=300)

cb_Entry=Entry(window, font=("Arial", 14), bg="white", fg="black")
cb_Entry.place(x=1320, y=200)

cu_Entry=Entry(window, font=("Arial", 14), bg="white", fg="black")
cu_Entry.place(x=1320, y=120)

        
     

# زر الشراء
buy_button = Button( window, text="buy", command=fatora  , bg="silver", fg="white", font=("Arial", 14), width=10)
buy_button.place(x=450, y=600)

dButton= Button(window, text='new bill',command=delete, bg="green", fg="white", font=("Arial", 14), width=10)
dButton.place(x=550, y=600)

# لعرض الإجمالي النهائي




# تشغيل الواجهة



window.mainloop()
@app.route("/generate-bill", methods=["POST"])
def generate_bill():
    data = request.json
    quantities = data["quantities"]
    name = data.get("name", "")
    phone = data.get("phone", "")
    location = data.get("location", "")
    bill = []
    total_all = 0

    for i, qty in enumerate(quantities):
        qty = int(qty)
        if qty > 0:
            product_name, price = products[i]
            total = qty * price
            bill.append({
                "name": product_name,
                "price": price,
                "qty": qty,
                "total": total

            })
            total_all += total
            print(total_all)
            wb = Workbook('ALI(2).xlsx')
            ws = wb.active
            for item in bill:
                ws.append([

    
        
            name,
            phone,
            location,
            item["qty"],
            item["price"],
            item["name"],
            item["total"],
            datetime.now().strftime("%Y-%m-%d"),

            wb.save('ALI(2).xlsx')

        ])