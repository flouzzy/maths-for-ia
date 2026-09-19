---
title: "Exercice 4 : Application des Inégalités"
difficulty: "★★★☆☆"
---

# Exercice 4 : Application des Inégalités

**Niveau :** ★★★☆☆

**Énoncé :**
Montrer l'inégalité de Hölder généralisée pour 3 fonctions : si $\frac{1}{p} + \frac{1}{q} + \frac{1}{r} = 1$, alors $\|fgh\|_1 \le \|f\|_p \|g\|_q \|h\|_r$.

**Correction Détaillée :**
L'idée est d'appliquer l'inégalité de Hölder classique deux fois.<br>Posons $\alpha$ tel que $\frac{1}{\alpha} = \frac{1}{p} + \frac{1}{q}$. Alors $\frac{1}{\alpha} + \frac{1}{r} = 1$.<br>Par l'inégalité de Hölder classique pour les exposants conjugués $\alpha$ et $r$ :<br>$\int |(fg)h| \le \|fg\|_\alpha \|h\|_r$.<br>Il nous reste à majorer $\|fg\|_\alpha$.<br>$\|fg\|_\alpha = (\int |fg|^\alpha)^{1/\alpha}$.<br>Appliquons Hölder à l'intégrale $\int |f|^\alpha |g|^\alpha$. Les exposants $p/\alpha$ et $q/\alpha$ sont conjugués car $\frac{\alpha}{p} + \frac{\alpha}{q} = \alpha(\frac{1}{p} + \frac{1}{q}) = \alpha \times \frac{1}{\alpha} = 1$.<br>Donc $\int |f|^\alpha |g|^\alpha \le (\int (|f|^\alpha)^{p/\alpha})^{\alpha/p} (\int (|g|^\alpha)^{q/\alpha})^{\alpha/q} = (\int |f|^p)^{\alpha/p} (\int |g|^q)^{\alpha/q}$.<br>En élevant à la puissance $1/\alpha$ :<br>$\|fg\|_\alpha = (\int |f|^\alpha |g|^\alpha)^{1/\alpha} \le (\int |f|^p)^{1/p} (\int |g|^q)^{1/q} = \|f\|_p \|g\|_q$.<br>On substitue cela dans la première inégalité :<br>$\|fgh\|_1 \le (\|f\|_p \|g\|_q) \|h\|_r = \|f\|_p \|g\|_q \|h\|_r$.
