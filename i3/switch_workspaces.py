import subprocess # Chamar comandos externos do shell
from i3ipc import Connection, Event # Conexão com i3wm e Manipulador de Eventos

i3 = Connection() 

# Altera workspace
def switch(number):
    if (int(number) % 2) == 0:
        subprocess.run(["feh", "--bg-fill", "/home/fan/Imagens/Wallpaper/a_cartoon_of_a_man_flying_through_the_airASCII.jpeg"])
    else:
        subprocess.run(["feh", "--bg-fill", "/home/fan/Imagens/Wallpaper/Who the hell do you think i am?ASCII.jpeg"])

# Pega a area de trabalho focada/atual
number_ws = i3.get_tree().find_focused().workspace().name
# Aplica a função de troca com subprocess
switch(number_ws)


# Registra o evento chamado
def on_workspace_focus(i3, e):
    switch(e.current.name)

i3.on(Event.WORKSPACE_FOCUS, on_workspace_focus)

i3.main()
