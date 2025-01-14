# ONE-PARAMETER SEMIGROUPS ON BANACH SPACES 

## CHAPTER A-I

BASICRESULTS ON SEMIGROUPS ON Banach Spaces


Since the basic theory of onemparameter semigroups can be found in several excellent books (e.g. Davies (1980), Goldstein (1985a), Pazy (1983) or HillewPhillips (1957)) we do not want to give a self-contained introduction to this subject here. It may however be useful to fix our notation, to collect briefly some important definitions and results (Section 1), to present a list of standard examples (Section 2) and to discuss standard constructions of new semigroups from a given one (Section 3).
In the entire chapter we denote by $E$ a (real or) complex Banach space and consider one - parameter semigroups of bounded linear operators $T(t)$ on $E$. By this we understand a subset $\left\{T(t): t \in \mathbb{R}_{+}\right\}$ of $L(E)$, usually written as (T(t)) ${ }_{t \geqslant 0}$, such that

$$
T(0)=I d
$$

$T(s+t)=T(s) \cdot T(t) \quad$ for all $s, t \in \mathbb{R}_{+}$.
In more abstract terms this means that the map $t \rightarrow T(t)$ is a homomorphism from the additive semigroup $\mathbb{R}_{+}{ }^{+}+$) into the multiplicative semigroup (L(E), *) . Similarly, a one-parameter group (T(t)) teR will be a homomorphic image of the group ( $\mathbb{R},+$ ) in (L(E), .).

## 1. STANDARD DEFINITIONS AND RESULTS

We consider a one-parameter semigroup (T(t)) t¥0 on a Banach space $E$ and observe that the domain $\mathbb{R}_{+}$and the range $L(E)$ of the (semi~
group) homomorphism $r: t+T(t)$ are topological semigroups for the natural topology on $\mathbb{R}_{+}$and any one of the standard operator topologiss on $L(E)$. We single out the strong operator topology on L(E) and require $\tau$ to be continuous.

Definition $1.1 . \quad$ A one-parameter semigroup ( $T(t))_{t \geqslant 0}$ is called strongly continuous if the map $t \rightarrow T(t)$ is continuous for the strong operator topology on $L(E)$, i.e. limt $t_{0} \| T(t) f-T\left(t_{o}\right) f=0$ for every $f \in E$ and $t, t_{0} \geqslant 0$,

