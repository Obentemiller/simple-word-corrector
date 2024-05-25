# word corrector (simple)
This repository contains a simple word correction program that helps correct misspelled names contained in the program's internal list. The program uses the joblib library to save and load the trained model.

## <how it works?>
-The program trains a model with a list of correct words. It then allows the user to input words that may be incorrect and attempts to correct those words based on previous training


## <Explanation of How the Code Works>

This program is a word corrector that helps to correct misspelled words based on a set of correctly spelled words provided in advance. It uses the `joblib` library to save and load the trained model, allowing the training to be reused without the need to redo it every time the program is run.

### <Code Structure>

1. <Importing Libraries>>
    <code in python>
    from joblib import dump, load
    from collections import defaultdict
    ```
    The program starts by importing `dump` and `load` from the `joblib` library for saving and loading the model, respectively. It also imports `defaultdict` from the `collections` module to create a dictionary that automatically initializes empty lists.

2. <Defining the CorretorPalavras Class>
    class CorretorPalavras:
        def __init__(self):
            self.banco_dados = defaultdict(list)

    The `CorretorPalavras` class is defined. The `__init__` method initializes a dictionary `banco_dados` where the keys are letters and the values are lists of words that start with that letter.

3. <Training Method>
    def treinar(self, palavras_corretas):
        for palavra in palavras_corretas:
            self.banco_dados[palavra[0]].append(palavra)
  
    The `treinar` method receives a list of correct words and organizes them in `banco_dados` based on the first letter of each word.

4. <Correction Method>>
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

    The `corrigir` method tries to find the best correction for a misspelled word. It looks up the correct words that start with the same letter as the misspelled word and calculates an "association" based on the number of matching characters in the same positions. The word with the highest association is returned as the possible correction.

5. <Example Usage>
    corretor = CorretorPalavras()
    corretor.treinar(list(set([...])))

    while True:
        palavra_errada = input("Enter the misspelled word: ")
        if palavra_errada.lower() == "sair":
            break

        correcao = corretor.corrigir(palavra_errada)
        print(f"Misspelled word: {palavra_errada}")
        print(f"Possible correction: {correcao}")

        dump(corretor, 'modelo_corretor.joblib')
        modelo_carregado = load('modelo_corretor.joblib')
        correcao_carregada = modelo_carregado.corrigir(palavra_errada)
        print(f"Using loaded model, Possible correction: {correcao_carregada}")

    A `CorretorPalavras` object is created and trained with a list of correct words. In an infinite loop, the program asks the user to input a misspelled word and tries to correct it. The suggested correction is displayed, and the model is saved and loaded again using `joblib` to demonstrate that the correction works even after the model is reloaded.

### <Use of `joblib>

The `joblib` library is used to serialize (save) and deserialize (load) the `CorretorPalavras` model. This is useful for preserving the state of the trained model and reusing it without having to retrain it.

- <Saving the Model>
    dump(corretor, 'modelo_corretor.joblib')
    The `dump` method saves the `corretor` object to the file `'modelo_corretor.joblib'`.

- <Loading the Model>
    modelo_carregado = load('modelo_corretor.joblib')

    The `load` method loads the saved model from the file `'modelo_corretor.joblib'`, allowing it to be reused.

With the use of `joblib`, the program can quickly save and load models, making execution more efficient and convenient, especially for applications that require multiple runs or model distribution.
