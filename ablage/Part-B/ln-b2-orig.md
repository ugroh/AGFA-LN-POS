# CHARACTERTYATION OFPDOSTIVE 

SEMIGROURS ON CG(X)
by
Wolfgang Rrendt

It lies in the very nature of the theory of one-parameter semigroups that frequently an operator $A$ is known to be a generator but the semigroup is not known explicitly. Thus, since the semigroup is uniquely determined by the generator, it is a central task in the theory to express properties of the semigroup in terms of its generator. In this chapter we do this for two properties. We characterize generators of positive semigroups and generators of lattice semigroups.

In Section 1 we consider a semigroup (T(t)) $t \geqslant 0$ on the real space $C(K)$ ( $K$ compact). It is shown that the semigroup consists of positive operators if and only if its generator satisfies a positive minimum principle (P). Even without assuming a priori that $A$ is a generator the positive minimum principle has strong conseguences. Together with a range condition it implies that $A$ is a generator (of a positive semigroupl. Moreover, we show that for a densely defined operator $A$ to be the generator of a positive semigroup it is already sufficient that the resolvent $k(\lambda, A)$ of $A$ exists and is positive for all sufficiently large real $\lambda$. For all these results it is essential to assume that $K$ is compact. Concerning the characterization of positive semigroups on $C_{o}(X)$ ( $x$ locally compact, non-compact) we follow a completely different line and will treat this case in the context of general Banach lattices in Chapter C-II.

A special class of positive semigroups are lattice semigroups; i.e., semigroups of lattice homomorphisms. We show in section 2 that (T(t)) tzo is a lattice semigroup if and only if its generator $A$ satisfies an identity $(\mathbb{K})$, the so-called Kato's equality (Theorem 2.5) . We refer to Chapter C-II for a discussion of this identity and classical analogs for the Laplacian due to Kato (1973).

After the abstract characterization in section 2 we show that every continuous semiflow on $x$ together with a cocycle defines a lattice semigroup in a canonical way, and on $C(K)$, every lattice semigroup can be so represented. This furnishes a wide class of examples. Furthermore, positive one-parameter groups on $C_{o}(x)$ (which form a particular type of lattice semigroups) are discussed. Their generators are similar to a derivation perturbated by a multiplication operator (Section 3).

## 1. Generators of Positive Semigroups on $C(K)$.

Let $X$ be a locally compact space. Throughout this section we denote by $C_{o}(X)$ the space of all real-valued continuous functions on $C_{o}(X)$ which vanish in infinity. Recall that a semigroup (T(t)) tep on $C_{o}(X)$ is called positive $i f T(t) \geq 0$ for all $t \geq 0$. It is easy to describe the positivity of (T(t)) $t_{\geq 0}$ in terms of the resolvent $R(\lambda, A)$ of its generator $A$ because of the close relation between these two objects. In fact, the resolvent is expressed by the semigroup by

$$
\text { (1.1) } \quad R(\lambda, A)=\int_{0}^{+} e^{-\lambda t} T(t) d t \quad(\lambda, \dot{d}(A)) ;
$$

and conversely, the semigroup by the resolvent via the formula

$$
(1.2) \quad T(t)=\lim _{n+\infty}(n / t R(n / t, n))^{n} \quad \text { strongly }
$$

(cf. A-II, Prop.1.10). So we obtain the following.

Proposition 1.1 . Let ( $T(t)$ ) tro be a semigroup with generator $A$. The semigroup is positive if and only if $R(\lambda, A) \geq 0$ for all sufficiently large real $\lambda$.

It is more difficult and more interesting to characterize the positivity of the semigroup by intrinsic conditions on the generator. This is the purpose of this section. As a first orientation we consider bounded genexators. We need the following lemma.

Lema 1.2. Let $X$ be $a$ locally compact space, $x \in X$ and $k$ a regular bounded Borel measure on $x$ such that $\mu(f x\})=0$. Then
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-03.jpg?height=66&width=1620&top_left_y=384&top_left_x=224) $f(x) \neq 0$.

We omit the easy proof.

Theorem 1.3. Let $X$ be locally compact and $A$ be a bounded operator on $C_{0}(x)$. The following assertions are equivalent.
(i) $e^{t A} \geq 0 \quad(t \geq 0)$.
(ii) For $0 \leq f \in C_{0}(X)$ and $x \in X$.

$$
f(x)=0 \text { implies }(A f)(x) \geq 0 .
$$

(iii) $A+\|A\| I d \geq 0$.

Proof. (i) implies (ii). Let $f \in C_{0}(X)+$ and $x \in X$ such that $\mathrm{f}(\mathrm{x})=0$. Then

$$
\begin{aligned}
(\text { Af) }(x) & =1 m_{t+0} 1 / t\left(\left(e^{t A} f(x)-f(x)\right)\right. \\
& =1 i_{t+0} 1 / t\left(\left(e^{t A} f(x)\right) \geqslant 0 .\right.
\end{aligned}
$$

(ii) implies (iii). Let $x \in x$. We have to show that (Af) $(x)+$ $\left\|\|_{i} f(x) \geq 0\right.$ for all $f \in C_{o}(X)$. Let $A^{\prime} \delta_{x}=\mu+c_{x}^{\delta}$ where $\mu \in M(X)$ such that $\mu([x]) \neq 0$ and $c \in \mathbb{R}$. We claim that $\ddagger \geqq 0$. Let $0 \leqq$ $f \in C_{0}(X)$ such that $f(x) \neq 0$. Then $\langle f, \mu\rangle=\left\langle E, A^{\prime} \delta_{x}\right\rangle=(A f)(x) \geq 0$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-03.jpg?height=78&width=1620&top_left_y=1703&top_left_x=224)
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-03.jpg?height=70&width=1614&top_left_y=1761&top_left_x=221)
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-03.jpg?height=70&width=1505&top_left_y=1821&top_left_x=224) (iii) implies (i). We have $e^{t A}=e^{-t\| \|^{x} \|} e^{t(A+\|A\|)} \geqq e^{-t\|A\|}$ Id for all $t \geqq 0$.

Example l.4. a) Let $B$ be a positive operator on $C_{o}(x)$ and m $X$ $\rightarrow \mathbb{R}$ be a continuous and bounded mapping. Let $\overrightarrow{A f}=B f-m \cdot f \quad(f \in$ $C_{o}(X)$. Then $e^{t h} \geq 0$ for all $t \geq 0$.
b) Let $A$ be a nxn - matrix. Then $e^{t A} \geq 0$ for all $t \geq 0$ if and only if $a_{i j} \geqq 0$ for $i \neq j$. This is the linear version of Kamke's theorem (see Kamke (1932)).

Now we come to the actual subject of this section, the characterization of strongly continuous positive semigroups on $C(K)$. Here $K$
denotes a compact space and $C(K)$ the space of all real-valued continuous functions on $K$. It will be essential that $K$ is compact for all what follows since it will be needed that the positive cone of $C(\mathrm{~K})$ has interior points.

We reformulate condition (ii) of Theorem 1.3 for unbounded operators.

Definition 1.5. An (unbounded) operator $A$ on $C(K)$ is said to satisfy the positive minimum principle if
for every $0 \leqq £ \in D(A)$ and $x \in K$,
(P)

$$
f(x)=0 \text { implies }(A f)(x) \geq 0 .
$$

Our next theorem shows that the positive minimum principle characterizes the positivity of the semigroup; and in fact, the proof is very elementary. Using more involved arguments we will later prove a much stronger result (Theorem 1.13).

Theorem l.6. Let $A$ be the generator of a strongly continuous semigroup on $C(K)$. Then the semigroup is positive if and only if the generator $A$ satisfies the positive minimum principle (P).

Proof. The necessity of the condition is proved as "(i) implies (ii)" in Theorem 1.3. Assume that ( P ) holds. We claim that $\mathrm{F}(\lambda, \mathrm{A}) 30$ for sufficiently large real $\lambda$. (This implies the positivity of the semigroup by Prop. 1.l). Let $s:=\inf \{\lambda \in \mathbb{R}:[\lambda, \infty) \in \rho(A)\}$. Then $s$ s $\omega(A)<\infty$. Let $0 \ll u \in C(K)$. Then $\lambda_{0}:=\inf (\lambda>s: R(\mu, A) u \geqslant 0$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-04.jpg?height=55&width=1226&top_left_y=1846&top_left_x=204)
we claim that $\lambda_{0}=s$.
In fact, if this is not true, then $\left[\lambda_{O}{ }^{\infty}\right) \subset \rho(A)$ and $R\left(\lambda_{0}, A\right) u \geq 0$ but $R\left(\lambda_{o}, A\right) u$ is not strictly positive. Consequently there exists $x \in K$ such that $\left(R\left(h_{o}, A\right) u\right)(x)=0$. Then $(P)$ implies that $A\left(R\left(\lambda_{O}, A\right) u\right)(x) \geq 0$. Hence, $0<u(x)=\lambda_{0}\left(R\left(\lambda_{0}, A\right) u\right)(x)-$ $A\left(R\left(\lambda_{0}, A\right) u\right)(x) \subseteq 0$, a contradiction. We have shown that $R(\lambda, A) u \gg 0$ for all $u \gg 0$ and $\lambda>s$. Since $\{u \in C(K): u \geqslant>0\}$ is dense in $C(K)+$, it follows that $R(\lambda, A) \geq 0$ for all $\lambda>s$.

Remark 1.7. The proof of Theorem 1.6 shows that for the generator $A$ of a positive semigroup on $C(K), R(\lambda, A) u \gg 0$ whenever $0 \ll u \in C(K)$ and $[\lambda, \infty) \subset \rho(A)$. In particular, $R(\lambda, A)$ a 0 whenever $[\lambda, \infty)<\rho(A)$.

If $A$ is a generator, then the positivity of the resolvent $R(\lambda, A)$ for large real $\lambda$ implies the positivity of the semigroup (by Prop. 1.1). On $C(K)$ much more is true. Even if $A$ is not supposed to be a generator, the existence and positivity of $k(\lambda, A)$ for large real $\lambda$ implies that $A$ is a generator (of a positive semigroup). This is surprising, because it means that in the case when the resolvent is positive, the norm condition on the resolvent sup $\left\{\left\|(\lambda-w)^{n} R(\lambda, \bar{A}){ }^{n}\right\|\right.$ : $n \in \mathbb{N}, \lambda \geq 0\}<\infty$ which appears in the Hille-Yosida theorem $(A-I I$. Thm. 1.7) is automatically fulfilled.

Theorem 1.8. Let $K$ be compact and $A$ be a densely defined operator on $C(K)$. Suppose that there exists $w \in \mathbb{R}$ such that $[w, m)$ © $p(B)$ and $R(\lambda, A) \geq 0$ for all $\lambda \geq w$. Then $A$ is the generator of a strongly continuous positive semigroup. Moreover,

```
(1.3) #(A) S W.
```

Proof. a) Rssume that $w<0$. Denote by 1 the constant-l-function. Let $u=R(0, A) 1$. We claim that $u>0$. If not, then there exists $x \in K$ such that $u(x)=0$. Let $f \in C(K)$. Then $|f| \equiv\|f\| l$. Consequently, $|R(0, A) f| \leqq R(0, A)|f| \leqq\|f\| R(0, A) 1=\|f\| u$. Hence $(R(0, A) f)(x)=0$ for all $f \in C(K)$. Since $D(A)=R(0, A) C(K)$, it follows that $D(A)$ is not dense, a contradiction. Detine $\|f\|_{0}=$ inf $\{\lambda>0:|f| \subseteq \lambda u\} * f / u \|_{\infty}$. Then il $\|_{0}$ is an equivalent norm on $C(K)$. Moreover, $\|f\|_{0} \leq 1$ if and only if $f \in[-u, u]$. By the resolvent equation we have
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-05.jpg?height=43&width=1571&top_left_y=1886&top_left_x=228) $\lambda \geqq 0$. This implies that $\lambda R(\lambda, A)$ is contractive for the norm $\left\|\|_{0}\right.$. Thus by the Hille-Yosida Theorem $A$ is the generator of a semigroup which is contractive with respect to the norm $\left\|\|_{0}\right.$, and so is bounded with respect to the supremum norm on $C(K)$.
b) If $w$ is arbitrary, let $\lambda>W$ and consider $A-\lambda$. Then $[w-\lambda, \infty) \subset p(A \sim h)$ and $R(\mu, A-\lambda)=R(\ldots+\lambda, A) \geq 0$ for all $\mu \in\left[W^{-\lambda}, \infty\right)$. Thus by a), $A-\lambda$ is the generator of a bounded positive semigroup. Consequently, $A$ is a generator as well and $\omega(\hat{A}) \leq \lambda$.

In Theorem 1.8 it is enough to assume that $R(\lambda, A) \geqq 0$ for some sequence $\left(\lambda_{n}\right) G \rho(A) r \mathbb{R}$ satisfying $\lim _{n \rightarrow \infty} \lambda_{n}=$ - This follows from the following lemma.

Lemma 1.9. Let $B$ be an operator on $C(R)$ (more generally, on a
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-06.jpg?height=55&width=1497&top_left_y=338&top_left_x=231) $0 \leq R\left(\mu_{2}, B\right)$ and $\mu_{1} \in \mu_{2}$, then $\left[\mu_{1}, \mu_{2}\right] \subset \rho(B)$ and

$$
\left.0 \leqq R\left(\mu_{2}, B\right) \leqq R(\mu, B) \leqq R^{\prime} \mu_{1} ; B\right) \quad \text { for all } \mu \in\left[\mu_{1}, H_{2}\right] .
$$

Proof. Let $M:=\left\{\mu \in \rho(B) \cap\left[\mu_{1}, \mu_{2}\right]=\left[\mu, \mu_{2}\right]=\rho(B)\right.$ and $R(\lambda, B) \geq 0$ for all $\lambda \in\left[\begin{array}{l}\text { a } \\ \text { 没 }\end{array}\right]$ )
a) The set $M$ is open. In fact, let $H \in M$. Then for small $h$ o one has $\mathrm{k}\left(\beta_{3}-\mathrm{h}, \mathrm{B}\right)=\sum_{\mathrm{n}=0}^{\infty} \mathrm{h}^{\mathrm{n}} \mathrm{R}(\mu, B)^{\mathrm{nt1}} \geq 0$.
b) M is closed. In fact, by the resolvent equation one has for
$\mu \in M, R\left(\mu_{1}, B\right)-R(\mu, B)=\left(\mu-\mu_{1}\right) R\left(\mu_{1}, B\right) R(\mu, B) \geqq 0$, hence $R(\mu, B) \leqq R\left(\mu_{1}, B\right)$. Consequently, $\operatorname{dist}(\mu, \sigma(B)) \geqq 1 /\|R(\mu, B)\| \underline{2}$ $1 /\left\|_{\mathrm{R}}\left(\mu_{1}, \mathrm{~B}\right)\right\|$ for all $\mu \in M$. This implies that $M$ is closed. The assertions al and b) imply that $M=\left[\mu_{1}, H_{2}\right]$.

Remark. a) The lemma shows in particular that the resolvent of the generator $A$ of a positive semigroup is decreasing on $(s(A), \infty)$.
b) There exigts a linear operator $B$ on $\mathbb{R}^{n}$ such that $R(\mu, B) \quad(0$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-06.jpg?height=72&width=1617&top_left_y=1420&top_left_x=228) (see Greiner-Voigt-Wolff (1981)).

