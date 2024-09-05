import ttkbootstrap as ttk
from ttkbootstrap.window import Window

class App:
    def __init__(self):
        # Cria a janela principal
        self.win = Window(themename='journal')
        self.win.title('App')
        self.__start__()

    def __start__(self):
        self.set_geometry()
        self.win.mainloop()  # Iniciar o loop principal da aplicação

    def set_geometry(self):
        # Definir o tamanho da janela
        window_width = 1000
        window_height = 600

        # Obtém as dimensões da tela
        display_width = self.win.winfo_screenwidth()
        display_height = self.win.winfo_screenheight()

        # Calcula a posição da janela para ficar centralizada
        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)

        # Define a geometria da janela
        self.win.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.win.minsize(500, 300)
        self.win.maxsize(1500, 900)

# Execução da aplicação
if __name__ == "__main__":
    app = App()

