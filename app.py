from flask import Flask, jsonify
from owncloud import Client, FileInfo
import requests
import os



app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/files')
def index():
    #Configurazione dell'URL di NextCloud e delle credenziali di accesso
    url = 'http://localhost:8081'
    username = 'ebraamsaad'
    password = 'ebraamsaad99'

    #Creare un oggetto Client per la connesisone a NextCloud

    client = Client(url)

    #Effettua il login

    client.login(username, password)
    #Ottenere la lista dei file presenti nella cartella specificata

    #folder_path = "."
    files = client.list(".")
    print(files)

    file_tree = {"files":[]}
    i = 0
    for file in files:
        file_name = os.path.basename(file.path)
        file_tree["files"].append(file_name)
        #if file_name== METADATA_FILENAME:
        #print (file_name + " " + str(i))
        print (file.path + " " + str(i))
        i+=1

    #Chiude la connessione a NextCloud

    client.logout()

    #Restituisce la lista dei file alla pagina HTML

    return file_tree

@app.route('/photos')
def view():
    url = 'http://0.0.0.0:8081'
    username = 'ebraamsaad'
    password = 'ebraamsaad99'
    client = Client(url)

    client.login(username, password)

    photos = client.list("/Photos")
    photo_tree = {"photos":[]}

    i = 0
    for photo in photos:
        photo_name = os.path.basename(photo.path)
        photo_attribute = photo.attributes["{DAV:}getcontenttype"]
        if photo_attribute == "image/jpeg":
            photo_tree["photos"].append(photo_name)
            print(photo.path + " " + str(i))
        i+=1
    
    return photo_tree
        




@app.route('/saluta')
def tisaluta():
    url = 'http://localhost:8081'
    username = 'ebraamsaad'
    password = 'ebraamsaad99'

    saluto = "ti saluta checco"
    return saluto



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

"""
@app.route('/aaa')
def hello2():
    

    oc.mkdir('testdir')

    oc.put_file('testdir/remotefile.txt', 'localfile.txt')

    link_info = oc.share_file_with_link('testdir/remotefile.txt')

    print ("Here is your link: ") + link_info.get_link()
    return "Hello World2"

"""