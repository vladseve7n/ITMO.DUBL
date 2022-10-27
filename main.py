import argparse

import numpy as np
import pandas as pd
import requests

from utils.Timer import Timer
from utils.USEImplement import USE
from utils.tools import preprocess_fn

cluster_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/clusters.json'
train_ds_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/train.csv'

implementations = {
    'USE': USE
}

t = Timer()


def main(implemntation: str = 'USE', preprocess: str = 'lower_clean', mean_type: str = 'median',
         distance: str = 'l1', threshold: float = 11.877):
    print('Data is loading...')
    # Загружаем данные
    train_ds = pd.read_csv(train_ds_url).drop('pair_id', axis=1)

    clusters = requests.get(cluster_url).json()['clusters']
    for cluster_id in range(len(clusters)):
        for name_id in range(len(clusters[cluster_id])):
            clusters[cluster_id][name_id] = preprocess_fn(preprocess, clusters[cluster_id][name_id])

    embed = implementations[implemntation]()

    unique_names = list(np.unique(np.append(train_ds.name_1.values, train_ds.name_2.values)))

    # Для каждого уникального названия ищем embedding
    t.start('emb_making')
    embeddings_dict = {preprocess_fn(preprocess, name): embed(preprocess_fn(preprocess, name)) for name in unique_names}
    print(f'Making embeddings take {t.stop("emb_making")} for {len(embeddings_dict)} samples. '
          f'{t.stop("emb_making") / len(embeddings_dict)} sec. for 1 sample')

    # Считаем embedding для каждого кластера
    cluster_embedding = {}
    for num, cluster in enumerate(clusters):
        cluster_embedding[num] = {}
        cluster_embedding[num]['cluster'] = cluster
        if mean_type == 'mean':
            embed_cluster = np.mean(np.array([embeddings_dict[x] for x in cluster]), axis=0)
        else:
            embed_cluster = np.median(np.array([embeddings_dict[x] for x in cluster]), axis=0)
        cluster_embedding[num]['embedding'] = embed_cluster

    # Далее по запросу сравниваем embedding полученного слова с embedding'ами кластеров
    while True:
        name_of_company = input('Введите название компании для поиска кластера:\n')

        if name_of_company.lower() == 'cancel':
            exit(0)
        t.start('res_spd')
        res_clus, min_distance, num_of_cluster = embed.find_closest_cluster(cluster_embedding,
                                                                            preprocess_fn(preprocess, name_of_company),
                                                                            distance=distance, thrsh=threshold)

        if res_clus:
            print(f'Кластер: {res_clus}\n'
                  f'Дистанция {distance}: {min_distance}')
            if name_of_company not in cluster_embedding[num_of_cluster]['cluster']:
                cluster_embedding[num_of_cluster]['cluster'].append(name_of_company)
                embeddings_dict[name_of_company] = embed(name_of_company)
                cls_emb = np.array([embeddings_dict[x] for x in cluster_embedding[num_of_cluster]['cluster']])
                if mean_type == 'mean':
                    embed_cluster = np.mean(cls_emb, axis=0)
                else:
                    embed_cluster = np.median(cls_emb, axis=0)
                cluster_embedding[num_of_cluster]['embedding'] = embed_cluster
                print(f'Название {name_of_company} добавлено в кластер!')

        else:
            print('Подходящий кластер не найден')
            embeddings_dict[name_of_company] = embed(name_of_company)
            next_key = len(cluster_embedding) + 1
            cluster_embedding[next_key] = {}
            cluster_embedding[next_key]['cluster'] = [name_of_company]
            cluster_embedding[next_key]['embedding'] = embeddings_dict[name_of_company]
            print('Создаем новый кластер с этой компанией')

        print(f"Speed of request: {t.stop('res_spd')}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process inputs.')
    parser.add_argument('-i', '--implementation', type=str,
                        help='What implementation of embedding to use', default='USE')
    parser.add_argument('-p', '--preprocess', help='What kind of preprocess to use', type=str,
                        default='lower_clean')
    parser.add_argument('-d', '--distance', help='What kind of distance between embeddings to use', type=str,
                        default='l1')
    parser.add_argument('-m', '--mean_type', help='What kind of meaning to use in clusters', type=str,
                        default='median')
    parser.add_argument('-t', '--threshold', type=float,
                        help='What kind of threshold to use in the way to make a choice about name matching',
                        default=11.877)
    args = parser.parse_args()
    main(args.implementation, args.preprocess, args.mean_type, args.distance, args.threshold)