Clearly one defines in a similar way weakly continuous, resp. uniformly continuous (compare A-II, Def..1.19) semigroups, but since we concentrate on the strongly continuous case we agree on the follow ing terminology:
![](https://cdn.mathpix.com/cropped/2025_01_13_d47bd7bb89767f3818bcg-2.jpg?height=52&width=1526&top_left_y=1145&top_left_x=319) tinuous one-parameter semigroup of bounded linear operators.

Next we collect a fey elementary facts on the continuity and boundedness of onewparameter semigroups.

Remarks l.2. (l) A one~parameter semigroup (T (t)) $t \geqslant 0$ on a Banach space $E$ is strongly continuous if and only if for any $f \in E$ it is true that $T(t) f \rightarrow f$ as $t \rightarrow 0$.
(2) For every strongly continuous semigroup (T(t)) $t \mathfrak{l}{ }^{(2)}$ there exist constants $M \mathcal{B} 1, W \in \mathbb{R}$ such that $\|T(t)\| \leqq M \cdot e^{w t}$ for every $t \geqq 0$. (3) If (T(t)) ${ }_{t \geqslant 0}$ is a one-parameter semigroup such that \|T(t)\| is bounded for $0<t \leqslant \delta$ then it is strongly continuous if and only if $\lim _{t \rightarrow 0} T(t) f=f$ for every $f$ in a total subset of $E$.

The exponential estimate from Remark $1.2,(2)$ for the growth of $\| T(t)$ f can be used to define an important characteristic of the semigroup.

Definition 1.3. By the growth bound (or type) of the semigroup (T(t)) $t \geq 0$ we understand the number

$$
\begin{equation*}
\omega:=\inf \left\{w \in \mathbb{R}: \text { There exists } M \in \mathbb{R}_{+} \text {such that }\|T(t)\| \leq e^{w t}\right. \tag{1.1}
\end{equation*}
$$

for $t \geqslant 0\}$

$$
=\lim _{t \rightarrow \infty} 1 / t \cdot \log \|T(t)\|_{\|}=\inf _{t>0} 1 / t \cdot \log _{\|} T(t) \|
$$

Particularily important are semigroups such that for every $t \geqq 0$ we have $\|T(t)\| \leqq M$ (bounded semigroups) or $\|T(t)\| s 1$ (contraction semigroups). In both cases we have $\omega \leq 0$.

It follows from the subsequent examples and from 3.1 that $w$ may be any number $-^{\infty} \leqq i<+^{\infty}$. Moreover the reader should observe that the infimum in ( 1.1 ) need not be attained and that $M$ may be larger than 1 even for bounded semigroups.

Examples 1.4. (i) Take $E=\mathbb{C}^{2}, A=\left(\begin{array}{ll}0 & 1 \\ 0 & 0\end{array}\right)$ and $T(t)=e^{t A}=\left(\begin{array}{ll}1 & t \\ 0 & 1\end{array}\right)$. Then for the 1 -norm on $E$ we obtain $\|T(t)\|=1+t$, hence (T(t)) $t \geqslant 0$ is an unbounded semigroup having growth bound $w=0$. (ii) Take $E=L^{1}(\mathbb{F})$ and for $f \in E, t \geqslant 0$ define

$$
T(t) f(x):= \begin{cases}2 \cdot f(x+t) & \text { if } x \in[-t, 0] \\ f(x+t) & \text { otherwise. }\end{cases}
$$

Each $T(t), t>0$, satisfies $\|T(t)\|=2$ as can be seen by taking $f:=l_{[0, t]}$. Therefore $(T(t))_{t \geq 0}$ is a strongly continuous semigroup which is bounded, hence has $w=0$, but the constant $M$ in (1.1) cannot be choosen to be 1 .

The most important object associated to a strongly continuous semigroup (T(t)) $t \geq 0$ is its 'generator' which is obtained as the (right) derivative of the map $t \rightarrow T(t)$ at $t=0$, Since for strongly continuous semigroups the functions $t \rightarrow T(t) f, f \in E$, are continuous but not always differentiable we have to restrict our attention to those $f \in E$ for which the desired derivative exists. We then obtain the 'generator' as a not necessarily everywhere defined operator.

Definition 1.5. To every semigroup (T(t)) t¥0 there belongs an operator (A,D(A)), called the generator and defined on the domain

$$
D(A):=\left\{f \in E: \lim _{h \rightarrow 0} \frac{T(h) f-f}{h} \text { exists in } E\right\}
$$

by Af $:=\lim _{h \rightarrow 0} \frac{T(h) f-\frac{f}{h}}{h}$ for $f \in D(A)$.

Clearly, $D(A)$ is a linear subspace of $E$ and $A$ is linear from $D(A)$ into $E$. Only in certain special cases (see 2.1) the generator
is everywhere defined and therefore bounded (use prop.1.9(i)). In general the precise extent of the domain $D(A)$ is escential for the characterization of the generator. But since the domain is canonically associated to the generator of a semigroup we shall write in most cases $A$ instead of (A,D(A)).

As a first result we collect some information on the domain of the generator.

Proposition 1.6. For the generator $A$ of a semigroup ( $T(t))_{t \geq 0}$ on a Banach space $E$ the following assertions hold:

If $f \in D(A)$ then $T(t) f \in D(A)$ for every $t \geqslant 0$.
(ii) The map $t \rightarrow T(t) f$ is differentiable on $\mathbb{F}_{+}$if and only if $\mathrm{f} \in \mathrm{D}(\mathrm{A})$. In that case one has

$$
\begin{equation*}
\frac{d}{d t} T(t) f=A T(t) f=T(t) A f . \tag{1.2}
\end{equation*}
$$

$$
\begin{equation*}
A \int_{0}^{t} T(s) f d s=T(t) f-f . \tag{1,3}
\end{equation*}
$$

(iv) If $f \in D(A)$ then

```
\int
```

(v) The domain $D(A)$ is dense in $E$.

The identity (1.2) is of great importance and shows how semigroups are related to certain Cauchy problems. We state this explicitely in the following theorem.

Theorem 1.7. Let (A,D(A)) be the generator of a strongly continuous semigroup $(T(t)) t \geq o$ on the Banach space $E$. Then the 'abstract Cauchy problem'
(ACP)

$$
\frac{d}{d t} \xi(t)=A \xi(t), \xi(0)=f_{0},
$$

has a unique solution $\xi: \mathbb{R}_{+} \rightarrow D(A)$ in $C^{1}\left(\mathbb{R}_{+}, E\right)$ for every $f_{o} \in D(A)$. In fact, this solution $i s$ given by $\xi(t):=T(t) f_{o}$.

For the important relation of semigroups to abstract Cauchy problems we refer to A-II, Section 1. Here we only point out that the above theorem implies that a semigroup is uniquely determined by its generam tor.
While the generator is bounded only for uniformly continuous semigroups (see 2,l below), it always enjoys a weaker but useful property,

Definition l.8. An operator $B$ with domain $D(B)$ on a Banach space $E$ is called closed if $D(B)$ endowed with the graph norm

$$
\|f\|_{B}:=\|f\|+\|B f\|
$$

becomes a Banach space. Equivalently, (B,D(B)) is closed if and only if its graph $\{(f, B f): f \in D(B)\}$ is closed in $E \times E$, i.e.
(1.5) $\quad f_{n} \in D(B), f_{n} \rightarrow E$ and $B f_{n} \rightarrow g$ implies $f \in D(B)$ and $B f=g$.

It is clear from this definition that the 'closedness' of an operator $B$ depends very much on the size of the domain $D(B)$. For example, a bounded and densely defined operator (B,D(B)) is closed if and only if $D(B)=E$.
On the other hand it may happen that ( $B, D(B)$ ) is not closed but has a closed extension (C,D(C)), i.e, $D(B) \subset D(C)$ and $B f=C f$ for every $f \in D(B)$. In that case, $B$ is called closable, a property which is equivalent to the following:
(1.6) $f_{n} \in D(B), f_{n} \rightarrow 0$ and $B f_{n} \rightarrow g$ implies $g=0$.

The smallest closed extension of ( $B, D(B)$ ) will be called the closure $\bar{B}$ with domain $D(\bar{B})$. In other words, the graph of $\bar{B}$ is the closure of $\{(f, B f): f \in D(B)\}$ in $E \times E$.
Finally we call a subset $D_{o}$ of $D(B)$ a core for $B$ if $D$ is $\|\cdot\|_{B}$-dense in $D(B)$. This means that a closed operator is determined (via closure) by its restriction to a core in its domain.

We now collect the fundamental topological properties of semigroup generators, their domains (see also A-II,Cor.l.34) and their resolw vents.

Proposition 1.9. For the generator $A$ of a strongly continuous semigroup (T(t)) tap the following holds:
(i) The generator $A$ is a closed operator.
(ii) If a subspace $D_{o}$ of the domain $D(A)$ is dense in $E$ and (T(t))-invariant, then it is a core for $A$.
(iii) Define $D\left(A^{n}\right):=\left\{f \in D\left(A^{n-1}\right): A f \in D\left(A^{n-1}\right)\right\}, D\left(A^{1}\right)=D(A)$. Then $D\left(A^{\infty}\right):=\Gamma_{n \in \mathbb{N}} D\left(A^{n}\right)$ is dense in $E$ and a core for $A$.

Example 1.10. Property (iii) above does not hold for general densely defined closed operators. Take $E=C[0,1], D(B)=C l[0,1]$ and $B f=q \cdot f$ for some nowhere differentiable function $q \in C[0,1]$. Then $B$ is closed, but $D\left(B^{2}\right)=(0)$.

Proposition l.11. For the generator $A$ of a strongly continous semigroup $(T(t)) t_{\geq 0}$ on a Banach space $E$ the following holds. If $\int_{0}^{\infty} e^{-\lambda t} T(t) \pm d t$ exists for every $f \in E$ and some $\lambda \in \mathbb{C}$, then $\lambda \in \rho(A)$ and $R(\lambda, A) f=\int_{0}^{\infty} e^{-\lambda t} T(t) \pm d t$. In particular,
(1.7) $R(\lambda, A)^{n+1} f=\frac{(-1)^{n}}{n!}\left(\frac{d}{d \lambda}\right)^{n} R(\lambda, A) f=\int_{0}^{\infty} e^{-\lambda t} t^{n / n!} T(t) f d t$
![](https://cdn.mathpix.com/cropped/2025_01_13_d47bd7bb89767f3818bcg-6.jpg?height=55&width=1200&top_left_y=1200&top_left_x=225)

Remarks 1.12. (1) For continuous Banach space valued functions such as $t \rightarrow T(t) f$ we consider the Riemann integral and define $\int_{0}^{\infty} T(t) f d t \quad a s \quad l_{m} m_{t \rightarrow \infty} \int_{0}^{t} T(s) f d s$. Sometimes such integrals for strongly continuous semigroups $(T(t))$ t $\geqslant 0$ are written as $\int_{a}^{b} T(t) d t$ and understood in the strong sense.
(2) since the generator (A,D(A)) determines the semigroup (T(t)) t>0 uniquely, we will speak occasionally of the growth bound of the generator instead of the semigroup, i.e. we write $\omega=\omega(A)=w(T(t)) t \geq 0)$. (3) For one-parameter groups it might seem to be more natural to define the generator as the 'derivative' rather than just the 'right derivative' at $t=0$. This yields the same operator as the following result shows:
The strongly continuous semigroup (T(t)) $t \geqslant 0$ with generator $A$ can be extended to a strongly continuous one-parameter group (u(t)) $t \in \mathbb{R}$ if and only if $-A$ generates a semigroup $(s(t))_{t \geq 0}$.

In that case (U(t)) $t \in \mathbb{R}$ is obtained as

$$
U(t):= \begin{cases}T(t) & \text { for } t \geqslant 0 \\ s(-t) & \text { for } t \leqslant 0\end{cases}
$$

We refer to [Davies (1980), Prop.1.14] for the details.

