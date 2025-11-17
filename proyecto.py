import tkinter as tk
class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Simple")
        master.geometry("300x400")

        self.entrada = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        columna = 0
        for boton in botones:
            accion = lambda x=boton: self.click_boton(x)
            tk.Button(master, text=boton, width=5, height=2, command=accion).grid(row=fila, column=columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def click_boton(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.entrada.get()))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Error")
        else:
            self.entrada.insert(tk.END, valor)
if __name__ == "__main__":
    ventana = tk.Tk()
    calculadora = Calculadora(ventana)
    ventana.mainloop()