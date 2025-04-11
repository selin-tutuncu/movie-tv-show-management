import json
import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkFont

# Kullanıcı bilgilerini saklamak için dosya adı
def ana_pencere():
    import json
    import tkinter as tk
    from tkinter import messagebox, ttk
    import tkinter.font as tkFont

    def dosyayi_oku():
        with open("verile.json", "r") as json_dosyasi:
            veriler = json.load(json_dosyasi)
            json_dosyasi.close()
        return veriler

    def dosyaya_yaz(veriler):
        with open("veriler.json", "w") as json_dosyasi:
            json.dump(veriler, json_dosyasi)
            json_dosyasi.close()

    def listele(menu_tur, menu_durum):
        if (menu_tur.get() == "Veri Turunu Seciniz:"):
            messagebox.showinfo("Mesaj!", "Listelemek İçin Veri Türünü Doldurarak Listeleyebilirsiniz")
            return

        if (menu_durum.get() == "Veri Durumunu Seciniz:"):
            messagebox.showinfo("Mesaj!", "Listelemek İçin Veri Durumunu Doldurarak Listeleyebilirsiniz")
            return

        for item in tree.get_children():
            tree.delete(item)
        i = 0
        veriler = dosyayi_oku()
        for veri in veriler:
            i += 1
            if (menu_tur.get() == "Hepsi" and menu_durum.get() == "Hepsi"):
                tree.insert("", "end", text=str(i),
                            values=(veri["Ad"], veri["Tur"], veri["Durum"], veri["Yildiz"], veri["Not"]))
            if (menu_tur.get() == "Hepsi" and menu_durum.get() != "Hepsi"):
                if (veri["Durum"] == menu_durum.get()):
                    tree.insert("", "end", text=str(i),
                                values=(veri["Ad"], veri["Tur"], veri["Durum"], veri["Yildiz"], veri["Not"]))
            if (menu_tur.get() != "Hepsi" and menu_durum.get() == "Hepsi"):
                if (veri["Tur"] == menu_tur.get()):
                    tree.insert("", "end", text=str(i),
                                values=(veri["Ad"], veri["Tur"], veri["Durum"], veri["Yildiz"], veri["Not"]))
            if (menu_tur.get() != "Hepsi" and menu_durum.get() != "Hepsi"):
                if (veri["Tur"] == menu_tur.get() and veri["Durum"] == menu_durum.get()):
                    tree.insert("", "end", text=str(i),
                                values=(veri["Ad"], veri["Tur"], veri["Durum"], veri["Yildiz"], veri["Not"]))

    def duzenle(tree, svar_anapencere2, svar_anapencere1):
        secili_eleman = tree.focus()
        if (secili_eleman == ""):
            messagebox.showerror("Hata!", "Duzenlemek İcin Tablodan Veri Secmelisiniz!!")
            return
        secilen_veri = tree.item(secili_eleman)
        index = int(secilen_veri["text"])
        veriler = dosyayi_oku()
        for i in range(0, len(veriler)):
            if (index == i + 1):
                font_style = tkFont.Font(family="Tahoma", size=10, weight="bold")
                pencere_ekle = tk.Toplevel()
                pencere_ekle.geometry("300x300")
                label_ad = tk.Label(pencere_ekle, text="FİLM ADI:", font=font_style)
                label_ad.place(x=10, y=10)

                entry_ad = tk.Entry(pencere_ekle)
                entry_ad.place(x=70, y=10)
                entry_ad.insert(0, veriler[i]["Ad"])

                label_tur = tk.Label(pencere_ekle, text="TÜR", font=font_style)
                label_tur.place(x=10, y=40)

                label_durum = tk.Label(pencere_ekle, text="DURUM:", font=font_style)
                label_durum.place(x=10, y=70)

                label_yildiz = tk.Label(pencere_ekle, text="YILDIZ:", font=font_style)
                label_yildiz.place(x=10, y=100)

                entry_yildiz = tk.Entry(pencere_ekle)
                entry_yildiz.place(x=70, y=100)
                entry_yildiz.insert(0, veriler[i]["Yildiz"])

                label_not = tk.Label(pencere_ekle, text="NOT:", font=font_style)
                label_not.place(x=10, y=130)

                entry_not = tk.Entry(pencere_ekle)
                entry_not.place(x=70, y=130)
                entry_not.insert(0, veriler[i]["Not"])

                svar1 = tk.StringVar()
                svar1.set(veriler[i]["Durum"])
                menuDurum = tk.OptionMenu(pencere_ekle, svar1, "Izlendi", "Izlenecek", "Bekleniyor")
                menuDurum.place(x=70, y=65)

                svar2 = tk.StringVar()
                svar2.set(veriler[i]["Tur"])
                menuTur = tk.OptionMenu(pencere_ekle, svar2, "Film", "Dizi")
                menuTur.place(x=70, y=35)
                buton_degistir = tk.Button(pencere_ekle, text="Değiştir",
                                           command=lambda: ekle(entry_ad, svar2, svar1, entry_yildiz, entry_not,
                                                                svar_anapencere2, svar_anapencere1, i), font=font_style)
                buton_degistir.place(x=40, y=160)
                return

    def sil(tree, svar_anapencere2, svar_anapencere1):
        secili_eleman = tree.focus()
        if (secili_eleman == ""):
            messagebox.showerror("Hata!", "Silmek İcin Tablodan Veri Secmelisiniz!!")
            return
        secilen_veri = tree.item(secili_eleman)
        index = int(secilen_veri["text"])
        veriler = dosyayi_oku()
        for i in range(0, len(veriler)):
            if (index == i + 1):
                veriler.pop(i)
                dosyaya_yaz(veriler)
                listele(svar_anapencere2, svar_anapencere1)
                messagebox.showinfo("Bilgilendirme", "Veri Basarili bir sekilde silindi")
                return

    def ekle(entry_ad, entry_tur, entry_durum, entry_yildiz, entry_not, svar_anapencere2, svar_anapencere1, mode):

        veriler = dosyayi_oku()
        if (entry_ad.get() == ""):
            messagebox.showerror("Hata!", "Ad Kısmı Boş Bırakılmamalı")
            return

        if (entry_tur.get() == "Seciniz:"):
            messagebox.showerror("Hata!", "Tür Kısmı Boş Bırakılmamalı")
            return

        if (entry_durum.get() == "Seciniz:"):
            messagebox.showerror("Hata!", "Durum Kismi Bos Birakilmamamli")
            return

        if (
                entry_yildiz.get() != "1" and entry_yildiz.get() != "2" and entry_yildiz.get() != "3" and entry_yildiz.get() != "4" and entry_yildiz.get() != "5" and entry_yildiz.get().strip() != ""):
            messagebox.showerror("Hata!", "yildiz puani 1-5 arasinda bir tamsayi olmali")
        if (entry_yildiz.get().strip() == ""):
            pass

        elif (int(entry_yildiz.get()) > 5 or int(entry_yildiz.get()) < 1) and (entry_yildiz.get().strip() != ""):
            messagebox.showerror("Hata!", "yildiz puani 1-5 arasinda bir tamsayi olmali")
            return

        veri = {"Ad": entry_ad.get(),
                "Tur": entry_tur.get(),
                "Durum": entry_durum.get(),
                "Yildiz": entry_yildiz.get(),
                "Not": entry_not.get()
                }
        if mode == -1:
            veriler.append(veri)
            dosyaya_yaz(veriler)
            messagebox.showinfo("Başarili!", "Veri Basarılı Bir Şekilde Eklendi!!")
            listele(svar_anapencere2, svar_anapencere1)
        else:
            veriler[mode] = veri
            dosyaya_yaz(veriler)
            messagebox.showinfo("Başarili!", "Veri Basarılı Bir Şekilde Degistirildi!!")
            listele(svar_anapencere2, svar_anapencere1)

    def yeniveriekleme(svar_anapencere2, svar_anapencere1):
        font_style = tkFont.Font(family="Tahoma", size=10, weight="bold")
        pencere_ekle = tk.Toplevel()
        pencere_ekle.geometry("300x300")
        label_ad = tk.Label(pencere_ekle, text="FİLM ADI:", font=font_style)
        label_ad.place(x=1, y=10)

        entry_ad = tk.Entry(pencere_ekle)
        entry_ad.place(x=70, y=10)

        label_tur = tk.Label(pencere_ekle, text="TÜR:", font=font_style)
        label_tur.place(x=12, y=40)

        label_durum = tk.Label(pencere_ekle, text="DURUM:", font=font_style)
        label_durum.place(x=4, y=70)

        label_yildiz = tk.Label(pencere_ekle, text="YILDIZ:", font=font_style)
        label_yildiz.place(x=3, y=100)

        entry_yildiz = tk.Entry(pencere_ekle)
        entry_yildiz.place(x=70, y=100)

        label_not = tk.Label(pencere_ekle, text="NOT:", font=font_style)
        label_not.place(x=12, y=130)

        entry_not = tk.Entry(pencere_ekle)
        entry_not.place(x=70, y=130)

        buton_ekle = tk.Button(pencere_ekle, text="Ekle",
                               command=lambda: ekle(entry_ad, svar2, svar1, entry_yildiz, entry_not, svar_anapencere2,
                                                    svar_anapencere1, -1), font=font_style)
        buton_ekle.place(x=40, y=160)

        svar1 = tk.StringVar()
        svar1.set("Seciniz:")
        menuDurum = tk.OptionMenu(pencere_ekle, svar1, "Izlendi", "Izlenecek", "Bekleniyor")
        menuDurum.place(x=70, y=65)

        svar2 = tk.StringVar()
        svar2.set("Seciniz:")
        menuTur = tk.OptionMenu(pencere_ekle, svar2, "Film", "Dizi")
        menuTur.place(x=70, y=35)

    pencere = tk.Tk()
    pencere.geometry("1350x500")
    pencere.configure(bg="#add8e6")  # Arka plan rengi

    tree = ttk.Treeview(pencere)
    tree.place(x=300, y=10, width=800, height=400)
    tree["columns"] = ("Ad", "Tur", "Durum", "Yildiz", "Not")
    tree.column("#0", width=50)  # Ana sütun (isim sütunu)
    tree.column("Ad", width=150)
    tree.column("Tur", width=100)
    tree.column("Durum", width=80)
    tree.column("Yildiz", width=80)
    tree.column("Not", width=300)

    # Sütun başlıklarını ayarlama
    tree.heading("#0", text="ID")
    tree.heading("Ad", text="Ad")
    tree.heading("Tur", text="Tur")
    tree.heading("Durum", text="Durum")
    tree.heading("Yildiz", text="Yildiz")
    tree.heading("Not", text="Not")

    # def secilen_eleman(tree):
    #     print(tree.item(tree.focus()))                                                     deneme kısmi

    # button1=tk.Button(pencere,text="Deneme",command=lambda:secilen_eleman(tree))
    # button1.place(x=1200,y=200)
    svar_anapencere1 = tk.StringVar()
    svar_anapencere1.set("Veri Durumunu Seciniz:")
    menuDurum = tk.OptionMenu(pencere, svar_anapencere1, "Izlendi", "Izlenecek", "Bekleniyor", "Hepsi")
    menuDurum.place(x=70, y=65)
    menuDurum["menu"].configure(bg="#add8e6")
    font_style1 = tkFont.Font(family="Verdana", size=9, weight="bold")
    font_style2 = tkFont.Font(family="Verdana", size=9, weight="normal")
    menuDurum.config(font=font_style1)

    svar_anapencere2 = tk.StringVar()
    svar_anapencere2.set("Veri Turunu Seciniz:")
    menuTur = tk.OptionMenu(pencere, svar_anapencere2, "Film", "Dizi", "Hepsi")
    menuTur.place(x=70, y=35)
    buton_listele = tk.Button(pencere, text="Listele", command=lambda: listele(svar_anapencere2, svar_anapencere1),
                              font=font_style1)
    buton_listele.place(x=120, y=108)
    menuTur["menu"].configure(bg="#add8e6")
    menuTur.config(font=font_style1)

    buton_yeniveri = tk.Button(pencere, text="Yeni Veri Ekle",
                               command=lambda: yeniveriekleme(svar_anapencere2, svar_anapencere1), font=font_style2)
    buton_yeniveri.place(x=1176, y=35)

    buton_sil = tk.Button(pencere, text="Veri sil", command=lambda: sil(tree, svar_anapencere2, svar_anapencere1),
                          font=font_style2)
    buton_sil.place(x=1175, y=65)

    buton_duzenle = tk.Button(pencere, text="Duzenle",
                              command=lambda: duzenle(tree, svar_anapencere2, svar_anapencere1), font=font_style2)
    buton_duzenle.place(x=1175, y=108)

    # Kullanıcının bir film veya dizi adı girerek arama yapabilmesini sağlamak
    def ara(entry_ara, tree):
        arama_metni = entry_ara.get().strip().lower()
        if not arama_metni:
            messagebox.showinfo("Uyarı", "Lütfen bir arama terimi giriniz!")
            return

        for item in tree.get_children():
            tree.delete(item)

        veriler = dosyayi_oku()
        i = 0
        for veri in veriler:
            if arama_metni in veri["Ad"].lower():
                i += 1
                tree.insert("", "end", text=str(i),
                            values=(veri["Ad"], veri["Tur"], veri["Durum"], veri["Yildiz"], veri["Not"]))

    # arama kutusunu guı ye eklemek
    entry_ara = tk.Entry(pencere)
    entry_ara.place(x=70, y=180)
    buton_ara = tk.Button(pencere, text="Ara", command=lambda: ara(entry_ara, tree), font=font_style1)
    buton_ara.place(x=220, y=177)

    # toplam izlenen film/dizi sayısını göstermek
    def raporla():
        veriler = dosyayi_oku()
        toplam_izlenen = sum(1 for veri in veriler if veri["Durum"] == "Izlendi")
        messagebox.showinfo("Rapor", f"Toplam izlenen içerik sayısı: {toplam_izlenen}")

    # raporlama butonu
    buton_rapor = tk.Button(pencere, text="Raporla", command=raporla, font=font_style1)
    buton_rapor.place(x=1175, y=177)

    pencere.mainloop()


