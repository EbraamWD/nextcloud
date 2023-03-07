from flask import Flask, render_template
from pyocclient import Client
import requests

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/')
def index():
    #Configurazione dell'URL di NextCloud e delle credenziali di accesso
    url = 'http://localhost:8081/apps/files/?dir=/&fileid=2'
    username = 'ebraamsaad'
    password = 'Its-My-Account99'

    #Creare un oggetto Client per la connesisone a NextCloud

    client = Client(url, username, password)

    #Effettua il login

    client.login()
    #Ottenere la lista dei file presenti nella cartella specificata

    folder_path = '/apps/files/?dir=/&fileid=2'
    files = client.list(folder_path)

    #Chiude la connessione a NextCloud

    client.logout()

    #Restituisce la lista dei file alla pagina HTML

    return render_template('index.html', files=files)





"""
@app.route('/aaa')
def hello2():
    

    oc.mkdir('testdir')

    oc.put_file('testdir/remotefile.txt', 'localfile.txt')

    link_info = oc.share_file_with_link('testdir/remotefile.txt')

    print ("Here is your link: ") + link_info.get_link()
    return "Hello World2"

"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
