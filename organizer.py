import os #Sistema operacional
import shutil #Incluir, mover, remover arquivos


def organizar_pasta(caminho_pasta):
    file_extensions = set() #Variavel vazia que armazenará informaçoes

    for filename in os.listdir(caminho_pasta): #lista os diretorios do caminho da pasta
        if os.path.isfile(os.path.join(caminho_pasta, filename)): #Verifica se é um arquivo ou uma pasta
            file_extension = filename.split(".")[-1].lower() #Remove tudo que estiver pra tras do arquivo ex: python.py = remove python.
            file_extensions.add(file_extension)

    for extension in file_extensions:
        folder_name = extension.capitalize() + "Files"
        folder_path = os.path.join(caminho_pasta, folder_name)
        
        if not os.path.exists(folder_path): # Se exixstir uma pasta com o mesmo nome, pode criar
            os.makedirs(folder_path)

        for filename in os.listdir(caminho_pasta):
            if os.path.isfile(os.path.join(caminho_pasta, filename)):
                file_extension = filename.split(".")[-1].lower() 
                if file_extensions == extension:
                    old_file_path = os.path.join(caminho_pasta, filename)
                    new_file_path = os.path.join(folder_path. filename)
                    shutil.move(old_file_path, new_file_path)
                    print(f"Arquivo {filename} movido para {folder_name}")

if __name__ == "__main__":
    caminho_pasta = r'c:\Users\Giovanni\Desktop\Giovanni\Utilidades Empresariais'
    organizar_pasta(caminho_pasta)


print("Acabou de organizar...")