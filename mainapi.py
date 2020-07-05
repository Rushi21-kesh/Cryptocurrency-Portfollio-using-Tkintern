from tkinter import *
import requests #import requests to get API 
import json #it use to load tha data
import sqlite3

con = sqlite3.connect('Cripto Coin.db')
cObj = con.cursor()

#cObj.execute("CREATE TABLE IF NOT EXISTS Coin(id INTEGER PRIMARY kEY, symbol TEXT,amount INTEGER, price REAL)")
#con.commit()

#cObj.execute("insert into Coin values(1,'BTC',2,2700)")
#con.commit()

#cObj.execute("INSERT INTO Coin VALUES(2,'EOS',100,1.5)")
#con.commit()

#cObj.execute("INSERT INTO Coin VALUES(3,'LTC',55,75.50)")
#con.commit()

#cObj.execute("INSERT INTO Coin VALUES(4,'XMR',40,27.50)")
#con.commit()

cObj.execute("delete from Coin where id > 4")
con.commit()

guitk = Tk()
guitk.title("Cryptocurrency Portfollio")
guitk.iconbitmap('favicon.ico')

def My_code():

    Req_api = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=46e13689-58c4-4a91-8ea4-a675234d5bf7")
    api = json.loads(Req_api.content)

    cObj.execute("SELECT * FROM Coin")
    coins = cObj.fetchall()

    
    def font_color(amount):
        if amount > 0:
            return "green"
        else:
            return "red"

    def insert_coin():
        cObj.execute("INSERT INTO Coin(symbol,price,amount) values(?,?,?)",(symbol_txt.get(),price_txt.get(),amount_txt.get()))
        con.commit()


#    coins = [
#        
#        {
#            'symbol':'BTC',
#            'amount_owned':2,
#            'price_per_coin': 2700
#        },
#        {
#            'symbol':'EOS',
#            'amount_owned':100,
#            'price_per_coin': 1.5
#        },
#        {
#            'symbol':'LTC',
#            'amount_owned':55,
#           'price_per_coin': 75.5
#        },
#        {
#            'symbol':'XMR',
#            'amount_owned':40,
#            'price_per_coin': 15.9
#        }
#    ]


    total_pl = 0
    idx_row = 1 #its use to increment th row index
    total_curr_amount = 0
    total_paid = 0

    for idx in range(0,300):
        for coin in coins:
            if coin[1] == (api["data"][idx]['symbol']):
                total_amount = coin[2] * coin[3]
                curr_amount=coin[2] * (api['data'][idx]['quote']['USD']['price'])
                P_L_percoin = (api['data'][idx]['quote']['USD']['price']) - coin[3]
                total_p_lcoin = P_L_percoin * coin[2]
                
                total_curr_amount +=  curr_amount
                total_paid +=total_amount
                total_pl += total_p_lcoin

