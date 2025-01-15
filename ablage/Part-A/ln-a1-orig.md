# ONE-PARAMETER SEMIGROUPS ON BANACH SPACES 

## CHAPTER A-I

BASICRESULTS ON SEMIGROUPS

ON B A N A C H S PA CES
by
Rainer Nagel and Ulf Schlotterbeck

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
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-02.jpg?height=52&width=1526&top_left_y=1145&top_left_x=319) tinuous one-parameter semigroup of bounded linear operators.

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

has a unique solution $\xi: \mathbb{R}_{+} \rightarrow D(A)$ in $C^{1}\left(\mathbb{R}_{+}, E\right)$ for every $f_{o} \in D(A)$. In fact, this solution is given by $\xi(t):=T(t) f_{o}$.

For the important relation of semigroups to abstract Cauchy problems we refer to A-II,Section 1. Here we only point out that the above theorem implies that a semigroup is uniquely determined by its generam tor.
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
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-06.jpg?height=55&width=1200&top_left_y=1200&top_left_x=225)

Remarks 1.12. (1) For continuous Banach space valued functions such as $t \rightarrow T(t) f$ we consider the Riemann integral and define $\int_{0}^{\infty} T(t) f d t \quad a s \quad l_{m} m_{t \rightarrow \infty} \int_{0}^{t} T(s) f d s$. Sometimes such integrals for strongly continuous semigroups $(T(t))$ t $\geqslant 0$ are written as $\int_{a}^{b} T(t) d t$ and understood in the strong sense.
(2) since the generator (A,D(A)) determines the semigroup (T(t)) t>0 uniquely, we will speak occasionally of the growth bound of the generator instead of the semigroup, i.e. we write $\omega=\omega(A)=w(T(t)) t \geq 0)$. (3) For one-parameter groups it might seem to be more natural to define the generator as the 'derivative' rather than just the 'right derivative' at $t=0$. This yields the same operator as the following result shows:
The strongly continuous semigroup (T(t)) $t \geqslant 0$ with generator $A$ can be extended to a strongly continuous one-parameter group (u(t)) $t \in \mathbb{R}$ if and only if $-A$ generates a semigroup $(s(t))_{t \geq 0}$.

In that case (U(t)) $t \in \mathbb{R}$ is obtained as

$$
U(t):= \begin{cases}T(t) & \text { for } t \geqslant 0 \\ s(-t) & \text { for } t \leqslant 0\end{cases}
$$

We refer to [Davies (1980), Prop.1.14] for the details.

## 2. STANDARD EXAMPLES

In this section we list and discuss briefly the most basic examples of semigroups together with their generators. These semigroups will reappear throughout this book and will be used to illustrate the theory. We start with the class of semigroups mentioned after Definition 1.1 .

### 2.1. Uniformly Continuous Semigroups

It follows from elementary operator theory that for every bounded operator $A \in L(E)$ the sum

$$
\xi_{n=0}^{m} t^{n} A^{n} / n!=: e^{t A}
$$

exists and determines a unique uniformly continuous (semi)group ( $e^{t A}$ ) $t \in \mathbb{R}$ having $A$ as its generator.
Conversely, any uniformly continuous semigroup is of this form: If the semigroup $(T(t))$ tzo is uniformly continuous, then $\frac{1}{t} \int_{0}^{t} T(s) d s$ uniformly converges to $T(0)=I d a s t \rightarrow 0$. Therefore for some $t$ ' $=0$ the operator $\frac{1}{t} \int_{0}^{t} T(s) d s$ is invertible and every $f \in E$ is of the form $f=\frac{1}{t} \int_{0}^{t^{t}} T(s) g d s$ for some $g \in E$. But these elements belong to $D(A)$ by (1.3), hence $D(A)=E$. Since the generator $A$ is closed and everywhere defined it must be bounded.
Remark that bounded operators are always generators of groups, not just semigroups. Moreover the growth bound $w$ satisfies $|w| \leqslant\|A\|$ in this situation.

The above characterization of the generators of uniformly continuous semigroups as the bounded operators shows that these semigroups are at least in many aspects - rather simple objects.

### 2.2. Matrix Semigroups

The above considerations expecially apply in the situation $E=\mathbb{C}^{n}$. If $n=2$ and $A=\left(a_{i j}\right)_{2 \times 2}$ the following explicit formulas for $e^{t A}$ might be of interest:
Set $s:=\operatorname{trace} A, d:=\operatorname{det} A$ and $D:=\left(s^{2}-4 d\right)^{1 / 2}$. Then

$$
\begin{aligned}
e^{t A}= & e^{t s / 2} \cdot\left[D^{-1} 2 \sinh (t D / 2) \cdot A+\left(\cosh (t D / 2)-s D^{-1} \sinh (t D / 2)\right) \cdot I d\right] \\
& \text { if } D \neq 0, \\
e^{t A}= & e^{t s / 2} \cdot[t A+(1-t s / 2) \cdot I d] \quad \text { if } D=0, r e s p .
\end{aligned}
$$

### 2.3. Multiplication Semigroups

Many Banach spaces appearing in applications are Banach spaces of (real or) complex valued functions over a set $X$. As the most
standard of these "function spaces", we mention the space $C_{0}(X)$ of all continuous complex valued functions vanishing at infinity on a locally compact space $X$, or the spacer $L^{P}(X, \Sigma, k), 1 \leqq p \leqq \infty$, of all (equivalence classes of) p-integrable functions on a $\sigma$-finite measure space $(X, 5, \mu)$.

On these function spaces $E=C_{o}(X)$, resp. $E=L^{P}(X, E, k)$, there is a simple way to define "multiplication operatorg" : Take a continuous, resp. measurable function $q: x \rightarrow \mathbb{C}$ and define

$$
M_{q} f:=q \cdot f, \text { i.e. } \quad M_{q} f(x):=q(x) \cdot f(x) \text { for } x \in X,
$$

for every $f$ in the "maximal" domain $D\left(M_{G}\right):=\{g \in E: G * G \in \mathbb{E} \in$.
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-08.jpg?height=69&width=1617&top_left_y=1025&top_left_x=228) for $1 \leqq p<{ }^{c}$. Moreover, $\left(M_{q}, D\left(M_{q}\right)\right)$ is a closed operator. This is easy in case $E=C_{0}(X)$. For $E=L^{P}(k), 1 \leqq p<a$, we consider a sequence $\left(f_{n}\right)=E$ such that $\lim _{n \rightarrow \infty} f_{n}=f \in E$ and $\lim _{n \rightarrow \infty} q_{n}=: g$ $\epsilon E$. Choose a subsequence $\left(f_{n(k)}\right)_{k \in \mathbb{N}}$ such that $\lim _{k \rightarrow \infty} f_{n(k)}(x)=$ $f(x)$ and $\lim _{k+\infty} g(x) f_{n(k)}(x)=g(x)$ for $w-a l m o s t$ every $x \in X$. Then $g=q \cdot f$ and $f \in D\left(M_{q}\right)$, i.e. $M_{q}$ is closed.
For such multiplication operators many properties can be checked quite directly. For example, the following statements are equivalent:
(a) $M_{q}$ is bounded.
(b) $q$ is (p-essentially) bounded.

