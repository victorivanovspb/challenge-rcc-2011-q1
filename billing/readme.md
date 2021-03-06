# &laquo;B&raquo; Тарифы 

* [Ограничения](#bounds)
* [Задание](#problem)
* [Формат входных данных](#input-format)
* [Формат выходных данных](#output-format)
* [Решение](#solution)


<a name="bounds"></a><h2>Ограничения</h2>
<dl>
    <dt>Ограничение по времени</dt>
    <dd>2 секунды</dd>
    <dt>Ограничение по памяти</dt>
    <dd>256 мегабайт</dd>
</dl>


<a name="problem"></a><h2>Задание</h2>
[russiancodecup.ru/ru/tasks/round/6/B/](http://www.russiancodecup.ru/ru/tasks/round/6/B/)

В настоящее время практически каждый оператор сотовой связи	имеет
обширный набор тарифов, которые позволяют каждому человеку выбрать
наиболее подходящий для себя. К сожалению, зачастую осуществить
этот выбор вручную очень тяжело.
	
У одного из сотовых операторов каждый тариф характеризуется тремя числами:  
* абонентная плата c<sub>i</sub> (задается в рублях),  
* минимальная тарифицируемая единица времени t<sub>i</sub> (задается в секундах),  
* стоимость минимальной тарифицируемой единицы времени p<sub>i</sub> (задается
в копейках, в одном рубле 100 копеек).  
		
Суммарная стоимость вызовов за месяц складывается из абонентной платы
и стоимостей каждого из исходящих вызовов. Стоимость вызова при использовании
i-ого тарифа вычисляется следующим образом: пусть время разговора равно
T секунд. Если T < t<sub>i</sub>, то стоимость вызова равна нулю. Иначе
стоимость вызова равна произведению k на p<sub>i</sub>, где k — минимальное
целое число, такое что k·t<sub>i</sub> ≥ T.

Задано описание тарифов и статистика исходящих вызовов абонента в течение
месяца — их число m и длительности d<sub>1</sub>, ..., d<sub>m</sub>
в секундах. Необходимо найти тариф, при котором суммарная стоимость этих
вызовов была бы минимальной.


<a name="input-format"></a><h2>Формат входных данных</h2>   
Первая строка содержит два целых числа n и m — соответственно количество тарифов
и исходящих вызовов абонента (1 ≤ n, m ≤ 100). Каждая из последующих n строк
описывает один тариф и содержит три целых числа:
	
c<sub>i</sub> (0 ≤ c<sub>i</sub> ≤ 100), t<sub>i</sub> (1 ≤ t<sub>i</sub> ≤ 3600),
p<sub>i</sub> (0 ≤ p<sub>i</sub> ≤ 1000).

Последняя строка содержит m целых чисел d<sub>1</sub>, ..., d<sub>m</sub>
(1 ≤ d<sub>i</sub> ≤ 3600 для всех i от 1 до m).


<a name="output-format"></a><h2>Формат выходных данных</h2>
Выведите одно число — номер тарифа, при использовании которого суммарная
стоимость исходящих вызовов абонента за рассматриваемый месяц минимальна.
Тарифы нумеруются целыми числами от 1 до n в том порядке, в котором они
заданы во входном файле. Если таких тарифов несколько, выведите номер
любого из них.


<a name="examples"></a><h2>Примеры</h2>
Входные данные:
```
2 1
100 60 100  
51 10 100  
600
```
   
Выходные данные:
```
1
```


<a name="solution"></a><h2>Решение</h2>
<dl>
    <dt>Решение</dt>
    <dd>
        <a href="./billing.py">billing.py</a>
    </dd>
    <dt>Тесты</dt>
    <dd>
        <a href="./billing_tests.py">billing_tests.py</a>
    </dd>
    <dt>Тестовые данные</dt>
    <dd>
        <a href="./tests_data">tests_data</a>
    </dd>
</dl>