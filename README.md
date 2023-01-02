# python-functions

## Consignes générales

Les fonctions... en Python!

Vous allez faire 3 exercices. Pour le rendu, remplissez **uniquement les fonctions** dans les fichiers désignés, veillez bien à n'ajouter aucun autre code dans ces fichiers. Évaluez votre note en local de temps en temps (cf ci-dessous).

Pendant que vous préparez vos exercices, pouvez tester vos fonctions en utilisant la construction
`if __name__ == "__main__":`


```python
def toto(un, deux, trois):
  # votre code
  # ...

if __name__ == "__main__":
  resultat = toto("un", 2, three)
  print(resultat)
```

## Rendre votre travail

Quand le résultat pour un des exercices est satisfaisant, git add, git commit, git push:

```shell
$ git add distance.py
$ # ajoutez aussi tout autre fichier que vous voulez committer
$ git commit --message "Distance"
$ git push
```

Rendus **obligatoires**:

- `distance`
- `numbers`
- `doubler_premier`
- `compare_all`

Rendus facultatifs:

- `doubler_premier_kwds`
- `compare_args`

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.


## Exercice - `distance`


Vous devez écrire une fonction `distance` qui prend un nombre quelconque d'arguments numériques non complexes, et qui retourne la racine carrée de la somme des carrés des arguments.

Par exemple:
`distance(x1, x2, ..., xn) = sqrt(x1*x1 + x2*x2 + ... + xn * xn)`

Par convention on fixe que `distance() = 0`.

```
# ATTENTION vous devez aussi définir les arguments de la fonction
def distance(votre, signature):
    return "votre code"
```

Quelques exemples:

```python
>>> distance()
0.0
>>> distance(1)
1
>>> distance(1)
1.4142135623730951
>>> distance(1, 1, 1, 1)
2.0
```

## Exercice - `numbers`

On vous demande d'écrire une fonction `numbers`:

* qui prend en argument un nombre quelconque d'entiers,
* et qui retourne un tuple contenant
 * la somme
 * le minimum
 * le maximum
de ses arguments.

Si aucun argument n'est passé, `numbers` doit renvoyer un tuple contenant 3 entiers `0`. Quelques
exemples:

```python
>>> numbers()
(0, 0, 0)
>>> numbers(6)
(6, 6, 6)
>>> numbers(5, 5, 9)
(19, 5, 9)
```

En guise d'indice, je vous invite à regarder les fonctions *built-in* [`sum`](https://docs.python.org/3/library/functions.html#sum), [`min`](https://docs.python.org/3/library/functions.html#min) et [`max`](https://docs.python.org/3/library/functions.html#max).


## Exercice - `doubler_premier`

On vous demande d'écrire une fonction qui prend en argument :

 * une fonction `f`, dont vous savez seulement que le premier argument est numérique, et qu'elle ne prend **que des arguments positionnels** (sans valeur par défaut) ;
 * un nombre quelconque - mais au moins 1 - d'arguments positionnels `args`, dont on sait qu'ils pourraient être passés à `f`.
 
Et on attend en retour le résultat de `f` appliqués à tous ces arguments, mais avec le premier d'entre eux multiplié par deux.

Formellement : `doubler_premier(f, x1, x2,..., xn) == f(2*x1, x2,..., xn)`

+++

Voici d'abord quelques exemples de ce qui est attendu. Pour cela on va utiliser comme fonctions:

* `add` et `mul` sont les opérateurs (binaires) du module operator;
* et `distance` est la fonction de l'exercice 1

```python
>>> from operator import add, mul
>>> doubler_premier(add, 1, 4)
6
>>> doubler_premier(mul, 1, 4)
8
>>> doubler_premier(distance, 1.5, 4.0)
5.0
>>> doubler_premier(distance, 2.0, 4.0, 4.0, 4.0)
8.0
```


## Exercice - `doubler_premier_kwds`

Vous devez maintenant écrire une deuxième version qui peut fonctionner avec une fonction quelconque (elle peut avoir des arguments nommés avec valeurs par défaut).

