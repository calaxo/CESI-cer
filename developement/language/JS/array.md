si un array est est en const on peut quand meme modifier les valeur qu'il y a dedans


methode=



immutable data structures

concat:

```js
t.concat(5)
```

ajoute 5 a l'array x

map:

```js
t.map(value => value * 2)
```

multiplie chaque valeurs de l'array par deux

```js
t.map(value => '<li>' + value + '</li>')
```

va entourer chaque valeurs de l'array avec les balise list utile pour [[list,tableau]] d'html

desctructing assignment
destructuration

```js
const [first, second, ...rest] = t
```

first est une variable qui vaudra la premiere valeur de l'array t

comme en python avec les [[tuple]] ou pour ecrire moins de ligne de code

