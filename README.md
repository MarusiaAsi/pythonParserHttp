# pythonParserHttp
Работа с запросами
Используя HTTP-запросы (не селениум, а именно запросы) , выполнить следующие шаги:
1.	Перейти по ссылке https://2ip.ru/ и спарсить свой ip-адрес
2.	Перейти по ссылке https://www.maxmind.com/en/geoip2-precision-demo и получить название таймзоны у своего ip-адреса (вместо представленной ссылки по которой невозможно получить ключ API, было использовано API c сайта https://www.bigdatacloud.com/https://www.bigdatacloud.com/)
3.	Перейти по ссылке https://gist.github.com/salkar/19df1918ee2aed6669e2 и получить список регионов, входящих в полученную таймзону
Результатом должен получиться файл, в котором первой строкой указано название таймзоны, второй строкой регионы, входящие в таймзону (если таковые имеются)
