import argparse

import numpy as np
import pandas as pd
import requests

from utils.USEImplement import USE

cluster_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/clusters.json'
train_ds_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/train.csv'
distance = 'l2'

implementations = {
    'USE': USE
}


def main(implemntation: str = 'USE'):
    train_ds = pd.read_csv(train_ds_url).drop('pair_id', axis=1)

    clusters = requests.get(cluster_url).json()['clusters']

    embed = implementations[implemntation]()

    unique_names = list(np.unique(np.append(train_ds.name_1.values, train_ds.name_2.values)))

    embeddings_dict = {name: embed(name) for name in unique_names}

    cluster_embedding = {}
    for num, cluster in enumerate(clusters):
        cluster_embedding[num] = {}
        cluster_embedding[num]['cluster'] = cluster
        embed_cluster = np.mean(np.array([embeddings_dict[x] for x in cluster]), axis=0)
        cluster_embedding[num]['embedding'] = embed_cluster
    while True:
        name_of_company = input('Введите название компании для поиска кластера:\n')
        if name_of_company.lower() == 'cancel':
            exit(0)
        res_clus, min_distance = embed.find_closest_cluster(cluster_embedding, name_of_company, distance=distance)
        if res_clus:
            print(f'Кластер: {res_clus}\n'
                  f'Дистанция {distance}: {min_distance}')
        else:
            print('Подходящий кластер не найден')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process inputs.')
    parser.add_argument('-i', '--implementation', type=str,
                        help='What implementation of embedding to use', default='USE')
    args = parser.parse_args()
    main(args.implementation)
