import tkinter as tk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


class Accordion(tk.Frame):
    def __init__(self, parent, bg=None, width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.configure(bg=bg)

        self.id = 0
        self.options_values = {}
        self.options = []

        self.pack()

    def add_option(self, option, value, fg_o, bg_o, font_o, font_v, wraplength=350, bg_v="#242e38", fg_v="#edebed"):

        option_frame = tk.Frame(self, bg=bg)

        option_label = tk.Label(option_frame, text=option, font=font_o, fg=fg_o, bg=bg_o, width=22,
                                anchor="w", relief="flat", cursor="hand2")
        option_label.bind("<Enter>", lambda e: e.widget.configure(bg="#595959"))
        option_label.bind("<Leave>", lambda e: e.widget.configure(bg="black"))
        option_label.pack(side="left", anchor="w", expand=1, fill='x', pady=1)

        option_img = tk.Button(option_frame, text="+", font="lucida 11", relief="groove", bd=0, bg="red",
                               cursor="hand2")
        option_img.pack(side="left")

        option_frame.pack(fill="x", expand=1)

        value_label = tk.Label(accordion, text=value, font=font_v, fg=fg_v, bg=bg_v, wraplength=wraplength,
                               justify="left")

        x = self.id

        option_img.bind("<Button-1>", lambda e: self.open_close(e, x))
        option_label.bind("<Button-1>", lambda e: self.open_close(e, x))

        self.options_values[self.id] = [False, option_frame, value_label]

        self.id += 1

    def open_close(self, e, id_):

        if self.options_values[id_][0]:
            self.options_values[id_][0] = False
            self.options_values[id_][2].pack_forget()
            return

        # remove all the options and values and show the value of option currently
        # clicked and then show the removed options again

        for key in self.options_values:
            if key != id_:
                if self.options_values[key][0]:
                    self.options_values[key][2].pack_forget()
                    self.options_values[key][0] = False
                if key > id_:
                    self.options_values[key][1].pack_forget()

        self.options_values[id_][2].pack(anchor="w", expand=1, fill='x', pady=1)
        self.options_values[id_][0] = True

        for key in range(id_ + 1, len(self.options_values)):
            self.options_values[key][1].pack(fill='x', expand=1)


first = "What is Python used for? Python is a computer programming language often " \
        "used to build websites and software, automate tasks, and conduct data analysis."

second = "What are JavaScript used for?" \
         "to create dynamic and interactive web content like applications and browsers."

third = "used for game programming, software engineering, data structures, developing browsers," \
        " operating systems, applications"

fourth = "Dart is a client-optimized language for developing fast apps on any platform. " \
         "Its goal is to offer the most productive programming language for multi-platform development."

root = tk.Tk()
root.title("Accordion In Tkinter")
bg = "#324252"
root.configure(bg=bg)
root.geometry("600x450")

tk.Label(root, text="Accordion In Tkinter", fg="#ff6200", bg=bg, font="cambria 18 bold").pack(pady=12)
accordion = Accordion(root, bg=bg)

accordion.add_option(option="Python", value=first, fg_o="white", bg_o="black",
                     font_o="lucida 15 ", font_v="lucida 12", wraplength=350)

accordion.add_option(option="Javascript", value=second, fg_o="white", bg_o="black",
                     font_o="lucida 15", font_v="lucida 12", wraplength=350)

accordion.add_option(option="C++", value=third, fg_o="white", bg_o="black",
                     font_o="lucida 15", font_v="lucida 12", wraplength=350)
accordion.add_option(option="Dart", value=fourth, fg_o="white", bg_o="black",
                     font_o="lucida 15", font_v="lucida 12", wraplength=350)
root.mainloop()
