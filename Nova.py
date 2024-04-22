import tkinter
import tkinter as tk
from gtts import gTTS
import wikipedia
import random
import pygame
from PIL import Image, ImageTk


window = tk.Tk()
window.geometry("1100x700+240+30")
window.attributes('-fullscreen', False)
window.resizable(False, False)
window.title("Nova: Bilgi Kütüphanesi")


image = Image.open("wp.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)



def web_search():
    user_istem = istem.get("1.0", tk.END).strip()
    print("Kullanıcı istemi: ", user_istem)
    gecmis.append(user_istem)
    son_arananlar.config(text=gecmis)
    try:
        wikipedia.set_lang("tr")
        page = wikipedia.page(user_istem)
        summary = page.summary[:2450]
        istem_cvp.config(text=summary)
        ses(summary)
        print("İstem Cevap: ", summary)
    except wikipedia.exceptions.PageError:
        istem_cvp.config(text="Aradığınız konu bulunamadı.")


def ses(text):
    tts = gTTS(text=text, lang="tr")
    pygame.mixer.init()
    tts.save("metin.mp3")
    ses1 = pygame.mixer.Sound("metin.mp3")
    ses1.play()


def gelistirici_hakkinda():
    hakkinda_window = tk.Toplevel()
    hakkinda_window.geometry("700x500+430+150")
    hakkinda_window.attributes('-fullscreen', False)
    hakkinda_window.resizable(False, False)
    hakkinda_window.title("NOVA: Geliştirici Bilgileri")


def ayarlar():
    ayarlar_window = tk.Toplevel()
    ayarlar_window.geometry("700x500+430+150")
    ayarlar_window.attributes('-fullscreen', False)
    ayarlar_window.resizable(False, False)
    ayarlar_window.title("NOVA: Ayarlar")

    settings_text = tk.Label(ayarlar_window, text="Ayarlar", font=("arial", 17 ,"bold"))
    settings_text.place(x=20, y=20)
    settings_cizgi = tk.Label(ayarlar_window, text="___________________________________________________________________________________________________________________________________________")
    settings_cizgi.config(fg="gray")
    settings_cizgi.place(x=0, y=50)

    info_text = tk.Label(ayarlar_window, text="Metin Boyutu")
    info_text.place(x=20, y=100)

    def metin_byt():
        byt = int(font_size_box.get())
        istem_cvp.config(font=("arial", byt))

    font_size_box = tk.Spinbox(ayarlar_window, from_=0, to=100, command=metin_byt )
    font_size_box.place(x=22, y=130)

    info_text2 = tk.Label(ayarlar_window, text="Metin Rengi")
    info_text2.place(x=20, y=170)

    def metin_rengi():
        def fg_color_black():
            istem_cvp.config(fg="black")
        def fg_color_red():
            istem_cvp.config(fg="red")
        def fg_color_blue():
            istem_cvp.config(fg="blue")
        def fg_color_green():
            istem_cvp.config(fg="green")

        font_color_black = tk.Button(ayarlar_window, text="Siyah", fg="black", command=fg_color_black, width=6)
        font_color_black.place(x=20, y=200)
        font_color_red = tk.Button(ayarlar_window, text="Kırmızı", fg="red", command=fg_color_red, width=6)
        font_color_red.place(x=20, y=230)
        font_color_blue = tk.Button(ayarlar_window, text="Mavi", fg="blue", command=fg_color_blue, width=6)
        font_color_blue.place(x=20, y=260)
        font_color_green = tk.Button(ayarlar_window, text="Yeşil", fg="green", command=fg_color_green, width=6)
        font_color_green.place(x=20, y=290)

    metin_rengi()

    def metin_arka_plan_rengi():
        def bg_color_black():
            istem_cvp.config(bg="black")
        def bg_color_red():
            istem_cvp.config(bg="red")
        def bg_color_blue():
            istem_cvp.config(bg="blue")
        def bg_color_green():
            istem_cvp.config(bg="green")

        color_black = tk.Button(ayarlar_window, text="Siyah", fg="black", command=bg_color_black, width=6)
        color_black.place(x=100, y=200)
        color_red = tk.Button(ayarlar_window, text="Kırmızı", fg="red", command=bg_color_red, width=6)
        color_red.place(x=100, y=230)
        color_blue = tk.Button(ayarlar_window, text="Mavi", fg="blue", command=bg_color_blue, width=6)
        color_blue.place(x=100, y=260)
        color_green = tk.Button(ayarlar_window, text="Yeşil", fg="green", command=bg_color_green, width=6)
        color_green.place(x=100, y=290)

    metin_arka_plan_rengi()


def gelistirici_ayarlari():
    gelistirici_ayarlari_window = tk.Toplevel()
    gelistirici_ayarlari_window.geometry("700x500+430+150")
    gelistirici_ayarlari_window.attributes('-fullscreen', False)
    gelistirici_ayarlari_window.resizable(False, False)
    gelistirici_ayarlari_window.title("NOVA: Geliştirici Ayarları")

def yeniler():
    yeniler_window = tk.Toplevel()
    yeniler_window.geometry("700x500+430+150")
    yeniler_window.attributes('-fullscreen', False)
    yeniler_window.resizable(False, False)
    yeniler_window.title("NOVA: Yeni Özellikler")

menu_frame = tk.Frame(window)
menu_frame.pack()

menu_bar = tk.Menu(menu_frame)
window.config(menu=menu_bar)

yeniler_bar = tk.Frame(window)
yeniler_bar.pack()

ayarlar_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayarlar", menu=ayarlar_menu)

ayarlar_menu.add_command(label="Ayarlar", command=ayarlar)
ayarlar_menu.add_command(label="Geliştirici Ayarları", command=gelistirici_ayarlari)

gelistirici_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Hakkında", menu=gelistirici_menu)

gelistirici_menu.add_command(label="Geliştirici Hakkında", command=gelistirici_hakkinda)

menu_frame.place(x=100, y=50)
yeniler_bar.place(x=100, y=50)

yeniler_menu = tk.Menu(yeniler_bar, tearoff=0)
menu_bar.add_cascade(label="Yeni Özellikler", menu=yeniler_menu)
yeniler_menu.add_command(label="En Yeniler", command=yeniler)

istem = tk.Text(window, bg="light gray", width=100, height=1, font=("arial",11))
istem.place(x=170, y=613)

istem_buton = tk.Button(window, text="Konuş", command=web_search)
istem_buton.place(x=977, y=610)


istem_oneri = ["Eyfel Kulesi", "İstiklal Marşı", "Boğaziçi Üniversitesi", "Yapay Zeka", "Python Programlama Dili", "OpenAI", "Filistin Devleti", "İklim Değişikliği", "Yönetim Bilişim Sistemleri", "Yök", "Erasmus Programı", "Müzik Önerisi", "Alper Gezeravcı", "Teknofest", "Orta Doğu", "İran", "Demir Kubbe"]
istem_oneri_random = "Şunu Aramayı Deneyin: " + random.choice(istem_oneri)
istem_öneri_text = tk.Label(window, text=(istem_oneri_random), fg="red", bg="white")
istem_öneri_text.place(x=196, y=587)

istem_cvp = tk.Label(window,  text="", wraplength=600, justify="left", font=("arial, 11"), bg="white", )
istem_cvp.place(x=240, y=50)


gecmis = []
son_arananlar_info = tk.Label(window, text="Son Arananlar:", fg="purple", bg="white", font="bold,11" )
son_arananlar_info.place(x=45, y=45)
son_arananlar = tk.Label(window, text=gecmis, bg="white", fg="black", wraplength=130)
son_arananlar.place(x=20, y=80)


alt_bilgi = tk.Label(window, text="Lütfen Nova'nın Geliştirme Aşamasında Olduğunu ve Bazı Özelliklerinin Kararsız yapıda olabileceğini Unutmayın!", fg="gray", bg="white")
alt_bilgi.place(x=260, y=655)

window.mainloop()
