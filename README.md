# Aplicação Kanban_logs

Status: Desenvolvedor ⚠️

Kanban Logs é uma aplicação web desenvolvida com Python, Django, e Bootstrap 5 que permite aos usuários registrar e organizar tópicos de estudo, acompanhados de anotações, em um formato visual de Kanban. A ferramenta ajuda a gerenciar o progresso de aprendizado de forma eficiente e prática.

## Tecnologias Utilizadas

- **Backend:**  <a href="https://docs.djangoproject.com/pt-br/5.1/faq/">Django</a> (Framework Python)
- **Frontend:** <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/"> Bootstrap 5</a> (Framework CSS)
- **Banco de Dados:** SQLite (ou qualquer outro compatível com Django)

## Pré-requisitos

- **Python3:** Download do <a href="https://www.python.org/downloads/">Python3.</a>
- **Django:** Digite no seu powershell ou terminal linux o comando `pip install django`.
- **Pip:** Gerenciador de pacotes do python que serve para instalação de dependências. Digite no seu powershell ou no terminal do linux o comando `python -m ensurepip --default-pip`.
- **Git:** Download do <a href="https://git-scm.com/downloads">Git.</a>

## Estrutura do Repositório
  Os projetos em Django utilizam a arquitetura MVT, Model, View, Template o que é bem semelhante a MVC.

- **Kanban_log/:** Diretório raiz do projeto ele é responsavel pela configuração e gerenciamento dos apps.
- **Kanban_logs/:** Diretório(app) principal.
- **user/:** Cóntem a parte logica do de gerenciamento de usuário como o de regitro e o login.
- **templates/:** Contém o esqueleto dos páginas.
- **manage.py:** Arquivo responsável pela inicialização do projeto.
- **urls.py:** Arquivo responsável pelo mapeamento de rotas.
- **views.py:** View desempenha o papel do Controller no MVC. Ela possui funções que processa as requisições HTTP, interage com os modelos e retorna uma resposta no caso uma página HTML.
- **models.py:** Model desempenha o papel da regra de négocio de Topic(tópico) e Entry(anotações) no caso do app user não precisou porquê a regra de négocio utilizado nesse caso foi a padrão importada do proprio django.
- **forms.py:** Padronização do formulário tanto o de Topic como o de Entry.
- **settings.py:** Responsável pela configuração do projeto, como a declaração de instalação de aplicativos e dependências como o Bootstrap, e a definição de qual banco de dados será utilizado na aplicação.
- **README.md:** Este arquivo.

## Como Executar

1. No terminal digite do powershell ou o git bash digite `git clone https://github.com/thiago-cloud/Kanban_log.git` de preferencia em Desktop.
2. Em seguida vá até a raiz do projeto Kanban_log
