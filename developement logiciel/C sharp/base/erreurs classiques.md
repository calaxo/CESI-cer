
    public class Workshop
    {


        public string Methode(int v1, int v2)
        {
            public string sortie = "zob" + (v1 + v2).ToString();
            return  sortie;

        }
    }


1.	Déclaration de variable dans une méthode :
•	Erreur : La ligne public string sortie = "zob" + (v1 + v2).ToString(); contient le mot-clé public, ce qui n'est pas permis pour une variable locale dans une méthode.
•	Correction : Supprimez le mot-clé public.