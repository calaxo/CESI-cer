

```js
const Hello = () => { 
	return (   
	<div>     
		<p>Hello world</p>  
	 </div>  )}
	
const App = () => {
  return (
    <div>
      <h1>Greetings</h1>
      <Hello />    </div>
  )
}
```


le composant hello est dans le composant app

on peut passer des chose entre les composant avec des props

```js
const Hello = (props) => {
  return (
    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>
    </div>
  )
}

const App = () => {
  return (
    <div>
      <h1>Greetings</h1>
      <Hello name="Maya" age={26 + 10} />
    </div>
  )
}
export default App
```

age et name sont passé dans les parametre de la balise et viennent indiquer la valeur pour props notamment pour ses enfant name et age

* les noms des composant doivent etre ecrit en majuscule pour ne pas se melanger avec le nom des objet dans le html

* il dit y avoir une div en parant dans le jsx pour specifier le parent

```js
const Hello = (props) => {

  const bornYear = () => {
    const yearNow = new Date().getFullYear()
    return yearNow - props.age
  }
  return (

    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>
      <p>So you were probably born in {bornYear()}</p>
    </div>
  )
}
const App = () => {
  const name = 'Peter'
  const age = 10
  return (
    <div>
      <h1>Greetings</h1>
      <Hello name="Maya" age={26 + 10} />
      <Hello name={name} age={age} />
    </div>
  )
}
export default App
```

dans le composant hello on a defini une fonction bornYear

dedans il y a des enfant du props appelé direct car la fonction peut y acceder



```js
const name = props.name 
const age = props.age
```

```js
<p>Hello {name}, you are {age} years old</p>
```

on peut simplifier l'ecriture avec name et age qui prennet direct ce qu'il y a dans le props

comme les [[fonctions]] en js normal


```js
const bornYear = () => new Date().getFullYear() - age

const bornYear = () => {
  return new Date().getFullYear() - age
}
```

avec un seul truc a renvoyer il n'y a pas besoin des accolades ou du return


```js
props = {
  name: 'Arto Hellas',
  age: 35,
}


```


```js
  const { name, age } = props
```

name et age on direct les valeurs

```js
const Hello = (props) => {
  const { name, age } = props
  ...
}
```

```js
const Hello = ({ name, age }) => {...}
```
plus besoin d'appeler l'onjet props


```js
const refresh = () => {

  ReactDOM.createRoot(document.getElementById('root')).render(

    <App counter={counter} />

  )

}

setInterval(() => {

  refresh()

  counter += 1

}, 1000)
```

la fonction serintervalle s'esxecute tout les une seconde et fait un refresh et un increment


car la methode pour render a eter mis dans une fonction refresh pour que ca soit plus simple


et le app js

```js
const App = (props) => {

  const {counter} = props

  return (

    <div>{counter}</div>

  )

}

  

export default App
```

qui affiche juste le compteur