Remark. Theorem 1.8 does not hold in $C_{o}(X)$, in general. In fact, the operator $A$ on $C_{o}\left(0,1 i\right.$ given by $A f(x)=f^{\prime}(x)+a / x f(x)$ $\left(x \in(0,1 \mathrm{I})\right.$ with domain $\mathrm{D}(\mathrm{A})=\left\{\mathrm{f} \in \mathrm{C}^{1}\left[0,1 \mathrm{I}: \mathrm{E}^{\prime}(0)=\mathrm{f}(0)=0\right\}\right.$ where $\alpha \in(0,1)$ satisfies the following: $\rho(A)=C, R(\lambda, A) \geqslant 0$ for all $\lambda \in \mathbb{R}$. But $A$ is not the generator of a semigroup (even if more general classes than $C_{o}$-semigroups are admitted). See Arendt (1985b) for this example and a general theory of resolvent positive operators. Another example is given by Batty-Davies (1983).

Next we investigate consequences of the positive minimum principle for a densely defined operator which is not a priori assumed to be a generator. For that we will make use of the theory of halfunorms developed in $A-I I, S \in c .2$.

For $0 \ll u \in C(K)$ let

$$
\begin{equation*}
\mathrm{P}_{\mathrm{u}}(f)=\inf \left\{\lambda \in \mathbb{R}_{+}: \mathrm{f} \leq \lambda u\right\}=\sup _{x \in K} f^{+}(x) / u(x) \tag{1.4}
\end{equation*}
$$

Then $P_{u}$ is a strict half-norm on $C(K)$ (see $\left.A-I I, ~ S e c .2\right)$. Note that (1.5) $\quad P_{u}(f) u-f \geq 0 \quad(f \in C(K))$.

For $x \in K$, define $\phi_{x} \in C(K)$ by $<f_{f} \phi_{x}=f(x) / u(x)$.
Let $£ \in C(K)$ such that $-f$ is not strictly positive. Then there exists $x \in K$ such that $f(x) / u(x)=P_{u}(f)$. For such an $x$ we have (1.6) $\quad \phi_{x} \in \operatorname{dp}_{u}(f)$
(see $A-I I, \sec .2$ for the definition of the subdifferential $d p_{u}$ ).
Note that for $f \in C(K)$ one has $f \geq 0$ it and only if $p_{u}(-f) \leq 0$ (i.e., the half-norm $P_{u}$ induces the given ordering on $C(K)$ (cf. A-II,Rem.2.8)). As a consequence, overy $P_{u}$-contractive bounded operator $T$ on $C(K)$ is positive.

Proposition 1.10. Let $A$ be a densely defined operator on $C(K)$. Then there exists a strictly positive $u \in D(A)$. For any such $u$ the following assertions are equivalent.
(i) A is $P_{u}$-dissipative.
(ii) $A u \leq 0$ and $A$ satisfies (P).

Proof. Since $\{u \in C(K) ; u \gg 0\}$ is open and non-empty and $D(A)$ is dense, there exists $0 \ll u \in D(A)$.
(i) implies (ii). One has $P_{u}(u)=1$. Let $x \in K$. It follows from (1.6) that $\phi_{x} \in d_{p}(u)$. Since $D(A)$ is Gense, it follows from $A-I I$, Thm. 2.7 that $A$ is strictly $P_{u}-d i s s i p a t i v e . ~ H e n c e ~<A u, \phi_{x}>x^{\prime} 0$. Thus $(A u)(x) \leqq 0$. We now show (P). Let $0 \leqslant f \in D(A)$ and $x \in K$ such that $f(x)=0$. We have to show that (Af) (x) $\geq 0$. Since $f(x)$ $=0$ and $P_{u}(-f)=0$ we have by (1.6) $\phi_{x} \in d p_{p}(-f)$. Since $A$ is strictly $P_{u}-d i s s i p a t i v e ~ w e ~ c o n c l u d e ~ t h a t ~-u(x)^{-1}(A f)(x)=\left\langle\mathcal{A}_{( }(-f), \phi_{X}{ }^{3}\right.$ $\leq 0$. Hençe (Af) (x) $\geqq 0$.
(ii) implies (i). Let $f \in D(A)$. If $\mathrm{P}_{\mathrm{u}}(\mathrm{f})=0$, then $\phi:=0 \in$ $d P_{u}(f)$ and $\langle\boldsymbol{R f}, \phi\rangle \leqq 0$. If $P_{u}(f)>0$, then there exists $x \in K$ such that $\phi_{x} \in d P_{u}(f)$. Hence, $0 \leq P_{u}(f) u-f$ and $\left(P_{u}(f) u-f\right)(x)=0$. It follows from ( $P$ ) that $P_{u}(f)(A u)(x)-(A f)(x) \geqq 0$. Hence (Af) (x) $s \mathrm{P}_{\mathrm{u}}(\mathrm{f})(\mathrm{Au})(\mathrm{X}) \leqslant 0$ (by (ii)); i.e., $\in A f, \phi_{X} \leq 0$.

Corollary 1.11 . Let $A$ be a densely defined operator on $C(K)$ If A satisfies (P) then $A$ is closable and the closure of $A$ satisfies (P) as well.

Proof. Let $u \in D(A)$ be strictly positive. Then there exists $\lambda \in \mathbb{R}$ such that $A u \leqq \lambda u$. The operator $B=A-\lambda$ satisfies ( $P$ ) as well and Bu $\underset{*}{ }$. Then by Prop. 1.10 , $B$ is $\mathrm{P}_{\mathrm{u}}$-dissipative. Hence B is closable and the closure $\bar{B}$ of $B$ is Pu-dissipative as well by $A-I I$ Prop. 2.9), Then by Prop. 1.10 B satisfies (P). Thus A is closable and its closure $\bar{A}=\bar{B}+\lambda$ satisfies (P) as well.

Corollary 1.12. Let $A \quad C(K) * C(K)$ be linear. If $A$ satigfies (P) then $A$ is bounded and $A+\|A\| I \geqslant 0$.

Proof. It follows from Corollary 1.11 that $A$ is closed. Hence A is bounded. Since A satisfies (P), it follows from Thm. I. 3 that $A$ $+\| \operatorname{lil}$ Id $\geqq 0$.

The next result is a strengthened form of Theorem 2.6. It is somewhat similar to the Lumer-Phillips theorem (A-II, Thm. 2.13). Note that, however, in contrast with the condition of dissipativity, $A+w$ satisfies (P) for any $w \in \mathbb{R}$ whenever ( $P$ ) hofds for $\mathbb{A}$. Thus ( $P$ ) is not a "metric" condition; that is, it does not imply any norm estimate for the semigroup. We also point out that, if (T(t)) $t \geq 0$ is a positive semigroup on $C(K)$, then in general none of the semigroups $\left(e^{-W t} T(t)\right)_{t \geq 0}(w \in \mathbb{R})$ is contractive (see Batty-Davies (1983) or Derndinger (1983)).

Theorem 1.13. Let $A$ be a densely defined operator on $C(K)$ which gatigfies (P). Then

$$
\lambda_{0}:=\inf \{\lambda \in \mathbb{P}: A u \leq \lambda u \text { for some } 0 \ll u \in D(A)\}<\infty
$$

(a) If ( $\lambda$ - $A) D(A)$ is dence for some $\lambda>\lambda_{0}$, then $A$ is closable and the clogure $\bar{A}$ of $A$ is the generator of a positive semigroup. (b) If $\lambda$ - $A$ is surjective for some $\lambda>\lambda_{0}$, then $A$ is the generator of a positive semigroup.

Proof. It follows from Prop. 1.10 that $\lambda_{0} \leqslant \infty$.
Assume that $(\lambda-A) D(A)$ is dense, where $\lambda>\lambda_{0}$. Let $\lambda_{0} \leqslant \mu<\lambda$ and $B=A-\mu$. Then $B$ satisfies ( $P$ ) and Bu $\leq 0$ for some atrictly positive $u \in D(B)=D(A)$. Thus $B$ is Pu-dissipative by Prop.1.10. Moreover, $((\lambda-\mu)-B) D(B)$ is dense. Thus by A-II,Cor.2.12 the closure $B$ of $B$ generates a $P_{u}$-contraction semigroup. Hence the
closure $\bar{A}=\bar{B}+\mu$ of $A$ generates a positive semigroup of type $\mu(\bar{A}) \leqq \lambda$.
If $(\lambda-\bar{A})$ is surjective, then $A=\bar{A}$.

The proof of Theorem 1.13 yields estimates for the growth bound of a positive semigroup (see A-III, (1.3)) which we state explicitly in the next corollary.

Corollary l.14. Let $A$ be the generator of a strongly continuous positive semigroup on $C(K)$. Then
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-09.jpg?height=46&width=1306&top_left_y=968&top_left_x=232)
(1.8) $s(A)=\inf \{\lambda \in \mathbb{R}: A u \leq \lambda u$ for some $0<c \in \in D(A)\}$; and
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-09.jpg?height=44&width=1443&top_left_y=1200&top_left_x=232)

Proof. Let $s=\inf \{\lambda \in R:[\lambda, \infty) \subset \rho(A)\}$, Clearly, $s \leq s(A)$. Moreover, by Remark 1.7 , $R(\lambda, A) \underline{x} 0$ for all $\lambda>s$, Hence it follows from (1.3) that $u(A) \leqq 5$. Consequently, $s=s(A)=\omega(A)$. Next we prove (1.9). Let $0<f \in D(A)$ such that $A \neq \geq f f$. Assume
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-09.jpg?height=47&width=1611&top_left_y=1547&top_left_x=231) contradiction.

Since $D(A)$ is dense, there exists a strictly positive $u \in D(A)$. Then $A u$ в $k u$ for some $\mu \in \mathbb{R}$. Hence, $w<\mu \leq s(A)$ by (1.9). Since $s(A)=s$ it is clear that $s(A) \in \sigma(A)$. It remains to show (1.8). Let $\lambda \rightarrow \operatorname{si}(A)$ and $u=R(\lambda, A) l$. Then $u$ is strictly positive (by Rem. 1.7) and $\overrightarrow{A u}=\lambda u-1 \leq \lambda u$ * This proves one inequality in (1.8). Assume now that $u \in D(A)$ is strictly positive such that $A u x$ xu . Then by the proof of Thru. 1.13 we have $\omega(A) \leq \lambda$. This proves the other inequality in (1.8).

Remark 1.15. If $A$ has compact resolvent, then by the Krein-Rutmann theorem there exists a positive eigenvector $u$ of $A$ corresponding to a real eigenvalue. So the equality is valid in (1.9) and the supremum is a maximum. If in addition the semigroup ig irreducible (see B-III,Sec. 3 below), then $u$ is strictly positive and in (1.8) the infimum is attained as well.
Conversely, if in (1.8) the infimum is attained, then $s(\vec{B})$ is an eigenvalue.

Example 1.16 . Let $A=\left(a_{i j}\right)$ be an $n^{\times n-m a t r i x}$ such that $a_{i j} \geq 0$ whenever $i \neq j$ (see Example $1.4 b$ ). Then by Corollary 1.13. $s(A)=\inf \{\lambda \in \mathbb{R}: A u \leq \lambda u$ for some strictly positive $u\}=$ $\inf u \gg 0$ inf $\{\lambda \in \mathbb{H}: A u \leqslant \lambda u\}=\inf \left\{\sup _{i} \sum_{j=1}^{n} a_{i j} u_{j} / u_{i}: u \gg 0\right\}$. This formula is due to collatz (1942) (see also [Schaefer (1974), Chap, Exercise 20] and wielandt (1950)).

Corollary 1.17. Let $(T(t))$ t $\geq 0$ be a strongly continuous positive semigroup on $C(K)$. Then $T(t) u \gg 0$ for all $u>0, t \geqq 0$.

Proof. Denote by $A$ the generator of (T(t)) tz0. Then by the proof of Thm. 1.13 there exist $u \gg 0$ and $\lambda \in \mathbb{R}$ such that $A-\lambda$ is $\mathrm{P}_{\mathrm{u}}$-dissipative. This implies that $\mathrm{P}_{\mathrm{u}}(\mathrm{T}(\mathrm{t}) \mathrm{f}) \underset{\mathrm{s}}{ } \mathrm{e}^{\lambda t_{\mathrm{p}}} \mathrm{p}_{\mathrm{u}}(\mathrm{f})$. observing that $f \gg 0$ if and only if $P_{u}(-f)<0$ the claim follows.

Remark 1.18. Corollaries 1.14 and 1.17 do not hold on $C_{o}(X)$, For example, let $X=[0,1)$ and

$$
(T(t) f)(x)=\left\{\begin{array}{lll}
f(x+t) & \text { if } x+t \leqq 1 \\
0 & \text { if } x+t>0
\end{array} .\right.
$$

Then (T(t)) $t \geq 0$ is a positive semigroup on $C_{0}(x)$ and $T(t)=0$ for all $t \geqq l$. The generator $A$ of $(T(t)){ }_{t \geq 0}$ has empty spectrum, so that (1.7) is violated. However, it is still true that $s(A)=\omega(A)$ for generators of positive semigroups on $C_{o}(X)$ (see B-IV, Thm. 1,4 ).

Remark 1.19. So far, the resulta of this section do not depend on the lattice structure of $C(K)$. They also hold on an ordered Banach space E with normal cone $E_{t}$ which has non-empty interior. We refer to Arendt-Chernoff-Kato (1982) and to Batty-Robinson (1984) for this more general setting.

Next we apply Theorem. 1.13 to prove a result on the multiplicative perturbation of a generator $A$ which is due to Dorroh (J966) in the case when $A_{2}$ is dissipative.

Theorem 1.20. Let $A$ be the generator of a positive semigroup on $C(K)$ and $m \in C(K)$ be strictly positive. Thon the operator meh given by $(m+A) f=m \cdot(\bar{f})$ on the domain $D(m \cdot A)=D(A)$ is the generator of a positive semigroup. Moreover,

$$
\begin{equation*}
\left\|m^{-1}\right\|_{\infty}^{-1} \omega(A) \leqq \omega(m \cdot A) \leqq\|m\|_{\infty} \omega(A) . \tag{1.10}
\end{equation*}
$$

Proof. We can assume that $\|m\|_{\infty} \leq 1$ (in fact, if $B:=\left(m /\|m\|_{\infty}\right) \cdot A$ is the generator of a positive semigroup, then by $R-I, 3.1$
$m \cdot A=\|m\|_{\infty} B$ also generates a positive semigroup). The assertion of the theorem holds for $A$ if and only if it is valid for $A-W$ ( $w \in \mathbb{R}$ ). So by the proof of Thri. 1.13 we can assume that there exists $0<c u \in C(K)$ such that $A$ is $\mathrm{P}_{\mathrm{u}}$-dissipative. We first show,
(l.ll) if $B$ is a $p_{u}$-dissipative operator and $0 \in q \in \mathcal{C}(K)$, then $q^{*} B$ is $P_{u}$-dissipative.

Let $f \in D(q \cdot B)=D(B)$, There exists $x \in K$ such that $\phi_{x} \in d p_{u}(f)$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-11.jpg?height=59&width=1602&top_left_y=910&top_left_x=227) $<B f, \phi_{x}>0$.

Next we show
if $B$ is the generator of a $P_{u}$-contraction semigroup and (1.12) $12 q \in C(K)+i s$ such that $\|l-q\|_{\infty}<1 / 2$, then $g * B$ generates a $\mathrm{Pu}_{\mathrm{u}}$-contraction semigroup.

