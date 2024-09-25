#importa a biblioteca 
import json

#classe ArquivoJson
class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios =[
                {
                    'codigo':0,
                    'nome': 'Admin',
                    'cpf':'000.000.000-00',
                    'e-mail': 'administrador.com.br',
                    'profissao': 'Administrador'
                }
            ]
            
            # serializando converte para o json o objeto Python como json
            json_dados = json.dumps(usuarios)
            with open(f"{nome_arquivo}.json","w", encoding="utf-8")as f:
                f.write(json_dados)
            return f"{nome_arquivo}.json criado com sucesso."    
        except Exception as e:
            return f"Não foi possível criar o arquivo. {e}."   
    def abrir_arquivo(self,nome_arquivo):
        #desserializando objeto json  em python
        with open(f"{nome_arquivo}.json", "r", encoding="utf-8") as f:
            dados = json.load(f)    
        return dados 
    def salvar_dados(self,usuarios,nome_arquivo):
        try:
            with open(f" {nome_arquivo}.json ", "w", encoding="utf-8" )as f:
                json.dump(usuarios,f)
            return f"Dados gravados com sucesso."
        except Exception as e:
            return f"Não foi possível salvar os dados. {e}." 
           
    #destrutor
    def __del__(self):
        return f'Manipulador destruído.'
    