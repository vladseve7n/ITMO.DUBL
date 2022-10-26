import argparse

import numpy as np
import pandas as pd
import requests

from utils.USEImplement import USE
from utils.tools import preprocess_fn

cluster_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/clusters.json'
train_ds_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/train.csv'
distance = 'l1'

implementations = {
    'USE': USE
}


def main(implemntation: str = 'USE', preprocess: str = 'lower_clean'):

    print('Загружаем данные...')
    # Загружаем данные
    train_ds = pd.read_csv(train_ds_url).drop('pair_id', axis=1)

    clusters = requests.get(cluster_url).json()['clusters']
    for cluster_id in range(len(clusters)):
        for name_id in range(len(clusters[cluster_id])):
            clusters[cluster_id][name_id] = preprocess_fn(preprocess, clusters[cluster_id][name_id])

    embed = implementations[implemntation]()

    unique_names = list(np.unique(np.append(train_ds.name_1.values, train_ds.name_2.values)))

    # Для каждого уникального названия ищем embedding
    embeddings_dict = {preprocess_fn(preprocess, name): embed(preprocess_fn(preprocess, name)) for name in unique_names}

    # Считаем embedding для каждого кластера
    cluster_embedding = {}
    for num, cluster in enumerate(clusters):
        cluster_embedding[num] = {}
        cluster_embedding[num]['cluster'] = cluster
        embed_cluster = np.mean(np.array([embeddings_dict[x] for x in cluster]), axis=0)
        cluster_embedding[num]['embedding'] = embed_cluster

    # Далее по запросу сравниваем embedding полученного слова с embedding'ами кластеров
    while True:
        name_of_company = input('Введите название компании для поиска кластера:\n')

        if name_of_company.lower() == 'cancel':
            exit(0)

        res_clus, min_distance = embed.find_closest_cluster(cluster_embedding,
                                                            preprocess_fn(preprocess, name_of_company),
                                                            distance=distance)

        if res_clus:
            print(f'Кластер: {res_clus}\n'
                  f'Дистанция {distance}: {min_distance}')
        else:
            print('Подходящий кластер не найден')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process inputs.')
    parser.add_argument('-i', '--implementation', type=str,
                        help='What implementation of embedding to use', default='USE')
    parser.add_argument('-p', '--preprocess', help='What kind of preprocess to use',
                        default='lower_clean')
    args = parser.parse_args()
    main(args.implementation)
