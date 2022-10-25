Exploratory analysis
==


```python
import pandas as pd
import seaborn as sns
```

Внешний вид данных


```python
data=pd.read_csv('train.csv')
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pair_id</th>
      <th>name_1</th>
      <th>name_2</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Iko Industries Ltd.</td>
      <td>Enormous Industrial Trade Pvt., Ltd.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Apcotex Industries Ltd.</td>
      <td>Technocraft Industries (India) Ltd.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Rishichem Distributors Pvt., Ltd.</td>
      <td>Dsa</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Powermax Rubber Factory</td>
      <td>Co. One</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Tress A/S</td>
      <td>Longyou Industries Park Zhejiang</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>497814</th>
      <td>497815</td>
      <td>BIT-MAT PRODUCTS</td>
      <td>The Goodyear Tire and Rubber Company</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497815</th>
      <td>497816</td>
      <td>Bnd Trading Co., Ltd.</td>
      <td>Zhong Shan Yue Liang Economy&amp; Trade Imp. &amp; Exp...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497816</th>
      <td>497817</td>
      <td>Xeikon Industrial Co., Ltd. Of Dongguan City</td>
      <td>Yi Cheng Trading Co., Ltd. Of Dongguan City</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497817</th>
      <td>497818</td>
      <td>Shanghai Kechuan Trading Co., Ltd.</td>
      <td>Shanghai M&amp;G Stationery Inc.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497818</th>
      <td>497819</td>
      <td>Dih Wei Industries Co.</td>
      <td>Burlington Industries Corporate</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>497819 rows × 4 columns</p>
</div>



Пример списка строк для одной компании. Для названия ЭВЕРИ ДЕННИСОН нет ни одного "совпадающего"


```python
data[((data.name_1=='ЭВЕРИ ДЕННИСОН')|(data.name_2=='ЭВЕРИ ДЕННИСОН'))].iloc[100:,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pair_id</th>
      <th>name_1</th>
      <th>name_2</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>393625</th>
      <td>393626</td>
      <td>CLOPAY</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>394052</th>
      <td>394053</td>
      <td>copernit spa</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>406187</th>
      <td>406188</td>
      <td>DYNASOL ELASTOMEROS, S.A.U</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>407598</th>
      <td>407599</td>
      <td>UTEKSOL</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>409725</th>
      <td>409726</td>
      <td>SWISSPOR (VAPAROID)</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>411476</th>
      <td>411477</td>
      <td>Carlisle Coatings &amp; Waterproofing, Inc.</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>412170</th>
      <td>412171</td>
      <td>Celu buvniecibas sabiedriba Igate Ltd</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>417434</th>
      <td>417435</td>
      <td>LG Chem Ltd.</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>421560</th>
      <td>421561</td>
      <td>Automotive Performance Material</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>424428</th>
      <td>424429</td>
      <td>RASCO BITUMENTECHNIC GMBH</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>424433</th>
      <td>424434</td>
      <td>Versalis S.p.A.</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>435179</th>
      <td>435180</td>
      <td>ALBEMARLE GREEN CREST</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>440135</th>
      <td>440136</td>
      <td>COPERNIT</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>440917</th>
      <td>440918</td>
      <td>LAGAN BITUMEN LTD</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>447414</th>
      <td>447415</td>
      <td>Coco Paving Inc.</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>451909</th>
      <td>451910</td>
      <td>WARDEN ASPHALT</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>452172</th>
      <td>452173</td>
      <td>Alpha Adhesives &amp; Sealants Ltd</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>460583</th>
      <td>460584</td>
      <td>JSR Corporation</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>475620</th>
      <td>475621</td>
      <td>Synthos Kralupy</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>476716</th>
      <td>476717</td>
      <td>C. Hasse &amp; Sohn Inh. E. Radecke Gmbh &amp; Co. Kg</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>480475</th>
      <td>480476</td>
      <td>Sinopec</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>481019</th>
      <td>481020</td>
      <td>COLAS POLSKA</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>481480</th>
      <td>481481</td>
      <td>BASF CENRTAL ASIA LLP</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>484257</th>
      <td>484258</td>
      <td>Lusocopla - Fábrica de Colas Industriais, Lda</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>485171</th>
      <td>485172</td>
      <td>Compogal - IndUstria De PolImeros, S.A.</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>487039</th>
      <td>487040</td>
      <td>DUKT</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>487931</th>
      <td>487932</td>
      <td>CENGIZ İNŞAAT</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
    <tr>
      <th>495064</th>
      <td>495065</td>
      <td>ELASTRON KIMYA</td>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



В представленных столбцах примерно по 17.7 тысяч уникальных наименований


```python
print(len(data['name_1'].unique()))
print(len(data['name_2'].unique()))
```

    17656
    17684
    

Подавляющее большинство наименований представлено в обеих колонках


```python
k1, k2=0, 0
name_1_unique=data['name_1'].unique()
name_2_unique=data['name_2'].unique()

for x in name_1_unique: 
    if x in name_2_unique: k1+=1
for x in name_2_unique: 
    if x in name_1_unique: k2+=1
print(k1, k2)
```

    17318 17318
    

Данные крайне несбалансированы - количетсво совпадений составляет менее 1% от числа наблюдений


```python
data.groupby('is_duplicate')[['pair_id']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pair_id</th>
    </tr>
    <tr>
      <th>is_duplicate</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>494161</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3658</td>
    </tr>
  </tbody>
</table>
</div>



Компании из колонки name_1, имеющие более одного совпадения


```python
df=data.groupby('name_1').sum('is_duplicate').reset_index(drop=False).sort_values('is_duplicate', ascending=False)
df[df.is_duplicate>1].reset_index(drop=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_1</th>
      <th>pair_id</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bridgestone India</td>
      <td>15658188</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bridgestone India Pvt., Ltd.</td>
      <td>11741099</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bridgestone Ncr</td>
      <td>10214884</td>
      <td>34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bridgestone Tire</td>
      <td>9531110</td>
      <td>34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bridgestone Tire Co.</td>
      <td>10727336</td>
      <td>34</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>443</th>
      <td>Zeon Europe Gmbh</td>
      <td>799553</td>
      <td>2</td>
    </tr>
    <tr>
      <th>444</th>
      <td>Soprema Drummondville</td>
      <td>602495</td>
      <td>2</td>
    </tr>
    <tr>
      <th>445</th>
      <td>Zeon Chemicals L P</td>
      <td>16314314</td>
      <td>2</td>
    </tr>
    <tr>
      <th>446</th>
      <td>Azienda Generale Italiana Petroli</td>
      <td>31378220</td>
      <td>2</td>
    </tr>
    <tr>
      <th>447</th>
      <td>Soprema Chilliwack</td>
      <td>859416</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>448 rows × 3 columns</p>
</div>



Гистограмма распределения значений из датасета выше


```python
fig=df[df.is_duplicate>1]['is_duplicate'].hist(bins=30,figsize=(15, 10))
```


    
![png](output_15_0.png)
    


Компании из колонки name_1, имеющие одно совпадение.


```python
df[df.is_duplicate==1].reset_index(drop=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_1</th>
      <th>pair_id</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BUHLER AG</td>
      <td>62589</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KIMBERLY-CLARK</td>
      <td>69551</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KIMBERLY-CLARK EUROPE LTD</td>
      <td>60439</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>KIMBERLY-CLARK (NANJING) CARE PRODUCTS CO., LTD.</td>
      <td>249033</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tokyo Zairyo (U.S.A.) Inc.</td>
      <td>177642</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>535</th>
      <td>Zeon Chemicals (Thailand) Co., Ltd</td>
      <td>236997</td>
      <td>1</td>
    </tr>
    <tr>
      <th>536</th>
      <td>Zeon Belts Private Ltd.</td>
      <td>7632365</td>
      <td>1</td>
    </tr>
    <tr>
      <th>537</th>
      <td>Zeon Advanced Polymix Co., Ltd.</td>
      <td>880567</td>
      <td>1</td>
    </tr>
    <tr>
      <th>538</th>
      <td>Zeon F&amp;B Co., Ltd</td>
      <td>475482</td>
      <td>1</td>
    </tr>
    <tr>
      <th>539</th>
      <td>Zeon Asia Pte Ltd</td>
      <td>281102</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>540 rows × 3 columns</p>
</div>



Полных совпадений чуть меньше 30


```python
data[data.name_1==data.name_2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pair_id</th>
      <th>name_1</th>
      <th>name_2</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5117</th>
      <td>5118</td>
      <td>ООО"ИМПОРТ МОДА"</td>
      <td>ООО"ИМПОРТ МОДА"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12160</th>
      <td>12161</td>
      <td>ООО"ГУЧЧИ РУС"</td>
      <td>ООО"ГУЧЧИ РУС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14857</th>
      <td>14858</td>
      <td>Lohmann GmbH &amp; Co. KG</td>
      <td>Lohmann GmbH &amp; Co. KG</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25949</th>
      <td>25950</td>
      <td>ООО"ПРИВАТ ТРЭЙД"</td>
      <td>ООО"ПРИВАТ ТРЭЙД"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38345</th>
      <td>38346</td>
      <td>ООО"СПЕЦИАЛЬНОЕ ОБОРУДОВАНИЕ"</td>
      <td>ООО"СПЕЦИАЛЬНОЕ ОБОРУДОВАНИЕ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>139209</th>
      <td>139210</td>
      <td>ООО"ФАВОРИТ СТАЙЛ</td>
      <td>ООО"ФАВОРИТ СТАЙЛ</td>
      <td>1</td>
    </tr>
    <tr>
      <th>150207</th>
      <td>150208</td>
      <td>ООО"ОЗОН ГИЙИМ РСЙ"</td>
      <td>ООО"ОЗОН ГИЙИМ РСЙ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>151690</th>
      <td>151691</td>
      <td>ООО "ХИММАРКЕТ"</td>
      <td>ООО "ХИММАРКЕТ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>169770</th>
      <td>169771</td>
      <td>ООО"ВЕРТИКАЛЬ СПОРТ"</td>
      <td>ООО"ВЕРТИКАЛЬ СПОРТ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>226434</th>
      <td>226435</td>
      <td>ООО "СТАРКОМ"</td>
      <td>ООО "СТАРКОМ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>227269</th>
      <td>227270</td>
      <td>RTL-INDUCTIVES OY</td>
      <td>RTL-INDUCTIVES OY</td>
      <td>1</td>
    </tr>
    <tr>
      <th>235444</th>
      <td>235445</td>
      <td>АО"ЕГОРЬЕВСК-ОБУВЬ"</td>
      <td>АО"ЕГОРЬЕВСК-ОБУВЬ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>247799</th>
      <td>247800</td>
      <td>Adhesives Research, Inc.</td>
      <td>Adhesives Research, Inc.</td>
      <td>1</td>
    </tr>
    <tr>
      <th>251290</th>
      <td>251291</td>
      <td>ООО"КАМИМП"</td>
      <td>ООО"КАМИМП"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>308463</th>
      <td>308464</td>
      <td>ООО"ЛО ТРЕЙД"</td>
      <td>ООО"ЛО ТРЕЙД"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>332968</th>
      <td>332969</td>
      <td>ООО "ХУСКВАРНА"</td>
      <td>ООО "ХУСКВАРНА"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>339736</th>
      <td>339737</td>
      <td>ООО"ДОМ ОДЕЖДЫ"</td>
      <td>ООО"ДОМ ОДЕЖДЫ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>360395</th>
      <td>360396</td>
      <td>ООО"АРТСАНА РУС"</td>
      <td>ООО"АРТСАНА РУС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>366261</th>
      <td>366262</td>
      <td>Zeon Europe Gmbh</td>
      <td>Zeon Europe Gmbh</td>
      <td>1</td>
    </tr>
    <tr>
      <th>418450</th>
      <td>418451</td>
      <td>ООО"ЭЛ КЕРАМИКА"</td>
      <td>ООО"ЭЛ КЕРАМИКА"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>426246</th>
      <td>426247</td>
      <td>ООО"ОЛИМП"</td>
      <td>ООО"ОЛИМП"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>449388</th>
      <td>449389</td>
      <td>ООО"ИМПЭКС"</td>
      <td>ООО"ИМПЭКС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>458348</th>
      <td>458349</td>
      <td>ООО"ГЭЛАКСИ КАРГО СЕРВИС"</td>
      <td>ООО"ГЭЛАКСИ КАРГО СЕРВИС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>476490</th>
      <td>476491</td>
      <td>ООО"ОРТГРАФ"</td>
      <td>ООО"ОРТГРАФ"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>479647</th>
      <td>479648</td>
      <td>ООО "КЬЮ ЭКСПРЕСС"</td>
      <td>ООО "КЬЮ ЭКСПРЕСС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>481655</th>
      <td>481656</td>
      <td>ООО "БРААС-ДСК 1"</td>
      <td>ООО "БРААС-ДСК 1"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>488071</th>
      <td>488072</td>
      <td>ООО "МАНДЕРС"</td>
      <td>ООО "МАНДЕРС"</td>
      <td>1</td>
    </tr>
    <tr>
      <th>488736</th>
      <td>488737</td>
      <td>ООО"НОВЫЙ МИР"</td>
      <td>ООО"НОВЫЙ МИР"</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



Корреляция Bag of words
==


```python
import numpy as np
import re
```

Данные


```python
data=pd.read_csv('train.csv')
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pair_id</th>
      <th>name_1</th>
      <th>name_2</th>
      <th>is_duplicate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Iko Industries Ltd.</td>
      <td>Enormous Industrial Trade Pvt., Ltd.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Apcotex Industries Ltd.</td>
      <td>Technocraft Industries (India) Ltd.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Rishichem Distributors Pvt., Ltd.</td>
      <td>Dsa</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Powermax Rubber Factory</td>
      <td>Co. One</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Tress A/S</td>
      <td>Longyou Industries Park Zhejiang</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>497814</th>
      <td>497815</td>
      <td>BIT-MAT PRODUCTS</td>
      <td>The Goodyear Tire and Rubber Company</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497815</th>
      <td>497816</td>
      <td>Bnd Trading Co., Ltd.</td>
      <td>Zhong Shan Yue Liang Economy&amp; Trade Imp. &amp; Exp...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497816</th>
      <td>497817</td>
      <td>Xeikon Industrial Co., Ltd. Of Dongguan City</td>
      <td>Yi Cheng Trading Co., Ltd. Of Dongguan City</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497817</th>
      <td>497818</td>
      <td>Shanghai Kechuan Trading Co., Ltd.</td>
      <td>Shanghai M&amp;G Stationery Inc.</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497818</th>
      <td>497819</td>
      <td>Dih Wei Industries Co.</td>
      <td>Burlington Industries Corporate</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>497819 rows × 4 columns</p>
</div>



Составляем датасет с уникальными наименованиями, присваиваем наименованиям id


```python
name_1_unique=data['name_1'].unique()
name_2_unique=data['name_2'].unique()

names_all=list(name_1_unique)
names_all.extend(list(name_2_unique))
names_all=list(np.unique(np.array(names_all)))
```


```python
data_names_collections=pd.DataFrame({'names':names_all})
#data_names_collections['id']=data_names_collections.index
data_names_collections
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alfagomma</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CONTITECH TRANSPORTBANDSYSTEME GMBH</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LANXESS Inc.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lanxess AG</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lanxess Accounting GmbH</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>18017</th>
      <td>ФИЛИАЛ КОМПАНИИ ЭКСОН НЕФТЕГАЗ ЛИМИТЕД</td>
    </tr>
    <tr>
      <th>18018</th>
      <td>ФИЛИАЛ КОМПАНИИ"ЭКСОН НЕФТЕГАЗ ЛИМИТЕД"</td>
    </tr>
    <tr>
      <th>18019</th>
      <td>ХИМИНВЕСТ ГРУПП, ООО</td>
    </tr>
    <tr>
      <th>18020</th>
      <td>ХИМИНВЕСТ НПФ, ООО</td>
    </tr>
    <tr>
      <th>18021</th>
      <td>ЭВЕРИ ДЕННИСОН</td>
    </tr>
  </tbody>
</table>
<p>18022 rows × 1 columns</p>
</div>



Убираем из всех наименований кавычки и приводим к нижнему регистру


```python
def quotes_mover(a):
    return a.replace('"',' "').replace('"','').replace(')','').replace('(','').lower()
```


```python
data_names_collections['names_cleaned']=data_names_collections['names'].apply(quotes_mover)
```

Превратим каждое предложение в список слов


```python
data_names_collections['collections']=data_names_collections['names_cleaned'].apply(lambda x: x.split(' '))
```


```python
data_names_collections
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>names</th>
      <th>names_cleaned</th>
      <th>collections</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alfagomma</td>
      <td>alfagomma</td>
      <td>[, alfagomma]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CONTITECH TRANSPORTBANDSYSTEME GMBH</td>
      <td>contitech transportbandsysteme gmbh</td>
      <td>[, contitech, transportbandsysteme, gmbh]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LANXESS Inc.</td>
      <td>lanxess inc.</td>
      <td>[, lanxess, inc.]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lanxess AG</td>
      <td>lanxess ag</td>
      <td>[, lanxess, ag]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lanxess Accounting GmbH</td>
      <td>lanxess accounting gmbh</td>
      <td>[, lanxess, accounting, gmbh]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18017</th>
      <td>ФИЛИАЛ КОМПАНИИ ЭКСОН НЕФТЕГАЗ ЛИМИТЕД</td>
      <td>филиал компании эксон нефтегаз лимитед</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед]</td>
    </tr>
    <tr>
      <th>18018</th>
      <td>ФИЛИАЛ КОМПАНИИ"ЭКСОН НЕФТЕГАЗ ЛИМИТЕД"</td>
      <td>филиал компании эксон нефтегаз лимитед</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед, ]</td>
    </tr>
    <tr>
      <th>18019</th>
      <td>ХИМИНВЕСТ ГРУПП, ООО</td>
      <td>химинвест групп, ооо</td>
      <td>[химинвест, групп,, ооо]</td>
    </tr>
    <tr>
      <th>18020</th>
      <td>ХИМИНВЕСТ НПФ, ООО</td>
      <td>химинвест нпф, ооо</td>
      <td>[химинвест, нпф,, ооо]</td>
    </tr>
    <tr>
      <th>18021</th>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>эвери деннисон</td>
      <td>[эвери, деннисон]</td>
    </tr>
  </tbody>
</table>
<p>18022 rows × 3 columns</p>
</div>



Считаем количество всех слов с повторениями


```python
def word_quantity(sentences):    
    words = []    
    for sentence in sentences:               
        words.extend(sentence)            
   # words = sorted(list(set(words)))    
    return words
```


```python
vocab=word_quantity(data_names_collections['collections'])
```




    ['',
     'alfagomma',
     '',
     'contitech',
     'transportbandsysteme',
     'gmbh',
     '',
     'lanxess',
     'inc.',
     '',
     'lanxess',
     'ag',
     '',
     'lanxess',
     'accounting',
     'gmbh',
     '',
     'lanxess',
     'chemical',
     'china',
     'co.,',
     'ltd.',
     '',
     'lanxess',
     'hong',
     'kong',
     'limited',
     '',
     'lanxess',
     'international',
     'trading',
     'shanghai',
     'co.,',
     'ltd.',
     '',
     'lanxess',
     'manufacturing',
     'netherlands',
     'b.v.',
     '',
     'lanxess',
     'sas',
     '',
     'so.f.ter.',
     'spa',
     '',
     'total',
     'oil',
     'india',
     'private',
     'limited,',
     '',
     'total',
     "'hengshui",
     'mechanical',
     '&',
     'electrical',
     'building',
     "co.,ltd.'",
     'camso',
     'loadstar',
     '',
     'pivt',
     '',
     'ltd.',
     '***',
     'ооо',
     '',
     'интерсвет',
     '',
     '***',
     'ооо',
     '',
     'интерторг',
     '',
     '***',
     'ооо',
     '',
     'интертулз',
     '',
     '***',
     'ооо',
     '',
     'интербалк',
     '',
     '***',
     'ооо',
     '',
     'сато',
     '',
     '***',
     'полимаркет,',
     'ооо',
     '1',
     '4103412224',
     'tel',
     'ex',
     '1',
     '410341',
     '23',
     '1',
     '7044245522',
     'tel',
     'ex',
     '1',
     '704424',
     '56',
     '1',
     '8168912400',
     'tel',
     'ex',
     '1',
     '816891',
     '76',
     '1',
     'dhl',
     'global',
     'forwarding',
     '1',
     'st',
     'notify',
     'party',
     '1',
     'st',
     'world',
     'medical',
     'supplies',
     'solution',
     'inc.',
     '10841',
     'ambassador',
     'drive',
     '123',
     'e',
     'latin',
     'america',
     's',
     'de',
     'rl',
     'de',
     'cv',
     '128',
     'yeouidaero',
     'youngdeungpo',
     'gu',
     '14',
     'th',
     'fl.',
     'guomao',
     'building',
     'hubin',
     '2',
     'nd',
     'bulkhaul',
     'usa',
     'inc.',
     '2',
     'nd',
     'norify',
     'party',
     'goodyear',
     'canada',
     'inc.',
     '2',
     'wedmore',
     'close',
     '21',
     'st',
     'century',
     'textiles',
     'ltd.',
     '210',
     'brands',
     'inc.',
     '210',
     'brands',
     'inc.',
     'dba',
     'canterbury',
     'usa',
     '210',
     'brands',
     'inc./canterbury',
     'offi',
     '2k',
     'polymer',
     'systems',
     'ltd',
     '',
     '3',
     'a',
     'pakistan',
     '3',
     'ds',
     'traders',
     '3',
     'k',
     'treads',
     'pvt',
     'ltd.',
     '3',
     'm',
     'brockville',
     'tape',
     '3',
     'm',
     'do',
     'brasil',
     'ltda',
     '3',
     'm',
     'india',
     'ltd.',
     '3',
     'm',
     'manaus',
     'industria',
     'de',
     'produtos',
     'quimicos',
     'ltda',
     '3',
     'm',
     'united',
     'kingdom',
     'plc',
     '3',
     'm',
     'center',
     '3',
     'pl',
     'guys',
     '3',
     'plus',
     'logistics',
     'atlanta',
     '3',
     'plus',
     'logistics',
     'co.',
     '3',
     'rd',
     'floor',
     'gate',
     '4',
     'nanpu',
     'building',
     'tia',
     '3',
     's',
     'fabrications',
     'pvt',
     'ltd.',
     '31',
     'mcu',
     'movement',
     'control',
     'unit',
     '3475',
     'piedmont',
     'rd.',
     'ne',
     'suite',
     '1200',
     '360',
     'athletics',
     '365',
     'incorprated',
     '3702960',
     'dxl',
     '3m',
     'company',
     'nyse:mmm',
     '3m',
     'deutschland',
     'gmbh',
     '3m',
     'europe',
     '4',
     'd',
     'ag',
     'world',
     '4',
     'fleet',
     'group',
     'gmbh',
     '4',
     'states',
     'trucks',
     'inc.',
     '4',
     'stroke',
     'energies',
     '511',
     'foodservice',
     'co.,',
     'ltd.',
     '555',
     'north',
     'point',
     'center',
     'east',
     'ste',
     '7',
     'cargo',
     'corp.',
     '6000',
     '8220',
     'charles',
     'page',
     'blvd',
     'sand',
     'springs',
     ':',
     'precious',
     'cargo',
     'nig',
     'ltd.',
     ':',
     'rupahali',
     'bd',
     'a',
     '&',
     'a',
     'chapple',
     'sole',
     'manufactures',
     'a',
     '&',
     'a',
     'international',
     'a',
     '&',
     'a',
     'international',
     'trading',
     'private',
     'ltd.',
     'a',
     '&',
     'd',
     'international',
     'trading',
     'dmcc',
     'a',
     '&',
     'p',
     'solutions',
     's.a.',
     'de',
     'c.v.',
     'a',
     'b',
     'm',
     'international',
     'a',
     'b',
     'sellos',
     'y',
     'banca',
     'ltda',
     'a',
     'bu',
     'weber',
     'algeria',
     'sarl',
     'a',
     'c',
     'e',
     'd',
     'limitada',
     'a',
     'c',
     'p',
     'test',
     'co.',
     'inc.',
     'a',
     'cme',
     'bag',
     'co.',
     'a',
     'f',
     'traders',
     'a',
     'g',
     'pieco',
     'distribution',
     'corp',
     'a',
     'j',
     'enterprises',
     'a',
     'j',
     'industries',
     'l',
     'l',
     'c',
     'a',
     'k',
     'h',
     'construction',
     '&',
     'trading',
     'corp',
     'a',
     'k',
     'khan',
     'penfabric',
     'co.,',
     'ltd.',
     'a',
     'k',
     't',
     'a',
     'n',
     'deringer',
     'inc.',
     'a',
     'one',
     'techniques',
     'pvt',
     'ltd.',
     'a',
     'r',
     'imp.',
     '&',
     'exp.',
     'a',
     'r',
     'resin',
     'a',
     's',
     'i',
     'enterprise',
     'a',
     's',
     'international',
     'a',
     'shipping',
     'a',
     't',
     'c',
     'tecnoval',
     'sociedad',
     'anonima',
     'a',
     'taka',
     'paint',
     'foshan',
     'co.,',
     'ltd.',
     'a',
     'to',
     'z',
     'textile',
     'mills',
     'ltd.',
     'a',
     'value',
     'co.,',
     'ltd.',
     'a',
     'w',
     'baxter',
     'ghana',
     'ltd.',
     'a&',
     'b',
     'rahma',
     'imp.',
     '&',
     'exp.',
     'ltd.',
     'a&b',
     'rahma',
     'imp.',
     '&',
     'exp.',
     'ltd.',
     'a&r',
     'a&t',
     'international',
     'logistics',
     'ltd.',
     'a.',
     'b.',
     'exp.',
     'pvt',
     'ltd.',
     'a.',
     'hartrodt',
     'usa.',
     'inc.',
     'as',
     'agent',
     'a.',
     'lava',
     '&',
     'son',
     'co.',
     'a.',
     'n.',
     'deringer',
     'inc.',
     'a.',
     'schulman',
     'de',
     'mexico',
     's.a.',
     'de',
     'c.v.',
     'a.',
     'schuth',
     'gmb',
     'h',
     'a.',
     'westensee',
     '&',
     'partner',
     'rohstoff',
     'gmbh',
     'a.',
     'walecka',
     '&',
     'son',
     'storage',
     'warehouse',
     'a.a.industries',
     'a.b.rubber',
     'mill',
     'a.c.t.',
     'logistics',
     'inc.',
     'a.e.d',
     'cohen',
     'inc.',
     'a.g.',
     'india',
     'retail',
     'pvt.,',
     'ltd.',
     'a.j.',
     'trucco',
     'inc.',
     'a.k.enterprise',
     'a.l.',
     'a.l.textile',
     'prop.',
     'anuragkumar',
     'l.',
     'marda',
     'a.n.bikes',
     'sal',
     'a.p.i.',
     'a.p.i.',
     'applicazioni',
     'plastiche',
     'industriali',
     's.p.a.',
     'a.p.i.',
     'applicazioni',
     'plastiche',
     'industriali',
     'spa',
     'a.r.thermosets',
     'pvt.,',
     'ltd.',
     'a.schulman',
     'inc.',
     'a.t.s.',
     'synthetic',
     'pvt',
     'ltd.',
     'a.v.thomas',
     '&',
     'co.,',
     'ltd.',
     'a1',
     'badiah',
     'veterinary',
     'center',
     'a702',
     'no.319',
     'xianxia',
     'road',
     'ab',
     'chemicals',
     'limited',
     'abena',
     'international',
     'a/s',
     'abro',
     'industries,',
     'inc.',
     'adi',
     'salambo',
     'adi',
     'commerce',
     'adi',
     'commerce',
     'ltd',
     'adriatica',
     'bitumi',
     'adriatica',
     'bitumi',
     's.p.a.',
     'agilent',
     'technologies',
     'mfg',
     'gmbh',
     '&',
     'shipping',
     'department',
     'agip',
     'agip',
     '',
     '',
     'eni',
     'group',
     'albemarle',
     'green',
     'crest',
     '',
     'alfa',
     'laval',
     'lund',
     'ab',
     'alfagomma',
     'industrial',
     'spa',
     'alibesa',
     'allnex',
     'nuplex',
     'alpha',
     'trading',
     'amolplastic',
     'leetkooh',
     'co.',
     'ankara',
     'insaat',
     'ankara',
     'insaat',
     'ticaret',
     've',
     'sanayi',
     'limited',
     'sirketi',
     'ankara',
     'i̇nşaat',
     '',
     'anser',
     'sp.z',
     'o.o',
     'apcotex',
     'industries',
     'limited',
     'apcotex',
     'industries',
     'limited',
     'bse:523694',
     'api',
     'aplix',
     'appia',
     'liants',
     'ouest',
     'appia',
     'liants',
     'ouest',
     '',
     'alo',
     'aps',
     'aps',
     'paving',
     'stone',
     'inc',
     'aps',
     'paving&stone',
     'inc',
     'arlanxeo',
     '',
     'arlanxeo',
     'brasil',
     's.a.',
     'armacell',
     'poland',
     'sp.',
     'z.o.o',
     '',
     'as',
     'tekni̇k',
     'mühendi̇sli̇k',
     'yapi',
     've',
     'yalitim',
     'malzemeleri̇',
     'alümi̇nyum',
     've',
     'plasti̇k',
     'san.',
     'ti̇c.',
     'a.ş.',
     'asfaltos',
     'chova',
     '',
     'asgco',
     '',
     'complete',
     'conveyor',
     'solutions',
     '',
     'asia',
     'pharm',
     'pack',
     'aspa',
     'aspa',
     'gmbh',
     'assa',
     'assa',
     'roofing',
     'solutions',
     'atab',
     '',
     'atab',
     'nv',
     'automotive',
     'performance',
     'material',
     'apm',
     'aymod',
     'aa',
     'spinning',
     'mills',
     'ltd.',
     'aa',
     'synthetic',
     'fibers',
     'ltd.',
     'aaa',
     'acme',
     'rubber',
     'co.',
     'aaa',
     'enterprise',
     'fze',
     'aacm',
     'agence',
     'maritime',
     'sarl',
     'aacm',
     'sarl',
     'aakash',
     'plastopack',
     'pvt.,',
     'ltd.',
     'aalborz',
     'chemical',
     'llc',
     'dba',
     'aal',
     'chem',
     'aamp',
     'of',
     'america',
     'aanu',
     'enterprises',
     'aapko',
     'forwarders',
     'inc.',
     'aarchem',
     'corporation',
     "aaron's",
     'inc.',
     'aastha',
     'auto',
     'tech',
     'pvt.,',
     'ltd.',
     'aayush',
     'trading',
     'ltd.',
     'ab',
     'decor',
     'llc',
     'ab',
     'dogman',
     'ab',
     'imp.',
     '&',
     'exp.',
     'ab',
     'rideudstyr',
     'ab',
     'tech',
     'industries',
     'abasteligente',
     'sa',
     'de',
     'cv',
     'abastos',
     'cantabria',
     's.a.',
     'de',
     'c.v.',
     'abb',
     'inc.',
     'abb',
     'india',
     'ltd.',
     'abb',
     'mexico',
     's.a.',
     'de',
     'c.v.',
     'abba',
     'chem',
     'supply',
     'c.a.',
     'abbott',
     'laboratories',
     'de',
     'mexico',
     'sa',
     'de',
     'cv',
     'abc',
     'group',
     'do',
     'brasil',
     'ltda',
     'abc',
     'group',
     'enterprises',
     'abc',
     'industries',
     'abc',
     'project',
     'wll',
     'abdali',
     'kassim',
     'abdihamid',
     'ahmed',
     'mumin',
     'abdikadir',
     'mohmed',
     'hussein',
     'abdul',
     'aziz',
     'saad',
     'alqahtani',
     'trad.',
     'abdul',
     'aziz',
     'savul',
     'and',
     'co.',
     'abdul',
     'hai',
     'saiemi',
     'ltd.',
     'abdul',
     'hamid',
     'abdul',
     'rahim',
     'al',
     'emadi',
     'tr',
     'abdul',
     'kadir',
     'hussain',
     'abdul',
     'rahman',
     'abdul',
     'azeez',
     'al',
     'abdul',
     'wahab',
     '&',
     'abdul',
     'majeed',
     'trading',
     'co.',
     'abdul',
     'wahab',
     'trading',
     'abdulaahi',
     'hussen',
     'ali',
     'abdulkarim',
     'y',
     'munshi',
     'est.',
     'abdulla',
     'abdul',
     'razzaq',
     'readymade',
     'abdulla',
     'mohammed',
     'ali',
     'shamhan',
     'abdullah',
     'ayed',
     'al',
     'anaizi',
     'trading',
     'est',
     'abdullah',
     'hussain',
     'ali',
     'abdullah',
     'mohammad',
     'al',
     'muhary',
     'trading',
     'abg',
     'elizabeth',
     'warehouse',
     'abhi',
     'rubber',
     '&',
     'chemicals',
     'abir',
     'trade',
     'international',
     'ltd.',
     'able',
     'sales',
     'co.',
     'inc.',
     'able',
     'sheet',
     'metal',
     'inc.',
     'able',
     'speed',
     'mfg.',
     'philip',
     'able',
     'tech',
     'shenzhen',
     'industries',
     'abn',
     'imp.',
     '&',
     'exp.',
     'pvt.,',
     'ltd.',
     'abrasivos',
     's.a.',
     'abro',
     'distribution',
     'services',
     'absa',
     'bank',
     'ltd.',
     'absolute',
     'denim',
     'co.,',
     'ltd.',
     'abud',
     'imp.',
     '&',
     'exp.',
     'abudul',
     'ali',
     'abuja',
     'steel',
     'mills',
     'ltd.',
     'abul',
     'hassan',
     'building',
     'materials',
     'trad',
     'aburnet',
     'lanka',
     'pvt.,',
     'ltd.',
     'abv',
     'machine',
     'works',
     'pvt.,',
     'ltd.',
     'abyel',
     'inc.',
     'ac',
     'whalm',
     '&',
     'co',
     'attn:',
     'sam',
     'whalan',
     'acaa',
     'industrial',
     'sales.',
     'academie',
     'du',
     'pacifique',
     'sud',
     'academy',
     ...]



Считаем сколько раз встречается каждое слово


```python
def word_count(vocab): 
    counts = dict()  
    for word in vocab: 
        if word in counts: 
            counts[word] += 1 
        else: counts[word] = 1 
    return counts 
```

Получаем топ-10 слов, которые встречаются больше всего


```python
data_words_count=pd.DataFrame({'words':list(word_count(vocab).keys()),'quant':list(word_count(vocab).values())})
data_words_count.sort_values('quant',ascending=False).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>words</th>
      <th>quant</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>ltd.</td>
      <td>5356</td>
    </tr>
    <tr>
      <th>11</th>
      <td>co.,</td>
      <td>2559</td>
    </tr>
    <tr>
      <th>77</th>
      <td>de</td>
      <td>1732</td>
    </tr>
    <tr>
      <th>6</th>
      <td>inc.</td>
      <td>1538</td>
    </tr>
    <tr>
      <th>32</th>
      <td>&amp;</td>
      <td>897</td>
    </tr>
    <tr>
      <th>16</th>
      <td>international</td>
      <td>823</td>
    </tr>
    <tr>
      <th>138</th>
      <td>co.</td>
      <td>715</td>
    </tr>
    <tr>
      <th>436</th>
      <td>sa</td>
      <td>668</td>
    </tr>
    <tr>
      <th>289</th>
      <td>pvt.,</td>
      <td>631</td>
    </tr>
    <tr>
      <th>17</th>
      <td>trading</td>
      <td>593</td>
    </tr>
  </tbody>
</table>
</div>



Теперь создаем списки с учетом наиболее часто встречающихся слов (Несколько добавляем от себя)


```python
def word_extraction(sentence):    
    ignore = ['ltd.', "co.,", "de",'inc.','&','international','co.','sa','pvt.,','trading','','ООО']   
    cleaned_text = [w for w in sentence if w not in ignore]    
    return cleaned_text
```


```python
data_names_collections['collections_cleaned']=data_names_collections['collections'].apply(word_extraction)
```

Создаем словарь уникальный слов


```python
def tokenize(sentences):    
    words = []
    for sentence in sentences:               
        words.extend(sentence)            
    words = sorted(list(set(words)))    
    return words
```


```python
vocab=tokenize(data_names_collections['collections_cleaned'])
```

Присваиваем каждому слову векторное обозначение


```python
def vector(sentence, vocab=vocab):
    bag_vector = np.zeros(len(vocab))        
    for w in sentence:            
        for i,word in enumerate(vocab):                
            if word == w:                     
                bag_vector[i] += 1                            
    return bag_vector
```


```python
data_names_collections['vector']=data_names_collections['collections_cleaned'].apply(vector)
```


```python
data_names_collections
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>names</th>
      <th>names_cleaned</th>
      <th>collections</th>
      <th>collections_cleaned</th>
      <th>vector</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alfagomma</td>
      <td>alfagomma</td>
      <td>[, alfagomma]</td>
      <td>[alfagomma]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CONTITECH TRANSPORTBANDSYSTEME GMBH</td>
      <td>contitech transportbandsysteme gmbh</td>
      <td>[, contitech, transportbandsysteme, gmbh]</td>
      <td>[contitech, transportbandsysteme, gmbh]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LANXESS Inc.</td>
      <td>lanxess inc.</td>
      <td>[, lanxess, inc.]</td>
      <td>[lanxess]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lanxess AG</td>
      <td>lanxess ag</td>
      <td>[, lanxess, ag]</td>
      <td>[lanxess, ag]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lanxess Accounting GmbH</td>
      <td>lanxess accounting gmbh</td>
      <td>[, lanxess, accounting, gmbh]</td>
      <td>[lanxess, accounting, gmbh]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18017</th>
      <td>ФИЛИАЛ КОМПАНИИ ЭКСОН НЕФТЕГАЗ ЛИМИТЕД</td>
      <td>филиал компании эксон нефтегаз лимитед</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед]</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>18018</th>
      <td>ФИЛИАЛ КОМПАНИИ"ЭКСОН НЕФТЕГАЗ ЛИМИТЕД"</td>
      <td>филиал компании эксон нефтегаз лимитед</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед, ]</td>
      <td>[филиал, компании, эксон, нефтегаз, лимитед]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>18019</th>
      <td>ХИМИНВЕСТ ГРУПП, ООО</td>
      <td>химинвест групп, ооо</td>
      <td>[химинвест, групп,, ооо]</td>
      <td>[химинвест, групп,, ооо]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>18020</th>
      <td>ХИМИНВЕСТ НПФ, ООО</td>
      <td>химинвест нпф, ооо</td>
      <td>[химинвест, нпф,, ооо]</td>
      <td>[химинвест, нпф,, ооо]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
    <tr>
      <th>18021</th>
      <td>ЭВЕРИ ДЕННИСОН</td>
      <td>эвери деннисон</td>
      <td>[эвери, деннисон]</td>
      <td>[эвери, деннисон]</td>
      <td>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...</td>
    </tr>
  </tbody>
</table>
<p>18022 rows × 5 columns</p>
</div>



Соединяем полученные данные с первоначальным датасетом


```python
df=data.merge(data_names_collections, how='left',left_on='name_1', right_on='names')\
[['pair_id','name_1','name_2','is_duplicate','vector']]

df=df.merge(data_names_collections, how='left',left_on='name_2', right_on='names',suffixes=('_1','_2'))\
[['pair_id','name_1','name_2','is_duplicate','vector_1','vector_2']]
```

Считаем корреляцию пирсона между векторами


```python
from scipy.stats.stats import pearsonr
```


```python
df['correlation']=df.apply(lambda x: pearsonr(x['vector_1'], x['vector_2'])[0], axis=1)
```

Корреляция между совпадающими и несовпадающими наименованиями отличается значительно


```python
df.groupby('is_duplicate').agg(Corr=('correlation', np.mean)).reset_index(drop=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>is_duplicate</th>
      <th>Corr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.105101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.437597</td>
    </tr>
  </tbody>
</table>
</div>


