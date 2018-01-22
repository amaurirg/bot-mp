import re
import os


busca = r'(href|src)="((img|css|js).*?)"'
troca = r'''\1="{% static '\2' %}"'''

paginas = [pagina for pagina in os.listdir("../templates/") if pagina.endswith(".html")]
os.chdir("../templates/")

for pagina in paginas:
    with open(pagina) as html_r:
        texto = html_r.read()
    if not re.search("{% load static %}", texto):
        with open(pagina, "w") as html_w:
            reg = re.sub(busca, troca, texto)
            html_w.write("{% load static %}\n" + reg)