#                print(api["data"][idx]['name'] + " => " + api["data"][idx]['symbol'])
#                print("price is : " + "$ {0:.2f}".format(api["data"][idx]['quote']['USD']['price']))
#                print("Total paid amount is => ","$ {0:.2f}".format(total_amount))
#                print("Current amount of coin => ","$ {0:.2f}".format(curr_amount))
#                print("You have Profit / loss per coin => ","$ {0:.2f}".format(P_L_percoin))
#                print("Total profit/loss is => ","$ {0:.2f}".format(total_p_lcoin))
#                print("-------------------------------------------------")
 
                portid = Label(guitk,text=coin[0],bg='snow',fg='black' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
                portid.grid(row=idx_row,column=0,sticky=N+S+E+W)

                name = Label(guitk,text=api["data"][idx]['symbol'],bg='snow',fg='black' ,font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                name.grid(row=idx_row,column=1,sticky=N+S+E+W)

                price = Label(guitk,text="$ {0:.2f}".format(api["data"][idx]['quote']['USD']['price']),bg='snow',fg='black',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                price.grid(row=idx_row,column=2,sticky=N+S+E+W)

                amountofcoin = Label(guitk,text=coin[2],bg='snow',fg='black',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                amountofcoin.grid(row=idx_row,column=3,sticky=N+S+E+W)

                paidamount = Label(guitk,text="$ {0:.2f}".format(total_amount),bg='snow',fg='black',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                paidamount.grid(row=idx_row,column=4,sticky=N+S+E+W)

                curramount = Label(guitk,text="$ {0:.2f}".format(curr_amount),bg='snow',fg='black',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                curramount.grid(row=idx_row,column=5,sticky=N+S+E+W)

                plpercoin = Label(guitk,text="$ {0:.2f}".format(P_L_percoin),bg='snow',fg=font_color(float("{0:.2f}".format(P_L_percoin))),font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                plpercoin.grid(row=idx_row,column=6,sticky=N+S+E+W)

                totalpl = Label(guitk,text="$ {0:.2f}".format(total_p_lcoin),bg='snow',fg=font_color(float("{0:.2f}".format(total_p_lcoin))),font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
                totalpl.grid(row=idx_row,column=7,sticky=N+S+E+W)

                idx_row +=1
                
    #print("Overall profit/loss is = > ","$ {0:.3f}".format(total_pl))
    

    #insert  data

    symbol_txt=Entry(guitk,borderwidth=3,relief='groove')
    symbol_txt.grid(row=idx_row+1,column=1,sticky=N+S+E+W)

    price_txt=Entry(guitk,borderwidth=3,relief='groove')
    price_txt.grid(row=idx_row+1,column=2,sticky=N+S+E+W)

    amount_txt=Entry(guitk,borderwidth=3,relief='groove')
    amount_txt.grid(row=idx_row+1,column=3,sticky=N+S+E+W)

    addcoin = Button(guitk,text="Add Coin",bg='Black',fg="snow",command=insert_coin, font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
    addcoin.grid(row=idx_row+1,column=4,sticky=N+S+E+W) 



    total_curramt = Label(guitk,text="$ {0:.3f}".format(total_curr_amount),bg='Black',fg='snow',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
    total_curramt.grid(row=idx_row,column=4,sticky=N+S+E+W)

    total_paidam = Label(guitk,text="$ {0:.3f}".format(total_paid),bg='Black',fg='snow',font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
    total_paidam.grid(row=idx_row,column=5,sticky=N+S+E+W)

    total_pl = Label(guitk,text="$ {0:.3f}".format(total_pl),bg='Black',fg=font_color(float(" {0:.3f}".format(total_pl))),font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
    total_pl.grid(row=idx_row,column=7,sticky=N+S+E+W)  
    

    api = ""

    refresh = Button(guitk,text="R e f r e s h",bg='Black',fg="snow",command=My_code , font="lato 12",padx='5',pady='5',borderwidth=3,relief='groove')
    refresh.grid(row=idx_row+1,column=7,columnspan = 8,sticky=N+S+E+W)  


def app_header():

    port_id = Label(guitk,text='Portfolio ID',bg='black',fg='bisque' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    port_id.grid(row=0,column=0,sticky=N+S+E+W)

    name = Label(guitk,text='Coin name',bg='black',fg='bisque' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    name.grid(row=0,column=1,sticky=N+S+E+W)

    price = Label(guitk,text='Price of coin',bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    price.grid(row=0,column=2,sticky=N+S+E+W)

    amountofcoin = Label(guitk,text='Amount of coin',bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    amountofcoin.grid(row=0,column=3,sticky=N+S+E+W)

    paidamount = Label(guitk,text='Total Paid Amount',bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    paidamount.grid(row=0,column=4,sticky=N+S+E+W)

    curramount = Label(guitk,text='Current Price of coin',bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    curramount.grid(row=0,column=5,sticky=N+S+E+W)

    plpercoin = Label(guitk,text='P/L per coin',bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    plpercoin.grid(row=0,column=6,sticky=N+S+E+W)

    totalpl = Label(guitk,text="Total P / L",bg='black',fg='bisque',font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    totalpl.grid(row=0,column=7,sticky=N+S+E+W)

app_header()
My_code() # call function
guitk.mainloop()
print("Done")

cObj.close()
con.close()