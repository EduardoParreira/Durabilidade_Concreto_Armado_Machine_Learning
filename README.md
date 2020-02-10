# Predicao de Durabilidade de Concretos Armados 

No ramo da Engenharia Civil, existe um problema grande quando analisamos a deterioração do concreto e consequentemente a sua durabilidade. Isso ocorre muito, pelos diferentes tipos de maneiras de executar o processo, diferentes tipos de materiais e diferentes condições climáticas que a estrutura fica exposta. 

Uma das principais causas do deterioramento, é o processo de carbonatação da estrutura. Entende-se por carbonatação, a incidência do carbono no concreto armado, por meio dos poros e fissuras. Sendo que por meio de análise in loco com auxilio de sensores, consegue-se levantar o coeficiente de carbonatação, ou seja, a velocidade que o carbono se infiltra na estrutura. Hoje pela norma brasileira, uma construção com 50 anos de idade deve ter no máximo 6 cm de carbonatação. 

A partir disso, existem calculos realizados para "prever" a profundidade do carbono no concreto, em determinado tempo. Porém, a maioria dos cálculos não se adequam a nossa realidade. Temos por exemplo o cálculo do modelo Europeu, que foi desenvolvido na Europa. Onde as condições climáticas são outras, assim como os processos de fabricação, que podem variar da nossa região. Um outro exemplo que se encaixa no contexto, é o cálculo do modelo de Tutti. 

A partir desse problema, teve-se a ideia de construir uma inteligência artifical para resolver essa questão. Onde construimos dois modelos neurais que foram treinados por data sets gerados dos modelos tradicionais, Europeu e Tutti. Onde depois de treinados, eles constituiram conhecimentos própios e passaram a "prever" a profundidade da carbonatação da estrutura. 

Foi utilizado redes neurais artificais, por meio de regressão linear. Onde a mesma, consiste em aproximação de valores. No caso, a profundidade gerada pela rede, teria que se aproximar da profunidade que foi passada nos data sets. Como métrica, para saber se a inteligencia estava gerando bons resultados, utilizamos a média absoluta do erro, pois para cada previsão, existia um erro entre o que era de fato esperado, portanto, quanto menor e média do erro, menos a rede erraria em sua previsão. Toda a estrutura das redes neurais construidas podem ser conferidas nos arquivo python que disponilzei por aqui. 

Após os treinamentos, obtivemos resultados satisfatórios. Para o primeiro modelo codificado, atigimos um média absoluta de erro de 2,45. Já para o segundo modelo, a média foi de 1,88. Esse números querem dizer que, para cada previsão, a inteligência artifical pode errar o valor já citado, tanto para cima, quanto para baixo em comparação com a realidade. Quando mostrado esses resultados para os profissionais da Engeharia Civil, os mesmos ficaram bastantes satisfeitos já que são resultados melhores do que eles lidam no dia a dia com modelos tradicionais.

O projeto já foi finalizado e aprovado pela banca final.
