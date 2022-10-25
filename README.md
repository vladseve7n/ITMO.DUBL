# ITMO.DUBL
В данном репозитории хранится код проекта для реализации поиска похожих компаний по их названию.

Основная идея подхода заключается в том, чтобы найти эмбеддинги названий компаний, а также возможных кластеров названий, чтобы при поиске похожих компаний по расстоянию между эмбеддингами решить, присутсвуют ли в данных похожие названия компаний или нет

## Генерация кластеров из тренировочного датасета
Для того, чтобы применить алгоритм поиска ближайшего кластера названий компаний для подхода с использованием эмбеддингов изображений был сформирован датасет кластеров, который находится [здесь](dataset/clusters.json)

Он представляет из себя json файл, где по тегу "clusters" находится список списков кластеров названий компаний:  

```json
{
  "clusters": [
    ["ALFAGOMMA INDUSTRIAL SPA", " Alfagomma"], 
    [" SO.F.TER. SPA", "Softer Us Inc."],
    ...,
  ]
}
```

Код генерации кластеров представлен в данном [файле](Cluster_generation.ipynb)  

Разведочный анализ представлень [здесь](Exploratory_analysis.md)
