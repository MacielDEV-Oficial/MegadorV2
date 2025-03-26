import sys

# Lista de bibliotecas necessárias

class INSTALARDOR_DO_SISTEMA:
    def __init__(self):
        self.LISTA_MENSAGEM = [
            "Erro: Algumas dependências necessárias não estão instaladas. Por favor, instale-as utilizando o comando PIP",
            "Todas as dependências estão instaladas. O sistema está pronto para execução!"]
        self.LISTA_DE_BIBLIOTECAS_DEPENDENTE = [
        "os",
        "colorama",
        "time",
        "platform"]

    def VERIFICAR_BIBLIOTECAS_NECESSARIAS(self):
        dependencias = []
        for biblioteca in self.LISTA_DE_BIBLIOTECAS_DEPENDENTE:
            try:
                __import__(biblioteca)
            except ImportError:
                dependencias.append(biblioteca)
            
                if dependencias:
                    print(self.LISTA_MENSAGEM[0])
            
                else:
                    print(self.LISTA_MENSAGEM[1])
                    
    
    def VERIFICAR_TIPO_DE_SISTEMA_OPERACIAL(self):
        import os
        import platform
        self.sistema_operacional = platform.system()

    
    def INICIAR_VERSAO_CORRESPONDENTE(self):
        match self.sistema_operacional:
            case 'Windows':
                from versoes.windows import Megador
                windows = Megador()
                windows.Update()
            case 'Linux':
                from versoes.linux import Megador
                linux = Megador()
                linux.Update()
    
    def INICIAR_INSTALADOR(self):
        self.VERIFICAR_BIBLIOTECAS_NECESSARIAS()
        self.VERIFICAR_TIPO_DE_SISTEMA_OPERACIAL()
        self.INICIAR_VERSAO_CORRESPONDENTE()

instalador = INSTALARDOR_DO_SISTEMA()
instalador.INICIAR_INSTALADOR()