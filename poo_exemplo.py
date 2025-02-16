import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# ===================== ABSTRAÇÃO ===================== #
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self._marca = marca  # Atributo protegido (Encapsulamento)
        self._modelo = modelo
        self._ano = ano

    @abstractmethod
    def exibir_info(self):
        pass

# ===================== HERANÇA E POLIMORFISMO ===================== #
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.__portas = portas  # Atributo privado (Encapsulamento)

    def exibir_info(self):
        return f"🚗 Carro: {self._marca} {self._modelo} ({self._ano}) - {self.__portas} portas"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.__cilindradas = cilindradas  # Atributo privado (Encapsulamento)

    def exibir_info(self):
        return f"🏍️ Moto: {self._marca} {self._modelo} ({self._ano}) - {self.__cilindradas}cc"

# ===================== INTERFACE GRÁFICA ===================== #
class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Veículos")

        # Labels e entradas
        tk.Label(root, text="Marca:").grid(row=0, column=0)
        self.entrada_marca = tk.Entry(root)
        self.entrada_marca.grid(row=0, column=1)

        tk.Label(root, text="Modelo:").grid(row=1, column=0)
        self.entrada_modelo = tk.Entry(root)
        self.entrada_modelo.grid(row=1, column=1)

        tk.Label(root, text="Ano:").grid(row=2, column=0)
        self.entrada_ano = tk.Entry(root)
        self.entrada_ano.grid(row=2, column=1)

        tk.Label(root, text="Número de Portas (se for Carro):").grid(row=3, column=0)
        self.entrada_portas = tk.Entry(root)
        self.entrada_portas.grid(row=3, column=1)

        tk.Label(root, text="Cilindradas (se for Moto):").grid(row=4, column=0)
        self.entrada_cilindradas = tk.Entry(root)
        self.entrada_cilindradas.grid(row=4, column=1)

        # Botões
        self.botao_adicionar_carro = tk.Button(root, text="Adicionar Carro", command=self.adicionar_carro)
        self.botao_adicionar_carro.grid(row=5, column=0)

        self.botao_adicionar_moto = tk.Button(root, text="Adicionar Moto", command=self.adicionar_moto)
        self.botao_adicionar_moto.grid(row=5, column=1)

        # Lista para exibir veículos cadastrados
        self.lista_veiculos = tk.Listbox(root, width=50)
        self.lista_veiculos.grid(row=6, column=0, columnspan=2)

    def adicionar_carro(self):
        marca = self.entrada_marca.get()
        modelo = self.entrada_modelo.get()
        ano = self.entrada_ano.get()
        portas = self.entrada_portas.get()

        if not (marca and modelo and ano and portas):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        carro = Carro(marca, modelo, ano, portas)
        self.lista_veiculos.insert(tk.END, carro.exibir_info())

    def adicionar_moto(self):
        marca = self.entrada_marca.get()
        modelo = self.entrada_modelo.get()
        ano = self.entrada_ano.get()
        cilindradas = self.entrada_cilindradas.get()

        if not (marca and modelo and ano and cilindradas):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        moto = Moto(marca, modelo, ano, cilindradas)
        self.lista_veiculos.insert(tk.END, moto.exibir_info())

# ===================== EXECUÇÃO DA APLICAÇÃO ===================== #
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
