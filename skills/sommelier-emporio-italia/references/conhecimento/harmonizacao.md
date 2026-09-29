# Harmonização de vinhos italianos com comida

Referência da skill **Sommelier Emporio Italia** para a equipa comercial e de catering. Junta os
princípios de harmonização, os clássicos regionais italianos, uma matriz por ingrediente e molho
(trufa, porcini, tomate, pesto, ragù, massas romanas, marisco, peixe cru, risotto, pizza, salumi,
queijos, sobremesas), a cozinha portuguesa com vinhos italianos, os formatos de catering e a
harmonização prato a prato do menu Emporio Italia Catering.

> **Como ler este ficheiro (revisão independente de 29/09/2026). Ler antes de usar.**
>
> - **[n]** remete para a secção [Fontes](#15-fontes). São factos com fonte: textos legais da UE relidos
>   nesta revisão nas versões consolidadas guardadas localmente (EUR-Lex), a lista oficial MASAF dos vinhos
>   DOP, os números de processo do registo eAmbrosia (queijos, salumi e outros produtos DOP/IGP) e fichas de
>   produtores conferidas nos resultados de pesquisa guardados nesta sessão de trabalho.
> - **(não verificado)** marca números, regras e datas de conhecimento corrente que **não** foi possível
>   confirmar com fonte. Durante a revisão, a quota de pesquisa web estava esgotada e o acesso direto a
>   sites (consorzi, MASAF, eAmbrosia, EUR-Lex online, Decanter, Wine Folly, etc.) estava bloqueado pela rede
>   do ambiente. Não usar esses valores em material para clientes sem confirmar primeiro (ver
>   [secção 14](#14-lacunas-e-onde-confirmar)).
> - **Harmonizações, sequências de serviço e argumentos de venda são juízo profissional de sommelier**,
>   não factos. Servem para vender e servir bem, não para citar como regra. Os títulos de secção
>   assinalam "(prática profissional)" quando todo o conteúdo é desse tipo.
> - **Vinhos do catálogo** vêm de `data/catalogo.json` (exportação Odoo de 20/02/2026 e lista trade do
>   2.º semestre de 2024). Sinais: **‡** = confirmar disponibilidade antes de propor (estado
>   "não confirmado 2026" ou sem disponibilidade na última exportação); **\*** = consta das exportações
>   Odoo mas ainda não tem ficha no catálogo da skill (Bellavista, Ferrari, Conti d'Arco, Antinori,
>   Cantina Orsogna, Joseph/Hofstätter). Confirma sempre com `scripts/procurar_vinhos.py`.
> - Este ficheiro **não** contém preços, custos, margens nem stock.
> - Coerência: as tabelas regionais resumem e harmonizam o que está em `regioes-norte.md`,
>   `regioes-centro.md` e `regioes-sul-ilhas.md`; as bolhas e os doces estão desenvolvidos em
>   `espumantes-doces-fortificados.md`; temperaturas e quantidades em `servico-e-carta-de-vinhos.md`;
>   cocktails e digestivos em `aperitivos-digestivos-destilados.md`.

## Índice

1. [Resumo em 60 segundos](#1-resumo-em-60-segundos)
2. [Método de trabalho: como pensar uma harmonização](#2-método-de-trabalho-como-pensar-uma-harmonização)
3. [Princípios](#3-princípios)
   - 3.1 Peso e intensidade · 3.2 Acidez · 3.3 Tanino, proteína e gordura · 3.4 Sal · 3.5 Doçura ·
     3.6 Umami · 3.7 Picante · 3.8 Amargo · 3.9 Textura · 3.10 Aroma · 3.11 Álcool · 3.12 Madeira ·
     3.13 Idade do vinho · 3.14 Semelhança e contraste · 3.15 Regionalidade · 3.16 Quadro de interações
4. [Estilos de vinho italiano e a sua função à mesa](#4-estilos-de-vinho-italiano-e-a-sua-função-à-mesa)
5. [Clássicos regionais italianos, prato a prato](#5-clássicos-regionais-italianos-prato-a-prato)
6. [Matriz por ingrediente e molho](#6-matriz-por-ingrediente-e-molho)
   - 6.1 Trufa · 6.2 Porcini e cogumelos · 6.3 Tomate · 6.4 Pesto · 6.5 Ragù · 6.6 Carbonara ·
     6.7 Cacio e pepe · 6.8 Amatriciana e gricia · 6.9 Frutos do mar · 6.10 Peixe cru · 6.11 Risotto ·
     6.12 Pizza · 6.13 Salumi · 6.14 Queijos italianos · 6.15 Sobremesas · 6.16 Legumes difíceis ·
     6.17 Métodos de confeção
7. [Cozinha portuguesa com vinhos italianos](#7-cozinha-portuguesa-com-vinhos-italianos)
8. [Formatos de catering e sequência de vinhos](#8-formatos-de-catering-e-sequência-de-vinhos)
9. [Menu de catering Emporio: harmonização prato a prato](#9-menu-de-catering-emporio-harmonização-prato-a-prato)
10. [Vegetariano e vegano](#10-vegetariano-e-vegano)
11. [Picante, cozinhas asiáticas e fusão](#11-picante-cozinhas-asiáticas-e-fusão)
12. [Erros comuns](#12-erros-comuns)
13. [Guia rápido para a equipa de sala](#13-guia-rápido-para-a-equipa-de-sala)
14. [Lacunas e onde confirmar](#14-lacunas-e-onde-confirmar)
15. [Fontes](#15-fontes)

---

## 1. Resumo em 60 segundos

(prática profissional)

1. **Harmoniza com o que manda no prato, não só com a proteína.** O molho, a gordura, o sal, a
   acidez, a doçura e o picante pesam mais do que "peixe" ou "carne". Um polvo à lagareiro e um polvo
   alla luciana (com tomate) pedem vinhos diferentes.
2. **Peso com peso, intensidade com intensidade.** Prato delicado, vinho delicado; prato rico, vinho
   com corpo. É a regra que mais erros evita.
3. **A acidez do vinho tem de acompanhar a do prato.** Tomate, limão, vinagre e alcaparras "apagam"
   vinhos de pouca acidez. É por isso que Sangiovese, Barbera e os brancos italianos funcionam tão bem à
   mesa.
4. **Gordura e sal pedem acidez e bolha.** Salumi, queijos, fritos e natas: Lambrusco secco,
   Franciacorta, Trento DOC, Prosecco Brut, brancos vivos.
5. **Proteína e gordura domam o tanino.** Barolo, Brunello, Taurasi e Sagrantino precisam de carne,
   queijo curado ou molhos ricos. Com pratos magros ou delicados, o tanino fica áspero.
6. **O vinho tem de ser pelo menos tão doce como a sobremesa.** Um Brut com bolo fica ácido e
   amargo. Moscato d'Asti, Asti, Brachetto, passiti e Vin Santo para o doce.
7. **Picante: pouco álcool, pouco tanino, fruta e, se possível, algum açúcar.** O álcool e o tanino
   aumentam a sensação de ardor. Nunca Amarone nem Barolo com caril picante.
8. **Umami endurece o tanino e o amargor.** Parmigiano muito curado, cogumelos, tomate seco, anchova,
   molho de soja: tintos de tanino fino, brancos com estrutura ou espumante com estágio.
9. **Amargo com amargo soma.** Alcachofra, radicchio, rúcula, beringela grelhada: vinhos frutados,
   sem madeira, pouco tânicos.
10. **Peixe e tanino alto dão sabor metálico.** Se o cliente quer tinto com peixe, escolhe tinto leve
    e fresco (Etna Rosso, Frappato, Piedirosso, Pinot Nero, Lambrusco) e serve-o fresco.
11. **Regionalidade é o primeiro atalho**: Lambrusco com Prosciutto di Parma, Nebbiolo com trufa,
    Vermentino com pesto, Montepulciano com arrosticini, Vin Santo com cantucci. Confirma depois com as
    regras 1 a 10.
12. **Na dúvida, espumante seco de metodo classico.** Um Franciacorta ou Trento DOC Brut ou Extra Brut é
    o trunfo mais versátil da carta: aperitivo, fritos, marisco, salumi, queijos, cozinha asiática.

---

## 2. Método de trabalho: como pensar uma harmonização

(prática profissional)

### 2.1 Os cinco passos

| Passo | Pergunta | Exemplo (Raviolo Amatriciano con Tartufo Nero) |
|---|---|---|
| 1. Decompor o prato | Qual é a base, o molho, a gordura, o tempero, o acompanhamento, a técnica? | Massa fresca com ovo, recheio de guanciale e pecorino, molho de tomate, trufa negra |
| 2. Encontrar o elemento dominante | O que se sente mais: sal, gordura, acidez, doce, amargo, picante, umami, aroma? | Acidez do tomate, gordura e sal do guanciale, umami do pecorino, aroma terroso da trufa |
| 3. Medir peso e intensidade | Leve, médio ou rico? Aroma discreto ou potente? | Médio a rico, aroma intenso |
| 4. Escolher o estilo | Qual estilo responde ao dominante? (ver [secção 4](#4-estilos-de-vinho-italiano-e-a-sua-função-à-mesa)) | Tinto de acidez alta e tanino médio, com fruta e algum carácter terroso |
| 5. Escolher o vinho do catálogo | Que vinho do catálogo tem esse perfil, a que patamar, com disponibilidade? | Montepulciano d'Abruzzo (Masciarelli), Chianti Classico (Cecchi), Barbera d'Alba Superiore (Fontanafredda Papagena), Etna Rosso (Donnafugata Sul Vulcano) |

### 2.2 Perguntas a fazer ao cliente (restaurante ou evento)

- Qual é o prato ou o menu, com a receita real (molho, guarnição, picante)? Pede a ficha técnica ao
  chefe quando for uma carta.
- Qual é a ocasião, quantas pessoas e que perfil de público (conhecedor, curioso, conservador)?
- Há preferência de cor ou de estilo ("só tinto", "nada doce", "sem bolhas")?
- Um vinho para toda a refeição ou um vinho por prato?
- Que patamar de preço e que vinhos da Emporio o cliente já compra?

### 2.3 Quando o cliente quer um só vinho para tudo

Escolhe o vinho que falha menos com o prato mais difícil. Por ordem de versatilidade (juízo):

1. **Espumante metodo classico Brut ou Extra Brut** (Franciacorta, Trento DOC, Alta Langa): vai do
   aperitivo à carne branca.
2. **Rosato com corpo** (Cerasuolo d'Abruzzo, Etna Rosato, rosados do Salento): peixe gordo, tomate,
   salumi, carnes brancas, cozinha picante suave.
3. **Tinto leve e ácido de tanino baixo** (Etna Rosso, Valpolicella Classico, Lacryma Christi Rosso,
   Pinot Nero): peixe com molho, pizza, massas com tomate, aves.
4. **Branco mediterrânico com estrutura** (Fiano, Greco di Tufo, Vermentino, Grillo): marisco,
   massas, carnes brancas, queijos frescos.
5. **Sangiovese ou Barbera jovem**: a escolha de "tinto para tudo" num restaurante italiano de massas e
   pizza.

---

## 3. Princípios

(prática profissional, exceto onde há fonte)

### 3.1 Peso e intensidade

- **Peso (corpo)** é a sensação de volume na boca: vem do álcool, do extrato, da glicerina, do açúcar e
  da textura. **Intensidade** é a força do sabor e do aroma. Um vinho pode ser leve e intenso (Moscato
  d'Asti, Sauvignon) ou encorpado e discreto (Chardonnay com madeira, Soave de guarda).
- **Regra:** iguala o peso do prato ao peso do vinho e, depois, a intensidade de sabor. A escala
  `corpo` de 1 a 5 do catálogo (`procurar_vinhos.py --formato json`) serve para isto.
- **Escala prática (catálogo Emporio):**
  - Corpo 1-2: Prosecco, Lambrusco, Pinot Grigio, Soave, Trebbiano, Valpolicella Classico, Lacryma
    Christi Rosso, Sherazade.
  - Corpo 3: Falanghina, Greco di Tufo, Vermentino, Grillo, Lugana, Arneis, Chianti, Barbera d'Alba,
    Langhe Nebbiolo, Etna Rosso, Montepulciano d'Abruzzo, Cerasuolo d'Abruzzo.
  - Corpo 4: Fiano Riserva (Pietracalda), Chardonnay com madeira (Chiarandà, Pomino Benefizio),
    Chianti Classico Riserva, Brunello, Barolo, Taurasi, Primitivo, Palazzo della Torre.
  - Corpo 5: Amarone, Sagrantino, Tancredi, grandes Super Toscanos.
- **Erro típico:** Amarone com um peixe grelhado (o vinho esmaga) ou Pinot Grigio leve com um estufado
  de javali (o vinho desaparece).

### 3.2 Acidez

- Um prato ácido (tomate, citrinos, vinagre, iogurte, alcaparras, vinho no molho) **faz o vinho parecer
  menos ácido, mais redondo e mais frutado**. Se o vinho tiver pouca acidez, fica chato e mole.
- Um vinho de acidez alta **corta a gordura** e "limpa" a boca entre garfadas.
- Itália é o país dos vinhos de acidez alta à mesa: Sangiovese, Barbera, Nebbiolo, Aglianico, Verdicchio,
  Greco, Carricante, Glera, Lambrusco. É um argumento comercial: "vinhos feitos para comer".
- **Casos práticos:** tomate cru ou pouco cozinhado (bruschetta, caprese, marinara) pede branco vivo,
  rosato ou tinto muito fresco. Molhos com limão ou vinho branco (piccata, vongole) pedem branco de acidez
  alta. Agridoce (caponata, sarde in saor) pede acidez e fruta, nunca tanino.

### 3.3 Tanino, proteína e gordura

- O tanino dá secura e aspereza (adstringência). **Proteína e gordura suavizam essa sensação**: é por
  isso que um Barolo jovem, duro sozinho, fica macio com um brasato ou com Parmigiano.
- **Tanino alto + prato magro ou delicado = aspereza.** Peito de frango, peixe branco, vitela magra ou
  legumes não chegam para um Sagrantino.
- **Tanino alto + peixe oleoso (sardinha, cavala, atum) = sabor metálico ou amargo.** Com peixe, o
  tinto tem de ter tanino baixo (regra prática corrente; o mecanismo exato não foi verificado).
- **Tanino + ovo** (carbonara, gema, frittata) tende a ficar metálico: prefere brancos com estrutura,
  rosati ou tintos leves.
- **Tanino + sal** funciona: o sal diminui a sensação de amargor e adstringência (ver 3.4).
- **Escala de tanino dos tintos do catálogo (juízo):**
  - Baixo: Lambrusco, Valpolicella Classico, Lacryma Christi Rosso (Piedirosso dominante), Sherazade, Red Angel
    (Pinot Nero), Etna Rosso.
  - Médio: Chianti, Barbera, Montepulciano d'Abruzzo, Langhe Nebbiolo jovem de estilo fácil, Nero d'Avola
    com madeira, Primitivo, Merlot, Palazzo della Torre.
  - Alto: Barolo, Brunello, Chianti Classico Riserva, Taurasi, Teodosio (Aglianico del Vulture),
    Montefalco Sagrantino, Amarone (tanino alto mas envolvido pela fruta e pelo álcool).

### 3.4 Sal

- O sal **aumenta a sensação de corpo** do vinho e **diminui o amargor, a adstringência e a perceção
  da acidez**. É o ingrediente mais amigo do vinho.
- Pratos salgados (salumi, Parmigiano, Pecorino Romano, anchova, bottarga, azeitonas, bacalhau mal
  demolhado) pedem **acidez e bolha** para refrescar, ou **doçura** em contraste (Gorgonzola com
  passito, Parmigiano com Lambrusco amabile e aceto balsamico).
- O sal permite tintos mais tânicos do que o peso do prato sugeriria: Pecorino curado com Sagrantino,
  Parmigiano 30 meses com Barolo.

### 3.5 Doçura

- **Regra de ouro: o vinho deve ser tão doce ou mais doce do que o prato.** A doçura do prato faz o
  vinho parecer mais ácido, mais amargo, mais adstringente e mais alcoólico, e menos frutado.
- **Uma pitada de doce no prato** (cebola caramelizada, abóbora, molhos agridoces, presunto com melão,
  cozinha asiática com açúcar) aceita um vinho com açúcar residual ligeiro: Prosecco **Extra Dry**,
  Lambrusco amabile, Gewürztraminer, Primitivo maduro.
- **A doçura no rótulo é regulada pela UE** e muda de escala entre espumantes e vinhos tranquilos ou
  frisantes **[1]**:

| Espumantes (Reg. Delegado (UE) 2019/33, Anexo III, Parte A) | Açúcar | Vinhos tranquilos e frisantes (Parte B) | Açúcar |
|---|---|---|---|
| Brut Nature / Pas Dosé / Dosaggio Zero | menos de 3 g/l, sem açúcar adicionado depois da segunda fermentação | *Secco* / seco | até 4 g/l, ou até 9 g/l se a acidez total (em ácido tartárico) não for mais de 2 g/l inferior ao açúcar |
| Extra Brut | 0 a 6 g/l | *Abboccato* / meio seco | acima do seco e até 12 g/l, ou até 18 g/l se a acidez total não for mais de 10 g/l inferior ao açúcar |
| Brut | menos de 12 g/l | *Amabile* / meio doce | acima do meio seco e até 45 g/l |
| **Extra Dry** | **12 a 17 g/l** | *Dolce* / doce | pelo menos 45 g/l |
| Dry / Secco / Asciutto | 17 a 32 g/l | | |
| Demi-Sec / Abboccato | 32 a 50 g/l | | |
| Dolce / Doux | mais de 50 g/l | | |

- **Consequências práticas:**
  - **Extra Dry é mais doce do que Brut** (12 a 17 g/l contra menos de 12 g/l) **[1]**. Os Prosecco
    Bolla do catálogo são Extra Dry segundo o Odoo (no Millesimato, a loja online indica Brut: confirmar a
    dosagem antes de propor). Para marisco cru, ostras e peixe grelhado, prefere um Brut ou Extra
    Brut (Carpenè Malvolti 1868 Extra Brut, Berlucchi '61 Extra Brut); para presunto com melão, cozinha
    asiática ou um toque agridoce, o Extra Dry é melhor.
  - **"Dry" num espumante é meio doce**, mas "secco" num Lambrusco frisante é seco: são escalas
    diferentes **[1]**.
  - **Lambrusco amabile** frisante segue a escala dos vinhos tranquilos e frisantes (acima do limite do
    meio seco e até 45 g/l) **[1]**; um Lambrusco *spumante* segue a escala dos espumantes. É um vinho de
    contraste para pratos salgados e picantes, e de semelhança para sobremesas de frutos vermelhos.
  - **Alguns tintos secos têm açúcar percetível:** o disciplinare do Primitivo di Manduria DOC admite
    até 18 g/l de açúcar residual **[18]**, o que explica a sensação macia e ajuda com pratos
    ligeiramente picantes ou com molho barbecue.

### 3.6 Umami

- Umami é o sabor "de caldo" do glutamato e de nucleótidos: Parmigiano e Grana muito curados, tomate
  maduro e seco, cogumelos (sobretudo secos), anchova e colatura, bottarga, carnes curadas, molho de
  soja, miso, algas, marisco.
- Efeito no vinho (juízo, coerente com o modelo de ensino WSET; não verificado nesta revisão): o umami,
  como a doçura, **acentua o amargor, a adstringência, a acidez e o calor do álcool** e **reduz a fruta e
  o corpo**. Um tinto jovem e tânico com cogumelos secos e Parmigiano 36 meses pode ficar duro.
- **Como compensar:** sal e um toque ácido no prato (é o que o chefe faz com limão ou vinagre);
  do lado do vinho, fruta madura, tanino fino, estágio em garrafa, bolha com longo estágio (Franciacorta
  millesimato, Riserva), ou brancos com textura.
- **Pares italianos de umami (juízo):** Parmigiano 30-36 meses com Amarone, Barolo evoluído ou
  Franciacorta Riserva; risotto ai porcini com Nebbiolo ou Chardonnay com madeira; pizza com anchova
  com Vermentino ou Greco; bottarga com Vermentino ou Carricante.

### 3.7 Picante (malagueta, peperoncino, 'nduja, piri-piri)

- O picante **aumenta a sensação de álcool, de amargor, de acidez e de adstringência** e **reduz a
  fruta e a doçura** (juízo; não verificado nesta revisão).
- **Faz:** baixo teor alcoólico, tanino baixo, muita fruta, alguma doçura (Extra Dry, amabile,
  Moscato), bolha, temperatura fresca. Exemplos: Lambrusco amabile ou secco, Prosecco Extra Dry,
  rosati, Gewürztraminer ou Müller-Thurgau do Alto Adige, Moscato d'Asti com picante forte e doce.
- **Evita:** Amarone, Primitivo muito alcoólico servido quente, Barolo, Sagrantino, brancos com muita
  madeira.
- Desenvolvido na [secção 11](#11-picante-cozinhas-asiáticas-e-fusão).

### 3.8 Amargo

- O amargor do prato **soma-se** ao amargor e à adstringência do vinho.
- Pratos amargos italianos: radicchio (Treviso, Chioggia), puntarelle, cime di rapa, friarielli, rúcula,
  alcachofra, chicória, beringela grelhada, carvão da brasa, café e cacau nas sobremesas.
- **Faz:** vinhos com fruta e sem madeira nova: Valpolicella, Bardolino, rosati, Lambrusco,
  Piedirosso; brancos frutados (Falanghina, Soave). O amargo fino de alguns brancos italianos (Greco,
  Verdicchio, Vermentino, Garganega) acompanha bem legumes ligeiramente amargos.
- **Evita:** tintos tânicos e madeira tostada com radicchio ou alcachofra.

### 3.9 Textura

- **Bolha e acidez** raspam a gordura e o amido: frito, panado, massa com manteiga, queijo derretido,
  batata frita. Franciacorta, Trento, Prosecco Brut e Lambrusco são os "detergentes" da mesa.
- **Cremoso com cremoso** (semelhança): burrata, risotto mantecato, molhos de natas, bacalhau com natas
  com Franciacorta **Satèn** (só uvas brancas, só Brut e menos de 5 atmosferas de pressão: bolha
  cremosa **[16]**), Fiano, Lugana, Chardonnay com estágio em madeira bem integrada.
- **Crocante e salgado** (taralli, grissini, supplì, fritto misto): espumante seco.
- **Gelatinoso e untuoso** (cabeça de porco, bollito, polvo, pele de leitão): acidez alta e bolha, ou
  tinto de acidez viva.

### 3.10 Aroma: pontes aromáticas

- Procurar um aroma comum entre prato e vinho reforça a ligação (semelhança):
  - **Terra, cogumelo, sub-bosque:** Nebbiolo evoluído, Pinot Nero, Nerello Mascalese com trufa e
    porcini.
  - **Ervas mediterrânicas:** Vermentino, Grillo e Pecorino com pesto, alecrim, orégão, tomilho.
  - **Frutos secos:** Fiano, Chardonnay com estágio, Vin Santo e Marsala com pistácio, amêndoa, avelã.
  - **Fruta vermelha:** Brachetto, Lambrusco, rosati com frutos do bosque, tomate maduro, pimento
    assado.
  - **Fumo e especiaria:** Syrah, Aglianico, Lagrein, Gewürztraminer com speck, fumados, pimenta.
  - **Pão e brioche:** metodo classico com longo estágio sobre as borras com massa folhada, pão,
    Parmigiano.
- Os produtores também usam esta lógica. Exemplo: a Donnafugata recomenda o Chiarandà (Chardonnay de
  Contessa Entellina, com estágio em madeira) com lagosta, sopa cremosa de legumes, peixe fumado e codorniz
  assada **[8]**.

### 3.11 Álcool

- Álcool alto dá corpo e calor. Com picante, **amplifica o ardor**; com pratos delicados, esmaga.
- Pratos ricos e de cozedura longa (brasato, estufados, caça) aguentam álcool alto: Amarone,
  Primitivo, Sagrantino, Tancredi.
- **Temperatura de serviço** muda tudo: um tinto a 22 °C numa esplanada de verão parece mais alcoólico e
  destrói a harmonização. Orientação da skill: tintos leves a 13-15 °C, médios a 15-17 °C e estruturados
  a 16-18 °C (prática profissional; tabela completa em `servico-e-carta-de-vinhos.md`).
- **O que indicam alguns produtores do catálogo** (confirma a lógica "tinto leve, servido mais fresco"):

| Vinho | Estilo | Temperatura indicada pelo produtor |
|---|---|---|
| Donnafugata Sherazade (Nero d'Avola, sem madeira) | Tinto leve e frutado | 15-16 °C, "ligeiramente fresco" **[7]** |
| Donnafugata Sedàra (Nero d'Avola com Syrah e Merlot) | Tinto médio | 16-18 °C **[9]** |
| Donnafugata Mille e una Notte (lote com estágio em barrica) | Tinto estruturado | 18 °C **[10]** |
| Donnafugata Chiarandà (Chardonnay com estágio) | Branco estruturado | 11-13 °C **[8]** |
| Donnafugata Anthìlia (Lucido/Catarratto dominante) | Branco fresco | 9-11 °C **[5]** |
| Donnafugata SurSur (Grillo) | Branco fresco | 9-11 °C **[6]** |
| Gianni Masciarelli Cerasuolo d'Abruzzo | Rosato com corpo | 10-12 °C **[12]** |

### 3.12 Madeira

- Madeira nova (barrica) acrescenta baunilha, tosta, especiaria e tanino.
- **Gosta de:** grelhados, fumados, tostados, assados, manteiga, natas, cogumelos salteados, carnes
  vermelhas.
- **Não gosta de:** peixe cru, marisco delicado, alcachofra e legumes verdes, picante, tomate cru,
  queijos frescos.
- Brancos com madeira do catálogo: Donnafugata Chiarandà, Frescobaldi Pomino Benefizio Riserva,
  Antinori Cervaro della Sala\*. Brancos sem madeira para peixe e marisco: Greco di Tufo, Falanghina,
  Vermentino, Etna Bianco, Grillo (SurSur), Gavi, Arneis, Lugana (confirmar o estágio na ficha de
  cada vinho).

### 3.13 Idade do vinho

- Vinhos jovens: fruta, acidez viva, tanino firme. Pedem pratos com sabor direto e gordura.
- Vinhos evoluídos (aromas terciários: couro, trufa, cogumelo, folha seca, especiaria): pedem pratos
  **complexos mas não agressivos**: trufa, cogumelos, carnes estufadas, aves de caça, queijos curados.
  Evita tomate muito ácido, picante e molhos doces, que apagam a finura.
- Um Barolo de 15 anos com tajarin al tartufo bianco é uma harmonização de "semelhança aromática"; o
  mesmo Barolo com uma pizza diavola é um desperdício.

### 3.14 Semelhança e contraste

| Estratégia | O que é | Exemplos italianos (juízo) |
|---|---|---|
| **Semelhança (congruente)** | Vinho e prato partilham peso, textura ou aroma | Burrata com Fiano; risotto alla milanese com Franciacorta Satèn; tajarin al tartufo com Barolo evoluído; pesto com Vermentino; Tiramisù all'Amaretto com Vin Santo (amêndoa) |
| **Contraste (complementar)** | O vinho equilibra um elemento dominante oposto | Gorgonzola piccante com Passito di Pantelleria (sal contra doce); fritto misto com Prosecco Brut (gordura contra acidez e bolha); Prosciutto di Parma com Lambrusco secco; 'nduja com Lambrusco amabile (picante contra doce e fruta) |
| **Ponte** | Um ingrediente do prato liga ao vinho | Vinho no molho (brasato al Barolo, risotto all'Amarone); pistácio com Grillo; frutos vermelhos com Brachetto |

- Não há uma estratégia "certa". Num menu de vários pratos, **alternar** semelhança e contraste dá
  ritmo. Num evento grande, prefere pares de semelhança (agradam a mais gente); o contraste doce-salgado
  surpreende conhecedores mas divide o público.

### 3.15 Regionalidade: "what grows together goes together"

- **O princípio:** cozinha e vinho de uma região evoluíram juntos. O Lambrusco nasce na terra do
  Prosciutto di Parma, do Parmigiano e da mortadella; o Nebbiolo na terra da trufa branca de Alba; o
  Vermentino na costa do pesto e do peixe. Os pares regionais são o atalho mais fácil de explicar ao
  cliente e a melhor história de sala.
- **Os limites (juízo):**
  - Muitos pares regionais são **culturais**, não técnicos. O Chianti com a bistecca funciona porque a
    carne é magra e grelhada com azeite; um Chianti ligeiro com um estufado muito rico pode não chegar.
  - A cozinha moderna (e o menu Emporio) mistura regiões: Cacio e Pepe **di Mare** é Roma com marisco.
    Aplica as regras antes da geografia.
  - Portugal não tem vinhos italianos "da região": usa a **analogia** (ver
    [secção 7](#7-cozinha-portuguesa-com-vinhos-italianos)): Lambrusco secco ou Franciacorta como o
    espumante da Bairrada com o leitão; Aglianico ou Nebbiolo onde se usaria Baga.

### 3.16 Quadro de interações: como o prato muda o vinho

Referência rápida para formação (juízo profissional, coerente com o modelo de ensino WSET; não
verificado nesta revisão).

| Elemento dominante no prato | O que faz ao vinho | Vinho que funciona | Vinho a evitar |
|---|---|---|---|
| Doçura | Mais ácido, amargo, adstringente e alcoólico; menos fruta e corpo | Igual ou mais doce: Moscato d'Asti, Asti, Brachetto, passito, Vin Santo, Extra Dry (doçura ligeira) | Brut, tintos secos tânicos |
| Umami | Mais amargo, adstringente, ácido e alcoólico; menos fruta | Fruta madura, tanino fino, estágio, bolha com borras longas | Tintos jovens muito tânicos, brancos neutros e leves |
| Acidez | Menos ácido, mais redondo, mais frutado | Acidez igual ou maior: Sangiovese, Barbera, Verdicchio, Greco, Vermentino, espumantes | Vinhos de acidez baixa e muito maduros |
| Sal | Mais corpo; menos amargor, adstringência e acidez | Quase todos; espumante e acidez para refrescar; doce em contraste | Poucos problemas |
| Gordura | Pede limpeza | Acidez e bolha; tanino com proteína | Brancos moles de acidez baixa |
| Amargo | Mais amargo | Fruta, sem madeira, pouco tanino | Tintos tânicos, madeira nova |
| Picante | Mais álcool, amargor, acidez e adstringência; menos fruta e doçura | Baixo álcool, pouco tanino, fruta, doçura ligeira, frio | Tintos alcoólicos e tânicos, madeira |
| Fumado / tostado | Liga à madeira e à especiaria | Tintos com estágio, Syrah, Aglianico, Lagrein, Pinot Nero | Brancos muito leves e aromáticos delicados |

---

## 4. Estilos de vinho italiano e a sua função à mesa

(prática profissional; os vinhos do catálogo são exemplos e devem ser confirmados com
`procurar_vinhos.py`)

| Estilo | Exemplos italianos | Função à mesa | Pratos-tipo | No catálogo Emporio (exemplos) |
|---|---|---|---|---|
| Espumante metodo classico Brut / Extra Brut / Pas Dosé | Franciacorta, Trento DOC, Alta Langa, Oltrepò Pavese Metodo Classico | O trunfo versátil; aperitivo; limpa gordura e sal | Fritos, marisco, crudo, salumi, queijos, leitão, cozinha asiática suave | Berlucchi '61 Extra Brut e '61 Nature; Fontanafredda Alta Langa; Bellavista Alma Gran Cuvée Brut e Non Dosato\*; Ferrari Brut\*; Conti d'Arco Trento Brut\* |
| Metodo classico Satèn / Blanc de Blancs | Franciacorta Satèn | Textura cremosa | Burrata, risotto, bacalhau com natas, massas com frutos secos | Berlucchi '61 Satèn e Cuvée Imperiale Satèn; Berlucchi '61 Nature Blanc de Blancs |
| Metodo classico Rosé / Pinot Nero dominante | Franciacorta Rosé, Trento Rosé | Ponte para atum, salmão, trufa, carnes brancas | Tártaro de atum, pato, cogumelos, presunto | Berlucchi '61 Rosé e '61 Nature Rosé; Palazzo Lana Extrême Riserva (Pinot Nero); Bellavista Alma Rosé\* |
| Prosecco Brut / Extra Brut | Conegliano Valdobbiadene, Prosecco DOC | Aperitivo leve, fresco, aromático | Focaccia, cicchetti, marisco cozido, fritos leves | Carpenè Malvolti 1868 Extra Brut e Brut (magnum); Carpenè Prosecco DOC Rosé Brut; Villa Sandi Il Fresco Brut‡ e La Rivetta 120‡ |
| Prosecco Extra Dry / Dry | idem | Doçura ligeira: acolhe agridoce, picante suave, presunto com melão | Sushi, cozinha asiática suave, aperitivos com doce | Bolla Prosecco DOC Extra Dry, Treviso Biologico, Rosé e Superiore Millesimato; Villa Sandi Valdobbiadene Extra Dry‡ |
| Lambrusco secco (tinto frisante) | Sorbara, Grasparossa, Salamino, Reggiano | Tinto com bolha e acidez; o par regional dos salumi | Prosciutto, mortadella, cotechino, pizza, leitão, cozido | Ceci Giuseppe Verdi Dry e Otello Nerodilambrusco 1813; Albinea Canali Ottocento Nero |
| Frisantes e espumantes doces e aromáticos | Lambrusco amabile, Moscato d'Asti, Asti, Brachetto d'Acqui | Contraste com sal e picante; sobremesas leves | Panettone, fruta, tiramisù com frutos vermelhos, cozinha picante | Ceci Giuseppe Verdi Amabile e Rosato Amabile; Fontanafredda Asti |
| Branco leve e neutro | Pinot Grigio, Soave, Trebbiano, Frascati | Fácil, fresco, sem arestas | Aperitivo, saladas, peixe simples, massas de legumes | Jermann e Corte Giara Pinot Grigio; Masciarelli Trebbiano d'Abruzzo; Pasqua Soave Classico‡ |
| Branco aromático | Gewürztraminer, Müller-Thurgau, Sauvignon, Moscato secco | Aromas intensos; aguenta especiarias | Cozinha asiática, caril suave, queijos de casca lavada, espargos (Sauvignon) | Jermann Sauvignon; Joseph Gewürztraminer\* e Müller Thurgau\* |
| Branco mineral e salino | Vermentino, Greco, Etna Bianco (Carricante), Verdicchio, Pecorino, Falanghina, Gavi | O "branco do mar": acidez, sal, amargo fino | Marisco, peixe grelhado, pesto, crudo, fritos, bacalhau | Feudi Greco di Tufo e Cutizzi, Falanghina e Serrocielo; Donnafugata Isolano; Valori Pecorino; Fontanafredda Gavi; Aragosta Vermentino‡; Sella&Mosca Cala Reala‡ |
| Branco estruturado e texturado | Fiano, Lugana, Friulano, Arneis, Chardonnay com estágio | Branco "de prato principal" | Polvo, bacalhau com natas, carnes brancas, risotto, queijos semi-curados | Feudi Fiano di Avellino e Pietracalda; Allegrini Lugana; Montezemolo Langhe Arneis; Jermann Vintage Tunina; Donnafugata Chiarandà; Pomino Benefizio |
| Rosato | Cerasuolo d'Abruzzo, Chiaretto, Etna Rosato, rosati do Salento | Entre branco e tinto: peixe gordo, tomate, salumi | Sardinhas, atum, pizza, arroz de marisco, cozinha picante suave | Gianni Masciarelli Cerasuolo d'Abruzzo; Donnafugata Rosa; Frescobaldi Alìe Rosé; Masciarelli Rosato |
| Tinto leve de tanino baixo | Etna Rosso, Frappato, Piedirosso, Valpolicella, Bardolino, Pinot Nero, Schiava | O tinto do peixe e da pizza; servir fresco | Atum, polvo, bacalhau assado, pizza, aves, salumi | Donnafugata Sul Vulcano; Feudi Lacryma Christi Rosso; Allegrini Valpolicella Classico; Jermann Red Angel; Donnafugata Sherazade |
| Tinto médio de acidez alta | Chianti, Chianti Classico, Rosso di Montalcino, Barbera, Montefalco Rosso | O tinto das massas, do tomate e da carne grelhada | Ragù, amatriciana, pizza, bitoque, arroz de pato | Cecchi Chianti e Chianti Classico; Frescobaldi Nipozzano; Montezemolo e Fontanafredda Barbera; Caprai Montefalco Rosso |
| Tinto macio e frutado | Montepulciano d'Abruzzo, Nero d'Avola, Primitivo, Merlot | Fácil, generoso, "agrada a todos" | Churrasco, lasanha, francesinha, cozido, picante suave | Masciarelli Montepulciano; Donnafugata Sedàra; Barone di Bernaj Nero d'Avola; Baglio al Sole Primitivo |
| Tinto tânico e estruturado | Barolo, Barbaresco, Brunello, Taurasi, Aglianico del Vulture, Sagrantino | Carne, caça, trufa, queijos curados | Brasato, cabrito, bistecca, filetto, Parmigiano 30 meses | Barolo Montezemolo e Fontanafredda; Brunello Cecchi e Castelgiocondo; Feudi Taurasi; Basilisco Teodosio; Caprai Sagrantino |
| Tinto de appassimento | Amarone, Ripasso, Palazzo della Torre | Corpo, álcool, fruta passa | Estufados, caça, queijos muito curados, chocolate amargo (Amarone) | Allegrini Amarone Classico e Palazzo della Torre; Pasqua Ripasso e Amarone‡ |
| Lote internacional ("Super Toscano" e similares) | Bolgheri, Toscana IGT, Tancredi | Estrutura e madeira; carne vermelha | Picanha, costeletão, cordeiro, grelhados | Campo alle Comete Stupore Bolgheri; Tenuta Frescobaldi di Castiglioni; Donnafugata Tancredi; Antinori Guado al Tasso e Tignanello\* |
| Doce (passito, Vin Santo, Moscato) | Passito di Pantelleria, Moscato di Pantelleria, Vin Santo, Recioto | Sobremesa, queijos azuis e curados | Cannoli, cantucci, tiramisù, doces conventuais, Gorgonzola | Donnafugata Ben Ryé e Kabir; Frescobaldi Pomino Vin Santo |
| Aromatizado / digestivo | Barolo Chinato | Chocolate, café, fecho | Chocolate negro, tiramisù, charuto | Fontanafredda Barolo Chinato |

---

## 5. Clássicos regionais italianos, prato a prato

(prática profissional; os pares são tradição de sommelier e de mesa regional, não regras. A descrição
dos pratos é culinária corrente (não verificada). Os estatutos DOP/IGP de queijos e salumi estão nas
secções 6.13 e 6.14, com o número de processo eAmbrosia **[22]**; as denominações de vinho citadas foram
conferidas na lista MASAF dos vinhos DOP **[21]**.)

Os ficheiros de região (`regioes-norte.md`, `regioes-centro.md`, `regioes-sul-ilhas.md`) têm mais
pormenor. Aqui fica a versão de consulta rápida, com o vinho do catálogo mais próximo quando existe.

### 5.1 Piemonte

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Tajarin al tartufo bianco d'Alba | Barolo ou Barbaresco com alguns anos | Notas terrosas do Nebbiolo evoluído com a trufa; massa de ovo e manteiga amaciam o tanino | Montezemolo Barolo Monfalletto e Enrico VI; Fontanafredda Barolo Vigna La Rosa |
| Vitello tonnato | Roero Arneis, Gavi, Alta Langa, Langhe Nebbiolo leve | Molho de atum, maionese e alcaparras pede acidez | Fontanafredda Pradalupo Roero Arneis, Gavi di Gavi, Alta Langa |
| Carne cruda all'albese | Dolcetto, Langhe Nebbiolo | Carne crua delicada: tanino médio, fruta | Montezemolo Langhe Nebbiolo; Fontanafredda Ebbio |
| Agnolotti del plin | Dolcetto, Barbera d'Alba | Recheio de carne e molho de assado | Montezemolo Barbera d'Alba; Fontanafredda Raimonda |
| Brasato al Barolo | Barolo | Guisado de vaca em Nebbiolo: ponte e proteína para o tanino | Fontanafredda Barolo Etichetta Platino |
| Bollito misto con bagnetto verde | Barbera d'Asti ou Nizza, Dolcetto | A acidez da Barbera corta a gordura das carnes cozidas | Montezemolo Barbera d'Alba Superiore Funtanì |
| Bagna cauda | Barbera, Dolcetto | Anchova, alho e azeite: tinto ácido, pouco tânico | Fontanafredda Raimonda |
| Castelmagno, Toma, Robiola | Barolo (Castelmagno), Arneis ou Erbaluce (Robiola) | Queijo de montanha curado com tanino; queijo fresco com branco | Barolo do catálogo; Montezemolo Langhe Arneis |
| Bonet, torta di nocciole | Moscato d'Asti, Asti; Barolo Chinato (bonet com cacau) | Doce com doce; quina com chocolate | Fontanafredda Asti e Barolo Chinato |

### 5.2 Valle d'Aosta

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Fonduta di Fontina | Petite Arvine, Chardonnay de montanha | Queijo derretido: acidez para cortar | Sem vinhos da região; alternativa: Franciacorta Satèn |
| Carbonade (vaca em vinho) | Fumin, Torrette | Estufado rústico | Alternativa: Langhe Nebbiolo |
| Lardo di Arnad, mocetta | Blanc de Morgex et de La Salle | Gordura e sal com branco alpino muito ácido | Alternativa: Franciacorta Pas Dosé |

### 5.3 Lombardia

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Risotto alla milanese | Franciacorta Satèn, Lugana | Açafrão, manteiga e cremosidade | Berlucchi '61 Satèn; Allegrini Lugana |
| Cotoletta alla milanese | Franciacorta Brut, Oltrepò Pinot Nero | Panado frito em manteiga: bolha | Berlucchi '61 Extra Brut; Bellavista Alma Gran Cuvée Brut\* |
| Ossobuco con gremolada | Valtellina Superiore, Barbera | Carne gelatinosa e citrinos: tinto ácido | Fontanafredda Papagena Barbera d'Alba Superiore |
| Bresaola della Valtellina | Rosso di Valtellina (Nebbiolo), Franciacorta Rosé | Carne magra e salgada: tanino fino, fruta | Montezemolo Langhe Nebbiolo; Berlucchi '61 Rosé |
| Pizzoccheri | Valtellina Superiore | Trigo-sarraceno, couve, batata e queijo | Langhe Nebbiolo |
| Casoncelli, tortelli di zucca | Lugana, Franciacorta Satèn | Doce da abóbora e amaretti, manteiga | Allegrini Lugana |
| Gorgonzola, Taleggio, Grana Padano | Franciacorta millesimato; Sforzato ou passito com Gorgonzola piccante | Sal e gordura: bolha; azul: contraste doce | Berlucchi '61 Nature; Donnafugata Ben Ryé |

### 5.4 Trentino-Alto Adige

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Speck | Trento DOC, Schiava, Pinot Nero, Lagrein | Fumado pede fruta e frescura | Ferrari Brut\*; Jermann Red Angel |
| Canederli | Pinot Bianco, Lagrein | Pão, speck e caldo | Pomino Bianco (Chardonnay e Pinot Bianco segundo a lista trade; não verificado) |
| Carne salada, polenta com cogumelos | Teroldego, Marzemino, Lagrein | Rústico e terroso | Langhe Nebbiolo |
| Strudel | Moscato Giallo, Gewürztraminer vendemmia tardiva | Maçã, canela, massa | Fontanafredda Asti |
| Cozinha asiática e caril (em Portugal) | Gewürztraminer, Müller-Thurgau | Aroma e ligeira doçura com especiaria | Joseph Gewürztraminer\* e Müller Thurgau\* |

### 5.5 Veneto

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Baccalà alla vicentina (bacalhau seco estufado em leite) | Soave Classico, Lugana, Lessini Durello | Ponte com o bacalhau português. Atenção: no Veneto, "baccalà" designa em regra o stoccafisso (bacalhau seco sem sal), e não o bacalhau salgado português (não verificado) | Allegrini Lugana; Pasqua Soave Classico‡ |
| Baccalà mantecato | Prosecco Brut, Soave | Creme de bacalhau em crostini: bolha e acidez | Carpenè Malvolti 1868 Extra Brut |
| Sarde in saor (agridoce) | Prosecco, Soave | Agridoce pede acidez e fruta; Extra Dry aceita o doce da cebola | Bolla Prosecco DOC Extra Dry |
| Risotto all'Amarone | Amarone ou Ripasso | O vinho está no prato | Allegrini Amarone Classico; Palazzo della Torre |
| Pastissada de caval, brasati | Amarone | Estufado longo e rico | Allegrini Amarone Classico |
| Bigoli in salsa (anchova e cebola) | Soave, Bardolino | Sal e doce da cebola | Pasqua Soave‡; Valpolicella Classico |
| Radicchio di Treviso grelhado | Valpolicella, Bardolino | O amargo pede tinto leve e frutado | Allegrini Valpolicella Classico |
| Cicchetti venezianos | Prosecco | Petiscos de balcão, bolha | Prosecco do catálogo |
| Tiramisù, pandoro | Recioto di Soave, Recioto della Valpolicella, Moscato | Doce com doce | Fontanafredda Asti; Donnafugata Ben Ryé |

### 5.6 Friuli Venezia Giulia

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Prosciutto di San Daniele | Friulano | O "tajut" friulano; branco com amêndoa e acidez | Jermann Vintage Tunina; Sirch Ribolla Gialla‡ |
| Frico (Montasio com batata) | Ribolla Gialla, Friulano, Refosco | Queijo frito: acidez | Jermann Pinot Grigio |
| Jota, brovada e muset | Refosco, Terrano | Rústico, ácido, com porco | Jermann Blau & Blau |
| Peixe e marisco do Adriático | Malvasia, Vitovska, Ribolla | Salinos, excelentes com marisco português | Jermann Sauvignon; Sirch Ribolla Gialla‡ |
| Gubana, presnitz | Picolit, Ramandolo | Doce de frutos secos | Pomino Vin Santo |

### 5.7 Liguria

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Trofie ou trenette al pesto | Vermentino, Pigato | Ervas, alho, pinhões, queijo: branco herbáceo sem madeira | Aragosta Vermentino‡; Sella&Mosca Vermentino‡; Fontanafredda Gavi |
| Focaccia genovese, focaccia di Recco, farinata | Vermentino, espumante seco | Azeite, sal, queijo: acidez e bolha | Prosecco Brut; Franciacorta |
| Coniglio alla ligure | Rossese di Dolceacqua | Tinto leve com ervas e azeitonas | Allegrini Valpolicella Classico |
| Cappon magro, peixe ao sal | Vermentino | Mar e ervas | Vermentino do catálogo‡ |

### 5.8 Emilia-Romagna

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Prosciutto di Parma, Culatello, Coppa Piacentina | Lambrusco secco (Sorbara, Salamino), Malvasia secca frisante | Bolha e acidez limpam a gordura doce | Ceci Otello 1813 e Giuseppe Verdi Dry; Albinea Canali Ottocento Nero |
| Mortadella Bologna (IGP) | Lambrusco Grasparossa, Pignoletto frisante | Gordura e especiaria | Ceci Otello 1813 |
| Parmigiano Reggiano | Lambrusco secco; tintos estruturados com o muito curado | Sal, umami e cristais | Lambrusco do catálogo; Allegrini Amarone Classico |
| Gnocco fritto e tigelle com salumi | Lambrusco secco | Frito e salumi | Albinea Canali Ottocento Nero |
| Tortellini in brodo | Lambrusco di Sorbara, Pignoletto | Caldo delicado e recheio de carne | Albinea Canali Ottocentorosa (rosato; confirmar doçura) |
| Tagliatelle al ragù, lasagne | Sangiovese da DOC Romagna **[21]**, Lambrusco Grasparossa | Tomate e carne: acidez | Cecchi Chianti; Donnafugata Sedàra (o produtor recomenda-o com lasanha **[9]**) |
| Cotechino e zampone com lentilhas | Lambrusco Grasparossa | Par de fim de ano: gordura gelatinosa | Ceci Giuseppe Verdi Dry |
| Parmigiano com Aceto Balsamico Tradizionale | Lambrusco amabile | Doce-ácido contra sal | Ceci Giuseppe Verdi Amabile |
| Zuppa inglese, ciambella | Albana passito, Lambrusco amabile | Doce com doce | Ceci Rosato Amabile |

### 5.9 Toscana

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Bistecca alla fiorentina | Chianti Classico Riserva, Brunello | Tanino e acidez com carne grelhada e gordura | Frescobaldi Castelgiocondo; Cecchi Brunello; Nipozzano Riserva |
| Pappardelle al cinghiale | Chianti Classico Riserva, Chianti Rufina | Caça com tomate: acidez do Sangiovese | Frescobaldi Nipozzano Riserva; Cecchi Chianti Classico Storia di Famiglia |
| Ribollita, pappa al pomodoro | Chianti jovem, Rosso di Montalcino | Rústico e vegetal, tinto leve e ácido | Cecchi Chianti; Castiglioni Chianti; Cecchi Rosso di Montalcino Gli Amici |
| Crostini di fegatini | Chianti Rufina; Vin Santo | Clássico florentino; fígado aceita doce | Nipozzano Riserva; Pomino Vin Santo |
| Finocchiona, salame toscano | Chianti | Sal, funcho e gordura com fruta ácida | Cecchi Chianti |
| Pici all'aglione, cacio e pepe senese | Rosso di Montalcino | Massa rústica de Siena | Cecchi Rosso di Montalcino Gli Amici |
| Cacciucco (Livorno) | Rosato, Morellino, Vermentino | Caldeirada com tomate e picante | Frescobaldi Alìe Rosé |
| Pecorino toscano | Vernaccia (fresco); Nobile ou Brunello (curado) | A cura do queijo acompanha a estrutura do vinho | Brunello do catálogo |
| Cantucci, panforte | Vin Santo | Tradição | Frescobaldi Pomino Vin Santo |

### 5.10 Umbria

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Strangozzi al tartufo nero di Norcia | Montefalco Rosso; Grechetto com estágio | Trufa negra com tinto médio ou branco estruturado | Caprai Montefalco Rosso; Caprai Grecante |
| Norcineria (prosciutto di Norcia, capocollo) | Montefalco Rosso | Salumi intensos | Caprai Montefalco Rosso |
| Porchetta | Montefalco Rosso, Grechetto | Gordura e funcho | Caprai Montefalco Rosso e Grecante |
| Piccione, palombaccio | Sagrantino | Caça de penas com molho escuro | Caprai Sagrantino Collepiano |
| Agnello, cordeiro na brasa | Sagrantino | Proteína e gordura para o tanino | Caprai Sagrantino 25 Anni |
| Lenticchie di Castelluccio com salsicha | Montefalco Rosso | Rústico de montanha | Caprai Montefalco Rosso Riserva |

### 5.11 Marche

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Brodetto | Verdicchio Classico Superiore | Caldeirada de peixe adriática | Alternativa: Valori Pecorino (o produtor sugere-o com peixe do Adriático **[13]**) |
| Olive all'ascolana | Pecorino, Verdicchio, Passerina espumante | Frito e sal: acidez e bolha | Valori Pecorino |
| Stoccafisso all'anconetana | Castelli di Jesi Verdicchio Riserva (DOCG) **[21]** | Bacalhau seco estufado: útil para o público português | Masciarelli Trebbiano d'Abruzzo; Castello di Semivicoli Pecorino‡ |
| Vincisgrassi | Cònero (DOCG) ou Rosso Cònero (DOC), Rosso Piceno **[21]** | Lasanha rica com ragù e miúdos | Masciarelli Montepulciano d'Abruzzo |

### 5.12 Lazio (cozinha romana)

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Cacio e pepe | Frascati Superiore; Trebbiano; Verdicchio | Pecorino e pimenta pedem acidez e alguma estrutura | Masciarelli Trebbiano d'Abruzzo; Frescobaldi Pomino Bianco |
| Carbonara | Frascati Superiore, Verdicchio, Cerasuolo d'Abruzzo | Ovo e guanciale: branco estruturado ou rosato | Gianni Masciarelli Cerasuolo; Feudi Fiano di Avellino |
| Amatriciana, gricia | Cesanese, Montepulciano d'Abruzzo, Chianti Classico | Tomate (amatriciana) e guanciale | Masciarelli Montepulciano; Cecchi Chianti Classico |
| Carciofi alla romana e alla giudia | Frascati, Pecorino, Vermentino | A alcachofra torna os vinhos doces e metálicos: brancos secos, salinos, sem madeira | Valori Pecorino |
| Supplì e fritti | Frascati, espumante brut | Fritura: acidez e bolha | Prosecco Brut; Berlucchi '61 Extra Brut |
| Abbacchio a scottadito ou al forno | Cesanese, Montepulciano Riserva | Cordeiro com ervas | Marina Cvetic Montepulciano Riserva |
| Saltimbocca alla romana | Frascati Superiore, Cesanese leve | Vitela, presunto e salva | Pomino Bianco; Valpolicella Classico |
| Coda alla vaccinara | Cesanese del Piglio, Montepulciano | Estufado longo | Villa Gemma Montepulciano Riserva |

### 5.13 Abruzzo e Molise

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Arrosticini (espetadas de carneiro) | Montepulciano d'Abruzzo jovem; Cerasuolo | O casamento regional por excelência | Masciarelli Montepulciano Linea Classica e Gianni Masciarelli; Cerasuolo |
| Maccheroni alla chitarra com ragù e pallottine | Montepulciano d'Abruzzo | Tomate e carne | Gianni Masciarelli Montepulciano |
| Pecora alla callara | Montepulciano Riserva | Estufado de ovelha longo | Villa Gemma e Marina Cvetic Riserva |
| Brodetto alla vastese | Trebbiano d'Abruzzo, Cerasuolo, Pecorino | Caldeirada com pimento | Gianni Masciarelli Trebbiano; Cerasuolo |
| Ventricina (salame picante) | Cerasuolo; Montepulciano jovem | Picante e gordura | Gianni Masciarelli Cerasuolo |
| Pecorino di Farindola | Trebbiano Riserva; Montepulciano Riserva | Queijo de ovelha de montanha | Marina Cvetic Montepulciano Riserva |

### 5.14 Campania

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Pizza margherita e marinara | Piedirosso fresco, Falanghina, Lacryma Christi | Tomate e mozzarella: acidez, fruta, pouco tanino | Feudi Lacryma Christi Rosso e Bianco; Falanghina del Sannio |
| Mozzarella di bufala | Falanghina, Greco jovem, Asprinio | Lácteo e ácido: branco vivo | Feudi Falanghina del Sannio e Greco di Tufo |
| Spaghetti alle vongole, frittura di paranza | Falanghina, Greco di Tufo | Iodo, alho, azeite, fritura | Feudi Serrocielo; Greco di Tufo |
| Polpo alla luciana | Piedirosso, Falanghina | Polvo com tomate: tinto leve ou branco vivo | Feudi Lacryma Christi Rosso |
| Ragù napoletano, Genovese | Aglianico, Taurasi | Cozedura longa de carne | Feudi Rubrato e Taurasi |
| Parmigiana di melanzane, sartù di riso | Aglianico jovem | O produtor recomenda o Rubrato para estes dois pratos **[14]** | Feudi Rubrato |
| Caciocavallo, provolone del Monaco | Fiano com anos; Taurasi | Pasta filata curada | Feudi Pietracalda; Taurasi |
| Sfogliatella, babà, pastiera | Passito; Moscato | Não pôr tintos secos na sobremesa | Donnafugata Kabir e Ben Ryé |

### 5.15 Puglia

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Burrata, stracciatella, mozzarella | Rosato de Negroamaro ou Bombino Nero; Fiano; Vermentino | Lácteo e cremoso: frescura e textura | Feudi Fiano di Avellino; Donnafugata Rosa |
| Orecchiette alle cime di rapa | Rosato do Salento, Negroamaro jovem | Amargo da rama, anchova e malagueta: fruta e frescura, sem madeira | Gianni Masciarelli Cerasuolo |
| Bombette, carne na brasa | Primitivo di Manduria, Gioia del Colle | Grelhados de porco e especiaria | Baglio al Sole Primitivo |
| Tiella barese, crudo di mare | Bombino Bianco, Verdeca, rosato | Arroz, batata, mexilhão; marisco cru | Feudi Greco di Tufo |
| Frise, taralli, focaccia barese | Rosato ou espumante | Aperitivo | Prosecco do catálogo |

### 5.16 Basilicata e Calabria

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Peperoni cruschi, lucanica | Aglianico jovem | Pimento seco frito e salsicha | Basilisco Teodosio |
| Cordeiro e cabrito no forno, caciocavallo podolico | Aglianico del Vulture Superiore | Estrutura para carne e queijo | Basilisco Teodosio; Feudi Taurasi |
| 'Nduja, soppressata, capocollo picante | Tinto de pouco tanino e fruta (Gaglioppo fresco, rosato de Cirò) | Tanino e álcool altos amplificam o picante | Gianni Masciarelli Cerasuolo; Lambrusco |
| Peixe-espada, cebola roxa de Tropea | Cirò Rosato, Greco | Peixe carnudo e doce da cebola | Donnafugata Rosa |

### 5.17 Sicilia

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Arancine, panelle, sfincione | Grillo, Catarratto, espumante, Frappato | Fritos e amido | Donnafugata Anthìlia (o produtor recomenda-o com fritos de peixe **[5]**); SurSur |
| Caponata (agridoce) | Frappato, Cerasuolo di Vittoria, Grillo com corpo | Agridoce: acidez e fruta, sem tanino | Donnafugata SurSur; Sherazade |
| Pasta alla Norma | Nero d'Avola sem madeira, Cerasuolo di Vittoria | Beringela, tomate e ricotta salata | Donnafugata Sherazade (o produtor sugere-o com esparguete com molho de tomate **[7]**) |
| Pasta con le sarde | Grillo, Inzolia, Etna Bianco | Sardinha, funcho selvagem, passas, pinhões | Donnafugata SurSur; Isolano |
| Busiate al pesto trapanese, couscous di pesce | Grillo, Zibibbo seco | Tomate, amêndoa, ervas | Donnafugata SurSur |
| Atum (tartare, tagliata), peixe-espada | Etna Rosso ou Rosato, Cerasuolo di Vittoria | Peixe carnudo com tinto leve | Donnafugata Rosa; Sul Vulcano; a Donnafugata recomenda até o Tancredi com atum ou peixe gordo **[4]** |
| Pistácio de Bronte, pesto de pistácio | Etna Bianco, Grillo, Chardonnay siciliano | Frutos secos e cremosidade | Donnafugata Isolano, SurSur, Chiarandà |
| Carnes grelhadas, involtini, falsomagro | Nero d'Avola Riserva, lotes com estágio | Carne e especiaria | Donnafugata Mille e una Notte e Tancredi |
| Cannoli, cassata, frutta martorana | Passito di Pantelleria, Malvasia delle Lipari, Marsala | Doce com doce | Donnafugata Ben Ryé e Kabir |

### 5.18 Sardegna

| Prato | Vinho tradicional | Porquê | No catálogo |
|---|---|---|---|
| Aragosta alla catalana, fregola con arselle, bottarga | Vermentino di Gallura, Vermentino di Sardegna | Mar, sal, iodo | Aragosta Vermentino‡; Sella&Mosca Cala Reala‡ |
| Culurgiones, malloreddus | Vermentino, rosato de Cannonau | Batata, pecorino e hortelã; molho de salsicha | Vermentino do catálogo‡ |
| Porceddu (leitão no espeto) | Cannonau di Sardegna Riserva, Carignano del Sulcis | O "leitão" italiano: gordura e pele estaladiça | Sella&Mosca Cannonau Riserva‡ |
| Pecorino sardo, fiore sardo | Cannonau; Carignano Riserva com o mais curado | Queijo de ovelha salgado | Sella&Mosca Cannonau‡ |
| Seadas com mel amargo | Moscato di Sardegna, Malvasia di Bosa | Doce com doce | Donnafugata Kabir |

---

## 6. Matriz por ingrediente e molho

(prática profissional, exceto onde há fonte. Para cada entrada: 1.ª escolha, alternativas, o que
evitar, e exemplos do catálogo.)

### 6.1 Trufa (tartufo)

| Preparação | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Trufa branca crua em lâminas (tajarin, uovo al tegamino, fonduta, carpaccio) | Nebbiolo evoluído: Barolo ou Barbaresco com 8 a 15 anos | Metodo classico com longo estágio (Riserva, millesimato antigo); Chardonnay evoluído | Tintos jovens muito tânicos; brancos aromáticos (tapam a trufa); madeira nova | Montezemolo Barolo Enrico VI; Fontanafredda Barolo Riserva Serralunga d'Alba; Berlucchi Palazzo Lana Extrême e Cuvée Franco Ziliani |
| Trufa negra cozinhada (molhos, recheios, carne) | Nebbiolo (Langhe ou Barolo), Pinot Nero, Nerello Mascalese | Montefalco Rosso, Sangiovese com estágio, Metodo classico Rosé | Tintos doces e sobremaduros | Montezemolo Langhe Nebbiolo; Jermann Red Angel; Donnafugata Sul Vulcano; Caprai Montefalco Rosso |
| Crema di tartufo, burro al tartufo, azeite trufado | Metodo classico Rosé ou Pinot Nero dominante; Langhe Nebbiolo | Chardonnay com estágio (com creme); Etna Rosso | Vinhos delicados demais (o aroma sintético de alguns produtos trufados é muito forte) | Berlucchi '61 Nature Rosé; Fontanafredda Alta Langa; Fontanafredda Ebbio |
| Trufa com ovo (uovo, frittata, carbonara al tartufo) | Branco estruturado ou espumante com estágio | Nebbiolo leve e evoluído | Tintos tânicos (ovo + tanino) | Donnafugata Chiarandà; Berlucchi '61 Nature |

- **Porquê:** a trufa partilha com o Nebbiolo e o Pinot Nero evoluídos os aromas de terra, sub-bosque
  e cogumelo. A trufa branca é mais delicada e perfumada do que a negra: pede vinhos mais finos. Nomes
  botânicos correntes: *Tuber magnatum* (branca de Alba), *Tuber melanosporum* (negra "pregiata")
  (não verificado nesta revisão).

### 6.2 Porcini e cogumelos

| Preparação | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Porcini trifolati (salteados com alho e salsa) | Etna Rosso, Pinot Nero, Langhe Nebbiolo | Barbera Superiore, Rosso di Montalcino | Brancos leves e neutros | Donnafugata Sul Vulcano; Jermann Red Angel; Fontanafredda Ebbio |
| Porcini grelhados ou assados | Rosso di Montalcino, Brunello, Nebbiolo | Aglianico com estágio | Brancos aromáticos | Cecchi Rosso di Montalcino e Brunello |
| Risotto ai porcini | Langhe Nebbiolo; Chardonnay com madeira integrada | Barbera d'Alba Superiore; Franciacorta millesimato | Tintos muito tânicos e jovens | Montezemolo Langhe Nebbiolo; Donnafugata Chiarandà; Pomino Benefizio |
| Cogumelos com natas (tagliatelle, vitela) | Chardonnay com estágio, Fiano Riserva | Franciacorta Satèn | Tintos tânicos | Donnafugata Chiarandà; Feudi Pietracalda |
| Cogumelos fritos ou panados | Espumante Brut | Falanghina | Tintos pesados | Berlucchi '61 Extra Brut |
| Porcini secos (molhos concentrados, umami alto) | Tinto de tanino fino com fruta madura | Amarone (molho de carne escuro) | Tintos jovens e duros | Allegrini Palazzo della Torre; Amarone Classico |

### 6.3 Tomate (pomodoro)

| Preparação | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Tomate cru (bruschetta, caprese, panzanella) | Rosato, Vermentino, Falanghina | Prosecco Brut, Sauvignon | Tintos tânicos, madeira | Donnafugata Rosa; Frescobaldi Alìe Rosé; Feudi Falanghina |
| Molho simples de tomate e manjericão, marinara | Sangiovese jovem, Barbera, Piedirosso, Nero d'Avola sem madeira | Cerasuolo d'Abruzzo, Montepulciano jovem | Brancos de acidez baixa; tintos com muita madeira | Cecchi Chianti; Fontanafredda Raimonda; Feudi Lacryma Christi Rosso; Donnafugata Sherazade **[7]** |
| Tomate de cozedura longa com carne | Ver 6.5 (ragù) | | | |
| Tomate concentrado e frito (parmigiana, pomodori secchi) | Aglianico jovem, Primitivo, Nero d'Avola | Montepulciano d'Abruzzo | Brancos leves | Feudi Rubrato (o produtor recomenda-o com parmigiana di melanzane **[14]**); Baglio al Sole Primitivo |
| Tomate com peixe (sopa de peixe, cacciucco, polvo alla luciana) | Rosato com corpo; tinto leve servido fresco | Branco com estrutura | Tintos tânicos | Gianni Masciarelli Cerasuolo; Donnafugata Sherazade (o produtor sugere-o com sopas de peixe **[7]**) |

- **Regra:** o tomate é ácido e ligeiramente doce. Pede vinho com acidez igual ou maior e fruta. É por
  isso que Sangiovese e Barbera são os tintos "de tomate" por excelência.

### 6.4 Pesto

| Tipo | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Pesto genovese (manjericão, alho, pinhões, queijo, azeite) | Vermentino, Pigato | Gavi, Sauvignon, Falanghina, Pecorino | Chardonnay com madeira; tintos tânicos | Vermentino do catálogo‡; Fontanafredda Gavi; Jermann Sauvignon; Valori Pecorino |
| Pesto alla trapanese (tomate, amêndoa, manjericão) | Grillo | Etna Bianco, rosato | Tintos pesados | Donnafugata SurSur; Isolano |
| Pesto di pistacchio | Grillo, Fiano | Chardonnay com pouca madeira, Franciacorta Satèn | Tintos tânicos | Donnafugata SurSur; Feudi Pietracalda; Berlucchi '61 Satèn |
| Pesto rosso (tomate seco) | Rosato; Nero d'Avola sem madeira | Montepulciano jovem | Brancos muito leves | Donnafugata Rosa; Sherazade |

### 6.5 Ragù e molhos de carne

| Tipo | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Ragù alla bolognese (tagliatelle, lasagne) | Sangiovese (Romagna, Chianti), Lambrusco Grasparossa | Barbera, Montepulciano | Brancos leves | Cecchi Chianti; Ceci Otello 1813; Donnafugata Sedàra (o produtor recomenda-o com lasanha **[9]**) |
| Ragù napoletano (pedaços de carne, cozedura longa) | Aglianico (Taurasi, Irpinia) | Piedirosso; Primitivo | Brancos | Feudi Rubrato e Taurasi |
| Genovese napoletana (cebola e vaca) | Aglianico | Fiano com estrutura (branco possível pela doçura da cebola) | Tintos leves de mais | Feudi Taurasi; Pietracalda |
| Ragù de caça (javali, lebre, pato) | Chianti Classico Riserva, Brunello, Sagrantino (lebre) | Nebbiolo, Nero d'Avola com estágio | Tintos leves | Frescobaldi Nipozzano; Cecchi Brunello; Caprai Sagrantino Collepiano; Donnafugata Mille e una Notte (o produtor recomenda-o com primeiros pratos com ragù **[10]**) |
| Ragù bianco (vitela ou salsicha, sem tomate) | Barbera, Dolcetto | Verdicchio Riserva, Montefalco Rosso, Fiano | Tintos muito tânicos | Montezemolo Barbera d'Alba; Caprai Montefalco Rosso |
| Brasato, stracotto, guanciale brasato | Barolo, Amarone, Taurasi | Montepulciano Riserva | Brancos e tintos leves | Fontanafredda Barolo; Allegrini Amarone; Villa Gemma Riserva |

### 6.6 Carbonara

- **O que manda:** gema de ovo (reveste a boca), guanciale (sal, gordura), Pecorino Romano (sal,
  umami), pimenta preta.
- **1.ª escolha:** branco com estrutura e acidez: Fiano, Trebbiano d'Abruzzo, Verdicchio, Frascati
  Superiore, Greco. **Alternativas:** Franciacorta Satèn ou Blanc de Blancs; rosato com corpo
  (Cerasuolo d'Abruzzo); tinto muito leve e ácido (Cesanese, Valpolicella) para quem só bebe tinto.
- **Evitar:** tintos tânicos (ovo e tanino ficam metálicos); brancos leves de acidez baixa.
- **No catálogo:** Feudi Fiano di Avellino; Gianni Masciarelli Trebbiano d'Abruzzo; Berlucchi '61
  Satèn; Gianni Masciarelli Cerasuolo d'Abruzzo.

### 6.7 Cacio e pepe

- **O que manda:** Pecorino Romano (muito sal, gordura, umami), pimenta preta (picante aromático),
  água da massa (amido, cremosidade).
- **1.ª escolha:** branco de acidez alta com alguma estrutura: Trebbiano d'Abruzzo, Frascati Superiore,
  Verdicchio, Greco di Tufo, Etna Bianco. **Alternativas:** espumante Extra Brut ou Pas Dosé (a bolha
  limpa o queijo); tinto leve e fresco (Cesanese, Rosso di Montalcino jovem, como se faz em Siena com os
  pici).
- **Versão "di mare" (menu Emporio):** o marisco puxa para branco salino (Greco, Carricante, Vermentino)
  ou para Blanc de Blancs.
- **Evitar:** tintos tânicos; brancos aromáticos doces; Chardonnay com muita madeira.
- **No catálogo:** Gianni Masciarelli Trebbiano; Feudi Greco di Tufo e Cutizzi; Donnafugata Isolano;
  Berlucchi '61 Nature Blanc de Blancs.

### 6.8 Amatriciana e gricia

| Prato | O que manda | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|---|
| Amatriciana (guanciale, tomate, pecorino, por vezes malagueta) | Acidez do tomate, gordura, sal | Montepulciano d'Abruzzo, Cesanese, Chianti Classico | Barbera, Cerasuolo d'Abruzzo, Etna Rosso | Masciarelli Montepulciano (Linea Classica e Gianni Masciarelli); Cecchi Chianti Classico Storia di Famiglia; Fontanafredda Papagena |
| Gricia (guanciale e pecorino, sem tomate) | Gordura e sal | Branco estruturado (Frascati Superiore, Verdicchio, Fiano) | Lambrusco secco; Cesanese leve | Feudi Fiano di Avellino; Ceci Giuseppe Verdi Dry |

### 6.9 Frutos do mar

| Prato | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Spaghetti alle vongole (amêijoa, alho, azeite, salsa, vinho branco) | Falanghina, Greco, Vermentino, Verdicchio | Pecorino; Prosecco Extra Brut | Tintos; madeira | Feudi Falanghina e Serrocielo; Greco di Tufo; Valori Pecorino |
| Cozze (impepata, alla marinara) | Vermentino, Falanghina | Bombino Bianco, Prosecco Brut | Madeira | Feudi Falanghina; Vermentino‡ |
| Gamberi, scampi, carabineiros | Metodo classico Pas Dosé ou Extra Brut; Etna Bianco | Vermentino, Fiano | Tintos tânicos | Berlucchi '61 Nature; Donnafugata Isolano |
| Gambero rosso cru | Metodo classico Rosé | Etna Rosato, Pas Dosé | Tintos | Berlucchi '61 Nature Rosé |
| Lagosta, lavagante (grelhada, com manteiga, catalana) | Chardonnay com estágio; Fiano Riserva; Franciacorta millesimato | Vermentino (catalana, com tomate cru e cebola) | Tintos | Donnafugata Chiarandà (o produtor recomenda-o com lagosta **[8]**); Feudi Pietracalda; Berlucchi '61 Nature |
| Polvo grelhado | Fiano, Greco; Etna Rosso fresco | Cerasuolo d'Abruzzo | Tintos tânicos | Feudi Pietracalda; Donnafugata Sul Vulcano |
| Fritto misto, frittura di paranza, calamari fritos | Prosecco Brut, Trento DOC, Franciacorta Brut | Falanghina, Pecorino, Grillo | Tintos | Carpenè Malvolti 1868 Extra Brut; Berlucchi '61 Extra Brut; Donnafugata Anthìlia (o produtor sugere-o com peixe frito **[5]**) |
| Brodetto, cacciucco, zuppa di pesce | Verdicchio; rosato com corpo | Tinto leve fresco (Nero d'Avola sem madeira); lote siciliano com peixe estufado | Tintos tânicos | Gianni Masciarelli Cerasuolo; Sherazade (sopas de peixe **[7]**); Donnafugata Mille e una Notte (o produtor sugere prová-lo com pratos saborosos de peixe estufado **[10]**) |
| Bottarga (massa, lâminas) | Vermentino, Carricante | Pas Dosé | Tintos, madeira | Donnafugata Isolano; Vermentino‡ |
| Nero di seppia (risotto, massa) | Etna Bianco ou Etna Rosso leve | Pas Dosé, Vermentino | Tintos pesados | Donnafugata Isolano e Sul Vulcano |

### 6.10 Peixe cru (crudo, carpaccio, tartare, sushi)

| Prato | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Crudo di mare (ostras, ouriço, lagostins crus) | Metodo classico Pas Dosé ou Extra Brut | Vermentino, Etna Bianco, Prosecco Extra Brut | Madeira, tintos, Extra Dry (o doce estraga o iodo) | Berlucchi '61 Nature e Nature Blanc de Blancs; Carpenè Malvolti 1868 Extra Brut; Bellavista Non Dosato\* |
| Carpaccio de peixe branco com citrinos | Vermentino, Greco, Falanghina | Anthìlia; Gavi | Madeira | Feudi Greco di Tufo; Donnafugata Anthìlia (o produtor recomenda-o com peixe cru **[5]**) |
| Tártaro de atum ou salmão | Rosé de metodo classico; rosato | Etna Rosso fresco; Pinot Nero | Tintos tânicos | Berlucchi '61 Rosé; Donnafugata Rosa; Gianni Masciarelli Cerasuolo |
| Atum mal passado (tagliata, selado) | Tinto leve ou médio de tanino fino | Rosato; lotes sicilianos | Tintos muito tânicos e alcoólicos com atum simples | Donnafugata Sul Vulcano; Sedàra (atum ligeiramente selado **[9]**); Tancredi só com atum cozinhado com molho rico (o produtor sugere-o com atum ou peixe gordo **[4]**) |
| Sushi e sashimi | Metodo classico Extra Brut ou Rosé; Prosecco Extra Dry (molho de soja doce, gengibre) | Vermentino, Lugana | Tintos tânicos; madeira | Berlucchi '61 Extra Brut; Bolla Prosecco DOC Extra Dry; Allegrini Lugana |
| Ceviche (lima, malagueta, cebola roxa) | Vermentino, Sauvignon, Pecorino | Prosecco Brut; Pas Dosé | Madeira, tintos | Jermann Sauvignon; Valori Pecorino |

- **Regra:** o peixe cru é delicado, salino e às vezes gordo (atum, salmão). Pede acidez, sal e bolha,
  sem madeira nem tanino. O rosé é a ponte para o peixe vermelho.

### 6.11 Risotto

| Risotto | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|
| Alla milanese (açafrão, tutano, manteiga) | Franciacorta Satèn, Lugana | Chardonnay leve; Barbera (tradição com ossobuco) | Berlucchi '61 Satèn; Allegrini Lugana; Pomino Bianco |
| Ai porcini, ai funghi | Langhe Nebbiolo; Chardonnay com madeira | Barbera Superiore | Montezemolo Langhe Nebbiolo; Donnafugata Chiarandà (o produtor sugere-o com risotto **[8]**) |
| Ai frutti di mare, alla pescatora | Vermentino, Greco, Blanc de Blancs | Fiano, Falanghina | Feudi Greco di Tufo; Berlucchi '61 Nature Blanc de Blancs |
| Verde (ervas, espinafres, espargos, ervilhas) | Sauvignon, Verdicchio, Vermentino, Pecorino | Prosecco Extra Brut | Jermann Sauvignon; Valori Pecorino |
| All'Amarone, al Barolo | O mesmo vinho ou irmão mais novo | Ripasso; Langhe Nebbiolo | Allegrini Palazzo della Torre; Fontanafredda Ebbio |
| Al radicchio (com speck ou taleggio) | Valpolicella, Bardolino | Pinot Nero | Allegrini Valpolicella Classico; Jermann Red Angel |
| Alla zucca (com amaretti, sálvia) | Lugana, Soave, Chardonnay | Fiano | Allegrini Lugana; Corte Giara Chardonnay |
| Al tartufo | Ver 6.1 | | |
| Al limone, con gamberi | Greco, Vermentino | Franciacorta Extra Brut | Feudi Cutizzi |

### 6.12 Pizza

A pizza junta **acidez** (tomate), **gordura** (mozzarella, azeite, salumi) e **sal**. Funcionam os
vinhos com acidez viva, fruta, pouco tanino e, muitas vezes, bolha. A regra do "tinto para a pizza" só
vale para tintos frescos e servidos frescos.

| Pizza | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Margherita | Piedirosso ou Lacryma Christi Rosso fresco; Falanghina | Lambrusco secco; Prosecco Brut; Cerasuolo d'Abruzzo; Nero d'Avola sem madeira | Barolo, Amarone, tintos com muita madeira | Feudi Lacryma Christi Rosso; Feudi Falanghina; Gianni Masciarelli Cerasuolo (o produtor inclui a pizza nas harmonizações **[12]**); Donnafugata Sherazade (pizza **[7]**) |
| Marinara (tomate, alho, orégão, sem queijo) | Falanghina, Greco | Rosato; Piedirosso | Brancos com madeira | Feudi Falanghina; Greco di Tufo |
| Diavola (salame picante) | Lambrusco secco ou amabile; Primitivo servido fresco | Montepulciano jovem; rosato | Tintos tânicos e alcoólicos servidos quentes | Ceci Otello 1813 ou Giuseppe Verdi Amabile; Baglio al Sole Primitivo; Masciarelli Montepulciano Linea Classica |
| Quattro formaggi | Franciacorta Satèn ou Brut; Lugana | Barbera; Soave. Se o Gorgonzola dominar, Lambrusco amabile em contraste | Tintos tânicos | Berlucchi '61 Satèn; Allegrini Lugana; Montezemolo Barbera d'Alba |
| Pistacchio e mortadella (com burrata ou stracciatella) | Lambrusco secco; Franciacorta Satèn | Grillo; Fiano | Tintos tânicos | Albinea Canali Ottocento Nero; Berlucchi Cuvée Imperiale Satèn; Donnafugata SurSur |
| Bianca (mozzarella e azeite; com batata e alecrim) | Falanghina, Vermentino, Prosecco Brut | Franciacorta; Pecorino | Tintos | Feudi Falanghina; Carpenè Malvolti 1868 Extra Brut |
| Salsiccia e friarielli | Aglianico jovem; Piedirosso | Montepulciano jovem | Brancos leves | Feudi Rubrato; Lacryma Christi Rosso |
| Prosciutto crudo e rúcula | Lambrusco secco; Prosecco Brut | Rosato | Tintos tânicos (rúcula amarga) | Ceci Giuseppe Verdi Dry; Donnafugata Rosa |
| Capricciosa (fiambre, cogumelos, alcachofra, azeitonas) | Barbera; Chianti | Cerasuolo d'Abruzzo | Tintos com madeira (alcachofra) | Fontanafredda Raimonda; Cecchi Chianti |
| Com trufa ou creme de trufa | Langhe Nebbiolo; Metodo classico Rosé | Etna Rosso | Brancos neutros | Fontanafredda Ebbio; Berlucchi '61 Rosé |
| Com anchova (napoli, romana) | Vermentino, Greco | Rosato | Tintos tânicos | Vermentino‡; Feudi Greco di Tufo |
| Pizza fritta, montanara | Prosecco Brut; Lambrusco secco | Falanghina | Tintos pesados | Carpenè Malvolti 1868 Extra Brut |

### 6.13 Salumi

| Salume | Perfil | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|---|
| Prosciutto di Parma | Doce, delicado, gordura fina | Lambrusco secco (Sorbara) | Franciacorta Satèn ou Brut; Prosecco Brut ou Extra Dry; Malvasia secca frisante | Ceci Otello 1813; Albinea Canali Ottocento Nero; Berlucchi '61 Satèn; Bolla Prosecco Superiore Extra Dry |
| Prosciutto di San Daniele | Doce, macio | Friulano; Ribolla Gialla | Franciacorta; Prosecco Brut | Jermann Vintage Tunina; Sirch Ribolla Gialla‡ |
| Prosciutto toscano, prosciutto crudo salgado | Mais sal e pimenta | Chianti | Rosso di Montalcino | Cecchi Chianti; Gli Amici |
| Culatello di Zibello | Intenso, macio, nobre | Lambrusco secco de qualidade; Franciacorta millesimato | Pinot Nero | Ceci Otello 1813; Berlucchi '61 Nature |
| Mortadella Bologna (IGP) | Gordura, especiaria, pistácio | Lambrusco Grasparossa; Pignoletto frisante | Franciacorta Brut; Barbera | Ceci Otello 1813; Berlucchi '61 Extra Brut; Fontanafredda Raimonda |
| Bresaola | Magra, salgada, carne vermelha curada | Nebbiolo (Valtellina, Langhe) | Franciacorta Rosé; rosato | Montezemolo Langhe Nebbiolo; Berlucchi '61 Rosé |
| Coppa, capocollo | Gordura marmoreada, especiaria | Lambrusco; Barbera | Montefalco Rosso | Ceci Giuseppe Verdi Dry; Caprai Montefalco Rosso |
| Speck | Fumado, especiaria | Pinot Nero; Trento DOC; Lagrein | Gewürztraminer (fumado e especiaria) | Jermann Red Angel; Ferrari Brut\*; Joseph Gewürztraminer\* |
| Salame (Milano, Felino, finocchiona) | Sal, gordura, alho ou funcho | Barbera; Chianti; Lambrusco | Dolcetto, Valpolicella | Montezemolo Barbera d'Alba; Cecchi Chianti |
| 'Nduja, soppressata e salumi picantes | Picante e gordura | Lambrusco amabile ou secco; rosato | Tintos frutados de tanino baixo | Ceci Giuseppe Verdi Amabile; Gianni Masciarelli Cerasuolo |
| Lardo (Colonnata, Arnad) | Gordura pura, ervas | Franciacorta Pas Dosé; Vermentino | Lambrusco secco | Berlucchi '61 Nature |
| Tábua mista para evento | Tudo o acima | **Lambrusco secco + Franciacorta Brut** (a dupla que resolve quase tudo) | Barbera | Ceci Otello 1813 + Berlucchi '61 Extra Brut |

**Estatuto na UE dos salumi citados** (número de processo no registo eAmbrosia **[22]**; útil para fichas
de produto e para distinguir o produto com denominação do genérico):

| Produto | Estatuto | N.º eAmbrosia |
|---|---|---|
| Prosciutto di Parma | DOP | PDO-IT-0067 |
| Prosciutto di San Daniele | DOP | PDO-IT-0065 |
| Prosciutto Toscano | DOP | PDO-IT-1494 |
| Prosciutto di Norcia | IGP | PGI-IT-1554 |
| Culatello di Zibello | DOP | PDO-IT-1492 |
| Coppa Piacentina | DOP | PDO-IT-1498 |
| Mortadella Bologna (é este o nome registado, sem "di") | IGP | PGI-IT-0325 |
| Bresaola della Valtellina | IGP | PGI-IT-1525 |
| Speck Alto Adige | IGP | PGI-IT-0327 |
| Salame Felino | IGP | PGI-IT-0597 |
| Finocchiona | IGP | PGI-IT-1120 |
| Capocollo di Calabria | DOP | PDO-IT-1570 |
| Soppressata di Calabria | DOP | PDO-IT-1569 |
| Lardo di Colonnata | IGP | PGI-IT-0269 |
| Valle d'Aosta Lard d'Arnad | DOP | PDO-IT-1493 |
| Cotechino Modena / Zampone Modena | IGP | PGI-IT-1500 / PGI-IT-1501 |

"Prosciutto crudo", "coppa" ou "salame" sem denominação são nomes genéricos. As regras de produção
(zonas, curas mínimas) destes produtos não foram verificadas nesta revisão.

### 6.14 Queijos italianos

**Regras de queijo (juízo):**
- Com queijo, **o branco e o espumante falham menos do que o tinto**: a gordura láctea e o sal gostam de
  acidez e bolha; o tanino pode ficar amargo e metálico com queijos frescos e cremosos.
- **Quanto mais curado o queijo, mais estrutura aguenta** o vinho (e mais sal, que suaviza o tanino).
- **Queijos azuis e muito salgados** gostam de **doce em contraste** (passito, Vin Santo, Marsala).
- **Casca lavada e aroma forte** (Taleggio): espumante, brancos aromáticos, tintos leves.
- Numa tábua variada, dois vinhos resolvem: **Franciacorta ou Trento Brut** e um **doce** (Ben Ryé ou
  Vin Santo).

**Parmigiano Reggiano por idade.** O Parmigiano Reggiano é DOP (eAmbrosia PDO-IT-0016) **[22]**. A cura
mínima de 12 meses é conhecimento corrente, mas não foi confirmada no disciplinare nesta revisão (não
verificado; confirmar no Consorzio del Formaggio Parmigiano Reggiano). A tabela é juízo de sommelier:

| Cura | Perfil | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|---|
| 12 a 18 meses | Lático, fresco, iogurte, erva; pasta mais húmida | Espumante Brut ou Satèn; Lambrusco secco | Soave, Lugana, Pinot Bianco | Berlucchi '61 Satèn; Ceci Giuseppe Verdi Dry; Allegrini Lugana |
| 24 meses | Equilibrado: manteiga, avelã, primeiros cristais | Lambrusco secco (Grasparossa); Franciacorta millesimato | Barbera; Chianti Classico; Valpolicella Classico | Ceci Otello 1813; Berlucchi '61 Nature; Montezemolo Barbera d'Alba |
| 30 meses | Sápido, umami, frutos secos, cristais | Tinto de tanino fino e estrutura (Brunello, Barolo com anos); Franciacorta Riserva | Chardonnay com estágio; Amarone | Cecchi Brunello; Montezemolo Barolo Monfalletto; Berlucchi Palazzo Lana |
| 36 meses ou mais | Intenso, picante, granuloso, caldo | Amarone; Barolo evoluído | Em contraste: Passito di Pantelleria, Vin Santo, Marsala Vergine; Barolo Chinato (meditação) | Allegrini Amarone Classico; Donnafugata Ben Ryé; Pomino Vin Santo; Fontanafredda Barolo Chinato |
| Com Aceto Balsamico Tradizionale | Doce-ácido e sal | Lambrusco amabile | Amarone | Ceci Giuseppe Verdi Amabile |

**Outros queijos italianos** (curas mínimas, zonas, tipo de coalho e outras regras de produção não
verificados nesta revisão; confirmar no consorzio respetivo. Estatutos DOP/IGP na tabela a seguir):

| Queijo | Perfil | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|---|
| Grana Padano (jovem a Riserva) | Como o Parmigiano, mais suave | Lambrusco secco; Franciacorta; Soave (jovem) | Valpolicella Superiore, Ripasso (curado) | | Ceci; Berlucchi; Allegrini Valpolicella |
| Pecorino Romano | Muito salgado, picante | Tinto frutado e ácido (Cesanese, Montepulciano, Cannonau) | Branco estruturado (Frascati Superiore, Trebbiano) | Brancos leves | Masciarelli Montepulciano; Gianni Masciarelli Trebbiano |
| Pecorino toscano fresco / curado | Doce e lático / sápido | Vernaccia, Vermentino / Chianti Classico Riserva, Brunello | Rosso di Montalcino | | Cecchi Chianti Classico; Brunello |
| Pecorino sardo, fiore sardo | Ovelha, fumado (fiore) | Cannonau | Carignano Riserva | | Sella&Mosca Cannonau‡ |
| Pecorino siciliano, Ragusano, caciocavallo | Pasta filata curada, picante | Nero d'Avola; Aglianico | Marsala Vergine com os mais velhos | | Donnafugata Sherazade e Mille e una Notte; Feudi Taurasi |
| Gorgonzola dolce | Cremoso, azul suave | Moscato d'Asti; Lambrusco amabile | Franciacorta Satèn; Passito | Tintos tânicos | Fontanafredda Asti; Ceci Giuseppe Verdi Amabile |
| Gorgonzola piccante | Azul intenso, salgado | Passito di Pantelleria; Recioto della Valpolicella; Sagrantino Passito | Amarone; Marsala | Brancos secos leves | Donnafugata Ben Ryé; Allegrini Amarone |
| Taleggio | Casca lavada, aroma forte, pasta macia | Franciacorta Brut ou millesimato | Langhe Nebbiolo; Gewürztraminer; Lugana | Tintos muito tânicos | Berlucchi '61 Nature; Fontanafredda Ebbio; Joseph Gewürztraminer\* |
| Burrata | Cremosa, lática, doce | Fiano, Falanghina, Greco jovem, Vermentino, Lugana | Rosato do Sul; Pas Dosé | Madeira, tanino | Feudi Fiano di Avellino e Falanghina; Allegrini Lugana; Donnafugata Rosa |
| Mozzarella di bufala | Lática, ácida, húmida | Falanghina, Greco | Prosecco Brut; rosato; Asprinio d'Aversa (não no catálogo) | Tintos | Feudi Falanghina e Greco di Tufo (o produtor sugere o Greco com queijos frescos e peixe **[15]**) |
| Stracciatella | Como a burrata, mais untuosa | Fiano; Franciacorta Satèn | Grillo | Tintos | Feudi Fiano; Berlucchi '61 Satèn |
| Asiago fresco / d'allevo stravecchio | Suave e lático / sápido e picante | Soave, Pinot Grigio / Valpolicella Superiore, Ripasso, Amarone | Bardolino | | Pasqua Soave‡; Pasqua Ripasso‡; Allegrini Amarone |
| Provolone dolce / piccante | Suave / intenso | Falanghina, Barbera leve / Aglianico, Primitivo | Montepulciano Riserva | | Feudi Falanghina; Rubrato; Baglio al Sole Primitivo |
| Fontina (e fonduta) | Doce, derretida | Nebbiolo; Chardonnay de montanha | Barbaresco com trufa | Tintos muito tânicos com a fonduta | Montezemolo Langhe Nebbiolo |
| Montasio | Doce a sápido | Friulano, Ribolla | Refosco (curado) | | Jermann Vintage Tunina; Blau & Blau |
| Castelmagno | Esfarelado, intenso | Barolo | Barbaresco | | Barolo do catálogo |
| Robiola, Stracchino | Fresco, ácido | Arneis, Erbaluce, Franciacorta | Prosecco Brut | Tintos | Montezemolo Langhe Arneis |
| Ricotta fresca / ricotta salata | Doce, lática / salgada | Soave, Vermentino, Prosecco / Grillo | | Tintos | Donnafugata SurSur |
| Scamorza affumicata | Fumada | Pinot Nero; Lambrusco secco | Lagrein | Brancos muito leves | Jermann Red Angel |

**Estatuto na UE dos queijos italianos citados** (número de processo eAmbrosia **[22]**):

| Queijo | Estatuto | N.º eAmbrosia |
|---|---|---|
| Parmigiano Reggiano | DOP | PDO-IT-0016 |
| Grana Padano | DOP | PDO-IT-0011 |
| Pecorino Romano | DOP | PDO-IT-0017 |
| Pecorino Toscano | DOP | PDO-IT-0020 |
| Pecorino Sardo | DOP | PDO-IT-0018 |
| Fiore Sardo | DOP | PDO-IT-0007 |
| Gorgonzola | DOP | PDO-IT-0010 |
| Taleggio | DOP | PDO-IT-0025 |
| Fontina | DOP | PDO-IT-0008 |
| Asiago | DOP | PDO-IT-0001 |
| Montasio | DOP | PDO-IT-0012 |
| Castelmagno | DOP | PDO-IT-0006 |
| Robiola di Roccaverano | DOP | PDO-IT-0024 |
| Toma Piemontese | DOP | PDO-IT-0026 |
| Provolone Valpadana | DOP | PDO-IT-0021 |
| Provolone del Monaco | DOP | PDO-IT-0466 |
| Caciocavallo Silano | DOP | PDO-IT-0003 |
| Ragusano | DOP | PDO-IT-1505 |
| Mozzarella di Bufala Campana | DOP | PDO-IT-0014 |
| Mozzarella di Gioia del Colle | DOP | PDO-IT-02384 |
| **Burrata di Andria** (menu Emporio) | **IGP** | PGI-IT-01393 |
| Squacquerone di Romagna | DOP | PDO-IT-0794 |
| Aceto Balsamico Tradizionale di Modena (não é queijo; acompanha o Parmigiano) | DOP | PDO-IT-1565 |

"Burrata", "stracciatella", "ricotta", "scamorza" e "mozzarella" sem denominação são nomes genéricos:
só a Burrata di Andria tem IGP. Não afirmar "DOP" num queijo sem confirmar no rótulo.

### 6.15 Sobremesas italianas

Regra: **o vinho tem de ser pelo menos tão doce como a sobremesa**; a intensidade da sobremesa pede a
intensidade do vinho (Moscato d'Asti para leve e fresco; passito e Vin Santo para denso e de frutos
secos; Barolo Chinato ou Recioto para chocolate).

| Sobremesa | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|
| Tiramisù clássico (café, cacau, mascarpone, ovo) | Moscato d'Asti ou Asti (frescura contra a gordura) | Passito di Pantelleria; Marsala Superiore Dolce; Barolo Chinato (liga ao café e ao cacau) | Brut, tintos secos | Fontanafredda Asti; Donnafugata Ben Ryé; Fontanafredda Barolo Chinato |
| Tiramisù com amaretto / com frutos vermelhos | Vin Santo ou passito (amêndoa) / Brachetto d'Acqui, Lambrusco amabile | Moscato di Pantelleria | Brut | Pomino Vin Santo; Ben Ryé; Ceci Rosato Amabile |
| Cannoli siciliani | Passito di Pantelleria; Malvasia delle Lipari | Moscato di Pantelleria; Marsala | Espumantes secos | Donnafugata Ben Ryé e Kabir |
| Cassata | Passito di Pantelleria | Moscato di Noto ou Siracusa | | Donnafugata Ben Ryé |
| Panettone | Moscato d'Asti; Asti | Recioto di Soave, Vin Santo, passito leve | Brut (fica ácido) | Fontanafredda Asti; Pomino Vin Santo |
| Pandoro | Moscato d'Asti; Recioto di Soave | Asti; Prosecco Dry | Brut | Fontanafredda Asti |
| Colomba pasquale | Moscato d'Asti | Vin Santo; Recioto di Soave | Brut | Fontanafredda Asti; Pomino Vin Santo |
| Cantucci (Cantucci Toscani IGP, PGI-IT-01290 **[22]**) | Vin Santo | Moscato di Pantelleria | Tintos secos | Frescobaldi Pomino Vin Santo |
| Pastiera napoletana | Passito ou Moscato | Falanghina passita; Greco di Bianco | Brut | Donnafugata Kabir |
| Sfogliatella, babà | Moscato passito; Marsala (babà) | Moscato d'Asti | | Donnafugata Kabir |
| Panna cotta (natural / com frutos vermelhos / com caramelo) | Moscato d'Asti / Brachetto / Vin Santo ou Marsala | | Brut | Fontanafredda Asti; Pomino Vin Santo |
| Zabaione, zuppa inglese | Marsala Superiore; Moscato d'Asti | Vin Santo | | Pomino Vin Santo |
| Crostata di frutta, torta della nonna | Moscato d'Asti | Vin Santo (torta della nonna, pinhões) | | Fontanafredda Asti; Pomino Vin Santo |
| Chocolate negro, torta caprese, bonet | Barolo Chinato; Recioto della Valpolicella; Sagrantino Passito | Ben Ryé (chocolate com laranja ou alperce) | Brut, tintos secos jovens | Fontanafredda Barolo Chinato |
| Chocolate de leite, gianduia | Brachetto; Moscato passito | Barolo Chinato | Brut | Ben Ryé |
| Semifreddo al torrone, nougat | Passito; Vin Santo | Moscato d'Asti | | Ben Ryé; Pomino Vin Santo |
| Gelato e sorbetto | Normalmente nenhum vinho; Moscato d'Asti com sorvete de fruta | Affogato: grappa ou amaretto | Tintos | Fontanafredda Asti |

**Vinhos doces do catálogo por intensidade (juízo):** Fontanafredda Asti (o mais leve, bolha, fruta) →
Donnafugata Kabir (Moscato di Pantelleria, de Zibibbo **[23]**; doce aromático) → Frescobaldi Pomino Vin
Santo (oxidativo, frutos secos; castas não verificadas) → Donnafugata Ben Ryé (Passito di Pantelleria de
uvas Zibibbo passificadas; a crítica descreve alperce, figo e mel **[23]**) → Fontanafredda Barolo Chinato
(tinto aromatizado, quina, para chocolate e café). Graduações e açúcares: confirmar nas fichas de produto
(não verificado nesta revisão).

### 6.16 Legumes e ingredientes difíceis

| Ingrediente | Problema | Solução | Evitar |
|---|---|---|---|
| Alcachofra | Torna os vinhos doces e metálicos (efeito atribuído à cinarina; não verificado) | Brancos secos, salinos, ácidos, sem madeira (Pecorino, Vermentino, Grillo, Sauvignon); espumante Extra Brut ou Pas Dosé | Tintos tânicos, madeira |
| Espargos | Vegetal e sulfuroso | Sauvignon, Verdicchio, brancos alpinos de acidez alta; espumante seco | Tintos, madeira |
| Beringela grelhada ou frita | Amarga e oleosa | Rosato; Nero d'Avola sem madeira; Aglianico jovem com parmigiana | Brancos neutros leves |
| Pimento assado / recheado | Doce, fumado | Rosato; Grillo; Vermentino; Cerasuolo | Tintos muito tânicos |
| Radicchio, puntarelle, cime di rapa, rúcula | Amargo | Tintos frutados e leves (Valpolicella, Bardolino), rosati, brancos frutados | Tanino e madeira |
| Espinafres, acelgas | Mineral, ligeiramente metálico | Brancos ácidos (Verdicchio, Greco) | Tintos tânicos |
| Cebola caramelizada, abóbora | Doce | Branco com textura (Lugana, Fiano), Extra Dry, Lambrusco amabile | Brut muito seco |
| Azeitonas, alcaparras | Sal e amargo | Espumante seco; Vermentino; rosato | Tintos tânicos |
| Alho cru, aïoli | Picante e persistente | Branco com corpo (Fiano, Greco); rosato | Brancos delicados |
| Ervas frescas (manjericão, hortelã) | Aromas verdes | Vermentino, Sauvignon, Pecorino | Tintos pesados |
| Leguminosas (grão, lentilhas, feijão) | Terrosas, amido | Tintos médios (Montepulciano, Chianti, Montefalco Rosso); Chardonnay com textura | Brancos leves |
| Ovo (gema líquida, frittata) | Reveste a boca, metálico com tanino | Espumante com estágio; branco estruturado | Tintos tânicos |
| Vinagre e citrinos (saladas, marinados) | Acidez muito alta | Vinho de acidez muito alta (Verdicchio, Pecorino, Extra Brut) | Tintos, brancos moles |

### 6.17 Métodos de confeção

| Técnica | Efeito no prato | Vinho que funciona (juízo) |
|---|---|---|
| Cru e marinado | Delicado, ácido | Brancos salinos, Pas Dosé, rosé |
| Vapor, cozido, escalfado | Delicado, húmido | Brancos leves a médios |
| Grelhado, brasa | Carvão, caramelização, amargo ligeiro | Tintos com estrutura e madeira (carne); rosati e tintos leves (peixe) |
| Frito, panado, tempura | Gordura, crocante | Espumante seco, brancos ácidos, Lambrusco |
| Assado no forno | Concentração, crosta | Tintos médios a estruturados; brancos com estágio (aves, peixe) |
| Estufado, braseado, cozedura longa | Gelatina, profundidade, umami | Tintos estruturados, appassimento, Aglianico, Nebbiolo |
| Fumado | Fumo, sal | Pinot Nero, Syrah, Lagrein, Gewürztraminer, espumante Rosé |
| Gratinado, natas, manteiga | Gordura láctea | Chardonnay com estágio, Satèn, Fiano |

---

## 7. Cozinha portuguesa com vinhos italianos

(prática profissional; os exemplos do catálogo seguem as harmonizações registadas nas fichas internas e
nos ficheiros de região. Os queijos portugueses da secção 7.11 são DOP, com número eAmbrosia **[22]**;
as regras de produção de cada um não foram verificadas nesta revisão.)

### 7.1 Porque funciona e como vender

- A cozinha portuguesa é de **azeite, alho, sal, peixe, marisco, porco, arroz e coentros**, muitas vezes
  com gordura generosa. Os vinhos italianos de **acidez alta, pouca madeira e perfil gastronómico** são
  uma resposta natural.
- **Analogias que o cliente português entende (juízo, sem valor de equivalência):**
  - Lambrusco secco e Franciacorta ↔ espumante da Bairrada com o leitão.
  - Nebbiolo e Aglianico ↔ Baga (acidez, tanino firme, precisa de comida).
  - Vermentino, Greco, Falanghina ↔ brancos de marisco (Arinto, Alvarinho jovem).
  - Fiano, Lugana, Chardonnay com estágio ↔ Encruzado, Alvarinho com estágio.
  - Montepulciano d'Abruzzo, Primitivo, Nero d'Avola ↔ tinto alentejano jovem e macio.
  - Amarone ↔ grandes tintos concentrados do Douro.
  - Cerasuolo d'Abruzzo ↔ um rosado com corpo, "quase tinto", para a mesa.
- **Frase de venda:** "Este vinho faz ao [prato] o que um [vinho português] faria, com uma história
  italiana para contar à mesa."

### 7.2 Bacalhau

| Prato | O que manda | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|---|
| Bacalhau à Brás | Ovo, batata palha (gordura, crocante), cebola, sal, azeitona | Branco médio com acidez: Lugana, Langhe Arneis, Grillo, Grechetto | Franciacorta Brut ou Satèn; Soave Classico | Tintos tânicos (ovo) | Allegrini Lugana; Montezemolo Langhe Arneis; Donnafugata SurSur; Caprai Grecante |
| Bacalhau com natas | Natas, béchamel, gratinado | Branco com estrutura e estágio: Chardonnay, Fiano Riserva | Franciacorta Satèn; Roero Arneis | Brancos leves e neutros; tintos | Donnafugata Chiarandà; Frescobaldi Pomino Benefizio; Jermann Chardonnay; Feudi Pietracalda; Berlucchi '61 Satèn |
| Bacalhau à lagareiro (assado, azeite, alho, batata a murro) | Azeite abundante, alho, peixe carnudo | Branco com corpo e salinidade: Fiano, Greco di Tufo Riserva, Etna Bianco, Vermentino | Tinto leve e ácido para quem quer tinto: Etna Rosso; Chianti Rufina Riserva (como se faz no Norte de Portugal com tinto) | Tintos pesados e com madeira | Feudi Pietracalda e Cutizzi; Donnafugata Isolano; Sella&Mosca Cala Reala‡; Donnafugata Sul Vulcano; Frescobaldi Nipozzano Riserva |
| Bacalhau com grão (salada, azeite e vinagre, cebola, ovo, salsa) | Vinagre, azeite, leguminosa | Branco de acidez alta: Pecorino, Vermentino, Verdicchio | Cerasuolo d'Abruzzo | Tintos tânicos; brancos moles | Valori Pecorino; Castello di Semivicoli Pecorino‡; Gianni Masciarelli Cerasuolo |
| Bacalhau à Gomes de Sá | Batata, cebola, azeitona, ovo | Pecorino, Grechetto, Soave | Lugana | Tintos tânicos | Valori Pecorino; Caprai Grecante |
| Pataniscas, pastéis de bacalhau | Fritura, sal | Espumante seco: Prosecco Brut, Franciacorta, Trento | Falanghina | Tintos | Carpenè Malvolti 1868 Extra Brut; Berlucchi '61 Extra Brut e Cuvée Imperiale Satèn |
| Bacalhau espiritual | Natas, cenoura, gratinado | Chardonnay com estágio | Fiano | Tintos | Donnafugata Chiarandà |

**Ponte histórica:** o *baccalà alla vicentina* e o *baccalà mantecato* do Veneto e o *stoccafisso
all'anconetana* das Marche mostram que Itália também cozinha bacalhau: Soave, Lugana e Verdicchio são os
brancos da tradição (juízo; ver 5.5 e 5.11).

### 7.3 Polvo

| Prato | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|
| Polvo à lagareiro | Branco com corpo: Fiano, Chardonnay com estágio moderado, Greco | Tinto leve de tanino fino: Etna Rosso | Feudi Pietracalda; Donnafugata Chiarandà; Pomino Bianco; Donnafugata Sul Vulcano e Cuordilava |
| Salada de polvo (vinagre, cebola, coentros) | Vermentino, Falanghina, Gavi | Rosato | Feudi Falanghina e Serrocielo; Fontanafredda Gavi; Donnafugata Anthìlia; Donnafugata Rosa |
| Arroz de polvo (tomate, vinho tinto por vezes) | Rosato com corpo; tinto leve | Greco | Gianni Masciarelli Cerasuolo; Feudi Lacryma Christi Rosso |

### 7.4 Sardinhas assadas e peixe gordo grelhado

- **O que manda:** peixe oleoso, sal grosso, brasa, pimento assado, pão (ou broa).
- **1.ª escolha:** rosato fresco (Cerasuolo d'Abruzzo, Rosa D&G, Alìe) ou branco mediterrânico salino
  (Vermentino, Grillo).
- **Alternativas:** tinto muito leve servido a 13-14 °C (Lacryma Christi Rosso); Lambrusco rosato secco.
- **Evitar:** tintos tânicos e com madeira (sabor metálico), brancos com madeira.
- **No catálogo:** Gianni Masciarelli Cerasuolo; Masciarelli Rosato; Donnafugata Rosa; Frescobaldi Alìe
  Rosé; Barone di Bernaj Grillo; Aragosta Vermentino‡; Pasqua 11 Minutes Rosé‡; Feudi Lacryma Christi
  Rosso.

### 7.5 Marisco: arroz de marisco, cataplana, amêijoas, caldeirada

| Prato | O que manda | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|---|
| Arroz de marisco (tomate, coentros, caldo, malagueta) | Iodo, tomate, caldo, textura malandrinha | Greco di Tufo, Vermentino, Fiano | Cerasuolo d'Abruzzo (tomate); Franciacorta Satèn ou millesimato | Feudi Greco di Tufo e Cutizzi; Cala Reala‡; Gianni Masciarelli Cerasuolo; Berlucchi '61 Satèn |
| Cataplana de peixe e marisco (tomate, pimento, cebola, coentros) | Tomate, pimento, caldo | Etna Bianco, Greco, Pecorino, Lugana | Rosato | Donnafugata Isolano; Feudi Greco di Tufo; Castello di Semivicoli‡; Pasqua Lugana‡ |
| Carne de porco à alentejana (porco e amêijoa) | Porco frito, amêijoa, coentros | Rosato com corpo; tinto leve | Greco | Gianni Masciarelli Cerasuolo; Feudi Lacryma Christi Rosso; Donnafugata Sherazade |
| Amêijoas à Bulhão Pato | Alho, azeite, coentros, limão, iodo | Falanghina, Vermentino, Grechetto, Arneis | Franciacorta Extra Brut; Lugana | Feudi Falanghina e Serrocielo; Caprai Grecante; Montezemolo Langhe Arneis; Berlucchi '61 Extra Brut |
| Marisco cozido (camarão, sapateira, santola) | Doce do marisco, sal | Espumante seco; Vermentino | Prosecco Superiore Brut | Berlucchi '61 Nature Blanc de Blancs; Carpenè Malvolti 1868 Extra Brut |
| Ostras | Iodo | Pas Dosé; Extra Brut | Vermentino | Berlucchi '61 Nature; Bellavista Non Dosato\* |
| Caldeirada | Peixes variados, tomate, batata, pimento | Rosato com corpo; tinto leve fresco | Verdicchio | Gianni Masciarelli Cerasuolo; Feudi Lacryma Christi Rosso; Donnafugata Rosa |

### 7.6 Leitão da Bairrada

- **O que manda:** pele estaladiça, gordura, pimenta, molho de alho e pimenta.
- **1.ª escolha:** espumante de metodo classico Brut, Extra Brut ou Rosé (a mesma lógica do espumante
  da Bairrada), ou Lambrusco secco (bolha, acidez e fruta vermelha).
- **Alternativas:** Prosecco Superiore Extra Brut; tinto de acidez viva e tanino firme para quem prefere
  tinto (Etna Rosso, Aglianico jovem, Cannonau).
- **No catálogo:** Berlucchi '61 Extra Brut, '61 Rosé e '61 Nature Rosé; Fontanafredda Alta Langa;
  Carpenè Malvolti 1868 Extra Brut; Ceci Otello 1813 e Giuseppe Verdi Dry; Albinea Canali Ottocento Nero;
  Donnafugata Sul Vulcano; Feudi Rubrato; Sella&Mosca Cannonau‡.
- **Argumento de venda:** "o porceddu sardo é o leitão italiano, e em Itália bebe-se Cannonau com ele"
  (ver 5.18).

### 7.7 Cabrito e borrego assados

- **O que manda:** carne rica e gelatinosa, gordura, ervas (alecrim, louro), batata assada.
- **1.ª escolha:** tinto estruturado de tanino firme e acidez: Barolo, Brunello, Taurasi, Sagrantino.
- **Alternativas:** Chianti Classico Riserva; Amarone (versões mais ricas, com molho escuro); Nero d'Avola
  com estágio.
- **No catálogo:** Montezemolo Barolo Monfalletto e Enrico VI; Cecchi Brunello; Frescobaldi
  Castelgiocondo; Feudi Taurasi; Caprai Sagrantino 25 Anni e Collepiano; Caprai Montefalco Rosso Riserva;
  Allegrini Amarone Classico; Donnafugata Mille e una Notte (o produtor recomenda-o com carré de
  borrego **[10]**).

### 7.8 Cozido à portuguesa

- **O que manda:** muitas carnes e enchidos (gordura, sal, fumado), couve, grão ou batata, caldo.
- **1.ª escolha:** Lambrusco secco (bolha e acidez para a gordura, tanino baixo para as couves).
- **Alternativas:** tinto macio e ácido de tanino médio (Montepulciano d'Abruzzo, Barbera, Primitivo
  servido fresco).
- **Evitar:** tintos muito tânicos e alcoólicos (a couve e o fumado endurecem-nos).
- **No catálogo:** Ceci Giuseppe Verdi Dry; Albinea Canali Ottocento Nero; Masciarelli Montepulciano
  Linea Classica; Pasqua Montepulciano Colori d'Italia‡; Baglio al Sole Primitivo; Fontanafredda
  Raimonda.

### 7.9 Arroz de pato

- **O que manda:** pato (gordura e sabor intenso), chouriço (fumado, pimentão), arroz de forno tostado.
- **1.ª escolha:** tinto médio de acidez viva: Chianti Classico, Montefalco Rosso, Barbera Superiore.
- **Alternativas:** Pinot Nero; Metodo classico Rosé; Palazzo della Torre (versão rica); Montepulciano
  d'Abruzzo (a Masciarelli aponta o Gianni Masciarelli Montepulciano até para pato à cantonesa **[11]**).
- **No catálogo:** Cecchi Chianti Classico Storia di Famiglia; Caprai Montefalco Rosso; Fontanafredda
  Papagena; Jermann Red Angel; Berlucchi '61 Rosé e '61 Nature Rosé; Allegrini Palazzo della Torre;
  Gianni Masciarelli Montepulciano.

### 7.10 Carnes do dia a dia: bitoque, francesinha, porco preto, bifanas

| Prato | O que manda | 1.ª escolha | Alternativas | Evitar | No catálogo |
|---|---|---|---|---|---|
| Bitoque (bife, ovo estrelado, molho, batata frita) | Carne grelhada, molho, gordura | Tinto macio de tanino médio: Montepulciano, Barbera, Nero d'Avola | Merlot; Montefalco Rosso | Tintos muito tânicos (ovo) | Masciarelli Montepulciano Linea Classica; Fontanafredda Raimonda; Donnafugata Sedàra; Corte Giara Merlot‡; Caprai Montefalco Rosso |
| Francesinha (carnes, queijo derretido, molho de tomate, cerveja e picante) | Molho picante, queijo, gordura | Tinto frutado, pouco tânico, fresco: Montepulciano d'Abruzzo; Lambrusco secco ou amabile | Barbera Superiore; Chianti; Primitivo fresco | Barolo, Amarone, tintos alcoólicos | Masciarelli Montepulciano Linea Classica; Ceci Otello 1813 ou Giuseppe Verdi Amabile; Fontanafredda Papagena; Cecchi Chianti; Baglio al Sole Primitivo |
| Porco preto grelhado (secretos, plumas, presas) | Gordura saborosa, brasa | Primitivo; Nero d'Avola; Montepulciano | Barbera Superiore; Etna Rosso | Brancos leves | Baglio al Sole Primitivo; Donnafugata Sedàra; Gianni Masciarelli Montepulciano |
| Bifanas, prego no pão | Molho de alho e vinho, pão | Lambrusco secco; tinto leve | Rosato | | Albinea Canali Ottocento Nero |
| Picanha, costeletão, posta mirandesa | Carne vermelha grelhada | Lote de tipo bordalês (Bolgheri), Aglianico, Brunello | Tancredi (carne vermelha e caça **[4]**) | Brancos | Campo alle Comete Stupore; Tenuta Frescobaldi di Castiglioni; Feudi Taurasi; Donnafugata Tancredi |
| Frango assado ou churrasco | Pele tostada, piri-piri opcional | Rosato; tinto macio (Sedàra) | Chardonnay com estágio (sem piri-piri) | Tintos tânicos com piri-piri | Donnafugata Sedàra (o produtor recomenda-o com frango assado e churrasco **[9]**); Gianni Masciarelli Cerasuolo |
| Chanfana, javali, caça | Molhos escuros, vinho, especiaria | Sagrantino; Aglianico; Amarone | Barolo | Tintos leves | Caprai Sagrantino; Feudi Taurasi; Allegrini Amarone |

### 7.11 Queijos portugueses

| Queijo | Perfil | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|---|
| Queijo Serra da Estrela DOP (PDO-PT-0213), amanteigado | Ovelha, cremoso, ligeiramente ácido e amargo (coalho de cardo: não verificado) | Doce em contraste: Passito di Pantelleria, Vin Santo | Branco rico com estágio; Langhe Nebbiolo; Franciacorta Satèn | Donnafugata Ben Ryé; Pomino Vin Santo; Donnafugata Chiarandà; Montezemolo Langhe Nebbiolo |
| Queijo Serra da Estrela DOP, velho (curado) | Duro, sápido, picante | Barolo, Taurasi, Sagrantino, Amarone | Franciacorta Riserva | Montezemolo Barolo Monfalletto; Feudi Taurasi; Caprai Sagrantino; Allegrini Amarone; Palazzo Lana |
| Queijo de Azeitão DOP (PDO-PT-0217) | Ovelha, amanteigado, mais intenso | Chardonnay com estágio; Franciacorta Satèn | Palazzo della Torre; Montefalco Rosso Riserva | Donnafugata Chiarandà; Pomino Bianco; Berlucchi '61 Satèn; Allegrini Palazzo della Torre |
| Queijo São Jorge DOP (PDO-PT-0267), curado | Vaca, picante, sápido | Chianti Classico Riserva; Barolo; Franciacorta Nature | Lambrusco secco de qualidade | Montezemolo Barolo Enrico VI; Berlucchi '61 Nature; Ceci Otello 1813 |
| Queijo de Nisa DOP (PDO-PT-0210), Queijo de Évora DOP (PDO-PT-0251), Queijo Serpa DOP (PDO-PT-0260): ovelha, curados | Intensos, salgados | Sagrantino; Aglianico; passito em contraste | Amarone | Caprai Sagrantino Collepiano; Feudi Taurasi; Ben Ryé |
| Queijo fresco, requeijão | Lático, doce | Prosecco Brut; Soave; Falanghina | Moscato d'Asti (com doce de abóbora) | Carpenè Malvolti 1868 Extra Brut; Feudi Falanghina; Fontanafredda Asti |
| Queijos azuis portugueses | Salgado, picante | Passito di Pantelleria | Barolo Chinato | Donnafugata Ben Ryé |

### 7.12 Doces portugueses

| Doce | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|
| Pastel de nata | Moscato d'Asti ou Asti | Moscato di Pantelleria; Vin Santo; Bellini | Fontanafredda Asti; Donnafugata Kabir; Pomino Vin Santo; Cipriani Bellini |
| Arroz doce (canela, limão) | Asti; Moscato d'Asti | Moscato di Pantelleria | Fontanafredda Asti; Donnafugata Kabir |
| Doces conventuais de ovos, açúcar e amêndoa (toucinho do céu, pão de rala, ovos moles) | Vin Santo; Moscato di Pantelleria | Passito di Pantelleria | Pomino Vin Santo; Donnafugata Kabir e Ben Ryé |
| Pão-de-ló | Vin Santo | Moscato d'Asti | Pomino Vin Santo; Fontanafredda Asti |
| Bolo-rei | Asti; Moscato d'Asti | Vin Santo | Fontanafredda Asti; Pomino Vin Santo |
| Leite-creme, pudim flan | Moscato d'Asti | Vin Santo; Marsala | Fontanafredda Asti; Pomino Vin Santo |
| Mousse ou bolo de chocolate, baba de camelo | Barolo Chinato (chocolate); Vin Santo (caramelo) | Ben Ryé | Fontanafredda Barolo Chinato; Pomino Vin Santo |
| Queijadas de Sintra, travesseiros (doçaria local, útil para eventos na zona de Sintra) | Moscato d'Asti | Vin Santo | Fontanafredda Asti; Pomino Vin Santo |

---

## 8. Formatos de catering e sequência de vinhos

(prática profissional. Quantidades por convidado, temperaturas, copos e logística estão em
`servico-e-carta-de-vinhos.md`, secções 2, 3 e 7; aqui trata-se da escolha e da ordem dos vinhos.
A Emporio Italia Catering faz eventos de 8 a 250 convidados.)

### 8.1 Regras de sequência

| Regra | Porquê | Exceções úteis |
|---|---|---|
| Leve antes de pesado | Um vinho encorpado "apaga" o seguinte se este for mais leve | Um espumante pode voltar no fim (brinde) |
| Seco antes de doce | A doçura torna ácido e amargo o vinho seco que vem a seguir | Um Extra Dry de boas-vindas antes de brancos secos funciona se houver comida entre eles |
| Branco antes de tinto | Em geral, o branco é mais leve | Um branco estruturado (Fiano Riserva, Chiarandà) pode vir depois de um tinto leve (Valpolicella) |
| Jovem antes de evoluído | O vinho evoluído precisa de atenção e de um palato não cansado | Com um queijo curado no fim, o tinto velho pode fechar |
| Menos álcool antes de mais álcool | O álcool cansa o palato | Os doces (menos álcool no Moscato d'Asti) vêm no fim pela doçura |
| Frio antes de temperatura ambiente | Ritmo de serviço e frescura | |
| Sobe a qualidade | O melhor vinho perto do prato principal | O brinde pode ser o vinho mais caro |

### 8.2 Aperitivo e boas-vindas (30 a 60 minutos)

- **Objetivo:** receber, refrescar, abrir o apetite. Comida: focaccia, grissini, taralli, azeitonas,
  lascas de Parmigiano, fritos pequenos.
- **Vinhos:** 1 espumante seco (Prosecco Brut ou Extra Brut; Franciacorta ou Trento em eventos premium);
  opção de cocktail de vinho (Bellini) e opção sem álcool (Bellini Zero‡, águas, sumos). Um Spritz ou um
  Negroni podem entrar (ver `aperitivos-digestivos-destilados.md`).
- **Extra Dry ou Brut?** Para boas-vindas sem comida ou com petiscos doces, o Extra Dry agrada a mais
  gente; com fritos, salumi e queijo, o Brut é melhor. A Villa Sandi apresenta o seu Valdobbiadene
  Prosecco Superiore Extra Dry como excelente aperitivo e bom com peixe marinado com ervas aromáticas e
  com primeiros pratos de ervas **[17]**.
- **No catálogo:** Carpenè Malvolti 1868 Extra Brut e Prosecco DOC Rosé Brut; Bolla Prosecco DOC Extra
  Dry; Villa Sandi Il Fresco Brut‡; Berlucchi '61 Extra Brut; Bellavista Alma Gran Cuvée Brut\*;
  Cipriani Bellini.

### 8.3 Cocktail volante (1,5 a 3 horas, canapés e pratos pequenos)

- **Princípio:** poucos vinhos, muito versáteis, porque os convidados comem de tudo ao mesmo tempo e
  normalmente usam um só copo.
- **Estrutura recomendada (3 ou 4 vinhos):**
  1. Espumante seco (acompanha tudo, de fritos a salumi).
  2. Branco mediterrânico com acidez e algum corpo (Greco, Vermentino, Grillo, Lugana, Falanghina).
  3. Tinto leve a médio, de tanino baixo, servido fresco (Etna Rosso, Valpolicella Classico, Chianti,
     Montepulciano d'Abruzzo), ou um **rosato** no verão.
  4. Opcional: um doce para a estação de sobremesas (Asti ou Moscato d'Asti).
- **Ordem de circulação dos canapés:** frios de peixe e vegetais → salumi e queijos → quentes de massa e
  carne → doces. Os vinhos acompanham essa ordem, mas ficam todos disponíveis.
- **Evitar:** tintos muito tânicos ou alcoólicos (cansam, mancham, não resultam com canapés de peixe);
  brancos com muita madeira; mais de 4 referências (confunde e complica a logística).
- **Proposta de catálogo (juízo):**
  - Patamar de entrada: Bolla Prosecco DOC Extra Dry; Barone di Bernaj Grillo; Masciarelli Montepulciano
    Linea Classica (ou Cantina Orsogna Coste di Moro\* e Mbettata Grillo\*).
  - Patamar médio: Carpenè Malvolti 1868 Extra Brut; Feudi Greco di Tufo ou Allegrini Lugana; Gianni
    Masciarelli Cerasuolo; Cecchi Chianti Classico Storia di Famiglia.
  - Patamar premium: Berlucchi '61 Satèn ou Bellavista Alma\*; Feudi Pietracalda ou Donnafugata Isolano;
    Donnafugata Sul Vulcano ou Montezemolo Langhe Nebbiolo.

### 8.4 Jantar sentado

Três modelos:

| Modelo | Quando | Estrutura | Nota |
|---|---|---|---|
| **3 vinhos** (clássico de evento) | Casamentos, empresas, menus de 3 a 4 pratos | Espumante (receção e entrada) → branco (peixe, massa) → tinto (carne) + doce opcional | O mais eficiente; cada vinho cobre dois pratos |
| **1 vinho por prato** | Jantares de degustação, 8 a 40 convidados, clientes conhecedores | 4 a 6 vinhos em doses de 7,5 a 10 cl (juízo) | Pede serviço treinado e copos suficientes |
| **2 vinhos para toda a refeição** | Almoços de trabalho, orçamentos contidos | Um branco com estrutura e um tinto leve a médio | Escolher os vinhos mais versáteis (ver 2.3) |

- **Regras de mesa:** servir o vinho antes de o prato chegar; nunca deixar o convidado com o copo vazio
  quando o prato está servido; tintos estruturados decantados ou abertos com antecedência; brancos e
  espumantes em balde com gelo e água.
- **Discurso de serviço:** uma frase por vinho, ligada ao prato ("o Greco di Tufo tem a salinidade que
  pede o mexilhão do risotto"). Formar a equipa com o guião da [secção 13](#13-guia-rápido-para-a-equipa-de-sala).

### 8.5 Live cooking e estações

Cada estação tem o seu vinho, servido ao lado, para que a harmonização se veja.

| Estação | Pratos-tipo | Vinho | No catálogo (exemplos) |
|---|---|---|---|
| Massa ao vivo (pasta station) | Cacio e pepe, carbonara, amatriciana, pesto | Um branco estruturado + um tinto de acidez viva | Feudi Greco di Tufo + Masciarelli Montepulciano |
| Risotto | Milanese, porcini, marisco | Franciacorta Satèn ou Lugana; Langhe Nebbiolo para os cogumelos | Berlucchi '61 Satèn; Allegrini Lugana; Montezemolo Langhe Nebbiolo |
| Crudo bar e marisco | Ostras, carpaccio, tártaro | Pas Dosé ou Extra Brut; rosé para o atum | Berlucchi '61 Nature e '61 Nature Rosé; Carpenè 1868 Extra Brut |
| Salumi e formaggi (corte ao vivo de presunto, roda de Parmigiano) | Prosciutto, mortadella, Parmigiano, burrata | Lambrusco secco + Franciacorta | Ceci Otello 1813 + Berlucchi '61 Extra Brut |
| Pizza ou focaccia | Margherita, bianca, mortadella e pistácio | Lambrusco secco; Piedirosso; Prosecco Brut | Albinea Canali Ottocento Nero; Feudi Lacryma Christi Rosso |
| Carving station (carne ao vivo) | Filetto, porchetta, roast beef | Tinto estruturado | Fontanafredda Barolo; Cecchi Brunello; Feudi Taurasi |
| Sobremesas | Tiramisù, cannoli, cantucci | Moscato d'Asti ou Asti; passito em doses pequenas | Fontanafredda Asti; Donnafugata Ben Ryé |

### 8.6 Prova de vinhos (wine tasting) com comida

- **Número de vinhos:** 5 a 8 é o ideal para uma prova comentada de 60 a 90 minutos (juízo).
- **Dose de prova:** 5 a 7,5 cl por vinho (juízo; ver contas em `servico-e-carta-de-vinhos.md` 7.1).
- **Ordem:** espumante → brancos leves → brancos estruturados → rosato → tintos leves → tintos
  estruturados → doce. Dentro de cada grupo, do mais novo ao mais velho.
- **Material:** um copo por vinho (ou pelo menos 3 copos em rotação), água sem gás, pão neutro ou
  grissini, cuspideiras, ficha de prova com o mapa de Itália, lápis.
- **Um petisco por vinho** mostra a harmonização melhor do que qualquer explicação: Prosecco com
  focaccia; Greco com mexilhão; Fiano com burrata; Lambrusco com mortadella; Chianti com salame; Barolo
  com Parmigiano 30 meses; Ben Ryé com Gorgonzola piccante.
- **Temas que vendem (juízo comercial):**
  - "Itália de norte a sul em 6 copos" (Franciacorta, Lugana, Greco, Chianti Classico, Barolo, Ben Ryé).
  - "Vinhos de vulcão" (Lacryma Christi, Greco di Tufo, Teodosio, Etna Bianco e Rosso, Ben Ryé).
  - "As bolhas de Itália" (Prosecco, Franciacorta Satèn, Alta Langa, Lambrusco, Asti).
  - "Três grandes tintos, três castas" (Nebbiolo, Sangiovese, Aglianico).
  - "Itália e Portugal, castas paralelas" (Nebbiolo e Baga, Vermentino e Arinto, Montepulciano e tinto
    alentejano, com um vinho português da Emporio como comparação quando existir).

### 8.7 Casamentos e grandes eventos

- **Brinde:** espumante seco em flûte ou, melhor, em copo de vinho branco. Para muitos convidados,
  magnum e grandes formatos dão impacto visual (formatos disponíveis em
  `servico-e-carta-de-vinhos.md` 7.1).
- **O bolo de noiva:** um bolo doce com um Brut é um erro técnico (o vinho fica ácido). Soluções: servir
  Asti ou Moscato d'Asti com o bolo; ou brindar com o Brut **antes** de cortar o bolo; ou sugerir ao
  cliente um bolo menos doce (frutas, natas leves).
- **Rotação de vinhos numa noite longa:** receção (espumante) → jantar (branco e tinto) → bolo (Asti) →
  festa (espumante ou cocktails). Não abrir tintos novos depois da meia-noite; a festa pede frescura.

### 8.8 Checklist de planeamento

1. Ler o menu final e identificar o elemento dominante de cada prato (ver secção 2).
2. Decidir o modelo (3 vinhos, 1 por prato, 2 para tudo).
3. Escolher estilos por prato e depois vinhos do catálogo, confirmando disponibilidade com
   `procurar_vinhos.py` e no Odoo.
4. Verificar a coerência da sequência (secção 8.1).
5. Calcular garrafas com a fórmula de `servico-e-carta-de-vinhos.md` 7.3.
6. Definir temperaturas, copos, baldes e gelo.
7. Escrever a ordem de serviço e a frase de sala para cada vinho.
8. Preparar um plano B: um vinho de substituição para cada referência e uma opção sem álcool.

---

## 9. Menu de catering Emporio: harmonização prato a prato

(prática profissional. Os vinhos são do catálogo; confirmar disponibilidade antes de propor. As
tabelas equivalentes em `castas.md` (secção 14), `espumantes-doces-fortificados.md` (13.2) e nos
ficheiros de região mostram as opções por família; esta secção é a proposta consolidada.)

### 9.1 Prato a prato

**1. Prosciutto di Parma & Prosciutto Crudo**
- *O que manda:* sal, gordura doce e delicada. (Prosciutto di Parma é DOP, PDO-IT-0067 **[22]**;
  "prosciutto crudo" é genérico.)
- *1.ª escolha:* Lambrusco secco (o par regional do Parma): Ceci Otello Nerodilambrusco 1813; Albinea
  Canali Ottocento Nero.
- *Alternativas:* Berlucchi '61 Satèn ou Cuvée Imperiale Satèn (premium); Bolla Prosecco Superiore
  Millesimato Extra Dry (a ligeira doçura acompanha o presunto); Feudi Falanghina del Sannio (branco).
- *Evitar:* tintos tânicos (o sal e a gordura fina não chegam para eles).
- *Frase de sala:* "Em Parma, o presunto come-se com Lambrusco: a bolha e a acidez limpam a gordura e
  deixam o doce do presunto."

**2. Mortadella, Bresaola & Coppa**
- *O que manda:* três perfis diferentes: mortadella (gordura, especiaria, pistácio), bresaola (magra,
  salgada), coppa (gordura marmoreada). Com denominação: Mortadella Bologna IGP e Bresaola della
  Valtellina IGP; a coppa só é DOP se for Coppa Piacentina **[22]**.
- *1.ª escolha:* Lambrusco secco para mortadella e coppa; Langhe Nebbiolo para a bresaola. Um só
  vinho para os três: Franciacorta ou Trento Brut.
- *No catálogo:* Ceci Giuseppe Verdi Dry; Montezemolo Langhe Nebbiolo ou Fontanafredda Ebbio;
  Berlucchi '61 Extra Brut; Ferrari Brut\* ou Conti d'Arco Trento Brut\*; Fontanafredda Raimonda
  (Barbera).
- *Evitar:* brancos leves e neutros (desaparecem com a especiaria).

**3. Parmigiano Reggiano & Burrata di Andria**
- *O que manda:* dois extremos. O Parmigiano (DOP) é salgado, umami e cristalino; a Burrata di Andria
  (IGP) **[22]** é cremosa, lática e doce.
- *1.ª escolha:* separar os dois quando for possível. Burrata: Feudi Fiano di Avellino ou Allegrini
  Lugana. Parmigiano: Lambrusco secco (24 meses) ou Allegrini Amarone Classico e Barolo (30 meses ou
  mais).
- *Um só vinho para os dois:* Franciacorta com estágio (Berlucchi '61 Nature ou Cuvée Imperiale
  Satèn) ou Greco di Tufo Cutizzi.
- *Premium:* Berlucchi Palazzo Lana Extrême Riserva com Parmigiano muito curado.
- *Evitar:* tintos tânicos com a burrata.

**4. Peperoni Ripieni & Carciofi Grigliati**
- *O que manda:* a alcachofra (torna os vinhos doces e metálicos) e o doce fumado do pimento.
- *1.ª escolha:* branco seco, herbáceo e salino, sem madeira: Donnafugata SurSur (Grillo) ou Valori
  Pecorino.
- *Alternativas:* Jermann Sauvignon; Fontanafredda Gavi; Feudi Greco di Tufo; espumante Extra Brut ou
  Pas Dosé (Berlucchi '61 Nature).
- *Evitar:* tintos tânicos e brancos com madeira.

**5. Crema di Tartufo Nero & Porcini**
- *O que manda:* aroma terroso intenso, umami, gordura do creme.
- *1.ª escolha:* Langhe Nebbiolo (Montezemolo) ou Etna Rosso (Donnafugata Sul Vulcano).
- *Alternativas:* Jermann Red Angel (Pinot Nero); Berlucchi '61 Nature Rosé ou Fontanafredda Alta
  Langa (se o momento for de bolhas); Donnafugata Chiarandà (branco).
- *Premium:* Barolo Monfalletto ou Fontanafredda Barolo del Comune di Serralunga d'Alba.
- *Evitar:* brancos leves e aromáticos.

**6. Focaccia, Grissini & Taralli**
- *O que manda:* azeite, sal, crocante; é o aperitivo.
- *1.ª escolha:* Prosecco seco: Carpenè Malvolti 1868 Extra Brut ou Villa Sandi Il Fresco Brut‡.
- *Alternativas:* Bolla Prosecco DOC Extra Dry (receção sem comida); Feudi Falanghina del Sannio ou
  Serrocielo; Cipriani Bellini (boas-vindas).
- *Evitar:* tintos estruturados logo no início.

**7. Spaghettoni Cacio e Pepe di Mare**
- *O que manda:* Pecorino (sal, gordura), pimenta, marisco (iodo).
- *1.ª escolha:* Greco di Tufo (Feudi Cutizzi) ou Fiano (Feudi Pietracalda).
- *Alternativas:* Donnafugata Isolano (Etna Bianco); Berlucchi '61 Nature Blanc de Blancs; Gianni
  Masciarelli Trebbiano d'Abruzzo (patamar de entrada).
- *Evitar:* tintos; brancos com muita madeira.

**8. Raviolo Amatriciano con Tartufo Nero**
- *O que manda:* acidez do tomate, gordura e sal do guanciale, umami do pecorino, aroma da trufa.
- *1.ª escolha:* Montepulciano d'Abruzzo (Gianni Masciarelli) ou Chianti Classico (Cecchi Storia di
  Famiglia).
- *Alternativas:* Donnafugata Sul Vulcano (Etna Rosso, liga à trufa); Fontanafredda Papagena (Barbera
  d'Alba Superiore); Gianni Masciarelli Cerasuolo d'Abruzzo (rosato com corpo); Antinori Peppoli\*.
- *Premium:* Marina Cvetic Montepulciano Riserva; Frescobaldi Nipozzano Riserva.
- *Evitar:* brancos leves; tintos muito tânicos e alcoólicos.

**9. Paccheri al Pistacchio e Stracciatella**
- *O que manda:* cremosidade (stracciatella), frutos secos (pistácio), gordura.
- *1.ª escolha:* Grillo (Donnafugata SurSur: a Sicília do pistácio) ou Fiano (Feudi Pietracalda).
- *Alternativas:* Donnafugata Chiarandà (volume); Berlucchi Cuvée Imperiale Satèn (bolha cremosa);
  Allegrini Lugana; Frescobaldi Pomino Bianco.
- *Evitar:* tintos tânicos; brancos muito leves.

**10. Risotto Verde con Cozze e Tartare di Tonno**
- *O que manda:* ervas (verde), iodo do mexilhão, atum cru (gordura, cor).
- *1.ª escolha:* Greco di Tufo (Feudi) ou Vermentino (Sella&Mosca Cala Reala‡, Aragosta‡).
- *Alternativas:* Carpenè Malvolti 1868 Extra Brut; Donnafugata Rosa ou Berlucchi '61 Rosé se o atum
  dominar; Valori Pecorino.
- *Evitar:* tintos tânicos; madeira.

**11. Filetto in Crosta di Speck con Porcini**
- *O que manda:* carne vermelha tenra, fumado e sal do speck, cogumelo (umami), massa folhada ou crosta.
- *1.ª escolha:* Barolo (Montezemolo Monfalletto ou Enrico VI; Fontanafredda Barolo Etichetta Platino) ou
  Brunello (Cecchi; Frescobaldi Castelgiocondo).
- *Alternativas:* Feudi Taurasi; Allegrini Amarone Classico (versão com molho escuro e rico);
  Frescobaldi Nipozzano Riserva; Donnafugata Mille e una Notte.
- *Patamar médio:* Montezemolo Langhe Nebbiolo; Caprai Montefalco Rosso Riserva; Feudi Rubrato.
- *Evento só de bolhas:* Berlucchi Palazzo Lana Extrême (Pinot Nero) ou '61 Nature Rosé.
- *Evitar:* brancos leves; tintos leves demais.

**12. Tiramisu all'Amaretto e Frutti di Bosco**
- *O que manda:* doçura, café e cacau (amargo), mascarpone (gordura), amêndoa (amaretto), frutos do
  bosque (acidez e fruta vermelha).
- *1.ª escolha:* Fontanafredda Asti (leve, fresco, para muitos convidados) ou Donnafugata Ben Ryé
  (premium, em pequenas doses; liga à amêndoa e ao alperce).
- *Alternativas:* Frescobaldi Pomino Vin Santo (amaretto); Ceci Rosato Amabile (frutos do bosque);
  Fontanafredda Barolo Chinato (café e cacau, como digestivo).
- *Evitar:* Brut e tintos secos.
- *Fora do vinho:* um Disaronno com gelo repete o amaretto (ver `aperitivos-digestivos-destilados.md`).

### 9.2 Menus prontos para propor

**A. Essencial (3 vinhos + doce opcional)**

| Momento | Pratos | Vinho |
|---|---|---|
| Receção e antipasti | Focaccia, salumi, Parmigiano e burrata, peperoni e carciofi | Carpenè Malvolti 1868 Extra Brut |
| Primi e peixe | Cacio e pepe di mare, paccheri, risotto verde | Feudi Greco di Tufo |
| Carne e trufa | Raviolo amatriciano, crema di tartufo, filetto | Gianni Masciarelli Montepulciano d'Abruzzo ou Cecchi Chianti Classico Storia di Famiglia |
| Sobremesa | Tiramisù | Fontanafredda Asti |

**B. Premium (1 vinho por momento, 6 vinhos)**

| Momento | Vinho |
|---|---|
| Receção, focaccia, salumi | Berlucchi '61 Satèn ou Bellavista Alma Gran Cuvée Brut\* |
| Parmigiano & burrata, peperoni & carciofi | Berlucchi '61 Nature Blanc de Blancs |
| Cacio e pepe di mare, paccheri, risotto verde | Feudi Pietracalda (Fiano di Avellino) |
| Crema di tartufo, raviolo amatriciano | Donnafugata Sul Vulcano ou Montezemolo Langhe Nebbiolo |
| Filetto in crosta di speck | Montezemolo Barolo Enrico VI ou Frescobaldi Castelgiocondo Brunello |
| Tiramisù | Donnafugata Ben Ryé |

**C. Só bolhas (para quem pede um evento "de espumante")**

| Momento | Vinho |
|---|---|
| Receção | Villa Sandi Il Fresco Brut‡ ou Carpenè Malvolti 1868 Extra Brut; Cipriani Bellini |
| Salumi, Parmigiano | Lambrusco secco (Ceci Otello 1813) e Berlucchi '61 Satèn |
| Peixe e marisco | Berlucchi '61 Nature Blanc de Blancs; Ferrari Perlé\* |
| Trufa, raviolo, filetto | Berlucchi '61 Nature Rosé; Fontanafredda Alta Langa; Palazzo Lana Extrême |
| Tiramisù | Fontanafredda Asti |

**D. Norte contra Sul (evento temático com duas linhas de vinhos)**

| Prato | Norte | Sul |
|---|---|---|
| Salumi | Ceci Otello 1813 (Emilia) | Feudi Falanghina del Sannio (Campania) |
| Burrata e Parmigiano | Allegrini Lugana (Veneto) | Feudi Fiano di Avellino (Campania) |
| Cacio e pepe di mare | Fontanafredda Gavi (Piemonte) | Donnafugata Isolano (Etna) |
| Paccheri al pistacchio | Berlucchi Cuvée Imperiale Satèn (Lombardia) | Donnafugata SurSur (Sicília) |
| Raviolo amatriciano | Fontanafredda Papagena (Piemonte) | Donnafugata Sul Vulcano (Etna) |
| Filetto | Montezemolo Barolo Monfalletto (Piemonte) | Feudi Taurasi (Campania) |
| Tiramisù | Fontanafredda Asti (Piemonte) | Donnafugata Ben Ryé (Pantelleria) |

---

## 10. Vegetariano e vegano

### 10.1 Princípios (prática profissional)

- **Sem proteína animal, o tanino fica mais áspero.** Com pratos vegetais, prefere brancos, rosati,
  espumantes e tintos de tanino baixo a médio. Os grandes tintos tânicos só com pratos vegetais muito
  ricos (cogumelos, leguminosas estufadas, queijo curado, se o cliente for vegetariano e comer queijo).
- **O umami vegetal** (cogumelos, tomate seco, miso, molho de soja, levedura nutricional, algas) tem o
  mesmo efeito do umami animal: endurece taninos e amargor (ver 3.6).
- **Leguminosas e cereais** (grão, lentilhas, feijão, farro, cevada) pedem tintos médios e terrosos ou
  brancos com textura.
- **Legumes grelhados e assados** (beringela, pimento, courgette, abóbora, cebola) gostam de rosato e de
  tintos leves; os grelhados com fumo aceitam Nero d'Avola ou Montepulciano jovem.
- **Legumes verdes e herbáceos** (espargos, ervilhas, favas, alcachofra, espinafres) pedem brancos
  secos, ácidos e sem madeira (ver 6.16).
- **Queijos "italianos" e vegetarianismo:** o Parmigiano Reggiano, o Grana Padano e o Pecorino Romano
  são tradicionalmente feitos com coalho animal, pelo que muitos vegetarianos não os comem (não
  verificado nesta revisão; confirmar nos disciplinari). Num menu vegetariano, perguntar ao chefe que
  queijo usa, porque isso muda o prato e o vinho.
- **Alguns produtores já apontam os seus brancos para pratos vegetais:** a Donnafugata recomenda o
  SurSur (Grillo) com pratos vegetarianos **[6]**, o Anthìlia com tarte de legumes **[5]** e o Chiarandà
  com sopa cremosa de legumes e leguminosas **[8]**; a Masciarelli inclui legumes da época nas
  harmonizações do Gianni Masciarelli Cerasuolo d'Abruzzo **[12]**.

### 10.2 Tabela de pratos vegetarianos e veganos (prática profissional)

| Prato | 1.ª escolha | Alternativas | No catálogo |
|---|---|---|---|
| Parmigiana di melanzane (vegetariana) | Aglianico jovem; Nero d'Avola sem madeira | Cerasuolo d'Abruzzo | Feudi Rubrato **[14]**; Donnafugata Sherazade |
| Caponata | Frappato ou Nero d'Avola leve; Grillo | Rosato | Donnafugata Sherazade e SurSur |
| Risotto de legumes ou de espargos | Sauvignon; Verdicchio; Pecorino | Prosecco Extra Brut | Jermann Sauvignon; Valori Pecorino |
| Massa com pesto (sem queijo, versão vegana) | Vermentino; Gavi | Grillo | Vermentino‡; Fontanafredda Gavi |
| Massa alla Norma | Nero d'Avola sem madeira | Cerasuolo d'Abruzzo | Donnafugata Sherazade |
| Cogumelos (risotto, polenta, estufado) | Langhe Nebbiolo; Pinot Nero; Etna Rosso | Chardonnay com estágio | Montezemolo Langhe Nebbiolo; Jermann Red Angel; Donnafugata Sul Vulcano |
| Lasanha de legumes, lasanha vegana de lentilhas | Sangiovese jovem; Montepulciano | Barbera | Cecchi Chianti; Masciarelli Montepulciano Linea Classica |
| Minestrone, ribollita, sopa de grão | Chianti jovem; Montepulciano | Fiano (sopas cremosas) | Cecchi Chianti; Castiglioni Chianti; Donnafugata Chiarandà |
| Legumes grelhados e hummus | Rosato; Grillo | Pecorino | Donnafugata Rosa; Barone di Bernaj Grillo |
| Curry vegetal suave | Gewürztraminer; rosato; Prosecco Extra Dry | Lambrusco amabile | Joseph Gewürztraminer\*; Bolla Prosecco DOC Extra Dry |
| Tofu salteado com soja e gengibre | Prosecco Extra Dry; Metodo classico Rosé | Pinot Grigio | Bolla Prosecco DOC Extra Dry; Berlucchi '61 Rosé |
| Hambúrguer vegetal, "carne" vegetal | Tinto macio de tanino baixo | Lambrusco secco | Donnafugata Sedàra; Ceci Otello 1813 |
| Pizza vegana (tomate, legumes, sem queijo) | Piedirosso; rosato | Falanghina | Feudi Lacryma Christi Rosso; Gianni Masciarelli Cerasuolo |
| Burrata ou mozzarella com tomate (vegetariano) | Fiano; Falanghina | Rosato | Feudi Fiano di Avellino; Falanghina |

### 10.3 Vinhos veganos: o que diz a lei e o que perguntar ao produtor

- **Porque um vinho pode não ser vegano:** na clarificação (colagem) podem usar-se agentes de origem
  animal. O Regulamento Delegado (UE) 2019/934, Anexo I, Parte A, Quadro 2, ponto 5 ("agentes de
  clarificação"), autoriza entre outros **[2]**:
  - de origem animal: **gelatina alimentar** (5.1), **cola de peixe** (*isinglass*, 5.5), **caseína**
    (5.6), **caseinatos de potássio** (5.7) e **albumina de ovo** (5.8);
  - de origem não animal: **proteínas de trigo, de ervilha e de batata** (5.2 a 5.4), **bentonite**
    (5.9), **dióxido de silício** (5.10), **caulino** (5.11), **taninos** (5.12), **quitosano** e
    **quitina-glucano** derivados de *Aspergillus niger* (o quitosano também de *Agaricus bisporus*)
    (5.13 e 5.14), **extratos proteicos de leveduras** (5.15) e **PVPP** (polivinilpolipirrolidona,
    5.16).
- **Alergénios no rótulo:** quando tem de ser indicada a presença de produtos à base de ovo ou de leite,
  o Regulamento Delegado (UE) 2019/33 fixa os termos a usar. Em português: "ovo", "proteína de ovo",
  "produto de ovo", "lisozima de ovo" ou "albumina de ovo"; "leite", "produtos de leite", "caseína de
  leite" ou "proteína de leite". Em italiano: "uovo", "proteina dell'uovo", "derivati dell'uovo",
  "lisozima da uovo" ou "ovoalbumina"; "latte", "derivati del latte", "caseina del latte" ou "proteina del
  latte" **[1]**.
- **Ingredientes e alergénios no rótulo do vinho:** desde 8 de dezembro de 2023 aplicam-se ao vinho a
  lista de ingredientes e a declaração nutricional. A lista de ingredientes pode ser dada por meio
  eletrónico (por exemplo, código QR), mas os alergénios têm de aparecer no próprio rótulo, com a palavra
  "contém" seguida do nome da substância **[20]**. Os sulfitos são alergénio de declaração obrigatória
  acima de 10 mg/l de SO₂ total **[3]**. O limiar a partir do qual o ovo e o leite usados na colagem têm
  de ser declarados não foi verificado nesta revisão; ver `servico-e-carta-de-vinhos.md` (secção 16).
- **"Vegano" no rótulo:** o Regulamento (UE) n.º 1169/2011 prevê que a Comissão adote atos de execução
  sobre a informação voluntária relativa à adequação de um alimento a vegetarianos ou veganos (art. 36.º,
  n.º 3, alínea b)) **[3]**. Se esses atos já foram adotados não foi verificado nesta revisão. Na prática,
  as menções "vegan" nos rótulos são normalmente certificações privadas (não verificado).
- **O que fazer:** as fichas do catálogo Emporio **não** indicam se cada vinho é vegano. Antes de
  garantir a um cliente que um vinho é vegano, pedir confirmação escrita ao produtor (agente de
  clarificação usado na colheita em causa). Nunca afirmar "vegano" só porque o vinho é biológico: a lista
  de produtos autorizados na produção de vinho biológico (Regulamento de Execução (UE) 2021/1165,
  Anexo V, Parte D) inclui gelatina alimentar, cola de peixe, caseína, caseinatos de potássio e albumina
  de ovo, na maioria dos casos "derivados de matéria-prima biológica, se disponível" **[19]**.

---

## 11. Picante, cozinhas asiáticas e fusão

(prática profissional, exceto onde há fonte)

### 11.1 Princípios para o picante

- **O que piora:** álcool alto, tanino alto, madeira nova, acidez muito alta sem fruta, vinhos muito
  secos e austeros.
- **O que ajuda:** baixo teor alcoólico, fruta madura, **açúcar residual ligeiro** (Extra Dry, amabile,
  Moscato), bolha, temperatura fresca, aromas exuberantes que "dialogam" com as especiarias
  (Gewürztraminer, Moscato, Müller-Thurgau).
- **Graus de picante e estilo de vinho (juízo):**
  - Picante ligeiro (pimenta, gengibre, caril suave): quase todos os brancos aromáticos, rosati, Extra
    Dry, tintos leves.
  - Picante médio (malagueta fresca, piri-piri moderado, 'nduja): Lambrusco, rosato com corpo, Prosecco
    Extra Dry, Gewürztraminer, Primitivo servido fresco (se houver carne e doçura no molho).
  - Picante forte (vindaloo, Sichuan, tailandês "à tailandesa"): Moscato d'Asti, Lambrusco amabile, ou
    admitir que a cerveja e as bebidas sem álcool podem servir melhor o cliente.

### 11.2 Por cozinha

| Cozinha | Pratos | Vinho italiano | Porquê | No catálogo |
|---|---|---|---|---|
| Japonesa | Sushi, sashimi | Metodo classico Extra Brut ou Rosé; Prosecco Extra Dry | Arroz ligeiramente doce, soja, peixe cru | Berlucchi '61 Extra Brut e '61 Rosé; Bolla Prosecco DOC Extra Dry |
| Japonesa | Tempura, karaage | Franciacorta Brut; Prosecco Brut | Fritura | Berlucchi '61 Extra Brut; Carpenè 1868 Extra Brut |
| Japonesa | Yakitori com tare, teriyaki | Lambrusco secco; Pinot Nero; Etna Rosso | Molho doce e salgado, grelhado | Ceci Otello 1813; Jermann Red Angel |
| Chinesa | Dim sum, crepes, rolos | Prosecco Extra Dry; Franciacorta Rosé | Fritos e cozidos a vapor, molhos agridoces | Bolla Prosecco; Berlucchi '61 Rosé |
| Chinesa | Pato lacado (à Pequim ou à cantonesa) | Pinot Nero; Montepulciano d'Abruzzo; Lambrusco secco | Gordura, pele, molho hoisin doce | Jermann Red Angel; Gianni Masciarelli Montepulciano (a Masciarelli sugere-o com pato à cantonesa **[11]**) |
| Chinesa | Sichuan, pratos muito picantes | Lambrusco amabile; Moscato d'Asti | Doce e baixo álcool acalmam o picante | Ceci Giuseppe Verdi Amabile; Fontanafredda Asti |
| Tailandesa | Caril verde ou vermelho, pad thai | Gewürztraminer; Müller-Thurgau; Prosecco Extra Dry | Coco, lima, especiarias, doce | Joseph Gewürztraminer\* e Müller Thurgau\*; Bolla Prosecco Extra Dry |
| Vietnamita | Rolos frescos, saladas com ervas | Branco fresco e aromático; Anthìlia | Ervas, lima, molho de peixe | Donnafugata Anthìlia (o produtor sugere-o com *spring rolls* **[5]**); Jermann Sauvignon |
| Indiana e goesa | Tikka masala, korma, caril de camarão | Rosato com corpo; Gewürztraminer; branco macio | Natas, especiarias, picante médio | Gianni Masciarelli Cerasuolo; Joseph Gewürztraminer\*; Pasqua PassioneSentimento Bianco‡ |
| Indiana e goesa | Vindaloo, sarapatel, picante forte | Lambrusco amabile; Moscato d'Asti | Picante forte | Ceci Giuseppe Verdi Amabile; Fontanafredda Asti |
| Indiana | Chamuças, pakoras | Prosecco Extra Dry | Fritura e especiaria | Bolla Prosecco DOC Extra Dry |
| Coreana | Frango frito coreano, bulgogi, kimchi | Franciacorta Brut (frango); Lambrusco secco (bulgogi); rosato ou Pas Dosé (kimchi) | Doce, alho, fermentados | Berlucchi '61 Extra Brut; Ceci Otello 1813; Berlucchi '61 Nature |
| Mexicana e Tex-Mex | Tacos, fajitas, churrasco | Tinto macio de tanino baixo | Especiaria, fumo, gordura | Donnafugata Sedàra (o produtor recomenda-o com tacos Tex-Mex e churrasco **[9]**) |
| Peruana | Ceviche, tiradito | Vermentino; Sauvignon; Pas Dosé | Lima, malagueta, peixe cru | Jermann Sauvignon; Berlucchi '61 Nature |
| Médio Oriente e Magrebe | Hummus, falafel, tagine, kebab | Grillo, Pecorino (mezze); Nero d'Avola, Primitivo (tagine com fruta seca) | Especiarias doces, grão, cordeiro | Barone di Bernaj Grillo; Donnafugata Sedàra; Baglio al Sole Primitivo |
| Húngara e da Europa Central | Goulash | Montepulciano d'Abruzzo | Paprika, estufado | Gianni Masciarelli Montepulciano (goulash **[11]**) |
| Brasileira (frequente em Portugal) | Feijoada; picanha; moqueca | Montepulciano ou Lambrusco secco (feijoada); Aglianico ou Bolgheri (picanha); Fiano ou rosato (moqueca) | Gordura e feijão; carne grelhada; coco e dendê | Masciarelli Montepulciano; Feudi Rubrato; Campo alle Comete Stupore; Feudi Fiano di Avellino |
| Fusão | Poke, bao, tacos de peixe, ceviche nikkei | Rosato; Prosecco Extra Dry; Metodo classico Rosé | Mistura de doce, ácido, cru e picante | Donnafugata Rosa; Bolla Prosecco; Berlucchi '61 Rosé |

- O Anthìlia da Donnafugata é sugerido pelo produtor também com salada César, atum e *spring rolls*
  **[5]**, e a Masciarelli propõe o Gianni Masciarelli Montepulciano d'Abruzzo com goulash e pato à
  cantonesa **[11]**: os próprios produtores italianos já vendem estes vinhos para cozinhas fora de Itália.

---

## 12. Erros comuns

(prática profissional)

| Erro | Porque falha | Correção |
|---|---|---|
| Harmonizar só pela proteína ("é peixe, é branco") | Ignora o molho, a gordura, o tomate, o picante | Identificar o elemento dominante (secção 2) |
| Brut com a sobremesa ou com o bolo de noiva | O doce torna o vinho ácido e amargo | Asti, Moscato d'Asti, passito; brindar antes do bolo |
| Pedir "o mais seco" e servir Extra Dry | Extra Dry tem 12 a 17 g/l, mais do que o Brut **[1]** | Extra Brut ou Pas Dosé para quem quer secura |
| Barolo, Amarone ou Sagrantino com peixe, sushi ou marisco | Tanino alto + peixe = metálico; o vinho esmaga o prato | Branco salino, espumante, rosato, tinto leve |
| Tinto tânico com alcachofra, espargos ou radicchio | Amargo com amargo; efeito metálico | Brancos secos sem madeira, espumante Extra Brut |
| Tinto potente e alcoólico com picante | O álcool aumenta o ardor | Lambrusco, rosato, Extra Dry, Moscato d'Asti |
| Chardonnay com muita madeira com peixe cru ou pratos delicados | A madeira tapa o prato | Branco sem madeira ou espumante |
| Branco leve com estufado ou caça | O vinho desaparece | Tinto estruturado |
| Tinto a 20-22 °C no verão | Parece alcoólico e mole; estraga a harmonização | Tintos leves a 13-15 °C, médios a 15-17 °C, estruturados a 16-18 °C (orientação da skill) |
| Espumante gelado a 2-4 °C com comida | Anestesia o aroma e o sabor | 6-8 °C para Prosecco e Asti; 7-9 °C para metodo classico sem ano, incluindo o Satèn; 9-11 °C para millesimato e Riserva (orientação de `servico-e-carta-de-vinhos.md`) |
| Vinho evoluído e caro com prato de sabor agressivo | Os aromas terciários perdem-se | Guardar o Barolo velho para trufa, cogumelos e carne estufada |
| Queijo com tinto por hábito | Muitos queijos ficam melhor com branco, espumante ou doce | Seguir a tabela 6.14 |
| Chocolate negro com tinto seco | O cacau amargo e o doce tornam o tinto áspero | Barolo Chinato, Recioto, Sagrantino Passito |
| Tiramisù com espumante seco "para refrescar" | Café, cacau e açúcar arrasam o Brut | Moscato d'Asti, Asti, passito, ou um digestivo |
| Cinco ou mais vinhos num cocktail volante | Confusão, desperdício, logística difícil | 3 ou 4 vinhos versáteis |
| Mudar de vinho a cada canapé | O convidado não tem tempo nem copo | Vinhos que cobrem vários canapés |
| Esquecer a opção sem álcool e a água | Parte dos convidados fica sem alternativa | Bellini Zero‡, águas, sumos |
| Prometer "vegano" ou "sem sulfitos" sem confirmar | Informação errada ao consumidor | Pedir confirmação escrita ao produtor (secção 10.3) |
| Chamar "DOP" a qualquer burrata, mozzarella ou coppa | Só as denominações registadas têm esse estatuto | Ver as tabelas de estatuto nas secções 6.13 e 6.14 |
| Propor um vinho sem confirmar a disponibilidade | Falha na entrega | `procurar_vinhos.py` e Odoo antes de enviar a proposta |
| Afirmar como facto uma harmonização "clássica" com números ou regras não verificadas | Perda de credibilidade | Usar só factos com fonte (marcados **[n]**) em material escrito |

---

## 13. Guia rápido para a equipa de sala

(prática profissional)

### 13.1 Três perguntas antes de sugerir

1. "O que vai comer?" (e, se for um menu, "qual é o prato principal?").
2. "Prefere branco, tinto, rosé ou bolhas? Algo mais leve ou mais encorpado?"
3. "Quer um vinho para toda a refeição ou um copo para cada prato?"

### 13.2 Sugestões de reflexo (quando não há tempo)

| Se a mesa pede... | Sugere | Frase |
|---|---|---|
| Salumi e queijos para partilhar | Lambrusco secco ou Franciacorta | "Em Emilia é assim que se come o presunto: com bolha e acidez." |
| Marisco, peixe cru, fritos | Franciacorta Extra Brut, Prosecco Extra Brut, Vermentino, Greco | "Seco e salino, como o mar." |
| Massa com tomate ou pizza | Chianti, Barbera, Montepulciano, Piedirosso | "Um tinto com acidez para o tomate, sem pesar." |
| Massa com natas, burrata, pistácio | Fiano, Lugana, Satèn | "Cremoso com cremoso." |
| Trufa e cogumelos | Langhe Nebbiolo, Etna Rosso, Barolo | "O Nebbiolo cheira a sub-bosque, tal como a trufa." |
| Carne vermelha, cabrito | Barolo, Brunello, Taurasi, Amarone | "Um grande tinto precisa de uma grande carne." |
| Sobremesa | Asti, Moscato d'Asti, Ben Ryé, Vin Santo | "Um vinho doce, porque um seco ficaria ácido com a sobremesa." |
| "Um só vinho para tudo" | Franciacorta Brut ou Cerasuolo d'Abruzzo | "É o vinho que acompanha do início ao fim." |

### 13.3 Como subir de gama com naturalidade

- Mostrar duas opções do mesmo estilo em patamares diferentes: "Para o filetto temos o Langhe Nebbiolo,
  fresco e elegante, ou o Barolo, a versão mais profunda da mesma casta."
- Contar a origem: "o Greco di Tufo da Feudi vem da zona de Tufo, de solos ricos em material tufáceo"
  **[15]**; "o Ben Ryé é um Passito di Pantelleria feito com uvas Zibibbo passificadas" **[23]**.
  Confirmar na ficha do vinho antes de usar números.

---

## 14. Lacunas e onde confirmar

Durante esta revisão, a quota de pesquisa web estava esgotada e o acesso direto a sites externos
(consorzi, MASAF, eAmbrosia, EUR-Lex online, revistas) estava bloqueado pela política de rede do
ambiente. A verificação usou as cópias locais dos textos legais da UE, a lista MASAF dos vinhos DOP, os
números eAmbrosia replicados na taxonomia do Open Food Facts e os resultados de pesquisa guardados nesta
sessão de trabalho. Para fechar as lacunas, é preciso alargar o acesso de rede nas definições do ambiente
(Network access) ou fazer as confirmações manualmente.

| Tema | O que falta confirmar | Onde confirmar |
|---|---|---|
| Parmigiano Reggiano | Cura mínima de 12 meses, classes de cura e harmonizações oficiais do consorzio (o estatuto DOP está confirmado) | https://www.parmigianoreggiano.com ; disciplinare no registo eAmbrosia (PDO-IT-0016) |
| Queijos e salumi italianos DOP/IGP | Zonas, curas mínimas, tipo de coalho (os estatutos estão confirmados nas tabelas 6.13 e 6.14) | Consorzi respetivos; https://ec.europa.eu/agriculture/eambrosia/geographical-indications-register/ |
| Queijos portugueses DOP | Regras de produção (coalho de cardo, curas); o estatuto DOP está confirmado | eAmbrosia; DGADR |
| Modelo de interações prato-vinho (quadro 3.16) | Formulação exata e fonte citável | Especificação WSET Level 2 e 3; https://www.wsetglobal.com |
| Alcachofra (cinarina), umami e picante | Mecanismo e fonte citável | Literatura científica; Jancis Robinson (Oxford Companion to Wine); GuildSomm |
| Peixe com tinto tânico (sabor metálico) | Mecanismo | Literatura científica |
| "Baccalà" no Veneto = stoccafisso | Confirmar a designação e as receitas | Accademia Italiana della Cucina |
| Origem de pratos (tiramisù, carbonara, amatriciana) | Datas e origem (retirado do texto por não estar verificado) | Accademia Italiana della Cucina |
| Graus alcoólicos e açúcar dos doces do catálogo (Ben Ryé, Kabir, Pomino Vin Santo, Asti, Barolo Chinato) | Números por colheita; castas do Pomino Vin Santo | Fichas técnicas dos produtores |
| Castas do Pomino Bianco | Composição e percentagens | Ficha Frescobaldi |
| Bolla Prosecco Millesimato | Brut ou Extra Dry (a loja online e o Odoo divergem) | Odoo; ficha Bolla |
| Villa Sandi Il Fresco Brut | Harmonizações oficiais (a menção a "pratos especiados" do rascunho foi retirada por não se confirmar) | https://www.villasandi.it |
| Nomes botânicos das trufas | *Tuber magnatum*, *Tuber melanosporum* | Literatura micológica; consorzi da trufa |
| Vinhos veganos do catálogo | Agente de clarificação por vinho e colheita | Pedido escrito a cada produtor |
| Atos de execução sobre a menção "vegano" (Reg. 1169/2011, art. 36.º) | Se foram adotados | EUR-Lex |
| Limiar de declaração do ovo e do leite no vinho | Valor e método | EUR-Lex (Reg. (UE) 2019/33 e atos anteriores) |
| Harmonizações sugeridas pelos produtores sem ficha consultada (Berlucchi, Bellavista, Ferrari, Fontanafredda, Montezemolo, Allegrini, Frescobaldi, Caprai, Cecchi, Ceci, Jermann, Carpenè Malvolti, Bolla) | Recomendações oficiais | Sites e fichas técnicas dos produtores |
| Rubrato (Feudi) | A ficha consultada é a reproduzida por retalhistas | https://www.feudi.it |

---

## 15. Fontes

**Textos legais da UE** (relidos nesta revisão nas versões consolidadas guardadas localmente):

1. Regulamento Delegado (UE) 2019/33 da Comissão, de 17 de outubro de 2018 (rotulagem e apresentação no
   setor vitivinícola). Anexo III, Partes A e B: menções do teor de açúcar para espumantes e para os
   restantes vinhos (incluindo frisantes); Anexo I, Parte A: termos relativos a sulfitos, ovo e leite.
   https://eur-lex.europa.eu/eli/reg_del/2019/33/oj
2. Regulamento Delegado (UE) 2019/934 da Comissão, de 12 de março de 2019 (práticas enológicas
   autorizadas). Anexo I, Parte A, Quadro 2, ponto 5: agentes de clarificação (5.1 a 5.18).
   https://eur-lex.europa.eu/eli/reg_del/2019/934/oj
3. Regulamento (UE) n.º 1169/2011 do Parlamento Europeu e do Conselho, de 25 de outubro de 2011
   (informação aos consumidores sobre os géneros alimentícios): art. 36.º, n.º 3, alínea b) (menção
   vegetariano/vegano) e Anexo II, ponto 12 (sulfitos acima de 10 mg/l de SO₂ total).
   https://eur-lex.europa.eu/eli/reg/2011/1169/oj

**Fichas de produtores** (conferidas nos resultados de pesquisa guardados nesta sessão de trabalho;
confirmar a colheita em causa antes de citar a um cliente):

4. Donnafugata, "Tancredi Dolce&Gabbana e Donnafugata" (carnes vermelhas e caça; atum ou peixe gordo).
   https://www.donnafugata.it/en/product/tancredi-dolcegabbana-e-donnafugata/ ;
   https://www.donnafugata.it/it/i-vini/tancredi-dolce-gabbana-e-donnafugata/
5. Donnafugata, "Anthìlia" Sicilia DOC Bianco (Lucido dominante; peixe cru e frito, tarte de legumes,
   queijos frescos, carnes brancas, peixe ligeiramente fumado, crustáceos, anchovas, primeiros pratos,
   atum, salada César, *spring rolls*; 9-11 °C). https://www.donnafugata.it/en/product/anthilia/ ;
   https://www.donnafugata.it/usa/en/product/anthilia/
6. Donnafugata, "SurSur" Grillo Sicilia DOC (sanduíches gourmet, pratos vegetarianos, primeiros pratos
   de marisco, carnes brancas grelhadas, queijos frescos; 9-11 °C).
   https://www.donnafugata.it/en/product/sursur/ ;
   https://www.donnafugata.it/wp-content/uploads/2026/06/SurSur-2025-ENG.pdf
7. Donnafugata, "Sherazade" Nero d'Avola Sicilia DOC (pelo menos 6 meses em cuba e 6 em garrafa; sopas
   de peixe, pizza, esparguete com molho de tomate, roast beef; 15-16 °C).
   https://www.donnafugata.it/en/product/sherazade/ ;
   https://www.donnafugata.it/wp-content/uploads/2026/06/Sherazade-2024_EN.pdf
8. Donnafugata, "Chiarandà" Contessa Entellina DOC Chardonnay (barrica e tonneau; lagosta, sopa cremosa
   de legumes, peixe fumado, codorniz assada; peixe, carnes brancas, risotto, leguminosas, queijos de
   cura média; 11-13 °C). https://www.donnafugata.it/en/product/chiaranda/ ;
   https://www.donnafugata.it/gbr/en/product/chiaranda/2021/
9. Donnafugata, "Sedàra" Sicilia DOC Rosso (Nero d'Avola, Syrah, Merlot e outras; lasanha, frango
   assado, churrasco, tacos Tex-Mex, atum ligeiramente selado; 16-18 °C).
   https://www.donnafugata.it/en/product/sedara/
10. Donnafugata, "Mille e una Notte" Sicilia DOC Rosso (Nero d'Avola, Petit Verdot, Syrah; assados e
    estufados de carne, primeiros pratos com ragù, carré de borrego, pratos saborosos de peixe estufado;
    18 °C). https://www.donnafugata.it/en/product/mille-e-una-notte/
11. Masciarelli, "Gianni Masciarelli Montepulciano d'Abruzzo DOC" (estágio em aço; cozinha italiana de
    inverno, goulash, pato à cantonesa).
    https://www.masciarelli.it/en/i-vini/gianni-masciarelli-montepulciano-dabruzzo-doc/
12. Masciarelli, "Gianni Masciarelli Cerasuolo d'Abruzzo DOC" (100 % Montepulciano; sopas, peixe frito,
    massa fresca, legumes da época, pizza; 10-12 °C).
    https://www.masciarelli.it/en/i-vini/gianni-masciarelli-cerasuolo-dabruzzo-doc/ ;
    https://www.masciarelli.it/wp-content/uploads/2019/05/GM-Cerasuolo_eng.pdf
13. Valori (grupo Masciarelli), "Abruzzo Pecorino" (aperitivos, menus de verão, pratos de peixe do
    Adriático). https://www.vinivalori.it/en/i-vini/abruzzo-pecorino/
14. Feudi di San Gregorio, "Rubrato" Irpinia Aglianico DOC (assados de carnes vermelhas e brancas,
    parmigiana di melanzane, sartù di riso), ficha reproduzida por retalhistas:
    https://www.bevandeadomicilio.com/vino-campania/6401-irpinia-aglianico-doc-rubrato-feudi-di-san-gregorio-vino-biologico.html ;
    https://vingral.com/cantina/feudi-san-gregorio-aglianico-doc-rubrato/
15. Feudi di San Gregorio, "Greco di Tufo" DOCG (100 % Greco da zona de Tufo, solos ricos em material
    tufáceo; peixe no forno ou grelhado, entradas leves, queijos frescos).
    https://www.feudi.it/en/taste-our-wines/greco-di-tufo
16. Consorzio per la tutela del Franciacorta, disciplinare (Satèn: só uvas brancas, só Brut, menos de 5
    atmosferas). https://franciacorta.wine/it/consorzio/disciplinare/ ;
    https://franciacorta.wine/wp-content/uploads/2024/05/Disciplinare-Franciacorta-DOCG_07052024.pdf
    (conferido em `espumantes-doces-fortificados.md`; não reaberto nesta revisão).
17. Villa Sandi, "Valdobbiadene Prosecco Superiore DOCG Extra Dry" (aperitivo; peixe marinado com ervas
    aromáticas; primeiros pratos de ervas).
    https://www.villasandi.it/it_en/valdobbiadene-prosecco-extra-dry-docg.html

**Disciplinari e listas oficiais:**

18. Primitivo di Manduria DOC: açúcar residual até 18 g/l (resultado de pesquisa guardado que resume o
    disciplinare). Consorzio di Tutela del Primitivo di Manduria:
    https://www.consorziotutelaprimitivo.com/disciplinare-doc/ ; MASAF, Catalogo nazionale:
    http://catalogoviti.politicheagricole.it/scheda_denom.php?t=dsc&q=2236 ;
    https://www.agraria.org/vini/primitivo-di-manduria-doc.htm

**Texto legal adicional:**

19. Regulamento de Execução (UE) 2021/1165 da Comissão, de 15 de julho de 2021 (produtos e substâncias
    autorizados na produção biológica), Anexo V, Parte D: produtos autorizados na produção e conservação
    de produtos vitivinícolas biológicos. https://eur-lex.europa.eu/eli/reg_impl/2021/1165/oj
20. Regulamento (UE) n.º 1308/2013 (OCM), art. 119.º, na redação do Regulamento (UE) 2021/2117 (art. 1.º,
    ponto 32; aplicável desde 8 de dezembro de 2023, art. 6.º): declaração nutricional, lista de
    ingredientes, meio eletrónico e indicação dos alergénios no rótulo com "contém".
    https://eur-lex.europa.eu/eli/reg/2013/1308/oj ; https://eur-lex.europa.eu/eli/reg/2021/2117/oj
21. MASAF, "Elenco alfabetico dei vini DOP italiani" (denominações e níveis DOC/DOCG citados: Cònero DOCG,
    Rosso Cònero DOC, Castelli di Jesi Verdicchio Riserva DOCG, Romagna DOC, Contessa Entellina DOC,
    Sicilia DOC, Irpinia DOC, Cerasuolo d'Abruzzo DOC, entre outras). Cópia consultada:
    https://raw.githubusercontent.com/dentingerlenz/mywine-cellar/main/scripts/geo/phase7/sources/it_DOP.txt
22. Registo eAmbrosia da UE (indicações geográficas de géneros alimentícios), números de processo dos
    queijos, salumi, Aceto Balsamico Tradizionale di Modena e Cantucci Toscani citados:
    https://ec.europa.eu/agriculture/eambrosia/geographical-indications-register/ . Como o eAmbrosia
    estava bloqueado pela rede, os números foram conferidos na taxonomia de categorias do Open Food Facts,
    que os replica:
    https://raw.githubusercontent.com/openfoodfacts/openfoodfacts-server/main/taxonomies/food/categories.txt
    Confirmar no registo antes de citar em material para clientes.
23. Wine Enthusiast, críticas de Donnafugata Ben Ryé 2012, 2013 e 2014 (Passito di Pantelleria, "100%
    dried Zibibbo grapes"; alperce, figo, mel) e Kabir 2006 (Moscato di Pantelleria, Zibibbo), no conjunto
    de dados winemag-data-130k-v2:
    https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-05-28/winemag-data-130k-v2.csv

**Referências internas da skill** (sem valor de fonte externa): `data/catalogo.json` (harmonizações
registadas por vinho), `regioes-norte.md`, `regioes-centro.md`, `regioes-sul-ilhas.md`, `castas.md`,
`espumantes-doces-fortificados.md`, `servico-e-carta-de-vinhos.md`,
`aperitivos-digestivos-destilados.md`.
