

```Csharp

delegate string MethodeDelegate(int v1, int v2);
// c'est un prototypt


    Methode methodeDelegate = new Methode(MaMethode);
    methodeDelegate();

```


il faut d'abbord fair un prototype du delegate avant de le remplur

Un **delegate** est un **pointeur de fonction** : il permet de stocker une méthode dans une variable.



ya aussi des delegé multicast

qui sont des délégé(delegate) avec plusieur méthode dedans



```Csharp

LeMulticastDelegate del = leAdececode.ma;

del += leBdececode.mb;


del();

```



