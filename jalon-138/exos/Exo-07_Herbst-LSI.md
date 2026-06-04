# Exercice 7 : Le Lemme de Herbst (Niveau 7)

## Énoncé
Soit $Y$ une variable aléatoire réelle centrée ($\mathbb{E}[Y] = 0$).
Supposons que pour tout $\lambda \ge 0$, la variable aléatoire $e^{\lambda Y}$ vérifie l'inégalité log-sobolévienne suivante :
$$\text{Ent}(e^{\lambda Y}) \le \frac{\lambda^2 v}{2} \mathbb{E}[e^{\lambda Y}]$$
où $v > 0$ est une constante.
1. Soit $\phi(\lambda) = \mathbb{E}[e^{\lambda Y}]$. Exprimer l'entropie $\text{Ent}(e^{\lambda Y})$ en fonction de $\phi(\lambda)$ et de sa dérivée $\phi'(\lambda)$.
2. En déduire que la fonction $\phi$ vérifie l'inégalité différentielle suivante pour tout $\lambda > 0$ :
$$\frac{d}{d\lambda}\left( \frac{\ln \phi(\lambda)}{\lambda} \right) \le \frac{v}{2}$$
3. En intégrant cette inégalité différentielle sur l'intervalle $(0, \lambda)$, démontrer que $\phi(\lambda) \le e^{\lambda^2 v / 2}$.
4. En déduire l'inégalité de concentration associée pour tout $t > 0$ :
$$\mathbb{P}(Y \ge t) \le \exp\left( - \frac{t^2}{2 v} \right)$$

---

## Correction Détaillée

### 1. Expression de l'entropie
Par définition, l'entropie de la variable aléatoire positive $Z = e^{\lambda Y}$ est :
$$\text{Ent}(e^{\lambda Y}) = \mathbb{E}[e^{\lambda Y} \ln(e^{\lambda Y})] - \mathbb{E}[e^{\lambda Y}] \ln \mathbb{E}[e^{\lambda Y}]$$
$$\text{Ent}(e^{\lambda Y}) = \mathbb{E}[Y \lambda e^{\lambda Y}] - \mathbb{E}[e^{\lambda Y}] \ln \mathbb{E}[e^{\lambda Y}]$$
$$\text{Ent}(e^{\lambda Y}) = \lambda \mathbb{E}[Y e^{\lambda Y}] - \phi(\lambda) \ln \phi(\lambda)$$

Exprimons maintenant $\phi'(\lambda)$. En supposant que l'on puisse dériver sous le signe d'intégration (grâce aux théorèmes de régularité usuels, $Y$ étant sous-gaussienne) :
$$\phi'(\lambda) = \frac{d}{d\lambda} \mathbb{E}[e^{\lambda Y}] = \mathbb{E}[Y e^{\lambda Y}]$$

On en déduit l'expression recherchée :
$$\text{Ent}(e^{\lambda Y}) = \lambda \phi'(\lambda) - \phi(\lambda) \ln \phi(\lambda)$$

### 2. Inégalité différentielle
L'hypothèse log-sobolévienne s'écrit :
$$\text{Ent}(e^{\lambda Y}) \le \frac{\lambda^2 v}{2} \mathbb{E}[e^{\lambda Y}]$$
En injectant l'expression obtenue à la question précédente :
$$\lambda \phi'(\lambda) - \phi(\lambda) \ln \phi(\lambda) \le \frac{\lambda^2 v}{2} \phi(\lambda)$$

