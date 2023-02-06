from app import *
data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#Opções

to_do_list = """
        
        [LISTA DE TAREFAS]                  
    

    ____________________________
    [    [1] LISTAR TAREFAS    ] 
    ____________________________    
    [    [2] ADICIONAR TAREFAS ] 
    ____________________________    
    [    [3] DELETAR TAREFAS   ] 
    ____________________________
    [    [4] DELETAR TUDO      ]


"""


#eu lista todas as tarefas

def lista_tarefas():

    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lista")

    rows = cursor.fetchall()

    for row in rows:
        tarefa = row[1]
        tempo = row[2]
        print(f'Tarefa: {tarefa} adicionada às {tempo}')

    conn.close()


def deletar_dados(tarefa):
    with sqlite3.connect('base.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lista WHERE tarefa=?", (tarefa,))
        conn.commit()


def inserir_tarefa(tarefa):
    cursor.execute("""
    INSERT INTO lista (tarefa, data)
    VALUES (?, ?)
    """, (tarefa, data))

    lista_tarefas()

    conn.commit()
    conn.close()

def deletar_todos_dados():
    with sqlite3.connect('base.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lista")
        conn.commit()


print(to_do_list)
opcao = input('Escolha uma opção: ')

if opcao == '1':
    lista_tarefas()
elif opcao == '2':
    tare = input('Qual tarefa você deseja inserir ?: ')
    print(f'Tem certeza que deseja Adicionar ([{tare}]) às suas tarefas ?')
    op = input('''

        [1] SIM | [0] NÃO 
    
    ''')
    if op == '1':
        inserir_tarefa(tare)
    if op == '0':
        lista_tarefas()


elif opcao == '3':
    tare = input('Qual tarefa você deseja DELETAR ?: ')
    print(f'Tem certeza que deseja DELETAR ([{tare}]) ?')
    op = input('''

        [1] SIM | [0] NÃO 
    
    ''')
    if op == '1':
        deletar_dados(tare)
        print("Tarefa DELETADA com sucesso!")
    else:
        print(f"Falha ao DELETAR tarefa {tare}")
    if op == '0':
        lista_tarefas()

elif opcao == '4':
    print(f'Tem certeza que deseja DELETAR TUDO ?')
    op = input('''

        [1] SIM | [0] NÃO 
    
    ''')
    if op == '1':
        deletar_todos_dados()
        print("Tarefa DELETADA com sucesso!")
    else:
        print(f"Falha ao DELETAR!")