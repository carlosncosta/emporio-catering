# Serviço de vinho e construção de cartas de vinhos

Referência da skill **Sommelier Emporio Italia**. Cobre o serviço à mesa e em eventos (temperaturas,
copos, abertura, decantação, ordem, quantidades, conservação, defeitos, vedantes) e a construção de
cartas de vinhos para restaurantes italianos em Portugal (estrutura, número de referências, vinho a
copo, preços, IVA, obrigações legais de informação, alergénios, redação, formação e venda). Termina
com modelos de carta feitos com vinhos do catálogo Emporio Italia.

> **Confidencialidade.** Este ficheiro não contém preços, custos, margens nem stock da Emporio Italia.
> Os valores em euros que aparecem nos exemplos de cálculo são **fictícios** e servem só para mostrar a
> conta. Preço trade e stock estão no ficheiro privado `data/precos_stock.csv`.

> **Estado de verificação (verificação independente, 29/09/2026). Ler antes de usar.**
> - **Legislação portuguesa e europeia: confirmada no texto integral** (cópias públicas do Diário da
>   República e do EUR-Lex nos repositórios `legalize-pt` e `legalize-eu`, que indicam o ELI/URL
>   oficial; o acesso direto ao DRE, ao Portal das Finanças e ao EUR-Lex estava bloqueado). Versões
>   consolidadas lidas: RJACSR de 24/03/2023, DL 138/90 de 10/12/2021, DL 50/2013 e DL 26/2016 de
>   29/01/2021, CIEC de 15/04/2026. **Alterações posteriores a essas datas não puderam ser
>   verificadas.** Antes de um documento para cliente, para a ASAE ou para a AT, confirmar no DRE e no
>   Portal das Finanças a versão em vigor.
> - **Recomendações de produtores** (temperaturas, copos, abertura): confirmadas nas fichas oficiais
>   (Donnafugata, Masciarelli) e numa nota de prova da The Wine Society.
> - **Prática profissional de sala.** Muitos números de serviço (temperaturas por estilo, cave, vida de
>   uma garrafa aberta, quantidades por convidado, número de referências, multiplicadores de preço) são
>   regras de ofício **sem fonte confirmada**. Estão marcados **(não verificado)**, quase sempre no
>   título da tabela ou da secção. Servem como ponto de partida, não como facto citável.

## Índice