La fonction `doubler_premier_kwds` que l'on vous demande d'écrire maintenant prend donc un premier argument `f` qui est une fonction, un second argument positionnel qui est le premier argument de `f` (et donc qu'il faut doubler), et le reste des arguments de f, qui donc, à nouveau, peuvent être nommés ou non.

```python
# avec ces deux fonctions

def add3(x, y=0, z=0):
    return x + y + z

def mul3(x=1, y=1, z=1):
    return x * y * z
```

On a les exemples suivants:

```python
>>> doubler_premier_kwds(add3, 1, 2, 3)
7
>>> doubler_premier_kwds(add3, 1, 2, z=3)
7
>>> doubler_premier_kwds(add3, 1, z=3, y=2)
7
>>> doubler_premier_kwds(mul3, 1, 2, 3)
12
>>> doubler_premier_kwds(mul3, 1, 2, 3)
12
```

Vous remarquerez que l'on n'a pas mentionné dans cette liste d'exemples:

```python
doubler_premier_kwds (muln, x=1, y=1)
```

que l'on ne demande pas de supporter puisqu'il est bien précisé que doubler_premier a deux arguments positionnels.

## Exercice - `compare_all`

On vous demande d'écrire une fonction `compare` qui prend en argument :

 * deux fonctions `f` et `g` ; imaginez que l'une d'entre elles fonctionne et qu'on cherche à valider l'autre ; dans cette version simplifiée toutes les fonctions acceptent exactement un argument ;
 * une liste d'entrées `entrees` ; vous pouvez supposer que chacune de ces entrées est dans le domaine de `f` et de `g` (dit autrement, on peut appeler `f` et `g` sur chacune des entrées sans craindre qu'une exception soit levée).

Le résultat attendu pour le retour de `compare` est une liste qui contient autant de booléens que d'éléments dans `entrees`, chacun indiquant si avec l'entrée correspondante on a pu vérifier que `f(entree) == g(entree)`.

Dans cette première version de l'exercice vous pouvez enfin supposer que les entrées ne sont pas modifiées par `f` ou `g`.

Pour information dans cet exercice :

 * `factorial` correspond à `math.factorial`
 * `fact` et `broken_fact` sont des fonctions implémentées par nos soins, la première est correcte alors que la seconde retourne 0 au lieu de 1 pour l'entrée 0.

Quelques exemples:

```python
>>> compare_all(fact, factorial, [0, 1, 5])
[True, True, True]
>>> compare_all(broken_fact, factorial, [0, 1, 5])
[False, True, True]
```

Ce qui, dit autrement, veut tout simplement dire que `fact` et `factorial` coïncident sur les entrées 0, 1 et 5, alors que `broken_fact` et `factorial` ne renvoient pas la même valeur avec l'entrée `0`.


## Exercice - `compare_args`

Nous reprenons ici la même idée que `compare_all`, mais en levant l'hypothèse que les deux fonctions attendent un seul argument. Il faut écrire une nouvelle fonction `compare_args` qui prend en entrée :

 * deux fonctions `f` et `g` comme ci-dessus ;
 * mais cette fois une liste (ou un tuple) `argument_tuples` de **tuples** d'arguments d'entrée.

Comme ci-dessus on attend en retour une liste `retour` de booléens, de même taille que `argument_tuples`, telle que, si `len(argument_tuples)` vaut `n`:

- Si `argument_tuples[i] == [a1, ..., aj]
- Alors `retour(i) == True` <=>  `f (a1, ..., aj) == g (a1, ..., aj)`

Pour information dans cet exercice :

 * `factorial` correspond à `math.factorial` ;
 * `fact` et `broken_fact` sont des fonctions implémentées par nos soins, la première est correcte alors que la seconde retourne 0 au lieu de 1 pour l'entrée 0 ;
 * `add` correspond à l'addition binaire `operator.add` ;
 * `plus` et `broken_plus` sont des additions binaires que nous avons écrites, l'une étant correcte et l'autre étant fausse lorsque le premier argument est nul.


Quelques exemples:

```python
>>> compare_args(broken_fact, factorial, [(0,), (1,), (5,)])
[False, True, True]
>>> compare_args(add, plus_broken, [(2, 3), (0, 4), (4, 5)])
[True, False, True]
```
