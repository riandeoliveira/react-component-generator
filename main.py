from shortcuts import *

# Extensões dos arquivos.
JSX = '.jsx'
CSS = '.module.css'

# Armazena nomes dos componentes.
COMPONENTS_NAMES_LIST = []

# Intervalo de tempo entre as execuções de comandos.
INTERVAL = 0.5

print('========== REACT COMPONENT GENERATOR ==========\n')
print('Preencha as informações abaixo:\n')

COMPONENT_NUMBER = int(input('Quantos componentes você deseja criar? '))

# Pega os nomes dos componentes.
def get_component_name(pos):
    COMPONENT_NAME = input('Qual é o nome do componente {}? '.format(pos + 1))
    COMPONENTS_NAMES_LIST.append(COMPONENT_NAME)

for i in range(COMPONENT_NUMBER):
    get_component_name(i)

print('Clique no diretório dos componentes.\n')

# Aguarda 5 segundos e pega a posição do cursor do mouse, indicando o diretório.
wait(5)
folder_position = pyautogui.position()

print('Criando componentes...\n')

# Retorna o código JSX base de um componente do React.
def get_jsx_code(component_name):
    JSX_CODE = """import styles from '../styles/""" + component_name + CSS + """';

const """ + component_name + """ = () => {
    return (
        <>

        </>
    );
}

export default """ + component_name + """;"""

    return JSX_CODE

# Cria um novo arquivo de acordo com seus argumentos.
def create_file(pos, extension, is_jsx):
    pyautogui.click(folder_position[0], folder_position[1], button='right')

    wait(INTERVAL)
    pyautogui.click(folder_position[0] + 10, folder_position[1] + 10)

    wait(INTERVAL)
    copy(pos + extension)

    wait(INTERVAL)
    press(1, 'ctrl', 'v')

    wait(INTERVAL)
    press(1, 'enter')

    if is_jsx:
        wait(INTERVAL)
        copy(get_jsx_code(pos))
        
        wait(INTERVAL)
        press(1, 'ctrl', 'v')

# Cria um arquivo JSX.
for i in range(COMPONENT_NUMBER):
    create_file(COMPONENTS_NAMES_LIST[i], JSX, True)

print('Componentes criados com sucesso!')
print('Agora clique no diretório onde ficarão os Modules CSS.\n')

wait(5)
folder_position = pyautogui.position()

print('Criando módulos...\n')

# Cria um arquivo Module CSS.
for i in range(COMPONENT_NUMBER):
    create_file(COMPONENTS_NAMES_LIST[i], CSS, False)

print('Módulos CSS criados com sucesso!\n')
print('===============================================')