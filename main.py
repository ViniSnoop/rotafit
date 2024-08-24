import customtkinter
import CRUD

import calculo

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.treino = None
        self.novoTreino = None

        # Janela
        self.title("Rotafit")
        self.geometry(f"{1280}x{720}")
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        # configurar GRID 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.telaInicial()

    def telaInicial(self):
        # Barra lateral

        self.janela_barralateral = customtkinter.CTkFrame(self, width=500, border_width=0)
        self.janela_barralateral.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Logo ROTAFIT

        self.logo_barralateral = customtkinter.CTkLabel(self.janela_barralateral, text="ROTAFIT",
                                                        font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_barralateral.grid(row=0, column=0, padx=200, pady=(100, 50))

        # Botão "Criar um novo Treino"

        self.botao_criar = customtkinter.CTkButton(self.janela_barralateral, command=self.criarTreino,
                                                   text="Criar um novo Treino", font=customtkinter.CTkFont(size=30),
                                                   width=300, height=100)
        self.botao_criar.grid(row=1, column=0, padx=20, pady=100)

        # Botão "Carregar Treinos"

        self.botao_carregar = customtkinter.CTkButton(self.janela_barralateral, command=self.lerTreino,
                                                      text="Carregar Treino", font=customtkinter.CTkFont(size=30),
                                                      width=300, height=100)
        self.botao_carregar.grid(row=2, column=0)

    def criarTreino(self):
        self.treino = CRUD.create_csv()
        self.novoTreino = self.treino
        self.frameUpdateEx()
    def lerTreino(self):
        self.treino = CRUD.read_csv()
        if self.treino != None:
            self.novoTreino = self.treino
            self.visualizarTreinos()



    def visualizarTreinos(self):
        # Se a tela de visualização já estiver criada, remova-a
        if hasattr(self, 'visu_Treinos'):
            self.visu_Treinos.destroy()

        self.janela_barralateral.grid_forget()

        # Barra lateral

        self.janela_barralateral = customtkinter.CTkFrame(self, width=500, border_width=0)
        self.janela_barralateral.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Criar nova tela para visualização de treinos
        self.visu_Treinos = customtkinter.CTkFrame(self, fg_color="transparent")
        self.visu_Treinos.grid(row=0, column=1, sticky="nsew")

        # Adicionar texto e botões na nova tela
        self.tituloVisuT = customtkinter.CTkLabel(self.janela_barralateral, text="Seu Treino:",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.tituloVisuT.grid(row=0, column=0, columnspan=2, padx=100, pady=(50, 50))

        # Salvar Treino
        self.BsaveTreino = customtkinter.CTkButton(self.janela_barralateral, text="Salvar",
                                                   font=customtkinter.CTkFont(size=20), width=150, height=50)
        self.BsaveTreino.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        # Definindo Parâmetros do Botão de Salvar de Treino:
        if self.novoTreino == self.treino:
            self.BsaveTreino.configure(state="Disabled", fg_color="transparent", border_width=2)
        else:
            self.BsaveTreino.configure(state="Enabled", command=self.BsaveTreino_C, border_width=0, fg_color="theme")

        # Alterar Exercícios
        self.alterarExercicio = customtkinter.CTkButton(self.janela_barralateral, text="Alterar Rotina",
                                                        font=customtkinter.CTkFont(size=20), width=150, height=50)
        self.alterarExercicio.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        # Voltar
        self.voltarmenu = customtkinter.CTkButton(self.janela_barralateral, command=self.VoltarBotao,
                                                  text="Voltar pro Menu inicial", font=customtkinter.CTkFont(size=20),
                                                  width=300, height=50, border_width=2)
        self.voltarmenu.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

        # Tempo médio de treino

        self.textoTempo = customtkinter.CTkLabel(self.visu_Treinos, text="Tempo Médio:", font=customtkinter.CTkFont(size=30,
                                                                                                                    weight="bold"))
        self.textoTempo.grid(row=7,column=2,padx=20,pady=20)
        self.TempoLabel = customtkinter.CTkLabel(self.visu_Treinos, text=calculo.calculoDeTempo(self.novoTreino),
                                                 font=customtkinter.CTkFont(size=30))
        self.TempoLabel.grid(row=8,column=2)

        # Adicionar exercícios ao frame de exercícios
        column = 0
        row = 1  # Começar a partir da linha 1 para os exercícios
        i = 0 # Contador de Exercícios
        for exercicios in self.novoTreino:
            if int(exercicios['qtd']) >= 0:  # Filtra os exercícios com quantidade maior que 0
                detalhes_str = (f"{exercicios['Nome']}, {5 * int(exercicios['qtd'])}x\n"
                                f"Tempo médio: {exercicios['tempo']} seg.")
                exercicio_label = customtkinter.CTkLabel(self.visu_Treinos, text=detalhes_str,
                                                         font=customtkinter.CTkFont(size=20))
                exercicio_label.grid(row=row, column=column, padx=20, pady=20, sticky="nw")

            # Ajustar a linha e coluna
            if (i + 1) % 7 == 0:
                column += 1  # Mudar para a próxima coluna a cada 7 exercícios
                row = 1  # Reiniciar a linha para a nova coluna
                i += 1 # Mudar para o próximo Exercício
            else:
                row += 1  # Mover para a próxima linha
                i +=1 # Mudar para o próximo Exercício

        # Configurar expansão do grid
        self.visu_Treinos.grid_rowconfigure(4, weight=1)
        self.visu_Treinos.grid_columnconfigure(1, weight=1)
        self.visu_Treinos.grid_columnconfigure(2, weight=1)

        self.janela_barralateral.grid_rowconfigure(4,weight=1)
    def VoltarBotao(self):
        self.visu_Treinos.grid_forget()  # Remove a tela de visualização dos treinos
        self.janela_barralateral.grid(row=0, column=0, rowspan=4, sticky="nsew")  # Reexibe a barra lateral
        self.update_idletasks()  # Atualiza a tela


    def BsaveTreino_C(self):
        CRUD.update_csv(self.novoTreino)


    def frameUpdateEx(self):
        # Se a tela de visualização já estiver criada, remova-a
        if hasattr(self, 'visu_Treinos'):
            self.visu_Treinos.destroy()

        self.janela_barralateral.grid_forget()

        # Barra lateral

        self.janela_barralateral = customtkinter.CTkFrame(self, width=500, border_width=0)
        self.janela_barralateral.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # Label pro grid Lateral

        self.labelFUE = customtkinter.CTkLabel(self.janela_barralateral,text="Alterar\nExercícios",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.labelFUE.grid(row=0,column=0, columnspan=2, padx=150 ,pady=(20,100),sticky='nwe')

        # Botão para Salvar o treino

        self.fueSaveB = customtkinter.CTkButton(self.janela_barralateral,width=250,height=100,corner_radius=20,text="Salvar Treino",font=customtkinter.CTkFont(size=30))
        self.fueSaveB.grid(row=1,column=0,padx=150,pady=20)

        # Criar tela para visualização de treinos
        self.visu_Treinos = customtkinter.CTkFrame(self, fg_color="transparent")
        self.visu_Treinos.grid(row=0, column=1, sticky="nsew")






if __name__ == "__main__":
    app = App()
    app.mainloop()
