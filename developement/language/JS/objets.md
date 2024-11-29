```js
const object3 = {
  name: {
    first: 'Dan',
    last: 'Abramov',
  },
  grades: [2, 3, 5, 3],
  department: 'Stanford University',
}
```

avec le titre de l'objet
et des chose dedans qui definisset des valeurs
il peut contenir tout et n'importe quoi meme d'autre objets

structure de donnés comme un [[disctonary]] de python

appeler un objet

avec un point
```js
object1.name
```

on peut sortir ou rentrer des valeur dans l'objet avec ce point

mais
```js
object1['secret number']
```

les crochet permettent de manipuler les proprieté avec  des espace 

et comme les [[class]] de python

```js
const arto = {
  name: 'Arto Hellas',
  age: 35,
  education: 'PhD',
  greet: function() {    
	  console.log('hello, my name is ' + this.name) 
  },
  }

arto.greet()  // "hello, my name is Arto Hellas" gets printed
```

greet est defini comme une propriétée classique mais s'est une fonction qui fait quelque chose et le this permet d'inquer l'objet luis meme 

```js
const referenceToAddition = arto.doAddition
```
avec ca on peut sortir le fonction doadditon de l'objet arto et l'appeler avec referencetoaddion

mais si il y avait un this dans la methode il sera perdu car il doit rester dans l'objet

ya aussi des vrai class de js mais s'est pas fou 
```js
class Person {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
  greet() {
    console.log('hello, my name is ' + this.name)
  }
}

const adam = new Person('Adam Ondra', 29)
adam.greet()

const janja = new Person('Janja Garnbret', 23)
janja.greet()
```

