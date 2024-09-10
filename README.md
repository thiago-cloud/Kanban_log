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
- **Pip:** Gerenciador de pacotes do Python que serve para instalação de dependências. Digite no seu Powershell ou no terminal do Linux o comando `python -m ensurepip --default-pip`.
- **Git:** Download do <a href="https://git-scm.com/downloads">Git.</a>

## Estrutura do Repositório
  Os projetos em Django utilizam a arquitetura MVT, Model, View, Template o que é bem semelhante a MVC.

- **Kanban_log/:** Diretório raiz do projeto ele é responsavel pela configuração e gerenciamento dos apps.
- **Kanban_logs/:** Diretório(app) principal.
- **user/:** Cóntem a parte logica do de gerenciamento de usuário como o de regitro e o login.
- **templates/:** Contém a parte logica do de gerenciamento de usuário como o de registro e o login.
- **manage.py:** Arquivo responsável pela inicialização do projeto.
- **urls.py:** Arquivo responsável pelo mapeamento de rotas.
- **views.py:** View desempenha o papel do Controller no MVC. Ela possui funções que processa as requisições HTTP, interage com os modelos e retorna uma resposta, no caso uma página HTML.
- **models.py:** Model desempenha o papel da regra de negócio de Topic(tópico) e Entry(anotações) no caso do app user não precisou porque a regra de negócio utilizado nesse caso foi a padrão importada do próprio Django.
- **forms.py:** Padronização do formulário tanto o de Topic como o de Entry.
- **settings.py:** Responsável pela configuração do projeto, como a declaração de instalação de aplicativos e dependências como o Bootstrap, e a definição de qual banco de dados será utilizado na aplicação.
- **README.md:** Este arquivo.

## Como Executar

1. No terminal do Powershell ou o git bash digite `git clone https://github.com/thiago-cloud/Kanban_log.git` em desktop ou pasta de sua preferência.
2. Em seguida vá até a raiz do projeto cd Kanban_log e digite: `. ll_env/Scripts/activate` para ativar o ambiente virtual do projeto.
3. Após ativar o ambiente do projeto você estara dentro do ambiente agora, digite `python -m ensurepip --default-pip` para instalar as depêndencias do gerenciador de pacotes pip.
4. Instale o django o comando é: `pip install django`.
5. Instalação do bootstrap5 o comando é: `pip install django-bootstrap-v5`
6. Build do projeto: `python .\manage.py runserver`.
7. OBS: Os comandos devem ser digitados na raiz do projeto com ambiente virtual ativo, ou seja, dentro do ambiente virtual que no caso o ambiente virtual criado se chama ll_env.
