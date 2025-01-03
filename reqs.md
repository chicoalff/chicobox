
# Requisitos Funcionais do CRUD de Projetos

## 1. Criar Projeto

*   **RF-PROJ-01:** O sistema deve apresentar um botão "Novo Projeto" que leva o usuário a uma interface de criação.
*   **RF-PROJ-02:** Na interface de criação de projetos, o sistema deve apresentar os seguintes campos obrigatórios:
    *   Nome do Projeto: Campo de texto para o nome do projeto.
    *   Descrição do Projeto: Campo de texto para a descrição detalhada do projeto.
    *   Tipo de Projeto: Dropdown com as opções "Interno" ou "Externo".
    *   Status: Checkbox indicando se o projeto está ativo ou inativo.
*   **RF-PROJ-03:** O sistema deve salvar automaticamente:
    *   Usuário responsável (logado).
    *   Data e hora da criação.

## 2. Editar Projeto

*   **RF-PROJ-04:** O sistema deve exibir um botão de "Editar" na listagem de projetos para cada item.
*   **RF-PROJ-05:** Ao clicar em "Editar", o sistema deve abrir a interface com os campos já preenchidos:
    *   Nome do Projeto.
    *   Descrição do Projeto.
    *   Tipo de Projeto.
    *   Status (ativo/inativo).
*   **RF-PROJ-06:** O sistema deve permitir a alteração dos campos e salvar as modificações:
    *   Data de atualização deve ser preenchida automaticamente.
    *   Registrar o usuário que realizou a atualização.

## 3. Excluir Projeto

*   **RF-PROJ-07:** O sistema deve apresentar um botão para "Excluir" na listagem de projetos.
*   **RF-PROJ-08:** Antes de excluir um projeto, o sistema deve exibir uma mensagem de confirmação:
    > "Tem certeza de que deseja excluir este projeto?"
*   **RF-PROJ-09:** O sistema deve validar se o projeto pode ser excluído:
    *   Bloquear exclusões que tenham dependências vinculadas (se aplicável).

# Requisitos Funcionais da Listagem e Busca de Projetos

## 4. Listagem de Projetos

*   **RF-LIST-01:** O sistema deve exibir uma tabela com os seguintes campos:
    *   ID: Identificador único do projeto.
    *   Nome do Projeto: Nome do projeto cadastrado.
    *   Usuário (Owner): Usuário responsável pelo projeto.
    *   Data de Atualização: Data e hora da última atualização do projeto.
    *   Status: Indicação de ativo/inativo.
*   **RF-LIST-02:** Cada linha da tabela deve incluir:
    *   Ícone de "Editar" (botão).
    *   Ícone de "Excluir" (botão).

## 5. Busca de Projetos

*   **RF-BUSC-01:** O sistema deve incluir uma barra de busca com o placeholder "Buscar Projeto".
*   **RF-BUSC-02:** A busca deve permitir filtrar projetos por:
    *   Nome do Projeto.
    *   Usuário responsável.
*   **RF-BUSC-03:** A busca deve atualizar dinamicamente os resultados exibidos na tabela.

## 6. Paginação

*   **RF-PAG-01:** O sistema deve incluir paginação para a listagem de projetos.
*   **RF-PAG-02:** Configuração inicial:
    *   10 projetos por página.
*   **RF-PAG-03:** Botões para navegar entre as páginas.

## 7. Responsividade

*   **RF-RESP-01:** A interface deve ser responsiva, adaptando-se para dispositivos móveis e desktops.
*   **RF-RESP-02:** A tabela de listagem deve permitir rolagem horizontal em telas menores.

--------------------------------------------------------------------------------------------
# Casos de Uso: CRUD de Projetos

## Caso de Uso 1: Criar Projeto

**Ator:** Usuário

### Fluxo Principal:
1. O usuário clica no botão **"NOVO PROJETO"**.
2. O sistema exibe a interface de cadastro de projeto.
3. O usuário preenche os campos com as informações do projeto (nome, descrição, etc.).
4. O usuário clica no botão **"Salvar"**.
5. O sistema valida os dados inseridos.
6. O sistema salva o projeto no banco de dados.
7. O sistema exibe a mensagem de sucesso.
8. O sistema redireciona o usuário para a lista de projetos.

### Fluxos Alternativos:
- **4a.** Se houver campos inválidos, o sistema exibe as mensagens de erro e solicita a correção.
- **6a.** Se ocorrer um erro ao salvar o projeto, o sistema exibe a mensagem de erro.

---

## Caso de Uso 2: Listar Projetos

**Ator:** Usuário

### Fluxo Principal:
1. O usuário clica no menu **"PROJETOS"**.
2. O sistema exibe a interface de listagem de projetos.
3. O sistema lista os projetos cadastrados, exibindo informações como nome, descrição e data de criação.

### Fluxos Alternativos:
- **3a.** Se não houver projetos cadastrados, o sistema exibe a mensagem **"Nenhum projeto encontrado"**.

---

## Caso de Uso 3: Visualizar Projeto

**Ator:** Usuário

### Fluxo Principal:
1. O usuário clica no botão **"Visualizar"** na lista de projetos.
2. O sistema exibe a interface de visualização do projeto, com suas informações detalhadas.

---

## Caso de Uso 4: Editar Projeto

**Ator:** Usuário

### Fluxo Principal:
1. O usuário clica no botão **"Editar"** na lista de projetos.
2. O sistema exibe a interface de edição do projeto, com os campos preenchidos com as informações atuais.
3. O usuário edita as informações do projeto.
4. O usuário clica no botão **"Salvar"**.
5. O sistema valida os dados inseridos.
6. O sistema atualiza o projeto no banco de dados.
7. O sistema exibe a mensagem de sucesso.
8. O sistema redireciona o usuário para a lista de projetos.

### Fluxos Alternativos:
- **4a.** Se houver campos inválidos, o sistema exibe as mensagens de erro e solicita a correção.
- **6a.** Se ocorrer um erro ao atualizar o projeto, o sistema exibe a mensagem de erro.

---

## Caso de Uso 5: Excluir Projeto

**Ator:** Usuário

### Fluxo Principal:
1. O usuário clica no botão **"Excluir"** na lista de projetos.
2. O sistema exibe uma mensagem de confirmação.
3. O usuário confirma a exclusão.
4. O sistema exclui o projeto do banco de dados.
5. O sistema exibe a mensagem de sucesso.
6. O sistema atualiza a lista de projetos.

### Fluxos Alternativos:
- **3a.** Se o usuário cancelar a exclusão, o sistema retorna para a lista de projetos.
- **4a.** Se ocorrer um erro ao excluir o projeto, o sistema exibe a mensagem de erro.
