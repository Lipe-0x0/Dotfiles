import subprocess # Chamar comandos externos do shell
from i3ipc import Connection, Event # Conexão com i3wm e Manipulador de Eventos
import logging # Verificação de info/erro/warning e inserção em arquivo log.txt
import time

rofi_purple = "/home/fan/Documentos/dotfiles/rofi/colors-purple.rasi"
rofi_red = "/home/fan/Documentos/dotfiles/rofi/colors-red.rasi"

WP_IMPAR = "/home/fan/Imagens/Wallpaper/WP_PAR/a_woman_standing_in_front_of_a_window.jpg"
WP_PAR = "/home/fan/Imagens/Wallpaper/WP_IMPAR/a_cartoon_of_a_monster.png"

WP_REAL = ""

# Configuração do log
logging.basicConfig(filename = "/home/fan/Documentos/dotfiles/i3/log.txt", level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode = "a")

# Verifica paridade e envia comando para o shell
def apply(num):
    global WP_REAL

    if (int(num) % 2) == 0:
        WP_REAL = WP_PAR
    else: WP_REAL = WP_IMPAR

    logging.info(WP_REAL) # Informa qual wallpaper subiu

    subprocess.run(["feh", "--bg-fill", WP_REAL])


# Recebendo chamada do evento(alteração de workspace) e passando para a função apply
def on_workspace_focus(i3, event):
    apply(event.current.num)

def run():
    i3 = Connection()
    focused = [w for w in i3.get_workspaces() if w.focused] # de todos workspaces ativos ele pega o que estiver focado
    apply(focused[0].num if focused else None) # se focused existir(for diferente de None) então rodar apply
    i3.on("workspace::focus", on_workspace_focus)
    i3.main()

while True:
    try:
        run()
    except Exception as erro:
        logging.exception(erro)
    time.sleep(1)

