# Exercice 8 : Espace d'Ultramétrie
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé formel
Une distance $d$ est dite ultramétrique si elle vérifie l'inégalité forte : $d(x,z) \le \max(d(x,y), d(y,z))$. Dans un tel espace, montrer que tout triangle est isocèle et que sa base est inférieure aux côtés égaux.

## Résolution pas à pas
**Étape 1 : Formulation du problème**

Soit $x, y, z$ trois points distincts formant un triangle topologique. Supposons sans perte de généralité que les trois distances ne sont pas égales, et qu'il y a une distance strictement supérieure aux autres, disons $d(x,z) > d(x,y)$ et $d(x,z) > d(y,z)$.

**Étape 2 : Contradiction par l'ultramétrie**

Selon l'inégalité ultramétrique :
$d(x,z) \le \max(d(x,y), d(y,z))$.
Or, notre hypothèse implique que le maximum à droite est strictement inférieur à $d(x,z)$.
Nous obtenons une contradiction évidente : un réel ne peut pas être strictement inférieur à lui-même.

**Étape 3 : Conclusion**

L'hypothèse selon laquelle une distance puisse être l'unique maximum est fausse. Par conséquent, les deux plus grandes distances du triangle doivent être exactement égales. Le triangle est donc toujours isocèle, et le troisième côté (la base) est nécessairement inférieur ou égal à ces deux côtés. Cette propriété fascinante régit les distances $p$-adiques en arithmétique. $\blacksquare$
