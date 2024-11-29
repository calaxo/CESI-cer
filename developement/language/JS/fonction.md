definiton


```js
const sum = (p1, p2) => {
  console.log(p1)
  console.log(p2)
  return p1 + p2
}
```
avec const comme une variable

sum est le nom de la fonction
p1 et p2 les parametres

=> pour definit la fonction

la fonction est entre les crochets
et return pour renvoyer des chose

les parenthesse ne sont necesaire que quand il y a plusieurs parametre d'entrée

```js
const sum = (p1, p2) =>  "blabla"

```


appel

```js
const result = sum(1, 5)
console.log(result)
```
classique



```js
const square = p => p * p
```

simple efficace pour appeler p et renvoyer p * p direct
utile pour l'utiliser dans la methode map des [[array]]

```js
const tSquared = t.map(p => p * p)
```
fait le carre de tout les valeurs de l'array 


sinon ancienn methode pas folle mais comme en [[_C]]

```js
function product(a, b) {
  return a * b
}

const result = product(2, 6)
// result is now 12
```



```js
const average = function(a, b) {
  return (a + b) / 2
}

const result = average(2, 5)
// result is now 3.5
```

plus bizzare mais utile pour les [[objects]]

en disant que average est une fonction de a b qui fait...