One has $\left\|M_{q}\right\|=\|q\|_{o}$ in this situation.

Observe that on spaces $C(K), K$ compact, there are no densely defined, unbounded multiplication operators.

By defining the multiplication semigroups

$$
T(t) f(x):=\exp (t \cdot q(x)) f(x) \quad, x \in X, f \in E,
$$

one obtains the following characterizations.

Proposition, Let $M_{q}$ be a multiplication operator on $E=C_{o}(X)$ or $E=L^{P}(X, L, H), 1 \leqq p<\infty$. Then the properties (a) and (b) , resp. ( $a^{\prime}$ ) and ( $b^{\prime}$ ), are equivalent:
(a) $M_{q}$ generates a strongly continuous semigroup.
(b) $\sup \{$ Re $g(x): x \in x\}<\infty$.

$$
\begin{aligned}
& \text { (a') } M_{q} \text { generates a uniformly } \\
& \text { continuous semigroup. } \\
& \text { (b') } \sup \{|\mathrm{q}(\mathrm{x})|: x \in \mathrm{x}\}<\mathrm{m} .
\end{aligned}
$$

As a consequence one computes the growth bound of a multiplication semigroup as follows:

```
w}=\operatorname{sup}{\operatorname{Re}q(x):x\inX}\quad\mathrm{ in the case E = C C (X),
\omega}=|-\operatorname{ess-sup{Re g(x) : x G X} in the case E = L P(\mu).
```

It is a nice exercise to characterize those multiplication operators which generate strongly continuour groups.

We point out that the above results cover the cases of sequence spaces such as $C_{0}$ or $1^{p}, 1 \leq p<\infty$. An abstract characterization of generators of multiplication semigroups will be given in C-II, Thm.5.13.

### 2.4. Tranglation (Semi) Groups

Let $E$ to be one of the following function spaces $C_{o}\left(\mathbb{R}_{+}\right), C_{0}(\mathbb{R})$ or $L^{P}\left(\mathbb{R}_{+}\right), L^{P}(\mathbb{R})$ for $1 \leqq p<{ }^{(1)}$. Define $T(t)$ to be the (left) translation operator

$$
T(t) f(x):=f(x+t)
$$

for $x, t \in \mathbb{R}_{+}$, resp. $x, t \in \mathbb{R}$ and $f \in E$. Then (T(t)) $t \geq 0$ is a strongly continous semigroup, resp. group of contractions on $E$ and its generator is the first derivative $\frac{d}{d x}$ with 'maximal' domain. In order to be more precise we have to distinguish the cases $E=C_{o}$ and $\mathrm{E}=\mathrm{L}^{\mathrm{P}}$ :
(i) The generator of the translation (semi) group on $E=C_{o}\left(\mathbb{R}_{+}\right)$is

$$
\begin{aligned}
& \text { Af }:=\frac{d}{d x} f=f^{\prime}, \\
& D(A):=\left\{f \in E: f \text { differentiable and } f^{\prime} \in E\right\}
\end{aligned}
$$

Proof. For $f \in D(A)$ it follows that for every $x \in \mathbb{R}_{(+)}$

$$
\lim _{h \rightarrow 0} \frac{T(h) f(x)-f(x)}{h}=1 i_{h \rightarrow 0} \frac{f(x+h)-f(x)}{h} \text { exists }
$$

(uniformly in $x$ ) and coincides with $A f(x)$. Therefore $f$ is differentiable and fle E.
On the other hand, take $f \in E$ differentiable such that $f$ ' $\in E$. Then

$$
\left|\frac{f(x+h)-f(x)}{h}-f^{\prime}(x)\right| \leq \frac{l}{h} \int_{x}^{x+h}\left|f^{\prime}(y)-f^{\prime}(x)\right| d y
$$

where the last expression tends to zero uniformly in $x$ as $h \rightarrow 0$. Thus $f \in D(A)$ and $f^{\prime}=A f$.
(ii) The generator of the translation (semi)group on $E=L_{(R)}^{(+)}{ }_{(R)}$, $1 \times p<\infty, i s$

$$
\begin{aligned}
& A f:=\frac{d}{d x} f=f^{\prime}, \\
& D(A):=\left\{f \in E: f \text { absolutely continuous, } f^{\prime} \in E\right\}
\end{aligned}
$$

Proof. Take $f \in D(A)$ such that $\quad \lim _{h+0} \frac{1}{h}(T(h) f-f)=g \in E$. Since integration is continuous we obtain for every $a, b \in \mathbb{P}_{( }(+)$that
(*) $\frac{1}{h} \int_{b}^{b+h} f(x) d x-\frac{1}{h} \int_{a}^{a+h} f(x) d x=\int_{a}^{b} \frac{f(x+h)-f(x)}{h} d x$
converges to $\int_{a}^{b} g(x) d x$ as $h \rightarrow 0+$. But for almost all $a, b$ the left hand side of (*) converges to $\mathrm{f}(\mathrm{b})$ - f(a). By redefining f on a nullset we obtain

$$
f(y)=\int_{a}^{y} g(x) d x+f(a) \quad, \quad y \in \mathbb{R}(+1,
$$

which is an absolutely continuous function whose derivative is (almost everywhere) equal to $g$.

On the other hand, let $f$ be absolutely continuous such that $\mathrm{f}^{\prime} \in \mathrm{L}^{\mathrm{P}}$. Then

$$
\begin{aligned}
& \lim _{h \rightarrow 0} \int\left|\frac{f(x+h)-f(x)}{h}-f^{\prime}(x)\right|^{p} d x \\
= & \lim _{h \rightarrow 0} \int \frac{1}{h}\left|\int_{0}^{h}\left(f^{\prime}(x+s)-f^{\prime}(x)\right) d s\right|^{p} d x \\
= & \lim _{h \rightarrow 0} \int\left|\int_{0}^{1}\left(f^{\prime}(x+u h)-f^{\prime}(x)\right) d u\right|^{p} d x \\
\leq & \lim _{h \rightarrow 0} \iint_{0}^{1}\left|f^{\prime}(x+u h)-f^{\prime}(x)\right|^{p} d u d x \\
= & \int_{0}^{1} l_{0} i_{h \rightarrow 0} \int\left|f^{\prime}(x+u h)-f^{\prime}(x)\right|^{p} d x d u=0, \text { hence } f \in D(A) .
\end{aligned}
$$

### 2.5. Rotation Groups

On $E=C(f)$, resp. $E=\mathrm{L}^{\mathrm{P}}(\mathrm{I}, \mathrm{m}), 1 \leq \mathrm{P}<\infty$, m Lebesgue measure we have canonical groups defined by rotations of the unit circle $f$ with a certain period, i.e. for $0<r \in \mathbb{R}$ the operators

$$
R_{T}(t) f(z):=E\left(e^{2 \pi i t / E} \cdot z\right)
$$

yield a group $\left(R_{T}(t)\right)_{t \in \mathbb{R}}$ having period $\mathrm{T}_{\mathrm{t}}$, i.e. $\mathrm{R}_{\mathrm{f}}(\mathrm{T})=\mathrm{Id}$. As in Example 2.4 one shows that its generator has the form

```
D(A) = {f & E : f absolutely continuour, f' € E},
Af(z)=(2\pii/r)\cdotz*f'(z).
```

An isomorphic copy of the group $\left(R_{l}(t)\right)_{t \in \mathbb{R}}$ ig obtained if we consider $E=\{f \in C[0,1]: f(0)=f(1)\}$, resp. $E=\mathrm{I}^{\mathrm{P}}([0,17)$ and the group of 'periodic translations'

```
T(t)f(x):=f(y) for }y\in[0,1],y=x+t mod 
```

with generator

```
D(A) := {f & E : { absolutely continuous, f' & E} ,
Af:== 年.
```

2.6. Nilpotent Translation Semigroups

Take $E=L^{P}([0, \tau], m)$ for $1 \leq p<\infty$ and define

$$
T(t) f(x):=\left\{\begin{array}{ll}
f(x+t) & \text { if } x+t \leqq \tau \\
0 & \text { otherwise }
\end{array} .\right.
$$

Then $(T(t))_{t \geq 0}$ is a semigroup satisfying $T(t)=0$ for $t \geqq T$. Its generator is still the first derivative $A=\frac{d}{d x}$, but its domain is
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-11.jpg?height=47&width=1615&top_left_y=1501&top_left_x=209) fact, if $f \in D(A)$ then $f$ is absolutely continuous with $f^{\prime} \in E$. By Prop.l.6.i it follows that $T(t) f$ is absolutely continuous and hence $\mathrm{f}(\mathrm{T})=0$.

### 2.7. One-dimensional Diffusion Semigroup

For the second derivative

$$
B f(x):=\frac{d^{2}}{d x^{2}} f(x)=f^{\prime \prime}(x)
$$

we take the domain
$D(B):=\left\{f \in C^{2}[0,1]: E^{\prime}(0)=f^{\prime}(1)=0\right\}$
in the Banach space $E=C[0,1]$. Then $D(B)$ is dense in $C[0,1]$, but closed for the graph norm. Obviously, each function

$$
e_{n}(x):=\cos \pi n x, \quad n \in \mathbb{Z},
$$

is contained in $D(B)$ and an eigenfunction of $B$ pertaining to the eigenvalue $\lambda_{n}:-\pi^{z_{n}}{ }^{2}$. The linear hull

$$
\operatorname{span}\left\{e_{n}: n \in f\right\}=: E_{0}
$$

forms a subalgebra of $D(B)$ which by the Stoneweierstrass theorem is dense in $E$.
We now use $e_{n}$ to define bounded linear operators

$$
e_{n} \otimes e_{n}: f \rightarrow\left(\int_{0}^{1} f(x) e_{n}(x) d x\right) e_{n}=<f_{r} e_{n}>e_{n}
$$

satisfying $\left\|e_{n} \otimes e_{n}\right\| \leqq 1$ and
$\left(e_{n} e_{n}\right)\left(e_{m} e_{m}\right)=\theta_{n, m}\left(e_{n} e_{n}\right)$ for $n \in \mathbb{Z}$.
For $t>0$ we define

$$
\begin{aligned}
T(t) & :=\sum_{n \in \mathbb{Z}} \exp \left(-\pi^{2} n^{2} t\right) \cdot e_{n} \otimes e_{n} \\
& =e_{0} \otimes e_{0}+2 \Sigma_{n=1}^{\infty} \exp \left(-\pi^{2} n^{2} t\right) \cdot e_{n} e_{n}
\end{aligned}
$$

or

$$
\begin{aligned}
& T(t) f(x)=\int_{0}^{1} k_{t}(x, y) f(x) d y \\
& \quad \text { where } k_{t}(x, y)=1+2 \sum_{n=1}^{\infty} \exp \left(-\pi^{2} n^{2} t\right) \cos \pi n x \cos \pi n y .
\end{aligned}
$$

The Jacobi identity

$$
\begin{aligned}
w_{t}(x) & :=1 /(4 \pi t)^{\frac{1}{2}} \quad \sum_{m \in Z} \exp \left(-(x+2 m)^{2} / 4 t\right) \\
& =\frac{1}{2}+\sum_{n \in \mathbb{N}} \exp \left(-\pi^{2} n^{2} t\right) \cos \pi n x
\end{aligned}
$$

and trigonometric relations show that

$$
k_{t}(x, y)=w_{t}(x+y)+w_{t}(x-y)
$$

which is a positive function on $[0,1]^{2}$. Therefore $T(t)$ is a bounded operator on $\mathrm{C}[0,1]$ with
$\|T(t)\|=\|T(t) 1\|=\sup _{x \in[0,1]} j_{0}^{1} k_{t}(x, y) d y=1$.
From the behavior of $T(t)$ on the dense subspace $E_{0}$ it follows that
$(T(t)) t \geqslant 0$ with $T(0)=I d$ is a strongly continuous semigroup on $E$ and its generator $A$ coincides with $B$ on $E_{o}$. Finally we observe that $E_{0}$ is a core for ( $A, D(A)$ ) by Prop.l.9(ii).
Consequently $(T(t))_{t \geq 0}$ is the semigroup generated by the closure of the second derivative with domain $\mathrm{D}(\mathrm{B})$.
2.8. n-dimensional Diffusion Semigroup

On $E=\mathbb{L}^{\mathrm{P}}\left(\mathbb{R}^{\mathrm{n}}\right), 1 \leqq \mathrm{p}<\infty$, the operators

$$
\begin{aligned}
T(t) f(x) & :=(4 \pi t)^{-n / 2} \int_{\mathbb{R}^{n}} \exp \left(-|x-y|^{2 / 4 t}\right) f(y) d y \\
& :=\psi_{t} * f(x)
\end{aligned}
$$

for $x \in \mathbb{R}^{n}, t>0$ and $\mu_{t}(x):=(4 \pi t)^{-n / 2} \exp (-|x| \geqslant / 4 t)$ form a strongly continuous semigroup:
In fact the integral exists for every $f \in \mathbb{I}^{P}\left(\mathbb{R}^{n}\right)$, since ${ }^{n} t$ is an element of the schwartz space $S\left(\Re^{\mathrm{n}}\right)$ of all rapidly decreasing smooth functions on $\mathbb{R}^{n}$.
Moreover,

$$
\|T(t) f\|_{P} \leqslant\left\|_{t}\right\|_{1}\|f\|_{P}=\|f\|_{P}
$$

by Young's inequality [Reed-simon (1975), p.28], hence $\|T(t)\| \leq 1$ for every $t>0$. Next we observe that $S\left(\mathbb{R}^{n}\right)$ is dense in $E$ and invariant under each $T(t)$. Therefore we can apply the Fourier trans-
formation $F$ which leaves $S\left(\mathbb{R}^{n}\right)$ invariant and yields $F\left(\mu_{t}^{* f}\right)=(2 \pi)^{n / 2} F\left(\mu_{t}\right) \cdot F(f)=(2 \pi)^{n / 2} \vec{\mu}_{t} \cdot \frac{\mathcal{H}_{1}}{n}$
where $f \in S\left(\mathbb{R}^{n}\right)$, 直 $=F f \in S\left(\mathbb{R}^{n}\right)$.
In other words, $F$ transforms $\left(T(t) \|_{S\left(\mathbb{R}^{n}\right)}\right) t \geqslant 0$ into a multiplication semigroup on $S\left(\mathbb{R}^{n}\right)$ which is pointwise continuous for the usual topology of $S\left(\mathbb{R}^{n}\right)$. The generator, i.e. the right derivative at 0 , of this semigroup is the multiplication operator

$$
\text { B帝 }(x):=-|x|^{2}+(x)
$$

for every $f \in S\left(\mathbb{R}^{n}\right)$.
Applying the inverse Fourier transformation and observing that the topology of $S\left(\mathbb{R}^{n}\right)$ is finer than the topology induced from $I^{P}\left(\mathbb{R}^{n}\right)$, we obtain that $(T(t)) t \geqq 0$ is a semigroup which is strongly continuous (use Remark 1.2 , (3)) and its generator A coincides with

$$
\Delta f(x)=\sum_{i=1}^{n} \frac{\xi^{2}}{\delta x^{2}} \quad f\left(x_{1}, \ldots, x_{n}\right)
$$

for every $f \in S\left(R^{n}\right)$.
Since $S\left(\mathbb{R}^{n}\right)$ is (T(t))-invariant we have determined the generator on a core of its domain (see Prop.l.9.ii).
In particular the above semigroup 'solves' the initial value problem for the 'heat equation'
$\frac{\delta}{\delta t} f(x, t)=\Delta f(x, t), f(x, 0)=f_{0}(x), x \in \mathbb{R}^{n}$.
For the analogous discussion of the unitary group on $\mathrm{L}^{2}\left(\mathbb{R}^{\boldsymbol{n}}\right)$ generated by
$C:=i \Delta$
we refer to Section $I X .7$ in Reed-Simon (1975).
Analogous examples to 2.7 are valid in $\pm[0,1]$, resp. to 2.8 in $C_{o}\left(\mathbb{R}^{n}\right)$.

## 3. STANDARD CONSTRUCTIONS

Starting with a semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$ it is possible to construct new semigroups on spaces naturally associated with $E$. Such constructions will be important technical devices in many of the subseguent proofs. Although most of these constructions are rather routine, we present in the sequel a systematic account of them for the convenience of the reader.
We always start with a semigroup ( $T(t)$ ) $t \geq 0$ on a Banach space $E$, and denote its generator by $A$ on the domain $D(A)$.

### 3.0. Similar Semigroups

There is an easy way how to obtain different (but isomorphic) semi-
groups out of a given semigroup ( $T(t))_{t a 0}$ on a Banach space $E$. Let $V$ be an isomorphism from $E$ onto $E$. Then $s(t):=V T(t) V^{-1}$, $t \geqq 0$, defines a strongly continuous semigroup. If $A$ is the generator of (T(t)) tep then

$$
B:=V^{-1} \text { with domain } D(B):=\left\{f \in E: V^{-1} £ \in D(A)\right\}
$$

is the generator of $(S(t))_{t \geq 0}$.

### 3.1. The Rescaled Semigroup

For fixed $\lambda \in \mathbb{C}$ and $a>0$ the operators

$$
S(t):=\exp (\lambda t) T(\alpha t)
$$

yield a new semigroup having generator

$$
B:=a A+h i d \text { with } D(B)=D(A) .
$$

This 'rescaled semigroup' enjoys most of the properties of the original semigroup and the same is true for the corresponding generators. However, by using this procedure certain constants associated with $(T(t))_{t \geq 0}$ and $A$ can be normalized. For example, by this rescaling we may in many cases suppose without loss of generality that the growth bound $\omega$ is zero.
Another application is the following: For $\hbar \in \mathbb{C}$ and $S(t):=\exp (-\lambda t) T(t)$ the formulas (1.3) and (1.4) yield:

$$
e^{-\lambda t} T(t) f-f=(A-\lambda) \int_{0}^{t} e^{-\lambda s} T(s) f d s
$$

$$
\begin{equation*}
\left(e^{\lambda t}-T(t)\right) \pm=(\lambda-A) \int_{0}^{t} e^{\lambda(t-s)} T(s) f d s \quad \text { for } f \in E \text {. } \tag{3.1}
\end{equation*}
$$

and

$$
\begin{align*}
& e^{-\lambda t} T(t) f-f=\int_{0}^{t} e^{-\lambda s} T(s)(A-\lambda) f d s \\
& o r  \tag{3.2}\\
& \left(e^{\lambda t}-T(t)\right) f=\int_{0}^{t} e^{\lambda(t-s)} T(s)(\lambda-A) f d s \quad \text { for } f \in D(A) .
\end{align*}
$$

3.2. The Subspace semigroup

Assume $F$ to be a closed (T(t))-irvariant or, equivalently, $R(\lambda, A)$-invariant $(\lambda \in \mathbb{C}$, Red $>\omega$ ) subspace of $E$. Then the semigroup ( $T(t){ }_{1}$ ) $t \geqslant 0$ of all restrictions $T(t)|:=T(t)| F$ is strongly continuous on $F$. If (A,D(A)) denotes the generator of (T(t)) t>0 it follows from the (T(t))-invariance and closedness of $F$ that $A$ maps $D(A) \cap F$ into $F$. Therefore
$A_{\mid}:=A_{\mid D(A) \cap F}$ with domain $D(A \mid):=D(A) \quad r: F$
is the generator of (T(t) $\mid$.

Conversely, if $F$ is a closed 'linear subspace of $E$ with $A(D(A) \cap F)=F$ such that $A$ is a generator on $F$, then $F$ is (T ( t ) ) -invariant.
An A-invariant subspace need not necessarily be (T(t))-invariant: Take for example the translation group with $T(t) f(x)=f(x+t)$ on $E=C_{0}(\mathbb{R})$ and $F:=\{f \in E: f(x)=0$ for $x \leq 0\}$.
3.3. The Quotient Semigroup
s.et $F$ be a closed ( $T(t)$ )-invariant subspace of $E$ and consider the quotient space $E_{/}:=E_{/ F}$ with quotient map $q: E+E_{/}$. The quotient operators

$$
T(t), q(f):=q(T(t) f), f \in E,
$$

are well defined and form a strongly continuous semigroup

$$
(T(t), t \geqslant 0
$$

on $E /$. For the generator ( $A /, D(A /)$ ) of ( $T(t) /)_{t \geqq 0}$ the following holds:

$$
D(A)=q(D(A)) \quad \text { and } \quad A / q(f)=q(A f)
$$

for every $£ \in D(A)$. Here we use the fact that every $\hat{f}:=q(f) \in$ D(A,) can be written as
$\hat{f}=\int_{0}^{\infty} e^{-\lambda s} \hat{T}(s) / \hat{g} d s=\int_{0}^{\infty} e^{-\lambda s} q(T(s) g) d s=q\left(\int_{0}^{\infty} e^{-\lambda s} T(s) g d s\right)=q(h)$
where $h \in D(A)$ and $\lambda>($ see (1.6)). In particular we point out that for every $\hat{\mathbb{E}} \in D(\mathbb{A}$,$) there exist representatives f \in \hat{\mathbb{F}}$ belonging to $D(A)$.

Example. We start with the Banach space $E=L^{1}(\mathbb{R})$ and the translation semigroup ( $T(t))_{t \geq 0}$ where $T(t) f(x):=f(x+t)$ (see Example 2.4). Then $L^{l}((-\infty, l])$ can be identified with the closed, (T(t))-invariant subspace

```
J :={f f E: f(x)=0 for 1< x< < }
```

and we obtain the subspace semigroup

$$
\left.T(t)\right|^{f(x)}=1_{(-\infty, 1]}(x) \cdot f(x+t),
$$

where $f \in L^{1}((-\infty, 1]), \underline{-}<x \leqq 1$ and $t \geqq 0$.
By 2.4 and 3.2 its generator is
$\mathrm{A}_{\mid} \mathrm{f}:=\mathrm{f}$,
for $\mathrm{f} \in \mathrm{B}(\mathrm{A} \mid)$
Next we identify $\mathbb{L}^{1}([0,1])$ with the quotient space $L^{1}((-\infty, 1])$ fit where

$$
I:=\left\{f \in L^{l}((-\infty, 1]): f(x)=0 \text { for } 0 \leqq x \leq 1\right\} \text {. }
$$

Again $I$ is invariant for the restricted semigroup $(T(t)$ ) and the
quotient semigroup $(T(t) / /)$ on $L^{1}([0, I])$ is the nilpotent translation semigroup as if Example 2.6. In particular it follows that the domain of the generator is
$D\left(A \mid / \prime=\left\{f \in L^{1}([0,1]): f \in A C\right.\right.$ with $f^{\prime} \in L^{1}([0,1])$ and $\left.f(1)=0\right\}$.

### 3.4. The Adjoint Semigroup

The adjoint operators (T(t)') ${ }_{t} \geqslant 0$ of a strongly continuous semigroup (T(t)) $t_{0}$ on a Banach space $E$ form a semigroup on $E$ which need, however, not be strongly continuous.

Example. Take the translation operators $T(t) f(x)=f(x+t)$ on $E=L^{1}(\mathbb{R})$ (see Example 2.4) and their adjoints $T(t) ' f(x)=f(x-t)$
on $E^{\prime}=L^{\infty}(\mathbb{R})$. Then $\left(T(t)^{\prime}\right) t \in \mathbb{R}$ is a one-parameter group which is not strongly continuous on $L^{*}(\mathbb{R})$ (take any non-trivial characteristic function).

Since the semigroup (T(t) ') $t \geq 0$ is obviously weak*-continuous in the senge that $\lim _{t^{+} s}\left\langle f,\left(T(t)^{\prime}-T(s)^{\prime}\right) \phi\right\rangle=0$ for every f $f E, \phi \in E^{\prime}$ and $s, t$ 齐 0 , it is natural to associate (T(t)') $t \geq 0$ its a weak*generator
$A^{\prime} \phi:=\sigma\left(E^{\prime}, E\right)-1 i m \frac{1}{h}\left(T(h)^{\prime} \phi-\phi\right)$ for every $\phi$ in the domain $D\left(A^{*}\right):=\left\{\phi \in E^{\prime}: \phi(E ', E)-1 i m \frac{l}{h}\left(T(h)^{\prime} \phi-\phi\right)\right.$ exists $\}$.
This operator coincides with the adjoint of the generator (A, D(A)), i.e.
$D\left(A^{\prime}\right)=\left\{申 \in E^{\prime}:\right.$ there exists $\psi \in E^{\prime}$ such that $\langle f, \psi\rangle=\langle A f, \phi\rangle$ for all $\mathrm{E} \in \mathrm{D}(\mathrm{A})\}$
and $A^{\prime} \phi=\psi$.
In particular, $A^{\prime}$ is a closed and $a\left(E^{+}, E\right)$ densely defined operator in $E^{\prime}$.

It follows from Thm.III.5.30 in Kato (1966) that the resolvent $R\left(h, A^{\prime}\right)$ of $A^{\prime}$ is $R(\lambda, A)$. In particular, the spectra $\sigma(A)$ and $\sigma\left(A^{\prime \prime}\right)$ coincide. But it is still necessary in some situations to have strong continuity for the adjoint semigroup. In order to achieve this we restrict $T(t)^{\prime}$ to an appropriate subspace of $E^{1}$.

Definition (Phillips, 1955). The semigroup dual of the Banach space E with respect to the strongly continuous semigroup (T(t)) tzo is

$$
E^{*}:=\left\{\phi \in E^{\prime}:\|\cdot\|-1 i m t+0 T(t)^{\prime} \phi=\phi\right\} .
$$

The adjoint semigroup on $E^{*}$ is given by the operators $T(t) *:=T(t) * E^{*} \quad, t \geq 0$.
Since $\left(T(t)^{*}\right) t \geqslant 0$ is strongly continuous on $E *$ we call its generator (A*,D(A*)) the adjoint generator.

The above definition makes sense since $E^{*}$ ig norm-closed in $E^{*}$ and (T(t) ')-invariant. The main point is that $E^{*}$ is still reasonably large. In fact, since $\int_{0}^{t} T(s)^{\prime} \phi d s$, understood in the weak sense, is contained in $E^{*}$ for every $\phi \in E^{\prime}, t \geq 0$ it follows that
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-17.jpg?height=53&width=1609&top_left_y=790&top_left_x=218)
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-17.jpg?height=61&width=1611&top_left_y=843&top_left_x=217) $E^{*}$ is $\sigma\left(E^{\prime}, E\right)-$ dense in $E^{\prime}$. In addition the estimate of $\|\cdot\|$ given above yields

```
|T(t)*|\leq|T(t)|\leqqM|T(t)*| for all t \ 0.
```

In the following proposition we describe the relation between $A^{*}$ and $\mathrm{A}^{*}$.

Proposition. For the adjoint generator $A^{*}$ of a strongly continuous semigroup (T(t)) $t \geq 0$ on $E$ the following assertions hold:
(i) $E^{*}$ is the $\|\cdot\|$-closure of $D\left(A^{*}\right)$.
(ii) $\quad D\left(A^{*}\right)=\left\{\phi \in D\left(A^{\prime}\right): A^{\prime} \phi \in E^{*}\right\}$.
(iii) $A^{*}$ and $A^{\prime}$ coincide on $D\left(A^{*}\right)$.

Proof. (i) Take $\phi \in D\left(A^{\prime}\right)$ fixed. For every $f \in D(A)$ with $\|f\| I$ we define a continuously differentiable function

$$
t \rightarrow \xi_{f}(t):=<T(t) f_{1} \phi^{2}
$$

on $[0,1]$ with derivative $\xi_{f}^{\prime}(t)=\langle T(t) A f, \phi\rangle=\left\langle T(t) f, A^{*} \phi\right\rangle$.
Since $\left\{\xi_{f}^{\prime}(t) ; t \in[0,1], f \in D(A),\|f\| \leq 1\right\}$ is bounded it follows that the set
$\left\{\xi_{\mathrm{f}}: f \in \mathrm{f}(\mathrm{A}),\|f\| \leqslant 1\right\}$
is equicontinuous at 0 , i.e. for every $\varepsilon>0$ there exists $0<t_{0}<1$ such that
$\left|\xi_{f}(s)-\xi_{f}(0)\right|=\left|<f, T(s)^{\prime} \phi-\phi\right\rangle \mid<\varepsilon$
for every $0 \leq s \leqq t_{0}$ and $f \in D(A),\|f\| \leqq 1$. But this implies $\|^{T}(s)^{\prime} \phi^{\prime}-\phi^{\prime} \dot{\|}<\varepsilon$ and hence $\phi \in E^{*}$. Conversely take $\psi \in E^{*}$. Then $\frac{l}{t} \int_{0}^{t} T(s) ' \psi d s, t>0$, belongs to $D\left(A^{\prime}\right)$ and nom converges to $\psi$ as $t \rightarrow 0, i . e . \psi$ belongs to the norm closure of $D\left(A^{\prime}\right)$.
(ii) and (iii): Since the weak* topology on $E$ is weaker than the norm topology it follows that $A^{*}$ is an extension of $A^{*}$.
Now take $\phi \in D\left(A^{\prime}\right)$ such that $A^{\prime} \phi \in E^{*}$. As above define the func-
tions $\xi_{f}$. The assumption on $\phi$ implies the set of all derivatives
$\{\xi=\mathrm{f} \in \mathrm{D}(\mathrm{A}),\|f\| \leqq 1\}$
to be equicontinuous at $t=0$. This means that for every $s>0$ there exists $0<t_{0}<1$ such that $\left|\xi_{f}^{\prime}(0)-\xi_{f}^{\prime}(s)\right| \leqslant \varepsilon$ for every $f \in D(A),\|f\|_{i} \leq 1$ and $0<s<t_{0}$.
In particular,

$$
\varepsilon>\left|\xi_{f}^{\prime}(0)-\frac{1}{s}\left(\xi_{f}(s)-\xi_{f}(0)\right)\right|=\left|\left\langle\mathcal{F}_{, ~} A^{\prime} \phi-\frac{1}{s}\left(T(s)^{*} \phi-\phi\right)\right\rangle\right|
$$

hence
$\varepsilon>\left\|_{\|}^{\prime} \phi-\frac{l}{s}\left(T(s)^{\prime} \phi-\phi\right)\right\|$
for all $0 \leq s \leq t_{0}$. From this it follows that $\phi \in D\left(A^{*}\right)$.

On reflexive Banach spaces we have $A^{*}=A^{\prime}$ by the above proposition. In other cases this construction is more interesting.

Example(continued). The adjoints of the (left) translation $T(t)$ on $E=L^{1}(\mathbb{R})$ are the (right) translations $T(t)^{\prime}$ on $E^{*}=L^{\infty}(\mathbb{R})$. The largest subspace of $L^{(1)}(\mathbb{R})$ on which these translations form a semigroup which is strongly continuous with respect to the sup-norm, is the space of all bounded uniformly continuous functions on $\mathbb{F}$, i.e. $E^{*}=C_{b u}(\mathbb{R})$.
Calculating $D\left(A^{\prime}\right)$ and $D\left(A^{*}\right)$ respectively, one obtains $D\left(A^{\prime}\right)=\left\{f \in L^{(\infty}(\mathbb{R})=£ \in A C, f^{\prime} \in L^{\infty}(\mathbb{R})\right\}$, $D\left(A^{*}\right)=\left\{f \in L^{(\mathbb{D}}(\mathbb{R})=f \in C^{l}(\mathbb{R}), f^{*} \in \mathcal{C}_{b u}(\mathbb{R})\right\}$.
Obviously, the function $x \rightarrow|\sin x|$ belongs to $D\left(A^{\prime}\right)$ but not to D ( $A^{*}$ ) .

### 3.5. The Associated Sobolev Semigroups

Since the generator $A$ of a strongly continuous semigroup ( $\mathbf{T}(t))_{t \geq 0}$ is closed, its domain $D(A)$ becomes a Banach space for the graph norm $\|f\|_{1}:=\|f\|+\|A f\|$.
We denote this Banach space by $E_{1}$ and the continuous injection from $E_{1}$ into $E$ by $i_{1}$. Since $E_{1}$ is invariant under ( $\left.T(t)\right)_{t \geq 0}$ * apply Prop.l.6.i - it makes gense to consider the semigroup $\left(T_{1}(t)\right)_{t \geq 0}$ of all restrictions $T_{1}(t):=T(t) \mid E_{1}$. The results of Prop.1.6 imply that $T_{1}(t) \in L\left(E_{1}\right)$ and $\left\|T_{1}(t) f=f\right\|_{1} \rightarrow 0$ as $t \rightarrow 0$ for every $f \in E_{1}$. Thus $\left(T_{1}(t)\right)_{t \geq 0}$ is a strongly continuous semigroup on $E_{1}$ and has a generator denoted by ( $A_{1}, D\left(A_{1}\right)$ ) Using Prop. 1.6 again we see that $A_{1}$ is the restriction of $A$ to $E_{1}$ with maximal domain, i.e.
$D\left(A_{1}\right)=\left\{f \in E_{1} ; A f \in E_{1}\right\}=D\left(A^{2}\right)$ and
$A_{1} f=A f$ for every $f \in D\left(A_{1}\right)$.
It is now possible to repeat this construction in order to obtain Banach spaces $E_{n}$ and semigroups $\left(T_{n}(t)\right)_{t \geqq 0}$ with generators ( $A_{n}, D\left(A_{n}\right)$ which are related as visualized in the following diagram:
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-19.jpg?height=723&width=1061&top_left_y=661&top_left_x=543)

For the translation semigroup on $\mathbb{E}^{P}(\mathbb{R})$ (see 2.3) the above construction leads to the usual 'sobolev spaces'. Therefore we might call En the $n$-th sobolev space and $\left(T_{n}(t)\right)_{t \geqslant 0}$ the $n-t h$ Sobolev semigroup associated to $E$ and $(T(t))_{t \geqslant 0}$.
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-19.jpg?height=50&width=1617&top_left_y=1774&top_left_x=202) $R(A, A)$ are isomorphisms from $E_{1}$ onto $E$, resp. from $E$ onto $E_{1}$ (show that $\|\cdot\|_{1}$ and $\|\cdot\|_{\lambda}$ with $\left\|_{\|}\right\|_{\lambda}:=\|_{\|}^{\|}-A$ ) $\|$ are equivalent). In addition, the diagram
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-19.jpg?height=306&width=715&top_left_y=2040&top_left_x=548)
commutes. Therefore all Sobolev semigroups ( $\left.E_{n},\left(T_{n}(t)\right)_{t z 0}\right)$, $n \in \mathbb{A}$, are isomorphic.
2. For $\lambda \in \rho(A)$ consider the norm

$$
\|f\|_{-1}:=\|R(\lambda, A) f\|
$$

for every $f \in E$ and define $E_{-1}$ as the completion of $E$ for $\|\cdot\|-1$.

Then ( $T(t)$ ) $t \geq 0$ extends continuously to a strongly continuous semigroup $\left(T_{-1}(t)\right)_{t \geq 0}$ on $E_{-1}$ and the above diagram can be extended to the negative integers.

### 3.6. The F-Product Semigroup

It is a very successful mathematical method to consider a sequence of points in a certain space as a point in a new and larger space. In particular such a method can serve to convert an approximate eigenvector of a linear operator into an eigenvector. Occasionally we will need such a construction and refer to section v.l of schaefer (1974) for the details.
If we try to adapt this construction to strongly continuous semigroups we encounter the difficulty that the semigroup extended to the larger space will not remain strongly continuous. An idea already used in 3.4 will help to overcome this difficulty.

Let $T=(T(t))$ t>0 be a strongly continuous semigroup on the Banach space $E$. Denote by $m(E)$ the Banach space of all bounded E-valued sequences endowed with the norm

$$
\left\|\left(f_{n}\right)_{n \in \mathbb{N}}\right\|:=\sup \left\{\left\|f_{n}\right\|: n \in \mathbb{N}\right\} .
$$

It is clear that every $T(t)$ extends canonically to a bounded linear operator

$$
T(t)\left(f_{n}\right):=\left(T(t) f_{n}\right)
$$

on $m(E)$, but the semigroup $(\hat{T}(t)) t \geqslant 0$ is strongly continuous if and only if $T$ has a bounded generator. Therefore we restrict our attention to the closed, ( $\mathbf{T}(\mathrm{t})$ )-invariant subspace
$m^{\top}(E):=\left\{\left(f_{n}\right) \in m(E): 1 m_{t \rightarrow 0}\left\|T(t) f_{n} \mathcal{F}_{n}\right\|=0\right.$ uniformly for $\left.n \in \mathbb{N}\right\}$. Then the restricted semigroup

$$
\tilde{T}(t)\left(f_{n}\right)=\left(T(t) f_{n}\right),\left(f_{n}\right) \in m^{\top}(E),
$$

is strongly continuous and we denote its generator by ( ${ }_{\mathrm{A}}^{\mathrm{A}}, \mathrm{D}(\hat{\mathrm{A}})$ ) . The following lemma shows that $A$ ig obtained canonically from $A$.

Lemma. For the generator $\tilde{A}$ of $(\tilde{T}(t))_{t \geq 0}$ on $m^{\top}(E)$ one has: (i) $D(A)=\left\{\left(f_{n}\right) \in m^{T}(E): f_{n} \in D(A)\right.$ and $\left.\left(A f_{n}\right) \in m^{\top}(E)\right\}$, (ii)

$$
A\left(f_{n}\right)=\left(A f_{n}\right) \text { for }\left(f_{n}\right) \in D(A)
$$

For the proof we refer to Lemma 1.4. of Derndinger (1980).

Now let $F$ be any filter on $\mathbb{N}$ finer than the Frechet filter (i.e. the filter of sets with finite complement). (In most cases $F$ will be either the Frechet filter or some free ultra filter.) Then the sub-
space of all F-null sequences in m(E)

$$
c_{F}(E):=\left\{\left(f_{n}\right) \in m(E): F-l i m\left\|f_{n}\right\|=0\right\}
$$

is closed in $m(E)$ and invariant under $(\hat{T}(t)) t \geqq 0$. We call the quotient spaces

$$
E_{F}:=m(E) / c_{F}(E) \quad \text { and } \quad E_{F}^{\top}:=m^{\top}(E) / C_{F}(E) r m^{\top}(E)
$$

the F-product of $E$ and the F-product of $E$ with respect to the semigroup $T$, respectively. Thus $E_{F}^{\top}$ can be considered as a closed linear subspace of $E_{F}$. We have $E_{F}^{T}=E_{F}$ if (and only if) $T$ has a bounded generator.
The canonical quotient norm on $E_{F}$ is given by $\left\|\left(f_{n}\right)+c_{F}(E)\right\|=F-1 i m \sup \left\|f_{n}\right\|$.
We can apply 3.3 in order to define the F-product semigroup $\left(T_{F}(t)\right)_{t \geqq 0}$ on $E_{F}^{\top}$ by

$$
T_{F}(t)\left(\left(f_{n}\right)+c_{F}(E)\right):=\left(T(t) f_{n}\right)+c_{F}(E) \cap m^{\top}(E)
$$

Thus $T_{F}(t)$ is the restriction of $T(t) F$ where $T(t) F$ denotes the canonical extension of $T(t)$ to the F-product $E_{F}$. (Note that (T(t) ${ }_{F}$ t $\geq 0$ is not strongly continuous unless $T$ has a bounded generator.)
With the canonical injection $j: f \rightarrow(f, f, f, \ldots)+c_{f}(E)$ from $E$ into $E_{F}^{\top}$ the operators $T_{F}(t)$ are extensions of $T(t)$ satisfying $\left\|T_{F}(t)\right\|=\|T(t)\|$. The basic facts about the generator ( $\left.A_{F}, D\left(A_{F}\right)\right)$ of $\left\{T_{F}(t)\right)_{t \geqslant 0}$ follow from 3.3 and are collected in the following proposition.

Proposition. For the generator $\quad\left(A_{F} D\left(A_{F}\right)\right)$ of the F-product semigroup the following holds:

$$
\begin{align*}
& D\left(A_{F}\right)=\left\{\left(f_{n}\right)+c_{F}(E): f_{n} \in D(A) ;\left(f_{n}\right),\left(A f_{n}\right) \in M^{\top}(E)\right\}  \tag{i}\\
& A_{F}\left(\left(f_{n}\right)+C_{F}(E)\right)=\left(A E_{n}\right)+c_{F}(E) . \tag{ii}
\end{align*}
$$

In case $A$ is a bounded operator then $D\left(A_{F}\right)=E_{F}^{T}=E_{F}$ and $A_{F}$ is the canonical extension of $A$ to $E_{F}$. We will show in A-iII, 4. 5 that the above construction preserves and even improves many spectral properties of the semigroup and its generator.

### 3.7. The Tensor Product Semigroup

Real- or complex-valued functions of two variables $x$, $Y$ are often limits of functions of the form $\sum_{i=1}^{n} f_{i}(x) g_{i}(y)$, which to some extent allows one to consider the variables $x$ and $y$ separately.

Since algebraic manipulation with these latter functions is governed by the formal rules of a tensor product, it is customary to identify (for example) the function

$$
(x, y) \rightarrow f(x) g(y)
$$

with the tensor product $f$ g $g$ and to consider limits of linear combinations of such functions as elements of a completed tensor product. To be more precise, we briefly present the most important examples for this situation.

Examples. 1. Let (X,,$\ldots)$ and ( $Y, \Omega, v$ ) be measure spaces. Identifying for $f_{i} \in L^{P}(\mu), g_{i} \in L^{P}(v)$ the elements $\sum_{i=1}^{n} f_{i} g_{i}$ of the tensor product

$$
L^{P}(\mu) \ominus I^{P}(v)
$$

with the (class of $\mu \times v-a . e .-$ defined) functions

$$
(x, y) \rightarrow \sum_{i=1}^{n} f_{i}(x) g_{i}(y),
$$

$L^{P}(\mu) \quad L^{P}(v)$ becomes a dense subspace of $L^{P}(X \times Y, \Sigma \times \Omega, \mu \times v)$ for $1 \leq \mathrm{P}<\infty$ 。
2. Similarly, let $X, Y$ be compact spaces. Then
$C(X) \otimes C(Y)$
becomes a dense subspace of $C(X X Y)$ by identifying, for $f \in C(X)$ and $g \in C(Y), f(g$ with the function
$(x, y) \rightarrow f(x) g(y)$.

We do not intend to go into a deeper investigation of the quite sophisticated problems related to normed tensor products of general Banach spaces, but will rather confine ourgelves to the discussion of certain special cases. These will always be related to one of the following standard methods to define a norm on the tensor product of two Banach spaces $E, F$;
Let $u: \pm \sum_{i=1}^{n} f_{i} g_{i}$ be an element of $E \geqslant F$. Then
(i) $\quad\|u\|_{\pi}:=\inf \left[\sum_{i=1}^{F l}\left\|h_{i}\right\|\left\|k_{i}\right\|: u=\sum_{i=1}^{F l} h_{i} \otimes k_{i}, h_{i} \in E, k_{i} \in F\right\}$ defines the "greatest cross norm $\pi$ " on $E$. $F$.
(ii) $\|u\|_{\varepsilon}:=\sup \left(<u, \phi \in \psi>: \phi \in E^{\prime}, \psi \in F^{\prime},\|\phi\|,\|\psi\| \leq 1\right\}$ defines the "least cross norm $E$ " on $E \times F$. Here, $<u, \phi$ © $\psi$ denotes the canonical bilinear form on ( $E=F$ ) $\times\left(E^{\prime} \otimes F^{\prime}\right)$, i.e. $\left\langle\sum_{i=1}^{n} f_{i} \otimes g_{i} \mid \phi \otimes \psi\right\rangle=\sum_{i=1}^{n}\left\langle f_{i}, \phi\right\rangle\left\langle g_{i}, \psi\right\rangle$.
(iii) if $E$ and $F$ are Hilbert spaces, $\|u\|_{h}=(u \mid u){ }_{h}^{1 / 2}$, where the scalar product $(\cdot \mid \cdot)_{h}$ is defined as in (ii), defines the "Hilbert norm h" on E F .

In the following we write $E \sigma_{a} F$ for the tensor product of $E$ and F endowed - if applicable - with one of the norms $\pi, E$, h just defined. In each care one has $\| f(g\|=\| f\| \| g \|$ for $f \in E, g \in f$. By E $\boldsymbol{g}_{\mathrm{a}} \mathrm{F}$ we mean the completion of $E{ }_{\mathrm{a}}^{\mathrm{m}} \mathrm{F}$. Moreover we recall how examples 1 and 2 above fit into this pattern:

$$
\begin{aligned}
& L^{1}(\mu \otimes v)=L^{1}(\mu) \tilde{\theta}_{\pi} L^{1}(v), \quad L^{2}(\mu \theta v)=L^{2}(\mu) \tilde{\theta}_{h} L^{2}(v), \\
& C(X M Y)=C(X) \quad C(Y) \quad .
\end{aligned}
$$

Finally we point out that for any $S \in L(E)$, $T \in L(F)$, the mapping

$$
\sum_{i=1}^{n} f_{i} \circlearrowleft g_{i} \rightarrow \sum_{i=1}^{n} S f_{i} \circlearrowleft T g_{i}
$$

defined on $E \in F$ is linear and continuous on $E \theta_{a} F$, hence has a continuous extension to $E \vec{a}_{\alpha} F$. This operator, as well as its continuous extension, will be denoted by $S$ e $T$ and satisfies $\|S \in T\|=\|S\|\|T\|$. The notation $A$ \& will also be used in the obvious way if $A$ and $B$ are not necessarily bounded operators on $E$ and $F$. We are now ready to consider semigroups induced on tensor product.
proposition. Let $\left(S(t) t_{t \geqslant 0}\right.$ and (T(t)) $t \geqslant 0$ be strongly continuous semigroups on Banach spaces $E, F$, and let $A$, $B$ be their generators. Then the family
$(s(t) \in T(t))_{t \geqslant 0}$
is a strongly continuous semigroup on $E \tilde{e}_{\alpha} F$. The closure of
$A \Leftrightarrow I d+I d \Theta B$,
defined on the core $D(A) \quad D(B)$ is its generator.
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-23.jpg?height=69&width=1620&top_left_y=2010&top_left_x=201) semigroup of operators on $E \vec{a}_{a} \mathbf{F}$. The strong continuity need only be verified at $t=0$ and on elements of the form $u=f 0 g \in E=F$. This verification being straightforward, there remains to show that the generator of $(S(t) \text { 埳 ( } t \text { ) })_{t a 0}$ is obtained as the closure of (A $A d+I d \in B, D(A) \quad D(B))$. To this end, let $f \in D(A)$ and
![](https://cdn.mathpix.com/cropped/2025_01_15_c4d840c576acbbb2eea4g-23.jpg?height=72&width=1178&top_left_y=2351&top_left_x=202)

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{1}{h}(T(h) f \otimes(S(h) g-g)+(T(h) f-f) \theta g) \\
& =(f \otimes B g)+(A f \otimes g)
\end{aligned}
$$

Since the elements of the form $f \otimes g, f \in D(A), g \in D(B)$, generate the linear subspace $D(A) \operatorname{D}(B) \quad O E \tilde{G}_{\alpha} F$, this subspace belongs
to the domain of the generator. Moreover, $D(A)$ D(B) is dense in $E{ }_{a} F$ and invariant under $(S(t) \theta T(t))$ t¥o, hence it is a core of A 0 Id + Id B by Prop.1.9.ii.

### 3.8. The Product of Commuting Semigroups

Let $(S(t))_{t \geq 0}$ and $(T(t)) t \geq 0$ be semigroups with generators $A$ and $B$, respectively on some Banach space $E$. It is not difficult to see that the following assertions are equivalent.
(i) $S(t) T(t)=S(t) T(t)$ for all $t \geqq 0$.
(ii) $R(\mu, A) R(\mu, B)=R(k, B) R(k, A)$ for some $\mu \in \rho(A) \cap \rho(B)$.
(iii) $R(\mu, A) R(\mu, B)=R(\mu, B) R(\&, A)$ for all $\mu \in \rho(A)$ 自 $\rho(B)$.

In that case $U(t)=S(t) T(t)(t \geq 0)$ defines a semigroup (U(t)) $t \geq 0^{*}$ Using Prop. $1.9(i i)$ one easily shows that $D_{o}: D(A) r(B)$ is a core for its generator $C$ and $C f=A f+B f$ for all $f \in D_{D}$.

NOTES,
For a more complete information on semigroup theory we refer the reader to hillePhillips (1957), to the recent monographs by Davies (1980), Goldstein (1985a) and Pazy (1983), to the survey article by krein-khazan (1985) and to the bibliography by Goldstein (1985b).

