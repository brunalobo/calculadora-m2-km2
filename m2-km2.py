import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        texto = entry.get()
        texto = texto.replace('.', '').replace(',', '.')  # Remove pontos e troca vírgula por ponto
        metros_quadrados = float(texto)
        km2 = metros_quadrados / 1_000_000
        resultado_label.config(text=f"{metros_quadrados:,.2f} m² = {km2:.6f} km²")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de m² para km²")
janela.geometry("400x400")

# Título
titulo_label = tk.Label(janela, text="Calculadora de Área", font=("Arial", 16))
titulo_label.pack(pady=10)

# Campo de entrada
entry = tk.Entry(janela, font=("Arial", 14))
entry.pack(pady=5)

# Botão de conversão
converter_button = tk.Button(janela, text="Converter", command=converter)
converter_button.pack(pady=5)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

# Rodar a janela
janela.mainloop()
