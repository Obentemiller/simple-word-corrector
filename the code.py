from joblib import dump, load
from collections import defaultdict

class CorretorPalavras:
    def _init_(self):
        self.banco_dados = defaultdict(list)

    def treinar(self, palavras_corretas):
        for palavra in palavras_corretas:
            self.banco_dados[palavra[0]].append(palavra)

    def corrigir(self, palavra_errada):
        possiveis_correcoes = self.banco_dados[palavra_errada[0]]
        melhor_correcao = ''
        max_assoc = 0

        for correcao in possiveis_correcoes:
            assoc = sum(1 for i, j in zip(correcao, palavra_errada) if i == j)
            if assoc > max_assoc:
                melhor_correcao = correcao
                max_assoc = assoc

        return melhor_correcao

corretor = CorretorPalavras()
corretor.treinar(list(set([
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", 
    "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", 
    "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "voavanga", 
    "watermelon", "xigua", "yellow passion fruit", "zucchini"
])))


while True:
    palavra_errada = input("Insira o nome do dorama chato kk: ")
    correcao = corretor.corrigir(palavra_errada)
    print(f"Palavra errada: {palavra_errada}, kkmó burrona")
    print(f"Correção possível: {correcao}, tá ai.")

    dump(corretor, 'modelo_corretor.joblib')
    modelo_carregado = load('modelo_corretor.joblib')
    correcao_carregada = modelo_carregado.corrigir(palavra_errada)
    print(f"Usando modelo carregado, Correção possível: {correcao_carregada}")

    if palavra_errada.lower() == "sair":
        break
