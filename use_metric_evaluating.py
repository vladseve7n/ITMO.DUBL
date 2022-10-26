import numpy as np
import pandas as pd
import requests
from sklearn.metrics import f1_score, accuracy_score
from utils.USEImplement import USE
from utils.tools import preprocess_fn
from copy import deepcopy
implementations = {
    'USE': USE
}

embed = implementations['USE']()

cluster_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/clusters.json'
train_ds_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/train.csv'
name_wo_couple_url = 'https://raw.githubusercontent.com/vladseve7n/ITMO.DUBL/main/dataset/name_wo_couple.json'

train_ds_ = pd.read_csv(train_ds_url).drop('pair_id', axis=1)
clusters_ = requests.get(cluster_url).json()['clusters']
name_wo_couple_ = requests.get(name_wo_couple_url).json()['name_wo_couple']
unique_names = list(np.unique(np.append(train_ds_.name_1.values, train_ds_.name_2.values)))

metrics_df = pd.DataFrame({'implementation': [],
                           'preprocess': [],
                           'mean_type': [],
                           'distance': [],
                           'threshold': [],
                           'f1': [],
                           'accuracy': []})

for preprocess in ['lower_clean', 'lower', 'none']:
    # Предпроцессинг информации
    clusters = deepcopy(clusters_)
    name_wo_couple = deepcopy(name_wo_couple_)

    for cluster_id in range(len(clusters)):
        for name_id in range(len(clusters[cluster_id])):
            clusters[cluster_id][name_id] = preprocess_fn(preprocess, clusters[cluster_id][name_id])

    for name_id in range(len(name_wo_couple)):
        name_wo_couple[name_id] = preprocess_fn(preprocess, name_wo_couple[name_id])

    embeddings_dict = {preprocess_fn(preprocess, name): embed(preprocess_fn(preprocess, name)) for name in unique_names}

    for mean_type in ['mean', 'median']:
        cluster_embedding = {}
        for num, cluster in enumerate(clusters):
            cluster_embedding[num] = {}
            cluster_embedding[num]['cluster'] = cluster
            if mean_type == 'mean':
                embed_cluster = np.mean(np.array([embeddings_dict[x] for x in cluster]), axis=0)
            else:
                embed_cluster = np.median(np.array([embeddings_dict[x] for x in cluster]), axis=0)
            cluster_embedding[num]['embedding'] = embed_cluster

        for distance in ['l1', 'l2']:
            # Считаем метрики для значений, которые попадают в кластер
            cluster_answers = []
            distances = []
            # Получаем все ответы алгоритма для кластеров и для имен без кластеров
            for cluster in clusters:
                for sample in cluster:
                    result_cluster, min_distance = embed.find_closest_cluster(cluster_embedding, sample,
                                                                              distance=distance)
                    distances.append(min_distance)
                    cluster_answers.append([sample, result_cluster, min_distance])

            print(f'Длина имен с известными кластерами : {len(distances)}')
            name_wo_couple_answers = []
            for sample in name_wo_couple:
                result_cluster, min_distance = embed.find_closest_cluster(cluster_embedding, sample,
                                                                          distance=distance)
                distances.append(min_distance)
                name_wo_couple_answers.append([sample, min_distance])
            print(f'Длина имен без кластеров : {len(name_wo_couple)}')

            # Проходимся с thresh
            for threshold in np.linspace(min(distances), max(distances), 64):
                y, y_pred = [], []

                # Разбираемся с именами для которых нам известен кластер
                for answer in cluster_answers:
                    y.append(1)  # Ставим в ответ 1 так, как мы точно знаем, что кластер есть
                    sample, result_cluster, min_distance = answer

                    # Если минимальное расстояние больше threshold'a
                    if min_distance > threshold:
                        y_pred.append(0)  # То мы отдаем в ответе, что кластера нет
                    elif sample in result_cluster:
                        y_pred.append(1)  # Если кластер есть и наше имя в нём присутствует, то кластер правильный
                    else:
                        y_pred.append(0)  # В случае, если кластер все же нашелся и нашего имени там не оказалось
                        # То в таком случае кластер неправильный

                # Разбираемся с именами кластер, которых нам не известен
                for answer in name_wo_couple_answers:
                    sample, min_distance = answer
                    y.append(0)
                    if min_distance > threshold:
                        y_pred.append(0)
                    else:
                        y_pred.append(1)

                f1 = f1_score(y, y_pred)
                accuracy = accuracy_score(y, y_pred)

                result = ["USE", preprocess, mean_type, distance, threshold, f1, accuracy]

                print(result)
                metrics_df.loc[len(metrics_df)] = result

                metrics_df.to_csv('use_metric_evaluating_result.csv')
