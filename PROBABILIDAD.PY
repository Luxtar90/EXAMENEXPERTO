import tkinter as tk
from tkinter import messagebox

def calcular_probabilidad():
    try:
        P_E1 = float(entry_pe1.get()) / 100  # Probabilidad de usar el ascensor 1
        P_E2 = float(entry_pe2.get()) / 100  # Probabilidad de usar el ascensor 2
        P_F_E1 = float(entry_pf_e1.get()) / 100  # Probabilidad de fallo dado que se usa el ascensor 1
        P_F_E2 = float(entry_pf_e2.get()) / 100  # Probabilidad de fallo dado que se usa el ascensor 2
        
        # Cálculo de las probabilidades usando el teorema de Bayes
        P_F = (P_F_E1 * P_E1) + (P_F_E2 * P_E2)  # Probabilidad total de fallo
        P_E1_F = (P_F_E1 * P_E1) / P_F  # Probabilidad de que haya fallado el ascensor 1

        messagebox.showinfo("Resultado", f"La probabilidad de que haya sido el ascensor 1 es: {P_E1_F:.2%}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Probabilidades")

# Crear y colocar los widgets
tk.Label(root, text="Probabilidad de usar el ascensor 1 ").grid(row=0, column=0, padx=10, pady=5)
entry_pe1 = tk.Entry(root)
entry_pe1.grid(row=0, column=1, padx=10, pady=5)
entry_pe1.insert(0, "45")

tk.Label(root, text="Probabilidad de usar el ascensor 2 ").grid(row=1, column=0, padx=10, pady=5)
entry_pe2 = tk.Entry(root)
entry_pe2.grid(row=1, column=1, padx=10, pady=5)
entry_pe2.insert(0, "55")

tk.Label(root, text="Probabilidad de fallo del ascensor 1 ").grid(row=2, column=0, padx=10, pady=5)
entry_pf_e1 = tk.Entry(root)
entry_pf_e1.grid(row=2, column=1, padx=10, pady=5)
entry_pf_e1.insert(0, "5")

tk.Label(root, text="Probabilidad de fallo del ascensor 2 ").grid(row=3, column=0, padx=10, pady=5)
entry_pf_e2 = tk.Entry(root)
entry_pf_e2.grid(row=3, column=1, padx=10, pady=5)
entry_pf_e2.insert(0, "8")

tk.Button(root, text="Calcular Probabilidad", command=calcular_probabilidad).grid(row=4, columnspan=2, pady=10)

# Iniciar el bucle principal
root.mainloop()
