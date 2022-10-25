# ITMO.DUBL
В данном репозитории хранится код проекта для реализации поиска похожих компаний по их названию.

Основная идея подхода заключается в том, чтобы найти эмбеддинги названий компаний, а также возможных кластеров названий, чтобы при поиске похожих компаний по расстоянию между эмбеддингами решить, присутсвуют ли в данных похожие названия компаний или нет

## Разведочный анализ данных
Разведочный анализ представлень [здесь](Exploratory_analysis.md)

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

## Проблемы в датасете
В датасете присутствуют пары не всех кластеров, пример:
В данных присутствуют следующие уникальные названия, которые по логике должны матчиться с друг другом
```
[' LANXESS Inc.', ' Lanxess AG', ' Lanxess Accounting GmbH', ' Lanxess Chemical (China) Co., Ltd.', ' Lanxess Hong Kong Limited', ' Lanxess International Trading (Shanghai) Co., Ltd.', ' Lanxess Manufacturing Netherlands B.V.', ' Lanxess Sas',]
```
Но в датасете этого не [происходит](Cluster_generation.ipynb):
```
name = ' LANXESS Inc.'
couples = train_ds[((train_ds['name_1'] == name) | (train_ds['name_2'] == name)) & (train_ds['is_duplicate'] == 1)]
print(len(couples)) # 0
```
![image](https://user-images.githubusercontent.com/75368806/197779985-101228da-1966-41f6-8a70-2acad9549172.png)
Еще один пример:
```
 ['BASF CENRTAL ASIA LLP', 'BASF Central Asia LLP'],
 
 ['Basf Quimica Colombiana S.A.', "Basf's Paper Chemicals (Huizhou) Co., Ltd.", 'Basf New Zealand Ltd.', 'Basf Bangladesh Ltd.', 'Basf Co., Ltd.', 'Basf Co., Ltd. Yeosu', 'Basf Mexicana S.A. De C.V.', 'Basf Corp.', 'Basf Pakistan (Private) Ltd.', 'Basf Construction Chemicals', 'Basf Auxiliary Chemicals', 'Basf Japan Ltd.', 'Basf Construction Chemicals Ua', 'Basf De Costa Rica Sociedad Anonima', 'Basf Peruana S.A.', 'Basf India Ltd.', 'Basf Pakistan Ltd.', 'Basf Corporation', 'Basf (China) Co., Ltd. Shanghai', 'Basf Colors & Effects Usa Llc', 'Basf Chile S A', 'Basf Turk Kimya San Ve Tic.Tld.Sti', 'Bdp International Basf Imp.', 'Basf India', 'Basf Turk Kimya San.Ve Tic Ltd.Sti', 'Basf Finlay Pvt., Ltd.', 'Basf Sa', 'Basf Turk Kimya San. Ve Tic.Sti', 'Basf Japan Ltd. 6 10 1 Roppongi', 'Basf Chile S.A.']
```
По логике эти два кластера должны быть совместны, но пары из двух названий замыкаются сами на себя:
![image](https://user-images.githubusercontent.com/75368806/197780787-0dfea324-c6c4-4e4d-be83-aefed4e77708.png)



## Подходы к векторизации текста
BugOfWords, TF-IDF, Word2Vec, [Doc2Vec](D2V_implementation.ipynb) и др. алгоритмы использующие внутри себя словарь, по которому происходит векторизация текста не очень подходят для данной задачи по следующим причинам:
- Есть вероятность словить ошибку OutOfDictionary, когда в запросе на поиск похожих компаний будет слово, которое не встречалось в исходном словаре при обучении;
- При добавлении новых названий компаний, векторы нужно будет персчитывать заново;
- Низкое качество векторизации, которое уступает нейросетевым подходам.

Использование [нейросетевых](USE_implementation.ipynb) подходов для векторизации текста:
- Универсальны, так как не используют словарь. Но универсальность не всегда хорошо складывается на точности в использования сети в определенном домене;
- Требуют больше ресурсов для векторзации текста, но при этом позволяют для каждого примера использовать один embedding, что позволяет единожды сделать обсчёт для всех семплов;


## Использование алгоритма
Для тестирвания работы алгоритма:
1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Запустите основной файл:

```
python main.py -i "USE"
```
Возможные значения для параметра -i:
- "USE". Использование сети Universal Sentence Encoder для созданя эмбеддингов названий компаний

