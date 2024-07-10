import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import Qt
from data import conect_to_database

class JanelaPrincipal(QMainWindow): #classe principal que vai conter elementos  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(450,150)
        self.setWindowIcon(QIcon('icon.png')) # Substitua pelo caminho correto do ícone
        self.interface()
        self.show()# faz a tela ser exibida

    def interface(self):
        central_widget = QWidget()
        layout_principal = QGridLayout()  # Instanciando QGridLayout corretamente
        central_widget.setLayout(layout_principal)

        self.status = QLabel('Conecte-se ao banco!')
        layout_principal.addWidget(self.status, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.botao_conectar = QPushButton('Conectar')
        self.botao_conectar.clicked.connect(self.connecting)
        layout_principal.addWidget(self.botao_conectar, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(central_widget)

    def connecting(self):
        conexao = conect_to_database()
        self.status.setText(f'Conexão: {conexao}')

qt = QApplication(sys.argv) #variavel qt instanciando a classe QApplication: permite usar recursos do SO
app = JanelaPrincipal() #instaciando a classe
sys.exit(qt.exec()) #encerra totalmente a aplicação assim que fechada
