import numpy as np
import tensorflow_hub as hub


class USE:
    def __init__(self):
        super().__init__()
        self.embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    def __call__(self, x: str):
        return self.embed([x])[0].numpy()

    def find_closest_cluster(self, cluster_embedding: dict, name_of_company: str, distance: str = 'l1',
                             thrsh: float = None):
        name_embedding = self(name_of_company)
        min_distance = 10e12
        result_cluster = None
        num_of_cluster = None
        for key in cluster_embedding:
            cluster = cluster_embedding[key]['cluster']
            cluster_embed = cluster_embedding[key]['embedding']
            if distance == 'l1':
                distnc = np.abs(cluster_embed - name_embedding).sum()
            else:
                distnc = (((cluster_embed - name_embedding) ** 2).sum()) ** (1 / 2)
            if distnc < min_distance:
                min_distance = distnc
                result_cluster = cluster
                num_of_cluster = key

        if thrsh is not None:
            if min_distance > thrsh:
                return None, None, None

        return result_cluster, min_distance, num_of_cluster