DOSYA_ADI = "kullanici_verileri.json"

# Kullanıcı verilerini yükle
def kullanici_verilerini_yukle():
    try:
        with open(DOSYA_ADI, "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}  # Dosya yoksa boş bir sözlük döner
    except json.JSONDecodeError:
        return {}  # JSON formatında sorun varsa boş bir sözlük döner

# Kullanıcı verilerini kaydet
def kullanici_verilerini_kaydet():
    with open(DOSYA_ADI, "w") as dosya:
        json.dump(kullanici_sifreler, dosya, indent=4)

# Kullanıcı verilerini yükle ve başlat
kullanici_sifreler = kullanici_verilerini_yukle()

# Kullanıcı adı ve şifre doğrulama
def kullanici_dogrula(kullanici_ad, sifre):
    if kullanici_ad in kullanici_sifreler and kullanici_sifreler[kullanici_ad] == sifre:
        return True
    return False

# Yeni kullanıcı ekleme
def yeni_kullanici_ekle(kullanici_ad, sifre):
    if kullanici_ad in kullanici_sifreler:
        return False  # Kullanıcı zaten kayıtlı
    kullanici_sifreler[kullanici_ad] = sifre
    kullanici_verilerini_kaydet()  # Dosyaya kaydet
    return True

def kayit_ekrani():
    pencere_kayit = tk.Toplevel()
    pencere_kayit.geometry("400x350")
    pencere_kayit.title("Kayıt Ol")
    pencere_kayit.configure(bg="#f0f8ff")

    kayit_font = tkFont.Font(family="Arial", size=12, weight="bold")

    # Kullanıcı Adı Etiketi ve Giriş
    tk.Label(
        pencere_kayit, text="Kullanıcı Adı:", font=kayit_font, bg="#f0f8ff", fg="#000080"
    ).place(relx=0.2, rely=0.2)
    entry_kullanici = tk.Entry(pencere_kayit, font=("Arial", 10))
    entry_kullanici.place(relx=0.5, rely=0.21)

    # Şifre Etiketi ve Giriş
    tk.Label(
        pencere_kayit, text="Şifre:", font=kayit_font, bg="#f0f8ff", fg="#000080"
    ).place(relx=0.2, rely=0.31)
    entry_sifre = tk.Entry(pencere_kayit, show="*", font=("Arial", 10))
    entry_sifre.place(relx=0.5, rely=0.32)

    # Şifre Onayı Etiketi ve Giriş
    tk.Label(
        pencere_kayit, text="Şifre Onayı:", font=kayit_font, bg="#f0f8ff", fg="#000080"
    ).place(relx=0.2, rely=0.40)
    entry_sifre_onay = tk.Entry(pencere_kayit, show="*", font=("Arial", 10))
    entry_sifre_onay.place(relx=0.5, rely=0.41)

    # Kayıt Ol Fonksiyonu
    def kayit_ol():
        kullanici_ad = entry_kullanici.get()
        sifre = entry_sifre.get()
        sifre_onay = entry_sifre_onay.get()

        if not kullanici_ad or not sifre or not sifre_onay:
            messagebox.showerror("Hata", "Tüm alanları doldurunuz!")
            return

        if sifre != sifre_onay:
            messagebox.showerror("Hata", "Şifreler birbiriyle uyuşmuyor!")
            return

        if yeni_kullanici_ekle(kullanici_ad, sifre):
            messagebox.showinfo("Başarılı", "Kayıt başarıyla tamamlandı!")
            pencere_kayit.destroy()
        else:
            messagebox.showerror("Hata", "Bu kullanıcı zaten kayıtlı!")

    # Kayıt Ol Butonu
    tk.Button(
        pencere_kayit,
        text="Kayıt Ol",
        font=kayit_font,
        bg="#4682b4",
        fg="white",
        command=kayit_ol,
    ).place(relx=0.4, rely=0.6)

# Örnek kullanımı: kayit_ekrani()



def giris_ekrani():
    pencere_giris = tk.Tk()
    pencere_giris.geometry("800x500")
    pencere_giris.title("Kullanıcı Girişi")
    pencere_giris.configure(bg="#f0f8ff")

    giris_font_style1 = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
    giris_font_style2 = tkFont.Font(family="Arial", size=12, weight="bold")

    tk.Label(
        pencere_giris,
        text="Kullanıcı Adı:",
        font=giris_font_style1,
        bg="#f0f8ff",
        fg="#000080"
    ).place(relx=0.35, rely=0.35)
    entry_kullanici = tk.Entry(pencere_giris, font=("Arial", 10))
    entry_kullanici.place(relx=0.485, rely=0.36)

    tk.Label(
        pencere_giris,
        text="Şifre:",
        font=giris_font_style1,
        bg="#f0f8ff",
        fg="#000080"
    ).place(relx=0.39, rely=0.45)
    entry_sifre = tk.Entry(pencere_giris, show="*", font=("Arial", 10))
    entry_sifre.place(relx=0.485, rely=0.46)

    def giris_yap():
        kullanici_ad = entry_kullanici.get()
        sifre = entry_sifre.get()
        if kullanici_dogrula(kullanici_ad, sifre):
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            pencere_giris.destroy()
            ana_pencere()
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")

    tk.Button(
        pencere_giris,
        text="Giriş Yap",
        font=giris_font_style2,
        bg="#4682b4",
        fg="white",
        command=giris_yap
    ).place(relx=0.485, rely=0.55)

    tk.Button(
        pencere_giris,
        text="Kayıt Ol",
        font=giris_font_style2,
        bg="#32cd32",
        fg="white",
        command=kayit_ekrani
    ).place(relx=0.485, rely=0.65)

    pencere_giris.mainloop()

# Uygulama Başlat
giris_ekrani()