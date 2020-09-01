#!/usr/bin/env python
# coding: utf-8
#Trabalho feito no jupyter notebook

#Bibliotecas necessárias
import pandas as pd
import numpy as np
import random
from collections import defaultdict

#Carrega o dataset
data = pd.read_pickle('corpus.pkl') #Carrega o dataset de transcrições dos humoristas
hassan_transc = data['transcript'].loc['hasan'] #Filtra apenas o dataset do humorista Hassan Minhaj

#Vale notar que o vetor de transição é criado implicitamente se criarmos os possíveis próximos estados repetindo
#as palavras que tem maior probabilidade proporcionalmente a sua probabilidade

def markov_chain(sentences): #Função que transforma a transcrição em uma cadeia de markov
    words = sentences.split() #Divide a transição em palavras
    dictio = defaultdict(list) #Cria um dicionário especial que recebe chaves novas como se fosse uma lista
    for prev_word, next_word in zip(words[0:-1], words[1:]): #Ordena as palavras em palavra anterior e palavra seguinte
            dictio[prev_word].append(next_word) #Faz append das palavras seguintes para cada chave de palavra única
    return dict(dictio) #Transforma o dicionário especial em um dicionário padrão
states = markov_chain(hassan_transc) #Chama a função

#Gera a primeira palavra da sentença aleatoriamente
n = 100 #Número de palavras para serem geradas
word1 = random.choice(list(states.keys())) #Gera a primeira aleatoriamente
Hasan_Says = word1 #Guarda primeira palavra em uma string

for i in np.arange(n): #Função que gera cada palavra da sentença
    word2 = random.choice(list(states[word1])) #Gera a segunda palavra da cadeia de markov. As palavras que mais se
    #repetem tem as maiores probabilidades de transição na cadeia
    word1 = word2 #Atualiza palavra 1
    Hasan_Says += ' ' + word2 #Une as palavras em uma sentença
print(Hasan_Says) #Printa a sentença total


# Gera o vetor de transição para uma palavra da transcrição (neste caso chamada de palavra zero)
word_transc = 'has' #Palavra zero escolhida para calcular o vetor de transição
next_words = states[word_transc] #Carrega a lista com todas as palavras que vem depois da palavra zero
word_series = pd.Series(next_words) #Transforma a lista em uma série
word_cont = word_series.value_counts()/word_series.value_counts().sum() #Conta o número de vezes que cada palavra aparece
#e divide pela soma de todas as palavras
print(word_cont)