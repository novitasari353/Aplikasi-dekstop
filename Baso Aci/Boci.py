
from PIL import ImageTk,Image
import Tkinter
from Tkinter import Toplevel
from cassandra.cluster import Cluster


def start():
    window = Tkinter.Tk()
    desktop = RegisUser(window)
    window.mainloop()

class Model:
    def __init__(self):
        self.cluster = cluster

    def list():
        cluster = Cluster(['127.0.0.1'], port = 9042)
        session = cluster.connect()

class RegisUser:
    def __init__(self, jendela):
        self.jendela = jendela
        self.jendela.title("Baso Aci Asik")
        self.jendela.geometry("600x700")

        self.hallo = Tkinter.Label(self.jendela, text = "Selamat Datang di Baso Aci Asik")
        self.hallo.config(font=("algerian", 20))
        self.hallo.place(x = 80, y = 40)
        
        self.img = ImageTk.PhotoImage(file="C:/Python27/bociiiiiii.jpeg")
        self.display = Tkinter.Label(self.jendela, image=self.img,)
        self.display.place(x= 150, y = 150)

        self.reg = Tkinter.Button(self.jendela, text = "Register",fg = "blue", width = 20,
                                          command = self.user)
        self.reg.config(font=("Calibri", 12))
        self.reg.place(x = 200, y = 450)

        self.tombolKeluar = Tkinter.Button(self.jendela, text = "Keluar", width = 10,
                                           command = self.jendela.destroy)
        self.tombolKeluar.config(font=("Calibri", 12))
        self.tombolKeluar.place(x = 20, y = 550)

   

    def user(self):
        self.jendelaBaru = Toplevel(self.jendela)
        self.app=UserView(self.jendelaBaru)

        self.labelayo = Tkinter.Label(self.jendelaBaru, text = "Yuk Register Dulu !!", fg = "Blue")
        self.labelayo.config(font =( "calibri", 15))
        self.labelayo.place(x= 180, y = 100)
                
        self.labelUsername = Tkinter.Label(self.jendelaBaru, text = "Username")
        self.labelUsername.config(font=("calibri", 15))
        self.labelUsername.place(x = 200, y = 200)
        self.entryUsername = Tkinter.Entry(self.jendelaBaru, width= 30)
        self.entryUsername.place(x = 170, y = 250)

        self.labelPassword = Tkinter.Label(self.jendelaBaru, text = "Password")
        self.labelPassword.config(font=("calibri", 15))
        self.labelPassword.place(x = 200, y = 300)
        self.entryPassword = Tkinter.Entry(self.jendelaBaru, width = 30)
        self.entryPassword.place(x = 170, y = 350)

        self.tblregis = Tkinter.Button(self.jendelaBaru, text = "Register",width = 10,
                                       command = self.menunya)
        self.tblregis.config(font=("calibri", 12))
        self.tblregis.place(x = 200, y = 400)

        self.tombolKeluar = Tkinter.Button(self.jendelaBaru, text = "Keluar", width = 10,
                                           command = self.jendela.destroy)
        self.tombolKeluar.config(font=("calibri", 12))
        self.tombolKeluar.place(x = 20, y = 550)

    def menunya(self):
        self.jendelaBaru1 = Toplevel(self.jendela)
        self.app = Menu(self.jendelaBaru1)

        self.labelisi = Tkinter.Label(self.jendelaBaru1, text ="Isi baso aci", bg = "sky blue")
        self.labelisi.config(font=("calibri", 14))
        self.labelisi.place (x= 10, y = 40)
        self.isian = Tkinter.Label(self.jendelaBaru1, text = "Cilok \n Cuankie Lidah \n Sukro \n Batagor Kering \n Bumbu Instant \n \n")
        self.isian.config(font=("calibri", 13))
        self.isian.place(x= 150, y = 40)

        self.img = ImageTk.PhotoImage(file="C:/Python27/isiboci.jpeg")
        self.display = Tkinter.Label(self.jendelaBaru1, image=self.img,)
        self.display.place(x= 300, y = 80)

        self.rasa = Tkinter.Label(self.jendelaBaru1, text ="Varian Rasa", bg = "sky blue")
        self.rasa.config(font=("calibri", 14))
        self.rasa.place (x= 10, y = 200)
        self.rasanya = Tkinter.Label(self.jendelaBaru1, text = "Original \n Sambal Geprek \n Kuah Tomyam  \n \n")
        self.rasanya.config(font=("calibri", 13))
        self.rasanya.place(x= 150, y = 200)

        self.cara = Tkinter.Label(self.jendelaBaru1, text ="Cara Pesan", bg = "sky blue")
        self.cara.config(font=("calibri", 14))
        self.cara.place (x= 10, y = 350)
        self.pesan = Tkinter.Label(self.jendelaBaru1, text = "Kirimkan pesananmu melalui Whatsapp ke nomor \n 085694760270 dengan format: \n Nama \n No Hp \n Alamat \n Banyak Pesanan \n Varian rasa yang dipilih")
        self.pesan.config(font=("calibri", 13))
        self.pesan.place(x= 150, y = 350)
        
        self.tombolKeluar = Tkinter.Button(self.jendelaBaru1, text = "Keluar", width = 10,
                                           command = self.jendela.destroy)
        self.tombolKeluar.config(font=("calibri", 12))
        self.tombolKeluar.place(x = 20, y = 550)


class UserView:
    def __init__(self,jendela):
        self.jendela = jendela
        self.jendela.title("Register")
        self.jendela.geometry("500x650")
        

class Menu:
    def __init__(self,jendela):
         self.jendela = jendela
         self.jendela.title("Boci")
         self.jendela.geometry("600x700")


        
if __name__ == '__main__':
    start()
