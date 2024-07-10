import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import Qt
from data import conect_to_database, register_users, show_users, check_login

class JanelaPrincipal(QMainWindow): # Classe principal que vai conter elementos  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(400,200)
        self.setWindowIcon(QIcon('icon.png')) # Substitua pelo caminho correto do ícone
        self.interface()
        self.show() # faz a tela ser exibida

    def interface(self):
        main_layout = QVBoxLayout()

        # Layout do formulário
        form_layout = QFormLayout()

        # Campos do formulário
        self.username_input = QLineEdit()
        self.senha_input = QLineEdit()
        self.senha_input.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addRow('Username:', self.username_input)
        form_layout.addRow('Senha:', self.senha_input)

        main_layout.addLayout(form_layout)

        # Botão para cadastrar aluno
        self.submit_button = QPushButton('Cadastrar-se')
        main_layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.registrando)

        self.login_button = QPushButton('Fazer Login')
        main_layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.fazendo_login)

        # Label para mostrar o status
        self.status_label = QLabel("")
        main_layout.addWidget(self.status_label)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def registrando(self):
        username = self.username_input.text()
        senha = self.senha_input.text()

        status = register_users(username,senha)
        self.status_label.setText(status)

        self.username_input.clear()
        self.senha_input.clear()

    def fazendo_login(self):
        username = self.username_input.text().strip()
        senha = self.senha_input.text()

        status = check_login(username,senha)
        self.status_label.setText(status)



qt = QApplication(sys.argv) # variável qt instanciando a classe QApplication: permite usar recursos do SO
app = JanelaPrincipal() # instanciando a classe
sys.exit(qt.exec()) # encerra totalmente a aplicação assim que fechada
