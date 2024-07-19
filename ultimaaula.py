import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import *
from tkinter import messagebox  # Importar o módulo messagebox

# Definir os dados iniciais
data = {
    'data': ['2024-07-19', '2024-07-18', '2024-07-17', '2024-07-16', '2024-07-15', '2024-07-14', '2024-07-13'],
    'vendas': [3, 2, 5, 1, 10, 2, 1],
    'produtos': ['Celular', 'Tablet', 'Computador', 'Televisão', 'Fone', 'Mouse', 'Teclado'],
    'preco': [2000, 1000, 3500, 2000, 10, 30, 80],
    'quantidade': [3, 2, 1, 1, 5, 2, 3]
}


df = pd.DataFrame(data)

def plot_vendas_por_vendedor(dataframe):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='produtos', y='vendas', data=dataframe, ci=None, color='black')
    plt.grid(True)
    plt.title('Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_vendas_ao_longo_do_tempo(dataframe):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='data', y='vendas', hue='produtos', data=dataframe, marker='o')
    plt.grid(True)
    plt.title('Vendas ao Longo do Tempo por Produto')
    plt.xlabel('Data')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_distribuicao_vendas(dataframe):
    plt.figure(figsize=(8, 8))
    df_sum = dataframe.groupby('produtos')['vendas'].sum().reset_index()
    plt.pie(df_sum['vendas'], labels=df_sum['produtos'], autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Vendas por Produto')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def estatisticas_vendas(dataframe):
    total_vendas = dataframe['vendas'].sum()
    media_vendas = dataframe.groupby('produtos')['vendas'].mean()

    stats_str = f"Total de Vendas: {total_vendas}\n\nMédia de Vendas por Produto:\n{media_vendas}"
    messagebox.showinfo("Estatísticas de Vendas", stats_str)


root = Tk()
root.title("Análise de Vendas")


label = Label(root, text="Análise de Vendas", font=("Arial", 19))
label.pack(pady=10)

btn_vendas_produto = Button(root, text="Vendas por Produto", command=lambda: plot_vendas_por_vendedor(df))
btn_vendas_produto.pack(pady=10)

btn_vendas_tempo = Button(root, text="Vendas ao Longo do Tempo", command=lambda: plot_vendas_ao_longo_do_tempo(df))
btn_vendas_tempo.pack(pady=10)

btn_distribuicao_vendas = Button(root, text="Distribuição de Vendas", command=lambda: plot_distribuicao_vendas(df))
btn_distribuicao_vendas.pack(pady=10)

btn_estatisticas = Button(root, text="Estatísticas de Vendas", command=lambda: estatisticas_vendas(df))
btn_estatisticas.pack(pady=10)

root.mainloop()
