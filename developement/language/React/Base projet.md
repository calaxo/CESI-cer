le fichier principal index.js

```js
import React from 'react'
import ReactDOM from 'react-dom/client'

import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
```

rend l'app et le defini comme la racine du dom


et le fichier app.js

```js
const App = () => (
  <div>
    <p>Hello world</p>
  </div>
)

export default App
```
on met le bout d'html qui est en fait du [[jsx]] dans la variable app
* il faut  fair export default app a lafin pout envoyer l'objet app dans l'index

[[composant]]