Puisque $\phi(\lambda) = \mathbb{E}[e^{\lambda Y}] > 0$, divisons l'inégalité par $\lambda^2 \phi(\lambda)$ pour $\lambda > 0$ :
$$\frac{\lambda \phi'(\lambda) - \phi(\lambda) \ln \phi(\lambda)}{\lambda^2 \phi(\lambda)} \le \frac{v}{2}$$
$$\frac{1}{\lambda} \frac{\phi'(\lambda)}{\phi(\lambda)} - \frac{\ln \phi(\lambda)}{\lambda^2} \le \frac{v}{2}$$

Dérivons maintenant la fonction $g(\lambda) = \frac{\ln \phi(\lambda)}{\lambda}$ par rapport à $\lambda$ pour $\lambda > 0$ :
$$g'(\lambda) = \frac{\frac{\phi'(\lambda)}{\phi(\lambda)} \lambda - \ln \phi(\lambda) \times 1}{\lambda^2} = \frac{1}{\lambda} \frac{\phi'(\lambda)}{\phi(\lambda)} - \frac{\ln \phi(\lambda)}{\lambda^2}$$

Nous constatons que le membre de gauche de notre inégalité différentielle est exactement la dérivée de $g(\lambda)$. On a donc :
$$\frac{d}{d\lambda}\left( \frac{\ln \phi(\lambda)}{\lambda} \right) \le \frac{v}{2}$$

### 3. Intégration et majoration de la transformée de Laplace
La fonction $\lambda \mapsto \frac{d}{d\lambda}\left( \frac{\ln \phi(\lambda)}{\lambda} \right)$ est bornée par $\frac{v}{2}$. Intégrons cette inégalité entre $\epsilon > 0$ et $\lambda$ :
$$\int_{\epsilon}^{\lambda} \frac{d}{du}\left( \frac{\ln \phi(u)}{u} \right) du \le \int_{\epsilon}^{\lambda} \frac{v}{2} du$$
$$\frac{\ln \phi(\lambda)}{\lambda} - \frac{\ln \phi(\epsilon)}{\epsilon} \le \frac{v}{2}(\lambda - \epsilon)$$

Étudions la limite quand $\epsilon \to 0^+$ du terme $\frac{\ln \phi(\epsilon)}{\epsilon}$. 
Puisque $Y$ est centrée et $\phi(0) = \mathbb{E}[e^{0}] = 1$, le développement limité de $\phi(\epsilon)$ en $0$ donne :
$$\phi(\epsilon) = \mathbb{E}[1 + \epsilon Y + \frac{\epsilon^2 Y^2}{2} + o(\epsilon^2)] = 1 + \epsilon \mathbb{E}[Y] + \frac{\epsilon^2 \mathbb{E}[Y^2]}{2} + o(\epsilon^2)$$
Comme $\mathbb{E}[Y] = 0$, on a $\phi(\epsilon) = 1 + \frac{\epsilon^2 \text{Var}(Y)}{2} + o(\epsilon^2)$.
D'où :
$$\ln \phi(\epsilon) = \ln\left(1 + \frac{\epsilon^2 \text{Var}(Y)}{2} + o(\epsilon^2)\right) \sim \frac{\epsilon^2 \text{Var}(Y)}{2}$$
En divisant par $\epsilon$ :
$$\lim_{\epsilon \to 0^+} \frac{\ln \phi(\epsilon)}{\epsilon} = \lim_{\epsilon \to 0^+} \frac{\epsilon \text{Var}(Y)}{2} = 0$$

En faisant tendre $\epsilon$ vers $0^+$ dans notre inégalité intégrée :
$$\frac{\ln \phi(\lambda)}{\lambda} - 0 \le \frac{v \lambda}{2} \implies \ln \phi(\lambda) \le \frac{\lambda^2 v}{2}$$
Par passage à l'exponentielle :
$$\phi(\lambda) \le \exp\left( \frac{\lambda^2 v}{2} \right)$$

### 4. Queue de distribution (Inégalité de concentration)
Par la méthode classique de Chernoff, pour tout $t > 0$ :
$$\mathbb{P}(Y \ge t) \le e^{-\lambda t} \mathbb{E}[e^{\lambda Y}] = e^{-\lambda t} \phi(\lambda) \le \exp\left( -\lambda t + \frac{\lambda^2 v}{2} \right)$$

En choisissant le paramètre optimal $\lambda^* = \frac{t}{v} > 0$ :
$$\mathbb{P}(Y \ge t) \le \exp\left( - \frac{t^2}{v} + \frac{t^2}{2 v} \right) = \exp\left( - \frac{t^2}{2 v} \right)$$

L'inégalité de concentration est formellement et rigoureusement établie.