1. [Resumo em 60 segundos](#1-resumo-em-60-segundos)
2. [Temperaturas de serviço](#2-temperaturas-de-serviço)
3. [Copos](#3-copos)
4. [Abrir garrafas: tranquilos, espumantes e frisantes](#4-abrir-garrafas-tranquilos-espumantes-e-frisantes)
5. [Decantação: quando, porquê e como](#5-decantação-quando-porquê-e-como)
6. [Ordem de serviço e protocolo à mesa](#6-ordem-de-serviço-e-protocolo-à-mesa)
7. [Quantidades para eventos e catering](#7-quantidades-para-eventos-e-catering)
8. [Conservação: cave, restaurante e garrafa aberta](#8-conservação-cave-restaurante-e-garrafa-aberta)
9. [Defeitos do vinho e devoluções](#9-defeitos-do-vinho-e-devoluções)
10. [Vedantes](#10-vedantes)
11. [Construir uma carta de vinhos para um restaurante italiano em Portugal](#11-construir-uma-carta-de-vinhos-para-um-restaurante-italiano-em-portugal)
12. [Programa de vinho a copo](#12-programa-de-vinho-a-copo)
13. [Preços e margens na restauração](#13-preços-e-margens-na-restauração)
14. [IVA e impostos sobre o vinho em Portugal](#14-iva-e-impostos-sobre-o-vinho-em-portugal)
15. [Obrigações legais: preços, afixação e venda de álcool](#15-obrigações-legais-preços-afixação-e-venda-de-álcool)
16. [Alergénios, sulfitos e rotulagem que chega à mesa](#16-alergénios-sulfitos-e-rotulagem-que-chega-à-mesa)
17. [Escrever as descrições da carta](#17-escrever-as-descrições-da-carta)
18. [Formação da equipa de sala e técnicas de venda](#18-formação-da-equipa-de-sala-e-técnicas-de-venda)
19. [Modelos de carta de vinhos italiana (catálogo Emporio)](#19-modelos-de-carta-de-vinhos-italiana-catálogo-emporio)
20. [Menu de catering Emporio: serviço, ordem e quantidades](#20-menu-de-catering-emporio-serviço-ordem-e-quantidades)
21. [Listas de verificação](#21-listas-de-verificação)
22. [Pendentes de verificação](#22-pendentes-de-verificação)
23. [Fontes](#23-fontes)

---

## 1. Resumo em 60 segundos

- **Temperatura é a primeira alavanca de qualidade.** Um erro frequente é o tinto servido quente
  (sala a 24-26 °C no verão) e o branco servido gelado (não verificado quanto à frequência). As fichas
  dos produtores do catálogo apontam, por exemplo, 9-11 °C para um branco fresco siciliano (Donnafugata
  Anthìlia) [25], 15-16 °C para um Nero d'Avola jovem (Sherazade) [27] e 18 °C para os tintos de
  guarda (Tancredi, Mille e una Notte) [24][29].
- **Espumante é um vinho sob pressão.** Por lei, um *vino spumante* tem pelo menos 3 bar a 20 °C e um
  espumante de qualidade pelo menos 3,5 bar; um *vino frizzante* tem entre 1 e 2,5 bar [18]. Abre-se
  frio, com o polegar sempre sobre a rolha e a garrafa apontada para longe das pessoas.
- **Contas de base para eventos:** uma garrafa de 75 cl dá 6 copos de 12,5 cl ou 5 de 15 cl; um magnum
  dá o dobro. As regras de consumo por convidado (secção 7) são prática profissional (não verificado).
- **IVA em Portugal continental:** o vinho **servido** num restaurante ou num serviço de catering paga
  **23 %**, porque a taxa intermédia dos serviços de alimentação e bebidas exclui as bebidas
  alcoólicas [6]. Num preço único com comida e bebida (menu com vinhos, catering por pessoa), o valor
  tem de ser repartido pelas taxas; se não for repartido, aplica-se 23 % a tudo [6]. No retalho, os
  "vinhos comuns" estão na Lista II (taxa intermédia, 13 %) [8][9]; espumantes e licorosos ficam, em
  regra, fora dessa verba (secção 14.3).
- **Carta obrigatória e com todos os preços.** O restaurante tem de ter listas de preços junto à entrada
  e no interior, em português, com **todas** as bebidas e respetivos preços, e não pode cobrar nada que
  o cliente não tenha pedido [1]. Os preços incluem todos os impostos [2].
- **Sulfitos:** acima de 10 mg/l de SO₂ total são alergénio de declaração obrigatória [17]. Num
  restaurante, a informação sobre alergénios tem de estar disponível num suporte de fácil apreensão
  pelo consumidor [13].
- **Venda a menores:** é proibido vender ou facultar bebidas alcoólicas a menores (menos de 18 anos) e a
  quem esteja notoriamente embriagado; o aviso tem de estar afixado e pode pedir-se identificação
  [3][4][5]. A violação é contraordenação económica muito grave [3].

---

## 2. Temperaturas de serviço

### 2.1 Porque importa

- Frio demais apaga o aroma e endurece taninos e acidez; quente demais faz sobressair o álcool e torna
  o vinho pesado. O vinho aquece no copo, sobretudo em esplanada, por isso serve-se 1-2 °C abaixo do
  alvo (prática profissional; não verificado).
- "Temperatura ambiente" é uma expressão antiga, de salas frias. Numa sala portuguesa no verão, um tinto
  "à temperatura ambiente" está quente demais.

### 2.2 Tabela por estilo (prática profissional; não verificado)

Os intervalos são referências de sala. Onde há ficha oficial do produtor, a coluna da direita dá o valor
publicado, que prevalece.

| Estilo | Exemplos do catálogo | Temperatura | Valor publicado pelo produtor |
|---|---|---|---|
| Espumante Charmat (Prosecco e outros *spumanti*) | Villa Sandi Il Fresco, Bolla Prosecco, Carpenè Malvolti 1868 | 6-8 °C | — |
| Espumante aromático doce | Fontanafredda Asti DOCG | 6-8 °C | — |
| Metodo Classico sem ano, incluindo Satèn sem ano (Franciacorta, Trento DOC) | Berlucchi '61 e '61 Satèn, Bellavista Alma, Ferrari Brut | 7-9 °C | — |
| Metodo Classico millesimato / Riserva | Berlucchi '61 Nature, Ferrari Perlé, Palazzo Lana | 9-11 °C | — |
| Lambrusco amabile e rosato | Ceci G. Verdi Amabile | 8-10 °C | — |
| Lambrusco secco e tintos frisantes secos | Ceci Otello | 10-12 °C | — |
| Branco leve e fresco | Pinot Grigio Corte Giara, Soave Pasqua, Gavi Fontanafredda, Falanghina Feudi | 8-10 °C | Anthìlia (Donnafugata): 9-11 °C [25] |
| Branco aromático / mineral de altitude | Roero Arneis, Pecorino, Etna Bianco, Greco di Tufo | 9-11 °C | — |
| Branco estruturado, com madeira ou borras | Cervaro della Sala, Pomino Benefizio, Vintage Tunina | 11-13 °C | Chiarandà (Donnafugata): 11-13 °C [26] |
| Rosado | Cerasuolo Masciarelli, Alìe Frescobaldi, Rosa Donnafugata | 9-12 °C | Cerasuolo d'Abruzzo (Gianni Masciarelli): 10-12 °C [31] |
| Tinto leve e frutado | Valpolicella Classico, Blau & Blau, Red Angel | 13-15 °C | Sherazade (Donnafugata): 15-16 °C, "ligeiramente fresco" [27] |
| Tinto médio | Chianti, Barbera d'Alba, Langhe Nebbiolo, Montepulciano d'Abruzzo | 15-17 °C | Montepulciano d'Abruzzo (Gianni Masciarelli): 16-18 °C [30]; Sedàra (Donnafugata): 16-18 °C [28] |
| Tinto encorpado e de guarda | Barolo, Brunello, Amarone, Taurasi, Sagrantino, Bolgheri, Tignanello | 16-18 °C | Tancredi: 18 °C [24]; Mille e una Notte: 18 °C [29] |
| Branco doce | Kabir Moscato di Pantelleria | 8-10 °C | — |
| Vin Santo, passiti de estágio longo | Pomino Vin Santo, Ben Ryé | 12-14 °C | — |
| Barolo Chinato (vinho aromatizado) | Fontanafredda Barolo Chinato | 14-16 °C, ou fresco como aperitivo | — |

### 2.3 Como chegar à temperatura certa (prática profissional; não verificado)

- **Balde com água e gelo** (não só gelo): é o método mais rápido, porque a água envolve a garrafa toda.
  Uma mão-cheia de sal acelera ainda mais.
- **Frigorífico doméstico** (4-5 °C): bom para espumantes; brancos estruturados saem frios demais e
  devem esperar uns minutos fora.
- **Tintos na sala quente:** 10-20 minutos no frigorífico ou uns minutos no balde antes de servir.
- **Armários de serviço por zonas:** o ideal num restaurante é ter uma zona para espumantes e brancos e
  outra para tintos, regulada para a temperatura de serviço, separada da cave de guarda.
- **Termómetro de garrafa ou de infravermelhos** na estação do escanção. A equipa acerta muito mais
  quando mede do que quando adivinha.
- **Em eventos no verão**, prever baldes também para os tintos e renovar o gelo a meio do serviço.

---

## 3. Copos

### 3.1 Princípios (prática profissional; não verificado)

- **Vidro liso, incolor e fino**, com pé. O pé evita aquecer o vinho com a mão e mantém o bojo limpo.
- **Bojo mais largo do que a boca**: concentra o aroma. Copos maiores para vinhos mais complexos e
  tintos de guarda; copos médios para brancos e tintos jovens.
- **Encher pouco**: cerca de um terço do copo nos tranquilos, para deixar espaço para rodar. Nos
  espumantes, dois terços a três quartos, em dois tempos para a espuma não transbordar.
- **Espumantes: tulipa em vez de flûte estreita.** A tulipa (bojo com boca mais fechada) deixa perceber
  o aroma de um Franciacorta ou de um Prosecco Superiore; a taça larga (tipo "coupe") perde a bolha
  depressa. Muitos consórcios e produtores italianos recomendam hoje copos de tulipa para os seus
  espumantes (não verificado).
- **Um copo universal** de boa qualidade (35-45 cl) resolve a maioria das situações numa trattoria ou
  pizzaria. Em fine dining, acrescentar um copo grande tipo Borgonha (Barolo, Nebbiolo, Pinot Nero) e um
  tipo Bordéus (Bolgheri, Tignanello, Amarone).

### 3.2 O que dizem os produtores do catálogo

| Vinho | Recomendação do produtor | Fonte |
|---|---|---|
| Donnafugata Anthìlia (branco fresco) | copo de tamanho e altura médios; 9-11 °C | [25] |
| Donnafugata Chiarandà (Chardonnay com estágio) | copo grande e relativamente alto; abrir 30 minutos antes; 11-13 °C | [26] |
| Donnafugata Sedàra (tinto médio) | copo de tamanho médio; 16-18 °C | [28] |
| Donnafugata Mille e una Notte (tinto de guarda) | em copo grande e bojudo, pode abrir-se minutos antes; caso contrário, cerca de duas horas antes; 18 °C | [29] |

### 3.3 Cuidados com os copos (prática profissional; não verificado)

- Lavar com detergente sem perfume, enxaguar bem e **polir a vapor** com pano de microfibra ou linho.
  Resíduos de detergente matam a bolha do espumante e deixam cheiro.
- Guardar de pé ou em grelhas, longe da cozinha e de fumos. Copos guardados ao contrário em prateleiras
  de madeira ou em armários fechados ganham cheiro a "armário": cheirar um copo vazio antes do serviço.
- Em eventos, prever **2 a 3 copos por convidado** (espumante de boas-vindas, branco, tinto), mais uma
  reserva para quebras e trocas.

---

## 4. Abrir garrafas: tranquilos, espumantes e frisantes

### 4.1 Vinho tranquilo com rolha (prática profissional; não verificado)

1. Apresentar a garrafa ao anfitrião com o rótulo virado para ele e confirmar produtor, vinho e colheita.
2. Cortar a cápsula **abaixo do anel** do gargalo, para o vinho não tocar na cápsula ao servir.
3. Limpar o gargalo com um pano.
4. Saca-rolhas de alavanca dupla ("de dois tempos"): espiral ao centro, sem atravessar a rolha até ao fim
   (evita fragmentos no vinho). Retirar a rolha devagar, sem estalido.
5. Olhar para a rolha (humidade, fugas, cheiro a mofo). A rolha é um indício; o diagnóstico faz-se no
   vinho (secção 9).
6. Limpar outra vez o gargalo e dar a provar ao anfitrião uma pequena quantidade.
7. Rolhas velhas e frágeis (colheitas antigas): saca-rolhas de lâminas (tipo "ah-so") ou de agulha
   dupla. Se a rolha cair para dentro, decantar por um filtro.

**Cápsula de rosca ou tampa metálica:** mesmo ritual de apresentação; segurar a base da cápsula e rodar
a garrafa, à vista do cliente. Não é sinal de vinho inferior (secção 10).

### 4.2 Espumante: a regra de segurança

**Porque é perigoso.** A pressão de um espumante é elevada: a lei europeia define *vino spumante* com
**pelo menos 3 bar** de sobrepressão a 20 °C em recipiente fechado e *vino spumante di qualità* com
**pelo menos 3,5 bar**; o *spumante di qualità di tipo aromatico* (como o Asti) tem pelo menos 3 bar
[18]. Um Metodo Classico anda normalmente bem acima do mínimo legal (cerca de 5-6 bar; não verificado).
A pressão sobe com a temperatura, por isso uma garrafa quente ou agitada é muito mais perigosa. Uma
rolha que salta pode causar lesões oculares graves (não verificado quanto a velocidades e números).

**Procedimento (prática profissional; não verificado):**

1. Garrafa **bem fria** e **não agitada** (não a transportar a correr, não a pousar com pancada).
2. Retirar a folha; **pôr o polegar sobre a rolha antes de soltar a gaiola** e não o tirar até ao fim.
3. Desapertar o arame da gaiola (é habitual dar seis meias-voltas); pode deixar-se a gaiola solta sobre
   a rolha, que ajuda a segurar.
4. Inclinar a garrafa cerca de 45°, **apontada para longe de pessoas, copos, candeeiros e janelas**.
5. Segurar a rolha e **rodar a garrafa, não a rolha**, deixando a rolha sair devagar, com um suspiro e
   sem estalo. Um estalo é gás (e bolha) perdido.
6. Se a rolha começar a subir sozinha, manter o polegar firme e deixar a pressão sair aos poucos.
7. Servir em dois tempos: um pouco, esperar a espuma baixar, completar.

**Nunca** apontar para alguém, nunca abrir com a garrafa quente, nunca usar saca-rolhas num espumante.
A *sabrage* (abrir com sabre) é espetáculo e risco: não recomendada em eventos com convidados perto.

### 4.3 Frisantes e Lambrusco

- O *vino frizzante* tem uma sobrepressão entre **1 e 2,5 bar** a 20 °C e pelo menos 7 % vol. de álcool
  adquirido [18]. Tem menos pressão, mas a rolha salta na mesma: aplicar a regra do polegar.
- Muitos frisantes e Lambrusco usam rolha em forma de cogumelo presa com arame ou cordel; abre-se como
  um espumante.

### 4.4 Serviço de espumante em eventos (prática profissional; não verificado)

- Não abrir garrafas com mais de alguns minutos de antecedência: a bolha perde-se no copo cheio.
- Para brindes com muitos convidados, servir em tabuleiro com copos cheios a dois terços, abertos em
  bateria por 2-3 pessoas treinadas.
- Garrafas abertas e não terminadas: rolha de espumante (tampa com abas) e balde.

---

## 5. Decantação: quando, porquê e como

### 5.1 As quatro razões (prática profissional; não verificado)

| Razão | Para que vinhos | O que fazer |
|---|---|---|
| **Separar o depósito** | Tintos com vários anos de garrafa, vinhos não filtrados, Barolo/Brunello/Amarone com idade | Garrafa de pé 24 h antes; decantar devagar, com luz por baixo do gargalo, e parar quando o depósito chegar ao ombro |
| **Arejar um vinho jovem e fechado** | Barolo, Taurasi, Sagrantino, Aglianico, Brunello, Amarone e grandes tintos jovens; alguns brancos estruturados | Decantar 1-3 horas antes (mais nos mais tânicos) e provar de hora a hora |
| **Dissipar redução** | Vinhos com cheiro a fósforo, ovo ou borracha ao abrir (secção 9) | Decantar com vigor; 15-30 minutos costumam chegar |
| **Espetáculo e temperatura** | Mesa que pede, garrafas grandes, vinho um pouco frio | Decantar aquece ligeiramente o vinho; usar com critério |

**Quando não decantar (ou só para separar o depósito e servir logo):** tintos muito velhos e frágeis
(perdem aroma em minutos); a maioria dos brancos leves; espumantes (há quem decante Franciacorta ou
Trento de colheitas maduras, mas é escolha de estilo, não regra).

### 5.2 O que dizem produtores e críticos sobre vinhos do catálogo

| Vinho | Recomendação | Fonte |
|---|---|---|
| Donnafugata Chiarandà (branco) | abrir 30 minutos antes; copo grande e alto | [26] |
| Donnafugata Mille e una Notte | em copo grande e bojudo, abrir minutos antes; noutro copo, cerca de duas horas antes; servir a 18 °C | [29] |
| Feudi di San Gregorio Taurasi 2019 | encorpado, taninos firmes e acidez viva; decantar com bastante antecedência, "até 12 horas" (nota de prova da The Wine Society) | [32] |
| Barolo jovem (Fontanafredda, Cordero di Montezemolo) | decantar 1-2 horas; 16-18 °C em copo largo | ver `regioes-norte.md` (prática profissional; não verificado) |
| Brunello jovem (menos de 10 anos) | decantar 1-2 horas; Riserva e colheitas antigas só para separar o depósito | ver `regioes-centro.md` (prática profissional; não verificado) |
| Sagrantino jovem (Caprai) | decantar 2 horas ou mais; 17-18 °C; só com pratos de proteína e gordura | ver `regioes-centro.md` (prática profissional; não verificado) |

### 5.3 Como decantar (prática profissional; não verificado)

1. Garrafa de pé (idealmente 24 h antes, para o depósito descer).
2. Decantador limpo, sem cheiro, enxaguado com um pouco do próprio vinho se houver dúvida.
3. Abrir, limpar o gargalo, provar.
4. Verter devagar e sem parar, com o gargalo sobre uma luz (vela ou lanterna); parar ao ver o depósito.
5. Apresentar a garrafa vazia ao lado do decantador (o cliente quer ver o rótulo).
6. Em eventos, decantar os grandes tintos na copa, identificar cada decantador e servir a partir dele.

---

## 6. Ordem de serviço e protocolo à mesa

### 6.1 Ordem dos vinhos numa refeição (prática profissional; não verificado)

1. **Espumante antes de tranquilo** (aperitivo).
2. **Leve antes de encorpado**, **simples antes de complexo**, **jovem antes de velho**.
3. **Seco antes de doce.** O vinho doce vai com a sobremesa ou depois dela.
4. **Branco antes de tinto** em regra, mas manda o prato: um branco estruturado (Fiano, Cervaro) pode vir
   depois de um tinto leve (Valpolicella, Lambrusco) se acompanhar um prato mais rico.
5. **Fresco antes de temperatura mais alta**, para a boca não estranhar.
6. **O vinho acompanha a intensidade do prato**: evitar servir um vinho mais leve depois de um muito
   potente sem "limpar" a boca (água, pão).

### 6.2 Escala de doçura dos espumantes (definida por lei)

A doçura do espumante não é intuitiva: **Extra Dry é mais doce do que Brut**. A ordem de serviço, do mais
seco ao mais doce, segue os teores legais de açúcar do Regulamento Delegado (UE) 2019/33 [20]. Os
exemplos vêm do catálogo Emporio (menção do rótulo segundo o catálogo).

| Menção no rótulo (termos em italiano) | Açúcar (g/l) | Exemplos do catálogo |
|---|---|---|
| Brut Nature / Pas Dosé / Dosaggio Zero | menos de 3; só se não houver açúcar adicionado após a segunda fermentação | Bellavista Alma Non Dosato, Berlucchi '61 Nature |
| Extra Brut | 0 a 6 | Villa Sandi La Rivetta 120, Carpenè Malvolti 1868 Extra Brut, Berlucchi '61 Extra Brut |
| Brut | menos de 12 | Ferrari Brut, Villa Sandi Il Fresco Brut |
| Extra Dry (também "extra secco") | 12 a 17 | Bolla Prosecco, Carpenè Malvolti 1868 Extra Dry |
| Sec / Secco / Asciutto / Dry | 17 a 32 | — |
| Demi-Sec / Abboccato | 32 a 50 | — |
| Doux / Dolce | mais de 50 | Fontanafredda Asti DOCG (dolce) |

**Na prática:** num menu, o Prosecco Extra Dry funciona no aperitivo e com charcutaria; para peixe cru,
marisco e pratos salinos, um Brut ou Extra Brut é mais seguro (juízo de harmonização; ver
`harmonizacao.md`).

### 6.3 Protocolo de serviço à mesa (prática profissional; não verificado)

1. **Apresentar** a garrafa ao anfitrião (quem pediu o vinho), rótulo à vista.
2. **Abrir** à vista do cliente (na mesa ou num aparador ao lado).
3. **Dar a provar** ao anfitrião cerca de 2-3 cl. A prova serve para detetar defeitos, não para "ver se
   gosta".
4. **Servir** os convidados primeiro, habitualmente pela direita, no sentido dos ponteiros do relógio,
   e o anfitrião por último.
5. **Encher** até cerca de um terço (tranquilos) e voltar a servir antes de o copo ficar vazio, sem
   encher em excesso (o cliente perde o controlo de quanto bebe).
6. **Deixar a garrafa** num balde (brancos, espumantes) ou numa mesa auxiliar (tintos), ao alcance do
   empregado, não necessariamente do cliente, conforme o estilo da casa.
7. **Antes de a garrafa acabar**, perguntar se deseja outra do mesmo vinho ou uma alternativa (secção 18).
8. **Copos novos** quando muda o vinho, sempre que possível.

---

## 7. Quantidades para eventos e catering

### 7.1 Contas de base (aritmética)

| Formato | 7,5 cl (prova / doce) | 10 cl (flûte de brinde) | 12,5 cl | 15 cl |
|---|---|---|---|---|
| Meia garrafa 37,5 cl | 5 | 3,75 | 3 | 2,5 |
| Garrafa 75 cl | 10 | 7,5 | 6 | 5 |
| Magnum 1,5 L | 20 | 15 | 12 | 10 |
| Jeroboam 3 L | 40 | 30 | 24 | 20 |
| 5 L | 66 | 50 | 40 | 33 |
| 6 L | 80 | 60 | 48 | 40 |

**Rendimento real:** em serviço há perdas (prova do escanção, fundo com depósito, copos derramados).
Contar com cerca de 5 % a menos do que o teórico, ou seja, **cerca de 5,5 a 6 copos de 12,5 cl por
garrafa** (prática profissional; não verificado).

**Formatos grandes no catálogo** (úteis para mesas de convidados e para impacto visual): Bellavista Alma
Gran Cuvée Brut em 3 L e 6 L; Gianni Masciarelli Montepulciano d'Abruzzo em Jeroboam de 3 L; Cordero di
Montezemolo em 5 L (Barolo Monfalletto, Barolo Enrico VI, Barbera d'Alba Superiore Funtanì); Donnafugata
Mille e una Notte em 3 L e Tancredi em vários formatos grandes; Pasqua 11 Minutes Rosé em magnum
(catálogo Emporio; confirmar disponibilidade com `procurar_vinhos.py`).

### 7.2 Consumo por convidado (prática profissional; não verificado)

Regra de trabalho para um público adulto que bebe vinho com moderação. Ajustar sempre com o cliente e com
o histórico da Emporio Italia Catering.

| Formato de evento | Duração típica | Copos por pessoa (12,5 cl) | Garrafas por pessoa |
|---|---|---|---|
| Aperitivo / boas-vindas | 30-60 min | 1-2 | 0,2-0,3 |
| Brinde isolado | — | 1 flûte de 8-10 cl | 1 garrafa para 7-8 pessoas |
| Cocktail volante | 2 h | 3-4 | 0,5-0,7 |
| Cocktail longo / "dinner cocktail" | 3 h | 4-5 | 0,7-0,8 |
| Jantar sentado com vinhos | 2,5-3 h | 3-4 | 0,5-0,7 |
| Jantar sentado + aperitivo + digestivo | 4 h | 4-6 | 0,7-1 |
| Casamento (receção + jantar + festa) | 6-8 h | 6-8 | 1-1,3 (todos os vinhos, incluindo espumante) |

**Fatores que fazem subir:** dias de calor, eventos longos, festas com dança, público habituado a beber
vinho à refeição, *open bar* sem outras bebidas, ementa com muito sal (charcutaria, queijos).
**Fatores que fazem descer:** almoços de trabalho, muitos não bebedores ou condutores, alternativa forte
de cerveja e cocktails, eventos curtos.

**Repartição por cor (prática profissional; não verificado):** partir de 1/3 espumante, 1/3 branco e
rosado, 1/3 tinto num cocktail; num jantar, ajustar ao menu (ementas de peixe e marisco pedem mais branco;
carne e trufa pedem mais tinto). No menu de catering Emporio, com charcutaria, massas ricas e um prato
principal de carne, uma divisão de 30 % espumante, 30 % branco, 40 % tinto é um bom ponto de partida.

**Não esquecer:** água (0,5 a 1 litro por pessoa, mais no verão), gelo, e uma margem de segurança de
10 % no vinho (prática profissional; não verificado).

### 7.3 Fórmula de cálculo

```
garrafas = convidados_que_bebem × copos_por_pessoa ÷ copos_por_garrafa × (1 + margem)
```

- `convidados_que_bebem`: total menos crianças, grávidas, condutores declarados, abstémios.
- `copos_por_garrafa`: 6 (12,5 cl), 5 (15 cl), 7,5 (flûte de 10 cl), ou 5,5-6 com perdas.
- `margem`: 0,10 por defeito.

**Exemplo 1 — cocktail volante de 2 h, 100 convidados, 90 bebem, 3,5 copos de 12,5 cl:**
90 × 3,5 ÷ 6 = 52,5 → com 10 % de margem ≈ **58 garrafas**, por exemplo 18 de Prosecco, 18 de branco,
22 de tinto, mais cerca de 100 litros de água.

**Exemplo 2 — casamento, 150 convidados, 135 bebem:**
- Receção (1 h): 2 flûtes de 10 cl de espumante → 135 × 2 ÷ 7,5 = 36 garrafas.
- Jantar (3 h): 4 copos de 12,5 cl → 135 × 4 ÷ 6 = 90 garrafas (por exemplo 35 de branco, 55 de tinto).
- Brinde do bolo: 1 flûte → 135 ÷ 7,5 = 18 garrafas (ou um Asti se o bolo for doce).
- Total 144 garrafas + 10 % ≈ **158 garrafas** (cerca de 1,1 garrafas por convidado que bebe sem a
  margem e 1,2 com a margem).

**Exemplo 3 — jantar sentado de 8 pessoas com 3 vinhos (espumante, branco, tinto), 2 copos de cada:**
8 × 2 ÷ 6 = 2,7 → **3 garrafas de cada vinho**; se o tinto for um Barolo decantado, abrir 2 e ter a 3.ª
de reserva.

### 7.4 Logística de catering (prática profissional; não verificado, salvo indicação)

- **Gelo:** contar 1 a 1,5 kg por garrafa a arrefecer em balde, mais gelo para água e cocktails.
- **Baldes:** 1 por cada 6-8 garrafas em serviço simultâneo; em mesas sentadas, 1 balde por mesa para o
  branco e o espumante.
- **Copos:** 2-3 por convidado mais 10-15 % de reserva; um copo de água por convidado.
- **Pessoal:** uma pessoa dedicada ao vinho por cada 40-50 convidados em jantar sentado; em cocktail, uma
  por cada 30-40 com tabuleiro.
- **Abertura antecipada:** tintos abertos 30-60 minutos antes (grandes tintos decantados na copa);
  espumantes só no momento.
- **Garrafas fechadas no fim:** acordar antes com o cliente se as garrafas não abertas são devolvidas,
  faturadas ou ficam para o cliente. A política de devolução à Emporio tem de ser confirmada com a direção
  comercial (não documentada nesta referência).
- **Transporte:** garrafas de pé em caixas, espumantes nunca ao sol nem na mala de um carro quente.
- **Recintos de espetáculo (regra legal):** em sala ou recinto de espetáculo, permanente ou temporário
  (por exemplo arraiais, concertos, festas académicas), as bebidas alcoólicas têm de ser servidas em
  **recipiente de material leve e não contundente** [3]. A regra não se aplica a recintos fixos de
  espetáculos artísticos com restauração (casas de fado, cafés-teatro, salas de casinos), a feiras com
  área reservada só a restauração e bebidas, nem a **mostras e ações de degustação em áreas delimitadas**
  [3]. Num jantar ou casamento privado em quinta ou hotel, a regra normalmente não se coloca, mas
  confirmar o enquadramento do local.

---

## 8. Conservação: cave, restaurante e garrafa aberta

### 8.1 Guarda de garrafas fechadas (prática profissional; não verificado)

| Fator | Referência | Porquê |
|---|---|---|
| Temperatura | 10-15 °C, idealmente 12-14 °C, **estável** | Variações rápidas fazem o vinho envelhecer mal; calor acima de 25 °C "coze" o vinho |
| Humidade | 60-75 % | Rolhas secas encolhem e deixam entrar ar; humidade excessiva estraga rótulos |
| Luz | Escuridão; iluminação LED sem UV | A luz degrada o vinho, sobretudo espumantes e brancos em vidro claro ("gosto de luz", secção 9) |
| Posição | **Deitada** com rolha natural; de pé com cápsula de rosca ou para consumo em poucas semanas | Mantém a rolha húmida |
| Vibração | Mínima | Longe de motores, frigoríficos industriais, máquinas de lavar |
| Cheiros | Sem produtos de limpeza, combustíveis, cozinha | A rolha não protege de odores fortes em guarda longa |

**No restaurante:** não guardar vinho em estantes de sala junto a janelas, por cima de fornos ou ao lado da
cozinha; as paredes de garrafas decorativas precisam de climatização. Rodar o stock por ordem de entrada
e de colheita (FIFO) e manter as colheitas da carta atualizadas.

**Vinhos que não melhoram na cave:** a maioria dos brancos frescos, rosados, Prosecco e Lambrusco são para
beber jovens (em regra até 1-2 anos após a colheita; não verificado). Na carta, trocar a colheita a tempo.

### 8.2 Vida de uma garrafa aberta (prática profissional; não verificado)

Com a garrafa bem fechada e **no frigorífico** (tintos incluídos, retirados 20-30 min antes de servir):

| Estilo | Rolha simples / tampa | Com vácuo ou gás inerte | Com sistema de agulha e árgon (tipo Coravin) |
|---|---|---|---|
| Espumante (com tampa de espumante) | 1-2 dias | 2-3 dias (tampa própria) | só com sistema próprio para espumantes |
| Branco leve, rosado | 2-3 dias | 3-5 dias | semanas |
| Branco estruturado | 3-4 dias | 4-6 dias | semanas |
| Tinto leve | 2-3 dias | 3-5 dias | semanas |
| Tinto encorpado e tânico | 3-5 dias | 4-7 dias | semanas a meses |
| Doces e passiti (o açúcar protege) | 1-2 semanas | 2-3 semanas | meses |
| Marsala, vinhos de estilo oxidativo | semanas | semanas | meses |
| Vermute e outros vinhos aromatizados | semanas no frigorífico | — | — |

**Regra de sala:** marcar cada garrafa aberta com data e hora (fita ou etiqueta) e provar antes de servir o
primeiro copo do dia. Se houver dúvidas, não servir.

---

## 9. Defeitos do vinho e devoluções

### 9.1 Quadro de defeitos (descrições: prática profissional; não verificado)

| Defeito | Como se reconhece | Causa habitual | Resolve-se? |
|---|---|---|---|
| **TCA ("gosto a rolha")** | Mofo, cave húmida, cartão molhado, jornal velho; fruta apagada mesmo quando o cheiro é fraco | 2,4,6-tricloroanisol, geralmente com origem na rolha (pode vir da adega); detetável em concentrações de nanogramas por litro (limiar não verificado) | Não. Trocar a garrafa |
| **Oxidação** | Brancos dourados a acastanhados; tintos jovens com cor de tijolo; maçã passada, noz, caramelo; boca plana | Entrada de ar (rolha seca ou defeituosa), calor, garrafa aberta há dias, vinho velho demais | Não |
| **Redução** | Fósforo riscado, ovo podre, borracha, couve cozida | Compostos de enxofre formados sem oxigénio; frequente em vinhos jovens e em cápsula de rosca | Muitas vezes sim: decantar e arejar 15-30 min |
| **Brettanomyces ("Brett")** | Estábulo, suor de cavalo, penso rápido, couro, especiaria fumada; fruta seca e final metálico | Levedura contaminante; compostos como 4-etilfenol e 4-etilguaiacol | Não. Em nível baixo há quem o aceite como "complexidade"; em nível alto é defeito |
| **Acidez volátil elevada** | Vinagre, verniz de unhas, cola | Bactérias acéticas; ácido acético e acetato de etilo | Não |
| **Dano por calor ("vinho cozido")** | Rolha empurrada para fora, cápsula pegajosa, marcas de vinho no gargalo; fruta cozida, compota, cor evoluída | Transporte ou armazenagem quente | Não |
| **Gosto de luz** | Couve, cebola, cartão molhado, sobretudo em espumantes e brancos | Exposição à luz, pior em vidro claro | Não |
| **Refermentação** | Gás e turvação num vinho que devia ser tranquilo; cheiro a levedura | Açúcar e leveduras residuais | Não |
| **Excesso de sulfuroso** | Cheiro picante de fósforo queimado ao abrir, que pica no nariz | Sulfitagem alta; às vezes em vinhos muito jovens | Às vezes atenua com arejamento |

**Não são defeitos** (explicar ao cliente com calma):
- **Cristais de tartaratos** no fundo ou na rolha (os "diamantes do vinho"): sais naturais do vinho que
  precipitam com o frio.
- **Depósito** em tintos com idade ou não filtrados.
- **Ligeira agulha de gás** em alguns brancos jovens.
- **Estilos oxidativos intencionais:** Marsala e Vin Santo têm por natureza notas de noz e caramelo.
- **Cor clara no Nebbiolo** (Barolo, Langhe Nebbiolo): é própria da casta, não é vinho "fraco".

### 9.2 Limites legais que ajudam a enquadrar

- **Acidez volátil máxima** (Regulamento Delegado (UE) 2019/934, anexo I, parte C) [19]:
  **18 miliequivalentes por litro** em brancos e rosados e **20 miliequivalentes por litro** em tintos.
  O mesmo regulamento equipara 0,12 g/l a 2 meq expressos em ácido acético [19], o que dá cerca de
  **1,08 g/l** (brancos e rosados) e **1,20 g/l** (tintos). Os Estados-Membros podem conceder
  derrogações a certos vinhos DOP/IGP envelhecidos pelo menos dois anos ou feitos por métodos
  particulares, e a vinhos com pelo menos 13 % vol. de título alcoométrico total [19].
- **Dióxido de enxofre total máximo** (anexo I, parte B) [19]:

| Vinho | Açúcar (glicose + frutose) | SO₂ total máximo |
|---|---|---|
| Tinto | menos de 5 g/l | 150 mg/l |
| Branco e rosado | menos de 5 g/l | 200 mg/l |
| Tinto | 5 g/l ou mais | 200 mg/l |
| Branco e rosado | 5 g/l ou mais | 250 mg/l |
| Espumante de qualidade (todas as categorias) | — | 185 mg/l |
| Outros espumantes | — | 235 mg/l |
| Vinho licoroso | menos de 5 g/l / 5 g/l ou mais | 150 / 200 mg/l |

  Certos vinhos doces com menções específicas (por exemplo *Spätlese*) têm limites mais altos, a partir
  de 300 mg/l [19]; em espumantes, os Estados-Membros podem autorizar mais 40 mg/l em zonas de clima
  difícil, só para vinhos que não saiam do país [19].
- **Vinho biológico:** o máximo é mais baixo: 100 mg/l nos tintos e 150 mg/l nos brancos e rosados com
  menos de 2 g/l de açúcar residual; nos restantes vinhos, o máximo geral reduzido em 30 mg/l [22].
  Relevante para os vinhos BIO do catálogo (Cordero di Montezemolo Barolo Monfalletto e Enrico VI BIO,
  Basilisco Teodosio, Valori Abruzzo Pecorino Bio, Bolla Prosecco DOC Biologico).

### 9.3 Protocolo de devolução no restaurante (prática profissional; não verificado)

1. **Ouvir** o cliente sem discutir. Provar o vinho (escanção ou responsável), longe da mesa se possível.
2. **Diagnosticar:**
   - **Defeito claro** (TCA, oxidação, cozido): pedir desculpa, trocar por outra garrafa do mesmo vinho
     (idealmente de outro lote) ou propor alternativa ao mesmo nível de preço. Não cobrar a garrafa
     defeituosa.
   - **Redução:** decantar e voltar a servir passados alguns minutos, explicando o que se fez.
   - **Sem defeito, o cliente não gosta:** a decisão é da casa. Boa prática: propor uma alternativa; se
     houver programa de vinho a copo, a garrafa aberta pode ir para o copo nesse dia.
   - **Temperatura errada:** corrigir (balde ou frigorífico) antes de concluir que o vinho "não presta".
3. **Registar** para reclamar ao fornecedor: data, vinho, colheita, número de lote (a menção "L..." no
   rótulo), descrição do defeito, fotografia do rótulo e da rolha. Guardar a garrafa com a rolha e
   pelo menos metade do vinho, fechada e no frigorífico.
4. **Comunicar ao comercial Emporio** com esses dados. Confirmar a política de substituição ou crédito
   da Emporio antes de a prometer a um cliente (não documentada nesta referência).
5. **Formar a equipa** com uma garrafa com TCA quando aparecer: é a melhor aula possível.

---

## 10. Vedantes

(Descrições: prática profissional; não verificado.)

| Vedante | Como é | Vantagens | Cuidados |
|---|---|---|---|
| **Rolha de cortiça natural** (peça inteira) | Cortiça maciça | Tradição, boa para guarda longa, perceção de qualidade | Risco de TCA e de variação entre garrafas; guardar deitada |
| **Rolha colmatada** | Cortiça natural com poros preenchidos com pó de cortiça | Mais barata, aspeto uniforme | Guarda média |
| **Rolha técnica / aglomerada** | Granulado de cortiça colado; às vezes com discos de cortiça natural nos topos | Consistente, económica | Guarda curta a média |
| **Rolha microaglomerada tratada** | Micro-granulado tratado para remover TCA (há marcas que anunciam limites de TCA libertável) | Risco de TCA muito menor, comportamento regular | Garantias variam por marca e modelo (não verificado) |
| **Rolha sintética** | Polímero | Sem TCA, barata | Deixa passar mais oxigénio; para vinhos de consumo rápido |
| **Cápsula de rosca** (screwcap) | Alumínio com vedante interno que regula a entrada de oxigénio | Sem TCA de rolha, abre sem saca-rolhas, fecha bem depois de aberta, guardável de pé | Pode favorecer redução em alguns vinhos |
| **Rolha de vidro** | Tampa de vidro com anel vedante | Estética, sem TCA | Pouco comum em Itália |
| **Rolha de espumante + gaiola** | Rolha em cogumelo, de aglomerado com discos de cortiça natural, presa por gaiola metálica (*muselet*) | Aguenta a pressão | Segurança na abertura (secção 4) |

**No catálogo:** a Masciarelli tem versões com **tampa metálica** ("Tappo in metallo" no catálogo; o tipo
exato de tampa, em princípio cápsula de rosca, está por confirmar) do Montepulciano d'Abruzzo DOC, do
Trebbiano d'Abruzzo DOC e do Rosato Colline Teatine IGT da Linea Classica. São práticas para vinho a copo
e para esplanada: abrem e fecham sem ferramenta e sem risco de rolha.

**Como falar disto com o cliente:** "a tampa metálica não é sinal de vinho barato; é uma escolha técnica do
produtor para manter o vinho fresco e sem risco de rolha".

---

## 11. Construir uma carta de vinhos para um restaurante italiano em Portugal

### 11.1 Princípios

1. **A carta serve a cozinha.** Primeiro ler o menu: que regiões, que proteínas, que molhos, que
   intensidade. Uma pizzaria napolitana e uma trattoria toscana pedem cartas diferentes.
2. **Coerência italiana, com portas abertas.** Um restaurante italiano vende autenticidade: a base da carta
   deve ser italiana. O cliente português, no entanto, conhece e pede vinho português; a decisão de ter
   alguns vinhos portugueses é comercial e é do restaurante. A Emporio vende vinho italiano: a
   recomendação natural é carta 100 % italiana, ou pelo menos o grosso dela.
3. **Três perguntas antes de escrever:** ticket médio por pessoa (e quanto do ticket é bebida), perfil do
   cliente (turistas, negócios, famílias, conhecedores) e capacidade da equipa para vender e servir.
4. **Legibilidade vence exaustividade.** Uma carta curta, bem escolhida e bem explicada vende mais do que
   uma lista longa que ninguém percebe (prática profissional; não verificado).
5. **Cada referência tem de ter uma razão:** um prato, um preço, um estilo, uma região em falta.
6. **Obrigação legal de base:** todos os vinhos à venda têm de constar da lista de preços, em português,
   com o preço com impostos incluídos (secção 15) [1][2].

### 11.2 Estruturas possíveis

| Estrutura | Como é | Melhor para | Cuidado |
|---|---|---|---|
| **Por estilo** (espumantes, brancos frescos, brancos estruturados, rosados, tintos leves, tintos encorpados, doces) | O cliente escolhe pelo gosto, não pela geografia | Pizzarias, trattorias, clientes pouco conhecedores | Indicar sempre a região em cada vinho |
| **Por região, de norte a sul** (Piemonte, Lombardia, Trentino-Alto Adige, Veneto, Friuli, Toscana, Umbria, Abruzzo, Campania, Puglia, Basilicata, Sicilia...) | Viagem pela Itália | Fine dining, enotecas, clientes conhecedores | Dentro de cada região, ordenar do mais leve ao mais encorpado |
| **Progressiva** (dentro de cada cor, do mais leve ao mais encorpado, ou do mais barato ao mais caro) | O cliente percebe onde está pelo lugar na página | Qualquer carta; combinável com as outras | Não misturar critérios na mesma secção |
| **Híbrida** (estilo nas secções principais, região como subtítulo nos tintos) | Equilíbrio entre simplicidade e profundidade | Trattorias de gama média-alta, hotéis | Manter a lógica visível |

**Ordem clássica das secções:** vinhos a copo (primeira página ou destacados) → espumantes (*bollicine*)
→ brancos (*bianchi*) → rosados (*rosati*) → tintos (*rossi*) → doces e de meditação (*dolci e da
meditazione*) → formatos grandes e meias garrafas → (opcional) aperitivos, amari e grappa.

**Ordem dentro de cada vinho (uma linha):** produtor · nome do vinho · denominação (DOCG/DOC/IGT) ·
região · colheita · (castas) · volume · preço. Boa prática: indicar a colheita, sobretudo nos vinhos em
que muda o estilo ou o preço, e atualizar a carta quando a colheita muda.

### 11.3 Número de referências por tipo de restaurante (prática profissional; não verificado)

| Tipo | Referências em garrafa | A copo | Notas |
|---|---|---|---|
| Pizzaria | 8-15 | 4-6 | 1-2 Prosecco, 3-4 brancos, 1 rosado, 4-6 tintos (médios, frutados), Lambrusco. Preços acessíveis |
| Trattoria / osteria | 20-40 | 6-8 | Todas as cores, 3 patamares de preço, 1-2 vinhos doces |
| Ristorante de gama média-alta | 40-80 | 8-12 | Profundidade em 3-4 regiões-chave (Piemonte, Veneto, Toscana, Campania/Sicilia) |
| Fine dining / enoteca | 120-400+ | 10-20 (com sistema de preservação) | Colheitas verticais, formatos grandes, Riserva |
| Hotel | Restaurante 40-120; bar 15-25; room service 10-15; banquetes 6-10 | 6-12 | Carta de banquetes curta, com stock garantido e preço por pessoa |

Como referência internacional de ambição, os prémios de carta de vinhos da Wine Spectator costumam ser
descritos com patamares de cerca de 90 referências (Award of Excellence), 350 (Best of Award of
Excellence) e 1000 (Grand Award) (não verificado).

### 11.4 Equilíbrio da carta (prática profissional; não verificado)

**Por estilo, numa trattoria com 30 referências:**

| Secção | Número | Peso |
|---|---|---|
| Espumantes (Prosecco, Franciacorta, Trento, Lambrusco) | 4-5 | 15 % |
| Brancos | 8-9 | 30 % |
| Rosados | 2 | 5-7 % |
| Tintos | 12-14 | 40-45 % |
| Doces / meditação | 1-2 | 5 % |

**Por região:** cobrir no mínimo o **Norte** (Piemonte, Veneto, Friuli ou Trentino-Alto Adige), o **Centro**
(Toscana obrigatoriamente; Umbria ou Abruzzo) e o **Sul e ilhas** (Campania, Sicilia, Puglia). Evitar que
uma só região passe de 30-35 % da carta, salvo se o restaurante for regional (uma trattoria toscana pode
ter metade da carta toscana).

**Por preço (em patamares):**

| Patamar | Função | Peso na carta |
|---|---|---|
| Entrada ("vinho da casa" e vinhos a copo) | Porta de entrada, volume | 20-25 % |
| Médio | Onde se vende mais; aqui estão os vinhos "de confiança" | 40-50 % |
| Premium | Ocasiões, clientes de negócios, subida de gama | 20-30 % |
| Prestígio | Imagem da casa (Barolo, Brunello, Amarone, Tignanello, grandes formatos) | 5-10 % |

**Evitar buracos de preço:** entre dois vinhos consecutivos da mesma secção não deve haver saltos
grandes; o cliente que quer "um pouco melhor" tem de encontrar uma opção.

**Cobrir os pedidos que vão aparecer sempre:** um Prosecco, um Pinot Grigio, um Chianti (ou Chianti
Classico), um Montepulciano d'Abruzzo, um Barolo, um Brunello, um Amarone e um Lambrusco são nomes
italianos que o cliente português costuma reconhecer (juízo comercial; não verificado com dados de
vendas).

### 11.5 Especificidades do mercado português (juízo comercial; não verificado)

- **O cliente compara com o supermercado e com o vinho português.** Um vinho italiano desconhecido a um
  preço de carta alto perde contra um Douro ou um Alentejo que o cliente conhece. Compensar com
  descrições claras, sugestão por prato e vinho a copo para provar.
- **Castas-ponte** ajudam a vender: comparar uma casta italiana com um estilo português conhecido. Ver
  `castas.md` para as comparações validadas.
- **Peixe e marisco pesam muito na restauração portuguesa**, mesmo em restaurantes italianos: reforçar
  brancos do Sul (Falanghina, Greco, Fiano, Grillo, Etna Bianco) e espumantes Brut.
- **Esplanada e calor** fazem vender rosados, espumantes e tintos leves servidos frescos.
- **Turistas** (Lisboa, Porto, Algarve) procuram os grandes nomes (Barolo, Brunello, Amarone).

---

## 12. Programa de vinho a copo

### 12.1 Doses e rendimento

| Dose | Copos por garrafa de 75 cl (teórico) | Uso típico |
|---|---|---|
| 7,5 cl | 10 | Vinhos doces, provas, menu de degustação |
| 10 cl | 7,5 | Espumante em flûte, menu de degustação |
| 12,5 cl | 6 | Dose muito usada em restauração |
| 15 cl | 5 | Dose "generosa"; esplanadas, vinho da casa |

**Enquadramento legal:** não se identificou norma portuguesa que imponha uma dose mínima para o vinho a
copo nem que obrigue a indicar a dose. A lei exige que todas as bebidas que o estabelecimento forneça
tenham preço na lista [1], e o regime geral de indicação de preços remete os géneros consumidos no local
em hotéis e estabelecimentos similares para disposições especiais [2]. **Boa prática:** indicar sempre a
dose ("copo 12,5 cl") junto ao preço, para o cliente comparar e para a equipa servir sempre igual.

**Medir sempre:** doseador, copo com marca de enchimento ou medida de 12,5/15 cl. Um empregado que serve
"a olho" 18 cl em vez de 12,5 cl tira só cerca de 4,2 copos da garrafa em vez de 6: **perde quase dois
copos por garrafa** (aritmética).

### 12.2 Quantos vinhos a copo e quais (prática profissional; não verificado)

- **Pizzaria:** 4-6 (um Prosecco, dois brancos, um rosado, dois tintos).
- **Trattoria:** 6-8 (um espumante, três brancos, um rosado, três tintos, e um doce a 7,5 cl).
- **Fine dining:** 10-20, com sistema de preservação e algumas referências de prestígio.
- **Escolher vinhos que aguentam aberto** (secção 8.2), com tampa metálica quando possível (por exemplo
  as versões "Tappo in metallo" da Masciarelli) e que vendam pelo menos uma garrafa por serviço.
- **Rodar a seleção** a cada estação (mais brancos e rosados no verão; mais tintos no inverno) e ter um
  "vinho do mês" para dar a provar vinhos do catálogo menos conhecidos.

### 12.3 Preservação (prática profissional; não verificado)

- **Rolha + frigorífico:** chega para vinhos que se esgotam em 1-2 dias.
- **Bomba de vácuo:** barata; ajuda pouco em vinhos aromáticos (o vácuo também puxa aroma).
- **Gás inerte (árgon) em spray ou em dispensador:** protege a superfície do vinho.
- **Sistema de agulha (tipo Coravin):** uma agulha atravessa a rolha, o vinho é servido e o espaço é
  preenchido com árgon; a rolha volta a fechar ao retirar a agulha. Permite servir a copo vinhos caros sem
  abrir a garrafa. As garrafas com cápsula de rosca e os espumantes precisam de acessórios próprios; a
  duração anunciada pelo fabricante não foi verificada.
- **Dispensadores com gás e refrigeração (tipo enomatic):** investimento alto, controlo de dose e de stock
  muito rigoroso; para enotecas e hotéis.

### 12.4 Controlo e rotação

- Etiqueta em cada garrafa aberta: **data, hora, iniciais**.
- Folha de controlo por turno: garrafas abertas, copos vendidos, garrafas acabadas. Diferenças grandes
  indicam doses erradas, ofertas não registadas ou perdas.
- Provar o primeiro copo de cada garrafa aberta no dia anterior antes de servir.
- A garrafa que chega ao fim de vida vai para a cozinha (molhos, risotto), não para o cliente.

### 12.5 Preço a copo (fórmula; os multiplicadores são prática profissional, não verificado)

O copo tem de pagar as perdas e o risco de sobras, por isso a soma dos copos de uma garrafa rende mais do
que a garrafa vendida inteira.

```
preço_copo_sem_IVA = (custo_garrafa_sem_IVA ÷ copos_reais) × multiplicador_copo
PVP_copo = preço_copo_sem_IVA × 1,23   (vinho servido, continente)
```

- `copos_reais` = 5,5-6 (12,5 cl) ou 4,7-5 (15 cl).
- `multiplicador_copo` um pouco acima do multiplicador usado na garrafa (secção 13).
- **Verificação de coerência:** comparar `copos_reais × PVP_copo` com o PVP da garrafa. Uma diferença de
  cerca de 20-30 % a favor do copo é uma referência de trabalho (não verificado).
- Há uma regra de sala mais agressiva, "**o primeiro copo paga a garrafa**" (o preço de um copo cobre o
  custo de compra da garrafa), usada sobretudo em vinhos de entrada (não verificado).

---

## 13. Preços e margens na restauração

> Esta secção explica **métodos** de fixação de preço. Não contém preços nem margens da Emporio. **Não
> foi encontrada fonte publicada sobre os multiplicadores habituais na restauração portuguesa** (não
> verificado): usar os valores abaixo como hipótese de trabalho e validar com o cliente e com dados de
> mercado (por exemplo AHRESP, DECO Proteste, imprensa especializada).

### 13.1 Conceitos

- **Custo (C):** preço de compra da garrafa, **sem IVA** (o IVA suportado é, em regra, dedutível pelo
  restaurante nos termos gerais do CIVA; confirmar o regime de cada cliente com o contabilista).
- **Preço de venda sem IVA (P):** o que fica para o restaurante.
- **PVP (preço na carta):** P + IVA. No vinho servido no continente, IVA de 23 % [6][10], logo
  **PVP = P × 1,23**. O preço na carta tem de incluir todos os impostos [2].
- **Multiplicador (M):** P ÷ C.
- **Margem bruta em euros:** P − C.
- **Custo de bebida em %:** C ÷ P (o equivalente ao "food cost").

| Multiplicador M | Custo de bebida (C ÷ P) | Margem bruta sobre o preço sem IVA |
|---|---|---|
| 2,0 | 50 % | 50 % |
| 2,5 | 40 % | 60 % |
| 3,0 | 33 % | 67 % |
| 3,5 | 29 % | 71 % |
| 4,0 | 25 % | 75 % |

### 13.2 Métodos de preço

1. **Multiplicador fixo:** P = C × M para toda a carta. Simples, mas torna os vinhos caros caríssimos e
   trava a subida de gama.
2. **Multiplicador decrescente (escalonado)** (valores indicativos; não verificado):

| Custo sem IVA (patamares fictícios) | Multiplicador indicativo |
|---|---|
| até 5 € | 3,0-3,5 |
| 5-10 € | 2,5-3,0 |
| 10-20 € | 2,2-2,5 |
| 20-40 € | 1,8-2,2 |
| mais de 40 € | 1,5-1,8, ou margem fixa em euros |

3. **Margem fixa em euros** para os vinhos de prestígio: P = C + X €. Ganha-se mais euros por garrafa do
   que num vinho barato, e o cliente sente que o vinho caro "compensa".
4. **Preço psicológico e arredondamento:** arredondar o PVP para valores limpos (por exemplo 24 €, 28 €,
   32 €) e manter degraus regulares.

**Exemplo fictício** (C = 10 € sem IVA; não é preço de catálogo):
- Garrafa: M = 2,5 → P = 25,00 € → PVP = 25,00 × 1,23 = 30,75 € → carta a 31 € (ou 30 €, absorvendo
  0,75 €).
- Copo de 15 cl com 5 copos reais: custo por copo 2,00 €; com multiplicador de copo 3,0 → 6,00 € sem IVA
  → 7,38 € → carta a 7,50 €. Cinco copos rendem 37,50 €, cerca de 21 % acima da garrafa.
- Copo de 12,5 cl com 5,7 copos reais: custo por copo 1,75 €; × 3,0 → 5,26 € → 6,47 € → carta a
  6,50 €. Seis copos rendem 39 €, cerca de 26 % acima da garrafa.
- Leitura para a sala: a partir de 4-5 copos do mesmo vinho na mesma mesa, a garrafa compensa ao cliente
  (argumento de venda da secção 18.3).

### 13.3 Arquitetura de preços da carta (prática profissional; não verificado)

- **Vinho mais barato da carta** perto do preço de um prato principal; é a referência mental do cliente.
- **Mais referências no patamar onde o restaurante quer vender** (normalmente o médio).
- **Âncora:** ter alguns vinhos de prestígio faz o patamar médio parecer razoável.
- **Coerência entre copo e garrafa:** o total dos copos de uma garrafa rende mais do que a garrafa
  inteira (secção 12.5), e a equipa sugere a garrafa quando a mesa pede vários copos do mesmo vinho.
- **Rever a carta sempre que muda o preço de compra**, e pelo menos duas vezes por ano.

### 13.4 Como a Emporio pode ajudar o cliente (juízo comercial)

- Propor a carta já com **patamares de preço** e com o vinho a copo resolvido.
- Mostrar **margem em euros por garrafa**, não só multiplicador: é o argumento para o cliente pôr vinhos
  melhores na carta.
- Os preços trade da Emporio e as margens do cliente só se discutem em proposta B2B, com os valores do
  ficheiro privado e a data da tabela; nunca num texto para consumidor final.

---

## 14. IVA e impostos sobre o vinho em Portugal

> Confirmado no texto dos diplomas indicados nas Fontes. As taxas e verbas mudam com os Orçamentos do
> Estado e não foi possível consultar o CIVA consolidado de 2026: confirmar no Portal das Finanças
> (Código do IVA, art. 18.º e listas anexas) antes de uma proposta.

### 14.1 Taxas no continente

- **Taxa reduzida 6 %** (Lista I), **taxa intermédia 13 %** (Lista II) e **taxa normal 23 %** (restantes
  bens e serviços). A intermédia de 13 % e a reduzida de 6 % vêm da Lei 12-A/2010 [9]; a normal passou a
  23 % com a Lei 55-A/2010 [10].

### 14.2 Vinho servido em restaurante, bar ou catering

- A verba 3.1 da Lista II (taxa intermédia) cobre as "prestações de serviços de alimentação e bebidas,
  **com exclusão das bebidas alcoólicas**, refrigerantes, sumos, néctares e águas gaseificadas ou
  adicionadas de gás carbónico ou outras substâncias" [6]. Esta redação produz efeitos desde
  1 de julho de 2016 [6]. Entre 2012 e junho de 2016 os serviços de alimentação e bebidas estavam todos à
  taxa normal, porque o Orçamento do Estado para 2012 revogou as verbas 3 e 3.1 [7].
- **Consequência:** a comida servida paga 13 %; **o vinho servido paga 23 %** (continente).
- **Preço único com comida e vinho** (menu de degustação com vinhos, menu de grupo com bebidas, catering
  "por pessoa" com vinhos incluídos): a mesma verba manda **repartir o valor tributável pelas várias
  taxas**, na proporção do preço de cada elemento segundo a tabela de preços ou do valor normal dos
  serviços; **se não houver repartição, aplica-se a taxa mais elevada à totalidade do serviço** [6].
  **Na prática para a Emporio Italia Catering:** nas propostas com vinho incluído, discriminar o valor
  da comida e o valor das bebidas alcoólicas (ou ter a tabela de preços que permita a repartição); caso
  contrário, todo o evento pode ter de ser faturado a 23 %. Validar com o contabilista.

### 14.3 Vinho vendido em retalho (garrafeira, loja online, supermercado)

- A Lista II inclui a verba **1.10 "Vinhos comuns"** (redação da Lei 109-B/2001, Orçamento do Estado
  para 2002) [8], que não foi revogada pelo Orçamento do Estado para 2012 (que revogou outras verbas da
  mesma lista) [7]. Logo, o vinho comum vendido como bem paga a **taxa intermédia de 13 %** no
  continente.
- **O que é "vinho comum":** segundo o entendimento da AT divulgado em fontes de fiscalidade, o conceito
  abrange os vinhos maduros e verdes, brancos, rosados ou tintos, secos a doces, **desde que não
  classificados como vinhos especiais** [14] (não se consultou o texto integral da informação da AT).
- **Espumantes e vinhos licorosos (Marsala):** na prática corrente são tratados como vinhos especiais e
  ficam à taxa normal de 23 % (não verificado no texto da AT: confirmar com o contabilista antes de
  fixar preços na loja online).
- **Vermute e outros vinhos aromatizados:** são "produtos vitivinícolas aromatizados", com regulamento
  europeu próprio (Reg. (UE) 251/2014) [23], e não vinho; não cabem na verba "vinhos comuns" (taxa
  normal; confirmar com o contabilista).
- Na restauração, esta distinção não interessa: o vinho servido, comum ou espumante, está excluído da
  taxa intermédia [6].

### 14.4 Regiões Autónomas

- Açores e Madeira têm taxas próprias, fixadas no DL 347/85 por remissão do art. 18.º do CIVA [11]. A
  versão consultada desse diploma é de 2015 e os valores mudaram depois disso: **confirmar as taxas em
  vigor antes de faturar para as ilhas** (não verificado para 2026).

### 14.5 Imposto especial de consumo (IEC)

- A taxa do IEC aplicável aos **vinhos tranquilos e espumantes é de 0 €** (CIEC, art. 72.º) [12].
- Os **produtos intermédios** pagam IEC por hectolitro de produto acabado: **87,92 €/hl** na versão
  consolidada do CIEC de 15/04/2026 (art. 74.º) [12]. Na classificação habitual entram aqui os vinhos
  licorosos (Marsala, Porto) e os vermutes; a definição exata do CIEC não foi confirmada. O IEC já vem
  incluído no preço de compra; interessa sobretudo para perceber porque estes produtos custam mais.

---

## 15. Obrigações legais: preços, afixação e venda de álcool

### 15.1 Lista de preços num restaurante (RJACSR, art. 135.º)

Nos estabelecimentos de restauração ou de bebidas **devem existir listas de preços junto à entrada do
estabelecimento e no seu interior**, para disponibilização aos clientes, **obrigatoriamente redigidas em
português**, com [1]:
- a indicação de **todos os pratos, produtos alimentares e bebidas** que o estabelecimento forneça e os
  respetivos preços, incluindo os do couvert, quando existente;
- a transcrição da regra de que **nenhum prato, produto alimentar ou bebida, incluindo o couvert, pode
  ser cobrado se não for solicitado pelo cliente ou por este for inutilizado** [1].
- **Couvert** é o conjunto de alimentos ou aperitivos identificados na lista como couvert, fornecidos a
  pedido do cliente antes do início da refeição [1].
- Quando o estabelecimento dispuser de equipamento adequado, a lista deve ser redigida também em
  **braille** [1].

**O que isto significa para a carta de vinhos:**
- **Todos os vinhos à venda têm de estar na lista com preço.** Não há "vinhos de cave" vendidos sem preço
  na lista, nem garrafas "sugeridas" sem preço visível.
- A carta pode ter traduções, mas **a versão em português é obrigatória** [1]. A regra geral do RJACSR
  (art. 26.º) exige que a informação sobre bens e serviços oferecidos ao público seja redigida em
  português, incluindo a facultada nos locais de venda [1].
- Um vinho oferecido "de boas-vindas" que o cliente não pediu **não pode ser cobrado** [1].
- **Os preços incluem todos os impostos, taxas e encargos**, em euros, de modo que o consumidor conheça o
  montante exato a pagar [2]. Os preços dos serviços devem constar de listas ou cartazes afixados de
  forma visível no local onde são propostos [2].

**Venda a retalho (loja online, garrafeira da Emporio):** o DL 138/90 obriga a exibir o preço de venda
ao consumidor e, nos géneros alimentícios, também o **preço por litro** [2]. Em promoções, a informação
de redução de preço tem de indicar o preço mais baixo praticado nos 30 dias anteriores [2]. Estas regras
não se aplicam a compras para atividade profissional (vendas B2B a restaurantes) [2].

### 15.2 Afixação à entrada (RJACSR, art. 134.º)

Junto à entrada, em local destacado, a entidade exploradora afixa [1]:
- nome e entidade exploradora;
- restrições de acesso ou permanência (por exemplo, admissão de menores e fumadores);
- permissão de admissão de animais de companhia, se aplicável (os cães de assistência não contam como
  restrição);
- símbolo internacional de acessibilidades, quando aplicável;
- consumo ou despesa mínima obrigatória, quando exista, em estabelecimentos com dança ou espetáculo
  (obrigatoriamente visível do exterior);
- existência de **livro de reclamações** (o RJACSR remete para o DL 156/2005) [1]. Hoje existe também o
  livro de reclamações eletrónico (não verificado nesta sessão quanto às obrigações atuais).

Facultativamente, pode afixar línguas faladas, especialidades da casa, climatização e distinções [1].

### 15.3 Venda de bebidas alcoólicas (DL 50/2013)

- É proibido **facultar, vender ou colocar à disposição** bebidas alcoólicas, em locais públicos ou
  abertos ao público, **a menores** e a quem se apresente **notoriamente embriagado** ou aparente possuir
  anomalia psíquica [3]. Desde o DL 106/2015 a proibição abrange todos os menores, qualquer que seja a
  bebida alcoólica [4]; a maioridade atinge-se aos 18 anos (Código Civil, art. 122.º e seguintes) [5].
- Pode ser exigido documento de identificação para comprovar a idade, e deve sê-lo **sempre que haja
  dúvidas** [3].
- A proibição tem de constar de **aviso afixado de forma visível**, impresso, em carateres facilmente
  legíveis e sobre fundo contrastante [3].
- É proibida a venda de bebidas alcoólicas, entre outros, em máquinas automáticas e em estabelecimentos
  de restauração situados em estabelecimentos de saúde; a proibição entre as 0 h e as 8 h não se aplica
  aos estabelecimentos de restauração ou de bebidas [3].
- Os restaurantes e bares só devem permitir, **para consumo fora do espaço licenciado** (por exemplo na
  via pública), recipientes de material leve e não contundente [3].
- Em recintos de espetáculo, serviço em recipientes leves e não contundentes, com as exceções da secção
  7.4 [3].
- **Coimas:** vender a menores ou a pessoas embriagadas é contraordenação económica **muito grave**; a
  falta do aviso é **grave**, ambas punidas nos termos do Regime Jurídico das Contraordenações
  Económicas [3].

**Na prática em catering:** briefing à equipa antes do evento sobre a recusa de servir menores e
convidados embriagados; em casamentos, combinar com os noivos como se identificam os menores.

### 15.4 Modelo de rodapé legal para a carta (texto-modelo)

> Preços em euros, com IVA incluído à taxa legal em vigor. Nenhum prato, produto alimentar ou bebida,
> incluindo o couvert, pode ser cobrado se não for solicitado pelo cliente ou por este for inutilizado.
> Todos os vinhos contêm sulfitos; alguns podem conter vestígios de ovo ou leite usados na clarificação:
> peça informação à equipa. Não é permitida a venda de bebidas alcoólicas a menores de 18 anos.
> Este estabelecimento dispõe de livro de reclamações.

(A frase sobre o couvert é a transcrição exigida pelo art. 135.º, n.º 1, alínea b), do RJACSR [1]. O
aviso sobre menores tem de estar **afixado** no estabelecimento [3]; repeti-lo na carta é facultativo.)

---

## 16. Alergénios, sulfitos e rotulagem que chega à mesa

### 16.1 Sulfitos como alergénio

- O anexo II do Regulamento (UE) 1169/2011 inclui, no ponto 12, o **"dióxido de enxofre e sulfitos em
  concentrações superiores a 10 mg/kg ou 10 mg/litro, expressos em SO₂ total"** [17]. Praticamente todos
  os vinhos passam este limiar, incluindo muitos vinhos "sem sulfitos adicionados", porque a
  fermentação produz sulfitos (não verificado quanto a valores típicos).
- **No rótulo** de vinho, a menção faz-se com os termos fixados por lei: em português "sulfitos" ou
  "dióxido de enxofre"; em italiano "solfiti" ou "anidride solforosa" [20]. O mesmo anexo define os
  termos para ovo (em português "ovo", "proteína de ovo", "produto de ovo", "lisozima de ovo",
  "albumina de ovo") e leite ("leite", "produtos de leite", "caseína de leite", "proteína de leite"),
  usados quando ficam resíduos de clarificantes [20].

### 16.2 No restaurante e no catering (géneros não pré-embalados)

- Um **estabelecimento de restauração coletiva**, na definição europeia, inclui restaurantes, cantinas,
  escolas, hospitais e empresas de catering [17]. Nos alimentos oferecidos sem pré-embalagem, **a
  informação sobre alergénios é obrigatória** [17].
- Em Portugal, os géneros fornecidos por estabelecimentos de restauração coletiva têm de indicar a
  denominação e os alergénios; os alergénios **devem estar disponíveis em qualquer suporte que permita a
  sua fácil apreensão pelo consumidor**; a denominação pode não estar imediatamente disponível, desde que
  se indique de modo bem visível como obter a informação [13]. A autoridade competente é a DGAV, sem
  prejuízo das competências da ASAE [13].
- **Garrafa servida inteira:** o rótulo já traz a menção (é um produto pré-embalado).
  **Vinho a copo, jarro ou cocktail com vinho (Spritz, Bellini):** o cliente não vê o rótulo, por isso
  a informação tem de estar disponível de outra forma (carta, quadro de alergénios, ficha na sala)
  (interpretação dos textos citados; confirmar com a ASAE/DGAV).
- **Solução simples:** uma linha na carta ("Todos os vinhos contêm sulfitos...") e um quadro de alergénios
  da carta de bebidas, com os vinhos que declaram ovo ou leite no rótulo.

### 16.3 Ingredientes e declaração nutricional dos vinhos

- Desde **8 de dezembro de 2023**, o rótulo dos vinhos tem de incluir a **declaração nutricional** e a
  **lista de ingredientes** [21]. A declaração nutricional pode limitar-se, no rótulo físico, ao **valor
  energético** (símbolo "E"), com a declaração completa por **meio eletrónico** identificado na garrafa
  (por exemplo código QR); a lista de ingredientes também pode ir para o meio eletrónico. Em ambos os
  casos, sem recolha nem rastreio de dados do utilizador e sem mistura com informação comercial [21].
  **Os alergénios têm de estar sempre no rótulo físico**, com a palavra "contém" seguida do nome da
  substância [21].
- Os vinhos produzidos antes dessa data podem, em princípio, ser vendidos até ao esgotamento das
  existências (não verificado). Em colheitas antigas do catálogo é normal não haver código QR.
- **Para a sala:** quando um cliente pergunta "que tem este vinho?", o código QR do contrarrótulo é a
  fonte oficial.

### 16.4 Vinhos vegan, biológicos e "naturais"

- **Vegan:** vinho sem clarificantes de origem animal (ovo, caseína, gelatina, cola de peixe). Só se
  afirma se o produtor o declarar.
- **Biológico:** certificação oficial europeia, com limites de SO₂ mais baixos (secção 9.2) [22].
- **"Natural":** não é categoria legal (não verificado); não usar como argumento de saúde.

---

## 17. Escrever as descrições da carta

### 17.1 Fórmula (prática profissional; não verificado)

**Linha de identificação:** Produtor · Vinho · Denominação · Região · Colheita · volume

**Descrição (15-25 palavras):** 1 frase de estilo e aroma + 1 frase de uso (prato ou momento).

> **Masciarelli · Gianni Masciarelli · Montepulciano d'Abruzzo DOC** · Abruzzo
> Tinto vivo e versátil, cereja, groselha e violeta, sem madeira. Pizza, massas com ragù, grelhados.
> (notas de prova segundo a descrição do produtor no catálogo)

### 17.2 Regras

1. **Português claro, sem jargão.** "Fresco", "frutado", "macio", "encorpado", "mineral", "floral",
   "especiado", "vivo" são palavras que o cliente percebe. Evitar listas de 8 aromas.
2. **Uma ideia forte por vinho** (a casta, o sítio, o estilo, o prato).
3. **Termos italianos em italiano** (DOCG, Riserva, Satèn, Metodo Classico, Ripasso, Superiore), com
   explicação curta onde ajude. Ver `glossario.md`.
4. **Nada de promessas que o vinho não cumpre** nem de pontuações antigas de outra colheita.
5. **Factos só se confirmados** na ficha do produtor (estágio, castas, altitude). Se não houver
   confirmação, descrever estilo em vez de técnica.
6. **Sugestão por prato** ligada ao menu real do restaurante ("com o Raviolo Amatriciano").
7. **Mesma estrutura em todas as linhas**, para a carta ser fácil de ler.
8. **Colheita e volume** visíveis; "copo 12,5 cl" no vinho a copo.
9. **Termos de doçura com significado legal:** não chamar "secco" ou "dolce" a um vinho por impressão;
   usar o termo do rótulo (tabela 17.3).

### 17.3 Vocabulário útil (português ↔ italiano)

| Português | Italiano | Uso |
|---|---|---|
| espumante | spumante / bollicine | secção de espumantes |
| frisante | frizzante | Lambrusco, Prosecco frizzante |
| branco / tinto / rosado | bianco / rosso / rosato | secções |
| encorpado | corposo, strutturato | tintos de guarda |
| fresco (acidez viva) | fresco, vivace | brancos, tintos leves |
| sápido, salino | sapido | brancos do Sul, vulcânicos |
| vinho de meditação | vino da meditazione | passiti, Amarone velho |

**Termos de doçura dos vinhos tranquilos** (Reg. Delegado (UE) 2019/33, anexo III, parte B) [20]:

| Português | Italiano | Açúcar |
|---|---|---|
| seco | secco, asciutto | até 4 g/l, ou até 9 g/l se a acidez total (em ácido tartárico) não estiver mais de 2 g/l abaixo do açúcar |
| meio seco | abboccato | acima do limite anterior e até 12 g/l, ou até 18 g/l se a acidez total não estiver mais de 10 g/l abaixo do açúcar |
| meio doce | amabile | acima do limite anterior e até 45 g/l |
| doce | dolce | pelo menos 45 g/l |

Para os espumantes, usar a escala da secção 6.2.

### 17.4 Exemplos com vinhos do catálogo (textos-modelo; validar com a ficha do produtor)

Os exemplos com fonte seguem as fichas dos produtores; os restantes são textos de estilo, sem afirmações
técnicas, a confirmar antes de imprimir.

- **Donnafugata · Anthìlia · Sicilia DOC Bianco** — Citrinos e fruta de polpa branca, com toque floral;
  fresco e sápido. Entradas, peixe cru ou frito, queijos frescos [25].
- **Donnafugata · Sherazade · Sicilia DOC Nero d'Avola** — Framboesa e ameixa, especiado suave, taninos
  macios; servido ligeiramente fresco. Pizza, esparguete com tomate, sopas de peixe [27].
- **Gianni Masciarelli · Cerasuolo d'Abruzzo DOC** — Rosado de cor cereja, morango, cereja e rosa-brava;
  cheio e fresco. Peixe frito, massa fresca, pizza [31].
- **Villa Sandi · Valdobbiadene Prosecco Superiore DOCG Millesimato Brut** — Bolha fina e final seco.
  Aperitivo, marisco, presunto (texto de estilo).
- **Berlucchi · '61 Satèn · Franciacorta DOCG** — Metodo Classico lombardo, bolha cremosa. Do aperitivo
  ao Parmigiano Reggiano (texto de estilo).
- **Allegrini · Valpolicella Classico DOC** — Tinto leve e vivo, fruta vermelha; bom ligeiramente
  fresco. Charcutaria, massas simples (texto de estilo).
- **Fontanafredda · Barolo del Comune di Serralunga d'Alba DOCG** — Nebbiolo de Serralunga, estruturado,
  de taninos firmes. Carne assada, trufa, porcini. Decantado (texto de estilo).
- **Feudi di San Gregorio · Greco di Tufo DOCG** — Branco da Irpinia com corpo e frescura. Massas de
  marisco, peixe no forno (texto de estilo).

---

## 18. Formação da equipa de sala e técnicas de venda

(Métodos: prática profissional; não verificado.)

### 18.1 Programa mínimo de formação (4 sessões de 60-90 minutos)

| Sessão | Conteúdo | Material |
|---|---|---|
| 1. Serviço | Temperaturas, copos, abertura segura de espumante, protocolo à mesa, decantação | Garrafas de treino, termómetro, decantador |
| 2. Itália em 60 minutos | As regiões da carta, as castas principais, DOCG/DOC/IGT, termos do rótulo (Classico, Superiore, Riserva) | Mapa, `classificacao-e-rotulagem.md`, `regioes-*.md` |
| 3. A carta da casa | Prova de todos os vinhos a copo e dos 6-8 mais vendidos; frase de venda de cada um; harmonização com o menu | Fichas de vinho de 1 página |
| 4. Venda, defeitos e lei | Técnicas de sugestão, objeções, gestão de devoluções, reconhecimento de TCA e oxidação; venda a menores e embriagados; alergénios | Garrafa com defeito (quando houver), guião de venda |

**Manutenção:** prova de 10 minutos antes do serviço sempre que entra um vinho novo; "vinho da semana"
provado por toda a equipa; ficha de 1 página por vinho com produtor, região, castas, estilo, temperatura,
3 pratos e 1 frase de venda.

### 18.2 Guião de sugestão por prato

1. **Perguntar antes de propor:** "Prefere branco, tinto ou espumante? Leve ou mais encorpado? Já tem um
   prato em mente?"
2. **Ligar ao prato:** "Com o *Paccheri al Pistacchio e Stracciatella* sugeria um branco com corpo e
   frescura, como o Lugana da Allegrini."
3. **Dar duas ou três opções em patamares diferentes**, apontando na carta (o cliente mostra o orçamento
   sem ter de o dizer).
4. **Explicar numa frase** porque resulta.
5. **Confirmar a temperatura e o serviço**, citando o produtor quando a ficha o indicar ("vou trazê-lo
   ligeiramente fresco, a 15-16 °C, como a Donnafugata recomenda para o Sherazade" [27]).

### 18.3 Técnicas de subida de gama e de venda adicional

- **Espumante de boas-vindas** proposto na chegada ("começamos com um Prosecco ou um Franciacorta?").
- **Garrafa em vez de copos:** mesa de 3 ou mais que pede copos do mesmo vinho → sugerir a garrafa
  (5 copos de 15 cl = 75 cl; secção 13.2).
- **Magnum** para mesas de 6 ou mais e para celebrações.
- **"Um degrau acima":** quando o cliente escolhe, sugerir com naturalidade uma opção ligeiramente acima e
  dizer o que ganha ("o Nipozzano Riserva tem mais estrutura para o filetto").
- **Segunda garrafa:** perguntar quando falta um copo por pessoa, não quando a garrafa já acabou.
- **Vinho com a sobremesa:** Asti DOCG com o *Tiramisu all'Amaretto e Frutti di Bosco*, dose de 7,5 cl.
- **Prova gratuita** de 2-3 cl do vinho a copo em dúvida.
- **Sugestão escrita na carta de comida** ("com este prato: ...") e no quadro do dia.

**Evitar:** empurrar o vinho mais caro sem razão; comentar o preço de forma embaraçosa; corrigir a escolha
do cliente; encher copos em excesso para acelerar a segunda garrafa; servir quem esteja notoriamente
embriagado (é proibido) [3].

### 18.4 Objeções comuns e respostas

| Objeção | Resposta |
|---|---|
| "Não conheço vinhos italianos" | Comparar com uma região portuguesa que o cliente conheça e oferecer prova do vinho a copo |
| "Prefiro vinho português" | Casta-ponte ou estilo equivalente (`castas.md`); oferecer prova do vinho a copo |
| "Está caro" | Mostrar a opção do patamar abaixo com a mesma lógica de harmonização |
| "Só bebo tinto" (com peixe) | Tinto leve e fresco (Valpolicella, Sherazade a 15-16 °C) ou um rosado com estrutura (Cerasuolo) |
| "O vinho sabe a rolha" | Protocolo da secção 9.3, sem discutir |

### 18.5 Indicadores para acompanhar

- Vendas de vinho por coberto e em % das vendas totais.
- % de mesas com vinho; garrafas por mesa.
- Venda a copo vs. garrafa; perdas no vinho a copo (folha de controlo).
- Os 5 vinhos mais e menos vendidos (os menos vendidos saem da carta ou mudam de lugar/descrição).

---

## 19. Modelos de carta de vinhos italiana (catálogo Emporio)

> **Antes de usar um modelo:** confirmar estado e disponibilidade de cada vinho com
> `python3 scripts/procurar_vinhos.py --estado todos --texto "<vinho>"` e preencher os preços com o
> cliente. Os nomes seguem o catálogo Emporio (Odoo de fevereiro de 2026 e lista trade de 2024); os
> vinhos marcados **†** constam da lista de 2024 mas não foram confirmados no catálogo de 2026. As
> descrições são textos-modelo (secção 17). Preços: sempre `€ __` (ver confidencialidade no topo).

### 19.1 Modelo A — Trattoria / ristorante (cerca de 40 referências, estrutura por estilo)

```
─────────────────────────────────────────────────────────────
                 CARTA DEI VINI · CARTA DE VINHOS
─────────────────────────────────────────────────────────────

VINI AL CALICE · VINHOS A COPO                copo 12,5 cl · garrafa 75 cl
  Prosecco DOC Treviso Brut "Il Fresco" · Villa Sandi† · Veneto     € __ · € __
  Pinot Grigio delle Venezie DOC · Corte Giara (Allegrini) · Veneto € __ · € __
  Falanghina del Sannio DOC · Feudi di San Gregorio · Campania      € __ · € __
  Cerasuolo d'Abruzzo DOC · Gianni Masciarelli · Abruzzo            € __ · € __
  Montepulciano d'Abruzzo DOC · Masciarelli (tampa metálica)        € __ · € __
  Chianti DOCG · Cecchi · Toscana                                   € __ · € __
  Valpolicella Ripasso Superiore DOC Black Label · Pasqua† · Veneto € __ · € __
  Asti DOCG · Fontanafredda · Piemonte                   copo 7,5 cl € __

BOLLICINE · ESPUMANTES
  Valdobbiadene Prosecco Superiore DOCG Millesimato Brut · Villa Sandi†      € __
  Prosecco DOC Rosé Brut · Carpenè Malvolti · Veneto                         € __
  Trento DOC Brut · Ferrari · Trentino                                       € __
  Franciacorta DOCG '61 Extra Brut · Berlucchi · Lombardia                   € __
  Franciacorta DOCG '61 Satèn · Berlucchi · Lombardia                        € __
  Franciacorta DOCG Alma Gran Cuvée Brut · Bellavista · Lombardia            € __
  Lambrusco Otello Nerodilambrusco 1813 · Ceci · Emilia-Romagna (IGT)        € __

BIANCHI FRESCHI E AROMATICI · BRANCOS FRESCOS E AROMÁTICOS
  Soave Classico DOC Villa Borghetti · Pasqua† · Veneto                      € __
  Lugana DOC · Allegrini · Veneto/Lombardia                                  € __
  Gavi DOCG (Gavi di Gavi) · Fontanafredda · Piemonte                        € __
  Roero Arneis DOCG Pradalupo · Fontanafredda · Piemonte                     € __
  Sicilia DOC Grillo SurSur · Donnafugata · Sicilia                          € __
  Abruzzo Pecorino DOC Castello di Semivicoli · Masciarelli · Abruzzo        € __

BIANCHI DI STRUTTURA · BRANCOS ESTRUTURADOS
  Greco di Tufo DOCG · Feudi di San Gregorio · Campania                      € __
  Fiano di Avellino DOCG · Feudi di San Gregorio · Campania                  € __
  Etna Bianco DOC Isolano · Donnafugata (Dolce&Gabbana) · Sicilia            € __
  Vintage Tunina · Venezia Giulia IGT · Jermann · Friuli Venezia Giulia      € __
  Cervaro della Sala · Umbria IGT · Castello della Sala (Antinori)           € __

ROSATI · ROSADOS
  Alìe Rosé · Toscana IGT · Tenuta Ammiraglia (Frescobaldi)                  € __
  Sicilia DOC Rosato Rosa · Donnafugata (Dolce&Gabbana)                      € __

ROSSI LEGGERI E MEDI · TINTOS LEVES E MÉDIOS
  Valpolicella Classico DOC · Allegrini · Veneto                             € __
  Barbera d'Alba DOC · Cordero di Montezemolo · Piemonte                     € __
  Langhe Nebbiolo DOC · Cordero di Montezemolo · Piemonte                    € __
  Chianti Classico DOCG · Banfi · Toscana                                    € __
  Sicilia DOC Nero d'Avola Sherazade · Donnafugata · Sicilia                 € __

ROSSI DI CORPO · TINTOS ENCORPADOS
  Chianti Rufina Riserva DOCG Nipozzano · Frescobaldi · Toscana              € __
  Montefalco Rosso DOC · Arnaldo Caprai · Umbria                             € __
  Irpinia Aglianico DOC Rubrato · Feudi di San Gregorio · Campania           € __
  Montepulciano d'Abruzzo DOC Riserva Marina Cvetic · Masciarelli · Abruzzo  € __
  Bolgheri Rosso DOC Stupore · Campo alle Comete · Toscana                   € __

GRANDI ROSSI · GRANDES TINTOS
  Barolo DOCG Monfalletto (bio) · Cordero di Montezemolo · Piemonte   20__   € __
  Brunello di Montalcino DOCG Castelgiocondo · Frescobaldi · Toscana  20__   € __
  Amarone della Valpolicella Classico DOCG · Allegrini · Veneto       20__   € __
  Taurasi DOCG · Feudi di San Gregorio · Campania                     20__   € __
  Montefalco Sagrantino DOCG 25 Anni · Arnaldo Caprai · Umbria        20__   € __
  Tignanello · Toscana IGT · Antinori                                 20__   € __

DOLCI E DA MEDITAZIONE · DOCES E DE MEDITAÇÃO               copo 7,5 cl · garrafa
  Moscato di Pantelleria DOC Kabir · Donnafugata (37,5 cl)            € __ · € __
  Pomino Vin Santo DOC · Frescobaldi                                  € __ · € __
  Barolo Chinato · Fontanafredda                                      € __ · € __

GRANDI FORMATI · FORMATOS GRANDES
  Franciacorta DOCG Alma Gran Cuvée Brut · Bellavista · 3 L / 6 L            € __
  Montepulciano d'Abruzzo DOC · Gianni Masciarelli · Jeroboam 3 L            € __

─────────────────────────────────────────────────────────────
Preços em euros, com IVA incluído à taxa legal em vigor. Nenhum prato,
produto alimentar ou bebida, incluindo o couvert, pode ser cobrado se não
for solicitado pelo cliente ou por este for inutilizado. Todos os vinhos
contêm sulfitos; peça à equipa informação sobre outros alergénios.
Venda de bebidas alcoólicas proibida a menores de 18 anos.
Colheitas sujeitas a alteração.
─────────────────────────────────────────────────────────────
```

**Notas ao modelo A:**
- Cerca de 40 referências em garrafa + 8 a copo; 3 patamares em cada secção; todas as grandes regiões.
- Denominações a confirmar no rótulo antes de imprimir: a menção "Classico" do Soave Villa Borghetti, a
  IGT exata do Lambrusco Otello e a forma de indicar o Gavi da Fontanafredda.
- Variante **por região** para fine dining: reorganizar as mesmas referências em Piemonte → Lombardia →
  Trentino → Veneto → Friuli → Toscana → Umbria → Abruzzo → Campania → Sicilia, e dentro de cada região
  do mais leve ao mais encorpado.

### 19.2 Modelo B — Pizzaria (12 referências, 5 a copo)

```
BOLLICINE
  Prosecco DOC Extra Dry · Bolla                                copo € __ · garrafa € __
  Lambrusco Dry G. Verdi "Antico Bruscone" · Ceci (Emilia IGT)              garrafa € __
BIANCHI
  Pinot Grigio delle Venezie DOC · Corte Giara                  copo € __ · garrafa € __
  Falanghina del Sannio DOC · Feudi di San Gregorio                         garrafa € __
  Sicilia DOC Grillo "Mbettata" · Cantina Orsogna                           garrafa € __
ROSATI
  Cerasuolo d'Abruzzo DOC · Gianni Masciarelli                  copo € __ · garrafa € __
ROSSI
  Montepulciano d'Abruzzo DOC · Masciarelli (tampa metálica)    copo € __ · garrafa € __
  Sicilia DOC Nero d'Avola Sherazade · Donnafugata                          garrafa € __
  Chianti DOCG · Cecchi                                         copo € __ · garrafa € __
  Primitivo di Manduria DOC · Feudi di San Gregorio†                        garrafa € __
  Valpolicella Classico DOC · Allegrini                                     garrafa € __
  Chianti Classico DOCG · Banfi                                             garrafa € __
```

Lógica: tintos médios, frutados e frescos para tomate e mozzarella (a Donnafugata recomenda o Sherazade
com pizza e esparguete com tomate [27]; a Masciarelli indica pizza para o Cerasuolo [31]); Lambrusco
para a pizza com charcutaria; Prosecco para aperitivo. (No Lambrusco G. Verdi, a lista de 2024 indica
DOC e o Odoo de 2026 indica Emilia IGT: confirmar no rótulo.)

### 19.3 Modelo C — Hotel: carta de banquetes (6-8 referências, preço por pessoa)

| Pacote | Espumante | Branco | Tinto | Doce |
|---|---|---|---|---|
| Essencial | Prosecco DOC (Bolla ou Villa Sandi Il Fresco†) | Pinot Grigio Corte Giara | Montepulciano d'Abruzzo Masciarelli | — |
| Clássico | Prosecco Superiore DOCG (Villa Sandi† ou Bolla) | Lugana Allegrini | Chianti Classico / Nipozzano Riserva | Asti Fontanafredda |
| Prestígio | Franciacorta Berlucchi '61 ou Bellavista Alma | Greco di Tufo ou Cervaro della Sala | Barolo ou Brunello | Kabir |

Lembrar a regra da repartição do IVA num preço por pessoa com comida e vinho (secção 14.2) [6].

---

## 20. Menu de catering Emporio: serviço, ordem e quantidades

A escolha fina dos vinhos está em `harmonizacao.md`. Aqui ficam a ordem de serviço, as temperaturas
(prática profissional, salvo indicação de fonte) e um exemplo de quantidades.

### 20.1 Sequência sugerida

| Momento | Pratos do menu | Estilo de vinho | Opções do catálogo | Temperatura |
|---|---|---|---|---|
| Receção | Focaccia, Grissini & Taralli; Prosciutto di Parma & Prosciutto Crudo; Mortadella, Bresaola & Coppa | Espumante seco e frutado; Lambrusco seco | Prosecco Superiore Brut (Villa Sandi†) ou Bolla Prosecco Superiore; Berlucchi '61 Extra Brut; Ceci Otello | 6-9 °C; Lambrusco 10-12 °C |
| Antipasti | Parmigiano Reggiano & Burrata di Andria; Peperoni Ripieni & Carciofi Grigliati | Metodo Classico; branco fresco e sápido (a alcachofra torna muitos vinhos adocicados: preferir brancos secos de acidez viva; não verificado) | Berlucchi '61 Satèn; Soave Classico Pasqua†; Gavi Fontanafredda | 8-10 °C |
| Antipasto de trufa | Crema di Tartufo Nero & Porcini | Nebbiolo jovem ou branco estruturado | Langhe Nebbiolo Cordero di Montezemolo; Fiano di Avellino Feudi | tinto 16 °C; branco 11-12 °C |
| Primi de mar | Spaghettoni Cacio e Pepe di Mare; Risotto Verde con Cozze e Tartare di Tonno | Branco do Sul com corpo e salinidade; rosado para o atum | Greco di Tufo Feudi; Etna Bianco Isolano; Cerasuolo Masciarelli (10-12 °C [31]) | 9-12 °C |
| Primi de terra | Raviolo Amatriciano con Tartufo Nero; Paccheri al Pistacchio e Stracciatella | Tinto médio de boa acidez (amatriciana); branco cremoso e fresco (pistácio) | Chianti Classico Banfi ou Barbera d'Alba Cordero; Lugana Allegrini | tinto 16 °C; branco 10 °C |
| Secondo | Filetto in Crosta di Speck con Porcini | Tinto de guarda, taninos finos | Nipozzano Riserva; Brunello Castelgiocondo; Barolo Fontanafredda (decantado) | 16-18 °C |
| Dolce | Tiramisu all'Amaretto e Frutti di Bosco | Espumante doce e aromático, pouco álcool | Asti DOCG Fontanafredda; Kabir (37,5 cl) | 6-8 °C; Kabir 8-10 °C |

### 20.2 Exemplo de quantidades: jantar volante + sentado, 80 convidados, 72 bebem, 4 horas

| Momento | Vinho | Copos por pessoa | Dose | Garrafas (sem margem) | Com 10 % |
|---|---|---|---|---|---|
| Receção (45 min) | Prosecco Superiore | 1,5 | 10 cl | 72 × 1,5 ÷ 7,5 = 14,4 | 16 |
| Antipasti + primi de mar | Branco (Greco di Tufo) | 1,5 | 12,5 cl | 72 × 1,5 ÷ 6 = 18 | 20 |
| Primi de terra + secondo | Tinto (Nipozzano Riserva) | 2 | 12,5 cl | 72 × 2 ÷ 6 = 24 | 27 |
| Sobremesa | Asti DOCG | 1 | 7,5 cl | 72 × 1 ÷ 10 = 7,2 | 8 |
| **Total** | | **6 copos** | | **63,6** | **71 garrafas** (≈ 1 por pessoa que bebe) |

(As doses por pessoa são prática profissional; não verificado. As contas são aritmética.)

Material: cerca de 240 copos de vinho (3 por pessoa) + 80 flûtes + reserva de 10-15 %; 5-6 baldes;
70-100 kg de gelo; 60-80 litros de água; 2 pessoas dedicadas ao vinho (prática profissional; não
verificado). Na proposta, discriminar comida e bebidas alcoólicas para a repartição do IVA (secção 14.2)
[6].

---

## 21. Listas de verificação

### 21.1 Abertura de serviço no restaurante

- [ ] Temperaturas dos armários de serviço conferidas (termómetro).
- [ ] Garrafas a copo abertas no dia anterior provadas; etiquetas com data e hora.
- [ ] Baldes, gelo, panos, saca-rolhas, decantadores limpos e sem cheiro.
- [ ] Copos polidos e cheirados.
- [ ] Carta atualizada (colheitas, vinhos esgotados retirados ou assinalados); todos os vinhos à venda com
      preço na lista [1].
- [ ] Doseadores / copos com marca na estação de vinho a copo.
- [ ] Aviso de proibição de venda de álcool a menores afixado [3]; lista de preços à entrada e no
      interior, em português [1]; livro de reclamações disponível e anunciado à entrada [1].
- [ ] Informação de alergénios da carta de bebidas acessível [13].

### 21.2 Evento de catering

- [ ] Contas de quantidades feitas com a fórmula da secção 7.3 e validadas com o cliente.
- [ ] Proposta com comida e bebidas alcoólicas discriminadas (repartição do IVA) [6].
- [ ] Acordo sobre garrafas não abertas no fim do evento.
- [ ] Temperatura: espumantes e brancos a frio desde a véspera; tintos protegidos do calor.
- [ ] Gelo, baldes, copos (2-3 por pessoa + reserva), flûtes, água.
- [ ] Grandes tintos decantados na copa e identificados.
- [ ] Briefing: abertura segura de espumante; não servir menores nem convidados embriagados [3].
- [ ] Recipientes leves se o local for recinto de espetáculo sem exceção aplicável [3].
- [ ] Informação de alergénios disponível para vinho a copo e cocktails [13].
- [ ] Registo de garrafas abertas e de eventuais defeitos (lote, fotografia) para a Emporio.

---

## 22. Pendentes de verificação

Itens que não foi possível confirmar em fonte (pesquisa web esgotada; acesso direto aos sites
bloqueado). Confirmar antes de usar como facto:

1. **Temperaturas por estilo** (tabela 2.2, colunas sem fonte), temperatura e humidade de cave, vida de
   uma garrafa aberta: confirmar em Decanter, Wine Spectator, GuildSomm ou nos consórcios (Franciacorta,
   Prosecco DOC, Conegliano Valdobbiadene, Trentodoc).
2. **Recomendação de copo de tulipa** pelos consórcios de espumante italianos.
3. **Pressão típica do Metodo Classico** (5-6 bar) e do Satèn; velocidade da rolha e dados de lesões
   oculares.
4. **Limiar sensorial do TCA** e compostos do Brett (AWRI, OIV).
5. **Consumo por convidado** em eventos (tabela 7.2): não há fonte oficial; comparar com o histórico da
   Emporio Italia Catering.
6. **Número de referências por tipo de restaurante e patamares da Wine Spectator** (90 / 350 / 1000).
7. **Multiplicadores e margens na restauração portuguesa**: procurar dados da AHRESP, da DECO Proteste ou
   da imprensa especializada.
8. **IVA do espumante e dos licorosos no retalho**: obter o texto integral da informação vinculativa da AT
   sobre a verba 1.10 "Vinhos comuns".
9. **Taxas de IVA em vigor nos Açores e na Madeira em 2026** e eventuais alterações ao CIVA em 2025-2026.
10. **Definição de "produtos intermédios" no CIEC.**
11. **Regime transitório dos rótulos** (vinhos produzidos antes de 8/12/2023 vendáveis até esgotar).
12. **Livro de reclamações eletrónico:** obrigações atuais (DL 156/2005 e alterações).
13. **Duração anunciada pelos fabricantes** de sistemas de preservação (Coravin e similares).
14. **Política de devoluções e créditos da Emporio Italia** para vinho com defeito e para garrafas não
    abertas em eventos.
15. **Menções exatas de rótulo** de alguns vinhos dos modelos: Soave Villa Borghetti (Classico?),
    Lambrusco Otello e G. Verdi (IGT ou DOC), tipo de tampa "Tappo in metallo" da Masciarelli, e
    disponibilidade em 2026 dos vinhos marcados †.

---

## 23. Fontes

**Como foram lidas.** A legislação foi lida no texto integral através das cópias públicas
`legalize-pt` (Diário da República) e `legalize-eu` (EUR-Lex), que reproduzem o texto oficial e indicam o
ELI ou o URL de origem; as ligações abaixo são as oficiais. Os dados dos produtores vêm das fichas
oficiais, lidas através de resultados de pesquisa guardados na sessão de investigação.

### Legislação portuguesa

1. Decreto-Lei n.º 10/2015, de 16 de janeiro — Regime Jurídico de Acesso e Exercício de Atividades de
   Comércio, Serviços e Restauração (RJACSR), anexo, arts. 26.º (informação em português), 27.º (livro
   de reclamações), 134.º (informações a afixar) e 135.º (lista de preços, couvert, braille). Versão
   consolidada de 24/03/2023: https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2015-73045620 ;
   ELI: https://data.dre.pt/eli/dec-lei/10/2015/p/cons/20230324/pt/html
2. Decreto-Lei n.º 138/90, de 26 de abril — indicação de preços; arts. 1.º (n.os 1, 2, 3, 6 e 7),
   2.º, 3.º, 4.º e 10.º. Versão consolidada de 10/12/2021:
   https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1990-137618153
3. Decreto-Lei n.º 50/2013, de 16 de abril — disponibilização, venda e consumo de bebidas alcoólicas;
   arts. 3.º, 4.º e regime contraordenacional. Versão consolidada de 29/01/2021:
   https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2013-58361867
4. Decreto-Lei n.º 106/2015, de 16 de junho — alteração ao DL 50/2013 (proibição para todos os menores):
   https://diariodarepublica.pt/dr/detalhe/decreto-lei/106-2015-67498687
5. Código Civil, art. 122.º e seguintes (maioridade aos 18 anos), redação do Decreto-Lei n.º 496/77:
   https://diariodarepublica.pt/dr/detalhe/decreto-lei/496-1977-300030
6. Lei n.º 7-A/2016, de 30 de março (Orçamento do Estado para 2016), arts. 145.º (nova redação das verbas
   1.8, 3 e 3.1 da Lista II do CIVA, com a regra de repartição do valor tributável) e 146.º (efeitos a
   1/7/2016): https://diariodarepublica.pt/dr/detalhe/lei/7-a-2016-73958532
7. Lei n.º 64-B/2011, de 30 de dezembro (Orçamento do Estado para 2012), art. 123.º, n.º 3 (revogação
   das verbas 1.3 a 1.9, 2.4, 3 e 3.1 da Lista II; a verba 1.10 não consta):
   https://diariodarepublica.pt/dr/detalhe/lei/64-b-2011-243769
8. Lei n.º 109-B/2001, de 27 de dezembro (Orçamento do Estado para 2002), art. 35.º, n.º 4 — nova redação
   da Lista II do CIVA, incluindo a verba 1.10 "Vinhos comuns":
   https://diariodarepublica.pt/dr/detalhe/lei/109-b-2001-229157
9. Lei n.º 12-A/2010, de 30 de junho — art. 18.º do CIVA: taxas de 6 % (Lista I) e 13 % (Lista II):
   https://diariodarepublica.pt/dr/detalhe/lei/12-a-2010-292110
10. Lei n.º 55-A/2010, de 31 de dezembro (Orçamento do Estado para 2011) — art. 18.º, n.º 1, alínea c),
    do CIVA: taxa normal de 23 %: https://diariodarepublica.pt/dr/detalhe/lei/55-a-2010-344942
11. Decreto-Lei n.º 347/85, de 23 de agosto — taxas de IVA nas Regiões Autónomas (versão consultada de
    2015): https://diariodarepublica.pt/dr/detalhe/decreto-lei/347-1985-181004
12. Código dos Impostos Especiais de Consumo (Decreto-Lei n.º 73/2010), arts. 72.º (vinho: taxa de 0 €)
    e 74.º (produtos intermédios: 87,92 €/hl). Versão consolidada de 15/04/2026:
    https://data.dre.pt/eli/dec-lei/73/2010/p/cons/20260415/pt/html ;
    https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2010-34478675
13. Decreto-Lei n.º 26/2016, de 9 de junho — execução do Regulamento (UE) 1169/2011; arts. 2.º
    (DGAV/ASAE) e 4.º (restauração coletiva: denominação e alergénios). Versão consolidada de
    29/01/2021: https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2016-211341602
14. Entendimento da AT sobre o conceito de "vinhos comuns" (verba 1.10 da Lista II), divulgado em
    taxfile.pt: http://www.taxfile.pt/file_bank/news4514_8_1.pdf ; ver também LexPoint, "Transmissão de
    vinhos de produção agrícola própria":
    https://www.lexpoint.pt/Default.aspx?PageId=128&ContentId=58274 (lidos só através de resumo de
    pesquisa; texto integral por confirmar).
15. Cópia de texto integral usada para ler a legislação portuguesa: https://github.com/legalize-dev/legalize-pt

### Legislação europeia

16. Cópia de texto integral usada para ler a legislação europeia: https://github.com/legalize-dev/legalize-eu
17. Regulamento (UE) n.º 1169/2011 — informação aos consumidores sobre géneros alimentícios; art. 2.º,
    n.º 2, alínea d) (restauração coletiva), art. 44.º (não pré-embalados) e anexo II, ponto 12
    (sulfitos > 10 mg/kg ou 10 mg/l de SO₂ total): http://data.europa.eu/eli/reg/2011/1169/oj
18. Regulamento (UE) n.º 1308/2013 — OCM; anexo VII, parte II (vinho espumante ≥ 3 bar e cuvée ≥ 8,5 %
    vol.; espumante de qualidade ≥ 3,5 bar e cuvée ≥ 9 % vol.; espumante de qualidade aromático ≥ 3 bar,
    ≥ 6 % vol. adquirido e ≥ 10 % vol. total; vinho frisante 1-2,5 bar e ≥ 7 % vol. adquirido; a 20 °C):
    http://data.europa.eu/eli/reg/2013/1308/oj
19. Regulamento Delegado (UE) 2019/934 — práticas enológicas; anexo I, parte B (SO₂ total máximo),
    parte C (acidez volátil máxima e derrogações) e equivalência 0,12 g/l = 2 meq de ácido acético:
    http://data.europa.eu/eli/reg_del/2019/934/oj
20. Regulamento Delegado (UE) 2019/33 — rotulagem do vinho; anexo I (termos para sulfitos, ovo e leite em
    cada língua) e anexo III, partes A (açúcar dos espumantes) e B (açúcar dos outros vinhos):
    http://data.europa.eu/eli/reg_del/2019/33/oj
21. Regulamento (UE) 2021/2117 — art. 1.º, ponto 32 (art. 119.º do Reg. 1308/2013: declaração nutricional
    e lista de ingredientes; energia no rótulo; restante por meio eletrónico; alergénios no rótulo com
    "contém") e art. 6.º (aplicação a partir de 8/12/2023): http://data.europa.eu/eli/reg/2021/2117/oj
22. Regulamento de Execução (UE) 2021/1165 — produção biológica; anexo V (SO₂ máximo no vinho
    biológico): http://data.europa.eu/eli/reg_impl/2021/1165/oj
23. Regulamento (UE) n.º 251/2014 — definição, rotulagem e indicações geográficas dos produtos
    vitivinícolas aromatizados: http://data.europa.eu/eli/reg/2014/251/oj

### Produtores e crítica

24. Donnafugata — Tancredi Dolce&Gabbana, Terre Siciliane IGT (servir a 18 °C):
    https://www.donnafugata.it/en/product/tancredi-dolcegabbana-e-donnafugata/
25. Donnafugata — Anthìlia, Sicilia DOC Bianco (9-11 °C; copo de tamanho e altura médios; entradas, peixe
    cru e frito, queijos frescos): https://www.donnafugata.it/en/product/anthilia/
26. Donnafugata — Chiarandà 2021, Contessa Entellina DOC Chardonnay (11-13 °C; copo grande e
    relativamente alto; abrir 30 min antes): https://www.donnafugata.it/gbr/en/product/chiaranda/2021/
27. Donnafugata — Sherazade, Sicilia DOC Nero d'Avola (15-16 °C, ligeiramente fresco; sopas de peixe,
    pizza, esparguete com tomate): https://www.donnafugata.it/en/product/sherazade/ ; ficha 2024:
    https://www.donnafugata.it/wp-content/uploads/2026/06/Sherazade-2024_EN.pdf
28. Donnafugata — Sedàra, Sicilia DOC Rosso (16-18 °C; copo médio):
    https://www.donnafugata.it/en/product/sedara/
29. Donnafugata — Mille e una Notte, Sicilia DOC Rosso (18 °C; copo grande e bojudo: abrir minutos antes;
    senão, cerca de duas horas antes): https://www.donnafugata.it/en/product/mille-e-una-notte/
30. Masciarelli — Gianni Masciarelli Montepulciano d'Abruzzo DOC (16-18 °C):
    https://www.masciarelli.it/en/i-vini/gianni-masciarelli-montepulciano-dabruzzo-doc/
31. Masciarelli — Gianni Masciarelli Cerasuolo d'Abruzzo DOC (10-12 °C; peixe frito, massa fresca,
    legumes, pizza): https://www.masciarelli.it/en/i-vini/gianni-masciarelli-cerasuolo-dabruzzo-doc/ ;
    ficha técnica: https://www.masciarelli.it/wp-content/uploads/2019/05/GM-Cerasuolo_eng.pdf
32. The Wine Society — Taurasi, Feudi di San Gregorio 2019 (encorpado, taninos firmes, acidez viva;
    decantar com antecedência, até 12 horas):
    https://www.thewinesociety.com/product/taurasi-feudi-di-san-gregorio-2019/

### Dados internos

- Catálogo Emporio Italia (`data/catalogo.json`; exportação Odoo de 20/02/2026 e lista trade do
  2.º semestre de 2024): nomes dos vinhos, denominações, formatos grandes e versões com tampa metálica.
  Sem preços nem stock neste ficheiro.
