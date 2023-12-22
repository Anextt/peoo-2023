import tkinter as tk
from tkinter import messagebox
import random

class ProximoTremShopBot:
    def __init__(self):
        self.nome_cliente = None
        self.destino = None
        self.endereco = None
        self.preco = None
        self.modelos_locomotivas = ["ge u20c", "baldwin consolidation", "ge 2 c+c 2", "gm g12", "rail pr7", "alco rs8"]

    def calcular_preco(self):
        # Aqui você pode adicionar lógica para calcular o preço com base no destino, modelo de locomotiva, etc.
        self.preco = 25  # Preço fixo de $25

    def responder_mensagem(self, mensagem):
        # Adicionando lógica para responder a mensagens específicas sobre modelos de locomotivas
        mensagem = mensagem.lower()
        if any(modelo in mensagem for modelo in self.modelos_locomotivas):
            return "Temos uma grande variedade de locomotivas disponíveis. O preço é $25. Como posso ajudar com a sua escolha?"
        else:
            return "Desculpe, não entendi. Pode reformular a pergunta?"

    def realizar_venda(self, nome_cliente, destino, endereco):
        self.nome_cliente = nome_cliente
        self.destino = destino
        self.endereco = endereco
        self.calcular_preco()

class VendaGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Próximo Trem Shop - Finalizar Compra")

        self.bot = ProximoTremShopBot()

        self.label_valor = tk.Label(self, text="Valor: $25")
        self.label_nome = tk.Label(self, text="Nome:")
        self.entry_nome = tk.Entry(self)

        self.label_cidade = tk.Label(self, text="Cidade:")
        self.entry_cidade = tk.Entry(self)

        self.label_endereco = tk.Label(self, text="Endereço:")
        self.entry_endereco = tk.Entry(self)

        self.btn_finalizar_compra = tk.Button(self, text="Finalizar Compra", command=self.finalizar_compra)

        self.label_valor.grid(row=0, column=0, columnspan=2, pady=10)
        self.label_nome.grid(row=1, column=0, sticky=tk.E)
        self.entry_nome.grid(row=1, column=1)
        self.label_cidade.grid(row=2, column=0, sticky=tk.E)
        self.entry_cidade.grid(row=2, column=1)
        self.label_endereco.grid(row=3, column=0, sticky=tk.E)
        self.entry_endereco.grid(row=3, column=1)
        self.btn_finalizar_compra.grid(row=4, column=0, columnspan=2, pady=10)

    def finalizar_compra(self):
        nome_cliente = self.entry_nome.get()
        destino = self.entry_cidade.get()
        endereco = self.entry_endereco.get()
        
        self.bot.realizar_venda(nome_cliente, destino, endereco)

        resumo = f"Nome: {nome_cliente}\nCidade: {destino}\nEndereço: {endereco}\nValor: ${self.bot.preco}"
        messagebox.showinfo("Compra Realizada", f"Obrigado por escolher o Próximo Trem Shop. Sua compra foi realizada com sucesso!\n\n{resumo}")
        self.destroy()

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Próximo Trem Shop Chatbot")

        self.bot = ProximoTremShopBot()
        self.venda_app = VendaGUI()

        self.conversa_text = tk.Text(self, height=10, width=50, state=tk.DISABLED)
        self.entrada_mensagem = tk.Entry(self, width=40)
        self.btn_enviar = tk.Button(self, text="Enviar", command=self.enviar_mensagem)

        self.conversa_text.grid(row=0, column=0, columnspan=2, pady=10)
        self.entrada_mensagem.grid(row=1, column=0, padx=10)
        self.btn_enviar.grid(row=1, column=1)

        self.adicionar_mensagem_chat("Bem-vindo ao Próximo Trem Shop! Como posso ajudar você hoje?")

    def enviar_mensagem(self):
        mensagem_comprador = self.entrada_mensagem.get()
        self.adicionar_mensagem_chat(f"Você: {mensagem_comprador}")

        resposta_bot = self.bot.responder_mensagem(mensagem_comprador)
        self.adicionar_mensagem_chat(f"Bot: {resposta_bot}")

        if "preço" in resposta_bot.lower():  # Se a resposta do bot menciona preço, exibir interface de venda
            self.deiconify()  # Exibe a janela principal
            self.withdraw()  # Esconde a janela de chat

    def adicionar_mensagem_chat(self, mensagem):
        self.conversa_text.config(state=tk.NORMAL)
        self.conversa_text.insert(tk.END, mensagem + "\n")
        self.conversa_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = ChatbotGUI()
    app.mainloop()

    # Após o chat, exibir a interface de venda
    app.venda_app.mainloop()