Because of (1.11) we only have to show that (I - q.B) is surjective. Note that $1 \in \rho(B)$. We have (Id - $q \cdot B)=(I d-B-(q-1) B)=$ (Id - (q-l)BR(l,B)) (Id - B) . Thus it suffices to show that Id $-(q-1) B R(1, B)$ is invertible. The norm $\|f\|_{u}=\max \left\{P_{u}(f), P_{u}(-f\}\right\}$ $=\sup _{x \in K}|f(x)| / u(x)$ is equivalent to the supremum norm. Denote by $\|T\|_{u}$ the operator norm corresponding to $\left\|\|_{u} \quad(T \in \mathbb{E} \in(E)\right.$. Then it is enough to show that $\|(q-1) B R(1, B)\|_{u}=\|(q-1)(R(1, B)-I)\|_{u} \subset 1$. For $r \in C(K)+$ denote $b y M_{r}$ the multiplication operator given by $M_{r} f=r \cdot f$. Then $\left\|M_{r}\right\|_{u}=\sup \left\{\|r \cdot f\|_{u}:\|f\|_{u} \leqslant 1\right\}=\sup \left\{\sup X_{x \in K}\right.$ $\left.r(x)|f(x)| / u(x):\|f\|_{u} \leqslant l\right\}$ x $\|r\|_{\text {c }}$. Since $B$ is $P_{u}$-dissipative we have $\|R(1, B)\|_{u} \leqq 1$ (by $A-I I, L e m m a \operatorname{lon}$ ). This gives $\|(q-1)(R(1, B)-I)\|_{u} \leq\left\|M_{(1-q)}\right\|_{u}\left(\|R(1, B)\|_{u}+1\right) \leq 2\|1-q\|_{\infty}<1$. The proof of (l.12) is complete.

There exists $k \in \mathbb{N}$ such that $\left\|1-m^{1 / k}\right\|_{\infty}<1 / 2$. Applying now (1.12) succesively to $B=m^{1 / k}, A_{2}$ and $g=m^{1 / k} \quad(1=1, \ldots, k-1)$ we obtain that meA generates a $p_{u}$-contraction semigroup (which in particular is positivel.

Finally we show (l.l0) to hold.
Let $0 \ll u \in D(A)=D(m \cdot A)$ and $A u \leq \lambda u$. Then $m \cdot A u \leq\|m\|_{\infty} \lambda u$. So (1.8) implies that $m(m \cdot A) ~\|m\|_{m}(A)$. This is one part of (1.10).

The other part follows from this since $\quad,(A)=a\left(m^{-1} \cdot m \cdot A\right)$
$\leqq\left\|m^{-1}\right\|_{\infty}(m \cdot A)$.

In the following lemma a condition ( $P^{\prime}$ ) is introduced which is dual to the positive minimum principle.

Lemma 1.21. Let $A$ be the generator of a strongly continuous positive semigroup on $C(K)$. Then for $f \in C(K)+, \quad \in\left\{\in D\left(\mathcal{R}^{\prime}\right)\right.$
( $\left.P^{\prime}\right)\langle f, \mu\rangle=0$ implies $\left\langle f, A^{\prime} \mu\right\rangle \geqq 0$.

Proof. $\left\langle f, A^{\prime} u\right\rangle=\lim _{t \rightarrow 0} \frac{1}{t}\langle T(t) f-f, \mu\rangle=\lim _{t \rightarrow 0} \frac{1}{t}\langle T(t) f, \mu\rangle \geqq 0$.

Example 1.22. Let $K=[-1,0]$. Let $a \in \mathbb{R}$ and $\&$ be a measure on $[-1,0]$ such that $\mu(0)=0$. Define the operator $A$ on $C[-1,0]$ $b y$ Af $=\mathrm{E}^{\prime}$ with domain $D(A)=\left\{f \in C^{1}[-1,0]: f^{\prime}(0)=\alpha f(0)+\right.$ <f, $\left\{\begin{array}{l}\text { > }\end{array}\right.$.
Claim: $A$ is the generator of a positive gemigroup if and only if山 20 。

Proof of the claim. Assume that $\vec{A}$ generates a positive semigroup. By the definition of $A$ one has $\delta_{0} \in D\left(A^{\prime}\right)$ and $A^{\prime} \delta_{0}=a \delta_{o}+\mu$. So
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-12.jpg?height=64&width=1615&top_left_y=1667&top_left_x=209) such that $f(0)=0$. By Lemma l. 2 this implies that $\mu \geq 0$. In order to show the converse assume that $\ddagger \geq 0$.
a) We show that $\vec{A}$ is densely defined. Consider the normed space $F=$ $C^{l}[-1,0]$ with the supremum norm. Then $\psi ; F \rightarrow$ iti given by $\psi(f)=$ $f^{\prime}(0)-a f(0)-\langle f, \mu\rangle$ is a discontinuous linear form on $F$, Consequently $D(A)=k e r \quad \psi$ is dense in $F$. Since $F$ is dense in $C[-1,0], D(A)$ is dense in $C[-1,0]$ as well.
b) A satisfies (P) (see Def. l.5) . In fact, let $f \in D(A)+$ and $x \in[-1,0]$ such that $f(x)=0$. It is clear that $A f(x)=f^{*}(x) \quad 30$ if $x<0$. But if $f(0)=0$, then $A f(0)=f^{\prime}(0)=\langle f, \mu\rangle \geq 0$ since $\mathrm{E} \in \mathrm{D}(\mathrm{A})$.
c) We show that $(\lambda-A)$ is bijective for $\lambda>\alpha+\|k\|$. Let
$g \in \mathbb{C}[-1,0]$. The solutions of the equation $\lambda f-\mathrm{f}^{\prime}=\mathrm{g}$ ( $f \in C[-1,0]$ ) are given by $f(x)=e^{\lambda y}\left[\int_{x}^{0} e^{-\lambda y} g(y) d y+c\right]$ where $c \in \in$. Moreover, $f \in D(A)$ if and only if
(2.8) $c\left(\lambda-a-\int_{-1}^{0} e^{\lambda x} d_{\mu}(x)=g(0)+\int_{-1}^{0} e^{\lambda x} \int_{x}^{0} e^{-\lambda y} g(y) d y d \mu(x)\right.$.

If $\lambda>a+\|k\|$ ，then $\lambda-a-\int_{-1}^{0} e^{\lambda x} d \mu(x) \neq 0$ and there exists exactly one $c \in \mathbb{F}$ satisfying（2．8）．We have shown that
（ $\lambda$－$A$ ）is bijective for $\lambda, a+\| ⿻ 川 ⿲ 丶 丶 丶 i l$
By Thm．l．l3，it follows from al，b）and c）that A generates a posi－ tive semigroup．

Let us mention in addition that it follows from a）in the proof that $\left(\alpha+\|\mu\|_{i}, \infty\right)-\rho(A)$ ，since $A$ is closed．By Remark 1.7 we thus have

$$
\begin{equation*}
s(A) \leqq \alpha+\|, k\| . \tag{2.9}
\end{equation*}
$$

Example 1．23．Let $E=C\left(\left[-1,0 j_{i} \Gamma^{n}\right)\right.$ ．Then $u \in E$ is given by $u=$ $\left(u_{1}, \ldots, u_{n}\right)$ where $u_{i} \in C[-1,0](i=1, \ldots, n)$ ．Let $A$ be defined by $A u=u^{\prime}=\left(u_{1}^{\prime}, \ldots, u_{n}^{\prime}\right)$ with domain $D(A)=\left(u \in C^{1}\left([-1,0], \mathbb{R}^{n 1}\right)\right.$ ： $\left.u^{\prime}(0)=L u\right\}$ ．
Here $L$ is defined by

$$
\mathrm{Lu}=\left\{\begin{array}{c}
\mathrm{L}_{11} u_{1}+\ldots+\mathrm{L}_{1 n} u_{n} \\
\vdots \\
\mathrm{~L}_{n 1} u_{1}+\ldots+\mathrm{L}_{n n} u_{n}
\end{array}\right\}
$$

where $L_{i j} \in C[-1,0]^{r} \quad(1 \leqq i, j \leqq n)$ ．
Let $L_{i i} \stackrel{c_{i}}{=}{ }_{0}+\mu_{i}$ with $\mu_{i}(\{0\})=0 \quad(i=1, \ldots, n)$ ．
Then $A$ generates a positive semigroup if and only if

$$
L_{i j} \geqq 0 \text { for } i \neq j \text { and } \mu_{i} \geqq 0 \quad(i, j=1, \ldots, n)
$$

This can be proved in a similar way as the claim in Example 1.21 （see Arendt（1984a））．

Example 1．24．Let $A$ on $C[0,1]$ be given by $A f=\mathrm{f}^{\boldsymbol{\prime}}$ with domain $D(A)=\left\{f \in C^{2}[0,1]: f^{\prime}(0)+a f(0)=0, f^{\prime}(1)+5 f(1)=0\right\}$ ，where $\alpha, B \in \mathbb{R}$ ．Then $A$ is the generator of positive semigroup．

Proof．The operator $A$ satisfies（P）．In fact，let $0 \leq f \in D(A)$ and $f(a)=0$ where $a \in[0,1]$ ．If $a \in(0,1)$ then $f^{\prime \prime}(a)$ a 0 since $f$ has a minimum in $a$ ．If $a=0$ ，then $f^{\prime}(0)=f^{\prime}(0)+\alpha f(0)=0$ since $f \in D(A)$ ．Consequently，$f(x)=\int_{0}^{x}(x-y) f "(y) d y \geqslant 0$ for all $x \geq 0$ ．This implies $f "(0) \geq 0$ ．The argument for $a=1$ is analo－ guous．

It remains to show that $k-A$ is surjective for large real $\mu$. Let $g \in C[0,1]$. Let $\lambda>0$ and $k=1 / 2 \lambda E_{i} e_{x} \int_{x}^{l} e^{-\lambda y} g(y) d y-$ $\left.e^{-\lambda x} \int_{x}^{1} e^{\lambda y} g(y) d y\right]^{\top}$. Then $k \in c^{2}\left[0,11\right.$ and $\lambda^{2} k-k^{*}=g$ - Let $h=$ $a e^{\lambda x}+\operatorname{le}^{-\lambda x}$, where $a, b \in \mathscr{G}$. Then $h \in c^{2}[0,1]$ and $\lambda^{2} h-h^{\prime \prime}=0$. Let $f=k+h$. Then $\lambda^{2} f-f^{r}=g$. The condition that $f \in D(A)$ leads to two linear equations in $a$ and $b$, and it is easy to see that they have a solution $(a, b) \in \mathbb{H}^{2}$ if $(\lambda+\alpha)(\beta-\lambda)+(\lambda-\alpha)(\lambda+\beta) \exp \left(\lambda^{2}\right) \frac{f}{3} 0$. Thus there exists a solution if $\lambda$ is large enough, and $\left(\lambda^{2}-\lambda\right)$ is surjective.
2. Lattice Semigroups on $C_{\text {g }}(X)$

Throughout this section $x$ denotes a locally compact space and $C_{o}(X, \mathbb{R})$ (resp. $C_{o}(X, \mathbb{C})$ ) the space of all real-valued (resp. complex-valued) continuous functions on $X$ which vanish at infinity. If we do not want to specify the field we simply write $C_{0}(X)$. Recall from $B-I$, sec. 3 that a linear bounded operator $T$ on $C_{o}(X)$ is positive if and only if
(2.1) $|T f| \leq T|f|$ for all $f \in C_{O}(X)$.

The operator $T$ is a lattice homomorphism if and only if in (2.1) equality holds; i.e.,
(2.2) $|T f|=T|f|$ for all $f \in C_{o}(X)$.

Remark 2.1. If $T$ is a lattice homomorphism on $C_{0}\{x, C)$, then $T$ leaves $C_{o}(X, R)$ invariant and the restriction $T_{i n}$ of $T$ to $C_{0}(X, \mathbb{R})$ is a lattice homomorphism. Conversely, the linear extension $T$ of a lattice homomorphism $T_{\mathbb{R}}$ or $C_{o}(X, R)$ to $C_{0}(X, \mathbb{C})$ is a lattice homomorphism (see B-I,Sec. 3).

A semigroup ( $T(t)$ ) $t \geq 0$ is called lattice semigroup if $T(t)$ is a lattice homomorphism for all $t \geq 0$. In section 3 we will give a concrete representation of lattice-semigroups which shows that there is a large variety of examples. This section is devoted to the characterization of lattice semigroups in terms of their generators.

The heuristic idea is the following. Let (T(t)) ${ }_{t \geq 0}$ be a lattice semigroup with generator $A$. Let $f \in D(A)$ and assume that the modulus function $\theta$ given by $0(g)=|g|$ is differentiable in $f$ (in some sense which has to be made precise). Then one expects that a chain rule holds so that $\theta(T(t) f)=|T(t)|$ is differentiable at $t=0$. Since $|T(t) f|=T(t)|f|$, this implies $|f| \in D(A)$ and $A|f|$ $=d /\left.d t\right|_{t=0} \theta(T(t) f)=D_{A f} \theta(f) d / d t t_{t=0} T(t) f=\left(D_{A f} \theta(f)\right.$ Af) (where the precise meaning of (D $A f^{\rho(f) \| A f}$ depends on the chain rule which we will have to establish). So we obtain an identity for the generator A which corresponds exactly to the lattice property $|T(t) f|=$ $T(t)|f|$ of the semigroup. We will see in c-II, sec. 5 that in a Banach lattice with order continuous norm the above argument is rigorous (for all $£ \in D(A)$, on $C_{o}(X)$ we have to use a weak form of the argument and $\mid E \in \in(A)$ only holds for special $f \in D(A)$ (see Cor. 2.8j.

We start by investigating differentiability of the modulus and by establishing a chain rule. For later use we formulate the following definition and proposition for a general Banach space $G$ even though only $G=\mathbb{C}$ will be considered in this section.

Definition 2.2, Let $G$ be a Banach space and $O=G \quad G$ a mapping. Let $f \in G, u \in G$. Then $G$ is called right-sided Gateaux differentiable in $f$ in direction $u$ if
(2.3) $D_{u}{ }^{\theta}(f):=1 m_{t+o} 1 / t(\theta(f+t u)-0(f))$ exists.

The mapping $\theta$ is right-sided Gateaux differentiable in $f$ if $D_{u}$ (f) exists for all directions $u \in G$; and if $\theta$ is right-sided Gateaux-differentiable in every point $f \in G$, then we call $\theta$ right-sided Gateaux differentiable.

Proposition 2.3 (chain rule). Let $G$ be a Banach space and $k: H$ : $G$ be right-sided differentiable in a $\in \mathbb{R}$ (with right derivative $\left.k^{\prime}(a)\right)$. Suppose that $\theta: G * G$ is a Lipschitz continuous mapping. If 0 is right-sided Gateaux-differentiable in $k(a)$ in the direc-
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-15.jpg?height=50&width=1623&top_left_y=2351&top_left_x=222) a and has a right derivative
(2.4) $\quad(0 \circ k)^{\prime}(a)=D_{k^{\prime}}(a)^{\rho(k(a))}$.

Proof. There exists $L \geqq 0$ such that $\|\theta(x)-\theta(y)\| \leq L\|x-y\|$ for all $x, y \in G$. Then
$\lim _{t+0}\left\|1 / t(\theta(k(a+t))-\theta(k(a)))-D_{k}(a) \theta(k(a))\right\| \varepsilon$
1 im-supt ${ }_{t+0} \| 1 / \mathrm{t}\left(\theta(k(a+t))-\theta\left(k(a)+t k^{\prime}(a)\right) \|+\right.$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-16.jpg?height=70&width=1420&top_left_y=502&top_left_x=295)
$1 i m-s u p_{t \neq O} L \cdot\left\|l / t\left(k(a+t)-k(a)-t k^{\prime}(a)\right)\right\|_{i}+0=0$.

For $z \in C$ we let
(2.5) $\quad \operatorname{sign} z= \begin{cases}z /|z| & \text { if } z \neq 0 \\ 0 & \text { if } z=0 .\end{cases}$

Lemma 2.4. The function $\theta: \mathbb{d} \rightarrow \mathbb{d}$ given by $e(z)=|z|$ is rightsided Gateaux differentiable and

$$
D_{u} \mathrm{~b}(\mathrm{z})= \begin{cases}\operatorname{Re}[(\operatorname{sign} \bar{z}) \cdot u] & \text { if } z \neq 0  \tag{2.6}\\ |u| & \text { if } z=0\end{cases}
$$

Proof. If $z=0$, relation (2.6) ig obvious from the definiton. Let $z=\left(x_{0}+i y_{o}\right) \neq 0$. We identify $\mathbb{C}$ and $\mathbb{R}^{2}$. Then $\theta(x, y)^{\circ}=\left(x^{2}+y^{2}\right)^{1 / 2}$ is differentiable in $z$ and $D_{u} \rho(z)=\left(\operatorname{grad} \theta\left(x_{o}, y_{o}\right) \mid u\right)=1 /|z|\left(\left(x_{0}, y_{o}\right) \mid\left(u_{1}, u_{z}\right)\right)=$ $1 /|z|\left(x_{o} u_{1}+y_{o} u_{2}\right)=1 /|z| \operatorname{Re}\left(\left(x_{0}-i y_{0}\right) \cdot\left(u_{2}+i u_{2}\right)\right)=\operatorname{Re}((\operatorname{sign} \bar{z})-u ?$, where $u=u_{1}+i u_{2}=\left(u_{1}, u_{2}\right) \in a_{2}=\mathbb{R}^{2}$ and (v|u) denotes the canonical scalar product of $v, u \in \mathbb{R}^{2}$.

Let $f, g \in C_{o}(x)$. We denote by (sign f) $(g)$ the bounded Borel function given by
(2.7) $\left[(\operatorname{sign} f)(g) j(x)= \begin{cases}(\operatorname{sign} f(x)) \cdot g(x) & \text { if } f(x) \neq 0 \\ |g(x)| & \text { if. } f(x)=0 .\end{cases}\right.$

Similarly, (sign f)(g) is defined by
(2.8) $\quad[(\operatorname{sign} f)(g)](x)=(\operatorname{sign} f(x)) \cdot g(x) \quad$.

We identify the dual space of $C_{o}(X)$ with $M(X)$, the space of all bounded regular Borel measures on $X$. We extend the duality by setting

$$
<h, \phi\rangle=\int h(x) d \phi(x)
$$

for every bounded Borel function $h$ on $x$ and every $\phi \in M(x)$.

After these preparations we now can show that the lattice property $|T(t) f|=T(t)|f| \quad o f$ the semigroup corresponds to the identity (2.9) below for the generator, which we call Kato's equality (cf. Remark 2.7).

Theorem 2.5. A strongly continuous semigroup (T(t)) $t \geqslant 0$ on $C_{0}(X)$ is a lattice semigroup if and only if its generator A satisfies

$$
\begin{align*}
& \subset \operatorname{Re}[(s i \hat{G n} \bar{f})(A f)], \phi\rangle=\langle | f\left|, A^{\prime} \phi\right\rangle \\
& \text { for all } f \in D(A), \phi \in D\left(\mathcal{A}^{\prime}\right) \quad \text { (Kato's equality). } \tag{2.9}
\end{align*}
$$

From the proof of the theorem we isolate the following lemma.

Lema 2.6. Let (T(t)) ${ }_{t \geq 0}$ be a semigroup on $C_{0}(X)$ with generator $A$. Then for every $f \in D(A), \phi \in M(X)$,

$$
\begin{equation*}
d / d t_{\mid t=0}\langle | T(t) f|, \phi\rangle=\langle\operatorname{Re}[(\operatorname{sig} n \bar{f})(A f) \underline{I}, \phi\rangle \tag{2.10}
\end{equation*}
$$

Proof. Let $f(D(A)$ and $x \in X$. Define the function $k(t)=$ (T(t)f)(x) (t $\geqslant 0$ ). Then $k$ is right-sided differentiable in 0 with derivative $k^{\prime}(0)=(A f)(x)$. It follows from the chain rule Prop. 2.3 that

$$
\begin{equation*}
d / d t|t=0|(T(t) f)(x) \mid=\operatorname{Re}[(\operatorname{sig} n \vec{f})(A f)](x) \tag{2.11}
\end{equation*}
$$

Moreover, $\quad 1 / t| | T(t) f|-|f|| \leq 1 / t|T(t) f-f|$. Thus $\sup _{1 \geq t>0} 1 / t$ $\||T(t) f| \rightarrow|f|\| \varepsilon \in$; i.e., the functions $k_{t} \in C_{o}(x)$ given by

$$
\begin{equation*}
k_{t}(x)=1 / t \quad(|(T(t) f)(x)|-|f(x)|) \quad(x<x) \tag{2.12}
\end{equation*}
$$

(t $>0$ ) are uniformly dominated by a constant. The dominated convergence theorem and (2.11) imply that
$d /\left.d t_{t=0}\langle | T(t) f\right|_{, \phi\rangle}=1 i m_{t+0}\left\langle k_{t} \mid \phi\right\rangle=\langle\operatorname{Re}[(\operatorname{sig} n \mathcal{f})(A f)], \phi\rangle$.

Progf of Theorem 2.5. Assume that (T(t)) $t \geq 0$ is a Iattice semigroup. Let $£ \in D(A), \phi \in D\left(A^{\prime}\right)$. It follows from the preceding lemma that
$\langle\operatorname{Re}[(\operatorname{sig} n$ f $)(A f)], \phi\rangle=d / d t|t=0\langle | T(t) f|, \phi\rangle=d / d t|t=0<T(t)| f|, \phi\rangle=$ $\langle | f\left|, A^{\prime} \phi\right\rangle$.
Conversely, assume that (2.9) holds. Let $t>0, f \in C_{0}(X)$, We have to show that $|T(t) f|=T(t)|f|$. Since $D(A)$ is dense in $C_{0}(X)$, we can assume that $f \in D(A)$. Moreover, since $D(A ')$ is $o\left(M(X), C_{O}(X)\right)$-dense in $M(X)$, it suffices to show that

$$
\begin{equation*}
\langle | T(t) f|, \phi\rangle=<T(t)|f|, \phi\rangle \tag{2.13}
\end{equation*}
$$

for all $\phi \in D\left(A^{\prime}\right)$.
Let $\phi \in D\left(A^{\prime}\right)$ and define the function $k(s)=\langle T(t-s)| T(s) f|, \phi\rangle$
( $s \in[0, t]$ ). We claim that $k$ is right-sided differentiable with derivative $k^{\prime}(s)=0$ for all $s \in[0, t]$. This implies that $k(0)=$ $\mathrm{k}(\mathrm{t})$ which is (2.13).

Since $\phi \in D\left(A^{\prime}\right)$ we have
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-18.jpg?height=56&width=1512&top_left_y=1203&top_left_x=218)
for all $g \in C_{o}(X)$. Consequently,

$$
{\overline{\mathrm{I}} \mathrm{im}_{h \neq 0}}^{1 / h}\left\|(\mathrm{~T}(\mathrm{t}-(\mathrm{s}+\mathrm{h}))-\mathrm{T}(\mathrm{t}-\mathrm{s}))^{\prime} \phi\right\|<\mathrm{m}
$$

by the uniform boundedness principle. Hence, since
$\lim _{h+0}|T(s+h) f|=|T(s) f|,(2.14)$ implies that
(2.15) $\left.\quad \lim _{h \neq 0} 1 / h<|T(s+h) f|,(T(t-(s+h))-T(t-s))^{\prime} \phi\right\rangle=$ $\left.-\varepsilon|T(s) f|, A ' T(t-s)^{\prime} \phi\right\rangle$ *

Using this we obtain
$\lim _{h \neq 0} 1 / \mathrm{h}(\mathrm{k}(\mathrm{s}+\mathrm{h})-\mathrm{k}(\mathrm{s}))$
$=1 \mathrm{im}_{h+0} 1 / \mathrm{h}(<T(\mathrm{t}-(\mathrm{s}+\mathrm{h}))|\mathrm{T}(\mathrm{s}+\mathrm{h}) \mathrm{f}|, \phi\rangle-\langle T(\mathrm{t}-\mathrm{s})| \mathrm{T}(\mathrm{s}+\mathrm{h}) \mathrm{f}|, \phi\rangle+$ $\left.\lim _{h \neq 0} 1 / h(<T(t-s))|T(s+h) f|-T(t-s)|T(s) f|, \phi\right\rangle$
$\left.=-\varepsilon|T(s) f|, A^{\prime} T(t-s)^{\prime \prime} \phi\right\rangle+\lim _{h \downarrow 0} 1 / h<\left(|T(s+h) f|-|T(s) f|, T(t-s)^{\prime} \phi\right\rangle$.
By Lemma 2.6 the last term is
$\left.-c|T(s) f|, A ' T(t-s)^{*} \phi\right\rangle+\left\langle\operatorname{Re}[(\operatorname{sign} \bar{T}(s) f)(A T(s) f)], T(t-s)^{*} \phi\right\rangle$, and this is 0 by hypothesis.

Remark 2.7. We will see in chapter C-IT that the inequality $|T(t) f| s T(t)|f|, ~ w h i c h ~ h o l d s ~ p r e c i s e l y ~ f o r ~ p o s i t i v e ~ s e m i g r o u p s, ~$ implies the inequality corxesponding to (2.9). For $A_{B}=A$ (the Laplacian) this is a version of the classical Kato's inequality.

Corollary 2.8. Let (T(t)) tzo be a lattice semigroup on $C_{o}(X)$ with generator $A$. $I f f \in D(A)$ and $f(x) \neq 0$ for all $x \in X$, then $\dot{f} \mid \in D(\bar{R})$ and $\operatorname{Re}[(\operatorname{sign} \bar{f})(A f)]=A|f|$.

Proof. If $f \in D(A)$ and $f(x) \neq 0$ for all $x \in x$, then $(\operatorname{sign} \bar{f})(A f)=(\operatorname{sign} \bar{f})(A f) \in C_{o}(y)$. Hence by (2.9),
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-19.jpg?height=55&width=1617&top_left_y=612&top_left_x=228) tion follows from the following lemma.

Lemma 2.9. Let $A$ be a densely defined closed operator on a (real or complex) Banach space $G$. Let $f, G \in G$ such that $\langle f, \phi\rangle=\left\langle g, \mathcal{R}^{\prime} \phi\right\rangle$ for all $\phi \in D(A \prime)$. Then $g \in D(A)$ and $A g=f$.

Proof. Denote by $G(A):=\{(h, A h): h \in D(A)\}$ G×G the graph of A. Assume that ( $g, f$ ) $\frac{k}{f}(A)$. Since $G(A)$ is closed, it follows from the Hahn-Banach theorem that there exists $\left(\psi_{1}, \psi_{2}\right) \in G^{\prime} \times G^{\prime}$ such that $\left\langle h, \psi_{1}\right\rangle+\left\langle A h, \psi_{2}\right\rangle=0$ for all $h \in D(A)$ and $\left\langle g, \psi_{1}\right\rangle+\left\langle f, \psi_{2}\right\rangle \frac{1}{T} 0$. By the definition of $A^{\prime}$ this implies that $\psi_{2} \in D\left(A^{\prime}\right)$ and $A^{\prime} \psi_{2}=-\psi_{1}$. Hence $\left.\left\langle f_{1} \psi_{2}\right\rangle \neq-<g, \psi_{1}\right\rangle=\left\langle g, A \psi_{2}\right\rangle$. So the condition in the lemma is violated.

Next twe prove a converge of Corollary 2.8.

Theorem 2.10. Let $A$ be the generator of a real semigroup ( $T(t)$ ) $t \geqq 0$ on $C(K, \mathbb{C})$, where $K$ is compact. Then (T(t)) $t \geqq 0$ is a lattice semigroup if and only if
$f \in D(A), f(x) \neq 0$ for all $x \in K$ implies $|f| \in D(A)$ and A $|f|=\operatorname{Re}((\operatorname{sign} \overline{\mathrm{I}}) \mathrm{Af})$.

Remark. Although we assume that $(T(t)) t \geq 0$ is a real semigroup (i.e., T(t)C(K,R) $\subset C(K, \mathbb{R})$ for all $t \geqslant 0$, it is important for the proof that we consider the space of all complex-valued continuous functions on $K$, In fact, if $K$ is connected, the condition in the theorem is always trivially satisfied for all $£ \in \mathbb{C}(\mathbb{R}, \mathbb{R})$.

Proof. It follows from cor. 2.8 that the condition is necessary. So assume that the condition is satisfied. Since (T(t)) $t=0$ is real, the restriction $T_{\mathbb{R}}(t)$ of $T(t)$ to $C(K, R)$ ( $\geqq \geqslant$ ) defines a strongly continuous semigroup. Its generator $A_{\mathbb{R}}$ is a restriction of $A$. since $D\left(A_{\mathbb{R}}\right)$ is dense in $C(\mathbb{K}, \mathbb{R})$, there exists a strictly positive
$u \in D\left(A_{\mathbb{R}}\right)$. Moreover, $\lim _{t \rightarrow 0} T(t) u=u$ uniformly. Thus there exists $t_{0}>0$ such that $T(t) u$ is strictly positive for all $t \in\left[0, t_{o}{ }^{7}\right.$.
Let $f \in D\left(A_{R}\right)$. For $\varepsilon>0$ let $f_{\varepsilon}=f+i \in u$. Then $T(t) f_{\varepsilon} \in D(A)$ and $\left|T(t) f_{\epsilon}\right|$ is strictly positive for all $t \in\left[0, t_{o}\right]$. By hypothesis, $\left|T(t) f_{\varepsilon}\right| \in D(A)$ and $\operatorname{Re}\left(\left(\operatorname{sign}\left(T(t) \bar{f}_{E}\right)\right) A T(t) f_{E}\right)=A\left|T(t) f_{E}\right|$ for all $t \in\left[0, t_{0}\right]$. One sees as in the proof of Thm. 2.5 that this implies that $\left|T(t) f_{E}\right|=T(t)\left|f_{E}\right|$ for $a l l t \in\left[0, t_{Q}\right]$. Letting $\varepsilon \rightarrow 0$ one obtains that $|T(t) f|=T(t)|f| \quad\left(t \in\left[0, t_{0} \boldsymbol{f}\right)\right.$. Since $D(A)$ is dense in $C(K, \mathbb{R})$ we conclude that $|T(t) f|=T(t)|f|$ for all $f \in C(K, \mathbb{R})$ and all $t \in\left[0, t_{0}{ }^{1}\right.$. Let $s>t_{o}$. Then $s / n \leqq t_{o}$ for some $n \in \mathbb{N}$. Hence $|T(s) f|=\left|T(s / n)^{n_{f}}\right|=T(s / n)^{n}|f|=T(s)|f|$ for all $f \in C(K, \mathbb{R})$. We have shown that $T_{\mathbb{R}}(t)$ is a lattice homomorphism for all $t \geq 0$; hence $T(t)$ is so as well (cf. Rem. 2.1).

Corollary 2.11. Let $A$ be the generator of a lattice semigroup on $C(K, C)(K$ compact). Assume that $m \in C(K)$ is strictly positive. Then $m \cdot A$ with domain $D(m \cdot A)=D(A)$ generates a lattice semigroup.

Proof. By Theorem 1.20 m-A is the generator of a strongly continuous semigroup. It remains to show that it is a lattice semigroup. We use Theorem 2.10. Let $f \in D(m \cdot A)=D(A)$ such that $f(x) \neq 0$ for all $x \in K$. Then $\operatorname{Re}[(\operatorname{sign} \bar{f}) m \cdot A f]=m \cdot \operatorname{Re}[(\operatorname{sign} \bar{f}) A f]=m \cdot A|f|$.

Example 2.12. The operator $A_{\text {max }}$ on the (real or complex space)
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-20.jpg?height=73&width=1615&top_left_y=1768&top_left_x=209) satisfies Kato's equality; i.e.,

$$
\begin{gather*}
\left.\left\langle\operatorname{Rer}_{\mathcal{E}}(\operatorname{sign} \bar{f})\left(\mathcal{A}_{\max } f\right)\right], \phi\right\rangle=\langle | f\left|, A_{\max }^{\prime} \phi\right\rangle  \tag{2.16}\\
\left(f \in D\left(A_{\max }\right), \phi \in D\left(A_{\max }^{\prime}\right)\right) .
\end{gather*}
$$

Moreover, ( $\lambda-A_{\text {max }}$ ) is surjective for $\lambda \geqq 0$ (cf. Ex. 1.22 ). Thus, since $\operatorname{ker}\left(\lambda-A_{\max }\right)=\mathbb{C e}_{\lambda} \quad\left(e_{\lambda}(x)=e^{\lambda x}\right)$, Kato's equality does not have as strong consequences as the positive minimum principle (which by Thm. 1.13 would imply that $A_{\text {max }}$ is a generator).

Proof. It is not difficult to prove that the adjoint A max of $A_{\text {max }}$ is given by
(2.17)

$$
\bar{A}_{\max }^{\prime} \phi=\phi(0) \delta_{o}-\phi(-1) \delta_{-1}-\mathrm{d} \phi
$$

with domain $D\left(A_{\text {max }}^{\prime}\right)=B V[-1,0]$ the space of all functions of bounded variation on $\left[-1,0!\right.$ ). Here we identify $B V[-1,0]\left[L^{1}[-1,0]\right.$ with a subspace of $C[-1,0]$ by setting $\langle f, \phi\rangle=\int_{-1}^{C l} f(x) \phi(x) d x$ (f $\in C[-1,0], \phi \in B V[-1,0]$ ) . For $\phi \in B V[-1,0]$, d $\phi$ denotes the linear form on $C[-1,0]_{-}$given by $f \rightarrow \int_{-1}^{0} f(\gamma) d \phi(x)$.
We now show $(2,16)$. Let $\left.\left.f \in D^{(A} A_{\text {max }}\right)=C^{I}-1,0\right]$, $\in \operatorname{D}\left(A_{\text {max }}^{\prime}\right)=$ BV[-1,0] . By Lemma 2.4 and the chain rule (Prop. 2.3) we have
$\mid f(x)!^{\prime}\left(:=d^{+} / d t|t=x \quad| f(t) \mid=\operatorname{Re}\left[(\operatorname{sign} \bar{f}) f^{\prime} \mid(x) \quad\left(\right.\right.\right.$ where $f^{\prime}(x)=$
(Ref)' $(x)+i(J m f)^{\prime}(x)$ in the complex case). Thus
Re[(sign $\bar{f}) A f \underline{f}, \phi\rangle=\int_{-1}^{0}\left|f(x): \phi(x) d x=\int_{-1}^{0} \phi(x) d\right| f(x) \mid=$
$\phi(0)|f(0)|-\phi(-1)|f(-1)|-\int_{-1}^{0}|f(x)| d_{\phi}(x)=\langle | f\left|, A_{\text {max }}^{\prime}\right\rangle$.

Example 2.13. Let $A$ on (the real or complex) space cr-1,0] be given by $A f=f^{\prime}$ with domain $D(A)=\left\{A^{\prime} \in C^{l}[-1,0]: f^{*}(0)=\right.$ Lf $\}$ where $L \in M[-1,0:=C[-1,0]$. Then $A$ is the generator of a lattice semigroup if and only if $L=a \delta_{0}$ for some $\alpha \geq 0$.

Proof. Assume that $A$ is the generator of a lattice semigroup $(T(t))_{t \geq 0}$. There exists $\mu(M[-1,0\rangle$ satisfying $\mu([0\})=0$ and $\alpha \in \mathbb{R}$ such that $L=a s_{0}+\mu$. We claim that
(2.18) $\mid\langle f, k\rangle=\langle!f \mid, H\rangle$ for all $f \in D(A)$ satisfying $f(0)=0$. In fact, by the definition of $A$ we have
(2.19) $\delta_{0} \in D\left(A^{\prime}\right)$ and $A^{\prime} \delta_{0}=L$.

Moreover, by Thm. 2.5, A satisfies Kato's inequality (2.9). Since $\mathrm{f}(0)=0$ this implies

$$
(\text { by }(2.9))
$$

![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-21.jpg?height=50&width=1617&top_left_y=2168&top_left_x=228) \{f $\left.\in C^{1}[-1,0]: f(0)=0\right\}$ which is discontinuous for the supremum norm, the space $D(A)=k e r \phi$ is dense in $F$ and consequently dense in $C_{o}[-1,0)$. It follows that (2.18) holds for all $f \in C_{o}^{[-1,0)}$. So by $B-I, S e c .2$, there exist $\beta \geqslant 0$ and $x \in[-1,0)$ such that $f=\beta \delta_{x}$. Assume that $B \neq 0$. It is easy to see that there exists a real function $f \in C^{l}[-1,0]$ satigfying $f^{\prime}(0)=\alpha f(0)+\beta f(x)$ and
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-21.jpg?height=55&width=1386&top_left_y=2577&top_left_x=229) $(\operatorname{sign} f(0)) f^{\prime}(0)=(\operatorname{sign} f(0))(\alpha f(0)+\beta f(x))=$

$$
\begin{aligned}
& =\left\langle\operatorname{Re}[(\operatorname{sign} f)(\bar{R} f)], \delta_{0}\right\rangle=\langle | f\left|, A^{\prime} \delta_{O}\right\rangle \\
& =\langle | f|, 山\rangle \text {. }
\end{aligned}
$$

$\left.\alpha|f(0)|+\beta(\operatorname{sign} f(0)) f(x) \neq \alpha|f(0)|+\beta|f(x)|=<|f|, a \delta_{0}+\beta \delta_{x}\right\rangle=$
$\langle | f\left|\mathcal{R}^{\prime} \delta_{0}\right\rangle$. This contradicts (2.9). We have shown that $\beta=0$; i.e., $L=a 0_{0}$.
The converse can be shown by using Thm. 2.5 again. However, if
$L=\alpha \delta_{o}$, then it is easy to see that $A$ generates the semigroup (T (t)) tzo given by
$(T(t) f)(x)= \begin{cases}f(x+t) & \text { if } x+t<0 ; \\ e^{t \alpha} f(0) & \text { if } x+t \geqq 0 .\end{cases}$
So (T(t)) $t \gtreqless 0$ is clearly a lattice semigroup.

## 3. SEMIFLOWS, FLOWS AND POSITIVE GROUPS

In this section we establish a relation between generators of lattice homomorphisms and derivations. On the space $C_{0}(\mathbb{R})$, for example, this will enable us, to give a detailed description of all generators of positive groups.

At first we consider a compact space $K$ and denote by $C(K)=C(K, \mathbb{R})$ the space of all real valued continuous functions on $K$. The extension of the subsequent results to the complex spaceis obvious.

A lattice homomorphism $T$ on $C(K)$ is an algebra homomorphism if and only if $T$ l $=1$ (see B-I,Sec. 3). We start by describing semigroups of algebra homomorphisms on $C(K)$.

Definition 3.1. A mapping $\quad$ : $\left[0,{ }^{\infty}\right) \times K \rightarrow K$ is called semiflow if for each $t \geqq 0$ the mapping $\phi_{t}$ given by $\phi_{t}(x)=\phi(t, x)$ is continuous and

| (3.1) $\phi_{s} \phi_{t}=\phi_{s+t}$ | for all $s, t \geq 0$ |
| :--- | :--- |
| (3.2) $\phi_{o}(x)=x$ | $(x \in K)$. |

A semiflow $\phi$ on $K$ induces a family (T(t)) tap of algebra homomorphisms on $C(K)$ by
(3.3) $T(t) f=f 0 \phi_{t}$.

Then clearly $T(t) T(s)=T(t+s)(t, s \geq 0) ;$ i.e., (T(t)) $t \geqq 0$ has the
semigroup property. Conditions for strong continuity are given in the following lemma.

Lemma 3.2. The following assertions are equivalent:
(i) The mapping $\phi: \mathbb{R}_{\not} \times K \rightarrow K$ is continuous (where $\mathbb{R} \times K$ carries the product topology).
(ii) The mapping $\phi$ is separately continuous.
(iii) (T(t)) $t_{20}$ is a strongly continuous semigroup on $C(K)$.

Proof. (i) trivially implies (ii).
If (ii) holds, then $t \rightarrow T(t) f$ is weakly continuous for every $f \in C(K) \quad$ (by the theorem of dominated convergence). This implies strong continuity (see for example [Davies (1980); Prop. 1.23]).

It remains to show that (iii) implies (i). Because of (3.1) it suffices to show that the restriction $\phi_{O}$ of $\phi$ to $[0,1) \times k$ is continuous. By hypothesis, the mapping $W$ : $F \rightarrow$ ( $t \rightarrow T(t) f$ ) from $C(k)$ into $C([0,1], C(K))$ is continuous. ldentifying $C([0,1], C(K))$ canonically with $C([0, l] \times k)$ the mapping $W$ obtains the form $f+f_{0}$. since $W$ is continuous, $\phi_{o}$ is continuous as well.

A semiflow is called continuous if it satisfies the equivalent conditions of Lemma 3.2.

Definition 3.3. An operator $\delta$ on $C(K)$ is called derivation if $D(\delta)$ is a subalgebra of $C(K)$ such that
(3.4) $\delta(f-g)=(\delta f) g+f(\delta g)$ for all $f, g \in D(\delta)$.
(3.5) $\quad 1 \in D(\delta)$

Note that (3.4) implies $\delta 1=0$.
A lattice semigroup (T(t)) $t \geqq 0$ on $C(K)$ is called Markovian if $T(t) 1=1$ for all $t \geq 0$.
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-23.jpg?height=53&width=1617&top_left_y=2121&top_left_x=228) A . The following assertions are equivalent.
(i) (T(t)) $t \geq 0$ is a Markovian lattice semigroup.
(ii) $T(t)$ is an algebra homomorphism for every $t \geqq 0$.
(iii) There exists a continuous semiflow $\phi$ on $K$ such that $T(t) f=f \circ \phi_{t} \quad(t \geqslant 0)$.
(iv) $A$ is a derivation.

Proof. (i) and (ii) are equivalent by the remark at the beginning of this section.

Assume that（ii）holds．Then there exists a continuous mapping $\phi_{t}: K \rightarrow K$ such that $T(t) f=f \phi_{t}$ for all $f \in C(K)$（see B－I，Sec． 3 ）． The semigroup property implies that $\left(\phi_{t}\right){ }_{t} \geqq 0$ is a continuous semi－ flow．This shows（iii）to hold．
If（iii）holds，then $T(t) l=1$ for all $t \geqq 0$ hence $1 \in D(A)$ and $A 1=0$ ．Let $f, g \in D(A)$ ．Then $d /\left.d t\right|_{t=0} T(t)(f \cdot g)=$ $d /\left.d t\right|_{t=0}(T(t) f) \cdot(T(t) g)=(A f) \cdot g+f \cdot(A g)$ ．Thus $f \cdot g \in D(A)$ and （3．4）holds．Hence $A$ is a derivation．
Finally assume that（iv）holda．We prove（ii），i．e．，we have to show that $T(t)(f, g)=T(t) f \cdot T(t) g$ for $t>0$ ．Since $D(\vec{A})$ is a dense subalgebra，we can assume that $f, g \in D(A)$ ．Define $n:[0, t]+C(K)$ by $\quad \eta(s):=T(t-s)[T(s) f \cdot T(s) g]$ ．Then $\eta_{1}(0)=T(t)(f \cdot g)$ and
$\eta(t)=T(t) f(T) g$ ．Since $A$ is a derivation，$\eta^{\prime \prime}(s)=0$ for $s \in[0, t]$ ．Hence $m(0)=\pi(t)$ ．This ghows（ii）to hold．

If $\hat{i}$ is the generator of a semigroup（T（t））$t \geq 0$ given by $T(t) f=f \circ \phi_{t}$ ，then we call $\phi$ given by $\phi(t, x)=\phi_{t}(x)$ the semiflow associated with（T（t））${ }_{t \geq 0}$（or associated with $\delta$ ）．We now can describe the generator of any lattice semigroup as a perturbation of a derivation．If 1 is in the domain of the generator，an additive perturbation（by a multiplication operator）suffices；in general a similarity transformation has to be applied in addition．This is the assertion of the following two theorems．

Theorem 3．5．Let $A$ be a generator of a semigroup（T（t））$t \geqq 0$ on $C(K)$ ．Suppose that $l \in D(A)$ ．Then the following assertions are equivalent．
（i）（T（t））${ }_{t ⿱ 丶 万 ⿱ ⿰ ㇒ 一 乂 心}$ is a lattice semigroup．
（ii）There exist a derivation $\delta$（generating a semigroup of algebra homomorphigms）and a multiplier $h \in C(K)$ such that $A=\delta+h$ （i．e．，$D(\bar{B})=D(\delta)$ and $\bar{A}=\delta f+h \cdot f$ for $f \in D(A)$ ）．

Moreover，if（ii）holds，then（T（t））$t \geqslant 0$ is given by
（3．6）（T（t）f）（x）＝ $\exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right) \cdot f(\phi(t, x))$
where $\phi$ is the semiflow associated with $\delta$ ．

Proof．Let $h=A l$ and $\delta=A-h$ ．Then the semigroup $\left(T_{o}(t)\right) t \geqslant 0$ generated by $f$ is a lattice semigroup if and only if（T（t）） $4 \geq 0$ is a lattice semigroup［since $T_{o}(t) f=\lim _{n+\infty}\left(e^{-t / n \cdot h} \cdot T\left(\frac{t}{n}\right)\right)^{n_{f}}$ and
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-24.jpg?height=78&width=1620&top_left_y=2674&top_left_x=212)
$A-I I,(1.8)$. Since $f 1=0$ one has $T_{o}(t) l=1$ for all $t \geq 0$ and the equivalence of (i) and (ii) follows with the help of Theorem 3.4. Now assume that (i) and (ii) hold. Let

$$
(S(t) f)(x)=\exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right) \cdot f(\phi(t, x))
$$

for all $x \in K, f \in C(R), t \geq 0$. Then one easily shows that (s (t)) ${ }_{t}$ ? is a strongly continuous semigroup. Denote by $B$ its generator. For $f \in D(\delta),\left.\frac{d}{d t}\right|_{t=0} S(t) f=h+f+\delta f$. Hence $\delta+h$ G . since $\delta+h$ also is a generator, it follows that $\delta+h=B$.

Theorem 3.6. An operator $A$ is generator of a lattice semigroup on $C(K)$ if and only if there exists a derivation of which is a generator, a function $h \in C(K)$ and a strictly positive function $P \in C(K)$ such that
(3.7) $\quad \mathrm{A}=\mathrm{M} \delta \mathrm{M}^{-1}+\mathrm{h}$
where $M \in(C(K))$ is given by $M f=p \cdot f$.

Proof. In order to show the non-trivial implication assume that $A$ generates a lattice semigroup. Since $D(A)$ is dense in $C(K)$, there exists $0 \ll \mathcal{P} \in D(A)$. Let $h(x)=(A p)(x) / p(x)$. The operator given by Mf $=f \cdot \mathrm{P}$ is a lattice isomorphism. Thus $\delta:=M^{-1}(A-h) M$ generates a lattice semigroup. Since $M 1=P \in D(A)$ one has $1 \in D(f)$ and $\delta 1=M^{-1}(A-h) p=0$. Thus $\delta$ is the generator of a semigroup of algebra homomorphisms, hence a derivation by Theorem 3.4.

At the end of this section we will show that any derivation on $C[0,1]$ which generateg a group is similar to a differential operator of firgt order. This in connection with Theorem 3.6. will enable us to describe all generators of positive groups as perturbations of a differential operator.
In Section 1 we had obtained a very simple condition describing generators of positive semigroups on $C(K)$ by the positive minimum principle and a range condition. This result yields a characterization of generators of automorphism groups by "locality" and a range condition. By an automorphism we understand an algebra isomorphism of $C(K)$ onto itself.

Theorem 3.7. Let $A$ be a densely defined operator on $C(K)$. The following assertions are equivalent.
(i) $A$ is the generator of an automorphism group.
(ii) $\quad 1 \in D(A)$ and $A=0 ;( \pm 1-A) D(A)=C(K)$ and $A$ is local, in the sence that for $0 \leqq f \in D(A)$. $f(x)=0$ implies $(A f)(X)=0 \quad(x \in K)$.

Proof. An invertible operator $T$ such that $T \geqq 0$ and $T^{-1} \geqq 0$ is an automorphism if and only if $T l=1$. Hence $A_{B}$ is the generator of an automorphism group if and only if $A$ and -A generate a positive group, $1 \in D(A)$ and $A l=0$. Thus Theorem 3.7. follows from Theorem 1.13.

Remark. It is remarkable that from locality, the range condition and $1 \in D(A), A l=0$ it follows that $D(A)$ actually is a subalgebra of $C(K)$ and $A$ is a derivation. The "order-theoretical" property of locality is in some aspects stronger than the algebraic property of being a derivation. For example a local, densely defined operator is closable (by Prop.l.ll) ; but there exist derivations on $C[0,1]$ which are not closable (see Bratteli-Robinson (1975)).

Remark (an excursion to $C^{*}$-algebras).
Theorem 3.7 also holds for non-commutative $c^{*}$-algebras. More precisely: Let $A$ be a $C^{*}$-algebra with unit $l$ and let $A_{h}$ be the real Banach space of all hermitian elements in $A$. Then $A_{h}$ is a real ordered Banach space and 1 is an interior point of $\left(A_{h}\right)_{+}$. Let $A$ be a densely defined operator on $A_{h}$.
Then $A$ is the generator of an automorphism group if and only if $1 \in D(A)$ and $A l=0 ;( \pm 1-A)(D(A))=A_{h}$ and $A$ is local in the sense that for $0 \leqq x \in D(A), 0 \leqq \phi \in\left(A_{h}\right)^{\prime}, \phi(x)=0$ implies $\phi(\mathrm{AX})=0$.
The proof of Theorem 3.7 can be carried over to this case if one notices the following. A strongly continuous group $T(t) t \in \mathbb{R}$ on $A_{h}$ is an automorphism group if and only if it is positive and $T(t) l=1$ for all $t \in \mathbb{R}$ [see Bratteli-Robinson (1979), Cor. 3.2.21].

Now we let $X$ be a locally compact space and consider positive groups on $C_{o}(X)=C_{o}(X, R)$, the space of all continuous real-valued functions on $x$ which vanish at infinity. Our aim is to describe their generators as perturbations of generators of automorphism groups; i.e., we will extend Theorem 3.6 by allowing $X$ to be noncompact but
restrict ourselves to positive groups (or equivalently semigroups of lattice isomorphisms). And in fact, it is not difficult to show by an exarmple that the corresponding result is wrong for lattice semigroups in general.
$A$ mapping $\phi: \mathbb{R} \times x+x$ ig called a flow on $X$ if the partial maps $\phi_{t}: X * X$ given by $\phi_{t}(x)=\phi(t, x)$ are continuous and satisfy

| $(3.8)$ | $\phi_{o}(x)=x$ | $(x \in x)$ |
| :--- | :--- | :--- |
| $(3.9)$ | $\phi_{s}^{0 \phi_{t}}=\phi_{s+t}$ | $(s, t \in \mathbb{R})$. |

It follows from the definition that each $\phi_{t}$ is a homeomorphism on $X$ and $\phi_{-t}=\left(\phi_{t}\right)^{-1}$.
$A$ flow $\phi$ is called continuous if it is continuous with respect to the product topology on $\mathbb{R} \times \mathrm{x}$.
Given a flow $\phi$ a family $\left(h_{t}\right)_{t \in R} \subset c^{b}(X)$ is called a cocycle of $\phi$ if
$(3.10) \quad h_{0}=1$
(3.11) $\quad h_{t+5}=h_{t} \cdot\left(h_{s} 0 \phi t\right) \quad(s, t \in \mathbb{R})$.

It follows from (3.10) and (3.11) that $h_{t}(x) \neq 0$ for all $x \in x$ and $1 / h_{t}(x)=h_{-t}\left(\phi_{t}(x)\right)(t \in \mathbb{R})$. The cocycle is called continuous if the mapping $(t, x) \rightarrow h_{t}(x)$ from $\mathbb{R} \times x$ into $\mathbb{R}$ is continuous with respect to the product topology on $\mathbb{R} \times x$.
Let $\phi$ be a flow and $\left(h_{t}\right)_{t \in f}$ a cocycle of $\phi$. Then
(3.12) $T(t) f=h_{t} \cdot f \phi_{t}$
defines a bounded operator $T(t)$ on $C_{o}(X)$ ( $t \in \mathbb{R}$ ). Clearly $T(s+t)=T(s) T(t)$ for $a l l$ $s, t \in \mathbb{R}$.

Proposition 3.8. Tet $\ddagger: \mathbb{R} \times x+x$ be a flow and ( $h_{t}$ ) $t \in \mathbb{R}$ a cocycle of $\phi$. If for every $x \in x$ the mappings $t * \phi_{t}(x)$ and $t \rightarrow h_{t}(x)$ are continuous, then (3.12) defines a strongly continuous group.

Proof, We first note that $\|T(t)\|$ is bounded on compact intervala of $\mathbb{R}$. This follows from [Hille-phillips (1957), 7.4.1] since $q(t)=\log \|T(t)\|$ defines a subadditive, measurable function from $\mathbb{R}$ into $\mathbb{R}$. [In fact, $\|T(t)\|=\sup _{x \in X}\left|h_{t}(x)\right|$ for $t \in \mathbb{R}$. So it follows from the assumption that $t \rightarrow\|T(t)\|$ is lower semicontinuous and hence measurablel. If $f \in C_{o}(x)$, then by hypothesis the function
$t \rightarrow h_{t}(x) f(\phi(t, x))=(T(t) f)(x)$ is continuous on $\mathbb{R}$. It follows from the dominated convergence theorem that $T(\cdot) f$ is weakly continuous. Hence (T(t)) $t \in \mathbb{R}$ is strongly continuous (see e.g*, [Davies (1980), Prop. 1.23 〕).

The group defined by (3.12) is positive whenever $\left(h_{t}\right)_{t \in \mathbb{R}} \in C^{b}(x){ }_{+}$* We now show that every positive group on $C_{o}(x)$ is of the form (3.12).

Proposition 3.9. Let (T(t)) tefi be a strongly continuous group of positive operators on $C_{o}(x)$. Then there exist a continuous fiow on $x$ and a continuous cocycle $\left(h_{t}\right)_{t \in n}$ of $\phi$ such that (3.12) holds.

Proof. Since $T(t)$ and $T(t)^{-1}=T(-t)$ are positive operators, $T(t)$ actually is a lattice isomorphism. Then there exist a homeomorphism $\phi_{t}$ on $X$ and $h_{t} \in C^{b}(X)+$ such that $T(t) f=h_{t} \cdot f_{0} \phi_{t}$ for all $f \in C_{0}(x)(t \in \mathbb{R})$. The group property of (T(t)) $t \in \mathbb{R}$ then implies that $\phi(t, x):=\phi_{t}(x)$ defines a flow on $x$ and that $\left(h_{t}\right)$ tef is a cocycle of $\phi$. It remains to show that $\phi$ and $\left(h_{t}\right) t \in R$ are continuous.
At first we consider the flow. Since we have $\phi_{t+s}=\phi_{t} \phi_{g}$ and every $\phi_{t}$ is a homeomorphism on $x$, it is enough to establish continuity of $\phi$ at points $\left(0, x_{0}\right) \in \mathbb{R} \times x$. Given a compact neighbourhood $V$ of $x_{0}=\phi\left(0, x_{0}\right)$, there exists a continuous function $f: x$ * $[0,1]$ satisfying $f\left(x_{0}\right)=1$ and supp $f \subset V$. There exists $t_{o}>0$ such that $\|T(t) f-f\|<\frac{1}{2}$ for $|t| \leqq t_{0}$. Let $W:=\left\{x \in X: \left\lvert\, f(x)!>\frac{1}{2}\right.\right\}$ then for $|t| \leqslant t_{0}$ and $x \in W$ we have $\left|h_{t}(x) \cdot f(\phi(t, x))-f(x)\right|<\frac{1}{2}$ and $|f(x)|>\frac{1}{2} ;$ hence $f(\phi(t, x)>0$. This implies that $\phi(t, x) \in V$ whenever $|t| \leqq t_{o}$ and $x \in w$.
To prove continuity of the cocycle we first remark that by strong continuity of (T(t)) $t \in \mathbb{R}$ the mapping ( $t, x$ ) $(T(t) f)(x)$ is continuous on $\mathbb{R} x X$ for every fixed $f \in C_{o}(x)$. Given compact subsets $A \in \mathbb{R}, B \subset X$, the set $C:=\phi(R \times B)$ is compact; hence there exists $f \in C_{o}(X)$ such that $\left.f\right|_{C}=1$. $\operatorname{For}(t, x) \in A \times B$ we have $h_{t}(x)=$ (T(t)f) (x). Thus $(t, x) * h_{t}(x)$ is continuous on $A_{1} \times B$.

Corollary 3.10. Let $\phi$ be a separately continuous flow. Then $\phi$ is continuous. If $\left(h_{t}\right) t \in \mathbb{R}$ is a cocycle of $\phi$ such that $t \rightarrow h_{t}(x)$ is continuous for every $x \in X$, then $\left(h_{t}\right) t \in \mathbb{R}$ is continuous.

This follows from Prop.3.8 and Prop.3.9.

Example 3.11. Let $\phi$ be a continuous flow on $X$.
a) Let $P$ be a continuous function on $X$ such that $i n f_{X \in X} p(x)>0$ and $\sup _{X \in X} P(x)<\infty$. Then
(3.13) $\quad \mathrm{P}_{\mathrm{t}}:=\mathrm{p} / \mathrm{po} \mathrm{\phi}_{\mathrm{t}} \quad(\mathrm{t} \in \mathbb{R})$
defines a continuous cocycle of $\phi$.
b) For $h \in c^{b}(x)$ define

$$
\begin{equation*}
h_{t}(x):=\exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right) \tag{3.14}
\end{equation*}
$$

Then ( $h_{t}$ ) $t \in \mathbb{R}$ is a continuous cocycle of $\phi$ (compare (3.6)).

Cocycles as defined by (3.13) are always globally bounded. In general this is false for cocycles of the second type. On the other hand, a cocycle described by (3.14) is differentiable with respect to $t$. This is not satisfied by cocycles of the first type in general. Thus neither (3.13) nor (3.14) gives a description of arbitrary cocycles. However every positive cocyle is a product of cocycles of the form (3.13) and (3.14). More precisely, we have the following lemma.

Lemma 3.12. Let $\phi$ be a continuous flow on $X$ and $\left(k_{t}\right)_{t \in \mathbb{R}}: C^{b}(X){ }_{+}$ a continuous cocycle of $\phi$. Then there exist $p \in C^{b}(x)$ satisfying $i n f_{x \in X} p(x)>0$ and $h \in C^{b}(X)$ such that
(3.15) $\quad k_{t}(x)=\left(p(x) / p(\phi(t, x)) \cdot \exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right.\right.$
for all $t \in \mathbb{R}, x \in X$.

Proof. We first note that there exist constants $M, w \geqq l$ such that

$$
\begin{equation*}
\left(M e^{(w-1)|t|}\right)^{-1} \leq k_{t}(x) \leq M e^{(w-1)|t|} \text { for all } t \in R, x \in x \text {. } \tag{3.16}
\end{equation*}
$$

In fact, let $(T(t))_{t \in R}$ be the group given by $T(t) f=k t^{*} f o \phi_{t}$ $\left(t \in \mathbb{R}, f \in C_{o}(X)\right)$. Then there exist constants $M, w \geq 1$ such that $(3.17)\|T(t)\| \leq \mathrm{Me}^{(w-1)|t|}$
for all $t \in \mathbb{R}$. since $\|T(t)\|=\sup _{x \in X} k_{t}(x)$ the right inequality of
(3.16) follows. Moreover, $k_{-t}=1 / k_{t}^{\circ} \phi_{-t}$. Hence $\|T(-t)\|$
$=s \operatorname{sp}_{X \in X} 1 / k_{t}(x)=\left[i n f_{X \in X} k_{t}(x)\right]^{-1}$. So (3.17) also implies the firgt inequality in (3.16).
Now we define $p$ and $h$ by

$$
p(x):=\int_{0}^{\infty} e^{-w s} k_{g}(x) d s, h(x)=w-1 / p(x) \quad(x \in x) .
$$

Then $P$ is a continuous function and we have $\left(M(2 w-1)^{-1}=\right.$
$=\int_{0}^{\infty} e^{-w s}\left(M e^{(w-1) s}\right)^{-1} d s$ w $p(x) \leq \int_{0}^{\infty} e^{-w s} M e^{(w-1) s} d s=M \quad$ for all
$x \in X$. In particular, it follows that $h \in C^{b}(X)$.
For all $x \in X, t \in \mathbb{R}$ we have
$k_{t}(x) \cdot p(\phi(t, x))=\int_{0}^{\infty} e^{-w s} k_{t+g}(x) d s=e^{w t} \int_{t}^{\infty} e^{-w s} k_{s}(x) d s$.
Now fix $x \in X$ and define $f: \mathbb{R} \rightarrow \mathbb{R}$ by
$f(t):=k_{t}(x) p\left(\phi(t, x) / p(x)=\left[e^{w t} / p(x)\right] \cdot \int_{t}^{\infty} e^{-w S_{k}}(x) d s\right.$.
The function $f$ is differentiable and satisfies the following differential equation $f^{\prime}(t)=w f(t)-k_{t}(x) / p(x)=h(\phi(t, x)) f(t)$. Moreover $f(0)=1$. Hence $f(t)=\exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right)$ for every $t \in \mathbb{R}$. This is (3.15).

As before we call a group $\left(T_{0}(t)\right)$ teR on $C_{0}(X)$ an automorphism group if each $T_{o}(t)$ is an algebra isomorphism on $C_{o}(X)$. Analogously an operator $\delta$ on $C_{o}(x)$ is called a derivation if $D(f)$ is a subalgebra of $C_{o}(X)$ and $\delta(f \cdot g)=(\delta f) \cdot g+f \cdot(\delta g)$ for all $f, g \in D(\delta)$.

Proposition 3.13. Let $\left(T_{0}(t)\right)_{t \in \mathbb{R}}$ be a group on $C_{0}(x)$. The following assertions are equivalent.
(i) ( $T_{o}^{(t))} t \in A^{(i s}$ an automorphism group.
(ii) There exists a continuous flow $\phi$ on $X$ such that

$$
T_{0}(t) f=f_{0} \phi_{t} \quad\left(f \in C_{o}(X), t \in \mathbb{R}\right)
$$

(iii) The generator of $\left(T_{o}(t)\right)$ tek is a derivation.

Proof. Every automorphism group is positive. So by Prop. 3.9 it is defined via (3.12) by some continuous flow and cocycle. It is easy to see that the cocycle is identically 1 . Thus (i) implies (ii). One shows as in Theorem 3.4 that (ii) implies (iii) and (iii) implies (i).

If $\left(T_{0}(t)\right), \in \mathbb{R}$ is an automorphism group with generator $\delta$ we call $\phi$ in (ii) of Prop. 3.13 the flow associated with ( $T_{o}$ (t)) $t \in \mathbb{F}$ (or associated with \& ).
Now we can show that every generator of a positive group is a perturbation of a derivation.

Theorem 3.14. An operator $A$ on $C_{D}(X)$ is the generator of a positive group (T(t)) $t \in \mathbb{R}$ if and only if there exist a derivation $\delta$ on $C_{0}(x)$ which is the generator of a group, a function $h \in c^{b}(X)$ and $p \in C^{b}(X)$ satisfying $\inf X_{x} \in(x)>0$ such that
(3.18) $\quad A=V \delta v^{-1}+h$
where $V: C_{o}(X) \rightarrow C_{D}(X)$ is given by $V f=P \cdot f$. In that case one has
(3.19) (T(t)f)(x)=[p(x)/p($\left.\left.\phi_{t}(x)\right)\right] \cdot\left(\exp \int_{0}^{t} h(\phi(s, x)) d s\right) \cdot f\left(\phi_{t}(x)\right)$
for all $f \in C_{0}(X), t \in \mathbb{R}, x \in X$.

Note: (3.18) means that $D(A)=\left\{f: V^{-1} f \in D(8)\right\}$ and $A f=V \delta V^{-1} f+h f$.

Proof. Assume that $A$ is given by (3.18). Since $y$ is a lattice isomorphism, it is clear that $V^{-1} \delta v$ generates a positive group; and consequently, $\vec{A}$ does so as well (cf. the proof of Theorem 3.5). Conversely, let (T(t)) CR be a positive group with generator $A$. By Prop. 3.9 and Lemma 3.12 we know that there exist a continuous flow $\phi, 0 \ll p \in C^{b}(x)$ and $h \in C^{b}(x)$ such that (3.19) holds. Let $\delta$ be the generator of the automorphism group defined by $\phi$. We have to show that (3.18) holds. As in Theorem 3.5 one sees that $\delta+h$ generates the group $(S(t))_{t \in \mathbb{R}}$ given by
$(S(t) f)(x)=\exp \left(\int_{0}^{t} h(\phi(s, x)) d s\right) \cdot f(\phi(x))$. Hence
$\forall \delta V^{-1}+h=y(\delta+h) V^{-1}$ generates $\left(V S(t) V^{-l}\right)_{t \in \mathbb{R}}=(T(t)) t \in \mathbb{R}$. This is (3.18) .

Since every generator of a positive group is the perturbation of a derivation, we now look for examples of derivations which generate a group.

Example 3.15. Let $x=\mathbb{R}^{n}$. Consider a function $F \in C^{l}\left(\mathbb{R}^{n}, \mathbb{R}^{n}\right)$ such that $\sup _{x \in \mathbb{R}^{n}}\|D F(x)\|<\infty$ where $D F(x) \in L\left(\mathbb{R}^{n}\right)$ denotes the derivative of $F$ in $x$. Then there exists a continuous flow $\phi$ on $\mathbb{R}^{n}$ such that
(3.20) $\frac{\partial}{\partial t} \phi(t, x)=F(\phi(t, x))$ for all $t \in \mathbb{R}, x \in \mathbb{R}^{n}$.

Consider the automorphism group $\left(T_{0}(t)\right)_{t \in l l}$ given by $T_{0}(t) f=f o \phi_{t}$
and denote by $\delta$ its generator.
Then $D_{0}=\left\{f \in C_{0}\left(\mathbb{R}^{n}\right) \cap C^{1}\left(\mathbb{R}^{n}\right): l_{i m}\|x\| \rightarrow \infty\|(g r a d f)(x)\|=0\right\}$ is a core of $\delta$ and
(3.21) (ff) $(x)=((\operatorname{grad} f)(x) \mid F(x))$ for all $f \in D_{0}, x \in \mathbb{R}^{n}$,
where $(\cdot \mid \cdot)$ denotes the scalar product in $\mathbb{R}^{n}$
Proof. Let $f \in D_{o}$. Then $g=f-($ grad $f \mid F) \in C_{o}\left(\mathbb{R}^{n}\right)$ and $(\mathbb{R}(1, \delta) g)(x)=\int_{0}^{\infty} e^{-t} f(\phi(x, t)) d t-\int_{0}^{\infty} e^{-t}((\operatorname{grad} f)(\phi(t, x)) \mid F(\phi(t, x))) d t$ $=f(x)$ by integrating by parts. Hence $f \in D(\delta)$ and $f-\delta f=g$; i.e. $\delta f=(g r a d f \mid F)$. This proves (3.21).

Next we show $T_{o}(t) D_{0} \in D_{0}$ for all $t \geqq 0$, which implies that $D_{0}$ is a core of $\delta$ by A-I,Thm.1.9 (or A-II, Cor.1.34).
Since $F \in \mathbb{C}^{1}\left(\mathbb{R}^{n}, \mathbb{R}^{n}\right)$, it follows that $\phi \in \mathcal{C}^{1}\left(\mathbb{R} \times \mathbb{R}^{n}, \mathbb{R}^{n}\right)$ (see e.g., [Hirsch-Smale (1974), 15.2]). Moreover for each $x \in \mathbb{R}^{n}$, $\frac{d}{d t}\left(D \phi_{t}(x)\right)$ $=D F\left(\phi_{t}(x)\right) \cdot D \phi_{t}(x)$ and $D \phi_{0}(x)=I d$, (see [Hirsch-Smale (1974), p. 300]; here $\operatorname{Id} \in L\left(\mathbb{R}^{n}\right)$ denotes the identity operator. Hence $D \phi_{t}(x)=I d+\int_{0}^{t} D F\left(\phi_{S}(x)\right) \cdot D \phi_{s}(x) d s$. Consequently $\left\|D \phi_{t}(x)\right\| \leqq 1+\int_{0}^{t} M \cdot\left\|D \phi_{s}(x)\right\| d s$ for all $t \geqq 0$ and $x \in \mathbb{R}^{n}$; where $M:=\sup _{x \in \mathbb{R}^{n}}\|D F(x)\|<\infty$ by hypothesis. Hence by Gronwall's inequality, $\left\|D \phi_{t}(x)\right\| \leqq e^{M t}(t \geq 0)$ for all $x \in \mathbb{R}^{n}$. Now let $f \in D_{0}$, $t \geqq 0$. Then $\left[\operatorname{grad}\left(f \circ \phi_{t}\right)\right](x)=\left[(\operatorname{grad} f)\left(\phi_{t}(x)\right)\right] \cdot D \phi_{t}(x)$. Hence $\left\|\left[\operatorname{grad}\left(f \circ \phi_{t}\right)\right](x)\right\| \leq e^{M t}\left\|(\operatorname{grad} f)\left(\phi_{t}(x)\right)\right\|$, and so $\lim _{\|x\|+\infty}\|[g r a d(f \circ \phi t)](x)\| \leq e^{M t} \lim _{\|x\| \rightarrow \infty}\left\|(\operatorname{lgrad} f)\left(\phi_{t}(x)\right)\right\|=0$. Thus ${ }_{f 0 \phi_{t}} \in D_{o}$ for all $t \geqq 0$.

As a second class of examples we consider derivations on $C_{0}(a, b)$. Eventually we will determine all derivations on $C_{0}(a, b)$, which are generators of a group. We start by looking at differential operators of first order. Let $-\infty \leqq a<b \leqq \infty$ and let $m$ : ( $a, b$ ) $\times \mathbb{R}$ be a continuous function. We consider the operator $\delta_{m}$ on $C_{o}(a, b)$ given by $\left(\delta_{m} f\right)(x)= \begin{cases}m(x) f^{\prime}(x) & \text { if m(x)} \neq 0 \\ 0 & \text { otherwise }\end{cases}$
with domain $D\left(\delta_{m}\right)=\left\{f \in C_{0}(a, b): f\right.$ is differentiable in $x$ if $m(x) \neq 0$ and $\left.\delta_{m} f \in C_{0}(a, b)\right\}$.
Note that $\delta_{\mathrm{m}}$ is a derivation on $c_{o}(a, b)$.

Definition 3.16. A function $m$ : $(a, b) * \mathbb{R}$ is admissible if it is continuous and the following holds.
Whenever $a \leq c<d \leq b$ such that $m(x) \neq 0$ for $x \in(c, d)$ and $m(c)=0$ or $c=a=-\infty$ and $m(d)=0$ or $d=b=+\infty$, then
$\int_{C}^{Z} 1 /|m(x)| d x=\int_{z}^{d} 1 /|m(x)| d x=\infty$ for $z \in(c, d)$.

Note: If $m$ is admissible and $a>-\infty$, then $m(a)=0$; similary, if $b<\infty$, then $m(b)=0$. Moreover every Lipschitz continuous function is admissible.

Theorem 3.17. Let $m:(a, b) \rightarrow \mathbb{R}$ be a continuous function. The operator $\delta_{m}$ is generator of an automorphism group on $c_{o}(a, b)$ if and only if m is admissible.
In that case $D_{o}\left(\delta_{m}\right):=\left[f \in D\left(\delta_{m}\right) ; f\right.$ is differentiable on (a,b)) is a core of ${ }^{\circ}$ m
Additional properties. If $m$ is admissible, then the flow $\phi$ defining the group generated by $\delta_{m}$ can be described explicitely:
The set $\{x \in(a, b): m(x) \neq 0\}$ is the union of a finite or countable number of disfoint intervals $\left(a_{n}, b_{n}\right)(n \in J)$. Let
$c_{n} \in\left(a_{n}, b_{n}\right)$ and $g_{n}(x)=\int_{C_{n}}^{x} 1 / m(y) d y \quad\left(x \in\left(a_{n}, b_{n}\right), n \in J\right)$. since $m$ is admissible, $q_{n}$ is a homeomorphism from ( $a_{n}, b_{n}$ ) onto $\mathbb{R}$. Now the flow $\phi$ is defined by
(3.22) $\phi(t, x)= \begin{cases}x & \text { if } m(x)=0 \\ g_{n}^{-1}\left(g_{n}(x)+t\right) & \text { if } x \in\left(a_{n}, b_{n}\right)\end{cases}$
for all $t \in \mathbb{R}$.

We first prove a special case of theorem 3.17.

Proposition 3.18. Suppose that $m(x) \neq 0$ for all $x \in(a, b)$. Then $\delta_{m}$ is the generator of a group on $C_{0}(a, b)$ if and only if $m$ is admissible. In that case the group generated by fris isimilar to the translation group on $c_{0}(R)$.

Proof. Let $q \in C^{1}(a, b)$ such that $q^{\prime}(x)=1 / m(x)$ for all $x \in(a, b)$. Then $q$ is $a c^{l}$-diffeomorphism from ( $a, b$ ) onto an interval (a', b') By Vf $=\mathrm{fog}$ one defines an isomorphism from $C_{o}\left(a^{\prime} b^{\prime}\right)$ onto $C_{o}(a, b)$. Let $B$ on $C_{o}\left(a^{\prime}, b^{\prime}\right)$ be given by
$B^{0}=V^{-1} \delta_{m} V$. Then $D(B)=\left\{g \in C_{o}\left(a^{\prime}, b^{\prime}\right): g \circ q \in D\left(\delta_{m}\right)\right\}$
$=\left\{g \in C_{o}\left(a^{\prime}, b^{\prime}\right) \Gamma C^{l}\left(a^{\prime}, b^{\prime}\right): g^{\prime} \circ q=m \cdot\left(g^{\circ} q^{\prime}\right)^{\prime} \in C_{0}(a, b)\right\}$
$=\left\{g \in C_{0}\left(a^{\prime}, b^{\prime}\right) \cap C^{\prime}\left(a^{\prime}, b^{\prime}\right): g^{\prime} \in C_{o}\left(a^{\prime}, b^{\prime}\right)\right\}$ and
$B g=V^{-1} \delta_{m^{\prime}} V^{\prime}=v^{-1}\left(m\left(g^{\circ} q^{\prime}\right)^{\prime}\right)=V^{-1}\left(g^{\prime} \circ q\right)=g^{\prime}$.

Now observe that m is admissible if and only if $a^{\prime}=-\infty$ and $b^{\prime}=\infty$.
If $a^{\prime}=-\infty$ and $b^{\prime}=m$, then $B$ is the generator of the translaw tion group on $C_{0}(\mathbb{R})$. Hence also ${ }_{f}$ is the generator of a group $(T(t))_{t \in \mathbb{R}}$ on $c_{o}(a, b)$.
Conversely, assume that $B$ generates a group (T(t)) $t \in \mathbb{R}$. Assume that $a^{\prime}>-{ }^{-\infty}$. Then $C_{o}\left(a^{\prime}, b^{\prime}\right)$ is a closed subspace of $C_{o}\left[a^{\prime}, b^{\prime}\right)$. Let
$\left(T_{1}(t) f\right)(x)= \begin{cases}f(x+t) & \text { for } x+t<b^{\prime} \\ 0 & \text { for } x+t \geqslant b^{\prime}\end{cases}$
for all $f \in C_{0}\left[a^{\prime}, b^{\prime}\right), x \in\left[a^{\prime}, b^{\prime}\right), t \geq 0$. Then $\left(T_{1}(t)\right) t \geq 0$ is $a$ semigroup on $C_{o}\left[a^{\prime}, b^{\prime}\right)$ with generator $B_{1}$ given by $B_{1} f=f^{\prime}$ with domain $D\left(B_{1}\right)=\left\{f \in C_{o}\left[a^{\prime}, b^{\prime}\right) A^{\prime}\left(a^{\prime}, b\right): \lim _{x}+b^{\prime} f^{\prime}(x)=0\right.$, If we consider $B$ as an operator on $C_{o}{ }^{\left[a^{\prime}, b^{\prime}\right), ~ t h e n ~} B \in B_{1}$. Let $f \in D(B)$. Then $u(t):=T(t) f \in D(B) \in D\left(B_{1}\right)$ for all $t \geqq 0$; and $u(t)=B u(t)=B_{1} u(t) ; u(0)=f$. It follows from $A-I$, Thm.l. $\quad$. (or A-II, Corl.2.) that $T_{1}(t) f=u(t)$. Hence $T_{1}(t) f \in C_{0}\left(a^{\prime \prime}, b^{\prime}\right)$ for all $t \geqq 0$ and $f \in D(B)$, This ig impossible since $a^{\prime} \geqslant \mathbf{~ - ~}^{\circ}$. Similary one shows that $b^{\prime}=\infty$.

Proof of Theorem 3.17. Suppose that m is admissible. It is easy to see that (3.22) then defines a continuous flow on (a,b) Moreover, for every $x \in(a, b)$ the function $\phi(*, x)$ is differentiable and satisfies
(3.23) $\frac{\partial}{\dot{j} t} \phi(t, x)=m(\phi(t, x)) \quad(x \in(a, b), t \in \mathbb{R})$.

Denote by $(T(t))_{t \in \mathbb{R}}$ the group on $C_{o}(a, b)$ given by $T(t) f=f \phi_{t}$ ( $t \in R, f \in C_{o}(a, b)$ ) and let $A$ be its generator. Take $g \in C_{o}(a, b)$ and $f=R(1, A) g$. Then $f(x)=\int_{0}^{\infty} e^{-t} g(\phi(t, x)) d t, x \in(a, b)$. If
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-34.jpg?height=84&width=1617&top_left_y=1940&top_left_x=205) then $f(x)=\int_{0}^{\infty} e^{-t} g\left(q_{n}^{-1}\left(q_{n}(x)+t\right)\right) d t=e_{n}^{(x)} \int_{q_{n}}^{\infty}(x) e^{-s_{g}^{n}\left(q_{n}^{-l}(s)\right) d s .}$ Thus $f$ is differentiable in $x$ and $f^{\prime}(x)=(1 / m(x))(f(x)-g(x))$. Consequently $E \in D\left(\delta_{m}\right)$ and $\delta_{m} \ddagger=E-g$. This shows that $A \subset \delta_{m}$. In order to show the converse inclusion, let $f \in D\left(\delta_{m}\right)$ and $g=f-$ $\delta_{m}(f) \in C_{0}(a, b) \quad$ Then $R(1, A) g(x)=f(x)$ if $m(x)=0$ and $R(1, A) g(x)=\int_{0}^{\infty} e^{-t} f(\phi(t, x)) d t-\int_{0}^{\infty} e^{-t} m(\phi(t, x)) f(\phi(t, x)) d t$ $=\int_{0}^{\infty} e^{-t_{f}}(\phi(t, x)) d t-\int_{0}^{\infty} e^{-t} \frac{\partial}{\partial t} f(\phi(t, x)) d t \quad(b y(3,23))$
$=f(x)$ by integrating by parts. Thig shows that $f=R(1, A) g \in D(A)$ and that $\delta_{m}$ is the generator of the group (T(t)) $t \in \mathbb{R}$.
Finally we show that $T(t) D_{0}\left(\delta_{m}\right) \in D_{o}\left(\delta_{m}\right)$, which implies that $D_{o}\left({ }_{m}\right)$ is a core (by $A-I I$, Cor 1.34 ). Let $t \in \mathbb{R}$. The function $\phi_{t}(\cdot)$ is
differentiable on $(a, b)$ and $m(x) \frac{\partial}{p x} \phi(t, x)=m(\phi(t, x))$ for all $x \in$ $(a, b)$. Let $f \in D_{o}\left(\delta_{m}\right)=D\left(\delta_{m}\right) C^{-}, t \in \Re$. Then $T(t) f=f o \phi_{t}$ is differentiable and so in $D_{o}\left(\delta_{m}\right)$.

Conversely, assume that $\delta_{m}$ is generator of a group (T(t)) $t \in \mathbb{R}$ on $C_{0}(a, b)$. Since $\delta_{m}$ is a derivation, there exists a continuous flow $\left(\phi_{t}\right)_{t \in i}$ on (a,b) such that $T(t) f=f o \phi_{t}$ for all $f \in C_{o}(a, b)$, $t \in \mathbb{R}$. In order to show that $m$ is admissible let $a \leq c<d \leq b$ such that $m(x) \pm 0$ for all $x \in(c, d)$ and $m(c)=0$ or $a=c=-\infty$ and $m(d)=0$ or $d=b=\infty$.
If $a<c$ then $m(c)=0$; consequently $\left(\delta_{m} f\right)(c)=0$ for all
$f \in D\left(\delta_{m}\right)$. Thus (T(t)f)(c) $\pm f(c)$ for $a l l f \in D\left(\delta_{m}\right)$ and $t \in \mathbb{R}$. This shows that $\phi(t, c)=c$ for all $t \in \mathbb{R}$. Consequently $\phi_{t}(a, c)-(a, c)$ for $a l l$ $t \in R$. Similary $\phi_{t}(d, b) \subset(d, b)$ for all $t \in \mathbb{R}$. Thus the space $E_{o}:=\left\{f \in C_{o}(a, b): f\right.$ vanishes off (c,d) $\}$ is invariant under the group $\{T(t))_{t \in i f}$. We denote the group restricted to $E_{o}$ by $\left(T_{0}(t)\right)_{t \in R}$ and by $A_{o}$ its generator. Then $D\left(A_{o}\right)=$
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-35.jpg?height=66&width=1617&top_left_y=1252&top_left_x=228) obtain $\vec{R}_{O}=\delta_{m}$, where $m$ ' denotes the restriction of $m$ to (c,d) . So it follows from Prop. 3.18 that $m^{r}$ is admissible.

Remark 3.19. If $\phi$ is a flow on (a,b), a point $x \in(a, b)$ is called stationary if $\phi(t, x)=x$ for all $t \in \mathbb{R}$. Let $\delta$ be the generator of the group (T(t)) $t \in \mathbb{R}$ associated with $\phi$. Then $x \in(a, b)$ is a stationary point if and only if ( $\delta f$ ) ( $x$ ) $=0$ for a 11 $f \in D(\delta)$. If $m$ is an admissible function on (a,b) then we have seen that $x \in(a, b)$ is a stationary point of the flow associated with $\delta_{m}$ if and only if $m(x)=0$. This does no longer hold for functions which are not admissible as the following example showr.

Example 3.20. Consider the flow $\phi(t, x)=\left(x^{1 / 3}+t\right)^{3}$ on $\mathbb{F}$ and the group ( $T(t))_{t \in \mathbb{R}}$ induced by this flow on $C_{o}(\mathbb{R})$. one can easily see that the generator $\delta$ of $(T(t)) t \in \mathbb{R}$ is the following operator. Let $m(x)=3 x^{2 / 3}$. Then $(\delta f)(x)=m(x) f^{*}(x)$ Eor $x \neq 0$ and $D(s)=\left\{f \in C_{0}(\mathbb{R}): f\right.$ is differentiable in $x \neq 0$ and $m(x) f^{\prime}(x)$ has a continuous extension in $\left.C_{o}(\mathbb{R})\right\}$. However the function $m$ is not admissible. And in fact m(0) $=0$ but 0 is not a stationary point of $\phi$. In particular, there exists a function $f \in D(f)$ such that ( $\delta f)(0) \neq 0$.

Next we describe an arbitrary continuous flow on an open interval.

Proposition 3.21. Let $-\infty \leq a<b \leqq m$. A mapping
$\phi: \mathbb{H} x(a, b) \rightarrow(a, b)$ defines a continuous flow if and only if there exists a finite or countable set of disjoint intervals
$\left(a_{n}, b_{n}\right)=(a, b) \quad(n \in J)$ and for every $n \in J$ there exists $a$ homeomorphism $r_{n}$ from $\left(a_{n}, b_{n}\right)$ onto $(-\infty, \infty)$ such that
$\phi(t, x)= \begin{cases}x & \text { if } x \notin U{ }_{n \in J}\left(a_{n}, b_{n}\right) \\ r_{n}^{-1}\left(r_{n}(x)+t\right) & \text { if } x \in\left(a_{n}, b_{n}\right), n \in J\end{cases}$
for all $t \in \mathbb{R}$
Note: $J=\emptyset$ if and only if $\phi(t, x)=x$ for all $x \in(a, b)$ and $t \in \mathbb{R}$.

Proof. It is not difficult to see that the construction in the proposition defines a continuous flow on (a,b) . Now let $\phi$ be a continuous flow. The set $k=\{x \in(a, b): \phi(t, x)=x$ for all $t \in \mathbb{R}\}$ is closed in ( $a, b$ ) Thus ( $a, b)$ ( $K$ is the union of $a$ finite or countable set of disjoint intervals ( $a_{n}, b_{n}$ ), ( $n \in \mathbb{d}$ ) .
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-36.jpg?height=67&width=1614&top_left_y=1257&top_left_x=215) injective mapping from $\mathbb{R}$ into $\left(a_{n}, b_{n}\right)$. Thus $\alpha_{n}$ is strictly monotonous. It is easy to see that $l^{\prime \prime m} t_{+\infty} \phi\left(t, x_{n}\right)$ is an element of $K$ whenever the limit exists in (a,b) ; similary for the limit as $t \rightarrow-\infty$. Consequently, $a_{n}(f)=\left(a_{n}, b_{n}\right) ; i, e ., a_{n}$ is a homeomorphism from $\mathbb{R}$ onto $\left(a_{n}, b_{n}\right)$. Define $r_{n}$ to be the inverse of $a_{n}$. Let $x \in\left(a_{n}, b_{n}\right)$. Then $\phi(t, x)=\phi\left(t, a_{n}\left(r_{n}(x)\right)\right)$
$=\phi\left(t_{, \phi}\left(r_{n}(x), x_{n}\right)\right)=\phi\left(t+r_{n}(x), x_{n}\right)=a_{n}\left(t+r_{n}(x)\right)=r_{n}^{-l}\left(r_{n}(x)+t\right)$ for all $t \in \mathbb{R}$. This proves that $\phi$ has the desired form.

If $m$ is an admissible function on (a,b), then $D(\delta)$ contains many differentiable functions. This can be expressed by two facts:
a) $C_{C}^{l}(a, b):=\left\{f \in C^{1}(a, b)\right.$ : $f$ vanishes in a neighbourhood of a and $b$ \} is contained in $D\left(s_{m}\right)$ (this follows from the definition of $f_{m}$ ) ; and
b) the set $D_{o}\left(\delta_{m}\right)$ of all differentiable functions in $D_{o}\left(\delta_{m}\right)$ is a core of ${ }^{m}$ m (this follows from Theorem 3.17).
We will show below that these two properties are characteristic for the operators $\delta_{m}$. For other generators of automorphim groups they can be violated dramatically as the following example shows.

Example 3.22. There exists a generator $f$ of an automorphism group on $C_{o}(\mathbb{R})$ such that $D(s) \hat{A} C^{l}(\mathbb{R})=\{0\}$. In fact, consider a strictly increasing continuous map $q$ from $\mathbb{R}$ onto $\mathbb{R}$ such that
$q^{\prime}(x)=0$ a.e. Then $V: C_{o}(\mathbb{R}) * C_{o}(\mathbb{R})$ given by $V f=f^{\circ} q$ is an algebra isomorphism. Let $A$ be the generator of the translation group on $C_{o}(\mathbb{R})$ and $\delta=V^{-1} A V$. Then $D(\delta)=\left\{f \in C_{o}(\mathbb{R}): V E \in D(A)\right\}=$ $\left\{f \in C_{0}(\mathbb{R}): f \circ q \in C^{1}(\mathbb{R}),(f \circ q)^{\prime} \in C_{0}(\mathbb{R})\right\}$.
Let $f \in C^{l}(\mathbb{R}) \quad O D(\delta)$. If $f \neq 0$, then $f$ is not constant. Hence there exists $x_{0} \in \mathbb{R}$ such that $f^{\prime}\left(x_{0}\right) \neq 0$. Then $f$ has a continuously differentiable inverse in some open neighbourhood of $x_{o}$. since fog $\in C^{l}(\mathbb{R})$, it follows that $q$ is continuously differentiable in some neighborhood of $q^{-1}\left(x_{o}\right)$. This is a contradiction since $q^{\prime}(y)=0$ a.e.

Theorem 3.23. Let $f$ be the generator of an automorphism group on $C_{o}((a, b))$, where $-\infty \leq a<b \leqq \infty$. The following assertions are equivalont.
(i) There exists a continuous admissible function $m:(a, b) \rightarrow \mathbb{F}$ such that $\delta=\delta_{\mathrm{m}}$.
(ii) $C_{C}^{1}(a, b) \subset D(\delta)$ and $D_{o}(\delta)=\{f \in D(\delta): f$ is differentiable $\}$ is a core of $\delta$.

Proof. We have already pointed out that (i) implies (ii). So assume that (ii) holds. Let. (T(t)) $t \in \mathbb{R}$ be the group generated by $\delta$ and $\phi$ the continuous flow associated with the group. We can assume that $\phi$ is of the form given in Prop. 3.21.
Let $n \in J$, We show that $r_{n}^{-1}: \mathbb{R}+\left(a_{n}, b_{n}\right)$ is continuously differentiable. Let $x_{o} \in\left(a_{n}, b_{n}\right)^{n}$. There exists $f \in C_{c}^{1}(a, b)$ such that $f(x)=x$ in a neighborhood of $x_{0}$. Then $r_{n}^{-1}\left(r_{n}\left(x_{0}\right)+t\right)$
$=f\left(\phi\left(t, x_{0}\right)\right)=(T(t) f)\left(x_{0}\right)$ for alj $t$ in some neighborhood of 0 . Since $f \in D(f)$ it follows that the function $t * r_{n}^{-1}\left(r_{n}\left(x_{0}\right)+t\right)$ is continuously differentiable in some neighborhood of ${ }^{n} 0$ and so $r_{n}^{-1}$ is continuously differentiable in $r_{n}\left(x_{0}\right)$. Since $r_{n}:\left(a_{n} b_{n}\right) \rightarrow \mathbb{R}$ is surjective this proves the claim.
Next we show $\left(\mathbf{r}_{n}^{-1}\right)^{\prime}(t) \neq 0$ for all $t \in \mathbb{F}$. In fact, let $x_{o} \in\left(a_{n}, b_{n}\right)$ and ascume that $\left(r_{n}^{-1}\right){ }^{\prime}\left(r_{n}\left(x_{0}\right)\right)=0$. Then for all $f \in D_{o}(\delta)$ one has
$(f f)\left(X_{0}\right)=\left.\frac{a}{\partial t}\right|_{t=0} f\left(r_{n}^{-I}\left(r_{n}\left(x_{o}\right)+t\right)\right)=f^{\prime}\left(X_{o}\right)\left(r_{n}^{-1}\right)^{\prime}\left(r_{n}\left(x_{0}\right)\right)=0$. Since $D_{o}(\delta)$ is a core of $\delta$ this implies that $\phi\left(t_{r} x_{0}\right)=x_{o}$ for all $t \in \mathbb{R}$. Hence $x_{o} \in K$, a contradiction. It follows that $r_{n}:\left(a_{n} b_{n}\right) \rightarrow \mathbb{R}$ is $a^{1} C^{1}$-diffeomorphism for all $n \in \pm$.

Define $m:(a, b) \rightarrow \mathbb{R}$ by

$$
m(x)= \begin{cases}0 & \text { if } x \in K \\ 1 / r_{n}^{\prime}(x) & \text { if } x \in\left(a_{n} b_{n}\right), n \in J\end{cases}
$$

Then $m$ is continuous and admissible. The given flow coincides with the one constructed from m in Theorem 3.17. Thus $\delta=\delta \mathrm{m}$.

Remark. Let $m$ : $(a, b)$ * $\mathbb{R}$ be continuous, Then $m$ is admissible if and only if the initial value problem

$$
\dot{Y}(t)=m(y(t)) \quad(t \in \mathbb{R}) ; \quad y(0)=x
$$

has a unique solution $y \in C^{l}(\mathbb{R},(a, b))$ which depends continuously on the initial value $x$ (i.e., if $x_{n} * x$ in ( $a, b$ ) then the solution $Y_{n} \in C^{1}(\mathbb{R},(a, b))$ with initial value $y_{n}(0)=x_{n}$ satisfies $y_{n}(t)+y(t)(n \rightarrow \infty)$ for all $\left.t \in \mathbb{R}\right)$. This is not difficult to see.

As we have seen above the operators $\delta_{m}$, where $m$ is an admissible function, do not exhaust all generators of automorphism groups. But one can obtain every such generator by a similarity transformation (see $\mathrm{A}-\mathrm{I}, 3.0$ ) from some $\delta_{\mathrm{m}}$.

Theorem 3.24. Let $-\infty \leq a<b \leq \infty$. An operator $\delta$ on $C_{o}(a, b)$ is the generator of an automorphism group on $c_{0}(a, b)$ if and only if there exists an algebra isomorphism $V$ from $C_{0}(a, b)$ onto $C_{0}(a, b)$ and an admissible function $m:(a, b) \rightarrow \mathbb{R}$ such that $\delta=V^{-1} \delta_{F} V^{\circ}$.

Proof. In order to prove the non-trivial implication let $(T(t)), t \in \mathbb{R}$ be an automorphism group on $c_{o}(a, b)$ with generator $\delta$. Let $\phi$ be the continuous flow on ( $a, b$ ) such that $T(t) f=f o \phi_{t}$ ( $f \in C_{o}(a, b)$, $t \in \mathbb{R})$. Then $\phi$ is of the form given in Prop. 3.21. For every $n \in J$ choose a $c^{1}$-diffeomorphism $q_{n}$ from $\left(a_{n}, b_{n}\right)$ onto ( $-\infty, \infty$ ) satisfy ing $g_{n} \prime(x)>0$ for all $x \in\left(a_{n}, b_{n}\right)$ in the case when $I_{n}$ is increasing and $G_{n}{ }^{\prime}(x)<0$ for all $x \in\left(a_{n}, b_{n}\right)$ in the case when $r_{n}$ is decreasing. Then $\beta_{n}:=r_{n}^{-1} \circ q_{n}$ is a homeomorphism from ( $\left.a_{n}, b_{n}\right)$
onto itself satisfying $\lim _{x+a_{n}} \beta_{n}(x)=a_{n}$ and $\quad \lim _{X \neq b_{n}} \beta_{n}(x)=b_{n}$.
Let $\beta:(a, b),(a, b)$ be defined by
$\beta(x)= \begin{cases}x & \text { if } x \in K \\ \beta_{n}(x) & \text { if } x \in\left(a_{n}, b_{n}\right), n \in \mathcal{J} .\end{cases}$
Then $\beta$ is a homeomorphism from ( $a, b$ ) onto ( $a, b$ ) and $\psi_{t}:=\beta^{-1}{ }_{o} t^{\circ \beta} \quad(t \in \mathbb{R})$ defines a continuous flow on (a,b).

Define $m:(a, b) \rightarrow \mathbb{R}$ by
$m(x)= \begin{cases}0 & \text { if } x \in K \\ 1 / q_{n}^{\prime}(x) & \text { if } x \in\left(a_{n}, b_{n}\right)\end{cases}$
Then $m$ is continuous and admissible and the flow $\psi$ coincides with the flow constructe from m in Theorem 3.17. Hence $f_{m}$ is the
![](https://cdn.mathpix.com/cropped/2025_01_15_35dbb10af78d6eeeeb17g-39.jpg?height=73&width=1620&top_left_y=609&top_left_x=212) $=V T(t) V^{-1} f$, where $V$ is the isomorphism on $C_{0}(a, b)$ given by $V f=f a \beta$. Consequently, $\delta=V^{-l} \delta_{m} V$.

Now we are able to describe arbitrary generators of positive groups on $C_{0}(a, b)$.

Theorem 3.25. Let $-\infty \leqq a<b \leqslant \infty$. An operator $A$ generates a positive group on $c_{o}(a, b)$ if and only if there exist

- a lattice isomorphism $v$ on $C_{0}(a, b)$,
- an admissible function m on (a,b),
- a bounded continuous function $h:(a, b) \rightarrow \mathbb{R}$ such that

$$
\begin{equation*}
A=V^{-1} \delta_{\mathrm{m}} V+h \tag{3.24}
\end{equation*}
$$

Proof. Iet $A$ be the generator of a positive group on $C_{o}(a, b)$. By Theorem 3.14 there exist a continuous bounded function $p:(a, b)+\mathbb{R}$ such that $i^{n} f_{x \in(a, b)} P(x)>0$ and $h \in C^{b}(a, b)$ and the generator $\delta$ of an automorphism group such that $A=M_{\text {s }}{ }^{-1}+h$ where $M \in L\left(C_{0}(a, b)\right) i s$ given by $M f=p \cdot f$. By Theorem 3.24 there exist an admissible continuous function $m:(a, b) \rightarrow \mathbb{R}$ and a lattice isomorphism $U \in L\left(C_{0}(a, b)\right)$ such that $\delta=U_{f_{m}} \mathrm{~J}^{-1}$. Setting $V=M U$ we obtain $A=V_{\mathrm{H}} \mathrm{V}^{-1}+\mathrm{h}$.

Finally we consider compact intervals. Let $-\infty \leq a<b s a$ and $\phi$ be a continuous flow on $[a, b]$. Then it is easy to see that $\phi(a, t)=a$ and $\phi(b, t)=b$ for $a l l t \in \mathbb{R}$. So the restriction $\phi_{o}$ of $\phi$ to ( $a, b$ ) is a continuous flow on ( $a, b)$.
Conversely, if $\phi_{o}$ is a continuous flow on (a,b) the extension $\phi_{o}$ to $\phi=\mathbb{R} x[a, b] *[a, b]$ by setting $\phi(t, a)=a ; \phi(t, b)=b$ for all $t \in \mathbb{F}$ defines a continuous flow on [a,b]. This consideration allows us to extend easily the preceding results to the space $C[a, b]$. Let $m$ : $(a, b)$, $\mathbb{R}$ be a continuous function. We define the operator $\tilde{\delta}_{\mathrm{m}}$ on $C[a, b]$ by $\tilde{\delta}_{\mathrm{m}} \mathrm{f}=\mathrm{g}$ such that
(3.25) $g(x)= \begin{cases}m(x) f^{\prime}(x) & \text { if } m(x) \neq 0 \\ 0 & \text { if } m(x)=0\end{cases}$
for $a l l x \in(a, b)$ and $D\left(f_{m}\right)=\{f \in C[a, b]: f$ is differentiable in $x \in(a, b)$ whenever $m(x) \neq 0$ and there exists a (necessarily unique) $g \in C[a, b]$ such that (3.25) holds $\}$.

Theorem 3.26. Let $m$ be a continuous function on ( $a, b$ ) The operator $\hat{S}_{\mathrm{m}}$ is generator of an automorphism group on $\mathrm{C}[\mathrm{a}, \mathrm{b}]$ if and only if m is admissible.

Proof. If $\tilde{\delta}_{\mathrm{m}}$ generates an automorphism group ( $T(t)$ ) $t \in \mathbb{R}$ then by the remark above $T(t) C_{0}(a, b)=C_{o}(a, b)(t \in \mathbb{R})$. The generator of the restricted group has the domain
$\left[f \in C_{0}(a, b) \cap D\left(\delta_{m}\right): \hat{S}_{\mathbb{m}} f \in C_{O}(a, b)\right\}=D\left(\delta_{m}\right)$. Hence $\delta_{m}$ is a generator and so m is adnissible by Theorem 3.17. Conversely, if m is admissible, then $\delta_{m}$ generates a group on $c_{0}(a, b)$ given by a flow $\phi_{o}$ on $(a, b)$. Extending $\phi_{o}$ to $[a, b]$ as above one obtains a continuous flow $\phi$ on [a,b] which defines a group (T(t)) teR ( It is easy to verify, that the generator of this group is $\tilde{\delta}_{\mathrm{m}}$.

Theorem 3.27. Let $\delta$ be the generator of an automorphism group on $C[a, b]$. Then there exists an admissible function $m$ : $(a, b) * \mathbb{R}$ and an algebra isomorphism $v$ from $C[a, b]$ onto $c[a, b]$ such that $\delta=\mathrm{V}^{-1} \tilde{\mathrm{~F}}_{\mathrm{m}} \mathrm{V}$.

Proof. The restriction $\delta_{0}$ of $\delta$ to $C_{o}(a, b)$ is the generator of an automorphism group. Thus by Theorem 3.24 there exists a continuous admissible function $m:(a, b) \rightarrow \mathbb{F}$ and an algebra isomorphism $V_{o}$ from $C_{0}(a, b)$ onto $C_{o}(a, b)$ such that $\delta_{0}=V_{0}^{-1} \delta_{m} v_{o}$. Let $v$ be the unique algebra isomorphism on $C[a, b]$ which extends $V_{o}$. Then it is easy to see that $\delta=\mathrm{v}^{-1} \hat{\delta}_{\mathrm{m}} \mathrm{V}$.

Theorem 3.28. An operator $A$ on $C[a, b]$ is generator of a positive group on $C[a, b]$ if and only if there exist

- a lattice isomorphism $V$ on $C[a, b]$
- an admissible function $m=(a, b)+\mathbb{R}$
- and a function $h \in C[a, b]$ such that $A=V^{-1} \tilde{S}_{\mathrm{f}} y+h$.

The proof follows from Theorem 3.14 via Theorem 3.27 in the same way as Theorem 3.25 (via Theorem 3.24).

NOTES.

Section l. Conceming bounded generators of positive semigroups and the positive minimum princfple we refer to the corresponding notes in Chapter C-IL.
Theorem 1.6 and 1.8 are due to Arendt-Chernoff-Kato (1982), but we give a more direct proof here. Theorem 1.13 and its corollary are from the same source.
In the case when A is dissipative Theorem 1.20 is due to Dorroh (1966). We use prectsely Dorroh's arguments to verify the range condition. other extensions of Dorroh's result have been given by Jumer (1974) and Lumer (1975).

Section 2. A characterization of generators of latice semigroups by Kato's equality is due to Nagel-thlig (1981) if the underlying space has order continuous norm (see C-II,Sec.5), for general Banach spaces and $C$ ( $X$ ) in particular the problem has been consfdered in Arendt (1982). Theorem 2.10 fs Gue to Uhlig (1979).

Section 3. The characterization of generators of lattice semigroups as perturbation of a derivation (Theorem 3.5 and 3.6) is due to Dertinger-Nagel (1979). The corresponding result for positive groups on $C$ ( $X$ ) (Theorem 3.14) was obtained by Arendt-Greiner (1984). Lin-Montgomery-Sine ( 9977 ) consider multiplicative perturbations of a generator of an automorphism group on $C(K)$ ( $K$ compact) by a furction $m$ which has a fintte number of zeros. The function $m$ is assumed to satisfy the "generalized Osgood condfion" which is similar to being admissable (in our sense) but in addition the given flow is involved in the definition.
Batty (1981) determined all densely defined derivations $\hat{\theta}$ on $\mathrm{C}[0,1]$ which are well-behaved (i.e., $\pm \delta$ fis dispersive) by a representation similar to Theorem 3.24. In contrast to Batty, here we assume that $\delta$ is the generator of a group. This simplifies the matter considerably since all continuous flows on an interval are easy to determine (Frop. 3.21). Our approach is inspired by delaubenfels (1984) to whom Theorem 3.24 is due.
For simplicity we confined ourselves to groups. Uhlig (1979) determined all semiflows on an interval.
In the sequel of Eatty's work (loc.cit.) a characterization of all densely defined closed derivations on $c[0,1]$ has been obtafned by Kurose 1 n a series of papers (1981), (1982), (1983).

