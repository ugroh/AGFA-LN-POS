\section*{CHAPTER A-I}

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

\section*{1. STANDARD DEFINITIONS AND RESULTS}

We consider a one-parameter semigroup (T(t)) t¥0 on a Banach space $E$ and observe that the domain $\mathbb{R}_{+}$and the range $L(E)$ of the (semi~
group) homomorphism $r: t+T(t)$ are topological semigroups for the natural topology on $\mathbb{R}_{+}$and any one of the standard operator topologiss on $L(E)$. We single out the strong operator topology on L(E) and require $\tau$ to be continuous.

Definition $1.1 . \quad$ A one-parameter semigroup ( $T(t))_{t \geqslant 0}$ is called strongly continuous if the map $t \rightarrow T(t)$ is continuous for the strong operator topology on $L(E)$, i.e. limt $t_{0} \| T(t) f-T\left(t_{o}\right) f=0$ for every $f \in E$ and $t, t_{0} \geqslant 0$,

Clearly one defines in a similar way weakly continuous, resp. uniformly continuous (compare A-II, Def..1.19) semigroups, but since we concentrate on the strongly continuous case we agree on the follow ing terminology:
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-012.jpg?height=52&width=1526&top_left_y=1145&top_left_x=319) tinuous one-parameter semigroup of bounded linear operators.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-016.jpg?height=55&width=1200&top_left_y=1200&top_left_x=225)

Remarks 1.12. (1) For continuous Banach space valued functions such as $t \rightarrow T(t) f$ we consider the Riemann integral and define $\int_{0}^{\infty} T(t) f d t \quad a s \quad l_{m} m_{t \rightarrow \infty} \int_{0}^{t} T(s) f d s$. Sometimes such integrals for strongly continuous semigroups $(T(t))$ t $\geqslant 0$ are written as $\int_{a}^{b} T(t) d t$ and understood in the strong sense.
(2) since the generator (A,D(A)) determines the semigroup (T(t)) t>0 uniquely, we will speak occasionally of the growth bound of the generator instead of the semigroup, i.e. we write $\omega=\omega(A)=w(T(t)) t \geq 0)$. (3) For one-parameter groups it might seem to be more natural to define the generator as the 'derivative' rather than just the 'right derivative' at $t=0$. This yields the same operator as the following result shows:
The strongly continuous semigroup (T(t)) $t \geqslant 0$ with generator $A$ can be extended to a strongly continuous one-parameter group (u(t)) $t \in \mathbb{R}$ if and only if $-A$ generates a semigroup $(s(t))_{t \geq 0}$.

In that case (U(t)) $t \in \mathbb{R}$ is obtained as
$$
U(t):= \begin{cases}T(t) & \text { for } t \geqslant 0 \\ s(-t) & \text { for } t \leqslant 0\end{cases}
$$

We refer to [Davies (1980), Prop.1.14] for the details.

\section*{2. STANDARD EXAMPLES}

In this section we list and discuss briefly the most basic examples of semigroups together with their generators. These semigroups will reappear throughout this book and will be used to illustrate the theory. We start with the class of semigroups mentioned after Definition 1.1 .

\subsection*{2.1. Uniformly Continuous Semigroups}

It follows from elementary operator theory that for every bounded operator $A \in L(E)$ the sum
$$
\xi_{n=0}^{m} t^{n} A^{n} / n!=: e^{t A}
$$
exists and determines a unique uniformly continuous (semi)group ( $e^{t A}$ ) $t \in \mathbb{R}$ having $A$ as its generator.
Conversely, any uniformly continuous semigroup is of this form: If the semigroup $(T(t))$ tzo is uniformly continuous, then $\frac{1}{t} \int_{0}^{t} T(s) d s$ uniformly converges to $T(0)=I d a s t \rightarrow 0$. Therefore for some $t$ ' $=0$ the operator $\frac{1}{t} \int_{0}^{t} T(s) d s$ is invertible and every $f \in E$ is of the form $f=\frac{1}{t} \int_{0}^{t^{t}} T(s) g d s$ for some $g \in E$. But these elements belong to $D(A)$ by (1.3), hence $D(A)=E$. Since the generator $A$ is closed and everywhere defined it must be bounded.
Remark that bounded operators are always generators of groups, not just semigroups. Moreover the growth bound $w$ satisfies $|w| \leqslant\|A\|$ in this situation.

The above characterization of the generators of uniformly continuous semigroups as the bounded operators shows that these semigroups are at least in many aspects - rather simple objects.

\subsection*{2.2. Matrix Semigroups}

The above considerations expecially apply in the situation $E=\mathbb{C}^{n}$. If $n=2$ and $A=\left(a_{i j}\right)_{2 \times 2}$ the following explicit formulas for $e^{t A}$ might be of interest:
Set $s:=\operatorname{trace} A, d:=\operatorname{det} A$ and $D:=\left(s^{2}-4 d\right)^{1 / 2}$. Then
$$
\begin{aligned}
e^{t A}= & e^{t s / 2} \cdot\left[D^{-1} 2 \sinh (t D / 2) \cdot A+\left(\cosh (t D / 2)-s D^{-1} \sinh (t D / 2)\right) \cdot I d\right] \\
& \text { if } D \neq 0, \\
e^{t A}= & e^{t s / 2} \cdot[t A+(1-t s / 2) \cdot I d] \quad \text { if } D=0, r e s p .
\end{aligned}
$$

\subsection*{2.3. Multiplication Semigroups}

Many Banach spaces appearing in applications are Banach spaces of (real or) complex valued functions over a set $X$. As the most
standard of these "function spaces", we mention the space $C_{0}(X)$ of all continuous complex valued functions vanishing at infinity on a locally compact space $X$, or the spacer $L^{P}(X, \Sigma, k), 1 \leqq p \leqq \infty$, of all (equivalence classes of) p-integrable functions on a $\sigma$-finite measure space $(X, 5, \mu)$.

On these function spaces $E=C_{o}(X)$, resp. $E=L^{P}(X, E, k)$, there is a simple way to define "multiplication operatorg" : Take a continuous, resp. measurable function $q: x \rightarrow \mathbb{C}$ and define
$$
M_{q} f:=q \cdot f, \text { i.e. } \quad M_{q} f(x):=q(x) \cdot f(x) \text { for } x \in X,
$$
for every $f$ in the "maximal" domain $D\left(M_{G}\right):=\{g \in E: G * G \in \in\}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-018.jpg?height=69&width=1617&top_left_y=1025&top_left_x=228) for $1 \leqq p<{ }^{c}$. Moreover, $\left(M_{q}, D\left(M_{q}\right)\right)$ is a closed operator. This is easy in case $E=C_{0}(X)$. For $E=L^{P}(k), 1 \leqq p < a $, we consider a sequence $\left(f_{n}\right)=E$ such that $\lim _{n \rightarrow \infty} f_{n}=f \in E$ and $\lim _{n \rightarrow \infty} q_{n}=: g$ $\epsilon E$. Choose a subsequence $\left(f_{n(k)}\right)_{k \in \mathbb{N}}$ such that $\lim _{k \rightarrow \infty} f_{n(k)}(x)=$ $f(x)$ and $\lim _{k+\infty} g(x) f_{n(k)}(x)=g(x)$ for $w-a l m o s t$ every $x \in X$. Then $g=q \cdot f$ and $f \in D\left(M_{q}\right)$, i.e. $M_{q}$ is closed.
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

\subsection*{2.4. Tranglation (Semi) Groups}

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

\subsection*{2.5. Rotation Groups}

On $E=C(f)$, resp. $E=\mathrm{L}^{\mathrm{P}}(\mathrm{I}, \mathrm{m}), 1 \leq \mathrm{P}<\infty$, m Lebesgue measure we have canonical groups defined by rotations of the unit circle $f$ with a certain period, i.e. for $0  \in \mathbb{R}$ the operators
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

Then $(T(t)) t \geq 0$ is a semigroup satisfying $T(t)=0$ for $t \geqq T$. Its generator is still the first derivative $A=\frac{d}{d x}$, but its domain is
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-021.jpg?height=47&width=1615&top_left_y=1501&top_left_x=209) fact, if $f \in D(A)$ then $f$ is absolutely continuous with $f^{\prime} \in E$. By Prop.l.6.i it follows that $T(t) f$ is absolutely continuous and hence $\mathrm{f}(\mathrm{T})=0$.

\subsection*{2.7. One-dimensional Diffusion Semigroup}

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
e_{n} \otimes e_{n}: f \rightarrow\left(\int_{0}^{1} f(x) e_{n}(x) d x\right) e_{n}= < f_{r} e_{n}>e_{n}
$$
satisfying $\left\|e_{n} \otimes e_{n}\right\| \leqq 1$ and
$\left(e_{n} e_{n}\right)\left(e_{m} e_{m}\right)=\hat{o}_{n, m}\left(e_{n} \otimes e_{n}\right)$ for $n \in \mathbb{Z}$.
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

\section*{3. STANDARD CONSTRUCTIONS}

Starting with a semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$ it is possible to construct new semigroups on spaces naturally associated with $E$. Such constructions will be important technical devices in many of the subseguent proofs. Although most of these constructions are rather routine, we present in the sequel a systematic account of them for the convenience of the reader.
We always start with a semigroup ( $T(t)$ ) $t \geq 0$ on a Banach space $E$, and denote its generator by $A$ on the domain $D(A)$.

\subsection*{3.0. Similar Semigroups}

There is an easy way how to obtain different (but isomorphic) semi-
groups out of a given semigroup ( $T(t))_{t a 0}$ on a Banach space $E$. Let $V$ be an isomorphism from $E$ onto $E$. Then $s(t):=V T(t) V^{-1}$, $t \geqq 0$, defines a strongly continuous semigroup. If $A$ is the generator of (T(t)) tep then
$$
B:=V^{-1} \text { with domain } D(B):=\left\{f \in E: V^{-1} £ \in D(A)\right\}
$$
is the generator of $(S(t))_{t \geq 0}$.

\subsection*{3.1. The Rescaled Semigroup}

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
where $f \in L^{1}((-\infty, 1]), \underline{-} < x \leqq 1$ and $t \geqq 0$.
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

\subsection*{3.4. The Adjoint Semigroup}

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-027.jpg?height=53&width=1609&top_left_y=790&top_left_x=218)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-027.jpg?height=61&width=1611&top_left_y=843&top_left_x=217) $E^{*}$ is $\sigma\left(E^{\prime}, E\right)-$ dense in $E^{\prime}$. In addition the estimate of $\|\cdot\|$ given above yields

\[
|T(t)*|\leq|T(t)|\leqqM|T(t)*| for all t \ 0.
\]

In the following proposition we describe the relation between $A^{*}$ and $\mathrm{A}^{*}$.

Proposition. For the adjoint generator $A^{*}$ of a strongly continuous semigroup (T(t)) $t \geq 0$ on $E$ the following assertions hold:
(i) $E^{*}$ is the $\|\cdot\|$-closure of $D\left(A^{*}\right)$.
(ii) $\quad D\left(A^{*}\right)=\left\{\phi \in D\left(A^{\prime}\right): A^{\prime} \phi \in E^{*}\right\}$.
(iii) $A^{*}$ and $A^{\prime}$ coincide on $D\left(A^{*}\right)$.

Proof. (i) Take $\phi \in D\left(A^{\prime}\right)$ fixed. For every $f \in D(A)$ with $\|f\| I$ we define a continuously differentiable function
$$
t \rightarrow \xi_{f}(t):= < T(t) f_{1} \phi^{2}
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

\subsection*{3.5. The Associated Sobolev Semigroups}

Since the generator $A$ of a strongly continuous semigroup ( $\mathbf{T}(t))_{t \geq 0}$ is closed, its domain $D(A)$ becomes a Banach space for the graph norm $\|f\|_{1}:=\|f\|+\|A f\|$.
We denote this Banach space by $E_{1}$ and the continuous injection from $E_{1}$ into $E$ by $i_{1}$. Since $E_{1}$ is invariant under ( $\left.T(t)\right)_{t \geq 0}$ * apply Prop.l.6.i - it makes gense to consider the semigroup $\left(T_{1}(t)\right)_{t \geq 0}$ of all restrictions $T_{1}(t):=T(t) \mid E_{1}$. The results of Prop.1.6 imply that $T_{1}(t) \in L\left(E_{1}\right)$ and $\left\|T_{1}(t) f=f\right\|_{1} \rightarrow 0$ as $t \rightarrow 0$ for every $f \in E_{1}$. Thus $\left(T_{1}(t)\right)_{t \geq 0}$ is a strongly continuous semigroup on $E_{1}$ and has a generator denoted by ( $A_{1}, D\left(A_{1}\right)$ ) Using Prop. 1.6 again we see that $A_{1}$ is the restriction of $A$ to $E_{1}$ with maximal domain, i.e.
$D\left(A_{1}\right)=\left\{f \in E_{1} ; A f \in E_{1}\right\}=D\left(A^{2}\right)$ and
$A_{1} f=A f$ for every $f \in D\left(A_{1}\right)$.
It is now possible to repeat this construction in order to obtain Banach spaces $E_{n}$ and semigroups $\left(T_{n}(t)\right)_{t \geqq 0}$ with generators ( $A_{n}, D\left(A_{n}\right)$ which are related as visualized in the following diagram:
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-029.jpg?height=723&width=1061&top_left_y=661&top_left_x=543)

For the translation semigroup on $\mathbb{E}^{P}(\mathbb{R})$ (see 2.3) the above construction leads to the usual 'sobolev spaces'. Therefore we might call En the $n$-th sobolev space and $\left(T_{n}(t)\right)_{t \geqslant 0}$ the $n-t h$ Sobolev semigroup associated to $E$ and $(T(t))_{t \geqslant 0}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-029.jpg?height=50&width=1617&top_left_y=1774&top_left_x=202) $R(A, A)$ are isomorphisms from $E_{1}$ onto $E$, resp. from $E$ onto $E_{1}$ (show that $\|\cdot\|_{1}$ and $\|\cdot\|_{\lambda}$ with $\left\|_{\|}\right\|_{\lambda}:=\|_{\|}^{\|}-A$ ) $\|$ are equivalent). In addition, the diagram
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-029.jpg?height=306&width=715&top_left_y=2040&top_left_x=548)
commutes. Therefore all Sobolev semigroups ( $\left.E_{n},\left(T_{n}(t)\right)_{t z 0}\right)$, $n \in \mathbb{A}$, are isomorphic.
2. For $\lambda \in \rho(A)$ consider the norm
$$
\|f\|_{-1}:=\|R(\lambda, A) f\|
$$
for every $f \in E$ and define $E_{-1}$ as the completion of $E$ for $\|\cdot\|-1$.

Then ( $T(t)$ ) $t \geq 0$ extends continuously to a strongly continuous semigroup $\left(T_{-1}(t)\right)_{t \geq 0}$ on $E_{-1}$ and the above diagram can be extended to the negative integers.

\subsection*{3.6. The F-Product Semigroup}

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

\subsection*{3.7. The Tensor Product Semigroup}

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-033.jpg?height=69&width=1620&top_left_y=2010&top_left_x=201) semigroup of operators on $E \vec{a}_{a} \mathbf{F}$. The strong continuity need only be verified at $t=0$ and on elements of the form $u=f 0 g \in E=F$. This verification being straightforward, there remains to show that the generator of $(S(t) \text { 埳 ( } t \text { ) })_{t a 0}$ is obtained as the closure of (A $A d+I d \in B, D(A) \quad D(B))$. To this end, let $f \in D(A)$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-033.jpg?height=72&width=1178&top_left_y=2351&top_left_x=202)
$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{1}{h}(T(h) f \otimes(S(h) g-g)+(T(h) f-f) \theta g) \\
& =(f \otimes B g)+(A f \otimes g)
\end{aligned}
$$

Since the elements of the form $f \otimes g, f \in D(A), g \in D(B)$, generate the linear subspace $D(A) \operatorname{D}(B) \quad O E \tilde{G}_{\alpha} F$, this subspace belongs
to the domain of the generator. Moreover, $D(A)$ D(B) is dense in $E{ }_{a} F$ and invariant under $(S(t) \theta T(t))$ t¥o, hence it is a core of A 0 Id + Id B by Prop.1.9.ii.

\subsection*{3.8. The Product of Commuting Semigroups}

Let $(S(t))_{t \geq 0}$ and $(T(t)) t \geq 0$ be semigroups with generators $A$ and $B$, respectively on some Banach space $E$. It is not difficult to see that the following assertions are equivalent.
(i) $S(t) T(t)=S(t) T(t)$ for all $t \geqq 0$.
(ii) $R(\mu, A) R(\mu, B)=R(k, B) R(k, A)$ for some $\mu \in \rho(A) \cap \rho(B)$.
(iii) $R(\mu, A) R(\mu, B)=R(\mu, B) R(\&, A)$ for all $\mu \in \rho(A)$ 自 $\rho(B)$.

In that case $U(t)=S(t) T(t)(t \geq 0)$ defines a semigroup (U(t)) $t \geq 0^{*}$ Using Prop. $1.9(i i)$ one easily shows that $D_{o}: D(A) r(B)$ is a core for its generator $C$ and $C f=A f+B f$ for all $f \in D_{D}$.

NOTES,
For a more complete information on semigroup theory we refer the reader to hillePhillips (1957), to the recent monographs by Davies (1980), Goldstein (1985a) and Pazy (1983), to the survey article by krein-khazan (1985) and to the bibliography by Goldstein (1985b).

In this chapter two different problems are treated:
1) to characterize generators of strongly continuous semigroups,
2) to characterize various properties of strongly continuous semigroups in terms of their generators.

In section 1 the first problem is solved by finding conditions on the Cauchy problem associated with $A$ and also by finding conditions on the resolvent of $A$. The second problem is treated for a hierarchy of smoothness properties of the semigroup.

Contraction semigroups are considered in section 2. Here, the first problem has a simple and extremely useful solution: A densely defined operator $A$ is generator of a contraction semigroup if and only if A is dissipative and satisfies a range condition. Our approach is quite general. We do not only consider contractions with respect to the norm but also with respect to "half-nomms". This will allow us to obtain results on positive contraction semigroups simultaneously by choosing a suitable halfmorm (cf. C-II, Sec.l).

The last section contains a surprising result: on certain Banach spaces (e.g., $L^{\text {ºn }}$ ) only bounded operators are generators of strongly continuous semigroups.
1. THE ABSTRACT CAUCHY PROBLEM, SPECIAL SEMIGROUPS AND PERTURBATION
by
Wolfgang Arendt

Linear differential equations in Banach spaces are intimately connected with the theory of one-parameter semigroups. In fact, given a closed linear operator $A$ with dense domain $D(A)$ the following statement is true (with some reservation regarding a technical detail): The abstract cauchy problem
$$
\begin{aligned}
& \dot{u}(t)=A u(t) \quad(t \geqslant 0) \\
& u(0)=f
\end{aligned}
$$
has a unique solution for every $f \in D(A)$ if and only if $A$ is the generator of a strongly continuous semigroup.

This is one characterization of generators which illustrates their important role for applicationg. The fundamental Hille-Yosida theorem gives a different characterization in terms of the resolvent and yields a powerful tool for actually proving that a given operator is the generator of a semigroup.

Another problem we will treat here is how diverse properties of a semigroup can be described in terms of its generator. This is a reasonable question from the theoretical point of view (since the generator uniquely determines the semigroup). It is of interest from the practical point of view as well: the generator is the given object, defined by the differential equation. It is useful to dispose of conditions of the generator itself giving information on the solutions (which might not be known explicitely). We discuss smoothness properties such as analyticity, differentiability, norm continuity and compactness of the semigroup.

A frequent method to obtain new generators out of a given one is by perturbation. We will have a brief look at this circle of problems at the end of this section.

The results are explained and illustrated by examples. Proofs are only given when new aspects are presented which are not yet contained in the literature, otherwise we refer to the recent monographs Davies (1980), Goldstein (1985a), Pazy (1983).

\section*{The Abstract Cauchy Problem}

Let $A$ be a closed operator on a Banach space $E$ and consider the abstract Cauchy problem
$(A \subset P) \quad\left\{\begin{array}{l}\dot{u}(t)=A u(t) \quad(t \geq 0) \\ u(0)=f .\end{array}\right.$
By a solution of (ACP) for the initial value $f \in D(A)$ we understand a continuously differentiable function $u:[0, \infty) \rightarrow E$ satisfying $u(0)=f$ and $u(t) \in D(A)$ for all $t a 0$ such that $\bar{u}(t)=A u(t)$ for $t \geqq 0$.

By A-I,Thm.1.7 there exists a unique solution of (ACP) for all initial values in the domain $D(A)$ whenever $A$ is the generator of a strongly continuous semigroup. The converse does not hold (see Example l.4. below). However, for the operator $A{ }_{1}$ on the Banach space $E_{1}=D(A)(s e e A-I, 3.5)$ with domain $D(A, 1)=D\left(A^{2}\right)$ given by $A_{1} f=A f\left(f \in D\left(A_{1}\right)\right)$ the following holds.

Theorern l.l. The following assertions are equivalent.
(i) For every $f \in D(A)$ there exists a unique solution of (ACP).
(ii) A ${ }_{1}$ is the generator of a strongly continuous semigroup.

Proof. (i) implies (ii).
Assume that (i) holds; i.e., for every $f \in D(A)$ there exists a unique solution $u(*, f) \in C^{l}([0,+), E)$ of (ACP). For $f \in E_{1}$ define $T_{1}(t) f:=u(t, f)(t \geqslant 0)$. By the uniqueness of the solutions it follows that $T_{1}(t)$ is a linear operator on $E_{1}$ and $T_{1}(s+t)=$ $T_{1}(s) T_{1}(t)$. Moreover, since $u(\cdot, f) \in C^{1}$, it follows that $t \rightarrow T_{1}(t) f$ is continuous from $[0, \infty)$ into $E_{1}$. We show that $T_{1}(t)$ is a continuous operator for all $t>0$.
Let $t>0$. Consider the mapping $\quad \pi: E_{1} \rightarrow C\left([0, t], E_{1}\right)$ given by $\eta(f)=T_{1}(\cdot) f=u(\cdot, f)$. We show that $\eta$ has a closed graph.
In fact, let $f_{n} \rightarrow f$ in $E_{1}$ and $\eta_{1}\left(f_{n}\right)=u\left(*, f_{n}\right) \rightarrow v \quad$ in $C\left([0, t], E_{1}\right)$. Then $u\left(s_{,} f_{n}\right)=f_{n}+\int_{0}^{S} A u\left(r, f_{n}\right) d r$. Letting $n \rightarrow \infty \quad$ we obtain $v(s)=f+\int_{0}^{s} A v(r) d r$ for $0 x s \leqq t$. Let
$\stackrel{v}{v}(s)=T_{1}(s-t) v(t)$ for $s>t$, and $\ddot{v}(s)=v(s)$ for $0 \leq s \leq t$.

Then $\tilde{v}$ is a solution of (ACP). It follows that $\stackrel{v}{v}(s)=T_{1}(s) f$ for all $s \geqslant 0$. Hence $v=\eta(f)$. We have shown that $\eta$ has a closed graph and so $\eta$ is continuous. This implies the continuity of $T_{1}(t)$. It remains to show that $A_{1}$ is the generator of ( $\mathrm{T}_{1}(\mathrm{t}){ }_{\mathrm{t}}^{\mathrm{t}} \mathrm{O} 0^{*}$

We first show that for $f \in D\left(A^{2}\right)$ one has
(1.1) $\quad \mathrm{AT}_{1}(\mathrm{t}) \pm=\mathrm{T}_{1}(\mathrm{t}) \mathrm{Af}$.

In fact, let $v(t)=f+\int_{0}^{t} u(s, A f) d s$. Then
$\dot{v}(t)=u(t, A f)=A f+\int_{0}^{t} A u(s, A f) d s=A\left(f+\int_{0}^{t} u(s, A f) d s\right)=A v(t)$.
Since $v(0)=f, i t$ follows that $v(t)=u(t, f)$.
Hence $A u(t, f)=A v(t)=\dot{v}(t)=u(t, A f)$. This is (1. 1).
Now denote by $B$ the generator of $\left(T_{1}(t)\right)_{t \geq 0}$.
For $f \in D\left(A^{2}\right)$ we have
$$
\lim _{t \rightarrow 0} \frac{T_{1}(t) f-f}{t}=A f
$$
and by (1.1),
$\lim _{t \rightarrow 0} A \frac{T_{1}(t) f-f}{t}=\lim _{t \rightarrow 0} \frac{T_{1}(t) A f-A f}{t}=A^{2} f$ in the norm of $E$.

Hence $\lim _{t \rightarrow 0} \frac{T_{1}(t) f-f}{t}=$ Af in the norm of $E_{1}$.
This shows that $A_{1}=B$. In order to show the converse, let $f \in D(B)$. Then $\lim _{t \rightarrow 0} \quad A \frac{T_{1}(t) f-f}{t}$ exists in the norm of $E$.

Since $\lim _{t \rightarrow 0} \frac{T_{1}(t) f-f}{t}=A f$ in the norm of E, it follows that Af $\in D(A)$, since $A$ is closed. Thus $f \in D\left(A^{2}\right)=D\left(A_{1}\right)$. We have shown that $B=A_{1}$.
(ii) implies (i).

Assume that ${ }^{A} 1$ is the generator of a strongly continuous semigroup $\left(T_{1}(t)\right)_{t \geqslant 0}$ on $E_{1}$. Let $f \in D(A)$ and set $u(t)=T_{1}(t) f$. Then $u \in C([0, \infty), E)$ and $A u(\cdot) \in C([0, \infty), E)$.
Moreover, $\int_{0}^{t} u(s) d s=\int_{0}^{t} T_{1}(s) f d s \in D\left(A_{1}\right)=D\left(A^{2}\right)$ and $A \int_{0}^{t} u(s) d s=$ $u(t)-u(0)=u(t)-E \quad(b y A-I,(1,3))$.
Consequently, $u(t)=f+A \int_{0}^{t} u(s) d s=f+\int_{0}^{t} A u(s) d s$.
Hence $u \in C^{l}([0, \infty), E)$ and $\dot{u}(t)=A u(t)$. Thus $u$ is a solution of (ACP) . We have shown existence.

In order to show uniqueness, assume that $u$ is a solution of (ACP) with initial value 0 . We have to show that $u \equiv 0$. Let $v(t)=\int_{0}^{t} u(s) d s$. Then $v(t) \in D(A)$ and $A v(t)=\int_{0}^{t} A u(s) d s=$ $\int_{0}^{t} \dot{u}(s) d s=u(t) \in D(A)$. Consequently, $v(t) \in D\left(A^{2}\right)$ for all $t \geqslant 0$. Moreover, $\quad \dot{v}(t)=u(t)=A v(t) \quad$ and $\quad \frac{d}{d t} A v(t)=A u(t)=A v(t)=$ $A^{2} v(t)$. Thus $v \in C^{1}\left([0, \infty), E_{1}\right)$ and $\dot{v}(t)=A_{1} v(t)$. Since $v(0)=0$, it follows that $v \equiv 0$. Thus $u \equiv v \equiv 0$.

If (ACP) has a unique solution for every initial value in $D(A)$, then A is the generator of a strongly continuous semigroup only if some additional assumptions on the solutions (continuous dependence from the initial value) or on $A(\rho(A) \neq \varnothing)$ are made.

Corollary 1.2. Let $A$ be a closed operator. Consider the following existence and uniqueness condition.
(EU) For every $f \in D(A)$ there exists a unique solution $u(\cdot, f) \in C^{1}([0, \infty), E)$ of the Cauchy problem associated with $A$ having the initial value $u(0, f)=f$.

The following assertions are equivalent.
(i) A is the generator of a strongly continuous semigroup.
(ii) A satisfies (EJ) and $\rho(A) \neq 0$.
(iii) $A$ satisfies (EJ) and for every $k \in \mathbb{R}$ there exists $h>$ iush that $(A-A) D(A)=E$.
(iv) A satisfies (EU), has dense domain and for every sequence (f ${ }_{n}$ ) in $D(A)$ satisfying $\quad \lim _{n \rightarrow \infty} f_{n}=0$ one has $l i m_{n \rightarrow \infty} u\left(t_{, ~}^{f} f_{n}\right)=0$ uniformly in $t \in[0,1]$.

Propf. It is clear that (i) implies the remaining assertions. So assume that $A$ satisfy (EU). Then by Theorem l.l., $\mathrm{A}_{1}$ is a generator. If there exists $\lambda \in \rho(A)$, then $(\lambda-A)$ is an isomorphism from $E_{1}$ onto $E$ and $A$ is similar to $A$ via this isomorphism [since $D\left(A_{1}\right)=\left[(\lambda-A)^{-1} f: f \in D(A)\right) \quad$ and $A f=(\lambda-A) A_{1}(\lambda-A)^{-1} f$ for all f $\in D(A)$, see $A-I, 3.0]$. Thus $A$ is a generator on $E$ and we have shown that (ii) implies (i). If (iii) holds, then there exists $\lambda>s\left(A_{1}\right)$ such that $(\lambda-A) D(A)=E$. We show that ( $\lambda-A$ ) is injective. Then $\lambda \in p(A)$ since $A$ is closed. Assume that $A f=\lambda f$ for some $f \in D(A)$. Then $E \in D\left(A^{2}\right)=D\left(A_{1}\right)$, and so $f=0$ since $\lambda \in \rho\left(A_{1}\right)$. This proves that (iii) implies (ii).

It remains to show that (iv) implies (i). Assertion (iv) implies that for all $t \geq 0$ there exist bounded operators $T(t) \in L(E)$ such that $u(t, f)=T(t) f$ if $f \in D(A)$. Moreover, sup $0 \leqslant t \leqslant 1\|T(t)\|_{\|}^{\prime} \in$. It follows that $T(\cdot) f$ is strongly continuous for all $f \in E$ (since it is so for $f \in D(A)$ and $D(A)$ is dense). Let $t>1$. There exist unique $n \in N$ and $s \in[0,1)$ such that $t=n+s . \operatorname{Let} T(t):=$ $T(1)^{n} T(s)$. From the uniqueness of the solutions it follows that $T(t) f=u(t, f)$ for all $t \geqq 0$ as well as $T(t+s) f=T(s) T(t) f$ for all $f \in D(A)$ and $s, t \geqslant 0$. Thus ( $T(t))_{t \geqslant 0}$ is a semigroup.
Denote by $B$ its generator. It follows from the definition that $A \subset B, \quad$ Moreover, $D(A)$ is invariant under the semigroup. $S o b y$ A-I,Prop.1.9.(ii) D(A) is a core of B. Since A is closed this implies that $A=B$.

Remark 1.3. It is surprising that from condition (ii) and (iii) in the corollary it follows automatically that $D(A)$ is dense. On the other hand this condition cannot be omitted in (iv). In fact, consider any generator $A$ and its restriction $A$ with domain $D(A)=\{0\}$. Then $A$ satisfies the remaining conditions in (iv) but is not a generator (if dim $E=0$ ).

Example l.4. We give a densely defined closed operator $A$, such that there exists a unique solution of (ACP) for all initial values in $D(A)$, but $A$ is not a generator.
Let $B$ be a densely defined unbounded closed operator on a Banach space $F$. Consider $E=F \oplus F$ and $A$ on $E$ given by
$$
A=\left(\begin{array}{ll}
0 & B \\
0 & 0
\end{array}\right)
$$
with domain $F \times D(B)$.
Then $D\left(A^{2}\right)=\{(f, g) \in F \times D(B): B g \in P\}=D(A) \quad$ and $\quad$ so $A_{1} \in L\left(E_{1}\right)$. In particular, $A_{1}$ is a generator, But $A$ is not. For instance condition (ii) in Corollary 1.2. does not hold, since for each $\lambda \in \mathbb{C}$, $(\lambda-A) D(A)=\{(\lambda f-B g, \lambda g): f \in F, g \in D(B)\}$
$$
\subset \mathrm{F} \times \mathrm{D}(\mathrm{~B}) \neq F \times F=E
$$

So $\rho(A)=\emptyset$.
As a further illustration, we note that the solution of the corresponding abstract Cauchy problem for the initial value (f,g) $\epsilon$ $F \times D(B)$ is given by $u(t)=(f+t B g, g)$. Since $B$ is unbounded, condition (iv) of Corollary l.2. is clearly violated.

Remark. Frequently a generator $A$ can be extended to a closed operator $B$, Then one can consider the abstract cauchy problem ACP (B) associated with $B$. It also has a solution for every initial value in $D(B)$, but none of the solutions is unique unless $A=B$.
[In fact, denote by (T(t)) ${ }_{t \geq 0}$ the semigroup generated by $A$. Let $f \in D(B)$. Let $\lambda>\omega(A)$. Then there exists $g \in D(A)$ such that $(\lambda-B) f=(\lambda \rightarrow A) g$. Let $h=f-g$. Then $h \in \operatorname{ker}(\lambda-B)$. Define $u$ by $u(t)=e^{\lambda t} h_{h}+T(t) g$. Then $u$ is a solution ACP(B) with initial value f. It follows from Cor.l.2 that there exists a non-trivial solution for the initial value 0.$]$

\section*{One-parameter groups}

Generators of one-parameter groups can be characterized similarly by existence and uniqueness of the solutions of the associated Cauchy problem. However, here the assumption of continuous dependence on the initial values can be relaxed (in fact, one has no longer to assume that the continuous dependence is uniform in $t$ ).

Theorem 1.6. Let $A$ be a closed densely defined operator. The following assertions are equivalent.
(i) A is generator of a strongly continuous one-parameter group.
(ii) For every $f \in D(A)$ there exists a unique function
$u(\cdot, f) \in \mathbb{C}^{1}(\mathbb{R})$ satisfying $u(t, f) \in D(A)$ for all $t \in \mathbb{R}$ and $u(0, f)=f$ such that $\frac{d}{d t} u(t, f)=A u(t, f)$; and if $f_{n} \in D(A)$ such that $\lim _{n \rightarrow \infty} f_{n}=0$, then $\lim _{n \rightarrow \infty} u\left(t, f_{n}\right)=0$ for all $t \in R$

Proof. It is clear that (i) implies (ii). If (ii) holds then there exist operators $T(t) \in L(E)$ such that $u(t, f)=T(t) f \quad(t \in \mathbb{R}$, $f \in D(A))$. It follows from the uniqueness of the solutions that $T(t+s)=T(t) T(s) \quad(s, t \in \mathbb{R})$. Let $\mathcal{E} \in E$. There exist $f_{n} \in D(A)$ such that $\lim _{n \rightarrow \infty} f_{n}=f_{\text {. }}$
Then $\lim _{n \rightarrow \infty} T(t) f_{n}=T(t) f$ for all $t \in \mathbb{R}$. Since $T(\cdot) f$ is continuous, it follows that $T$ (.)f is measureable. Hence by
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-041.jpg?height=64&width=1617&top_left_y=2418&top_left_x=208) interval $J \subset(0, \infty)$. Because of the group property this implies that $T(\cdot)$ is norm bounded on bounded subsets of $\mathbb{R}$. $T(\cdot) f$ is continuous if $f \in D(A)$. Since $D(A)$ is dense this implies the strong continuity of (T( t$)_{t \in \mathbb{R}}$.

\section*{The Hille-Yosida theorem}

Given an operator A frequently it is easier to obtain information about its resolvent than to solve the Cauchy problem. Therefore the following theorem is central in the theory of one-parameter semigroups.

Theorem 1.7 (Hille-Yosidal. Eet $A$ be an operator on a Banach space E. The following conditions are equivalent.
(i) A is the generator of a strongly continuous semigroup.
(ii) There exist $w, M \in \mathbb{R}$ such that $(w, \infty) \subset \rho(A)$ and $\left\|(\lambda-w)^{n} R(\lambda, A){ }^{n}\right\| \leqq M$ for all $\lambda>W$ and $n \in \mathbb{N}$.

In general it is not easy to give an estimate for the powers of the resolvent which enables one to apply Theorem l.7. However, there is an important case when it suffices to consider merely the resolvent.

Corollary 1.8. For an operator $A$ on a Banach space $E$ the following assertions are equivalent.
(i) A is the generator of a strongly continuous contraction semigroup.
(ii) $(0, \infty) \subset \rho(A)$ and $\|\lambda R(\lambda, A)\| \cong 1$ for all $\lambda>0$.

The difficult part in the proof of Theorem l.7. is to show that (ii) implies (i). One has to construct the semigroup out of the resolvent. We mention two formulas which can be used for the proof.

Proposition 1.9. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geq 0^{\circ}}$ For $\lambda>0$ let $A(\lambda)=\lambda^{2} R(\lambda, A)-\lambda I d(=\lambda A R(\lambda, A))$. Then
(1.2) $T(t) f=\lim _{\lambda \rightarrow \infty} e^{t A(\lambda)} f$ for all $f \in E$ and $t \geqslant 0$.

Yosida's proof consists in showing that the limit in (1.2) exists under the hypothesis (ii) of Theorem l.2. (see [Davies (1980)], [Goldstein (1985b)] or [Pazy (1982)]). The proof of Hille (see [Kato (1966)]) is inspired by the following formula.

Proposition 1.10. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geqq 0}$. Then
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-043.jpg?height=72&width=1406&top_left_y=404&top_left_x=211)
```
for all f & E and t }\geqq0\mathrm{ .
```

\section*{Holomorphic semigroups}

We now describe a hierarchy of smoothness conditions on the semigroup, starting with the most restrictive class; namely, holomorphic semigroups. The generators of these semigroups can be characterized by a particularly simple condition.
For $\alpha \in(0, \pi ?$ we define the sector $s(a)$ in the complex plane by $S(\alpha)=\left\{r e^{i \theta}: r \geq 0, \theta \in(-\alpha, \alpha)\right\}$.

Definition l.ll. Let $a \in(0, \pi / 27$. A strongly continuous semigroup ( $T(t))_{t \geq 0}$ is called a bounded holomorphic semigroup of angle $a$ if T(*) is the restriction of a holomorphic function
$$
T: S(a) \neq l(E)
$$
satisfying
```
(1.4)T(z)T(z')=T(z+\mp@subsup{z}{}{\prime})
```
(1.5) For each $\alpha_{1} \in(0, \alpha)$ the set $\left\{T(z): z \in S\left(\alpha_{1}\right)\right\}$ is uniformly bounded and $1 i m_{n \rightarrow \infty} T\left(z_{n}\right) f=f$ for every null-sequence ( $z_{n}$ ) in $s\left(\alpha_{1}\right)$ and every $f \in E$.

Remark. A function $T: S(\alpha) \rightarrow L(E)$ is holomorphic with respect to the operator norm if and only if it is strongly holomorphic if and only if it is weakly holomorphic fYosida (1965); V.3].

Theorem 1.12. Let $A$ be a densely defined operator on a Banach space $E$ and $a \in(0, \pi / 2\urcorner$. Then $A$ is the generator of a bounded holomorphic semigroup of angle a if and only if
$$
S(a+\pi / 2) \subset \rho(A)
$$
and for every $a_{1} \in(0, \alpha)$ there exists a constant $M$ such that
$$
\begin{equation*}
\|R(\lambda, A)\| \leqq M /|\lambda| \quad\left(\lambda \in S\left(\alpha_{1}+\pi / 2\right)\right) \tag{1.6}
\end{equation*}
$$

For the proof we refer to [Davies (1980)], for example.
kemark. Let $A$ be the generator of a bounded holomorphic semigroup (T(t)) tzo of angle $a$, and let $z_{0} \in S(\alpha)$. Then $z_{Q} A$ generates a
bounded semigroup $(S(t))_{t \geqslant 0}$ given by $S(t)=T\left(z_{0} t\right) \quad(t \geqq 0)$ (where again we denote by $T$ the holomorphic extension of $(T(t))_{t \geq 0}$ on S(a)).

As an application of Theorem 1.12. we prove the following.

Corollary 1.13. Let $A$ be the generator of a bounded group. Then $A^{2}$ generates a bounded holomorphic semigroup of angle $\pi / 2$.

Proof. Let $0<\alpha_{1}<\pi / 2 ; \lambda \in S\left(\alpha_{1}+\pi / 2\right)$. There exist $r$ e and $B \in\left(-\beta_{1}, \beta_{1}\right)$ where $\beta_{1}:=\left(\alpha_{1}+\pi / 2\right) / 2$, such that $\lambda_{2}=r^{2} e^{i 2 \beta}$. Then $\left(A-A^{2}\right)=\left(r e^{i \beta}-A\right)\left(r e^{i \beta}+A\right)$; so it follows that $\lambda \in \rho\left(A^{2}\right)$ and (1.7) $R\left(\lambda, A^{2}\right)=R\left(r e^{i B}, A\right) R\left(r e^{i \beta},-A\right)$.

Since $A$ generates a bounded group, there exists a constant $\mathbb{N} \geq 0$ such that $\|R(\mu, A)\| \leqq \mathbb{N} / \operatorname{Re}^{\prime},\|R(\mu,-A)\| \leq \mathbb{N} /$ Re $\mu$ for all $\mu \in S(\pi / 2)$. Consequently, $\left\|R\left(\lambda, A^{2}\right)\right\| \leq N^{2} / r^{2}(\cos B)^{2} \leqq 1 / r^{2} \cdot\left[N / \cos e_{1} \jmath^{2}=M /|\lambda|\right.$.

The corollary will be extended below. We first consider an example.
Example (The Laplacian on $E=C_{o}\left(\mathbb{R}^{n}\right)$ or $L^{p}\left(\mathbb{F}^{n}\right)(1 \leqq p<\infty)$ ).
a) Let $n=1$. Then $(U(t) f)(x)=f(x+t) \quad(t \in \mathbb{R}, x \in \mathbb{R})$ defines an isometric group on $E$. Its generator $A$ is given by $A f=f^{\prime}$ with $D(A)=\left\{f \in C^{l}(\mathbb{R}) \quad r: C_{O}(\mathbb{R}): f^{\prime} \in C_{0}(\mathbb{R})\right\}$ in the case $E=C_{0}(\mathbb{R})$ and $D(A)=\left\{f \in E \cap A C(\mathbb{R}): f^{\prime} \in \mathbb{E}\right\}$ in the case $E=L^{P}$ (see $A-I, 2,4$ ). Thus $A^{2}$ generates a bounded holomorphic semigroup by Cor.l.13.
b) Let $E=C_{o}\left(\mathbb{R}^{n}\right)$ or $L^{P}\left(R^{n}\right) \quad(1 \leqq p<\infty)$.

For $i \in\{1, \ldots, n\}$ denote by $\left(\mathrm{J}_{\mathrm{i}}(\mathrm{t}) \mathrm{I}_{\mathrm{t} \in \mathrm{ir}}\right.$ the group given by
$\left(U_{i}(t) f\right)(x)=f\left(x_{1}, \ldots, x_{i-1}, x_{i}+t, \ldots, x_{n}\right) \quad\left(x \in \mathbb{R}^{n}, t \in \mathbb{R}\right)$ and $b y A_{i}$ its generator. Since $\square_{i}(t) \rrbracket_{j}(s)=\square_{j}(s) U_{i}(t) \quad(s, t \in \mathbb{R}, i, j \in(1, \ldots, n))$ it follows that the resolvents of $A_{i}$ commute. So the same is true for the resolvents of $A_{i}{ }^{2}$ (cf. (1.7) and A-I, 3.8).
Denote by $\left(T_{i}(t)\right)_{t \geq 0}$ the semigroup generated by $A_{i}{ }^{2} \quad(i=1, \ldots, n)$. Then for $z, z^{\prime} \in S(\pi / 2)$ one has $T_{i}(z) T_{j}\left(z^{\prime}\right) \Rightarrow T_{j}\left(z^{\prime}\right) T_{i}(z)$ $(i, j=1, \ldots, n)$. Consequently, $T(t):=T_{1}(t) \circ \ldots \circ T_{n}(t) \quad(t \geq 0)$ defines a holomorphic semigroup of angle $\pi / 2$. According to $A-I, 3.8$ the domain of its generator $A$ contains $D\left(A_{1}{ }^{2}\right) ~ C i . . r: D\left(A_{n}{ }^{2}\right)$; in particular $D_{0}=\left\{f \in E \quad r: C^{2}\left(\mathbb{R}^{n}\right) ; D^{\alpha} f \in E\right.$ for every multiindex a with $|a| \leq 2\} \subset D(A)$ and the generator is given by
$A f=\left(A_{1}^{2}+\ldots+A_{n}^{2}\right) f=\sum_{i=1}^{n} \frac{\partial^{2}}{\left(\partial x_{i}\right)^{2}} f=\Delta f \quad$ for all $f \in D_{0}$.

Let $a \in(0, \pi / 2 j$. A semigroup (T(t)) $\quad$ tミ0 is called holomorphic of angle $\alpha$ if it possesces an extension $T: S(\alpha) \rightarrow L(E)$ for some $\alpha \in[0, \pi / 2]$ which satisfies all the requirements of Definition l.ll except that it is not required to be bounded on any sector $s\left(a_{1}\right)$.

Theorem 1.14. A densely defined operator $A$ is the generator of a holomorphic semigroup if and only if there exist $M>0$ and $r \geqslant 0$ such that $\lambda \in \rho(A)$ and $\| R(\lambda, A)|i M /|\lambda|$ whenever $\operatorname{Re} \lambda>0$, $|\lambda| \geq r$.

Proof. It is not difficult to show that $A$ generates a holomorphic semigroup of angle $\alpha$ if and only if for every $\alpha_{1} \in(0, a)$ there exists $w \in l$ such that $A-w$ generates a bounded holomorphic semigroup of angle $\alpha_{1}$ (cf.[Reed-Simon (1978b), p. 252]). As a consequence one obtaing the following. A densely defined operator A generates a holomorphic semigroup of angle a $\in(0, \pi / 2]$ if and only if for every $a_{1} \in[0, \alpha)$ there exist a constant $M \geq 0$ and $r \geq 0$ such that
$$
S\left(\alpha_{1}+\pi / 2\right) \backslash B(r)=\rho(A) \quad(\text { where } B(r)=\{z \in \mathbb{C}:|z| \text { 草 } r\})
$$
and
$$
\|R(\lambda, A)\| \leqslant M /|\lambda| \quad \text { for all } \quad \lambda \in S\left(a_{1}\right) \backslash B(r)
$$

This shows that the condition of the theorem is necessary. Conversely, assume that the condition holds. Since $\|R(\lambda, A)\| \infty$ when $\lambda$ approaches $\sigma(A)$ (cf. Lemma 1.21 below), it follows that $\lambda \in p(A)$ and $\|R(\lambda, A)\| \leq M /|\lambda|$ if $\operatorname{Re} \lambda=0$ and $|\lambda|>r$ as well.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-045.jpg?height=52&width=1617&top_left_y=1756&top_left_x=205) $\left\|\xi \mathrm{R}\left(\mathrm{i}_{\boldsymbol{\eta}, \mathrm{A}} \mathrm{A}\right)\right\|_{\boldsymbol{j}} \leqslant \mathrm{M} /|\eta| \leqslant \mathrm{C}, \mathrm{M}=1 / 2$.
Hence $R\left(\xi+i_{\eta}, A\right)=\sum_{n=0}^{\infty}(-\xi)^{n} R\left(i_{\Pi}, A\right)^{n+1}$ exists and
$$
\begin{aligned}
\left\|R\left(\xi+i_{\eta}, A\right)\right\| & \leqq\left(\left|\xi+i_{\eta}\right|^{-1} \cdot\left|\xi+i_{\eta}\right| \cdot \sum_{n=0}^{\infty}|\xi|^{n} M^{n+1} /|\eta|^{n+1}\right. \\
& \leqq\left(\left|\xi+i_{\eta}\right|\right)^{-1} \cdot M-\left(|\xi|^{2}+|\eta|^{2}\right)^{-1 / 2} /|n| \cdot \sum_{n=0}^{\infty} M^{n} c^{n} \\
& \leqq\left(2 M-\left(c^{2}+1\right)^{-1 / 2}\right) /\left|\xi+i_{\eta}\right| \\
& =N /\left|\xi+i_{\eta}\right| .
\end{aligned}
$$

This together with the assumption implies that there exist $\mathbb{N}^{\prime}$ a 0 and $\alpha \in(0, \pi / 2 T$ such that $\lambda \in \rho(A)$ and $\|R(\lambda, A)\| N N / \lambda \mid$ for all $h \in S(\alpha+\pi / 2)$.

Compared with the Hille-Yosida theorem, Theorem l.l4 gives a very simple criterion for an operator to be the generator of a (holomorphic) semigroup. Merely the resolvent and not its powers have to be
estimated. However, the resolvent has to be known in the right halfplane instead of a right half-line.

On the other hand, given a strongly continuous semigroup, merely an estimate on a vertical line implies that the semigroup is holomorphic. More precisely, the following holda.

Corollary. A strongly continuous semigroup with generator A is holomorphic if and only if there exist $w>\sin$ and $M \geq 0$ such that one has $\|R(w+i n, A)\| \leq M /|n|$ for $\| l l n \in \mathbb{R}$.

Proof. In fact, assume that the condition holds. Since A-w is the generator of a bounded semigroup one has $\|R(\lambda, A-w)\| N / R e \lambda$ for some $N>0$ and all $\lambda \in \mathbb{C}$ satisfying Rè $>0$. Consequently, for every $\quad \alpha \in(0, \pi / 2), \quad \|\left. R(\lambda, A-w)\right|_{1} \leqq(|\lambda| / R e \lambda) \cdot N /|\lambda| \leqq N\left(\cos ^{\alpha}\right)^{-1} /|\lambda|$ for all $\lambda \in S(\alpha)$. The remaining estimate for a sector around the imaginary axis is given by the proof of Thm.l.14 and shows that A-w generates a holomorphic semigroup. The reverse implication is clear.

We now prove the following extension of Cor.l.l3.

Theorem 1.15. Let $A$ be the generitor of a strongly continuous group. Then $A^{2}$ generates a holomorphic semigroup of angle $\pi / 2$.

Proof. There exists $w \geq 0$ such that ( $\pm A-w$ ) generates a bounded semigroup. Consequently, there exists $M \geqq 0$ such that
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-046.jpg?height=53&width=986&top_left_y=1844&top_left_x=227)
Let $\alpha \in(0, \pi / 2)$. There exist $r_{0} \leqslant 0$ and $\beta \in(0, \pi / 2)$ such that $S(\alpha+\pi / 2) \backslash B\left(r_{0}\right) \measuredangle\left\{z^{2}: z \in S(B)+w\right\}$.
[In fact, the line $\{w+r(\cos \beta+i \sin \beta)=r \geq 0\}$ can be para-
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-046.jpg?height=47&width=1617&top_left_y=2078&top_left_x=228) on B). Then $z(t)^{2}=(w+t)^{2}-t^{2} / e^{2}+i 2 t(w+t) / E$.
Thus $\lim _{t \rightarrow \infty} \operatorname{Imz}(t)^{2} / \operatorname{Rez}(t)^{2}=2 \varepsilon /\left(\varepsilon^{2}-1\right)$. Choose $\beta \in(\pi / 4, \pi / 2)$ such that $\tan (\alpha+\pi / 2)>2 \varepsilon /\left(\varepsilon^{2}-1\right) .1$
Now let $\lambda \in S(\alpha+\pi / 2) \backslash B\left(r_{0}\right)$. Then there exist $\theta \in(-B, \beta)$ and $r \geq 0$ such that $h=\left(r e^{i \theta}+w\right)^{2}$. Thus $\left(\lambda-A^{2}\right)=\left(r e^{i \theta}+w-A\right)\left(r e^{i \theta}+w-A\right)$. Hence $\lambda \in \rho\left(A^{2}\right)$ and $R\left(\lambda, A^{2}\right)=R\left(r e^{i \theta}, A-w\right) R\left(r e^{i \theta},-A-w\right)$. We conclude that $|\lambda| \cdot\left\|R\left(\lambda, A^{2}\right)\right\| \leqq|\lambda| \cdot M^{2} /(\cos \theta)^{2} r^{2} \leqq\left(|\lambda| / r^{2}\right) \cdot M^{2} /(\cos \beta)^{2}$. Thus $|\lambda| \cdot R\left(\lambda, A^{2}\right)$ is uniformly bounded for $\lambda \in S(a+\pi / 2)=B\left(r_{0}\right)$.

Remark. In Theorem 1.15 the assumption that $\pm A$ are generators can be relaxed. In fact, the proof shows the following. If $A$ is a dencely defined operator such that $\{\lambda \in C \quad \operatorname{Re} \lambda>0\} \subset \rho( \pm A-w)$ and $\|R(\lambda, \pm A-w)\| \leq M / R e \lambda$ for some $M \geqq 0$, w $\geqslant 0$, then $A^{2}$ generates a holomorphic semigroup of angle $\pi / 2$.

Next we consider semigroups satisfying a less restrictive smoothness condition.

\section*{Differentiable semigroups}

Let $(T(t))_{t \geq 0}$ be a strongly continuous semigroup with generator A. Let $t_{o} \geqq 0$ and $f \in E$. Then the function $t \rightarrow T(t) f$ is right sided differentiable in $t_{o}$ if and only if $T\left(t_{o}\right) f \in D(A)$; and in that case it is differentiable in every $s>t_{o}$ and the derivative is AT (s)f (this followg from A-I, Prop. 1.6(ii)).

Definition 1.16 . A strongly continuous semigroup ( $T(t)$ ) t¥o on a Banach space $E$ is called eventually differentiable if there exists $t_{0} \geqq 0$ such that the function $t \rightarrow T(t) f$ from ( $\left.t_{0}, \infty\right)$ into $E$ is differentiable for every $f \in E$. The semigroup is called differentiable if $t_{o}$ can be chosen 0 .

It is not difficult to see that if (T(t)) $t \geqq 0$ is differentiable for $t>t_{o}$, then it is n-times differentiable in all $s>n t_{o}$ and $T(s) E \subset D\left(A^{n}\right) \quad(n \in \mathbb{N})$. $I f \quad(T(t))_{t \geq 0} \quad i s$ differentiable, then the function $t \rightarrow T(t) f$ from $(0, \infty)$ into $E$ is infinitely often differentiable for every $f \in E$.

Generators of (eventually) differentiable semigroups can be characterized similarly as those of holomorphic semigroups by the spectral behavior of the resolvent. Whereas the spectrum of the generator of a holomorphic semigroup is included in a sector, the spectrum of the generator of an eventually differentiable semigroup is limited by a function of exponential growth (instead of a line).

Theorem l.17. A strongly continuous semigroup (T(t)) t¥0 is eventually differentiable if and only if its generator $A$ satisfies the following; there exist constants $c>0, b>0$, M>0 such that
$$
\Sigma:=\left\{\lambda \in \varepsilon ; c e^{-b \cdot \operatorname{Re} \lambda} \leqq\left|I_{\operatorname{m} \lambda}\right|\right\rangle \subset \rho(A)
$$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-048.jpg?height=52&width=1518&top_left_y=542&top_left_x=229)

Theorem 1.18. A strongly continuous semigroup (T (t)) $t \geq 0$ is differentiable if and only if its generator $A$ satisfies the following: for all b>0 there exist $c>0, M_{>0}$ such that
$$
\Sigma:=\left\{\lambda \in \subset: c e^{-b \cdot \operatorname{Re} \lambda} \cong|\operatorname{Im} \lambda|\right\} \subset \rho(A)
$$
and $\|R(\lambda, A)\| \leqq M .|\operatorname{Im} \lambda|$ for all $\lambda \in \Sigma$ satisfying Re $\lambda \leqslant \omega(A)$.

For the proofs of these two theorems we refer to [Pazy (1983), Chap. 3, Theorem 4.7 and 4.8.).

Norm continuous semigroups

Let $(T(t))_{t \geqslant 0}$ be a strongly continuous semigroup and $t^{\prime}>0$. If $l^{\prime} m_{t+t^{\prime}}\left\|T(t)-T\left(t^{\prime}\right)\right\|=0$, then $i t$ follows from the semigroup property, that the function $t \rightarrow T(t)$ is norm continuous on the whole half line ( $\left.t^{\prime}, \infty\right)$.

Definition 1.19. A semigroup (T(t)) $\mathrm{t} \geqslant \mathrm{o}$ (s called eventually norm continuous if there exists $t^{\prime} \geqq 0$ such that the function $t \rightarrow T(t)$ from ( $t^{\prime},{ }^{*}$ ) into $L(E)$ is norm continuous. The semigroup is called norm continuous if $t^{\prime}$ can be chosen equal to 0 .

The spectrum of generators of eventually norm continuous semigroups still is compact in every right half-plane.

Theorem 1.20. Let $A$ be the generator of an eventually norm continuous semigroup. Then for every $b \in \mathbb{R}$ the get
$[\lambda \in \sigma(A): \operatorname{Re} \lambda \geq b\}$
is bounded.

For the proof of Theorem 1.20 we use the following lemma.
Lemma 1.21. Let $A$ be an operator and $\lambda \in \rho(A)$. Then
$$
\operatorname{dist}(\lambda, \sigma(A))=r(R(\lambda, A))^{-1}
$$

Proof. One has $\{0\rangle \cup \sigma(R(\lambda, A))=\{0\} \cup\left\{(\lambda-\mu)^{-1} ; \mu \in \sigma(A)\right\}$ [Davies (1980), Lemma 2.11. . Hence $r(R(\lambda, A))=\sup \left\{|\lambda-\mu|^{-1}:\{\in \sigma(A)\}=\right.$ $[\inf \{|\lambda-\mu|: \mu \in \sigma(A)\}\}^{-1}=\operatorname{dist}(\lambda, \sigma(A))^{-1}$.

Propf of Thar. 20. It is enough to show the following. Let a $>\mathrm{w}(\mathrm{A})$. Then for every $\leqslant>0$ there exist $n \in \mathbb{N}$ and $r_{o} \mathbb{Z} 0$ such that $\left\|\mathrm{R}(\mathrm{a}+\mathrm{ir}, \mathrm{A})^{\mathrm{n}}\right\|^{1 / \mathrm{n}}<\varepsilon$ for all $r \in \mathbb{R}$ satisfying $|r|{ }^{\circ} \mathrm{r}_{\mathrm{o}}$.
[In fact, then we have by the lemma,
$\operatorname{dist}(a+i r, o(A))=r(R(a+i r, A))^{-1} \geq\left\|R(a+i r, A)^{n}\right\|^{-1 / n}>1 / \varepsilon \quad$ whenever $|r| \geq r_{0}{ }^{\text {I }}$.
So let $\varepsilon>0$. If $\operatorname{Re} \lambda>\omega(A)$, then by $A-I$, Prop.l.11,
$R(\lambda, A)^{n+1}=1 / n!\int_{0}^{m} e^{-\lambda t_{t} n^{n} T(t) d t} \quad(n \in W)$. Let $t^{\prime \prime}>0$ such that $t \rightarrow T(t)$ is norm continuous on $\left[t^{\prime}, \infty\right)$. Let $w \in(\omega(A)$, a). There exists $M \geq 1$ such that $\|T(t)\| \leq M e^{w t}$ for all $t a 0$. Let $\mathbb{N}:=M \cdot \int_{0}^{t^{\prime}} e^{-a t_{e} w t} d t$. Since $\lim _{n \rightarrow \infty} c^{n} / n!=0 \quad$ for $a l l$ $c=0$, there exists $n \in \mathbb{N}$ such that $N \cdot\left(t^{n}\right)^{n} / n!<\varepsilon^{n+1} / 3$. Choose $T \geqq t^{\prime}$ such that $1 / n!\cdot \int_{T}^{\infty} t^{n} e^{-a t}\|T(t)\| d t < E^{n+1} / 3$.
Since ( $T(t)$ ) t 0 is norm continuous for $t \geqslant t$, it follows from the Riemann-Lebesgue lemma that there exists $r_{0} \geq 0$ such that $\left\|1 / n!\cdot \int_{t^{1}}^{T} t^{n} e^{-i r t_{e}} e^{-a t^{\prime}}(t) d t\right\|<\varepsilon^{n+l} / 3$ whenever $\quad r \mid \geqq r_{0}$
All together we obtain for $|r| \geqslant r_{O_{0}}$ $\left\|\mathrm{R}(\mathrm{a}+\mathrm{ir}, A)^{n+1}\right\|=1 / n t \cdot \| \int_{0}^{\infty} e^{-(a+i r) t_{t}{ }^{n} T(t) d t \|}$
$$
\begin{aligned}
& \leqq 1 / n t \cdot \int_{O}^{t^{\prime}} e^{-a t} t^{n}\|T(t)\| d t \\
& +1 / n!\cdot \int_{1}^{T} \int^{T} t^{n} e^{-i r t} e^{-a t} T(t) d t \beta \\
& +1 / n!\cdot \int_{T}^{\infty} e^{-a t} t^{n}\|T(t)\| d t \\
& \leqq 1 / n!\cdot\left(t^{\prime}\right)^{n} \int_{O}^{t^{\prime}} e^{-a t} M e^{w t} d t+2 / 3 \cdot E^{n+1} \\
& \leqq N \cdot\left(t^{\prime}\right)^{n / n} /+2 / 3 \cdot e^{n+1} \leqq \varepsilon^{n+1} .
\end{aligned}
$$

A complete characterization of eventually norm continuous semigroups in terms of their generator seems not to be known.
Eventually norm continuous semigroups are of particular interest in spectral theory (cf. A-III, Thm. 6.6 ). Moreover their asymptotic behavior is easy to describe (see A-IV, (1.8)).

Next we describe special norm continuous semigroups.

Compact semigroups

Let $(T(t))_{t \geq 0}$ be a strongly continuous semigroup and $t_{0}>0$. If $T\left(t_{0}\right)$ is compact, then it follows from the semigroup property that $T(t)$ is compact for all $t \geq t_{0}$. Moreover, $t \rightarrow T(t)$ is norm continuous in every $t>t_{0}$
[In fact, since $T(h) \rightarrow$ Id strongly with $h+0$, it follows that $\lim _{h+0} T(h) f=f$ uniformly on every compact subset $K$ of $E$. Now let $t \geqq t_{0}$. Then $K=T \bar{T} \bar{U}$ is compact where $u$ denotes the unit ball of $E$ ). Hence $l_{i m} h^{\prime} \neq T(h+t) f=\lim _{h \neq 0} T(h) T(t) f$ uniformly for $f \in \mathbb{J}$. So the semigroup is right-sided norm continuous on [to*) and so norm continuous on $\left(t_{0}, \infty\right)$.

Definition 1.22 . A strongly continuous semigroup (T(t)) $t \geq 0$ is called compact if $T(t)$ is compact for all $t>0$; the semigroup is called eventually compact if there exists $t_{o}>0$ such that $T\left(t_{0}\right)$ is compact (and hence $T(t)$ is compact for all $t \geqslant t_{0}$ ).

We want to find a relation between the compactness of the semigroup and the compactness of the resolvent of its generator.

Definition 1.23. Let $A$ be an operator and $p(A) \neq \emptyset$. We say, $A$ has a compact resolvent if $R(A, A)$ is compact for one (and hence all) $\lambda \in \rho(A)$.

Proposition 1.24 . Let (T(t)) tき0 be a strongly continuous semigroup and assume that its generator has a compact resolvent. If $t \rightarrow T(t)$ is norm continuous in $t_{0}$, then $T(t)$ is compact for all $t \geqq t_{0}$.

Proof. Considering $\left(e^{-w t} T(t)\right)$ tzo for some $w>0$ if necessary, we can assume that $s(A)<0$. Let $S(t) \epsilon L(E)$ be given by $S(t) f=\int_{0}^{t} T(s) f d s(t \geq 0)$. Then $A S(t) f=T(t) f-f$ for all $f \in E$, and so $S(t)=R(0, A)(I d-T(t))$ is compact for all $t \geqslant 0$. since $t \rightarrow T(t)$ is norm continuous for $t \geqq t_{o}$, one has $\lim _{h \downarrow 0} \frac{1}{h}\left(S\left(t_{o}+h\right)-S\left(t_{0}\right)\right)=T\left(t_{o}\right)$ in the operator norm. Thus $T\left(t_{o}\right)$ is compact as limit of compact operators.

Theorem 1.25. A strongly continuous semigroup (T(t)) tı0 is compact if and only if it is norm continuous and its generator $A$ has compact resolvent.

Proof. Assume that (T(t)) $t \geq 0$ is compact. Then $T(-)$ is norm continuous on ( $0, \infty$, and so $\int_{0}^{t} e^{-w s} T(s) d s$ is compact as the norn limit of linear combinations of compact operators, where $w>w(A)$.
Since $R(w, A)=1 i m t \rightarrow \infty \quad \int_{0}^{t} e^{-w s} T(s) d s$ in the operator norm, it follows that $R(w, A)$ is compact. This proves one implication. The other follows from Proposition 1.24.

Remark 1.26.a) Generatorg of eventually compact semigroups do not necessarily have compact resolvent. Consider the nilpotent translation semigroup ( $T(t))_{t \geqslant 0}$ on $F:=L^{1}[0,1]$ (see $A-I, E x .2 .6$ ). Let $E=F{ }_{0} F=L^{1}([0,1] \times[0,1.7)$ and $S(t)=T(t)$ oId (tצ0). Then (S (t)) tz0 is a strongly continuous semigroup (see A-I, 3.7). Denote by $B$ its generator. $(S(t))$ t30 is a nilpotent semigroup (so it is eventually compact), but $R(\lambda, B)=R(\lambda, A)$ Id is not compact.
b) It is obvious that a group (T(t)) $t \in \mathbb{R}$ is eventually norm continuous if and only if it is norm continuous in 0 ; i.e., its generator is bounded.
On the other hand, the generator of the rotation group ( $A-I, E x, 2,5$ ) has a compact resolvent. Hence this condition does not imply any smoothness property of the semigroup.

Positive eventually compact semigroups have remarkable properties in the setting of the Perron-Frobenius theory (see e.g., B-III, Cor. 2.12).

The following scheme indicates the relation between the different classes of semigroups defined so far.
```
holomorphic * differentiable * eventually differentiable
\begin{tabular}{ccc}
$\psi$ & & $\downarrow$ \\
norm continuous & $\rightarrow$ & eventually norm continuous \\
$\dagger$ & $\rightarrow$ & + \\
compact & $\rightarrow$ & eventually compact
\end{tabular}
```

All these classes are different. This is shown by the following examples.

Example 1.27. The nilpotent shift semigroup (A-I.2.6) is obviously eventually differentiable, eventually compact and eventually norm continuous. But it is not norm continuous and consequently not differentiable or compact.

Fxample 1.28. We consider multiplication semigroups (see A-I,2.3). Let $E=C_{0}(X)$, where $X$ is a locally compact space, or $E=L^{P}(x, \Sigma, \mu)$, where $1 \leq p<\infty$ and $(x, \Sigma, \mu)$ is a $\sigma$-finite measure space. Let $m: X \rightarrow \mathbb{R}$ be continuous [resp. measurable] such that $[\operatorname{egs}]-\sup _{x \in X} \operatorname{Re}(m(x))<\infty$.
Then $A f=m+f$ with domain $D(A)=\{f \in E: m+f \in E\}$ is the generator of the semigroup $(T(t))$ tzo given by $\quad(T(t) f)(x)=e^{t m(x)} f(x)$ ( $t \geq 0, x \in X, f \in E)$. Observe that $\sigma(A)=\overline{m(X)}$ in case $E=C_{0}(X)$ and $\sigma(A)=[\operatorname{ess}]$-image $(m):=\{\lambda \in \mathbb{C}: \mu(\{x \in X:|m(x)-\lambda|<\varepsilon\}) \neq 0$ for all $\varepsilon>0$ ) if $E=L^{P}$ (see A-II,2.3). Consequently. $s(A)=w(A)=[e s s]-\sup _{x \in X} \operatorname{Re}(m(x))$.
a) The semigroup is norm continuous for $t>0$ if and only if it is eventually norm continuous if and only if $[\lambda \in \sigma(A):$ Re $\lambda \geqq b\}$ is bounded for every $b \in \mathbb{R}$. Thus the property proved in Theorem 1.20 characterizes generators of eventually norm continuous semigroups in the case that the semigroup consists of multiplication operators.

Proof. Ascume that $\{\lambda \in o(A): \operatorname{Re} \lambda \geqslant b\}$ is bounded for every $b \in \mathbb{R}$. Let $t \gg 0$. We show that the semigroup is norm continuous in $t^{\prime}$. Let $E>0$. Let $b \in \mathbb{F}$ such that $2 e^{\left(t^{\prime}+l\right) b}<\varepsilon$. If $\operatorname{Re}(m(x)) \leqq b_{r}$ then $\left|e^{\operatorname{tm}(x)}-e^{t \cdot m(x)}\right| \leq e^{t \cdot \operatorname{Re}(m(x))}+e^{t^{\prime} \cdot \operatorname{Re}(m(x))} \leqslant 2 e^{\left(t^{\prime}+1\right) b}<E$ Whenever $\left|t-t^{\prime}\right| \leq 1$.
By hypothesis, the set $H:=\{m(x): x \in X, \operatorname{Re}(m(x)) \geqq b\}$ in the case $E=C_{Q}(X)$ and $H:=\{m(x): R e \lambda \geqq b$ and for all $n>0$ $\mu(f x \in X:|m(x)-\lambda|<\eta\}) \neq 0)$ in the case $E=L^{P}(X, \Sigma, \mu)$ is a bounded subset of C .
Thus $\lim _{t \rightarrow t}\left|e^{t z}-e^{t^{\prime} z}\right|=0 \quad$ uniformly for $z \in H$. Hence there exists $\delta \in(0,1]$ such that
[ess]-sup $\left\{\left|e^{\operatorname{tm}(x)}-e^{t \cdot m(x)}\right|: x \in X, \operatorname{Re}(m(x))>b\right\}<\varepsilon \quad$ whenever $\left|t-t^{\prime}\right|<$ s. Together with the inequality above, we obtain that $\| T(t)$ $-\left.T\left(t^{\prime}\right)\right|_{j}=[\operatorname{ess}]-\sup \left\{\left|e^{t m(x)}-e^{t ' m(x)}\right|: x \in X\right\} \in E \quad$ whenever $\left|t-t^{\prime}\right|<\delta$. We have shown that the semigroup is norm continuous for $t>0$ whenever $\{\lambda \in o(A): \operatorname{Re\lambda } 2 b\}$ is bounded for all $b \in \mathbb{R}$.
b) The semigroup is right-sided differentiable in a fixed point $t>0$ if and only if there exists $c>0$ such that $\{\lambda \in \mathbb{E}$; $|\operatorname{Im\lambda }|>c \cdot e^{-t \operatorname{Re\lambda }} \mid=p(A)$.

Proof. The semigroup is right-sided differentiable in $t$ if and only if $T(t) E=D(A)$ if and only if $e^{t m} . f \cdot m \in E$ for $a l l f \in E \quad$ if and only if $e^{\text {tm }} \cdot m$ is [essentially] bounded if and only if $e^{\text {tRe } m}$. Im m is [essentially bounded if and only if there exists $c>0$ such that [ess]-image (m) $=\left\{\lambda \in \mathbb{C}: e^{t \operatorname{Re\lambda }}|\operatorname{Im\lambda }| \leq c\right\}$ if and only if there exists $c>0$ such that $\left\{\lambda \in \mathbb{C}:|\operatorname{Im} \lambda|>c \cdot e^{-t R e h}\right\} c \rho(A)$.
c) (T(t) $t_{20}$ is a bounded holomorphic semigroup of angle $\theta$ if and only if $S(\theta+\pi / 2) E \rho(A)$.

Proof. The condition is necessary by Theorem 1.12.
Conversely, if $S(\theta+\pi / 2)=\rho(A)$, then one verifies directly that $(T(z) f)(x)=e^{z \cdot m(x)} f(x) \quad(f \in E, x \in X)$ defines a family (T(z))$z \in S(\theta)$ of bounded operators satisfying conditions (1.4) and (1.5).
d) Choosing $X=N$ and $\mu$ the counting measure we have $E=C_{o}$ or $\ell^{\mathrm{P}}(1 \leqslant p<\infty)$. Then A has a compact resolvent if lim $_{n+\infty}|m(n)|=$. [In fact, let $\lambda>s(A)$. Then $(R(\lambda, A) f)(n)=(\lambda-m(n))^{-1} f(n)$. Hence $R(\lambda, A)$ is compact if and only if $\left(\lambda-(m(n))^{-l}\right) \quad n \in \mathbb{N} \in C_{0} \cdot 3$
The semigroup is compact if and only if it is eventually compact if and only if $\lim _{n \rightarrow \infty} \operatorname{Re}(m(n))=-\infty$.
e) Now it is easy to give concrete examples. Again let $X=\mathbb{N}$, so that $E=C_{o}$ or $\ell p(1 \leq p<\infty)$. Let $m(n)=-n+i \cdot \exp \left(n^{2}\right)$. Then the semigroup is compact and (consequently) norm continuous for $t>0$, but it is not eventually differentiable. Let $m(n)=-n+i e^{t} n$. Then the semigroup is differentiable for $t>t^{\prime}$ but not differentiable in $t \in\left[0, t^{\prime}\right]$. If $m(n)=-n+i \cdot n^{2}$, then the semigroup is differentiable but not holomorphic.

\section*{Perturbation of Generators}

A useful way to construct new semigroups out of a given one is by additive perturbation.

Theorem 1.29. Let $A$ be the generator of a strongly continuous semigroup (T(t)) tzo and let $B \in L(E)$. Then $A+B$ with domain $D(A+B)=D(A)$ is the generator of a strongly continuous semigroup $(S(t))_{t \geqslant 0^{*}}$

It is possible to express the new semigroup $(S(t))_{t \geq 0}$ by known objects. The product formula
(1.8) $S(t) f=\lim _{n \rightarrow \infty}\left(T(t / n) e^{t / n \cdot B}\right)_{f}^{n_{f}}$
holds for all $t \geqslant 0$ and $f \in E$.
Moreover, $S(t)$ is the solution of the following integral equation (1.9) $S(t) f=T(t) f+\int_{0}^{t} T(t-s) B S(s) f d s \quad(t \geqq 0, f \in E)$.

Let $S_{o}(t)=T(t)$ and
(1.10) $\quad S_{n}(t) f=\int_{o}^{t} T(t-s) B S_{n-1}(s) f d s \quad(f \in E)$ for $n \in \mathbb{N}$. Then
(1,11) $\quad s(t)=\sum_{n=0}^{\infty} \quad S_{n}(t)$,
where the series converges in the operator norm uniformly on bounded intervals. We refer to [Davies (1980), III.1.], [Goldstein (1985a), I. 6 ] or [Pazy (1983), Chap. 3] for these results.

Several special properties discussed above are preserved by bounded perturbations.

Theorem 1.30. Let (T (t) $t \geq 0$ be a strongly continuous semigroup with generator $A$. Let $B \in L(E)$. If $(T(t)){ }_{t} \geq 0$ is holomorphic or norm continuous or compact, then so is the semigroup (s(t)) $\mathrm{t}_{\mathrm{o}}$ generated by $A+B$.

If $A$ has a compact resolvent then 50 has $A+B$.
Let $t_{0} \geqq 0$. If $(T(t))_{t \geqslant 0}$ is norm continuous for $t>t_{0}$ and if $B$ is compact, then $(S(t)){ }_{t \geq 0}$ is also norm continuous for $t>t_{o}$.

Proof. If (T(t)) $t_{0}$ is norm continuous for $t>0$, then $S_{n}(t)$ in (1.10) is norm continuous in $t>0$ for every n. Thus ( $s$ ( $t$ ) $t \geq 0$ is norm continuous in $t \geqslant 0$ by (l.11). There exists $\lambda_{0} \in \mathbb{R}$ such that $\|R(\lambda, A)\|\left(2\|B\|^{-1} \text { for Re } 2 \lambda_{0} \text {. Hence (Id - BR }(\lambda, A)\right)^{-1}$ exists for Reh $\leqslant \lambda_{0}$. Since $(\lambda-(A+B)) f=(\operatorname{Id}-B R(\lambda, A))(A-A) f$ for all $f \in D(A)$ it follows that $(A-(A+B))^{-1}$ exists and is given by
(1.12) $\quad R(\lambda, A+B)=R(\lambda, A)(I d-B R(\lambda, A))^{-1}$
whenever Reג $\geqq \lambda_{0}{ }^{*}$ Now if $A$ generates a holomorphic semigroup,
there exists $M \geqq 0$ such that $\left\|R\left(\lambda_{0}+i \eta, A\right)\right\| \leqq M /|\eta|$ for all $\| \in \mathbb{R}$. Conseguently, $\quad\left\|R\left(\lambda_{o}+i n, A+B\right)\right\| \|\left(I d-B R\left(\lambda_{o}+i n, A\right){ }^{-1} \|-M /|\eta| x 2 M /|\eta|\right.$ for all $n \in \mathbb{R}$. Thus $A+B$ generates a holomorphic semigroup by the corollary of Thm.l.14. Moreover, it follows from (1.12) that $R(\lambda, A+B)$ is compact whenever $R(\lambda, A)$ is compact. Consequently by Theorem 1.25 and the assertion proved above, (s (t)) ${ }_{t \geqslant 0}$ is compact whenever (T(t)) $t \geq 0$ is compact.
Finally assume that $B$ is compact and $t_{0} \geqq 0$ such that ( $T(t){ }_{t} \geqslant 0$ is norm continuous for $t>t_{o}$. Fix $t>t_{o}$. Denote by $u$ the unit ball of $E$ and fix $s \in(0, t]$. Then $\lim _{h \rightarrow 0}(T(t+s-h)-T(t-s)) f=0$ for all $f \in \bar{B} \bar{S}(\bar{s}) \bar{U}=: K$.
since $K$ is compact it follows that the limit exists uniformly in £ $\in K$; i.e. $\quad \lim _{h \rightarrow 0}\|(T(t+s-h)-T(t-s)) B S(s)\|=0$. It follows from the dominated convergence theorem that
(1.13) $\quad 1 i m_{h \rightarrow 0} \int_{0}^{t}\|(T(t+s-h)-T(t-s)) B S(s)\| d s=0$.

Using (1.9) we obtain $\|S(t+h)-S(t)\|$
$\leqslant\|T(t+h)-T(t)\|+\left\|\int_{0}^{t+h} T(t+h-s) B S(s) d s-\int_{0}^{t} T(t-s) B S(s) d s\right\|^{2}$
$\leq\|T(t+h)-T(t)\|+\left\|\int_{t}^{t+h} T(t+h-s) B S(s) d s\right\|$
$$
+\int_{0}^{t}\|(T(t+h-s)-T(t-s)) B S(s)\| d s+0 \text { when } h * 0
$$

In C-IV, Ex.2.15 a generator $A$ of an eventually differentiable and eventually compact semigroup and a bounded operator $B$ will be given such that the semigroup generated by $A+B$ is not eventually norm continuous.

Using Theorem 1.29 we now prove a perturbation result due to DeschSchappacher (1984). Instead of assuming that $B \in L(E)$ we assume that $B \in L(D(A))$. The short proof given below is due to G.Greiner.

Theorem 1.31. Let (T(t)) $2 \geq 0$ be a strongly continuous semigroup with generator $A$. Assume that $B: D(A) \rightarrow D(A)$ is linear and continuous For the graph norm on $D(A)$.
Then $A+B$ with domain $D(A+B)=D(A)$ is the generator of a strongly continuous semigroup. Moreover, there exists a bounded operator $C$ on $E$ such that $A+B$ is similar to $A+C$.

Proof. We first show that (Id - BR(h, A)) is invertible for some $\lambda$ $\epsilon$ C. Choose $\lambda_{0} \in \rho(A)$. Then $S:=\left(\lambda_{0}-A\right) B R\left(\lambda_{0}, A\right) \in L(E)$. Let $\lambda>$ $s(A)$ be so large such that $\|S R(\lambda, A)\|<1$.

Then $\left(1-\left(\lambda_{0}^{-A) R R}\left(\lambda_{0}, A\right) R(\lambda, A)\right)\right)^{-1}=(1-\operatorname{SR}(\lambda, A))$ is invertible. Consequently, also $(1-B R(\lambda, A))^{-1}$ exists (since $\sigma\left(T R\left(\lambda_{0}, A\right)\right)$ ( 0 ) $=$ $\left.\sigma\left(R\left(\lambda_{0}, A\right) T\right) \quad[0\}, T=\left(\lambda_{0}-A\right) B R(\lambda, A)\right)$.
Let $C=(A-\lambda) B(A-\lambda)^{-1} E L(E)$. Then $A+C$ is the generator of a strongly continuous semigroup by Theorem 1.29 . We show that $A+B$ is similar to $A+C$. In fact, let $U=(1-B R(\lambda, A))$. Then $U$ is an isomorphism on $E$ such that $\square(D(A))=D(A)$.
Moreover, $U(A+C) U^{-1}=U(A-\lambda+C) U^{-1}+\lambda=U\left[(A-\lambda-(A-\lambda) B R(\lambda, A)] U^{-1}+\lambda\right.$ $=U(A-\lambda)[1-B R(\lambda, A)] U^{-1}+\lambda=U(A-\lambda)+\lambda=A-\lambda+B+\lambda=A+B$.

Corollary 1.32. Keeping the hypotheses and notations of Theorem 1.31 denote by $(S(t))_{t \geq 0}$ the semigroup generated by $A+B$. If ( $\left.T(t)\right)_{t \geq 0}$ is norm continuous or compact or holomorphic, then (s(t)) $t \geq 0$ has the corresponding properties. If $B$ is compact as an operator on $D(A)$ endowed with the graph norm and if (T(t)) tep is eventually norm continuous then so is $(S(t))$ t?0"

Proof. This follows from Theorem 1.30 since (US (t) $U^{-1}$ ) tzo has A+C as generator.

\section*{Domains of Uniqueners}

Given a semigroup (T(t)) tzo frequently it is frequently difficult to determine the precise domain of its generator $A$. So it is important to know which (possibly strict) subspaces of $D(A)$ determine the semigroup uniquely. This can be formulated more precisely in the following way. Let $D_{0}$ be a subspace of $D(A)$ and consider the restriction $A_{o}$ of $A$ to $D_{o}$ Under which condition on $D_{o}$ is $A$ the only extension of $A_{o}$ which is a generator? one obvious condition is that $D_{o}$ is a core. [In fact, in that case, $A$ is the closure of $A_{o}$. Since every generator $B$ extending $A_{o}$ is closed, it follows that $A \subset B$ and hence $A=B$ since $P(A) \cap(B) \neq 07$.

We now show that cores are the only domains of uniqueness.

Theorem 1.33. Let $A$ be the generator of a semigroup and $D_{o} a$ subspace of $D(A)$. Consider the restriction $A$ of $A$ to $D_{0}$. If $D_{o}$ is not a core of $A$, then there exists an infinite number of extensions of $A_{o}$ which are generators.

Proof. If $D$ f $f$ not dense in $D(A)$ with respect to the graph norm, then there exigts a non-zero linear form $\phi$ on $D(A)$ which is continuous for the graph norm such that $\phi(f)=0$ for all $f \in D_{o}$. Let $u \in D(A)$ and $B: D(A)+D(A)$ be given by $B f=\phi(f) u$ for all $f \in D(A)$. Then $B$ is continuous for the graph norm. So by Theorem 1.31 the operator $A+B$ with domain $D(A)$ is a generator. Clearly, $A+B \neq A$ if $u \neq 0$ but $A f+B f=A f$ for all $f \in D_{0}$. It is obvious that an infinite number of generators can be constructed in that way.

Corollary 1.34 . Let ( $T(t))_{t \geqslant 0}$ be a strongly continuous semigroup with generator $A$. Let $D_{o}$ be a dense subspace of E. Assume that $D_{0} \subset D(A)$ and $T(t) D_{0} \in D_{0}$ for all $t \geqslant 0$. Then $D_{o}$ is a core.

Proof. Let $(S(t)) t \geq 0$ be a semigroup with generator $B$ such that ${ }^{B}\left\|_{D O}={ }^{A}\right\|_{D_{0}}$ Let $f \in D_{o}$. Then $u(t):=T(t) f$ satigfies $u(0)=f$ and $\quad \dot{u}(t)=A T(t) f=B T(t) f=B u(t) \quad(t \geq 0)$. Since $\quad v(t)=s(t) f$ (tzo) also is a solution of the Cauchy problem defined by $B$ with initial value $f$ it follows that $s(t) f=T(t) f(t \geq 0)$. Since $D_{0}$ is dense in $E$, it follows that $S(t)=T(t)(t \geq 0)$.

\section*{2. CONTRACTION SEMIGROUPS AND DISSIPATIVE OPERATORS}
by
Wolfgang Arendt

The Hille-Yosida theorem gives a characterization of generatorg in terms of the resolvent of the operator. However, given an operator $A$, frequently it is difficult to compute the resolvent (and its powers). So it is desirable to find conditions more immanent on $A$. This is possible for generators of contraction semigroups. For later purposes (see B-II and C-II) it will be useful not only to consider semigroups which are contractive with respect to the norm but to consider more general sublinear functionals than the norm as well.
So our setting is the following. By $E$ we denote a real Banach space throughout, and $p=E \rightarrow \mathbb{R}$ is a continuous sublinear function; i.e., $p$ satisfies
\begin{tabular}{ll} 
(2.1) & $p(f+g) \leqq p(f)+p(g)$ \\
$(2.2)$ & $p(\lambda f)=\lambda p(f)$
\end{tabular}$\quad(f \in g \in E)$.

The continuity of $p$ implies that there exists a constant $c>0$ such that
```
(2.3) |p(f)| sc|f|
(f\inE).
```

Moreover, it follows from (2.1) and (2.2) that
```
(2.4) p(f) + p(-f) 彐p(0)=0 (f GE).
```

A bounded operator $T$ on $E$ is called p-contractive if $p(T f) \leqq$ $p(f)$ for all $f \in E$. Similarly, a semigroup $(T(t)){ }_{t} \geq 0$ is called p-contractive if $T(t)$ is $p$-contractive for all $t \geqq 0$. Of course, the most important case we have in mind in this section is the case when $P$ is the norm function $N$ given by $N(f)=\|f\|$ ( $f \in E$ ). An $N$-contractive operator is just a contraction in the usual gense.

Remark. However in Chapter B-II and C-II it will be important to dispose of a variety of sublinear functionals other than $\mathbb{N}$. For example, we will consider $\mathbb{N}^{+}$on $C[0,1]$ given by $\mathbb{N}^{+}(f)=$ $\sup _{x \in[0,1]} f(x)$. Then a bounded operator $T$ is $N^{+}$-contractive if and only if $T$ is positive and $\|T\| \leq 1$.

We first want to solve the following problem. Given the generator A of a semigroup (T(t)) ${ }_{t \geq 0}$ find a condition on $A$ which is equivalent to $T(t)$ being p-contractive for all $t z 0$.

The subdifferential $d p$ of $p$ in $f$ is defined by
(2.5) $d p(f)=\left\{\phi \in E^{\prime}:\langle g, \phi\rangle <  p(g) \right.$ for all $g \in E$,
$$
\langle f, \phi\rangle=p(f)\} .
$$

It follows from the Hahn-Banach theorem that dp(f) $\neq \emptyset$ for all $f \in E$.

Definition 2.1. An operator $A$ on $E$ is called p-dissipative if for all f $f D(A)$ there exists $\phi \in d p(f)$ such that $\langle A f, \phi\rangle \leqq 0$; A is called strictly p-dissipative if for all $f \in D(A)$ the inequality $\langle A f, \phi\rangle \leqq 0$ holds for all $\phi \leqslant d p(f)$.

For convenience we want to have a distinctive name for the norm function. So we denote by $\mathbb{N}: E \rightarrow \mathbb{R}$ the function given by $N(f)=$ $\|f\|$ throughout. Then (2.5) can be written in the form
$$
\begin{equation*}
d N(f)=\left\{\phi \in E^{\prime}:\|\phi\| \leqslant 1,\langle E, \phi\rangle=\|f\|\right\} . \tag{2,6}
\end{equation*}
$$

A [strictiy] $N$-dissipative operator is simply called [strictly] dissipative (which is in accordance with the usual nomenclature).

Example 2.2. a) Let $E=C[0,1], f \in E$.
Then there exists $x \in[0,1]$ such that $|f(x)|=\left\|_{\|}\right\|_{i_{f}}$. Define $\phi \in E^{\prime}$ by $\langle g, \phi\rangle=(\operatorname{sign} f(x)) g(x)$. Then $\phi \in d N(f)$. Note that dN(f) may be an infinite set.
b) Let $H$ be a Hilbert space, $f \in H, f \neq 0$. Then $d N(f)=\left\{\phi_{f}\right\}$ where $\left\langle g, \phi_{f}\right\rangle=1 /\|f\|(g \mid f)$.
c) A - $\left\|_{\text {A }}\right\| I d$ is strictly dissipative for every bounded operator A.

Proposition 2.3. Let $A$ be an operator on $E$.
Then $A$ is $p$-dissipative if and only if
(2.7) $p(f) \leqslant p(f-t A f) \quad$ for all $f \in D(A), t>0$.

If in particular $(w, \infty) \in \rho(A)$ for some $w \in \mathbb{R}$, then $A$ is $p$-dissipative if and only if
$$
\begin{equation*}
P(\lambda R(\lambda, A) f) \leq p(f) \quad \text { for all } f \in E, \lambda>w . \tag{2.8}
\end{equation*}
$$

Proof. Assume that $A$ is $p$-dissipative. Let $f \in D(A), t \geqslant 0$. There exists $\phi \in \mathrm{dp}(\mathrm{f})$ such that $\langle\mathrm{Af}, \phi\rangle \leq 0$. Hence, $p(f)=\langle f, \phi\rangle=\langle f-t A f+t A f, \phi\rangle E \leq f-t A f, \phi\rangle \leqq p(f-t A f) \cdot S o$ $(2.7)$ holds.
Converse, let $f \in D(A)$. For every $t>0$ choose $\phi_{t} \in d p(f-t A f)$. Then $\pm<g, \phi_{t}>\leqslant p( \pm g) \leqslant c\|g\|$ for all $g \in E, t>0$. Thus the net $\left(\phi_{t}\right)_{t>0}$ is bounded. Consequently it posseses a $\sigma\left(E^{\prime}, E\right)$ - limit point $\phi$ as $t \rightarrow 0$. We show that $\phi \in d p(f)$ and $\langle A f, \phi\rangle \leqq 0$. Since $\left\langle g, \phi t^{>} \leqq p(g)\right.$ for all $t>0$ it follows that $<g, \phi>\leqq p(g)$ $(g \in E)$. Moreover, $\left\langle f, \phi_{t}>-t<A f, \phi_{t}>=p(f-t A f)(t>0)\right.$. Letting $t \rightarrow 0$ yields $\langle f, \phi\rangle=p(f)$.
We have proved that $\phi \in \operatorname{dp}(f)$. By hypothesis we have for all $t>0$, $\left.\left.\left.p(f) \leq p(f-t A f)=<f-t A f, \phi_{t}\right\rangle=\left\langle f, \phi_{t}\right\rangle-t<A f, \phi_{t}\right\rangle \leq p(f)-t<A f, \phi_{t}\right\rangle$. Consequently $\left\langle A f, \phi_{t}>0\right.$ for all $t>0$. Thus <Af, $\phi>0$.

Remark 2.4. The function $p$ is convex. So the one-sided Gateauxderivatives
$D_{g}^{+} p(f)=\lim _{t \downarrow 0} 1 / t(p(f+t g)-p(f)) \quad$ and $\mathrm{D}_{\mathrm{g}}^{-} \mathrm{p}(\mathrm{f})=\lim _{\mathrm{t}+\mathrm{O}} 1 / \mathrm{t}(\mathrm{p}(\mathrm{f}+\mathrm{tg})-\mathrm{p}(\mathrm{f}))$
exist and satisfy $D_{g}^{-} p(f) \leqq D_{g}^{+} p(f)$ for all $f, g \in E$ (cf. Moreau (1966)). Moreover,
$$
\begin{equation*}
\left.\mathrm{D}_{\mathrm{g}}^{+} \mathrm{p}(\mathrm{f})=\sup \{<\mathrm{g}, \phi\rangle: \phi \in \mathrm{dp}(f)\right\} \tag{2.9}
\end{equation*}
$$
$$
\begin{equation*}
D_{g}^{-} p(f)=\inf \{\langle g, \phi\rangle: \phi \in \operatorname{dp}(f)\} \tag{2.10}
\end{equation*}
$$

Thus $A$ is $p$-dissipative if and only if $D_{A f}^{-} p(f) \cong 0$, and $A$ is strictly p-dissipative if and only if $\mathrm{D}_{\mathrm{Af}}^{+} \mathrm{P}$ (f) $\leqq 0$ for all $f \in$ D(A).

Corollary 2.5. Let $A$ be a closable operator. If $A$ is p-dissipative, then so is its closure.

Theorem 2.6. Let $P$ be a continuous sublinear functional on a real Banach space $E$. Let $A$ be the generator of a strongly continuous semigroup (T(t)) $t \geqslant 0$. The following assertions are equivalent.
(i) $\quad \mathrm{P}(\mathrm{T}(\mathrm{t}) \mathrm{f}) \leqq \mathrm{p}(\mathrm{f}) \quad$ for all $\mathrm{t} \boldsymbol{\mathrm { C }} \mathrm{O}, \mathrm{f} \in \mathrm{E}$.
(ii) A is strictly p-dissipative.
(iii) There exists a core $D$ of $A$ such that $A \mid D$ is p-dissipative.

Proof. Assume that (i) holds. Let $f \in D(A), \phi \in \operatorname{dp}(f)$. Then $\langle A f, \phi\rangle=\lim _{t \rightarrow 0} l / t(\langle T(t) f, \phi\rangle-\langle f, \phi\rangle)$
$\left.=\lim _{t \rightarrow 0} 1 / t( < p(T(t) f)-p(f)) \leqq 0$.
This proves (ii).
It is trivial that (ii) implies (iii). So let us assume (iii). Then
it follows from Cor. 2.5 that $A$ is p-discipative. Hence by (2.8)
$p(\lambda R(\lambda, A) g) \leqq p(g)$ for all $g \leqslant E, \lambda>w(A)$. Hence $\lambda R(\lambda, A)$ is p-contractive for $\lambda>w(A)$. This implies that $T(t)$ is p-contractive by the formula (1.3)
$T(t)=\lim _{t \rightarrow 0}(n / t R(n / t, A))^{n} \quad($ strongly $)$ for $t \geqq 0$.

We have shown that for generators, p-dissipativity is equivalent to p-contractivity of the semigroup. Now we will consider a p-disai= pative operator A (which is not a generator a priori) and investi= gate under which additional hypotheses $A$ is the generator of a
(necessarily contractive) semigroup. At first we present some consequences of $p$-dissipativity.

Theorem 2.7. Let $A$ be a p-dissipative operator. If $D(A)$ is dense, then $A$ is strictly p-dissipative.

Proof. Let $f \in D(A), \phi \in \operatorname{dp}(f)$. Then for every $t>0$ and $g \in D(A)$ we have
$\langle A f, \phi\rangle=1 / t(\langle f+t A f, \phi\rangle-\langle f, \phi\rangle) \leqq l / t(p(f+t A f)-p(f))$

    $\leqq l / t(p(f+t g)+t p(A f-g)-p(f))$
    $\leqq 1 / t(p((I d-t A)(f+t g))+t p(A f-g)-p(f)) \quad(b y$ (2.7))
    $\leq 1 / t\left(p(f)+t p(g-A f)+t^{2} p(-A g)+t p(A f-g)-p(f)\right)$
    $\leq 1 / t\left(2 t c\|g-A f\|_{i}+t^{2} c\|A g\|_{i} \quad(b y(2.3))\right.$
    $=2 c\|g-A f\|+t c\|A g\|$.

Letting $t \rightarrow 0$ we obtain $A f, \phi>\equiv 2 c\|G-A f\|$ for all $g \in D(A)$. Since $D(A)$ is dense in $E$, this implies that $\langle A f, \phi\rangle \leqq 0$

We now impose stronger conditions on $p$. A continuous sublinear function $p: E \rightarrow \mathbb{R}$ is called half-norm if
(2.11) $\mathrm{P}(\mathrm{f})+\mathrm{p}(-\mathrm{f})>0$ whenever $\mathrm{f} \neq 0$;
and $p$ is called a strict half-norm if in addition there exists some constant $d>0$ such that
(2.12) $p(f)+p(-f) \geqq d\|f\| \quad$ for all $£ \in E$.

If $p$ is a half-norm, then
(2.13) $\|f\|_{\mathrm{p}}=\mathrm{p}(\mathrm{f})+\mathrm{p}(-\mathrm{f})$
$(f \in E)$
defines a norm on $E$ which is equivalent to the given norm if and only if $p$ is strict.

Remark 2.8. Every half-norm $P$ induces a closed proper cone $E \quad:=$ $\{ \pm \in E: p(-f) \leq 0\}$ on $E$. Any p-contractive operator $T$ on $E$ leaves the cone $E_{p}$ invariant (i.e. $T$ is positive for the corresponding ordering).
Conversely, given a closed proper cone $E_{+}$on $E$, then $p(f)=$ dist $\left(-\mathrm{f}_{\mathrm{f}} \mathrm{E}_{+}\right)=\inf \left\{\|f+\mathrm{f}\|: g \in \mathrm{E}_{+}\right\}$defines a half-norm on E such that $E_{+}=E_{P}$. This half-norm is called the canonical half-norm on the ordered Banach space ( $E, E_{+}$) , The canonical half-norm is strict if and only if the cone $E_{+}$is nommal ithis is equivalent to the fact that for every $\phi \in E^{\prime}$ there exist positive linear forms $\phi_{1}$ and $\phi_{2}$ on $E$ such that $\phi=\phi_{1}-\phi_{2}$ (see [Batty-Robinson (1984)] and [Schaefer (1966), Chap.v]).

Proposition 2.9. Let $A$ be a $p$-dissipative operator where $p$ is a half-norm. If $D(A)$ is dense, then $A$ is closable fand the closure of $A$ is p-dissipative as well (by Cor. 2.5)).

Proof. Let $f_{n} \in D(A), \lim _{n^{+\infty}} f_{n}=0, \lim _{n^{* \infty}} A f_{n}=g$. We have to show that $g=0$. To this end let $h \in D(A)$. Then (2.7) gives
$p\left(f_{n}+t h\right) \leqq p\left(f_{n}+t h-t A\left(f_{n}+t h\right)\right) \quad(t>0)$. Letting $n \rightarrow \infty \quad$ we obtain $p(t h) \cong p\left(t h-t g-t^{2} A h\right) \quad(t>0)$.
Hence $p(h) \leq p((h-g)-t A h) \quad(t>0)$ by positive homogeneity. Letting $t+0$ finally we obtain $p(h) \leqslant p(h-g)$ for all $h \in D(A)$. since $D(A)$ is dense by hypothesis, we can approximate $g$ by $h \in$ $D(A)$ and conclude that $P(g) \leqslant P(0)=0$. Since $\lim _{n+\infty} A\left(-f_{n}\right)=-g_{\text {r }}$ we have $p(-g) \leqq 0$ by symmetry. Hence $p(g)+p(-g) \leq 0$ which implies $g=0$ by (2.ll).

Lemma 2.10. Let $p$ be a half-norm and $A$ a p-dissipative operator. Then
(2.14) $\quad \lambda\|f\|_{\mathrm{p}} \leqq\|(\lambda-A) f\|_{\mathrm{p}} \quad$ for all $f \in D(A), h>0$.

In particular, ( $\lambda-A)$ is injective for all $h>0$.
If $p$ is strict and $A$ is closed, then im( $-A$ ) is closed for all $\lambda>0$.

Proof. Let $\lambda>0, f \in D(A)$. Then by (2.7), $\left.\lambda_{p(t f)}^{f} p(\lambda-A)( \pm f)\right)$. Hence $\lambda\left\|_{i f}\right\|_{p}=\lambda p(f)+\lambda p(-f) \leq p((\lambda-A) f)+p(-(h-A) f)=\|(\lambda-A) f\|_{p} *$ Thus (2.14) is proved. Now suppose that $p$ is strict. Then $\|$. ${ }^{\circ}$ is equivalent to the given norm, Let $\lambda>0$ and $g \in(i m(\lambda-A))$. Then $g=\lim _{n \rightarrow \infty}(\lambda-A) f_{n}$ for some seguence $\left(f_{n}\right){ }_{n \in \mathbb{N}} G D(A)$. It followr from (2.14) that ( $\left.f_{n}\right)_{n \in \mathbb{N}}$ is a Cauchy sequence. Let $f=\lim _{n \rightarrow \infty} f_{n}$. Then $\lim _{n \rightarrow \infty} A f_{n}=\lambda l i m_{n \rightarrow \infty} f_{n}-\lim _{n \rightarrow \infty}(\lambda-A) f_{n}=\lambda f-g$ existg. If $A$ is closed, this implies that $f \in D(A)$ and $A f=\lambda f-g$. Hence $g \neq(\lambda-A) f \in \operatorname{im}(\lambda-A)$. We have shown that im( $h \rightarrow A$ ) is closed.

The following is the main theorem of this section.

Theorem 2.ll. Let $p$ be a strict half-norm and $A$ an operator on E . The following assertions are equivalent.
(i) A is the generator of a p-contraction semigroup.
(ii) $D(A) \quad i s$ dense, $A$ is $p-d i s s i p a t i v e$ and im( $-A$ ) $=E$ for some $\lambda>0$.

Proof. since $P$ is a strict half-norm we can assume that $\|f\|=\|f\|_{p}$ for all $f \in E$. (i) implies (ii) by Theorem 2. 6.
Now suppose that (ii) holds. Then it follows from Lemma 2.10 that $\mu \in \rho(A)$ and $\|\mu R(\mu, A)\| \leq 1$ whenever $\mu>0$ such that im( $\mu-A)=E$. So by hypothesis $\lambda \in \rho(A)$ and dist $(\lambda, \sigma(A)) \cong\|R(\lambda, A)\|^{-1} 2 \lambda$. Hence $(0,2 \lambda) \subset \rho(A)$. Iterating this argument we see that $(0, \infty) \subset \rho(A)$. It follows from the Hille-Yosida theorem that A generates a contraction semigroup (T(t)) $t \geqslant 0$. Finally, from Thn. 2.6 it follows that (T(t)) $t \geq 0$ is $p-c o n t r a c t i v e . ~$

Of course, the norm function $N$ given by $N(f)=\| f j$ is a strict half-norm. In the case when $p=N$, Theorem 2.11 is due to Luner and Phillips (1961). It turns out to be extremely useful in showing that a concrete operator is a generator. Because of its importance we state this special case explicitly below (including the complex case). Before that let us formulate Theorem 2.11 for the care when the operator is merely given on a core.

Corollary 2.12. Let $P$ be a strict half-norm and $A$ be a densely defined operator. If $A$ is p-dissipative and ( $A$ - A) has dense range for some $\lambda>0$, then $A$ is closable and the closure $\bar{A}$ of $A$ generates a p-contraction semigroup.

Proof. It follows from Prop. 2.9 that $A$ is closable and the closure $\bar{A}$ is p-dissipative. Lemma 2.10 implies that $(\lambda-\bar{A}) D(\bar{A})=E$. So Thm. 2.11 yields the desired conclusion.

We conclude this section indicating the results for the complex case.

Let $E$ be a complex Banach space and $p: E \rightarrow \mathbb{R}_{+}$be a seminorm on $E$ (i.e. $p(f+g) \leqq p(f)+p(g)$ and $p(\lambda f)=|\lambda| p(f)$ holds for all $f_{y} g \in E, \lambda \in \mathbb{C}, \quad$. The subdifferential $d p(f) \quad o f \quad p$ in $f \in E$ is defined by
(2.15) $d p(f)=\left\{\phi \in E^{\prime}: \operatorname{Re}\langle g, \phi\rangle \leq p(g)\right.$ for $a l l g \in E$ and $\langle f, \phi\rangle=p(f) \quad$ ).

We assume in addition that $p$ is continuous. Then it follows from the Hahn-Banach theorem that $d p(f) \neq \emptyset$ for any $f \in E$.

A linear operator $A$ on $E$ is called p-dissipative if for all
$f \in D(A)$ there exists $\phi \in \operatorname{dp}(f)$ such that Re < Af, $\boldsymbol{f}\rangle \leq 0$.
The arguments given above show that also in the situation considered here $A$ is p-dissipative if and only if
$$
p((1-t A) £) \geqq p(f)
$$
for all f € $\mathrm{D}(\mathrm{A})$, t 亿 0 .

The results of this section carry over if they are appropriately modified. We explicitly state the most important result for the case when $P$ is the norm. A linear operator $A$ is simply called dissipative if it is $N$-dissipative where $N(f)=\|f\| \quad(f \in E)$.

Theorem 2.13 (Lumer-Phillipa). Let $A$ be a densely defined operator on a complex Banach space $E$. The following assertions are equivalent.
(i) A is closable and the closure of $A$ is the generator of a contraction semigroup.
(ii) $A$ is dissipative and ( $\lambda$ - A) has dense range for some $\lambda>0$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-064.jpg?height=232&width=689&top_left_y=1706&top_left_x=638)

In this section we shall prove that on $L^{\infty}$, on $H^{m}$ (D), and on some other classical Banach spaces every strongly continuous semigroup of operators ig uniformly continuous.

Leman 3.1. Let $\bar{T}=(T(t))_{t} \geq 0$ be a one-parameter semigroup of operators on a Banach space $E$. Suppose that $s=1 i m$ sup ${ }_{t} \| T(t)$ - Idj is finite. If $\lim t \rightarrow 0\left\|(T(t)-I d)^{2}\right\|=0$, then $T$ is uniformly continuous.

Proof. The identity $2(T(t)-I d)=T(2 t)-I d-(T(t)-I d)^{2}$ shows
that $2\|T(t)-I d\|-\left\|(T(t)-I d)^{2}\right\| \leqq\|T(2 t)-I d\|$. Hence
$2 s \leqslant 1 i m \sup _{t+0}\|T(2 t)-I d\|$. Obviously, lim sup $t+0\|T(2 t)-I d\|=s$ and so, $2 \mathrm{~s} \leq \mathrm{s}$. Consequently, $\mathrm{s}=0$.

Remarks. 1. If in Lemma $3.1 T=(T(t)) t \geq 0$ is strongly continuous, in which case $s \in \infty$, one can replace $\lim _{\mathrm{H}, 0}\left\|(T(t)-I d)^{2}\right\|=0$ by the weaker condition lim sup r(T(t) - Id) < 1 [Lotz (1985), Lemma 2] where $r$ denotes the spectral radius.
2. The condition $s<\infty$ in Lemma 3.1 is essential as the following example shows:

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be nonmoontinuous with $f(s+t)=f(s)+f(t)$ for all $s, t \in \mathbb{R}$ (see [Hamel (1905)]). Then $\{(t, f(t)): t \in \mathbb{R}\}$ is dense in $\mathbb{R}^{2}$. Hence for the semigroups $T=(T(t)) t \geq 0$ on $\mathbb{R}^{2}$ with
$$
T(t)=\left(\begin{array}{ll}
1 & f(t) \\
0 & 1
\end{array}\right) \quad \text { for } t \geqslant 0
$$
we have $s=m$. Therefore $T$ is not uniformly continuous. However, $(T(t)-I d)^{2}=0$ for all $亡 \geqq 0$.

Leman 3.2. Let $T=(T(t))_{t \geq 0}$ be a one-parameter semigroup of operatorg on a Banach space $E$. Then the following assertions are equivalent:
(a) $\quad T^{\prime}=\left(T(t)^{\prime}\right) t \geq 0$ is a strongly continuous semigroup on the dual $E^{\prime \prime}$.
(b) ( $\left.(T(t)-I d) x_{n}\right)$ converges weakly to zero for every bounded sequence $\left(x_{n}\right)$ in $E$ and every sequence $\left(t_{n}\right)$ in $[0, \infty)$ with 1 im $t_{n}=0$.

Moreover, (a) implies
(c) $T$ is strongly continuous.

Proof. Let $x^{\prime} \in E^{\prime}$ and $t_{n} \geqq 0$ be given. Then lim $\|\left(T\left(t_{n}\right)\right.$ Id) ${ }^{\prime} x^{\prime} \|=0$ if and only if $\lim \left\langle x_{n},\left(T\left(t_{n}\right)-I d\right)^{\prime} x^{\prime}\right\rangle=0$ for every bounded sequence $\left(x_{n}\right)$ in $E$. This easily implies the equivalence of (a) and (b). In particular, (a) implies that ( (T(t, $)$ - Id)x) converges weakly to zero for every sequence ( $t_{n}$ ) in $[0, \infty)$ with lim $t_{n}=0$ and every $x \in E$. Hence $T$ is strongly continuous by Propositon 1.23 in [Davies (1980)].

We recall that a Banach space $E$ is called a Grothendieck space if every weak* convergent sequence in $E$ * converges weakly.

Theorem 3.3. Let $E$ be a Grothendieck space. If $T=(T(t))_{t \geqslant 0}$ is a strongly continuous semigroup in $E$, then $T^{\prime \prime}=\left(T(t)^{\prime \prime}\right) t \geq 0 \quad i s$ strongly continuous in $E "$.

Proof. Suppose that $\left(x_{n}^{*}\right)$ is a bounded sequence in $E^{\prime}$ and that $t_{n} \geqq 0$ with 1 im $t_{n}=0$. Put $v_{n}=T\left(t_{n}\right)-I d$. Then 1 im $\|_{\|} V_{\|}=0$ and therefore $\lim \left\langle x, v_{n}^{\prime} x_{n}^{\prime}\right\rangle=0$ for every $x \in E$. Hence ( $V_{n}^{\prime} x_{n}^{\prime}$ ) $w^{*}$-converges to zero. Since $E$ is a Grothendieck space ( $V_{n}^{\prime} x_{n}^{\prime}$ ) converges weakly to zero. Now Lemma 3.2 implies that (T(t)") is strongly continuous.

Recall now that a Banach space $E$ is said to have the Dunford-Pettis property if $\quad$ im $\left\langle x_{n}, x_{n}^{\prime}\right\rangle=0$ whenever $\left(x_{n}\right)$ in $E$ and ( $\left.x_{n}^{\prime}\right)$ in $E^{r}$ converge weakly to zero.

Theorem 3.4. Let $E$ be a Banach space with the Dunford-Pettis property and let $T=(T(t))_{t \geq 0}$ be a one-parameter semigroup of operators on $E$. If $T^{\prime \prime}=\left(T(t)^{+\prime}\right) t \geqslant 0$ is strongly continuous in $E^{\prime \prime}$. then $T$ is uniformly continuous.

Proof. Suppose that $T^{\prime \prime}$ is a strongly continuous semigroup. Then Leman 3.2 implies that $T$ and $T$ are strongly continuous. Hence by
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-066.jpg?height=73&width=1615&top_left_y=1594&top_left_x=229) finite. By Lemma 3.1 it suffices to show that $\lim _{t \rightarrow 0}\left\|(T(t) \sim I d)^{2}\right\|=$ 0 . Let $t_{n} \geq 0$ with lim $t_{n}=0$ be given. Then there exists a bounded sequence $\left(x_{n}\right)$ in $E$ and a bounded sequence ( $x_{n}^{\prime}$ ) in $E$ ' such that $\left\|\left(T\left(t_{n}\right)-I d\right)^{2}\right\|_{i}=\left\{\left(T\left(t_{n}\right)-I d\right) x_{n},\left(T\left(t_{n}\right)-I d\right)^{s} x_{n}^{\prime}\right\rangle$. since $T$ and $T "$ are strongly continuous, Lemma 3.2 implies that $\left(\left(T\left(t_{n}\right)-I d\right) x_{n}\right)$ and $\left.\left.\left(T_{(1}\right)-I d\right)^{\prime} x_{n}^{\prime}\right)$ converge weakly to zero. since $E$ has the Dunford-Pettis property, lim $\left\|\left(T\left(t_{n}\right)-I d\right)^{2}\right\|=0$. Consequently, $\quad \lim _{t \rightarrow 0}\left\|(T(t)-I d)^{2}\right\|=0$.

An immediate consequence of Theorem 3.3 and Thoerem 3.4 is the following.

Theorem 3.5. Let $E$ be a Grothendieck space with the Dunford-Pettis property. Then every strongly continuous semigroup of operators on $E$ is uniformly continuous.

A compact Hausdorff space is called an F-space if the closures of two disjoint open $F_{\sigma}$-sets are disjoint and is called a stonean (res, o-Stonean) space if the closure of every open set (res., open $F_{o}$-set) is open. Every $\sigma-S t o n e a n ~ s p a c e ~ i s ~ a n ~ F-s p a c e . ~ . ~$

Theorem 3.6. Every strongly continuous semigroups of operators on one of the following Banach spaces is uniformly continuous:
1) $C(K)$, where $K$ is a compact $F$-space.
2) $L^{\infty}(S, \Sigma, \mu)$ for any measure space ( $5, \Sigma, \mu$ ).
3) The Banach space $B(S, \Gamma)$ of bounded $\Sigma$-measurable functions on
$S$ if $\quad$ is a otalgebra of subsets of $S$.
4) The Banach space $H(O)$ of bounded continuous solutions of
$$
\dot{L}_{1 \leqq i \leq n}\left(\partial^{2} \mathrm{f} / \partial \mathrm{x}_{\mathrm{i}}^{2}\right)=0
$$
on an open subset 0 of $\mathbb{R}^{n}$.
5) The Banach space $W(0)$ of bounded continuous solutions of
$$
\sum_{1 \leq i \leq n}\left(\partial^{2} f / \partial x_{i}^{2}\right)=\left(\partial f / \partial x_{n+1}\right)
$$
on an open subset 0 of $i^{n+1}$.
6) The Banach space $H^{\text {m }}$ (o) of bounded analytic functions on a finitely connected domain $O$ of the complex plane.

Proof. By Theorem 3.5 it suffices to show that the space listed above are Grothendieck spaces with the DunforduPettis property.
l I If $K$ is compact, then $C(K)$ has the Dunford-Pettis property [Grothendieck (1953) Théoreme 4]. If $K$ is a compact F-space, then C(K) is a Grothendieck space [Seever (1958) Theorem 2.5]; the special caser for stonean and $\sigma$-Stonean spaces are due to [Grothendieck (1953), Theoreme 9] and [Ando (1961)] respectively.
2) and 3) It is well known that every o-order complete AM-space with unit is isometric to a space $C(K)$ where $K$ is a compact
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-067.jpg?height=50&width=1615&top_left_y=1985&top_left_x=209) complete AM-spaces with unit and therefore by l) Grothendieck spaces with the Dunford-Pettis property.
4) and 5) These spaces are order complete vector lattices. This follows from [Bauer (1966) pp. 18-22, Standardbeispiele 1 and 2 p.55]. Since these spaces contain the constant functions on 0 they are complete for the supremum-norm. Indeed if ( $f_{n}$ ) is a Cauchy-sequence for this norm, it is easily seen that ( $f_{n}$ ) converges in norm to $\inf f_{n} \sup \left(f_{k}: n < k \right)$. Therefore these spaces are o-order complete AM-spaces with unit and so as before Grothendieck spaces with the Dunfordupettis property.
6) Bourgain [(1980), Cor. 3] proves that $H^{\infty}$ (D) has the DunfordPettis property and in [ (1984), Proposition III.1], that $H^{*}(D)$ is a

Grothendieck space, where $D$ is the open unit disc $\{z:|z|<1\}$. If $O$ is a finitely connected domain and $H^{*}$ does not only contain the constant functions, then $H^{(0)}(O)$ is isomorphic to a finite direct sum of copies of $H^{\infty}$ (D). (Note that $H^{(0}$ (D) is isomorphic to $\left\{f \in H^{\infty}(D) ; f(0)=0\right\}$ via the map $f \rightarrow z f$. Then uge [Grothendieck (1953), p. 77 and Prop.4.4.1]). Hence $H^{\infty}(0)$ is a Grothendieck space with the Dunford-Pettis property.

Final Remark. It follows from Theorem 3.6 that on $L^{\infty}$ the infinitesimal generator of a strongly continuous semigroup is necessarily bounded. It is not obvious that on $L^{\text {º }}$ ([0, 1$]$ ) there exist ciosed densely defined unbounded operators. To see this let $A$ be a closed densely defined unbounded operator form $\ell^{2}$ into $L^{\infty}([0,1])$ with donain $D$ (such operators can easily be constructed) . By the khintchine inequality, the map $R:\left(a_{n}\right)+\sum_{n} r_{n}$ where $r_{n}$ denotes the $n^{\text {th }}$ Rademacher function, from $t^{2}$ into $L^{1}([0,1])$ is a topological isomorphism. Hence $T=R^{\prime} \operatorname{maps} L^{+}([0,1])$ onto $\ell^{2}$. Banach's homomorphism theorem implies that $T^{-1}(D)$ is dense in $L^{\circ}([0,1])$ and that $A T$ is a closed densely defined unbounded operator on $L^{\text {º }}([0,1])$ with domain $T^{-1}(D)$. This solves a problem raised by R.Kaufman.
H. Porta and the author have shown that if a Banach space $E$ has an infinite dimensional separable quotient space and $F$ is an infinite dimensional Banach space then there always exists a closed densely defined unbounded operator from $E$ into $F$.

\section*{NOTES.}

Section l. The abstract Cauchy problem is treated systematically in the monographs of Krein (1971) and Fattoríni (1983). We refer to these books for more detajls and historical notes. One implication of Theorem $1 . l$ is proved in Krein (1971) (Thin.2.11).
The Hille-Yosida theorem has been proved independently by Hille (1948) and Yosída (1948) for contraction semigroups. The extenston to arbitrary strongly continuous semigroups is independently due to Feller (1953), Miyadera (1952) and Phillips (1953). Thus our termfnology is sifghtly incorrect, some authors refer to the general version as the Hille-Yosida-Phillips theorem which is slightly more correct. Holomorphic semigroups belong to the standard material of the theory of oneparameter semigroups. Our Theorem 1.14 deviates from the usual presentation since the condition on the resolvent is merely required on a half-plane.
Differentiable semigroups are treated in detail in the book of Pazy (1983) who discovered Theorem 1.17 and 1.18 .

The spectral property of eventually norm contintous semigroups given in Theorem 1.20 is contalned in Hille-Phillips (1957) (Thn. 16.4.2) with a proof depending on Gelfand theory. For norm continuous semigroups it is contained in Fazy (1983) with a simpler proof. The elementary proof we give here is due to $C$. Greiner.
Theorem 1.29 on the perturbation by bounded operators is due to Phjlifips (1953) who also investigated permanence of smoothness properties by this kind of perturbation, We also refer to Pazy (1983) (Sec.3.1). The observation that eventually norm continuity is preserved by perturbation by a compact operator (see Thm. 1,30 ) seems to be new.
The perturbation by continuous operators on the graph of the generator is due to Desch-Schappache: (1984). The short proof we give here is due to G. Greiner and has the advantage to yfeld the same permanence for smoothness properties as in the classical case (Cor.1.32).
The characterization of a core as "domein of uniqueness" (Thm.l.33) seems to be new. In this section we have presented part of the standard theory of one-parameter semigroups fincluding some new aspects. A very elegant brief introduction to oneparameter semigroups is given in the treatise of Kato (1966) where one can also find all the results on perturbation theory going beyond the elementary facts we discuss here. A complete information on the general theory can be obtajned by consulting the books of Davies (1980), Goldstein (1985a) and Pazy (1983). The monograph of Goldstein (1985a) in particular contains a variety of examples and applications.

Section 2. Dissipative operators were introduced by Lumer-Philifps (1961). The analogous notion of dispersiveness is due to Phillips (1962), Our approach follows closely Arendt-Chernoff-Kato (1982) where half-noms were introduced. Related previous results were obtained by Calvert (1971), Hasegawa (1966), Sato (1968), Bentlan-Picard (1979) and Pfocard (1972), where the two last consider non-linear semigroups. A further investigation of half-norms can be found in Batty-Robinson (1983) who consider ordered Banach spaces other than Banach lattices in great detafl. We also refer to the historical notes given there.

Section 3. It had been proved by Kishimoto-Robfnson (1981) that every generator of $a_{\text {ap }}$ positive semigroup on L is bounded. That every strongly continuous semigroup on $L^{\text {L }}$ is uniformly continuous was first shown by Lotr (1982), (1984), (1985). The proof of Lerma 3.1 was communicated to the author by $T$. Couihon, who independently obtained a particular case (Coulhon (1984)).

\title{
SPECTRAITHEORY \\ by \\ Giinther Greiner and Rainer Nagel
}

\section*{1. INTRODUCTION}

In this chapter we start a systematic analysis of the spectrum of a strongly continuous semigroup $T=(T(t))_{t} ¥_{0}$ on a complex Banach space $E$. By the spectrum of the semigroup we understand the spectrurn $o(A)$ of the generator $A$ of $T$. In particular we are interested in precise relations between $\sigma(A)$ and $\sigma(T(t))$. The heuristic formula
$$
T(t)=e^{t A}
$$
serves as a leitmotiv and suggests relations of the form
$$
\because \sigma(T(t))=e^{t \sigma(A)}=\left\{e^{t \lambda}: \lambda \in \sigma(A)\right\} ",
$$
called 'spectral mapping theorem'. These - or similar - relations will be of great use in Chapter IV and enable us to determine the asymptotic behavior of the semigroup $T$ by the spectrum of the generator. As a motivation as well as a preliminary step we concentrate here on the spectral radius
(1.1) $\quad r(T(t)):=\sup \{|\lambda|: \lambda \in \sigma(T(t))\}, t \geqslant 0$
and show how it is related to the spectral bound
$(1.2) \quad s(A):=\sup \left\{\operatorname{Re}^{\lambda}: \lambda \in \sigma(A)\right\}$
of the generator $A$ and to the growth bound
(1.3) $w:=\inf \left\{w \in \mathbb{R}:\left\|_{i}^{2} T(t)\right\| \leqq M_{w} \cdot e^{w t}\right.$ for all $t \geq 0$ and
suitable $\left.\mathrm{M}_{\mathrm{W}}\right\}$
of the semigroup $T=(T(t))_{t z 0}$. (Recall that we sometimes write $w^{T}$ ) or $w(A)$ instead of $w$ ) The Examples 1.3 and 1.4 below illustrate the main difficulties to be encountered.

Proposition l.1. Let $w$ be the growth bound of the strongly continuous semigroup $T=(T(t))_{t \geq 0}$. Then
$$
\begin{equation*}
I(T(t))=e^{\omega t} \tag{1.4}
\end{equation*}
$$
for every $t \geq 0$.

Proof. From A-I, (1.1) we know that
$$
\omega(T)=\lim _{t \rightarrow \infty} \frac{1}{t} \log \|T(t)\| .
$$

Since the spectral radius of $T(t)$ is given as
$$
r(T(t))=\lim _{n^{+\infty}}\left\|_{T} T(n t)\right\|^{1 / n}
$$
we obtain for $t>0$
$$
\begin{aligned}
I(T(t)) & =\lim _{n \rightarrow \infty} \exp \left(t(n t)^{-1} \log \|T(n t)\|\right) \\
& =e^{i \omega t}
\end{aligned}
$$

It was shown in A-I, Prop.l.ll that the spectral bound $s(A)$ is always dominated by the growth bound $w$ and therefore $e^{s(A) t} \leqq r(T(t))$. If the above mentioned spectral mapping theorem holds - as is the case for bounded generators (e.g., see Thm. VII. 3.1l of Dunford-Schwartz (1958)) we obtain the equality
$$
e^{s(A) t}=I(T(t))=e^{\omega t}
$$
hence $s(A)=w$. Therefore the following corollary is a consequence of the definitions of $s(A)$ and $\omega$.

Corollary 1.2. Consider the semigroup $T=(T(t)) t z 0$ generated by some bounded linear operator $A \in L(E)$. If Ren $\& 0$ for each $\lambda \in o(A)$ then $\lim _{t \rightarrow \infty}\|T(t)\|=0$.

Through this corollary we have re-established a famous result of Liapunov which assures that the solutions of the linear Cauchy problem
$$
\dot{x}(t)=A x(t), x(0)=x_{0} \in \mathbb{C}^{n} \text { and } A=\left(a_{i j}\right)_{n \times n}
$$
are 'stable' ; i.e., they converge to zero as $t \rightarrow \infty$, if the real parts of all eigenvalues of the matrix $A$ are smaller than zero.
For unbounded generators the situation is much more difficult and $s(A)$ may differ drastically from 4 .

Example 1.3. (Banach function space, Greiner-Voigt-Wolff (1981)) Consider the Banach space $E$ of all complex valued continuous functions on $\mathbb{R}_{+}$which vanish at infinity and are integrable for $e^{x} d x$, i.e.
$$
E:=C_{o}\left(\mathbb{R}_{+}\right) \cap L^{l}\left(\mathbb{R}_{+}, e^{x} d x\right)
$$
endowed with the norm
$$
\|f\|:=\|f\|_{\infty}+\|f\|_{1}=\sup \left\{|f(x)|: x \in \mathbb{R}_{+}\right\}+\int_{0}^{\infty}|f(x)| e^{x} d x .
$$

The translation semigroup
$$
T(t) f(x):=f(x+t)
$$
is strongly continuous on $E$ and one shows as in $A-I, 2.4$ that its generator is given by
$$
A f=f^{\prime}, D(A)=\left\{f \in E: E \in \mathbb{C}^{1}\left(\mathbb{R}_{+}\right), f^{\prime} \in E\right\}
$$

First we observe that $\|T(t)\|=1$ for every $t \geq 0$, hence $w(T)=0$. Moreover it is clear that $A$ is an eigenvalue of $A$ as soon as Red < -1 (in fact : the function
$$
x \rightarrow \varepsilon_{\lambda}(x):=e^{\lambda x}
$$
belongs to $D(A)$ and is an eigenvector of $A$, hence $s(A) \geq-1$. For $f \in E, \operatorname{Re\lambda }>-1$,
$$
\|\cdot\|_{1}^{-1 i m} t_{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s_{T}} T(s) f d s
$$
exists since $\|T(s) f\|_{1} \leq e^{-5}\|f\|_{1}, s \geq 0$, and
$$
\|\cdot\|_{\infty}-1 i m_{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s) f d s
$$
exists since $\int_{0}^{\infty} e^{x}|f(x)| d x<\infty$. Therefore $\int_{0}^{\infty} e^{-\lambda s} T(s) f$ ds exists in $E$ for every $f \in E$, Red $>-1$. As we observed in $A-I$, Prop.l.ll this implies $\lambda \in \rho(A)$. Therefore $T=(T(t))$ ta $\quad$ is a semigroup having $s(A)=-1$ but $\omega(T)=0$.

Example 1.4. (Hilbert space, Zabczyk (1975)) For every $n \in \mathbb{N}$ consider the $n$-dimensional Hilbert space $E_{n}:=\mathbb{C}^{n}$ and operators $A_{n} \in L\left(E_{n}\right)$ defined by the matrices
$$
A_{n}=\left[\begin{array}{lllll}
0 & 1 & \cdot & \cdots & 0 \\
\cdot & 0 & 1 & & \cdot \\
\cdot & \cdot & * & 1 \\
0 & \cdot & & \cdot & 0
\end{array}\right\}_{n \times n}
$$

These matrices are nilpotent and therefore o( $\left.A_{n}\right)=\{0\}$. The elements $x_{n}:=n^{-1 / 2}(1, \ldots, 1) \in E_{n}$ satisfy the following properties :
(i) $\quad\left\|x_{n}\right\|=1$ for every $n \in \mathbb{N}$,
(ii) $\quad \lim _{n \rightarrow \infty}\left\|A_{n} x_{n}-x_{n}\right\|=0$,
(iii) $\lim _{n \rightarrow \infty}\left\|\exp \left(t A_{n}\right) x_{n}-e^{t} x_{n}\right\|=0$.

Consider now the Hilbert space $E:=\oplus_{n \in N} E_{n}$ and the operator $A:=\left(A_{n}+2 \pi i n\right){ }_{n \in \mathbb{N}}$ with maximal domain in $E$. Analogously we define a semigroup $T=(T(t))_{t} \quad$ by
$$
T(t):=\left(e^{2 \pi i n t} \exp \left(t A_{n}\right)\right)_{n \in \mathbb{N}}
$$

Since $\left\|\exp \left(t A_{n}\right)\right\| \leqq e^{t}$ for every $n \in \mathbb{N}, t \geqq 0$, and since $t \rightarrow T(t) x$ is continuous on each component $E_{n}$ it follows that $T$ is strongly continuous. Its generator is the operator A as defined above.
For $\lambda \in \mathbb{C}, \operatorname{Re\lambda }>0$, we have $\lim _{n \rightarrow \infty}\left\|R\left(\lambda-2 \pi i n, A_{n}\right)\right\|=0$, hence $\left(R\left(\lambda, A_{n}+2 \pi i n\right)\right)_{n \in \mathbb{N}}=\left(R\left(\lambda-2 \pi i n, A_{n}\right)\right)_{n \in \mathbb{N}}$
is a bounded operator on $E$ representing the resolvent $R(\lambda, A)$. Therefore we obtain $s(A) \leq 0$. On the other hand, each $2 \pi i n$ is an eigenvalue of $A$, hence $s(A)=0$.
Take now $x_{n} \in E_{n}$ as above and consider the sequence $\left(x_{n}\right){ }_{n} \in \mathbb{N}$. From (iii) it follows that for $t>0$ the number $e^{t}$ is an approximate eigenvalue of $T(t)$ with approximate eigenvector $\left(x_{n}\right)_{n \in \emptyset}$ (see Def.2.1 below). Therefore $e^{t} \leqq r(T(t)) \leqq\left\|^{\prime} T(t)\right\|$ and hence $\omega(T) \geq 1$. On the other hand, it is easy to see that $\|T(t)\|=e^{t}$, hence $\omega(T)=1$.
Finally if we take $S(t):=e^{-t / 2} \cdot T(t)$ we obtain a semigroup having spectral bound - $\frac{1}{2}$ but such that $\lim _{t \rightarrow \infty}\|S(t)\|=\infty$ in contrast with Cor. 1,2 .

These examples show that neither the conclusion of Cor.1.2, i.e. 's(A) < 0 implies stability', nor the 'spectral mapping theorem'
$$
\sigma(T(t))=\exp (t \cdot \sigma(A))
$$
is valid for arbitrary strongly continuous semigroups. A careful analysis of the general situation will be given in Section 6 below, but we will first develop systematically the necessary spectral theoretic tools for unbounded operators.

\section*{2. THE FINE STRUCTURE OF THE SPECTRUM}

As usual, with a closed linear operator $A$ with dense domain $D(A)$ in a Banach space $E$, we associate its spectrum $\sigma(A)$, its resolvent set $p(A)$ and its resolvent
$$
\lambda \rightarrow R(\lambda, A):=(\lambda-A)^{-1}
$$
which is a holomorphic map from $\rho(A)$ into $L(E)$. In contrast to the finite dimensional situation, where a linear operator fails to be surjective if and only if it fails to be injective, we now have to dis~ tinguish different cases of 'non-invertibility' of $k$ - A. This dis~ tinction gives rise to a subdivision of $o(A)$ into different subsets. We point out that these subsets need not be disjoint, but our defini-
tion seems to be justified by the fact that for each of the following subsets of o(A) there exist canonical constructions converting the corresponding spectral values into eigenvalues (see Prop. 2.2.ii and Prop. 4.5 below).

Definition 2.1. For a closed, densely defined, linear operator $A$ with domain $D(A)$ in the Banach space $E$ denote by the
(i) point spectrum $P \sigma(A)$ the set of all $\lambda \in \mathbb{C}$ such that $\lambda-A$ is not injective.
(ii) aporoximate point spectrum Ao(A) the set of all $\lambda \in \mathbb{C}$ such that $\lambda-A$ is not injective or $(\lambda-A) D(A)$ is not closed in E.
(iii) residual spectrum $R$ (A) the set of all $A \in \mathbb{C}$ such that ( $A$ - A) $D(A)$ is not dense in $E$.

From these definitions it follows that $\lambda \in \mathcal{E}$ is an eigenvalue of $A, i, e, \lambda \in P o(A), i f$ and only if there exists an eigenvector $0 \neq \mathrm{f} \in \mathrm{D}(\mathrm{A})$ such that $A f=\lambda f$. It follows from the open Mapping Theorem that $\lambda \in A \sigma(A)$ if and only if $\lambda$ is an approximate eigenvalue, i.e. there exists a sequence ( $\left.f_{n}\right)_{n \in \mathbb{N}}=\mathrm{D}(\mathrm{A})$, called an approximate eigenvector, such that $\left\|f_{n}\right\|=1$ and $1 i_{n} m_{n}\left\|A_{n}-\lambda f_{n}\right\|$ $=0$.
Clearly we have $P \sigma(A) \quad \therefore \quad A \sigma(A)$ and o(A) $=A \sigma(A) \quad U$ Ro(A) where the union need not be disjoint.

The following proposition is a first indication that the subdivision we made implies nice properties.

Proposition 2.2. For a closed, dencely defined, linear operator (A,D(A)) in a Banach space $E$ the following holds:
(i) The topological boundary $\partial \sigma(A)$ of $\sigma(A)$ is contained in Ao (A) .
(ii) $R o(A)=P o\left(A^{\prime}\right)$ for the adjoint operator $A^{r}$ on $E^{\prime}$.

Proof. (i) Take $\lambda_{o} \in \partial o(A)$ and $\lambda_{n} \in \rho(A)$ such that $\lambda_{n} \rightarrow \lambda_{o}$. Since $\left\|R\left(\lambda_{n}, A\right)\right\|\left(\operatorname{dist}\left(A_{n}, o(A)\right)\right)^{-1} \quad($ see Prop. $2.5 .(i i))$, by the uniform boundedness principle we find $\bar{f} E$ such that
$$
\lim _{n \rightarrow \infty}\left\|R\left(\lambda_{n}, A\right) f\right\|=\infty
$$

Define $\quad g_{n} \in D(A) \quad b y$
$$
g_{n}:=\left\|R\left(\lambda_{n}, A\right)\right\|^{-1} R\left(\lambda_{n}, A\right) f
$$
and use the identity
$$
\left(\lambda_{0}-A\right) g_{n}=\left(\lambda_{0}-\lambda_{n}\right) g_{n}+\left(\lambda_{n}-A\right) g_{n}
$$
to show that $\left(g_{n}\right){ }_{n \in \mathbb{N}}$ is an approximate eigenvector corresponding to $\lambda_{0}$.
(ii) This is a simple consequence of the Hahn-Banach theorem.

In order to illuminate the above definitons we now return to the Standard Examples introduced in Section 2 of $A-I$ and discuss the fine structure of the spectrum of these strongly continuous semigroups, i.e. of their generators and their semigroup operators.

\subsection*{2.3 The Spectrum of Multiplication Semigroups.}

Take $E=C_{o}(X)$ for some locally compact space $X$ and take a continuous function $q$; $X \rightarrow C$ whose real part is bounded above. As obu served in A-I, 2.3 the multiplication operator
$$
M_{q}: f \rightarrow q \cdot f
$$
with maximal domain $D\left(M_{q}\right)$ generates the multiplication semigroup $T(t) f:=e^{t q} \cdot f \quad, f \in E$.

Since $M_{q}$ is bounded if and only if $g$ is bounded we conclude that $M_{q}$ is invertible (with bounded inverse $M_{l / q}$ ) if and only if
$$
0 \$ \operatorname{Tq}(x)=x \in x T
$$

Therefore we obtain
$$
\left.\sigma\left(M_{q}\right)=\overline{q(\bar{X})}=\overline{\mathrm{q}(\mathrm{x})}: x \bar{x}\right)
$$
and
$$
\phi(T(t))=\overline{\exp (t g(x)): x \in x\}}
$$

In particular the following 'weak spectral mapping theorem is valid:
$$
\sigma(T(t))=\overline{\exp \left(t \sigma\left(M_{q}\right)\right)}
$$

In addition we observe that to each spectral value of $A$ (resp. of $T(t)$ ) there exists an approximate eigenvector and hence
$$
\sigma(A)=A \sigma(A) \quad \text { and } \quad \sigma(T(t))=A \sigma(T(t)) .
$$

Since each Dirac functional is an eigenvector for the adjoint multiplication operator we obtain
$$
\mathrm{q}(\mathrm{X})=\operatorname{Ro}\left(\mathrm{M}_{\mathrm{q}}\right) \quad \text { and } \mathrm{e}^{\operatorname{tq}(\mathrm{X})}=\operatorname{Ro}(\mathrm{T}(\mathrm{t}))
$$

The eigenvalues of $M_{q}$ can be characterized as follows:
$\lambda \in \operatorname{Po}\left(M_{q}\right)$ if and only if the set $\{x \in X: q(x)=\lambda\}$ has non empty interior (analogously for Po(T(t)) , For example, it followr that $\operatorname{Po}\left(M_{q}\right)=\emptyset \quad$ for $E=C_{0}\left(\mathbb{R}_{+}\right)$and $q(x)=-x, x \in \mathbb{R}_{+}$.

On $E=L^{P}(X, \Sigma, \mu)$ analogous results are valid, but their exact formulation - using the notion 'essential range', see Goldstein (1985a) is left to the reader.
2.4 The Spectrum of Translation Somigroups.

First we consider the translation semigroup
$$
T(t) f(x):=f(x+t)
$$
on $E=C_{0}\left(\mathbb{R}_{+}\right) \quad\left(\right.$ or $L^{P}\left(\mathbb{R}_{+}\right)$, see $\left.A-I, 2.4\right)$. Its generator $A$ is the first derivative and for every $\lambda \in \mathbb{C}, \operatorname{Re\lambda }<0$, the function $\varepsilon_{\lambda}: x+e^{\lambda x}$ belongs to $D(A)$ and satisfies
$$
A E_{\lambda} \neq \lambda E_{\lambda}
$$
hence $\lambda \in P \sigma(A)$. Since $T=(T(t)) t \geq 0$ is a contraction semigroup it follows that $o(A)=\{\lambda \in \mathbb{C}: \operatorname{Re\lambda } \leq 0\}$ and iR $\subset A_{0}(A)$ (uge Prop. 2.2.(i) or show directly that $f_{n}(x)=e^{i a x} \cdot e^{-x / n}$ defines an approximate eigenvector for $i \alpha, \alpha \in \mathbb{R}$, Using the same functions one obtains
$$
\operatorname{Po}(T(t))=\left\{\mathrm{e}^{\lambda t}: \operatorname{Reh}<0\right\}=\{\mathrm{z} \in \mathbb{C} ;|\mathrm{z}|<1\}
$$
and $\sigma(T(t)) \neq\{z \in \mathbb{Z} \in|z| \leqq 1\}$ for every $t>0$.
In the case of the translation group on $E=C_{0}(\mathbb{R})$ one has that $\sigma(A) \subset i \mathbb{R}$. As above one obtains approyimate eigenvectors for every $a \in \mathbb{R}$ from $E_{n}(x)=e^{i \alpha x} \cdot e^{-|x| / n}$, hence
$$
\sigma(A)=A \sigma(A)=\mathbb{R}
$$

The generator $A$ of the nilpotent translation semigroup $A-I, 2,6$ has empty spectrum by A-I,Prop.l.ll. The resolvent is given by
$R(\lambda, A) f(x)=e^{\lambda x} \int_{x^{\prime}} e^{-\lambda} S_{f}(s) d s \quad\left(f \in L^{P}([0, \bar{\tau}], \lambda \in \mathbb{C})\right.$.
Finally the generator of the periodic translation group from $A-I, 2.5$ on $E=\{f \in C[0,1.1: f(0)=f(1)\}$ has point spectrum
$$
P \sigma(A)=2 \pi i Z
$$
with eigenfunctiong $g_{n}(x):=\exp (2 \pi i n x)$. In Section 5 we show that $\sigma(A)=2 \pi i \bar{Z}$.

We now return to the general theory and recall from Corollary 1.2 that it is very useful (e.g., for stability theory) to be able to convert
spectral values of the generator $A$ into spectral values of the gemigroup operator $T(t)$ and vice versa. As shown in Examples 1,3 and 1.4 this is not possible in general. Therefore we tackle first a much easier 'spectral mapping theorem'; the relation between $\sigma(A)$ and $o\left(R\left(\lambda_{0}\right)\right)$, where $R\left(\lambda_{0}\right):=R\left(\lambda_{o}, A\right)$ for some $\lambda_{o} \in \rho(A)$.

Proposition 2.5. Let (A,D(A)) be a densely defined closed linear operator with non-empty resolvent set $\rho(A)$. For each $\lambda_{o} \in(A)$ the Eollowing assertions hold :
(i)
$\sigma\left(R\left(\lambda_{O}\right)\right) \quad\{0\}=\left(\lambda_{O}-\sigma(A)\right)^{-1}$, In particular, $I\left(R\left(\lambda_{O}^{O}\right)\right)=\left(\text { dist }\left(\lambda_{O}, \sigma(A)\right)\right)^{-1}$.
(ii) Analogous statements hold for the point-, approximate point-, residual spectra of $A$ and $R\left(\lambda_{o}, A\right)$.
(iii) The point $\alpha$ is isolated in $\sigma(A)$ if and only if $\left(\lambda_{0}^{-\alpha}\right)^{-1}$ is isolated in $\sigma\left(R\left(\lambda_{0}\right)\right)$. In that case the residues (resp., the pole orders) in $a$ and in $\left(\lambda_{0}-\alpha\right)^{-1}$ coincide.

Proof. (i) is well known. It can be found for example in [DunfordSchwartz (1958), VII.9.2].
(ii) We show that $\alpha \in A_{\sigma}(A)$ if $\left(\lambda_{o}-\alpha\right)^{-l} \in A \sigma\left(R\left(A_{0}\right)\right)$ and leave the proof of the remaining statements to the reader. Take $\left(f_{n}\right)_{n \in H_{i}} \in E$ such that $\left\|f_{n}\right\|=1,\left\|\left(\lambda_{o}-\alpha\right)^{-1} f_{n}-R\left(\lambda_{o}, A\right) f_{n}\right\|+0$ and $\left|\left|R\left(A_{o}, A\right) f_{n}\right| \geq \frac{1}{2}\right| \lambda_{o}-\left.a\right|^{-1}$. Define
$$
g_{n}:=\left\|R\left(\lambda_{0}, A\right) f_{n}\right\|^{-1} \cdot R\left(\lambda_{0}, A\right) f_{n} \in D(A)
$$
and deduce from
$$
\begin{aligned}
(\alpha-A) g_{n} & =\left\|R\left(\lambda_{0}, A\right) f_{n}\right\|^{-1} \cdot\left[\left(\lambda_{0}-A\right)-\left(\lambda_{0}-\alpha\right)\right] R\left(\lambda_{0}, A\right) f_{n} \\
& =\| R\left(\lambda_{0}, A\right) f_{n} j^{-1} \cdot\left(\lambda_{0}^{-\alpha)\left[\left(\lambda_{0}-\alpha\right)^{-1}-R\left(\lambda_{0}, A\right)\right] f_{n}}\right.
\end{aligned}
$$
that $\left(g_{n}\right)$ is an approximate eigenvector of $A$ to the eigenvalue $a$. (iii) Take a circle $\Gamma$ with center a and sufficiently small radius. Then the residue $P$ of $R(, A)$ at $a$ is
$$
\begin{aligned}
P & =\frac{1}{2 \pi i} \int_{\Gamma} R(z, A) d z \\
& =\frac{1}{2 \pi i} \int_{\Gamma}\left(\lambda_{O}-z\right)^{-2} R\left(\left(\lambda_{O}^{-z}\right)^{-1}, R\left(\lambda_{O}, A\right)\right) d z \\
& \left.-\frac{1}{2 \pi i} \int_{\Gamma}\left(\lambda_{O}^{-z}\right)^{-1} d z, \text { (use } \$ \$\right)
\end{aligned}
$$

If $\lambda_{0}$ lies in the exterior of $\Gamma$ the second integral is zero. The
substitution $\underset{z}{z}:=\left(\lambda_{0}-z\right)^{-1}$ yields a path $\sum_{\Gamma}$ around $\left(\lambda_{o}^{-\alpha}\right)^{-1}$ and we obtain
$$
P=\frac{1}{2 \pi i} \int_{\Gamma} R\left(z, R\left(\lambda_{O}, A\right)\right) d z,
$$
which is the residue of $R\left(\ldots R\left(\lambda_{0}, A\right)\right)$ at $\left(A_{o}-a\right)^{-1}$. The final assertion on the pole order follows from the identities
$$
V_{-n}=\left(\left(\lambda_{0}-\alpha\right)^{-1} R_{\left(\lambda_{0}, A\right)}\right)^{n-1_{0}}{ }_{-n}, \quad n \in \mathbb{N},
$$
where $U_{n}, r e s p . ~ V_{n}$ stand for the $n$-th coefficient in the Laurent series of $R(, A)$, resp. $R\left(., R\left(\lambda_{o}, A\right)\right)$ at $a$, resp. $\left(\lambda_{o}^{-\alpha}\right)^{-1}$. This has already been proved for $n=1$ and follows for $n>1$ by induction, using the relations
$$
U_{-n-1}=(A-\alpha) U_{-n} \text { and } v_{-n-1}=\left(R\left(\lambda_{0}, A\right)-\left(\lambda_{o}^{-\alpha}\right)^{-1}\right) v_{-n}
$$

\section*{3. SPECTRAL DECOMPOSITION}

In the next two sections we develop some important techniques for our further investigation of semigroups and their generators. Even though these methods are well known (compare, e.g. Section VII. 3 of DunfordSchwartz (1958)) or rather technical, it is useful to present them in a coherent way.

Our interest in this section is the following : Let $E$ be a Banach space and $T=(T(t))_{t} \sum_{0}$ a strongly continuous semigroup with generator A . Suppose that the spectrum $\sigma(A)$ splits into the disjoint union of two closed subsets $o_{1}$ and $o_{2}$. Does there exist a corresponding decomposition of the space $E$ and the semigroup $T$ ?

In the following definition we explain what we understand by "corres" ponding decomposition".

Definition 3.1. Assume that $\sigma(A)$ is the disjoint union
$$
\sigma(A)=\sigma_{1} \cup \sigma_{2}
$$
of two non-empty closed subsets $\sigma_{1}, \sigma_{2}$. A decomposition
$$
E=E_{1} \oplus E_{2}
$$
of $E$ into the direct sum of two non-trivial closed T-invariant subspaces is called a spectral decomposition corresponding to ${ }^{\circ}{ }_{1} U \sigma_{2}$ if the spectrum o( $A_{i}$ ) of the generator $A_{i}$ of $T_{i}:=\left(\left.T(t)\right|_{i}\right)_{t \geqslant 0}$ coincides with $\sigma_{i}$ for $i=1,2$.

For a better understanding of the above definition we recall that to every direct sum decomposition $E=E_{1} \oplus E_{2}$ there corresponds a continuous projection $P \in L(E)$ such that $P E=E_{1}$ and $P^{-1}(0)=F_{2}$. Moreover, the subspaces $E_{1}, E_{2}$ are T-invariant if and only if $P$ commutes with the semigroup $T$, i.e. $T(t) P=P T(t)$ Eor every $t 20$. In this case it follows that the domain $D(A)$ of the generator $A$ splits analogously and $D(A) \cap E_{i}$ is the domain $D\left(A_{i}\right)$ of the generator $A_{i}$ of the restricted semigroup $T_{i}, i=1,2$. We write
$$
\mathrm{A}=\mathrm{A}_{1} \oplus \mathrm{~A}_{2},
$$
say that " $A$ commutes with $P$ " and call $P$ a spectral projection. In terms of the generator $A$ this means that for $f \in D(A)$ we have $P f \in D(A)$ and $A P f=P A f$.
The existence of such projections is very helpful since it reduces the semigroup $T$ into two (possibly simpler) semigroups $T_{1}, T_{2}$ such that
$$
\sigma(A)=\sigma\left(A_{1}\right) \cup \sigma\left(A_{2}\right) \quad \text { and } \quad \sigma(T(t))=\sigma\left(T_{1}(t)\right) \cup \sigma\left(T_{2}(t)\right)
$$

For example, in some cases (see Theorem 3.3 below) it can be shown that one of the reduced semigroups has additional properties.

In order to achieve such decompositions we will assume that $\sigma$ (A) decomposes into sets $\sigma_{1}$ and $\sigma_{2}$ and will then try to find a corresponding spectral projection. Unfortunately such spectral decomposi* tions do not exist in general.

Example 3.2. Take the rotation semigroup from A-I, 2.4 on the Banach space $L^{P}(\Gamma), 1 \leqq p<\infty, \tau=2 \pi$. It was stated in 2.4 and will be proved in Section 5 that its generator $A$ has spectrum
$$
\sigma(A)=P_{\sigma}(A)=i \pi .
$$
where $E_{k}(z):=z^{k}$ spans the eigenspace corresponding to $i k, k \in \mathbb{Z}$, Now, $\sigma(A)$ is the disjoint union of $o_{1}:=\{0, i, 2 i, \ldots\}$ and $\sigma_{2}:=\{-i,-2 i, \ldots\}$. By a result of M. Riesz there is no projection $P^{2} \in L\left(L^{1}(\Gamma)\right)$ satisfying $P_{E_{k}}=E_{k}$ for $k \geqslant 0, P \varepsilon_{k}=0$ for $k<0$ (see Lindenstrauss-Tzafriri (1979), p.165), hence there is no spectral decomposition of $L^{l}(\Gamma)$ corresponding to $\sigma_{1}, \sigma_{2}$. On the other hand, for $L^{P}(\Gamma), l < p <\infty$, such a spectral projection exists (l.c., 2.c.15). As long as $p \neq 2$ we can always decompose $\sigma$ (A) into suitable subsets admitting no spectral decomposition (1.c., remark before 2.c.l5). Clearly, for $p=2$ such spectral decompositions always exist.

In the above example both subsets ${ }^{\circ}{ }_{1}, \sigma_{2}$ of $\sigma(A)$ are unbounded. But as soon as one of thege sets ig bounded a corresponding spectral decomposition can always be found.

Theorem 3.3. Let $T$ be a strongly continuous semigroup on a Banach space $E$ and assume that the spectrum $\sigma(A)$ of the generator $A$ can be decomposed into the disjoint union of two non-empty closed subsets $\sigma_{1}, \sigma_{2}$. If $\sigma_{1}$ is compact then there exists a unique corresponding spectral decomposition $E=E_{1} \oplus E_{2}$ such that the restricted semigroup $T_{1}$ has a bounded generator.

Proof. We ascume the reader to be familiar with the spectral decomposition theorem for bounded operators (see e.g. [Dunford-schwartz (1958), p.572]) and apply the "spectral mapping theorem" for the resolvent (A-III, Thm. 2.5) in order to decompose $R(\lambda, A)$ instead of $A$ : For $\lambda_{0}>\omega_{0}(T)$ it follows from $A-I I I$, Thm. 2.5 that $o\left(R\left(\lambda_{0}, A\right)\right)$ \{0\} $=\left(\lambda_{0}-\sigma(A)\right)^{-1}$. From $\sigma(A)=\sigma_{1} U \sigma_{2}$ we obtain a decomposition of $o\left(R\left(\lambda_{0}, A\right)\right)$ (0] into
$$
t_{1}:=\left(\lambda_{0}^{-\sigma_{1}}\right)^{-1} \quad, \quad \tau_{2}:=\left(\lambda_{0}-\sigma_{2}\right)^{-1} .
$$

Since ${ }^{\circ} 1$ is compact the set ${ }^{\tau} 1$ is compact and does not contain 0 . only in the case that $\sigma_{2}$ is unbounded the point 0 will be an accumulation point of ${ }^{\tau} 2$. Therefore $\sigma\left(R\left(\lambda_{0}, A\right)\right) \quad U$ $[0]$ is the disjoint union of the closed sets ${ }^{\tau} 1$ and $t_{2} \cup\{0\}$.
Take now $P$ to be the apectral projection of $R\left(\lambda_{0}, A\right)$ corresponding to this decomposition. Then $P$ commutes with $R\left(h_{0}, A\right)$ (by definition), with $R(\lambda, A)$ for every $\lambda>\omega(T)$ (use the series representation of the resolvent), with $T(t)$ for each $t \geqslant 0$ (use $A-I I$, Prop.l.10) and therefore with the generator $A$ (in the sense explained above). In particular, we obtain
$$
R\left(\lambda_{0}, A\right) P=R\left(\lambda_{0}, A_{1}\right), R\left(\lambda_{0}, A\right)(I d-P)=R\left(\lambda_{0}, A_{2}\right)
$$
for the generator ${ }^{A_{1}}$ of $T_{1}=(T(t) P){ }_{t \geqslant 0}$ and $A_{2}$ of $T_{2}=(T(t)(I d-P))_{t \geq 0}$. Applying the Spectral Mapping Theorem 2.5 we conclude
$$
\sigma\left(A_{1}\right)=\sigma_{1} \text { and } \quad \sigma\left(A_{2}\right)=\sigma_{2},
$$
i.e., $P$ is a spectral projection corresponding to $\sigma_{1}, \sigma_{2}$. Finally, the above spectral decomposition of $R\left(\lambda_{0}, A\right)$ is unique and satisfies 0 \& $o\left(R\left(\lambda_{0}, A_{1}\right)\right)$. Therefore $R\left(\lambda_{0}, A_{1}\right)^{-l}=\left(\lambda_{0}-A_{1}\right) \quad i s$ bounded.

Example. If we do not require $T_{1}$ to be uniformly continuous the above spectral decomposition need not be unique :
Consider a decomposition $E=E_{1} \oplus E_{2}$ and add a direct summand $E_{3}$ with a strongly continuous semigroup $T_{3}$ whose generator $A_{3}$ has empty spectrum (e.g. A-I, Example 2.6). Then still $\sigma(A)=\sigma_{1} U \sigma_{2}$ but $E_{1} \oplus\left(E_{2} \oplus E_{3}\right)$ and $\left(E_{1} \oplus E_{3}\right) \oplus E_{2}$ are two different spectral decompositions corresponding to ${ }^{\circ}, o_{2}$.

The importance of the above theorem stems from the fact that $T_{I}$ has a bounded generator and therefore is easy to deal with. In particular the asymptotic behavior of $T_{1}$ can be deduced from the location of ${ }^{\sigma}{ }_{1}$ -

Corollary 3.4. Assume that $\sigma$ (A) splits into non-empty closed sets $\sigma_{1}, \sigma_{2}$ where $\sigma_{1}$ is compact and consider the corresponding spectral decomposition $E=E_{1} \oplus E_{2}$ for which $T_{1}$ is uniformly continuous. For all constants $v, w \in \mathbb{R}$ satisfying
$$
v<\inf \left\{\operatorname{Re} \lambda: \lambda \in \sigma_{1}\right\} \text { and } \sup \left\{\operatorname{Re} \lambda: \lambda \in \sigma_{1}\right\} < w
$$
there exist $m, M \geq 1$ such that
$$
\mathrm{m} \cdot \mathrm{e}^{\mathrm{vt}}\|\mathrm{f}\| \leqq\left\|\mathrm{T}_{1}(\mathrm{t}) \mathrm{f}\right\| \leqq \mathrm{M} \cdot \mathrm{e}^{\mathrm{wt}}\|\mathrm{f}\|
$$
for every $f \in E_{1}, t \geq 0$.
Proof. Since the generator $A_{1}$ of $T_{1}$ is bounded we have $T_{1}(t)=$ $=\exp \left(t A_{1}\right)$ and $a\left(T_{1}(t)\right)=\exp \left(t \sigma\left(A_{1}\right)\right)$. Therefore by the remark following Prop.l.l the spectral bound $s\left(A_{1}\right)$ coincides with the growth bound $w\left(T_{1}\right)$ and we have the upper estimate. The lower estimate is obtained by applying the same reasoning to $-\mathrm{A}_{1}$ which generates the semigroup ( $\left.\mathrm{T}_{1}(\mathrm{t})^{-1}\right) \mathrm{t} \supseteq 0$ on $\mathrm{E}_{1}$.

It is clear from Examples 1.3, 1.4 that no norm estimates for $\left(T_{2}(t)\right)$ t $\quad$ can be obtained from the location of $\sigma_{2}$. Only by adding appropriate hypotheses we will achieve spectral decompositions admitting norm estimates on both components (see A-III,6.6).
Another way of obtaining such norm estimates is by constructing spectral decompositions starting from a semigroup operator $T\left(t_{0}\right)$ (instead of $A$ resp. $R(\lambda, A)$, as in Thm.3.3).

Corollary 3.5. If $\sigma\left(T\left(t_{0}\right)\right)={ }^{\tau}{ }_{1} U{ }^{\tau}{ }_{2}$ for two non-empty, closed, disjoint sets ${ }^{\tau} 1$, ${ }_{2}$ and if $p$ is the spectral projection correspon-
ding to $T\left(t_{0}\right)$ and ${ }^{\tau} 1,{ }_{2}$, , then $\sigma(A)$ splits into closed subsets ${ }_{1}, \sigma_{2}$ and $P$ is the corresponding spectral projection for $T$ and $\sigma_{1}, \sigma_{2}$.

Proof. The spectral projection $p$ of $T\left(t_{o}\right)$ is obtained by integrating $R\left(\lambda, T\left(t_{0}\right)\right)$ (see e.g. 「Dunford-Schwartz (1958), Section VII. 3 I). Since every $T(t), t \geqslant 0$, commutes with $T\left(t_{0}\right)$ it must conmute with $R\left({ }^{2}, T\left(t_{0}\right)\right)$, hence with $P$. The statement on the decomposition $\sigma(A)=\sigma_{1} \quad{ }^{\prime} \sigma_{2}$ follows from the spectral Inclusion Theorem 6.2 below.

This decomposition can be applied as follows to the study of the asymptotic behavior of $T$ : In the situation of Cor. 3.5 assume
$$
\sup \left\{|\lambda|: \lambda \in \tau_{2}\right\} < a <\inf \left\{|\lambda|: \lambda \in \tau_{1}\right\}
$$

If we set $\beta:=(\log \alpha) / t_{0}$ and use [pazy (1984), Chap. 1, Thm. 6.5] we obtain $\omega\left(T_{2}\right)<\beta$ and $\omega\left(T_{1}^{-1}\right)<\beta$ by prop.l.l. Therefore we have constants m, M m l such that
$$
\begin{array}{ll}
\|T(t) f\| & \leqslant M \cdot e^{B t}\|f\| \\
\|T(t) f\| & \text { for } f \in E_{2}, \\
\left\|t e^{\beta t}\right\| & \text { for } f \in E_{1} .
\end{array}
$$

As nice as they might look results of this type are unsatisfactory : we need information on the semigroup in order to estimate its asymptotic behavior. In Chapter IV we will try to obtain such results by exploiting information about the generator only.

\subsection*{3.6 Isolated singularities and poles.}

In case that $\lambda_{o}$ is an isolated point of o(A) the holomorphic function $\dot{\lambda} \rightarrow R(\lambda, A)$ can be expanded as a Laurent series
$R(\lambda, A)=\sum_{n=-\infty}^{+\infty} U_{n}\left(\lambda-\lambda_{0} j^{n}\right.$ for $0 \leqslant\left|\lambda-\lambda_{0}\right|<\delta$ and some $\theta>0$. The coefficients $U_{n}$ are bounded linear operators given by
(3.1) $U_{n}=\frac{1}{2 \pi i} \int_{\Gamma}\left(z-\lambda_{0}\right)^{-(n+1)} R(z, A) d z \quad, \quad n \in \mathbb{Z}$,
where $r=\left\{z \in \mathbb{C}:\left|z-\lambda_{0}\right|=8 / 2\right\}$.
The coefficient $U_{-1}$ is the spectral projection corresponding to the spectral set $\left\{\lambda_{0}\right\}$ (see Def.3.1), it is called the residue of R(*,A) at $A_{0}$, and will be denoted by $F$. From (3.1) one deduces
(3.2) $U_{-(n+1)}=\left(A-\lambda_{0}\right)^{n}{ }^{n} P$ and
$$
U_{-(n+1)} \cdot U_{-(m+1)}=U_{-(n+m+1)} \text { for } n, m \geq 0 \text {. }
$$

If there exists $k>0$ such that $v_{-k} \neq 0$ while $v_{-n}=0$ for all $n>k$ the point $\lambda_{o}$ is called a pole of $R(\cdot, A)$ of order $k$. In view of (3.2) this is true if $\mathrm{J}_{-\mathrm{k}} \neq 0$ and $\mathrm{U}_{-(k+1)}=0$. In this case one can retrieve $\mathrm{U}_{\mathrm{z}}$ as
(3.3) $\mathrm{J}_{-\mathrm{k}} \Rightarrow \lim _{\lambda \rightarrow \lambda_{O}}\left(\lambda-\lambda_{\mathrm{O}}\right)_{\mathrm{R}}(\lambda, A)$.

The dimension of $P E$ (i.e., the dimension of the spectral subspace corresponding to $\left\{\lambda_{0}\right\}$ ) is called algebraic multiplicity ma of $\lambda_{o}$, while the geometfic multiplicity is $m_{g}:=\operatorname{dim} k e r\left(\lambda_{o}-A\right)$. In case $m_{a}=1$ we call $\lambda_{o}$ an algebraically simple pole. If $k$ is the pole order $(k=m$ in case of an essential singularity) we have
(3.4) $\max \left\{m_{\mathrm{g}}, \mathrm{k}\right\} \check{\mathrm{m}_{\mathrm{a}}} \leqq \mathrm{k} \cdot \mathrm{m}_{\mathrm{g}}$,
where $\infty \cdot 0=$. These inequalities yield the following implications: - $m_{a}<\infty$ if and only if $\lambda_{o}$ is a pole with $m_{g}<\infty$, $\cdots$ if $\lambda_{o}$ is a pole with order $k$, then $\lambda_{\rho} \in \operatorname{Po}(A)$ and $P E=\operatorname{ker}\left(\lambda_{0}-A\right)^{k}$.

If $A$ has compact resolvent then every point of $\sigma(A)$ is a pole of finite algebraic multiplicity. This is a consequence of Prop. 2.5 (iii) and the well-known Riesz-schauder Theory for compact operators (see [Dunford-Schwartz (1958), VII.4.5!).
3.7. The essential spectrum.

For $T \in L(E)$ the Fredholm domain $P_{F}(T)$ is
(3.5) $\rho_{F}(T):=\{\lambda \in \mathbb{C}: \lambda \rightarrow T$ is a Fredholm operator $\}$
$=\{\lambda \in \mathbb{C}: \operatorname{ker}(\lambda-T)$ and $E / i m(\lambda-T)$
are finite dimensional\} .
An equivalent characterization of $\rho_{F}(T)$ is obtained through the Calkin algebra $L(E) / K(E)$, where $K(E)$ stands for the closed ideal of all compact operators. In fact, $\rho_{\mathrm{F}}(T)$ coincides with the resolvent set of the canonical image of $T$ in the calkin algebra. The complement of $\rho_{F}(T)$ is called essential spectrum of $T$ and denoted by $\sigma_{e s s}(T)$. The corresponding spectral radius, called essential spectral radius, satisfies
$$
\begin{equation*}
r_{e s s}(T):=\sup \left\{|\lambda|: \lambda \in \sigma_{\operatorname{ess}}(T)\right\}=\lim _{n \rightarrow \infty}\left\|T^{n}\right\|_{\mathrm{ess}}^{1 / n} \tag{3.6}
\end{equation*}
$$
where $\|T\|_{\text {ess }}=\operatorname{dist}(T, K(E)):=\inf \{\|T-K\|: K \in K(E)\}$ is the norm of $T$ in $L(E) / K(E)$.

For every compact operator $K$ we have $\|T-K\|_{\text {ess }}=\|T\|_{\text {ess }}$, hence
$$
\begin{equation*}
r_{e s s}(T-K)=r_{e s s}(T) \tag{3.7}
\end{equation*}
$$

A detailed analysis of $P_{F}(T)$ can be found in Section IV.5.6 of Kato (1966). In particular we recall that the poles of $\mathrm{R}(\cdot, \mathrm{T})$ with finite algebraic multiplicity belong to $\rho_{F}(T)$. Conversely, an element of the unbounded component of $\rho_{F}$ (T) either belongs to $\rho(T)$ or is a pole of finite algebraic multiplicity. Thus ress $(T)$ can be characterized as follows
(3.8) $r_{e s s}(T)$ is the smallest $r \in \mathbb{R}_{+}$such that every $\lambda \in \sigma(T)$,
$|\lambda|>r$ is a pole of finite algebraic multiplicity.
Now, if $T=(T(t))_{t \geq 0}$ is a strongly continuous semigroup then VIII.1, Lemma 4 of Dunford-Schwartz (1958) applied to the function $t * \log \|T(t)\|$ ess ensures that
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-085.jpg?height=78&width=1611&top_left_y=949&top_left_x=234) is well defined (possibly $-\infty$ ). By the definition of ${ }^{\text {es }}$ (T) and by (3.6) we have
$(3.10) \quad r_{\operatorname{ess}}(T(t))=\exp (t \cdot \omega \operatorname{ess}(T)), t \geqq 0$.

Obviously, wess $\leftrightarrows$ a and equality occurs if and only if $r_{e s s}(T(t))=r(T(t))$ for $t \geqq 0$.
If $\omega_{\text {ess }}<\omega$ there exists an eigenvalue $h$ of $T(t)$ satisfying $|\lambda|$ $=r(T(t))$, hence by Theorem 6.3 below there exists $\lambda_{1} \in \operatorname{Po}(A)$ such that $\operatorname{Re} \lambda_{1}=\omega$. Thus wess $\subset \omega$ implies $s(A)=\omega(T)$, i.e., we have
$$
\begin{equation*}
\omega(T)=\max \left\{\omega_{\operatorname{ess}}(T), \mathrm{s}(A)\right\} . \tag{3.11}
\end{equation*}
$$

As a final observation we point out that
(3.12) 山ess $^{(T)}=\omega_{\mathrm{ess}}(S)$
whenever $T$ is generated by $A$ and $S$ is generated by $A+K$ for some compact operator $K$ (see Prop. 2.8 and Prop. 2.9 of $B-I V$ ).

\section*{4. THE SPECTRUM OF INDUCED SEMIGROITP}

In the previous section we tried to decompose a semigroup into the direct sum of two hopefully simpler objects. Here we present other methods to reduce the complexity of a semigroup and its generator. Foming subspace or quotient semigroups as in $A-I, 3,2, A-I, 3.3$ are such methods. But also the constructions of new semigroups on canonically associated spaces such as the dual space, see $A-I, 3.4$, or the $F$-product, see $A-I, 3.6$, might be helpful. We review these construc-
tions under the spectral theoretical point of view and collect a number of technical properties for later use.

We start by studying the spectrum of subspace and quotient semigroups. To that purpose assume that the strongly continuous semigroup $T=(T(t))_{t \geqq 0}$ leaves invariant some closed subspace $N$ of the Banach space F . There are canonically induced semigroups ${ }^{T} \mid$ on $N$, resp. $T /$ on $E_{N}$ and their generators $A_{N}$, resp. $A$, are canonically obtained from the generator $A$ of $T$ (see $A-I$, section 3). The following example shows that the spectra of $A, A /$ and $A / m a y ~ d i f f e r ~$ quite drastically.

Example 4.1. As in the example in A-I, 3.3 we consider the translation semigroup on $E=L^{1}(M)$ and the invariant subspace $N:=\{f \in E: f(x)=0$ for $x \geqslant 1\}$. Then o(A) $=i \mathbb{R}$ but $\sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda) \leqq 0\}$. Next we take the translation invariant subspace $M:=\{f \in \mathbb{N}: f(x)=0$ for $0 \leq x \leqq l\}$ and obtain $\sigma\left(A_{\mid /}\right)=\emptyset$ for the generator $A_{Y / /} \quad$ of the quotient semigroup $T_{\mid /}$ (use the fact that ${ }^{\top} \mid /$ is nilpotent).

In the next proposition we collect the information on o(A) which in general can be obtained from the 'subspace spectrum' o(A) and the 'quotient spectrum' $\sigma(A$,$) .$

Proposition 4.2. Using the standard notations the following inclusions hold:
$$
\begin{equation*}
\rho_{+}(A) \quad[\quad[\rho(A) \Gamma \rho(A /)] \quad \rho(A) \quad[\rho(A \mid) \cap \rho(A,)] \cup[\rho(A \mid) \Gamma \sigma(A,)] \tag{iii}
\end{equation*}
$$
(i)
where $\rho_{+}(A)$ denotes the connected component of $\rho(A)$ which is unbounded to the right.

Proof. (i) Assume $\lambda \in \rho(A)$, i.e. ( $\lambda-A)$ is a bijection from $D(A)$ onto $E$. Since $N$ is T-invariant we have $D(A \mid)=D(A)$ in $N$ and $(\lambda-A) D(A \mid) \subset N$. If $(\lambda-A) D(A \mid)=N$ then $\left.R(\lambda, A) N=D(A)^{\prime}\right)$ and the induced operators $R(\lambda, A) \mid$, resp. $R(\lambda, A)$, are the inverses of $\left(\lambda-A_{\mid}\right)$, resp. $\left(\lambda-A_{7}\right)$. If $(\lambda-A) D\left(A_{\|}\right) \neq N$ then $\lambda \in \sigma(A \mid)$. In addition there exists $f \in D(A) \backslash \mathbb{N}$ such that $g:=(\lambda-A) f \in N$. Hence for $\hat{f}:=\hat{f}+\mathbb{N}, \hat{g}:=g+N \in E$, it follows that $(\lambda-A, \mid \hat{f}=\hat{g}=0$, i.e. $\lambda \in \sigma(A$,$) .$
(ii) Take $\lambda \in \rho(A \mid)$ п $\rho(A /)$. Then ( $\lambda-A$ ) is injective: ( $\lambda-A) f=0$ implies $(\lambda-A /) \hat{f}=0$, hence $\hat{f}=0$, i.e. $f \in N$ and therefore $f=0$.

In addition, (h-A) is surjective: For $g \in E$ there exists $f \in E /$ such that $(\lambda-A) f=g$, i.e. there exists $h \in N$ such that $(h-A) f-g=h=(k-A) k$ for some $k \in D(A \mid)$.
Therefore we obtain $(\lambda-A)(f-k)=g$.
(iii) The integral representation of the resolvent for $\lambda>$ w(T) (see $A-I$, Prop.1.11) shows that $R(\lambda, A) N=N$. By the power series expansion for holomorphic functions this extends to all $\lambda \in \mathcal{P}_{+}(A)$. Therefore the restriction $R(\lambda, A) \mid$ coincides with the resolvent $R(\lambda, A \mid)$. On the other hand $R(h, A)$, is well defined on $E /$ and satisfieg
$$
R(\lambda, A) /(f+\mathbb{N})=R(\lambda, A) f+N
$$
(use again the integral representation). This proves that
$$
\mathrm{R}(\lambda, \mathrm{~A}) /=\mathrm{R}(\lambda, A /)
$$

Corollary 4.3. Under the above assumptions take a point $\mu$ in the closure of $P_{+}(A)$. Then
$$
\begin{equation*}
\mu \in \sigma(A) \text { if and only if } \mu \in \sigma(A \mid) \text { or } \mu \in \sigma(A,) \tag{i}
\end{equation*}
$$
```
1. is a pole of R(•,A) if and only if r is a pole of
``` $\mathrm{R}(\cdot, \mathrm{A} \mid)$ and of $\mathrm{R}(\cdot, \mathrm{A} /)$. In that case,
$$
\max (k \mid, k,) \leq k \quad s \quad k \mid+k
$$
for the respective pole orders.

Proof. (i) follows from Prop.4.2, inclusions (ii) and (iii).
(ii) By the previous assertion we may assume that for some $\delta>0$ the pointed disc
$$
\{\lambda \in \mathbb{C}: 0<|\lambda-\mu|<\delta\}
$$
is contained in $\rho(A) \cap \rho(A) \cap \rho(A$,$) Call U_{n}$ the coefficients of the Laurent expansion of $R(\cdot, A)$. Since $N$ is $R(\hbar, A)$-invariant for $\lambda \in \rho_{+}(A)$ the same holds for each $U_{n}$. With the obvious notations we have
$$
\mathrm{R}(\lambda, A)=\sum \mathrm{U}_{\mathrm{n}}(\lambda-\mu)^{\mathrm{n}}, R(\lambda, A)\left|=\sum \mathrm{U}_{\mathrm{n}}\right|^{(\lambda-\mu)^{\mathrm{n}}} \text { and } \mathrm{R}(\lambda, A) /=\sum_{\mathrm{n}} \quad(\lambda-\mu)^{n}
$$
which shows max $(k \mid, k /) \leqq k$. If $R(\cdot, A) \mid$ has a pole in $A$ of order
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-087.jpg?height=76&width=1617&top_left_y=2529&top_left_x=228) that $U_{-(m+1)^{E} \subset \mathbb{N}} \mathrm{if} R(., A)$ has a pole in $\mu$ of order $m$.

Therefore $U_{-(e+1)}{ }^{\circ} U_{-(m+1)}=0$. The relations (3.2) imply $\mathrm{U}_{-(m+1+1)}=0$, hence the pole order of $\mathrm{R}(., \mathrm{A})$ is dominated by $8+m$.
4.4. Spectrum of the adjoint semigroup.

We recall from $A-I, 3.4$ that to every strongly continuous semigroup $T=(T(t))_{t \geqslant 0}$ there corresponcs a strongly continuous adjoint semigroup $T^{*}=\left(T(t)^{*}\right) t \geq 0$ on the semigroup dual
$$
E^{*}=\left\{\phi \in E^{\top}: l \mathbf{i m}_{t \rightarrow \infty}\left\|T(t)^{r} \phi-\phi\right\|=0\right\}
$$

Its generator $A^{*}$ is the maximal restriction of the adjoint $A^{\prime}$ to E* . For these operators the spectra coincide, or more precisely
(i) $\sigma(T(t))=\sigma\left(T(t)^{\prime}\right)=\sigma\left(T(t)^{*}\right)$,
$$
\mathbb{R}_{\sigma}(T(t))=P_{\sigma}\left(T(t)^{\top}\right)=P_{\sigma}\left(T(t)^{*}\right) .
$$
$$
\begin{align*}
& \sigma(A)=\sigma\left(A^{\prime}\right)=\sigma\left(A^{*}\right), R_{\sigma}(A)=P_{\sigma}\left(A^{\prime}\right)=P_{\sigma}\left(A^{*}\right) \cdot  \tag{ii}\\
& s(A)=g\left(A^{*}\right), \mu(A)=\omega\left(A^{*}\right) . \tag{iii}
\end{align*}
$$

The left part of these equalities is either well known or has been stated in Prop. $2.2(i i)$. The first statment of (iii) follows from (ii), while the second is an immediate consequence of the estimate $\|T(t) *\|$ $\|T(t)\| \underline{\|} \leq M \cdot \| T(t) * \tilde{j}_{i}$ given in $A-I, 3.4$. As a sample for the remaining
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-088.jpg?height=53&width=1614&top_left_y=1564&top_left_x=221) and therefore $A \cdot i s$ invertible it follows from $A-I, 3.4$ that $A *$ is a bijection from $D\left(A^{*}\right)$ onto $E^{*}$. Conversely assume that $A^{*}$ is invertible. Then $A^{r}$ must be injective by the Proposition in $A-I, 3.4$. Moreover $A^{\prime}\left(D\left(A^{\prime}\right)\right)$ containg $A^{*}\left(D\left(A^{*}\right)\right)=E^{*}$ and is $\sigma^{\prime}\left(E^{\prime}, E\right)-$ dense in $E^{\prime}$. By standard duality arguments follows that $A$ is injective with dense image. We show that $A(D(A))$ is closed: For $f \in D(A)$ choose $\phi \in D(A$,$) such that \|\phi\|_{i} \leqq 1$ and $|<f, \phi>| \geqq \frac{1}{2}\|f\|$. Then
$$
\begin{aligned}
\left\|\left(A^{*}\right)^{-1}\right\|\|A f\| & \geq\left\|_{\|}\left(A^{*}\right)^{-1}\right\| A^{1}\langle A f, \phi\rangle\left|\geqq\left|\left\langle A f,\left(A^{*}\right)^{-1} \phi\right\rangle\right|\right. \\
& \approx \left\lvert\,\langle E, \phi>| \geqq \frac{1}{2}\|£\| .\right.
\end{aligned}
$$
hence
$$
\|A f\| \geqq \frac{1}{2}\left\|\left(A^{*}\right)^{-1}\right\|^{-1}\|f\|
$$
and $A(D(A))$ is closed since $A$ is closed.

\subsection*{4.5 Spectrum of the F-product semigroup.}

As stated in $A-T, 3.6$ the F-product semigroup $T_{F}=\left(T_{F}(t)\right) t_{t \geqslant 0}$ on $E_{F}^{\top}$ of a strongly continuous semigroup $T$ on $E$ serves to convert sequences in $E$ into points in $E_{F}^{\top}$. In particular it can be ured to
convert approximate eigenvectors of the generator $A$ into eigenvectors of $A_{F}$.

Proposition. Let $A$ be the generator of a strongly continuous semigroup. Then the generator $A_{F}$ of the $F$-product semigroup satisfies
(i) $A \sigma(A)=A^{\sigma}\left(A_{F}\right)=\operatorname{Po}\left(A_{F}\right)$.
(ii) $\sigma(A)=\sigma\left(A_{f}\right)$.

Remark: In case $A$ is bounded then $A$ is a generator and $E_{F}^{T}=E_{F}$ (cf. A-I, 3.6). Thus the proposition applies to bounded linear operators and their canonical extensions to the $F$-product $E_{F}$.

Proof of the proposition. (i) The inclusion $\operatorname{Po}\left(A_{F}\right) \subset A O\left(A_{f}\right)$ holds trivially. We show that $A \sigma\left(A_{F}\right) \subset A \sigma(A): T a k e \quad h \in A \sigma\left(A_{F}\right)$ and an associated approximate eigenvector $\left(\hat{f}^{m m}\right) n \in \mathbb{N}$, i.e. $\hat{f}^{m m} \in D\left(A_{F}\right)$, $\left\|\hat{f}^{m}\right\|=1$ and $\left(\lambda-A_{F}\right) \hat{f}^{m} \rightarrow 0$ as $m \rightarrow \infty$. By the considerations in $A-I, 3.6$ we can represent each $\hat{f}^{m}$ as a normalized sequence $\left(f_{n}^{[m}\right) n \in \mathbb{N}$ in $D(A)$ such that
$$
\lim _{m^{\prime} \rightarrow \infty} 1 \mathrm{imsup} \mathrm{sin}_{\mathrm{n} \rightarrow \infty}\left\|(\lambda-\mathrm{A}) \mathrm{f}_{\mathrm{n}}^{\mathrm{m}}\right\|=0 .
$$

Therefore we can find a sequence $g_{k}=f_{k}^{m(k)}$ satisfying
$$
\lim _{k \rightarrow \infty}\left\|(\lambda-A) g_{k}\right\|=0,
$$
i.e. $\lambda \in A \sigma(A)$.

Finally we show $A \sigma(A)=P \sigma\left(A_{F}\right)$ for $\lambda \in A \sigma(A)$ take a corresponding approximate eigenvector ( $f_{n}$ ). By $A-I$ (3.2) we have
$$
\begin{aligned}
\left\|T(t) f_{n}-f_{n}\right\| & \leqslant\left\|T(t) f_{n}-e^{\lambda t_{f}}\right\|+\mid e^{\lambda t}-1 \\
& \left.=\| \int_{0}^{t} e^{\lambda(t-s)} T(s)(\lambda-A) f_{n} d s|j+| e^{\lambda t}-1\right]
\end{aligned}
$$
which converges to zero uniformly in $n$ as $t \rightarrow 0$, i.e. $\left(f_{n}\right) \in m^{\top}(E)$. By the characterization of $D\left(A_{F}\right)$ given in $A-E, 3.6$ it follows that
$$
\hat{E}:=\left(f_{n}\right)+c_{F}(E) \in D\left(A_{F}\right),
$$
and $A_{f} \hat{f}=\lambda \hat{f}$, i.e. $\lambda \in \operatorname{Po}\left(A_{F}\right)$.
(ii) The inclusion $\sigma(A) \in \sigma\left(A_{F}\right)$ follows from (i) and the inclusion $\operatorname{Ro}(A)=\operatorname{Ro}\left(A_{F}\right): \operatorname{For} \lambda \in \operatorname{Ro}(A)$ choose $f \in E$ such that $\|(\lambda-A) g-f\| \geq 1$ for every $g \in D(A)$. Then $\left\|\left(\lambda \sim A_{F}\right) \hat{g}-\hat{f}\right\| \geq 1$ for every $\hat{g} \in D\left(A_{F}\right)$ and $\hat{f}=(f, f, \ldots)+C_{F}(E)$. Therefore $\lambda \in R o\left(A_{F}\right)$. We now show $\rho(A)=\rho\left(A_{F}\right)$ : Assume $\lambda \in \rho(A)$. By (i) $\left(\lambda-A_{F}\right)$ has to be injective. Choose $\hat{\mathrm{E}}=\left(\mathrm{f}_{1}, \mathrm{f}_{2}, \ldots\right)+\mathrm{C}_{\mathrm{F}}(\mathrm{E})$ such that $\left(f_{n}\right) \in m^{\top}(E)$. Then $\left(R(\lambda, A) f_{n}\right) \in m^{\top}(E)$ and $\left(\lambda-A_{F}\right)\left(\left(R(\lambda, A) f_{n}\right)+c_{F}(E)\right)$ $=\left(E_{n}\right)+C_{F}(E)$, i.e., $\left(\lambda-A_{F}\right)$ is surjective and $\lambda \in P\left(A_{F}\right)$.

Applying the proposition to a single operator $T(t)$ we obtain $A \sigma(T(t))=P \sigma(T(t) F)$. Note that in general Ao(T(t)) $\neq P \sigma(T f(t))$ (see the Examples 1.3 and 1.4 in combination with Theorem 6.3).

\section*{5. THE SPECTRJM OF PERIODIC SEMIGROUPS}

In this section we determine the spectrum of a particularly simple class of strongly continuous semigroups and thereby achieve a rather complete description of the semigroup itself. Besides being nice and simple these semigroups gain their importance as building blocks for the general theory.

Definition 5.1. A strongly continuous semigroup $T=(T(t))$ t $\quad$ on $a$ Banach space $E$ is called periodic if $T\left(t_{0}\right)=I d$ for some $t_{0}>0$. The period $t$ of $T$ is obtained as $\left.T:=i n d i t_{o}>0: T\left(t_{0}\right)=I d\right)$.

We immediately observe that periodic semigroups are groups with inverses $T(t)^{-1}=T(n t-t)$ for $0 \leqq t \leqq n t, \tau$ the period of $T$. Moreover, they are bounded, hence the growth bound is zero and $\sigma(A) \subset \mathbf{i} \mathbb{R}$.

Lemma 5.2. Let $T$ be a strongly continuous semigroup with period $r>0$ and generator $A$. Then
$$
\begin{gather*}
\sigma(A) c 2 \pi i / t \cdot Z, \text { and } \\
R(\mu, A)=\left(1-e^{-\mu t}\right)^{-1} \int_{0}^{\tau} e^{-\mu s_{T}} T(s) d s \tag{5.1}
\end{gather*}
$$
for $\mu \not 2 \pi i / T \cdot \boldsymbol{Z}$.

Proof. From the basic identities $A-I,(3,1)$ and $A-I,(3.2)$ for $t=r$ r it follows that ( $u-A$ ) hag a left and right inverse if $\mu \neq 2 \pi i n / \tau$, $n \in \mathbb{Z}$, and that the inverse is given by the above expression.

The representation of $R(u, A)$ given in $A-I, P r o p .1 . l l$ shows that the resolvent of the generator of a periodic semigroup is a meromorphic function having only poles of order one and the residues
$$
P_{n}:=\lim _{\mu \rightarrow \mu_{\mathrm{n}}}\left(\mu \rightarrow \mu_{\mathrm{n}}\right) R(\mu, A) \quad \text { in } \quad H_{n}:=2 \pi i n / t, n \in \mathbb{Z} \text {, are }
$$
$$
\begin{equation*}
P_{n}=t^{-l} \int_{0}^{t} \exp \left(-\mu_{n} s\right) T(s) d s \tag{5,2}
\end{equation*}
$$

Moreover, it follows that the spectrum of $A$ consists of eigenvalues only and each $P_{n}$ is the spectral projection belonging to $H_{n}$ (see
3.6). Another way of looking at $P_{n}$ is given by saying that $P_{n}$ is the n-th Fourier coefficient of the $\tau$-periodic function $s \rightarrow T(s)$ From this it follows that no non-zero $\phi \in \mathrm{E}^{\prime}$ vanishes on all $\mathrm{P}_{\mathrm{n}} \mathrm{E}$ simultaneously. By the Hahn-Banach theorem we conclude that spann $U_{n \in f} P_{n} E$ is dence in $E$.
Since $P_{n} E \subset D(A)$ we obtain from $A-I,(3.1)$ that
$$
\begin{equation*}
A P_{n} f=\mu_{n} P_{n} f \tag{5.3}
\end{equation*}
$$
for every $f \in E, n \in \mathbb{Z}$. This and $A-I,(3,2)$ imply
(5.4) $T(t) P_{n} f=\exp \left(\mu_{n} t\right) \cdot P_{n} f$
for every $t \geqslant 0$. Therefore $\mu_{n}$ is an eigenvalue of $A$ and $\exp \left(\mu_{n} t\right)$ is an eigenvalue of $T(t)$ if and only if $P_{n} \frac{i}{i} 0$. In that case, $P_{n} E$ is the corresponding eigenspace and we have the following 1 emme.

Lemma 5.3. For a $\quad$ mperiodic semigroup $T$ we take $\mathrm{k}_{\mathrm{n}}:=2 \pi i n / t$, $n \in \mathbb{Z}$ and consider
$$
P_{n}:=\tau^{-1} \cdot \int_{0}^{t} \exp \left(-\mu_{n} s\right) T(s) d s .
$$

Then the following assertions are equivalent:
(a) $\mathrm{P}_{\mathrm{n}} \neq 0$
(b) $\mu_{n} \in P_{\sigma}(A)$
(c) $\exp \left(\mu_{n} t\right) \in P_{\sigma}(T(t))$ for every $t>0$.

The action of $A$, resp. $T(t)$ on the subspaces $P_{n} E, n \in \mathbb{Z}$, is determined by (5.3), resp. (5.4). Moreover,
$$
\begin{aligned}
P_{m} P_{n} f & =t^{-l} \cdot \int_{0}^{T} \exp \left(-_{m} s\right) T(s) P_{n} f d s= \\
& =r^{-1} \cdot \int_{0}^{T} \exp \left(\left(_{n} n^{-\mu_{m}}\right) s\right) P_{n} f d s=0
\end{aligned}
$$
for $n \neq m$, i.e. the subspaces $P_{n} E$ are "orthogonal". Since their union is total in $E$ one expects to be able to extend the representations (5.3) and (5.4) of $A$ and $T(t)$. This is possible if
$$
\Gamma_{-\infty}^{+\infty} \mathrm{P}_{\mathrm{n}}=I \mathrm{~d}
$$
where the series should be summable for the strong operator topology. Unfortunately this is false in general since the family of projections
$$
Q_{H}:=\sum_{n \in H} P_{n}
$$
where $H$ runs through all finite subsets of $\mathbb{Z}$, may be unbounded (see the example below). Nevertheless the following is true.

Theorem 5.4. Let $T=(T(t))_{t \geqq 0}$ be a $T$-periodic semigroup on a Banach space $E$ with generator $A$ and associated spectral projections
$\mathrm{P}_{\mathrm{n}}:=\tau^{-1} \cdot \int_{0}^{\tau} \exp \left(-\mu_{\mathrm{n}} \mathrm{s}\right) \mathrm{T}(\mathrm{s}) \mathrm{ds}, \mu_{\mathrm{n}}:=2 \pi i n / \tau, \mathrm{n} \in \mathbb{Z}$.
For every $f \in D(A)$ one has $f=\sum_{-\infty}^{+\infty} P_{n} f$ and therefore
$$
\begin{align*}
& T(t) f=\sum_{-\infty}^{+\infty} \exp \left(\mu_{n} t\right) P_{n} f \quad \text { if } f \in D(A) \text {, }  \tag{i}\\
& A f=\sum_{-\infty}^{+\infty} \mu_{n} P_{n}{ }^{f} \quad \text { if } f \in D\left(A^{2}\right) \text {. } \tag{ii}
\end{align*}
$$

Proof. It suffices to prove the first statement. Then (i) and (ii) follow by (5,3) and (5.4).
We assume $T=2 \pi$ and show first that $\sum_{d^{+\infty}}^{+\infty} P_{n} f$ is summable for $f \in D(A): F O r g$ : $f=A f$ we obtain $P_{n} g=P_{n} A f=A P_{n} f=i n P_{n} f$. Take $H$ to be a finite subset of $Z$ \{ $\{0\}$ and $\phi \in E^{\prime}$. Then
$$
\begin{aligned}
\left|\sum_{n \in H}\left\langle P_{n} f, \phi\right\rangle\right| & =\mid \sum_{n \in H}(i n)^{-1}\left\langle P_{n} g, \phi>\vdots\right. \\
& \cong\left(\sum_{n \in H} n^{-2}\right)^{1 / 2}\left(\left.\sum_{n \in H}\left\langle\leqslant p_{n} g, \phi\right\rangle\right|^{2}\right)^{1 / 2} .
\end{aligned}
$$

From Bescel's inequality we obtain for the second factor
$$
\begin{aligned}
\Sigma_{n \in H}\left|\left\langle P_{n} g, \phi\right\rangle\right|^{2} & \leqq 1 / 2 \pi \cdot \int_{0}^{2 \pi}|\langle T(s) g, \phi\rangle|^{2} \mathrm{~d} s \\
& \leqq\|\phi\|^{2} \cdot 1 / 2 \pi \cdot \int_{0}^{2 \pi}\|T(s) \mathrm{g}\|^{2} \mathrm{ds}
\end{aligned}
$$

With the constant $c:=\left(1 / 2 \pi \cdot \int_{0}^{2 \pi}\|T(s) g\|^{2} d s\right)^{1 / 2}$ we obtain
$$
\left\|\sum_{n \in H} P_{n} f\right\|_{f}^{\prime} c\left(\Gamma_{n \in H} n^{-2,1 / 2}\right.
$$
for every finite subset $H$ of $\mathbb{Z}$, i.e. $\sum_{m=1}^{+\infty} P_{n} f$ is summable.

Next we set $h:=L_{-\infty}^{+\infty} P_{n} f$ and observe that for every $\phi^{t} \in E^{t}$ the Fourier coefficients of the continuous, t-periodic functions
$$
s \rightarrow\langle T(s) h, \phi\rangle \text { and } s+\left\langle T(s) f_{r} \phi\right\rangle
$$
coincide. Therefore these functions are identical for $s \geqslant 0$ and in particular for $s=0$, i.e. $\langle h, \phi\rangle=\langle f, \phi\rangle$. By the Hahn-Banach Theorem we obtain $f=h$.

The above theorem contains rather precise information on periodic semigroups. In particular, it characterizes periodic semigroups by the fact that $\sigma(A)$ is contained in $i \alpha z$ for some $a \in \mathbb{R}$ and the eigenw functions of $A$ form a total subset of $E$.

If we suppose in addition that a periodic semigroup has a bounded generator it follows that the spectrum of its generator is bounded.

Therefore only a finite number of spectral projections $P_{n}$ are distinct from 0 and we have the following characterization.

Corollary 5.5. Let $T=(T(t))_{t \notin 0}$ be a semigroup with bounded generator on some Banach space $E$. This semigroup has period $t / k$ for some $k \in \mathbb{N}$ if and only if there exist finitely many pairwise orthogonal projections $P_{n},-m \leqq n \subseteq m, P_{-m} \neq 0$ or $P_{m} \neq 0$, such that
$$
\begin{equation*}
\sum_{m \mathrm{~m}}^{+\mathrm{m}} P_{\mathrm{n}}=I \mathrm{~d}, \tag{i}
\end{equation*}
$$
$$
\begin{equation*}
T(t)=\Gamma_{-m}^{+m} \exp (2 \pi \operatorname{int} / T) P_{n}, \tag{ii}
\end{equation*}
$$
$$
\begin{equation*}
A=\sum_{-m}^{+m}(2 \pi i n / t) P_{n} \tag{iii}
\end{equation*}
$$

Example 5.6. From A-I,2.5 we recall briefly the rotation group $R_{\tau}(t) f(z):=f(\exp (2 \pi i n t / \tau) \cdot z) \quad o n \quad E=C(\Gamma)$, resp. $E=L^{p}(\Gamma, m)$ for $1 \leqq p<\infty$. The spectrum of the generator
$$
\begin{aligned}
A f(z) & =(2 \pi i / \tau) z \cdot f^{\prime}(z) \\
\sigma(A) & =(2 \pi i / \tau) \cdot \not Z
\end{aligned}
$$

The eigenfunctions $E_{n}(z):=z^{n}$ yield the projections
$$
\left.\begin{array}{rl}
P_{n} & =(1 / 2 \pi i) \cdot E_{-}(n+1) \\
P_{n} f(z) & =(1 / 2 \pi i) \cdot\left(\int_{\Gamma} f(w) w^{-}(n+1) d w\right.
\end{array}\right) \cdot z^{n} .
$$

It is left as an exercise to compute the norms of $Q_{m}:=\Gamma_{m m}^{+m} P_{n}$ in $L^{P}(\Gamma)$ for various $p$ and then check the assertions of Theorem 5.4. clearly, this proves some classical convergence theorems for Fourier series (compare Davies (1980), Chap.8.1).

\section*{6. SPECTRAL MAPPING THEOREMS}

We now return to the question posed in the introduction to this chapter: In which form and under which conditions is it true that the spectrum o(T(t)) of the semigroup operators is obtained - via the exponential map - from the spectrum $\sigma(A)$ of the generator, or briefly
$$
\sigma(T(t))=\exp (t \sigma(A)) ?
$$

This and similar statements will be called spectral mapping theorems for the semigroup $T=(T(t))$ ta0 and its generator $A$.

In addition, we saw in Prop. l.l that the validity of such a spectral mapping theorem implies
$$
s(A)=i(A)
$$
for the spectral- and growth bounds and therefore guarantees that the location of the spectrum of $A$ determines the asymptotic behavior of $T$. As we have seen in Examples 1.3 and 1.4 the last statement does not hold in general. We therefore present a detailed analysis, where and why it fails and what additional assumptions are needed for its validity. Before doing so we have another look at the examples.

\subsection*{6.1 The counterexamples revisited.}
(iv) The Example 1.3 can be strengthend in order to yield a semigroup $T=(T(t)) t \geqslant 0$ with generator $A$ such that $\sigma(A)=\theta$ but $\|T(t)\|=r(T(t))=1$ for $t \geq 0$, i.e. $s(A)=-\infty$, $\omega=0$ and $s(A) \leqslant \omega:$

Take the translation semigroup on the Banach space $E:=C_{o}\left(\mathbb{R}_{+}\right) \cap L^{1}\left(\mathbb{R}_{+}, e^{x^{2}} d x\right)$ with $\|f\|:=\sup \left\{|f(x)|: x \in \mathbb{R}_{+}\right\}+\int_{0}^{\infty}|f(x)| e^{x^{2}} d x$ (see Greiner-Voigt-Wolff (1981)).
(v) Another modification of Example 1.3 yields a group $T=(T(t))_{t \in \mathbb{R}}$ satisfying $s(A)<\omega$. Therefore the spectral mapping theorem does not hold (see Wolff (1981)).

The next few theorems form the core of this chapter. We show that only one part of the spectrum and one inclusion is responsible for the failure of the spectral mapping theorem. The usefulness of this detailed analysis will become clear in the subsequent chapter on stability and asymptotics.
6.2. Spectral Inclusion Theorem. Let $A$ be the generator of a strongly continuous semigroup $T=(T(t))_{t ? 0}$ on some Banach space . . Then
$$
\exp (t o(A))=o(T(t)) \text { for } t \geqq 0
$$

More precisely we have the following inclusions:
$$
\begin{equation*}
\exp (t \cdot \operatorname{Po}(A)) \quad \therefore \quad \operatorname{Po}(T(t)) \tag{6,1}
\end{equation*}
$$
$$
(6.2) \exp (t \cdot \operatorname{Ao}(A)) \subset A \sigma(T(t))
$$
$$
\text { (6.3) } \exp (t \cdot \operatorname{Ro}(\mathrm{~A}))=\operatorname{Ro}(\mathrm{T}(\mathrm{t}))
$$

Proof. Since $e^{\lambda t}-T(t)=(\lambda-A) \int_{0}^{t} e^{\lambda(t-s)} T(s)$ ds (see $\left.A-I,(3,1)\right)$ it follows that ( $\left.e^{\lambda t}-T(t)\right)$ is not bijective if $(\lambda-A)$ fails to be bijective, which proves the main inclusion.
The inclusion (6.1) becomes evident from the following proof of (6.2): Take $\lambda \in A o(A)$ and an associated approximate eigenvector $\left(f_{n}\right) \subset D(A)$. Then
$$
g_{n}:=e^{\lambda t} f_{n}-T(t) f_{n}=\int_{0}^{t} e^{\lambda(t-s)} T(s)(\lambda-A) f_{n} d s
$$
converges to zero as $n \rightarrow \infty$. Consequently, $e^{\lambda t} \in A \sigma(T(t))$ and in fact, the same approximate eigenvector ( $f_{n}$ ) does the job for all $t \geq 0$.

For the proof of (6,3) we take $\lambda \in \operatorname{Ro}(A)$ and observe that
$\left(e^{\lambda t}-T(t)\right) f=(\lambda-A)\left(\int_{0}^{t} e^{\lambda(t-s)} T(s) f d s\right) \epsilon(\lambda-A) D(A)$
for every $f \in E$.

As we know from the Examples 6.1, the converse inclusions do not hold in general, i.e., not every spectral value of a semigroup operator $T(t)$ comes - via the exponential map - from a spectral value of the generator. But at least this is true for some important parts of the spectrum.
6.3 Spectral Mapping Theorem for Point and Residual Spectrum. Let A be the generator of a strongly continuous semigroup $T=(T)(t){ }_{t \geqslant 0}$. Then
$\exp (t \cdot \operatorname{Po}(A))=\operatorname{Po}(T(t))\{\{0\}$,
(6.5) $\exp (t \cdot \operatorname{Ro}(A))=\operatorname{Ro}(T(t)) \quad[0\}$, for $t \geqq 0$.

Proof. For the proof of (6.4) take $t_{0}>0$ and $0 \geq \lambda \in \operatorname{Po}\left(T\left(t_{0}\right)\right)$. After rescaling the semigroup $T=(T(t))$ tig to the semigroup (exp (-t. $\left.\left.\log \lambda / t_{o}\right) T(t)\right)_{t \geq 0}$ we may assume $h=1$. Then the cloged, T-invariant subspace
$$
G:=\left\{g \in E: T\left(t_{0}\right) g=g\right\}
$$
is non trivial. The restrictod semigroup $T_{\text {; }}$ is periodic with period $\tau \leqq t_{o}$ and the spectrum of its generator $A^{\prime} \mid$ contains at least one eigenvalue $\nu=2 \pi i n / t_{o}$ for some $n \in Z$ (see Lemma 5.3) . Since every eigenvalue of $A \mid$ is an eigenvalue of $A$ we obtain that $1 \in \exp \left(t_{0} \cdot P o(A)\right)$. The converse inclusion has been proved in (6.1). In fact, even more can be said: Let $g \in G$ be an eigenvector of $T$ ( $\mathrm{t}_{\mathrm{o}}$ ) corresponding to the eigenvalue $\lambda=1$. For each $n \in \mathbb{Z}$ define
$$
g_{n}:=P_{n} g=1 / t_{0} \cdot \int_{0}^{t_{0}} \operatorname{oxp}\left(-2 \pi i n s / t_{0}\right) T(s) g d s \in G
$$
as in section 5. Then $g_{n}$ is an eigenvector of $A \mid$, hence of $A$ with eigenvalue $2 \pi i n / t_{0}$ as soon as $g_{n}$ is distinct from zero. Since $D(A \mid)$ is dence in $G$ it follows from Theorem 5.4 that this holds for at least one $n \in \mathbb{Z}$. From the proof of (6.1) we know that this $g_{n}$ is in fact an eigenvector for each $T(t), t \geqslant 0$.
Since $\operatorname{Ro}(A)=\operatorname{Po}(A *)$ and $\operatorname{Ro}(T(t))=\operatorname{Po(T(t)*)}(s e e 4.4)$ the assertion (6.5) follows from (6.4).

Note that the proof is essentially an application of the structure theorem for periodic semigroups as given in Thm.5.4. The information gained there can be reformulated into statements on the eigenspaces of $A$ and $T(t)$.

Corollary 6.4. For the eigenspaces of the generator A. resp. of the semigroup operators $T(t), t * 0$, the following holds:
$$
\begin{equation*}
\operatorname{ker}(\mu-A)=\prod_{s \geq 0}^{\cap} \operatorname{ker}\left(e^{\mu s}-T(s)\right), \tag{i}
\end{equation*}
$$
$$
\begin{equation*}
\operatorname{ker}\left(e^{\mu t}-T(t)\right)=\overline{\operatorname{span}}_{n \in I} \operatorname{ker}(\mu+2 \pi i n / t-A), \mu \in \mathcal{C} \tag{ii}
\end{equation*}
$$

Remark that analogous statements are valid for ker (u - A') and $\operatorname{ker}\left(e^{\mu t}-T(t)^{\prime}\right) \quad$ if we take in (ii) the $\sigma\left(E^{\prime}, E\right)$-closure.

Without proof (see Greiner (1981), Prop.l.10) we add another corollary showing that poles of the resolvent of $T(t)$ correspond necessarily to poles of the resolvent of the generator. Again the converse is not true as shown by Example 5.6.

Corollary 6.5. Assume that $\epsilon^{\mu t}$ is a pole of order $k$ of $R(*, T(t))$ with residue $P$ and $Q$ as the k-th coefficient of the Laurent series. Then
(i) $\quad+2 \pi i n / t$ is a pole of $k(., A)$ of order $\leqq k$ for every $n \in \mathbb{Z}$,
(ii) the residues $P_{n}$ in $\mu+2 \pi i n / t$ yield $P E=\overline{\operatorname{span}} n_{n \in} P_{n} E$,
(iii) the k-th coefficient of the Laurent series of R(., A) at $\mu+2 \pi i n / t$ is $Q_{n}=\left(t \cdot e^{\mu t}\right) 1-k \cdot Q^{0}(1 / t) \int_{0}^{t} e^{-(\mu+2 \pi i n / t) s_{T}(s)} d s$.

From Theorem 6.2 and 6.3 it follows that the approximate point apectrum is the trouble maker in the sense that not every approximate eigenvalue of $T(t)$ corresponds to an approximate eigenvalue of the generator A. Since nothing more can be said in general we now look for additional hypotheses on the semigroup implying the spectral mapping theorem.

As a simple example we assume $T\left(t_{0}\right)$ to be compact for some $t_{o}>0$. Then $o(T(t)),\{0\}=P o(T(t))$ \{ $\{0\}$ for $t \geq t_{o}$ and the spectral mapping theorem is valid by (6.4). A different class of semigroups verifying the spectral mapping theorem is given by the uniformly continuous semigroups (compare Cor.1.2) .
Both cases, and many more, are included in the following result.

\subsection*{6.6 Spectral Mapping Theorem for Eventually Norm Continuous} semigroups.
Let $T=(T(t))_{t \geqslant 0}$ be an eventually norm continuous semigroup with generator A. Then the spectral mapping theorem is valid, i.e.
$$
\begin{equation*}
\sigma(T(t)) \backslash\{0\} \neq e^{t \cdot \sigma(A)} \quad \text { for every } t \geq 0 . \tag{6.6}
\end{equation*}
$$

Proof. By the previous considerations it suffices to show that $A \sigma(T(t)) \backslash\{0\} \subset e^{t \cdot \sigma(A)}$ for $t>0$. This will be done by converting approximate eigenvectors into eigenvectors in the semigroup F-product (see 4.5). The assertion then follows from (6.4) and assertion (ii) of the Proposition in 4.5.
Assume $t \rightarrow T(t)$ to be norm continuous for $t \geqq t_{0}$. Moreover it suffices to consider $1 \in \operatorname{Ac}\left(T\left(t_{1}\right)\right)$ for some $t_{1}>0$, i.e. we have a normalized sequence $\left(f_{n}\right){ }_{n \in N}=E$ such that.
$$
1 \mathrm{im}_{n \rightarrow \infty}\left\|T\left(t_{1}\right) f_{n}-f_{n}\right\|=0 .
$$

Choose $k \in \mathbb{N}$ such that $k t_{1}>t_{o}$ and define $g_{n}:=T\left(k t_{1}\right) f_{n}$. Then
$$
\lim _{\mathrm{n} \rightarrow \infty}\left\|\mathrm{~g}_{\mathrm{n}}\right\|=1 \mathrm{im} \mathrm{n}_{\mathrm{n}+\infty}\left\|\mathrm{T}\left(\mathrm{t}_{1}\right)^{\mathrm{k}_{\mathrm{f}}}\right\|=1 \mathrm{im}_{\mathrm{n} \rightarrow \infty}\left\|\mathrm{f}_{\mathrm{n}}\right\|=1
$$
and
$$
\lim _{n \rightarrow \infty} \tilde{\|} T\left(t_{1}\right) g_{n}-g_{n} \dot{I}_{\|}=0,
$$
i.e. $\left(g_{n}\right)_{n \in \mathbb{N}}$ yields an approximate eigenvector of $T\left(t_{1}\right)$ with approximate eigenvalue 1 . But the semigroup $T$ is uniformly continuous on sets of the form $T\left(t_{o}\right) V, V$ bounded in $E$. In particular, it is uniformly continuous on the sequence $\left(g_{n}\right){ }_{n \in \mathbb{N}}$ ' which therefore defines an element $\hat{g}$ in the semigroup $F$-product $E_{F}^{\top}$.
Obviously, $\hat{\mathbb{S}}$ is an eigenvector of $T_{F}\left(t_{j}\right)$ with eigenvalue 1 and by (6.4) we obtain an eigenvalue $2 \pi i n / t_{1}$ of $A_{F}$ for some $n \in \mathbb{Z}$. The coincidence of $\sigma(A)$ and $\sigma\left(A_{F}\right)$ proves the assertion.

We point out that the above spectral mapping theorem implies the coin~ cidence of spectral bound and growth bound for eventually norm continuous semigroups, hence we have generalized the Liapunov stability Theorem 1.2 to a much larger class of semigroups. As mentioned before this will be of great use in many applications. Therefore we state explicitly the spectral mapping theorem for several important classes of semigroups all of which are eventually norm continuous (cf. the diagram preceding AuIf,Ex.1.27).

Corollary 6.7. The spectral mapping theorem
$$
\begin{equation*}
\sigma(T(t)) \backslash\{0\}=e^{t \cdot \sigma(A)}, t \geqq 0, \tag{6.6}
\end{equation*}
$$
holds for each of the following classes of strongly continuous semi~ groups:
(i) eventually compact semigroups,
(ii) eventually differentiable semigroups,
(iii) holomorphic semigroups,
(iv) uniformly continuous semigroups.

Another application of the above spectral mapping theorem can be made to tensor product semigroups (see $A-I, 3.7$ ). Let $T_{1}=\left(T_{1}(t)\right){ }_{t \geqslant 0}$, $T_{2}=\left(T_{2}(t)\right)_{t \geqslant 0}$ be strongly continuous semigroups on Banach spaces $E_{1}, E_{2}$ with generator $A_{1}, A_{2}$. The tensor product semigroup $T=T_{1} g T_{2}$ on some (Appropriate) tensor product $E:=E_{1} \tilde{g}_{2} E_{2}$ has the generator $A=A_{1} I d+I d \theta A_{2}$, but in general the spectrum of $A$ is not determined by the spectra of $A_{1}, A_{2}$. But with an additional hypotheris the following can be proved.

Corollary 6.8. If $T_{1}$ and $T_{2}$ are eventually norm continuous then
$$
\sigma(A)=\sigma\left(A_{1}\right)+\sigma\left(A_{2}\right),
$$
where $A$ is the generator of the tensor product semigroup
$$
T_{1} \otimes T_{2}=\left(T_{1}(t) \& T_{2}(t)\right)_{t \geqq 0}
$$

Proof. Clearly, the tensor product semigroup ig eventually norm continuous and hence the spectral mapping theorem 6.6 is valid for all three semigroups $T_{1}, T_{2}$ and $T$. Moreover the spectrum of the tensor product of bounded operators is the product of the spectra [Reed-Simon (1978), XITI.97. Therefore
$$
\sigma\left(T_{1}(t) \theta T_{2}(t)\right)=\sigma\left(T_{1}(t)\right) \cdot \sigma\left(T_{2}(t)\right), t \geq 0
$$

Consequently we have the following identity for every $t \geqq 0$ :
$$
\begin{aligned}
e^{t \cdot \sigma(A)} & =\sigma\left(T_{1}(t) \otimes T_{2}(t)\right) \quad(0) \\
& =\sigma\left(T_{1}(t)\right) \cdot \sigma\left(T_{2}(t)\right) \quad\{0\} \\
& =e^{t \cdot \sigma\left(A_{1}\right)} \cdot e^{t \cdot \sigma\left(A_{2}\right)} \\
& =e^{t\left(\sigma\left(A_{1}\right)+\sigma\left(A_{2}\right)\right)}
\end{aligned}
$$

From this identity we want to deduce $\sigma(A)=\sigma\left(A_{1}\right)+\sigma\left(A_{2}\right)$. " $E$ : Take $\xi \in \sigma(A)$. Then for every $t>0$ there exist $\mu_{t} \in o\left(A_{1}\right)$, $\lambda_{t} \in \sigma\left(A_{2}\right)$ and $n_{t} \in \mathbb{Z}$ such that $E=\mu_{t}+\lambda_{t}+2 \pi i n_{t} / t$. since the real parts of $\mu_{t}, \lambda_{t}$ are bounded above, they lie in some interval [a,b] . But
$$
\sigma\left(A_{i}\right) r:\left(\left[a_{1}, b_{1}+i \mathbb{R}\right)\right.
$$
is compact for $i=1,2$, since $A_{i}$ is the generator of an eventuw ally norm continuous semigroup (see $A-I T$, Thm. 1.20). By taking $t$
sufficiently small we conclude that $n_{t}, \neq 0$ for some $t>0$, i.e. $\xi=\mu_{t},+\lambda_{t}$.
$" \supset ":$ Choose $\mu \in \sigma\left(A_{1}\right), \lambda \in \sigma\left(A_{2}\right)$. For every $t>0$ there exist $\eta_{t} \in \sigma(A), m_{t} \in \mathbb{Z}$ such that $\mu+\lambda=n_{t}+2 \pi i m_{t} / t$.
since $\operatorname{Re} \mu+\operatorname{Re} \lambda=\operatorname{Re} \eta_{t}$ and $\left\{I_{m} n_{t}: t>0\right\}$ is bounded
- $T=\left(\mathbb{F}_{1}(t) T_{2}(t)\right)_{t \geqslant 0}$ is eventually norm continuous $\sim$ it follows that $m_{t}$, $=0$ for some $t^{\prime}>0$.

\section*{7. WEAK SPECTRAL MAPPING THEOREMS}

In the previous section we showed under which hypotheses a spectral mapping theorem of the form
(7.1) $\quad \sigma(T(t)) \backslash\{0\}=e^{t \cdot \sigma(A)}, t \geqq 0$,
is valid for the generator $A$ of a strongly continuous semigroup (T(t)) $t_{t \geq 0}$.
Anong the various examples showing that (7.1) does not hold in general we recall the following.
Take the Banach space $E=C_{0}$, the multiplication operator $A\left(x_{n}\right)_{n \in N}$ $=\left(i n x_{n}\right)_{n} \in$ with maximal domain and the corresponding semigroup $T(t)\left(x_{n}\right)_{n \in \mathbb{N}}=\left(e^{i n t} x_{n}\right)_{n \in \mathbb{N}}$. Then $\sigma(A)=\{i n: n \in \mathbb{N}\}$ and the spectral mapping theorem is valid only in the following weak form:
$$
\begin{equation*}
\sigma(T(t))=\overline{\exp (t * \sigma(A)}), t \geq 0 . \tag{7.2}
\end{equation*}
$$

In this section we prove similar weak spectral mapping theorems. We start with a generalization of the above example.
Consider the Banach space $E=C_{D}\left(X, \mathbb{C}^{n}\right)$ of all continuous $\mathbb{C}^{n}$-valued functions vanishing at infinity on some locally compact space $X$. In analogy to $A-I, 2.3$ we associate to every continuous function $q: X \rightarrow M(n)$, where $M(n)$ denotes the space of all complex $n \times n-$ matrices, a "multiplication operator"
$M_{q}: f+q \cdot f$ such that $(q \cdot f)(x)=q(x) \cdot f(x), x \in X$,
on the maximal domain $D\left(M_{q}\right)=\{f \in E: q \cdot f \in E\}$. If $\left\|e^{t q(x)}\right\|$ is uniformly bounded for $0 \leq t \leq 1$ and $x \in x$ it follows that $M_{q}$ generates the multiplication semigroup
$$
(T(t) f)(x)=e^{t q(x)}(f(x)), f \in E, x \in X, t \geqslant 0 .
$$

Since $M_{q}$ has a bounded inverse if and only if $q(x)^{-1}$ exists and is uniformly bounded for $x \in x$ it follows that the eigenvalues of each matrix $q(x)$ are always contained in $\sigma\left(M_{q}\right)$. In fact, much more can be said in case the function is bounded.

Lemma 7.1. The spectrum of the matrix valued multiplication operator $M_{p}$ where $p: X \rightarrow M(n)$ is bounded is given by $o\left(M_{p}\right)=U_{x \in X} o(p(x))$.

Proof. It remains to show that 0 ( $\overline{U_{x \in X} \sigma(p(x))}$ implies $0 \& \sigma\left(M_{p}\right)$. Since det $p(x)$ is the product of $n$ eigenvalues (according to their multiplicity) of $p(x)$ the hypothesis implies that
$d:=\inf \{\mid$ det $p(x) \mid: x \in X\}>0$. By Formula 4.12 in Chapter $I$ of Kato (1966) we obtain
$$
\left\|p(x)^{-1}\right\| y \cdot\|p(x)\|^{n-1} \cdot|\operatorname{det} p(x)|^{-1} \cong y / a \cdot\left\|M_{p}\right\|^{n-1}
$$
for every $x \in x$ and a constant $\gamma$ depending only on the norm chosen on $\mathbb{C}^{n}$. Therefore $x \rightarrow p(x)^{-1}$ defines a bounded continuous function on $x$ which obviously yields the inverse of $M \mathbf{p}$, i.e., $0 \nless \circ\left(M_{p}\right)$.

Theorem 7.2. Let $A=M_{q}$ be a matrix multiplication operator on $c_{o}\left(X, C^{n}\right)$ generating a strongly continuous semigroup (T(t)) $t \geqq 0=$ (etq(-) $)_{t \geq 0}$. Then the Weak Spectral Mapping Theorem of the form
$$
\begin{equation*}
o(T(t))=\overline{\exp (t \cdot \sigma(A)}) \tag{7.2}
\end{equation*}
$$
is valid.

Proof. By the spectral Inclusion Theorem 6.2 we always have $\exp (t \sigma(A)) \subset \sigma(T(t))$. Since $T(t)$ is a matrix multiplication operator with a bounded function we obtain from Lemma 7.1
$\sigma(T(t))=\overline{U_{x \in X}} \overline{\sigma(\exp (t q(x)))}=\overline{U_{x \in X} \exp \left(t_{\sigma}(q(x))\right)}=\overline{\exp \left(t_{\sigma}(A)\right)}$,
which proves the assertion.

Corollary 7.3. The growth bound is (A) and the spectral bound $s(A)$ coincide for matrix multiplication semigroups.

Remark. The above results remain valid for other Banach spaces of $\mathrm{c}^{\mathrm{n}}$-valued functions such as $\mathrm{L}^{\mathrm{p}}\left(\mathrm{X}, \mathrm{c}^{\mathrm{n}}\right), 1 \leqq p<\infty$.

The example given at the beginning of this section can be generalized in a different way. In fact, $A\left(x_{n}\right)$ : $=\left(i n x_{n}\right)$ on $E=c_{0}$ generates a bounded group, and we will show that this property too ensures that the Weak Spectral Mapping Theorem (7.2) holds. Without any boundedness assumption on $(T(t)) t \in \mathbb{R}$ this result cannot be true (see [HillePhillipg (1957), Sec. 23.16 or [Wolff(1981) j).

Theorem 7.4. Let $T=(T(t))_{t \in \mathbb{R}}$ be a strongly continuous group on some Banach space $E$ such that $\|T(t)\| f(t)$ for some polynomial $p$ and all $t \in \mathbb{R}$. Then the Weak Spectral Mapping Theorem holdg, i.e.,
$$
\begin{equation*}
\sigma(T(t))=\exp (t \cdot \sigma(A)) \quad \text { for all } t \in \mathbb{R} . \tag{7.2}
\end{equation*}
$$

From the proof we isolate a series of lemmas for which we always ascume the hypothesis made in Thm. 7.4. Moreover we recall from Fourier andlysis that the Fourier transformation $t \rightarrow \vec{\phi}$, $\phi(\alpha):=\int_{\rightarrow \infty}^{\infty} \phi(x) e^{-i \alpha X} d x$, and its inverse $Y \rightarrow+$ $\Psi(x):=1 / 2 \pi \cdot \int_{-\infty}^{\infty} \Psi(\alpha) \cdot e^{i \alpha x}$ da are topological isomorphisms of the Schwartz space $S(=S(\mathbb{R}))$. Since the subspace $\mathcal{D}$ of all functions having compact support is dense in $S$ it follows that $\left\{\phi \in S\right.$; $\left.{ }_{\phi}^{\psi} \in D\right\}$ is dense in $S$.

Lemma 7.5. For every function $\phi \in S$ we obtain an operator $T(\phi) \in L(E) \quad b y$
$$
T(\phi) f:=\int_{-\infty}^{\infty} \phi(s) T(s) \notin d s, f \in E .
$$

This operator can be represented as
(7.3)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-102.jpg?height=61&width=1537&top_left_y=1409&top_left_x=214)

Proof. That $T(\phi)$ is well-defined follows from the polynomial bound edness of $(T(t))_{t \in \mathbb{R}}$. In fact, $\phi \rightarrow T(\phi)$ is continuous from $S$ into (L(E), $\|\cdot\|$ ) .

We obtain
$$
\begin{aligned}
& T(\phi) f=1 i_{E \rightarrow 0} \int_{-\infty}^{\infty} \phi(s) e^{-E \mid s i} T(s) f d s \\
& =1 i m{ }_{\varepsilon \rightarrow 0} \int_{-\infty}^{\infty} 1 / 2 \pi \int_{-\infty}^{\infty}+(\alpha) e^{i \alpha s^{-\varepsilon}|s|_{T(s)} f d a} d s \\
& =\lim _{\varepsilon \rightarrow 0} 1 / 2 \pi \int_{-\infty}^{\infty} \hat{\phi}(\alpha) \quad \int_{-\infty}^{\infty} e^{i \alpha s} e^{-\varepsilon|s|} T(s) f d s d a \\
& =1 \mathrm{~m}_{\xi \rightarrow 0} 1 / 2 \pi \int_{-\infty}^{\infty} \hat{\phi}(\alpha)[R(\varepsilon \sim i \alpha, A) f-R(-\varepsilon-i \alpha, A) f] d a .
\end{aligned}
$$

Here we used that polynomially bounded semigroups have growth bound 0 , hence $i(A)=\omega(-A)=0$. Hence the integral representation of R(e-ia,A) (cf. A-I, Prop.1.11) exists for $\varepsilon \neq 0$.

Lemma 7.6. If $E \neq\{0\}$, then $\sigma(A) \neq \varnothing$.

Proof. If $\sigma(A)=\emptyset$ then (7.3) implies $T(\phi)=0$ whenever $\dot{\phi}$ has compact support. since these functions form a dense subspace of $S$ we conclude that $T(\phi)=0$ for all $\phi \in S$.

Choosing an approximate identity $\left(\Psi_{n}\right) n_{n}=D$ we obtain
$$
f=T(0) f=1 i m_{n \rightarrow \mathbb{N}} T\left(\Psi_{n}\right) f=0
$$
for every $f \in E$.

Proof of Theorem 7.4 (1 ${ }^{\text {st }}$ part). By the Spectral Inclusion Theorem 6.2 we have to show that every spectral value of $T(t)$ can be approximated by exponentials of spectral values of $A$. In view of the rescaling procedure it suffices to prove this when $\mathbf{- 1} \in\left(T \boldsymbol{f}_{\boldsymbol{m}}\right)$ ), provided that the following condition is satisfied.
(7.4) There exists $\varepsilon>0$ such that $U_{k \in Z} i[2 k+1-2 E, 2 k+1+2 \varepsilon]=\rho(A)$. Assume now that (7.4) holds. Then each of the sets $\sigma_{k}:=\left\{i_{\alpha} \in \sigma(A) ; \alpha \in[2 k-1,2 k+l]\right\}$ is a spectral set of $A$ with corresponding spectral projection $P_{k}$. If we choose $\phi_{o} \in \mathcal{D}$ such that supp $d_{o}=[-1+\varepsilon, 1-\varepsilon]$ and $\phi_{o}(x)=1$ for $x \in[-1+2 \varepsilon, 1-2 \varepsilon]$ it follows from (7.3) and the integral representation of $P_{k}$ (cf.(3.1))
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-103.jpg?height=76&width=1606&top_left_y=1224&top_left_x=225) the assertions (7.3) and (7.4) imply
$$
\begin{equation*}
P_{k}=\int_{-\infty}^{\infty} e^{i 2 k s} \stackrel{\rightharpoonup}{\phi}_{o}(s) T(s) d s \text { for } k \in \mathbb{Z} \tag{7,5}
\end{equation*}
$$

At this point we isolate another lemma.

Lemma 7.7. $\operatorname{span} U_{k \in Z} P_{k} E$ is dense in $E$.

Proof. The closure of span $U_{k \in \mathbb{Z}} P_{k}{ }^{E}$ is a T-invariant subspace $G$ of $E$. Consider the quotient group $(T(t) / f \in \mathbb{R}$ induced on $E / G$, The spectrum of its generator $A$, is contained in o(A) by Prop.4.2.iii. Moreover the spectral projection corresponding to o(A/) in $\sigma$ is the quotient operator $\mathrm{P}_{\mathrm{k} / \mathrm{L}}$. Obviously $\mathrm{P}_{\mathrm{k} /}=0$, therefore $\sigma(A,) \| \sigma_{k}=0$ for every $k \in \mathbb{Z}$ and $\sigma(A /)=0$. By Lemmat 7.6 this implies $E / G=\{0\}$, i.e. $G=E$.

Proof of Theorem 7.4 ( $2^{\text {nd }}$ part). We return to the situation of the first part. Using (7.5) the spectral projection $P_{k}$ can be transformed into
$$
\begin{aligned}
P_{k} & =\int_{-\infty}^{\infty} e^{i 2 k s} \overleftarrow{\phi}_{o}(s) T(s) d s \\
& =\sum_{m \in \mathcal{F}} \int(m+1 / 2) \pi e^{(m+2 k s} \dot{\phi}_{o}(s) T(s) d s \\
& =\int_{-\pi / 2}^{\pi / 2} e^{i 2 k s} \sum_{m \in \mathcal{L}} \stackrel{+}{o}^{\left(s+m_{\pi}\right)} T\left(s+m_{\pi}\right) d s
\end{aligned}
$$
i.e., $P_{k} f$ is the $k-t h$ Fourier coefficient of the $\pi$-periodic, continuous function $\xi_{f}: s \rightarrow \sum_{m \in \mathbb{Z}} \overleftarrow{\phi}_{o}(s+m \pi) T(s+m \pi) f, f \in E$, Since the projections $P_{k}$ are mutually orthogonal, i.e. $P_{k} P_{m}=0$ for $k \neq m$, it follows that $g=\sum_{n \in \mathbb{Z}} P_{n} g$ for every $g \in \operatorname{span} U_{k \in \mathbb{Z}} P_{k} E$. In particular, the Fourier coefficients of the function $\xi_{g}$ are absolutely sumable, hence the fourier series of ${ }_{5} \mathrm{~g}$ converges to $\xi$. For $g=0$ we obtain
$g=\sum_{n \in \mathbb{Z}} P_{n} g \cdot e^{-i n 0}=\sum_{m \in \mathbb{Z}} \Phi_{O}(0+m \pi) T(0+m \pi) g\left(g \in \operatorname{span} U_{k \in \mathbb{Z}} P_{k} E\right)$. since $\operatorname{span} U_{k \in \mathcal{F}} \mathrm{P}_{\mathrm{k}}{ }^{\mathrm{F}}$ is dense (Lemma 7.7) we conclude that
$$
\begin{equation*}
\sum_{\mathrm{m} \in \mathbb{Z}} \ddagger_{\mathrm{O}}(\mathrm{~m} \mathrm{\pi}) \mathrm{T}(\mathrm{mF})=I \mathrm{~A} . \tag{7.6}
\end{equation*}
$$

As the final step we construct the inverse operator of id $+T(\pi)$ showing that $-1 \in \rho(T(\pi))$. We define $\psi_{o}(\alpha):=\phi_{0}(\alpha) \cdot\left(1+e^{i \pi \alpha}\right)^{-1}$, $\alpha \in \mathbb{R}$. Then we have $\Psi_{0} \in S$ and $\Psi_{o}\left(1+e^{i \pi}\right)=\phi_{0}$, hence $\Psi_{0}(x)+\Psi_{0}(x+\pi)=\$_{o}(x)$ for all $x \in \mathbb{R}$. Then (7.6) implies $I d=\Sigma_{m \in \mathbb{Z}} \dot{\phi}_{D}(m \pi) T(m \pi)$
$=\sum_{m \in Z}\left(\Psi_{O}(m \pi)+\Psi_{O}((m+1) \pi)\right) T(m \pi)$
$=\left[\xi_{m \in Z} \Psi_{o}(m \pi) T(m \pi)\right](I d+T(\pi))$.

In the rest of this section we discusg the behavior of the single spectral values $\lambda$ of $T(t), t \geqslant 0$. The aim is a characterization of $\sigma(T(t)$ ) involving only properties of the generator. By the rescaling procedure $A-I, 3.1$ we may assume $\lambda=1$ and $t=2 \pi$.
From the spectral Inclusion Theorem 6.2 we know that $1 \in p(T(2 \pi))$ implies $i f=\rho(A)$. As seen in many examples the converse does not hold and we are now looking for additional conditions.

Henceforth we assume $i \not \subset \rho(A)$ and define for $k \in \mathbb{Z}$
$$
\begin{equation*}
Q_{k}:=1 / 2 \pi \int_{0}^{2 \pi} e^{-i k s} T(s) d s=1 / 2 \pi(1-T(2 \pi)) R(i k, A), \tag{7.7}
\end{equation*}
$$
(cf. Formula $A-I,(3.1))$.

Our approach is based on Fejer's Theorem for Banach space valued functions). Let us recall this result. Suppose $\xi$; [0, $2 \pi] \rightarrow E$ is a continuous function and let $\xi_{k}$ : $=1 / 2 \pi \int_{0}^{2 \pi} e^{-i k s} \xi(s) d s$ be its k-th Fourier coefficient. Then the Fourier series is cesaro sumable to $\xi$ in every point $t \in(0,2 \pi)$. Moreover one has
(7.8) $1 / 2(\xi(0)+\xi(2 \pi))=C_{1}-\sum_{k \in T} \xi_{\mathrm{n}}:=1 \mathrm{im}_{\mathrm{N} \rightarrow \mathrm{m}} 1 / \mathrm{N} \cdot \sum_{\mathrm{n}=0}^{\mathrm{N}-1}\left(\sum_{\mathrm{k}=-\mathrm{n}}^{\mathrm{n}} \xi_{\mathrm{k}}\right)$.

This result enables us to prove the following proposition:

Proposition 7.8. Let (T(t)) tき0 be a semigroup on a Banach space E and denote its generator by $A$. Then the following conditions are equivalent:
(a) $1 \in p(T(2 \pi))$;
(b) $\quad i \boldsymbol{Z}=\rho(\mathrm{A})$ and the series $\sum_{k \in \boldsymbol{Z}} R(i k, A) f$ is Cesaro-summable for every $f \in E$,
(c) iZ $\subset \rho(A)$ and the series $\sum_{k \in \mathbb{Z}} R(i k, A) Q_{k} f$ is cesaro-summable for every $f \in E$.

Proof. (a) $\rightarrow(b):$ The Spectral Inclusion Theorem implies if $\subset p(A)$. By (7.7) we have $R(i k, A)=2 \pi \cdot(1-T(2 \pi))^{-1} Q_{k}$. since $\sum_{k \in \mathbb{Z}} Q_{k} f$ is Césaro-summable (towards $1 / 2(f+T(2 \pi) f)$ ) (see (7.8)) it follows that $\sum_{k \in \mathcal{E}} \mathrm{R}(\mathrm{ik}, \mathrm{A}) \mathrm{f}$ is Cesaro-summable as well.
(b) \&A> (c): If we use $A-I,(3.1)$ and integrate by parts, we obtain $R(i k, A) Q_{k} f\left(1 / 2 \pi \int_{0}^{2 \pi} e^{-i k s} T(s) R(i k, A) f(s\right.$ $=1 / 2 \pi \int_{0}^{2 \pi}\left[R(i k, A) f-\int_{0}^{5} e^{-i k t} T(t) f d t\right] d s$ $=R(i k, A) f-1 / 2 \pi \int_{0}^{2 \pi} e^{-i k t}(2 \pi-t) T(t) f d t$.
Fejer's theorem ensures that $\bar{L}_{k \in Z}(1 / 2 \pi) \int_{0}^{2 \pi} e^{-i k t}\left(2_{\pi}-t\right) T(t) f d t$
is Cesaro summable. Hence $\sum_{k \in \mathbb{Z}} R(i k, A) Q_{k} f$ is Cesaro-summable if and only if $\sum_{k \in \mathbb{Z}}$ R(ik,A)f is.
$(b) \rightarrow(a):$ We have $Q_{k}=\frac{1}{2 \pi}(1-T(2 \pi)) R(i k, A)$. Furthermore we know by (7.7) and (7.B) that $\sum_{k \in Z} Q_{k} f$ is Cesaro-sumable towards $\frac{1}{2}(f+T(2 \pi) f)$.
If we define $S: E \rightarrow E$ by $S f:=\frac{f}{2}+\frac{1}{2 \pi} * C_{1}-\sum R(i k, A) f$ then we have $(1-T(2 \pi)) S f=\frac{1}{2}(f-T(2 \pi) f)+\frac{1}{2 \pi} * C_{1}-\Gamma(1-T(2 \pi)) R(i k, A) f=$
$$
=\frac{1}{2}(f-T(2 \pi) f)+\frac{1}{2}(f+T(2 \pi) f)=f .
$$

Since $s$ commutes with $T(2 \pi)$ it follows that $S$ is the inverge of (1-T(2m)) thus $1 \in \rho(T(2 \pi))$.

Based on the equivalence of (a) and (b), one can state a characterization of the spectrum of $T(t)$ in terms of the generator and its resolvent only. However, in general it is difficult to verify the summability condition stated in (b).

In Hilbert spaces the boundedness of the resolvents will suffice (see Thm. 7.10 below).

Lemma 7.9. Let (T(t)) $\underset{t \geqq 0}{ }$ be a semigroup on some Hilbert space $H$ and assume $i f \subset \rho(A)$ for the generator $A$. Then we have
(i) $\quad\left(Q_{k} f\right) k \in \mathbb{Z} \in \ell^{2}(H)$ for every $f \in H$, and
(ii) if $\sup _{k \in \mathbb{Z}}\left\|^{\| R}(i k, A)\right\|<\infty$, then $\sum_{k \in \mathbb{Z}} R(i k, A) f_{k}$ is surmable whenever $\left(f_{k}\right)_{k \in \mathcal{Z}} \in \ell^{2}(H)$.

Proof. (i) We consider the Hilbert space $L^{2}([0,2 \pi], H)$ and obtain $0 \leqq\left\|T(\cdot) f-\sum_{k=-n}^{n} Q_{k} E \cdot e^{i k \cdot}\right\|^{2}$
$=\int_{0}^{2 \pi}\|T(s) f\|_{i}^{2} d s-\int_{0}^{2 \pi} \sum_{k=-n}^{n}\left(T(s) f \mid e^{i k s}{Q_{k}}^{f}\right) d s-$
$\int_{0}^{2 \pi} \sum_{k=-n}^{n}\left(e^{i k s} Q_{k} f \mid T(s) f\right) d s+\int_{0}^{2 \pi}\left(\sum_{k=-n}^{n} e^{i k s} Q_{Q_{k}} f \mid \sum_{\ell=n}^{n} e^{\left.i \ell s Q_{\ell} f\right) d s}\right.$
$=\int_{0}^{2 \pi}\|T(s) f\|^{2} d s-2 \pi \sum_{k=-n}^{n}\left\|Q_{k} f\right\|^{2}$, (use (7.5)).
It follows that $\sum_{k \in T}\left\|Q_{k} f\right\|^{2} \cong \frac{1}{2 \pi} \cdot \int_{0}^{2 \pi}\|T(s) f\|^{2} d s<\infty$.
(ii) Fix $\lambda>0$ sufficiently large and set
$$
g_{k}:=(1+\lambda R(i k, A)) f_{k}, k \in \mathbb{Z} .
$$

Jsing the resolvent equation and then (A-I, (3.1)) we obtain $R(i k, A) f_{k}=R(\lambda+i k, A) g_{k}=\left[1-e^{-2 \pi \lambda} T(2 \pi)\right]^{-1} \int_{0}^{2 \pi} e^{-\lambda s} e^{-i k s} T(s) g_{k} d s$. This yields for every finite subset $N$ of $\mathbb{Z}$
$$
\begin{aligned}
& \left\|_{i} \sum_{k \in N} R(i k, A) f_{k}\right\| \leqq\left\|\left(1-e^{-2 \pi \lambda} T(2 \pi)\right)^{-1}\right\| \cdot \int_{0}^{2 \pi}\|T(s)\|\left\|\sum_{k \in \mathbb{N}} e^{-i k s} g_{k}\right\| d s \leqq \\
& \left.\quad \leqq\left\|\left(1-e^{-2 \pi \lambda} T(2 \pi)\right)^{-1}\right\| \cdot\left(\int_{0}^{2 \pi}\|T(s)\|_{1}^{2} d s\right)^{1 / 2} \cdot\left\|\int_{0}^{2 \pi}\right\| \sum_{k \in \mathbb{N}} e^{-i k s} g_{k} \|^{2} d x\right)^{1 / 2} \\
& \quad=c\left(\sum_{k \in \mathbb{N}}\left\|g_{k}\right\|^{2}\right)^{1 / 2} \leqq c(1+\lambda M)\left(\sum_{k \in N}\left\|f_{k}\right\|^{2}\right)^{1 / 2} .
\end{aligned}
$$

Here $c:=\left\|_{i}\left(1-e^{-2 \pi \lambda} T(2 \pi)\right)^{-1}\right\| \cdot\left(\int_{0}^{2 \pi}\|T(s)\|^{2} d s\right)^{1 / 2}$ and $\mathrm{M}:=\sup _{\left.\mathrm{k} \in \boldsymbol{T}^{\dot{\|} R(i k}, \mathrm{A}\right) \|} \|$

Theorem 7.10. Let $A$ be the generator of a semigroup (T(t)) ta0 on some Hilbert space $H$. Then the following form of the spectral mapping theorem is valid
$$
\begin{aligned}
& \sigma(T(t)) \backslash\{0\}=\left\{e^{h t}: \text { either } \mu_{k}:=\right. \lambda+2 \pi i k / t \in \sigma(A) \text { for some } k \in \mathbb{Z} \\
& \text { or }\left(\left\|R\left(\mu_{k}, A\right)\right\| f\right) \\
&k \in \mathbb{Z} \text { is unbounded }\} .
\end{aligned}
$$

Proof. If $e^{\lambda t} \mid \sigma(T(t))$ it follows from the spectral inclusion theorem that $\psi_{k} \neq \sigma(A)$ for every $k \in \mathbb{Z}$ and from A-Ir 3,1 , Formula (3.1), that $\left\|R\left(\mu_{k}, A\right)\right\|$ is bounded. For the converse inclusion it suffices to assume $t=2 \pi$ and $\lambda=0$ (use the rescaling procedure $A-I, 3.1)$. Assuming that $i \mathbb{I} \subset \rho(A)$ and $\|R(i k, A)\|$ is bounded then $\sum_{k \in \mathbb{L}} R(i k, A) Q_{k} f$ is summable by Lemuta 7.9 . Since every summable series is Césaro-summable condition (c) of Prop. 7.8 is satisfied and we conclude $1 \in \mathrm{f}(\mathrm{T}(2 \pi))$.

As an immediate consequence we obtain an interesting characterization of the growth bound id of semigroups on Hilbert spaces.

Corollary 7.11. The growth bound of a semigroup (T(t)) $t \geqslant 0$ on a Hilbert space $H$ satisfies
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-107.jpg?height=46&width=1449&top_left_y=568&top_left_x=232)
bounded for $u \in E$ \} .

The Example 1.3 above in combination with $\mathrm{C}-$ III, Cor. 1.3 shows that (7.9) is not valid in arbitrary Banach spaces.

NOTES.
Section l. It was already known to Hille-phillips (1957) that for strongly continuous semigroups ( $T(t)$ ) with generator A the spectral mapping theorem " $\sigma$ ( $T(t)$ ) $=\exp (t \sigma(A))^{\prime \prime}$ may be violated fn various ways [1.c., Sec.23.16.1. The simple Examples 1.3 and 1.4 are due to Wolff (see Greiner-Voigt-Wolff (1981)) and Zabczyk (1975). A more sophisticated example of a posttive group with "s (A) ew $A$ " is gitven ln Wolfi (1981).

Section 2. In Deftnition 2.1 we define the residual spectrum of A f.n such a way that it coincides with the point spectrum of the adjotnt A' (see Prop. 2.2.(ti)). It therefore differs slightly from the one used, e.g., by Schaefer (1974). The spectral mapping theorem for the resolvent (Thm. 2.5) is well known and can, e.g., be deduced from Lemma 9.2 and Thm. 3.11 of Chap.VII in Dunford-Schwartz (1958).

Section 3. The general theory of spectral decompositlons can be found in [Kato (1966), Chap.III, $\$ 6.4]$. Applications to solated slagtularities like 3.6 are discussed extensfvely in [l.c., Chap.III, $\$ 6.5]$ and [Yosida (1965), Chap. VIII, Sec.8]. There are wany ways to fntroduce an "essential spectrum" (see the footnote on page 243 of Kato (19663). However each one yields the same "essential spectral radius".

Section 4. These results are taken from Jerndinger (1980) and Greiner (1981).
Section 5. Perfodic semigroups are studied explicttely tn Eart (1977) but most of the results of this section seem to be well known.

Section 6. The Spectral Inclusion Theorem 6.2 and the Spectral Mapping Theorem 6.6 for eventually norm continuous semigroups date back to Hflle-Phillips (1957). Davies (1980\} gives an elegant proof using Banach algebra techndques. Tensor products of operators and their spectral theory have been studied by Ichfnose and others (see Chap. XIII.9 of Reed-Simon (1978)). The spectral mapping theorem in Corollary 6.8 generalizes Thai XIII. 35 of Reed~Stmon (1978) (see also Herbst (1982)).

Section 7. Matrix valued mult lplication semigroups appear as solution, via Fourier transformation, of systems of partial dffferential equations. Kreiss finftiated a systematic investigation (see, e.g.. Kreiss (1958), Kreiss (1959), Mt1ler-Strang
(1966) and the Weak Spectral Mapping Theorem 7.2 must have been known to him. The direct proof of the Weak Spectral Mapping Theorem 7.4 for polynomially bounded groups seems to be new. The result can also be deduced from the theory of spectral subspaces of group representations (see, e.g., Combes-Delaroche (1978) , since the Arveson spectrum of a strongly continuous one-parameter group can be identified with the spectrum of the generator (see Evans (1976)). The final part of this section is taken Frome Greiner (1985) and yields a new approach to Gearhart's characterization of the spectrum of semigroups on Hilbert spaces [Gearhart (1978) ]. Different proofs can be Found in Herbst (1983), Howland (1984) and PríB (1984).
by
Frank Neubrander

In this chapter we study the asymptotic behavior of the solutions of the initial value problem
$$
\begin{equation*}
\dot{u}(t)=A u(t)+F(t), u(0)=f \tag{*}
\end{equation*}
$$
with respect to time $t \geqslant 0$. Here $A$ will be a generator of a strongly continuous semigroup $(T(t)) t \geq 0$ on a Banach space $E$ and $F(\cdot)$ is a function from $\mathbb{R}_{+}$with values in $E$.
In Section 1 we investigate whether and how fast a solution $T(\cdot) f$ of the homogeneous problem tends to the zero solution as $t \rightarrow \infty$; in Section 2 we consider the long term behavior of the solutions of (*) for different classes of forcing terms $F$.
1. STABILITY : HOMOGENEOUS CASE

Let $(T(t)) t \geqslant 0$ be a semigroup on $E$ with generator $A$ An initial value $f \in D(A)$ ig called stable if the solution $t \rightarrow T(t) f$ of
$(\mathrm{ACP}) \quad \dot{u}(\mathrm{t})=\mathrm{Au}(\mathrm{t}), \mathrm{u}(0)=\mathrm{f}$
converges to zero as t tends to infinity. The semigroup is called stable if every solution converges to zero; i.e., if every initial value $f \in D(A)$ is stable.

If the space $E$ is finite dimensional, then the stability of the semigroup implies that the decay is exponential. More precisely, the statements
(a)
(b)
$$
\begin{aligned}
& \|T(t) f\| \rightarrow 0 \text { for every } f \in \mathbb{C}^{\mathrm{M}}, \\
& \|T(t)\| \leq M e^{-\omega t} \text { for some } \omega>0
\end{aligned}
$$
are equivalent. Moreover, these statements hold if and only if
$$
s(A)=\sup \{\operatorname{Re} h: h \in \sigma(A)\}<0,
$$
see $A-I I I, C o r .1 .2$.

As already discussed in Chapter $A \rightarrow I I I$ the situation is far more difficult in the infinite dimensional case. Here, and for unbounded generators, we have to distinguish between strong and generalized (mild) solutions of $u(t)=A u(t)$ and between various notions of stability. Recall that for $f \in D(A)$ the function $T(\cdot) f$ is a strong solution of (ACP) (see A-II, Cor.l.2.); for arbitrary $f \in E$ the function $T(\cdot) f$ is called a generalized or mild solution of (ACP). Next we introduce several constants characterizing the growth of the solutions of (ACP).

Definition 1.1 ( $1^{s t}$ part). Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$. Then
(i) $\quad \omega(f):=\inf \left\{w: \| T(t) f \mid \leq M e^{W t}\right.$ for some $M$ and every $\left.t z 0\right\}$ is called the (exponential) growth bound of T(:)f.
(iii) $\omega_{1}(\vec{R}):=\sup \{\omega(f): f \in D(\vec{R})\}$ is called the (exponential) growth bound of the solutions of the cauchy problem $u(t)=A u(t)$.
$i(A)=\sup \{u(f): f \in E\}$ is called the (exponential) growth
bound of the mild solutions of the cauchy problem
$\dot{u}(\mathrm{t})=\mathrm{Au}(\mathrm{t})$.

Note that, by the Principle of Uniform Boundedness, sup(w(f): $f \in E\}$ $=\inf \left\{\omega: \mid f(t) \| \sum M e^{\mu t}\right.$ for some $M$ and every $\left.t \geqq 0\right\}$. Hence $\omega(A)$ coincides with the growth bound of the semigroup (T(t)) teo as defined in $A-T, 1.3$. With the constants defined above we obtain the following stability concepts.

Definition 1.1 ( $2^{\text {nd }}$ part). The semigroup $(T(t))$ t $\geq 0$ is called
(iv) uniformly exponentially stable if $w(A)<0$;
(v) exponentially stable if $\omega_{1}(A)<0$;
(vi) uniformly stable if $\|T(t) f\|_{i} \rightarrow 0$ (as $t \rightarrow \infty$ for every $f \in E$;
```
    stable if |T(t)f|->0 (as t t m) for every f f D(B).
```

The interrelation between these stability concepts is given by
<smiles>NCN[AlH2]</smiles>

If $A$ is a bounded operator, i.e., if $D(A)=E$, then (iv) 《w> (v) and (vi) as $^{\prime}$ (vii). J.f A is unbounded then the stability notions may differ as we will see in the following examples.

Examples 1.2 . (a) Let $E=C_{0}$. Then $A$ : $\left(x_{n}\right)_{n \in \mathbb{N}} \rightarrow\left(-1 / n \cdot x_{n}\right)_{n \in \mathbb{N}}$ generates the semigroup $T(t)\left(x_{n}\right)=\left(e^{\left.-t / n_{x_{n}}\right)}{ }_{n} \in \mathbb{N}\right.$. It is easy to see that $\|T(t)\|=i$ and $\|T(t) f\|_{i} \rightarrow 0$ for every $f \in c_{0}$. Moreover, $A$ is a bounded operator, hence $D(A)=E$. This gives an example for a (uniformly) stable but not exponentially stable semigroup. The translation semigroups generated by the first derivative on $\mathrm{C}_{0}\left(\mathbb{R}_{t}\right)$ or $L^{P}\left(\mathbb{R}_{+}\right)$for $1 < p <\infty$ give further examples for (uniformly) stable but not exponentially stable semjoroups. Moreover, as seen in $A_{i} \bar{i}$, Ex.1.l4, the foplacian $\Delta$ on $C_{o}\left(\mathbb{R}^{n}\right)$ generates a bounded holomorphic semigroup given by
$$
T(t) E(x)=(4 \pi t)^{-n / 2} \cdot \int_{R^{n}} e^{-(x-y)^{2} / 4 t} f(y) d y
$$
which cannot be exponentially stable because $0 \in \sigma(A)\left(i m A \nmid C_{0}\left(\mathbb{R}^{n}\right)\right)$, see Cor.l.5 below. By a straightforward (2-e)-argument using $(4 \pi t)^{-n / 2} \int_{R^{n}} \exp \left(-y^{2} / 4 t\right) d y=1$ one can easily show that $\|T(t) f\|+0$ for all $f \in C_{0}\left(\mathbb{R}^{n}\right)$ (see also BuIII,Ex,1.7). Therefore, the Laplacian on $C_{o}^{\left(R^{n}\right)}$ (and also on $L^{P}\left(\mathbb{R}^{n}\right)$ for $1 < p <\infty$, see Ex. 1.15 below) generates a (uniformly) stable but not exponentially stable semigroup.
(b) Note that the condition $0 \leqq \omega(A)=\inf \left[\omega:\|T(t)\| \leqq M e^{\omega t}\right.$ for all $t \geq 0\}$ does not exclude that the semigroup ( $T(t)$ ) $t \geq 0$ is expou nentially stable. In fact, as shown in $A-I I I, 1.3$ the translation semigroup $(T(t)) t \geqq 0$ on $E:=C_{0}\left(\mathbb{R}_{+}\right) \cap L^{1}\left(\mathbb{R}_{+}, e^{x} d x\right)$ satisfies $\|T(t)\|$ $=1$, hence $\omega(A)=0$, and for every $\lambda \in \mathbb{C}$ with Re $\lambda>-1$ the resolvent of the generator ig given $a g$ R(h, $A) f=\int_{0}^{\infty} e^{h t} T(t) f d t$ for every $\ddagger \in E$. From the equation $A-I, 3.2$
$$
T(t) f=e^{\lambda t}\left(f-\int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f(s)\right.
$$
and the existence of $\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f$ ds it follows that $\|T(t) f\| \leqq M-e^{\lambda t}$ for every $f \in D(A)$ and some constant $M$ depending
on $f$. This yields ${ }^{\mu}(A) \leqq \sim l<0=\omega(A)$. Thus we have a semigroup which is exponentially, but not uniformly exponentially stable.
(c) Rescaling this semigroup (see Aw, 3.1) we obtain a semigroup with $-1 / 2={ }^{w}(A)$ and $1 / 2=w(A)$. Therefore there are exponentially stable and hence stable semigroups which are not bounded and hence not uniformly stable. We conclude from this example that there may be an essential difference between the long term behavior of the semigroup (T(t)) ${ }_{\text {t }} \geq 0$ (i.e. of the set of all mild solutions) and the long term behavior of the strong solutions $\{T(\cdot] f: f \in D(A)\}$ of (ACP).

In the following we characterize the exponential growth bounds $w(f)$, ${ }_{1}(A)$ and ${ }^{\omega}(A)$ by certain abscissas of simple or absolute conw vergence of the Laplace transform of $T(\cdot) f$. These characterizations will be the basic tool in showing that for certain semigroups the growth bounds $w(A)$ and/or ${ }^{11}$ (A) coincide with the spectral bound $\Sigma(\bar{B})=\sup \{\operatorname{Re\lambda }: \lambda \in \sigma(A)\}$.

We remark first that $s(A)$ can be regarded as the abscissa of holomorphy of the Laplace transform $\lambda \rightarrow \int_{0}^{\infty} e^{\lambda t} T(t) d t$ of the semigroup $(T(t))_{t \geq 0}$.
Next we recall that the Laplace transform exists for every $\lambda \in \mathbb{C}$ with Re $\lambda>\operatorname{Re} \sharp$ as soon as it exists for $k$. This follows from the equation
$$
\begin{align*}
\int_{0}^{t} e^{-\lambda s} f(s) d s= & e^{-(\lambda-\mu) t} \cdot \int_{0}^{t} e^{-\mu s} f(s) d s  \tag{1.1}\\
& +(\lambda-\mu) \int_{0}^{t} e^{-(\lambda-\mu) s} \int_{0}^{s} e^{-\mu r} f(r) d r d s
\end{align*}
$$

Note that even boundedness of $\int_{0}^{t} e^{-\mu s} f(s) d s$ implies the existence of the Laplace transform for ke $\lambda>$ Re $\mu$. Therefore the gubset of $\mathbb{C}$ for which the Laplace transform exists ig always a halfuplane $\{\lambda \in \mathbb{C}$ : $\operatorname{Re} \lambda>y\} \cup H$, where $H$ is a subset of the line $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda=\gamma\}$.

In the subsequent theorem we show that the bound of the half-plane for which the Laplace transform of $T(*) f$ (f $\in E$ ) exists absolutely and the bound of the half-plane for which the Laplace trangform of $T \|^{*}$ )Af (f $\in D(A))$ exists strongly coincide with the growth bound w(f) $=$ $\inf \left(\omega:\|T(t) f\| \leqq M e^{\omega t}\right.$ for all $\left.t \geqq 0\right\}$.

Theorem 1.3. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$. Then, for every $f \in E$, (1.2) $\quad \omega(f)=1 i m s u_{t \rightarrow \infty} 1 / t \cdot \log \| T(t) f$,
and
(i) $\quad \omega(f)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t\right.$ exists $\}$.

If ker $A=\{0\}$, then for every $f \in D(A)$ we have
(ii) $\quad$ (f) $=\inf \left(\mathrm{Re} \lambda: \int_{0}^{\infty} e^{-h t} T(t) A f\right.$ dt exists as an improper Riemann integral\} .

Proof. The proof of (1.2) is omitted (see Hille-Philitips (1957), p.306). In order to prove (i) and (ii) we need the following lemma.

Lemma. Let $F \in C\left(\mathbb{R}^{+}, \mathbb{R}^{+}\right)$be such that $\int_{0}^{\infty} F(t)$ dt exists. If there is a positive number m and an interval [0, $n]$ such that $F(t+s) \leqq$ $m$.F(s) for all $s \geq 0$ and $t \in[0, n]$, then $\lim _{s \rightarrow \infty} F(s)=0$.

Proof of the lemma. For all $s>0$ there exists a>0 such that $A(a):=\int_{a}^{\infty} F(s) d s, \frac{n}{m} \cdot \varepsilon$. For all $t>a+n$ there exists $r \in[t-n, t]$ such that $F(r) \leq{\underset{\sim}{n}}_{1}^{1} \cdot A(a)$.
Therefore, $F(t)=F(t-r+r) \leqq m \cdot F(r) \leqq \frac{m}{n} \cdot A(a) \leqq \varepsilon$.

In order to prove (i) we define $b ;=\operatorname{inf(Re\lambda }: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\|^{\prime} d t$ exists). A straightforward application of the lemma shows that $\mu(f) \leqslant b$. The definition of $u(f)$ gives the reverse inequality. It remains to prove statement (ii) of Thm. 1.3 .
Assume that ker $A=\{0\}$ and let $f \in D(A), \lambda \in \mathbb{C}$ with $\operatorname{Re} \lambda>$ (f). From the equation
$$
\int_{0}^{t} e^{-\lambda s} T(s) \lambda f d s=e^{-\lambda t} T(t) f-f+\lambda \int_{0}^{t} e^{-\lambda s} T(s) f d s
$$
it follows that $\int_{0}^{\infty} e^{-\lambda s} T(s) A f d s$ exists,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-113.jpg?height=64&width=1431&top_left_y=2147&top_left_x=221)

Next we show that $b<0$ implies $b \leqq m(f)$. Suppose $b<0$, Then, $b y(1,1), \int_{0}^{\infty} T(s) A f d s$ exists, By $\int_{0}^{T} T(s) A f d s=T(r) f-f$ we see that $l_{i m} r_{\rightarrow \infty} T(r) f=: g$ exists. But, for every $t \geqq 0, T(t) g=g$ and therefore $g \in \operatorname{Ker} A$ or $g=0$, Hence $\int_{t}^{\infty} T(s) A f d s=-T(t) f$. Then choosing $r, b < r<0$, and integrating by parts we obtain
$-T(t) f=\operatorname{Lim}{ }_{u \rightarrow \infty} \int_{t}^{u} e^{r s} e^{-r s} T(s) A f d s$
$=\lim u_{\rightarrow \infty}\left(e^{r u} \int_{0}^{u} e^{-r g} T(s) A f d s-e^{r t} \int_{0}^{t} e^{-r s} T(s) A f d s\right.$ $\left.-I \int_{t}^{u} e^{r s} \int_{0}^{s} e^{-r v} T(v) A f d v d s\right)$
$=-e^{r t} \int_{0}^{t} e^{-r s} T(s) A f d s-r \int_{t}^{\infty} e^{r s} \int_{0}^{s} e^{\sim r v} T(v) A f d v d s$.
From $\left\|\int_{0}^{t} e^{-r s} T(s) A f d s\right\| \leq M$ for some $M$ and every $t \geqq 0$ we con clude that $\|T(t) f\| \leqq \vec{A} e^{r t}$ for all $t \geqq 0$ and some constant $\vec{M}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-114.jpg?height=52&width=1300&top_left_y=708&top_left_x=207)
If $b \geqq 0$ and $w>b$, then $\left[\int_{0}^{t} e^{-w s} T(s) A f d s \| \leqq M\right.$ for $a l l$ $t \geqslant 0$. By $T(t) f-f=\int_{0}^{t} e^{W G} e^{-w s} T(s) A f d s$
$$
=e^{w t} \int_{0}^{t} e^{-w s} T(s) \hat{A} f d s-W \int_{0}^{t} e^{w s} \int_{0}^{s} e^{-W I} T(r) A f d r d s
$$
we obtain $\|T(t) f \sim E\|\left\{M e^{w t}+M\left(e^{w t} \sim 1\right) \leqq 2 M e^{w t}\right.$. Hence w(f) $\leq w$ for every $w>b$, i.e., $\quad(f) \leqq b$.

From (1.2) and the Uniform Boundedness Principle it follows that the growth bound ${ }^{\omega}(A)=\sup (\dot{A}(f): f \in D(A)\}$ satisfies
(1.3) $w_{1}(A)=\operatorname{inf(w:for}$ every $f \in D(A)$ there exists a constant $M$ such that $\|T(t) f\| \leqq M e^{w t}$ for every $\left.t \geq 0\right\}$
$$
=1 i m \sup _{t \rightarrow \infty} 1 / t+\log \|T(t) R(\lambda, A)\| \quad(\lambda \in \rho(A))
$$

The subsequent theorem will be of particular importance in the stability theory of positive semigroups. We show that the constant ${ }^{4}$ (A) coincides with the abscissa of simple convergence of the Laplace transform of the semigroup and with the abscissa of absolute convergence of the Laplace transform of the strong solutions of (ACP).

Theorem 1.4. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$. Then
(1.4) $\quad \omega_{1}(A)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t\right.$ exists as an improper Riemann integral for every $f \in E\}$
$$
=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} \text { lie }-\lambda t \mathrm{~T}(\mathrm{t}) \mathrm{fl} \mathrm{l} \mathrm{dt}\right. \text { exists for every }
$$
$$
f \in D(A)\} .
$$

Remarks. (a) One can show that the abscissas of uniform, strong and weak convergence of the Laplace transform coincide isee C-IIT, Thm. 1.2 , last part of the proof). Therefore, by Thm.1.4,
$$
\begin{align*}
& \left.{ }^{\omega}\right]_{1}(A)=\inf \left(\mathrm{ke} \lambda: \text { weakwlim} t \rightarrow \infty \quad \int_{0}^{t} e^{-\lambda s} T(s) \text { ds exists }\right\}  \tag{1.5}\\
& =\inf \left\{\operatorname{Re} \lambda: \text { uniform-1im}{ }_{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s)\right. \text { ds exists\}. }
\end{align*}
$$
(b) In the equations (1.4) and (1.5) the term "Re $\lambda$ " may be replaced by ${ }^{n \lambda} \in \mathbb{R}^{\prime \prime}$ (use (1.1)).

Proof of Thm.l.4. The equality ${ }^{\omega} l^{(A)}=\operatorname{inf(Re} \lambda=\int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t$ exists for all $f \in D(A)\}$ follows from the definition of ${ }_{\mathrm{H}}(\mathrm{A})$ and the lemma used in the proof of Thm. 1,3 .
We prove $\omega_{1}(A)=\operatorname{inf(Re} \lambda: \int_{0}^{\infty} e^{-\lambda s_{T}}(s) f d s$ exists for every $\left.f \in E\right\}$. The identity
$$
T(t) f=e^{\lambda t}\left(f-\int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f d s\right)
$$
yields
${ }^{\mu} l^{(A)} \leqq \inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t\right.$ exists for every f $f$ im $\left.(\lambda-\lambda)\right\}$. Therefore
${ }_{\omega}(A) \leqq \inf \left\{\right.$ Re $\lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t$ exists for every $\left.f \in E\right\}=: b$. Take $\lambda \in \mathbb{C}$ with Re $\lambda>{ }^{\prime}{ }_{1}(A)$. Then $\int_{0}^{\infty} e^{-\lambda t} T(t) f$ dt exists for every $f \in D(A)$. Define $g:=\int_{0}^{1} e^{-\lambda t} T(t) f d t$. Then $g \in D(A)$ and $\int_{0}^{n} e^{-\lambda t} T(t) f d t=\sum_{k=0}^{n-1} e^{-\lambda k} T(k) g$. Since $\operatorname{Re} \lambda>\omega_{1}(A)$ it follows that the sum converges for every $g \in D(A)$. Therefore the integral converges as $n \rightarrow \infty \quad\left(n \in N\right.$ for every $f \in E$. For every $t \in \mathbb{R}_{+}$ define a bounded operator $T_{t}$ by $f * \int_{0}^{t} e^{-h s} T(s) f d s$. As seen above, $T_{n}{ }^{f}$ converges as $n \rightarrow m(n \in N i$ for every $f \in E$. It follows from the Uniform Boundedness Principle that the family ( $\mathrm{T}_{\mathrm{n}}$ ) $\mathrm{n} \in \mathrm{d}$ is uniformly bounded.
For every $t \in \mathbb{R}+$ there exist $n \in \mathbb{N}$ and $t^{\prime} \in[0,1)$ such that $T_{t}=T_{t}+e^{-\lambda t^{\prime}} T^{\prime}\left(t^{\prime}\right) T_{n}$. Since the operator families on the right side of the equation are uniformly bounded the same is true for $\left(T_{t}\right)_{t a 0}$. Since ( $\left.T_{t}{ }^{f}\right){ }_{t} \geqslant 0$ converges for every $f \in D(A)$ it follows that $\left(T_{t}{ }^{f}\right) t \geqq 0$ converges for every $f \in E$. Thus $b \leqslant w^{(A)}$.

The inequality
$\mathbb{M}(A) \geqq \inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t\right.$ exists for every $\left.f \in E\right\}$ in combination with the lemma of Thm.l. 3 implies that the growth bound w(A) coincides with the abscissa of absolute convergence of the Laplace transform of $(T(t))_{t \geq 0}$; i.e..
$(1,6) \quad \mu(A)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|_{0} e^{-\lambda t} T(t) f\right\| d t\right.$ existsfor every $\left.f \in E\right\}$.
$A s$ seen in A-I, Prop.1.11, if $\quad \int_{0}^{\infty} e^{-\lambda t} T(t) f$ dt exists for every $f \in E$, then $\lambda \in f(A)$ and $R(h, A) f=\int_{0}^{\infty} e^{-\lambda t} T(t) f d t$. This and Thm.l. 4 yield the following corollary.

Corollary $1.5 . \quad$ Let $\boldsymbol{R}^{\prime}$ be the generator of a strongly continuous semigroup (T(t)) $\quad(\xi 0$ on a Banach space E Then
$$
s(A) \leftrightarrows \omega^{\circ}(A) \leftrightarrows
$$

Example 1.2.(2) shows that the uniform exponential stability of the
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-116.jpg?height=49&width=1611&top_left_y=638&top_left_x=214) following example we will see that not only the semigroup ii.e.r all generalized solutions of (ACP)), but also the strong solutiong can be ungtable even when $g(A)<0$. In fact, we will give an example of a semigroup with $s(A)<\omega_{1}(A)<\Leftrightarrow\left(A_{1}\right)$.

Example $1.6, ~ 5 n A-I I I, E x .1 .4$ it was shown that the semigroup (T(t)) $t \leq 0$ on the Hilbert space $E=\left\{1 x^{1}, x^{2}, \ldots, x^{n} \in \mathbb{E}^{n}: \sum_{i=1}^{\infty}\left\|x^{i}\right\| \in \infty\right\}$ given by $T(t):=\left(e^{2 \pi i n t} \exp \left(\tan _{n}\right)\right)_{n \in \mathbb{N}}$ with
$$
A_{n}=\left\{\begin{array}{ccccc}
0 & 1 & 0 & \ldots & 0 \\
\cdot & . & & & 0 \\
\cdots & & \cdots & & 0 \\
\cdots & & & . & 1
\end{array}\right]_{n \times n}
$$
has growth $e^{t}\left(\|T(t)\|=e^{t}\right)$. Thus $\quad\left(\mathcal{R}_{2}\right)=1$ whereas the generator $A:\left(2 \pi i n+\beta_{n}\right){ }_{n} \in \mathbb{N}$ has spectral bound 0 . We will show first that for this semigroup $\psi_{1}(A)=$ (A) holds (we will uge thig to construct a
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-116.jpg?height=61&width=852&top_left_y=1663&top_left_x=214)
Let $e_{n}=n^{-1 / 2},(1, \ldots, 1) \in c^{n}$, Then we have
$\left\|\exp \left(\tan _{n}\right) \cdot e_{n}\right\|^{2}=$
$$
=\frac{1}{n} \cdot\left\|\left(1+t+\ldots+\frac{t^{n-1}}{(n-1)!}, 1+t+\ldots+\frac{t^{n-2}}{(n-2)!} \ldots, 1+t, 1\right)\right\|^{2}=
$$
$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1}\left(\sum_{j=0}^{r} \frac{1}{j!} \cdot t^{j}\right)^{2}=
$$
$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1}\left(\sum_{j, s, 0}^{I}, \frac{1}{j!s+} \cdot t^{j+s}\right)=
$$
$$
=\frac{1}{n} \cdot \sum_{\mathrm{r}=0}^{\mathrm{n}-1} \sum_{i=0}^{2 r} t^{i} \sum_{j+s=i} \frac{1}{j!5!}=
$$
$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1} \sum_{i=0}^{2 r} \frac{t^{i}}{i!} \sum_{j=0}^{i}\binom{i}{j}=
$$
$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1} \sum_{i=0}^{2 r} \frac{1}{i!}(2 t)^{i}
$$
$$
\equiv \frac{1}{\Omega^{2}} \cdot \sum_{j=0}^{n+1} \frac{1}{i!}(2 t)^{i}
$$

For $0<G<1$ we consider $x_{G} \in$ fit defined as follows
$$
x_{q}:=\left(q * e_{1}, 2 q^{2} e_{2}, \ldots+q^{n} e_{n}, \ldots\right)
$$

Then $X_{q} \in D(A)$ and
$$
\begin{aligned}
\left\|T(t) x_{q}\right\|^{2} & =\sum_{n=1}^{\infty} n^{2} q^{2 n}\left\|\exp \left(t A_{n}\right) e_{n}\right\|^{2} \geqq \\
& \geqq \sum_{n=1}^{\infty} n^{2} q^{2 n}\left(\frac{1}{n^{2}} \cdot \sum_{i=0}^{n=1} \frac{1}{i!}(2 t)^{i}\right) \\
& =\sum_{i=0}^{\infty} \sum_{n=i+1}^{\infty}\left(q^{2 n} \cdot \frac{1}{i!}(2 t)^{i}\right) \\
& =\sum_{i=0}^{\infty} q^{2 i+2} \cdot\left(1-q^{2}\right)^{-1} \cdot \frac{1}{i!}(2 t)^{i}= \\
& =\frac{q^{2}}{1-q^{2}} \cdot \sum_{i=0}^{\infty} \frac{1}{i!}\left(2 t q^{2}\right)^{i}=\frac{q^{2}}{1-q^{2}} \cdot e^{2 t q^{2}} .
\end{aligned}
$$

It follows that $\left(x_{q}\right) \geqq q^{2}$. Thus
$$
1=\sup \left\{\omega\left(x_{q}\right): 0<q<1\right\} \leqq \omega_{1}(A) \leq \mu(A)=1 .
$$

Rescaling the semigroup (i.e. looking at $e^{-3 / 2 \cdot t} T(t)$ ) we obtain a semigroup generator $\vec{A}$ on the Hilbert space $E$ with $-3 / 2=5(\bar{A})$ and $\omega_{1}(A)=\omega(A)=-1 / 2$. On the other hand, Example 1.2. (2) yields a semigroup on a Banach space $F$ with generator $B$ such that $-1=s(B)=\omega_{1}(B)$ while $\omega(B)=0$. Now the operator $C:=A \oplus B$ on the Banach space $E \Phi F$ is a semigroup generator for which
$s(C)=\max \{s(A), s(B)\}=-1,{ }^{\omega} 1(C)=\max \left\{\omega_{1}(A){ }_{f} \omega_{1}(B)\right\}=-1 / 2$ and
$\omega(C)=\max \{\omega(A), \omega(B)\}=0$.
(1.7) Important remark: For eventually nom continuous semigroups, in particular for compact, differentiable, holomorphic or nilpotent semigroups the spectral mapping theorem o(T(t)) $\{0\}=\mathrm{e}^{\mathrm{to}(\mathrm{A})}$ holds, and therefore
$$
\begin{equation*}
\Sigma(A)=\omega_{1}(\bar{A})=\omega(A) \tag{1,8}
\end{equation*}
$$
is valid (Cor.1.5 and AmIII, Cor.6.7).
Hence, if $A$ is the generator of an eventually norm continuous semigroup, then the exponential growth bounds of the strong and the mild solutions of $\dot{u}(t)=A u(t)$ are determined by the spectral bound $s(A)=\sup \{\operatorname{Re} \lambda: \lambda \in o(A)\}$.

In general, the growth bound w(A) can be obtained through the Hille-Yosida theorem (see $\mathrm{A}-\mathrm{II}, \mathrm{Thm}, 1,7$ ) as
(1.9) $\quad \omega(A)=\inf \left\{w:\left\|R(\lambda, A)^{n}\right\| \leq M \cdot(\operatorname{Re} \lambda-w)^{-n}\right.$ for some $M$ and every $n \in A$ and $\lambda \in \mathbb{C}$ with $k e \lambda>w)$.

In view of the difficulties in estimating all powers of the resolvent this equation is of little practical interest. If $A$ is the generator
of a semigroup on a Hilbert space $H$, then it is shown in $\bar{A} w I I$, Cor.7.ll that
(1.10) $\quad 山(A)=\inf \left(w:\|R(\lambda, A)\|_{i} \leq M_{W}\right.$ for Re $\left.\lambda>w\right\}$.

Unfortunately, the identity (1.10) does not hold on arbitrary Banach spaces, but we will see in section 1 of $C=I v$ that for every positive semigroup on a Banach lattice the identity
(1.11) $s(A)={ }_{\omega} 1(A)=\inf \left\{w:\|R(\lambda, A)\| \leq M_{w}\right.$ for $\left.\operatorname{Re} \lambda>w\right\}$
is valid. Therefore, for positive semigroups with $s(A)={ }_{\omega}(A)<(A)$ (see Ex.1.2.(2)) the equation (1.10) is not true. However, we can prove the following theorem.

Theorem 1.9. Let $A$ be the generator of a strongly continuous semiw group ( $T(t))_{t \geq 0}$ on a Banach space $E$. If there are constants $a \geqq 0$ and $q \geqslant s(A)$ and if there are $C \in \mathbb{H}_{+}, n \in \mathbb{N}$ such that, for every $\lambda \in \mathbb{C}$ with $\operatorname{Re} \lambda>g$ and $\left|I_{m} \lambda\right|>a$ we have $\|R(\lambda, A)\| \leqq C|\lambda|^{n-2}$, then $\sup \left\{u(f), f \in D\left(A^{n}\right)\right\} \geqq G$.

Proof. The hypothesis $\|R(\lambda, A)\| \leqq C|\lambda|^{n-2}$ is invariant under rescaling; i.e., the resolvent $R(\lambda,-b+A)$ of the generator $-b+A$ of the rescaled semigroup $e^{-b t} T(t)$ satisfies $\|R(\lambda,-b+A)\| \cong \tilde{C}|\lambda|^{n-2}$ for every $\lambda \in \mathbb{C}$ with Re $\lambda>q m b$ and $\mid$ Im $\lambda \mid>a+2 b$ and a suitable constant $\bar{C}$. Therefore we may assume that $b:=\max (\omega(A), q)<0$, Let $\omega(A) < p <0$. Then, by the inversion formula for the Laplace transform for every $f \in D(A)$ and $p^{\prime}=\max \{p, q\}<0$,
$$
\begin{equation*}
T(t) f=\frac{1}{2 \pi i} \cdot \int_{P^{\prime} \sim i \infty}^{P^{\prime}+i \infty} e^{\lambda t} R(\lambda, \bar{A}) f d \lambda . \tag{1.12}
\end{equation*}
$$
(For a proof of the vector valued version of the inverrion formula one may follow [widder (1946), p. 66?; also see the notes to this section.)
By the resolvent equation we obtain
$$
R(\lambda, A) R(0, A)^{n}=\sum_{k=1}^{n}(-1)^{k+1} \cdot \lambda^{-k} R(0, A)^{n+1-k}+(-1)^{n} \cdot \lambda^{-n} R(\lambda, A) .
$$

Using that $\frac{1}{2 \pi i^{\prime}} \cdot \int_{\mathrm{P}^{\prime}-\mathrm{im}}^{\mathrm{P}^{\prime}+\mathrm{im}} \mathrm{e}^{\lambda t} \cdot \lambda^{-k} \mathrm{~d}_{\lambda}=0$ for $\mathrm{k} \geqq 1, \mathrm{p}^{\prime}<0$ and $\mathrm{t}>0$ we obtain
(1.13) $T(t) R(0, A)^{n_{f}}=(\sim 1)^{n} \cdot \frac{1}{2 \pi i} \cdot \int_{P^{\prime}-i=1 \infty}^{P^{\prime}+i=} e^{\lambda t} \cdot \lambda^{-n} R(\lambda, A) f(\lambda$
for every $f \in E$ and $t>0$.
If $G \in P^{\prime}$, then, by Cauchy's Integral Theorem and since $\|R(\lambda, A)\|$ $c \cdot|\lambda|^{n-2}$ we see that the path of integration can be shifted to Reג = q ;
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-118.jpg?height=86&width=1338&top_left_y=2567&top_left_x=219)

Therefore $\left\|T(t) R(0, A)^{n} f\right\| \leqq c^{\prime} e^{q t}\|f\| \int_{-m}^{m}\left(q^{2}+s^{2}\right)^{-l} d s=M^{2} e^{q t} \cdot\|f\|^{\prime}$ or $\|T(t) f\| \leqq M \cdot e^{q t}\left\|_{R^{n}} f\right\|$ for $f \in D\left(A^{n}\right)$.

In view of the characterizations given in section 1 of $A-I I$, the semigroups occuring in the theorem are holomorphic if $n=1$. In this case one may apply (1.7) to obtain the stronger statement (1.8).

Instead of making assumptions on the resolvent of $A$ we now take a different view and characterize the property ${ }^{n} \omega(A)<0 "$ in terms of the semigroup $(T(t))_{t \geqslant 0}$ directly.

Proposition 1.10 . Let $A$ be the generator of the strongly continuous semigroup ( $T(t))_{t \geqq 0}$. Then the following statements are equivalent:
(a) $\omega(A)<0$
(b) $\quad \lim _{t \rightarrow \infty}\left\|_{i} T(t)\right\|=0$
(c) $\left\|T\left(t^{\prime}\right)\right\|<1$ for some $t^{\prime}>0$.

Proof. The only nontrivial implication (c) $\rightarrow(a)$ follows from
$\omega(A)=\lim _{t+\infty} \frac{1}{t} \log \|T(t)\| \quad(\operatorname{see} A-I,(1.1))$ and $\frac{\log \|T(t)\|}{t} \leqslant \frac{\log \left\|T\left(t^{*}\right)\right\|^{i}}{t^{\prime}}+\frac{\log \|T(t)\|_{i}}{n t^{t}+s}$ for $t=n t^{\prime}+s, s \in\left[0, t^{\prime}\right)$.

Other less obvious characterizations of the property "w( A$)<0$ " are given in the next theorem. The equivalence of (a) and (c) is known as Datko's Theorem.

Theorem 1.11 . Let $A$ be the generator of a strongly continuous semigroup ( $T(t)$ ) $t \geqq 0$ on a Banach space $E$. Then the following statements are equivalent:
(a) $\quad \infty(A)<0$.
(b) $s(A)<0$ and there is $t_{0}>0$ such that
$$
|\lambda|<1 \text { for every } \lambda \in \operatorname{Ao}\left(T\left(t_{0}\right)\right)
$$
(c) For every (some) psl exists $\int_{0}^{\infty}\|T(t) f\|^{P} d t$ for every $f \in E$.

Proof. The implication ${ }^{\prime \prime}(a) \rightarrow(b)$ follows from $r(T(t))=e^{a(A) t} \varepsilon I$ and $s(A) \leqq w(A)<0$. For the point and residual spectrum the spectral mapping theorem is valid (see $A-I I I, T h m .6 .3$ ). The approximate point spectrum is closed, hence the additional information in (ii)
implies $|\lambda| \leq r<1$ for some $r$ and each $\left.\lambda \in \operatorname{Aof}\left(t_{o}\right)\right)$. Conseu quently, $\exp \left(\omega(A) \cdot t_{0}=I\left(T\left(t_{O}\right)\right) \leqq \max \left(\exp \left(t_{0} \cdot s(A)\right), r\right)\right\} \ll \quad$ or $\omega(A)<0$. This proves $"(b) \rightarrow(a) "$. For a proof of the equivalence of (a) and (c) we refer to Datko (1972) or Pazy (1983), Thm.4.4.1.

Rescaling a given semigroup (T(t)) $t \geq 0$ one obtains the following corollary from (1.1) and statement (c) of the above theorem.

Corollary 1.12 . Let $(T(t)) t \geq 0$ be a strongly continuous semigroup on a Banach space $E$. Then the set of complex numbers $\lambda$ for which $\int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t$ exists for every $f \in E$ is an open right halfplane.

In the next theorem we give two necessary conditions for stability of (T(t)) $t \geq 0$ in terms of the generator $A$. We will see in Chapter $C-I V$ that for positive semigroups a condition similar to statement (ii) below is even sufficient for stability of the semigroup. We emphasize that stable semigroups need not be uniformly bounded (see Ex. $1.2(3)$ ) and that $s(A)=\omega(A)=0$ does not imply boundedness or even stabil~ ity of the semigroup (see also $A-I$, Ex.1.4.(i)).

Theorem 1.13. Let $A$ be the generator of a stable semigroup (T(t)) $t \supseteq 0$ on a Banach space $E$. Then the following asgertions hold:
(i) $\quad g(A) \equiv 0$ and $\operatorname{Re} \lambda \in 0$ for every $\lambda \in \operatorname{Po}(A) \cup R o(A)$.
(ii) $\lim _{\lambda \rightarrow 0+} h_{R}(\lambda, A) f$ exists for every $f \in D(A)$.

Proof. (i) If (T(t)) $t \geqslant 0$ is stable, then $\|T(t) f\| \leqq M_{f}$ Eor every $\mathrm{f} \in \mathrm{D}(\mathrm{A})$. Therefore $\mathrm{s}(\mathrm{A}) \subseteq \omega_{1}(\mathrm{~A}) \leqq 0$.
Assume there is $\lambda \in \operatorname{Po}(A)$ with Re $\lambda=0$. Then by $A w I I, C o r .6 .4$ there is $g \neq 0$ such that $T(t) g=e^{h t} g$ for all $t$ a . Since $\left|e^{\lambda t}\right|=1$ this contradicts the stability of the semigroup. Assume there is $\lambda \in \operatorname{Ro}(A)=P \sigma\left(A^{\prime}\right)$ with Re $\lambda=0$. Then there is $0 \neq \Phi \in E^{\prime}$ with $T(t)^{*} \Phi=\exp (\lambda t) \cdot \Phi$ for all $t \geqq 0$. Choose $f \in D(\bar{A})$ such that $\langle f, \phi\rangle \neq 0$. Then $|\langle T(t) f, \Phi\rangle|=|\langle f, \Phi\rangle|>0$ for every $t \geqq 0$ which contradicts the stability of the semigroup.
(ii) From the stability of the semigroup and the identity
$\int_{0}^{t} T(s) A f d s=T(t) f-f$ we see that $\int_{0}^{\infty} T(s) A f$ ds exists for every $f \in D(A)$. But ${ }^{\mu} 1(A) \leqq 0$ and hence $R(\lambda, A) A f=\int_{0}^{\infty} e^{-\lambda s} T(s) A f d s$ for every $\lambda>0$ (see Thm.1.4). By a classical theorem of Laplace transform theory (for a proof of the vector valued version one may
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-121.jpg?height=67&width=1620&top_left_y=275&top_left_x=224) and is equal to $\int_{0}^{m} T(s) A f d a$. The identity $R(\lambda, A) A f=\lambda R(h, A) f-f$ yields the existence of $1 \mathrm{im}_{\lambda \rightarrow 0+} \lambda \mathrm{R}(\lambda, A) \mathrm{f}$ for every $\mathrm{f} \in \mathrm{D}(\mathrm{A})$.

Bounded holomorphic semigroups (see AwI, Def.l.ll) satisfy $\| A T(t) \mid E m \cdot t^{-1}$ [Goldstein (1985a), p.33], hence $T(t) f \rightarrow 0$ as $t \rightarrow \infty$ whenever $£ \in$ im $A$. If im $A$ is dense (i.e., 0 ( $R_{g}(A)$ ) we obtain uniform atability and the following corollary.

Corollary 1.14. Let $A$ be the generator of a bounded holomorphic semigroup $(T(t)) t \geqslant 0$ on a Banach space $E$. Then the following statements are equivalent.
(a) $0 \leqslant P_{\sigma}(\bar{A}) \cup R_{\sigma}(A)$.
(b) $(T(t))_{t \geq 0}$ is uniformly stable.

Example 1.15 The Laplacian $A$ generates a bounded holomorphic semi* groups on $L^{\mathrm{P}}\left(\mathbb{R}^{n}\right)$ for $\pm \leq p<\infty$ (see the example proceeding Cor.l. 13 of Chap. $A-I I$ ). All solutions of $\Delta f=0$ are either constant or unbounded, therefore $0 \underset{f}{f} \quad \mathrm{O}(\Delta)$. If $1 < p <\infty$, then the adjoint of the Laplacian on $L^{P}\left(\mathbb{R}^{n}\right)$ is the Laplacian on $L^{q}\left(\mathbb{R}^{n}\right)$ where $\frac{1}{\mathrm{p}}+\frac{1}{\mathrm{q}}=1$. Therefore $0 \not \equiv \operatorname{Ro}(\Delta) \cup \operatorname{Po}\left(\Delta^{\prime}\right)$ and we obtain by Cor.1.14 that $\Delta$ generates uniformly atable semigroups on the space $L^{P}\left(\mathbb{R}^{n}\right)$ for $1 < p <\infty$ which are, by ims $\neq L^{P}\left(\mathbb{R}^{n}\right)$ and cor.l.5, not exponenw tially stable.

As seen in Thm. 1.4, exponential stability can be defined by saying that the abscissa of convergence of the Laplace transform of (T (t)) $t \geqq 0$ is less than zero. This should be compared to the assertion of our final theorem.

Theorem l. L6. Let $A$ be the generator of a strongly continuous semigroup (T(t)) te0 on a Banach space $E$. The following assertions are equivalent:
(a) (T(t)) $t \geq 0$ is stable.
(b) ker $A=\{0\}$ and $\int_{0}^{\infty} T(t) \neq d t$ exists for allfimin.

Furthermore the following statements are equivalent:
(a') (T(t)) $t \geqslant 0$ is stable and bounded.
(b') (T(t)) $t \geq 0$ is uniformly stable.
(c') (T(t)) $t$ ( ${ }^{\prime} 0$ is bounded and there is a dense subspace $D$ such that $\quad \int_{0}^{\infty} T(t) f d t$ exists for every $f \in D$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-122.jpg?height=79&width=1615&top_left_y=563&top_left_x=209) $\int_{0}^{t} T(s) A f d s=T(t) f-f, \quad-f$ as $t \rightarrow$. . Therefore (al implies (b). On the other hand, if $\int_{0}^{t} T(s) h f d s$ converges as $t * \infty$, then, by the equation above, $g:=1 i m l_{t \rightarrow \infty} T(t) f$ exists. But ker $A=\{0\}$ and therefore $g=0$. This proves " $(b) \rightarrow(a)^{\prime \prime}$.
The implication " $\left(a^{\prime}\right) \rightarrow\left(b^{\prime}\right) "$ is obvious. If $T(t) f \rightarrow 0$ for every $f \in E$, then $\|T(t)\| \leq M$ and $0 \notin \operatorname{Ro}(A) \quad$ (Thm.1.12). Therefore $D:=\operatorname{im} A$ is dense and $\int_{0}^{\infty} T(t) f d t$ exists for every $f \in D$. This proves " (b') $\rightarrow\left(c^{\prime}\right)^{\prime \prime}$. We have to show that (c') implies (a'). Define $G:=\left\{h \in E: h=\int_{0}^{\infty} T(t) g d t\right.$ for some $\left.g \in D\right\}$. We will show that $G$ is dense in $E$. First we notice that $g \sim T(s) g \in D$ when ever $g \in D$ and $s \in \mathbb{R}_{+}$.
Define $h_{s}=\frac{1}{s} \cdot \int_{0}^{\infty} T(t)(g-T(s) g) d t=\frac{1}{s} \cdot \int_{O}^{s} T(t) g$ dt. Then $h_{s} \in G$ and $h_{s}+g$ as $s * 0$. Therefore $D \subset \bar{G}$ or $\bar{G}=E$. Now let $h \in G$. Then $T(t) h=T(t) \int_{0}^{\infty} T(s) g d s=\int_{t}^{\infty} T(s) g d s \rightarrow 0$ as $t \rightarrow \infty$. But $\|T(t)\| \in M$ and therefore $T(t) f * 0$ for every $f \in E$.

Remarks 1.17. (a) If $B$ is the generator of a stable semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$, then, by the previous theorem, im $A=\left\{f \in E: \int_{0}^{\infty} T(t) f\right.$ dt exists $\}=H$.
If $g \in H$, then $\int_{0}^{\infty} T(t) g d t \in D(A)$ and $A \int_{0}^{\infty} T(t) g d t=-g$. Therew fore $g \in i m h$ and we obtain that the dense subspace im $A$ is given by
(1.14) $\quad$ im $A=\left\{f \in E: \int_{0}^{\infty} T(t) f d t\right.$ exists $\}$
in case that $A$ is the generator of a stable semigroup ( $T(t)$ ) $t \geqq 0$.
(b) If $u(f)<0$ for every $f \in D(A)$, then (T(t)) is stable (but might not be exponentially stable if
$0=H_{1}(A)=\sup (u(f): f \in D(A)\}$. In this case it can be seen by a proof similar to the one of Thm. 1.4, that o(A) has to be contained in the open left half-plane; i.e. Fe $\lambda<0$ for $\lambda \in \sigma(A)$.
(c) If one defines a semigroup (T(t)) tap to be weakly stable if $<T(t) f, \Phi>0$ as $t \rightarrow \infty$ for every $f \in D(A)$ and $\Phi \in E \prime$ or as weakly uniformly stable if $\langle T(t) f, \Phi\rangle \rightarrow 0$ as $t * \infty$ for every $f \in E$ and $\phi \in E$, then Theorem 1.13 and 1.16 can be reformulated in a
weak form (i.e.; we replace stable by weakly stable and 'lim' by 'weak-lim'). The proofs require only some obvious modifications.
If $A$ has a compact resolvent or $i$ : $A$ is the generator of a bounded holomorphic semigroup, then weak stability implies stability. In general, this is no longer true; e.g., the translation semigroup on $L^{2}(\mathbb{R})$ is weakly uniformly stable but not stable (see also BuTV,Ex.1.2).

\section*{2. STABIJITY: INHOMOGENEOUS CASE}

Wring the results of the first section, we now investigate the long term behavior of the solutions of the inhomogeneous initial value problem
$$
\begin{equation*}
\dot{u}(t) \Rightarrow A u(t)+F(t) \quad, \quad u(0)=f \tag{2.1}
\end{equation*}
$$
where $A$ is the generator of a strongly continuous semigroup on a Banach space $E$ and $F(\cdot)$ is a locally integrable function from $\mathbb{R}+$ into $E$ called forcing_term. A function $u(*)$ is called a (strong) solution of (2.1) if $u\left({ }^{\circ}\right): \mathbb{R}_{+}+D(A), u\left({ }^{*}\right) \in C^{1}\left(R_{+}, E\right)$ and (2.1) is satisfied for $t \geqslant 0$,
The assumption that $A$ is the generator of a semigroup (T(t)) $t \geqq 0$ yields the uniqueness of the solution of (2.1). If u(.) is a solution of (2.1), then the function $v(s):=T(t-s) u(s), 0 \leqq s \leqq t$, is differentiable and $V^{*}(s)=T(t-s) F(s)$. But $F(*)$ is locally integrable, and by $\int_{0}^{t} T(t-s) F(s) d s=v(t)-v(0)=u(t)-T(t) f$ we see that the solution $u(t)$ of (2.1) is given by
$$
\begin{equation*}
u(t)=T(t) f+\int_{0}^{t} T(t-s) F(s) d s \tag{2.2}
\end{equation*}
$$

Example. Let $(T(t)) t \geqq 0$ be not eventually differentiable. Then there exists $g \in E$ such that $t \rightarrow T(t) g$ is not differentiable on ( $0, \infty$ ). The initial value problem $u(t)=A u(t)+T(t) g, u(0)=0$ has no (strong) solution $u(\cdot)$ because otherwise
$$
u(t)=\int_{0}^{t} T(t-s) T(s) g d s=t T(t) g
$$
has to be differentiable on $\mathbb{R}_{+}$.
Whenever the expression (2.2) makes sense we call it a generalized (or mild) solution of (2.1). If $F(*)$ is continuous and $f \in D(A)$, then the generalized solution of (2.1) is a strong solution if and only if $v(t): \int_{0}^{t} T(t-s) F(s) d s$ is differentiable (see Pazy (1983) Chap. 4 ,

Thm, 2.4). There are several sufficient conditions on the generator $A$, the forcing term $F(\cdot)$ or the space $E$ such that every mild solution is a strong solution of (2.1) (see Travis (1979) or Pazy (1983) Sec.4.2).

It is our aim in this section to study the asymptotic behavior of the solutions of (2.1) as $t \rightarrow$. To that purpose we consider absolutely integrable or periodic forcing terms $F(*)$, and assume the semigroup to be uniformly stable.

Similar results for integrable and convergent forcing terms $F(\cdot)$ can be obtained if the semigroup is supposed to be uniformly exponentially stable (see Pazy (1983), p.119 or Neubrander (1985b)). However, if the semigroup is positive, these results even hold for stable semigroups (see Section C-IV). From Theorem 1.13.(i) we recall that for stable semigroups im A is dense in $E$.

Theorem 2, 1. Let $A$ be the generator of a uniformly stable semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$. If there is $g \in i m \mathcal{B}^{\prime}$ such that $\int_{0}^{m}\|F(s)-g\|_{i}^{d s}$ exists, then every generalized solution $u(\cdot)$ of (2,1) converges as $t \rightarrow \infty$ and $\lim _{t \rightarrow \infty} u(t)=$ h where $h \in D(A)$ with $A_{h}=g$.

Proof. If $u(\cdot)$ is a generalized solution of (2,1), then, by (2.2), $u(t)=T(t) f+\int_{0}^{t} T(s) g d s+\int_{0}^{t} T(t-s)(F(s)-g) d s$. By the uniform stability and Thm.l.l4 we see that the first term converges to zero and that the second one converges to h . We have to show that the third term oonverges to zero. Take $g>0$ and $G(s):=F(s)-g$. Then
$$
\begin{aligned}
\left\|\int_{0}^{t} T(t-s) G(s) d s\right\| & \leqq\left\|\int_{0}^{t^{\prime}} T\left(t-t^{\prime}+t^{\prime}-s\right) G(s) d s\right\|+\left\|\int_{t^{\prime}}^{t} T(t-s) G(s) d s\right\| \\
& \leqq\left\|^{\prime} T\left(t-t^{\prime}\right) \int_{0}^{t^{\prime}} T\left(t^{\prime}-s\right) G(s) d s\right\|+M \int_{t^{\prime}}^{*}\|C(s)\| d s .
\end{aligned}
$$

Since the semigroup is uniformly stable we obtain
$T\left(t \sim t^{\prime}\right) \int_{0}^{t^{\prime}} T\left(t^{\prime}-s\right) G(s) d s \quad 0 \quad a s \quad t * 0$ for every $t^{\prime} \geqq 0$. Therefore $\left\|\int_{0}^{t} T(t-s) G(s) d s\right\|_{i} \leqslant E$ for all sufficiently large $t$.

In the subsequent theorem we see that if $A$ is the generator of a uniformly stable semigroup, if the forcing term $F(\cdot)$ is puperiodic and if $\int_{0}^{P} T(p-s) F(s) d s \quad \in \quad i m(I d-T(p))$ (notice that, by Thm.1.13. (i) and A-III, Lemma 5.3, $\overline{\text { im (Id }-T(P))}=E$ ), then (2.1) admits a unique p-periodic, asymptotically stable mild solution.

Lemma 2.2. Let $A$ be the generator of a strongly continuous semigroup (T(t)) $t \geq 0$ on a Banach space $E$ and let $F(\cdot)$ be a p-peri* odic, locally integrable function, $p>0$. Then the following statements are equivalent;
(a) $\dot{u}(t)=\bar{R} u(t)+F(t)$ admits a (unique) generalized p-periodic solution.
(b) There exists a (unique) $f \in E$ such that (Id $-T(p)) f=$ $\int_{o}^{P} T(p-s) F(s) d s$.

Proof. " (a) $\rightarrow(b) "$ Let $f:=u(0)$ be the initial value for which (2.1) has the p-periodic solution. Then we have
$$
\begin{aligned}
u(t)=u(t+p) & =T(t) T(p) f+\int_{0}^{P} T(t+p-s) F(s) d s+\int_{p}^{t+p} T(t+p-s) F(s) d s \\
& =T(t)\left[T(p) f+\int_{0}^{P} T(p-s) F(s) d s\right]+\int_{0}^{t} T(t-s) F(s) d s
\end{aligned}
$$
for every $t \geqq 0$. Therefore $f=u(0)=T(p) f+\int_{0}^{p} T(p-s) F(s) d s$. clearly, if u(.) is a unique periodic solution with u(0) $=\mathrm{E}$, then $f$ is the unique element for which $f=T(p) f+\int_{0}^{P} T(p-s) F(s) d s$ holds.
" (b) $\rightarrow$ (a)". Define u(.) as in (2.2). Then
$u(t+p)=T(t)\left[T(p) E+\int_{0}^{P} T(p-s) F(s) d s\right]+\int_{0}^{t} T(t-s) F(s) d s=u(t)$.

If $f$ is unique, then, by the considerations above, the solution is unique.

Remark 2.3. Let $A$ be the generator of a strongly continuous semigroup ( $T(t)$ ) $t \geqslant 0$ for which the spectral mapping theorem (see $A m I I$, Sec. 6 ) is valid and let $F$ be a puperiodic forcing term. If $\frac{2 \pi i n}{P} \in \rho(A)$ for every $n \in Z$, then, by Lemma 2.2,
$\dot{u}(t)=A u(t)+F(t)$ has a unique puperiodic solution with initial value $(I d-T(p))^{-l}\left(\int_{0}^{P} T(p-s) F(s) d s\right)$.

As a consequence of Thm. 1.13 and $A \sim I I I, C o r .6 .4$, for a uniformly stable semigroup there exists at most one $f \in E$ such that $(I d-T(p)) f=\int_{0}^{p} T(p-s) F(s) d s$. This and Lemma 2.2 is used to prove the following theorem.

Theorem 2.4. Let $A$ be the generator of a uniformly stable semigroup $(T(t))_{t \geqslant 0}$ and let $F(\cdot)$ be a puperiodic locally integrable function such that $(I d-T(p)) f=\int_{o}^{P} T(p-s) F(s) d s$ for some $f \in E$. Then the
unique p-periodic generalized solution
$$
u(t)=T(t) f+\int_{0}^{p} T(p-s) F(s) d s
$$
is asymptotically stable; i.e., for every generalized solution $v(\cdot)$ of (2.1) we have $\mathrm{lim}_{\mathrm{t} \rightarrow+}\|v(\mathrm{t})-\mathrm{u}(\mathrm{t})\|=0$.

Example 2.5. Let $E$ be the Banach space $C_{0}\left(\mathbb{R}_{+}\right) ; A=\frac{d}{d x}$ with $\bar{D}(A)=\left\{f \in E: f^{\prime} \in C^{1}\right.$ and $\left.f^{\prime} \in E\right\}$ is the generator of the uniformly stable translation semigroup $T(t) f(x):=f(t+x)$. Applying (1.14) we obtain that $i m A=\left\{f: \int_{0}^{\infty} f(x) d x\right.$ exists\} is dense in $C_{0}\left(\mathbb{R}_{+}\right)$. Let $r \in \operatorname{im} A_{1}$ and let $F(\cdot)$ be a p-periodic real-valued function.

We apply Theorem 2.4 to the initial value problem
$$
\begin{equation*}
\frac{d}{d t} u(t, x)=\frac{d}{d x} u(t, x)+r(x) F(x+t) \quad, u(0, \cdot) \in D(A) . \tag{*}
\end{equation*}
$$

We may rewrite (*) as
$$
\begin{equation*}
\dot{v}(t)=A v(t)+G(t) \tag{**}
\end{equation*}
$$
where $v(t)=u(t,-)$ and $G: \mathbb{R}_{+} \rightarrow E$ is defined by
$$
G(t)(x)=r(x) F(x+t)
$$
$G \quad i s \quad p$-periodic with values in $E$ and $h_{o}=\int_{o}^{p} T(p-t) G(t)$ dt is the function $x \rightarrow\left[\int_{0}^{P} T(p-t) G(t) d t .7(x)=F(x) \int_{x}^{x+p} r(s) d s\right.$. For the function $f=\int_{k=0}^{\infty} T(k p) h_{0}$, which is given by $x \rightarrow F(x) \int_{x}^{\infty} r(s) d s$, we clearly have (Id - T(p))f $=h_{o}$. Therefore (**) has a unique p-periodic generalized solution (Thm.2.4) although iR $\in$ o( $\mathcal{A}$ ) (compare with Remark 2.3).
The unique p-periodic generalized solution u(t, *) is given by $u(t, x)=F(x+t) \int_{x+t}^{\infty} r(s) d s+F(x+t) \int_{X}^{x+t} I(s) d g=F(x+t) \int_{X}^{\infty} r(s) d s$. For every solution $v(t, \cdot)$ of (*) we have, by Thm. 2.4:
$\sup \left(\left|v(t, x)-F(x+t) \int_{x}^{+} r(s) d s\right|: x \in \mathbb{R}_{+}\right\} \rightarrow 0$ as $t \rightarrow 0$.

WOTES.
Section 1. The exponential growth bounds w(f) and w(A) as well as the characterizations (1.2), (1.6) and Theorem 1.3 (i) can be found in Hille-Phillips (1957). Growth bounds similar to $\omega_{1}$ (A) were considered first in [D'Jacenko (1976) ] and in [Zabczyk (19793, Prop.2]. Example 1.2.(2) is taken Erom wolff (1981); other 'counterexamples' can be Found in Hillemphilltps (1957), Folas (1973), Triggiani (1975), Zabczyk (1975) and Grefner-Vofgt-Nolff (1981). The statements (1.2), (1.6) and Theorem l.3.(1) are semigroup versions of results of classical Laplace transform
theory, see Hille-Phillips (1957) and widder (1946). Theorem 1.3. (f. () is a semigroup version of Theorem 1.2 .7 and 1.2 .8 fn Doetsch (1950). The lemata in the proof of Thm. 1.3 is taken from Mil'stein (1975). Theorem 1.4 and Corollary 1.5 can be found in Neubrander (1985a). Example 1.6 follows Remark 2 in Zabczyk (1975). Statement ( 1.8 ) is sometimes called the 'spectrum determined growth assumption', see, for example, Triggianf. (1975b). Theorem 1.9 is due to Slemrod (1976). The proor given here is based on a much sharper version of the inversion formula for the Laplace transform, than the one given by HillewFhillips (1957), p.349. Visin Widder (1946), p. 66 or Doetsch (1950), p. 212 one can show the followtng theorem (see Neubrander (1984b)).

Theorem. Let $A$ be the generator of a strongly continuous semigroup (T(t)) t ( on a Eanach space $E$. For every $f \in D(A)$ and $P^{>} \omega_{1}(A)$ we have
$$
T(t) f=\frac{1}{2 \pi i} \int_{P+i^{\infty}}^{p+i^{\infty}} e^{\mu t} R(\mu, A) f d \mu .
$$

The equivalence of the statements (1.12). (1.13) and 'u(A) \& 0 , were observed by many authors, see for example, Balakrishnan (1976), p.178 or Benchimol (1978). Theorem 1.11 is due to Jatko (1970) and Delfour (1974); for a proof see Pazy (1983), p. 116. Theorems 1.13 and 1.16 can be found in Neubrander (1985b) and Corollary l. 14 is due to Komatsu (1969). An example of an unstable semigroup generator a with Re $\mu<0$ for all $\mu \in \sigma(A)$ is given in Datko (1983).

Section 2. For a discusston of well-posedness of lnhonogeneous Cauchy problems we refer to Goldstein (1985a), p. 83 and Pazy (1983), p. 105. Further results on the asymptotic behavtor of the solutions of the inthomogeneous problem can be found in Reo-Hengartner (1974), Zaidnan (1979), Pazy (1983), and Neubrander (1985b). Results simillar to Lemma 2.2 and Theorem 2.4 are due to Prub (1984). For a djscussion of the asyaptotic behtvior of the solutions of $\mathrm{a}^{\prime}(\mathrm{t})=\mathrm{A}(\mathrm{t}) \mathrm{u}(\mathrm{t})+\mathrm{F}(\mathrm{t})$ see Datko (1972) and pazy (1983)sp.172.

\section*{PART B}

\section*{POSITIVE SEMIGROUPS ON $C_{0}(X)$}

CHAPTER B-I

\section*{BASIC RESULTS ON SPACES C C (X)}
by
Rainer Nagel and Ulf Schlotterbeck

This part, of the book is devoted to a study of one-parameter semigroups of operators on spaces of continuous functions of type $C_{0}(X)$, spaces which are Banach lattices of a very special kind. We treat this case separately since we feel that an intermingling with the abstract Banach lattice situation considered in Part $C$ would have made it difficult to appreciate the easy accessibility and the pilot function of methods and results available here. In this chapter we want to fix the notation we are going to use and to collect some basic facts about the spaces we are considering.

If $X$ is a locally compact topological space, then $C_{0}(x)$ denotes the space of all continuous complex-valued functions on $x$ which vanish at infinity, endowed with the supremum-norm. If $X$ is compact, then any continuous function on $x$ "vanishes at infinity" and $C_{0}(X)$ is the space of all continuous functions on $X$. We often write $C(X)$ instead of $C_{0}(X)$ in this situation. We sometimes study real-valued functions and write the corresponding real spaces as $C_{o}(X, \mathbb{R})$ and $C(X, \mathbb{R})$, and the notations $C_{o}(X, C)$ and $C(X, C)$ are used if there is the possibility of confusion between both cases.

\section*{1. ALGEBRAIC AND ORDER-STRUCTURE: IDEALS AND QUOTIENTS}

Any space $C_{0}(X)$ is a commutative $C^{*}$-algebra under the sup-norm and the pointwise multiplication, and by the Gelfand Representation Theorem any commutative $c^{\star}-a l g e b r a ~ c a n, ~ o n ~ t h e ~ o t h e r ~ h a n d, ~ b e ~ c a n o n i-~$ cally represented as an algebra $C_{o}(x)$ on a suitable locally compact space $X$. The algebraic notions of ideal, quotient, homomorphism are
well known and need not be explained further. Another natural and important structure of $C_{o}(X)$ is the pointwise ordering, under which $C_{o}(X, \mathbb{F})$ is a (real) Banach lattice and $C_{o}(X, C)$ a complex Banach lattice in the sense explained in Chapter C-I. Concerning the order structure of $C_{o}(x)$ we use the following notations: For a function $f$ in $C_{0}(\mathrm{X}, \mathbb{R})$
```
f\geqq0 means f(t) }\geq0\mathrm{ for all t & X (f is then called
positive),
f > 0 means that f is positive but does not vanish iden*
    tically,
f >> means that f(t) >0 for all t in X (f is then
called strictly positive).


The notion of an order ideal explained in Chapter $C-I$ applies of course to the Banach lattices $C_{o}(X)$ and might give rise to confusion with the corresponding algebraic notion. However, since we are mainly considering closed ideals and since a closed linear subspace I of $C_{o}(\mathrm{X})$ is a lattice ideal if and only if $I$ is an algebraic ideal, we may and will simply speak of closed ideals without specifying whether we think of the algebraic or the order theoretic meaning of this word. An important and frequently used characterization of these objects is the following: $A$ subspace $I$ of $C_{o}(X)$ is a closed ideal if and only if there exists a closed subset $A$ of $X$ such that a function $f$ belongs to $I$ if and only if $f$ vanishes on $A$. $A$ is of course uniquely determined by $I$ and is called the support of $I$. If $I=I_{A}$ is a closed ideal with support $A$ then $I_{A}$ is naturally isomorphic to $C_{0}(X, A)$ and the quotient $C_{0}^{(X)} / I^{(X)}$ is (under the natural quotient structure) again a Banach algebra and a Banach lattice that can be identified canonically (via the map $f+I+f_{A}$ ) with $C_{0}(A)$.

\section*{2. LINERR FORMS AND DUALITY}

The Riesz Representation Theorem asserts that the dual of $C_{0}(x)$ can be identified in a natural way with the space of bounded regular Borel measures on $X$. While there is no natural algebra structure on this dual, the dual ordering (see $C-I$ ) makes $C_{o}(X)$ ' into a Banach lattice. We will occasionally make use of the order structure of $C_{o}(X)$ ' but since at least its measure theoretic interpretation is supposed to be well-known, it may suffice here to refer to Chapter c-I, Sections 3
and 7 , for a more detailed discussion and to recall some basic notations here: If $H$ is a linear form on $C_{0}(X, B)$ then

means u(f) \geqq 0 for all f \geqq 0 ; th is then called
    positive (positivity automatically implies continuity),
~ > means that }\mu\geqq0\mathrm{ , but }\mu\mathrm{ does not vanish identically,
|>>0 meang that }\mu(f)>0\mathrm{ for any f > O; u is then called
strictly positive.


If $\mu$ is a linear form on $C_{0}(X, C)$, then $H$ can be written uniquely as $\mu_{1}=H_{1}+H_{2}$ where $H_{1}$ and $H_{2}$ map $C_{o}(X, R)$ into $\mathbb{F}$ (decomposition into real and imaginary parts). We call 4 positive (strictly positive) and use the above notations if $H_{2} \# 0$ and $\mu_{1}$ is positive (strictly positive). We point out that strictly positive linear forms need not exist on $C_{o}(X)$, but if $X$ is separable then a strictly positive linear form is obtained by suming a suitable sequence of point measures.

The coincidence of the notions of a closed algebraic and a closed lattice ideal in $C_{0}(X)$ has of course its effect on the algebraic and the lattice theoretic notions of a homomorphism. The case of a homomorphism into another space $C_{0}(Y)$ will be discussed below. As for homomorphisms into the scalar field, we have essentially coincidence between the algebraic and the order theoretic meaning of this word, more exactly: A linear form $\mu \neq 0$ on $C_{0}(X)$ is a lattice homomorphism if and only if $\&$ is, up to normalization, an algebra homonorphism (algebra homomorphisms $\neq 0$ must necessarily have norm 1 ). since the algebra homomorphisms $\neq 0$ on $C_{0}(x)$ are known to be the point measures (denoted by $\delta_{t}$ ) on $X$ and since on the other hand iu is a lattice homomorphism if and only if $|\mu(f)|$ equals $f(|f|)$ for all f , it follows that this latter condition on $w$ is equivalent to bs aby for a suitable $t$ in $x$ and a positive roal number a . This can be summarized by saying that $X$ can be canonically identified, via the map $t \rightarrow \delta_{t}$, with the gubset of the dual $C_{o}(X)$ ' consisting of the non-zero algebra homomorphisms, which is also the set of all normalized lattice homomorphisms. This identification is a topological isomorphism with respect to the weak*-topology of $\mathrm{C}_{\mathrm{O}}(\mathrm{X})^{\prime}$.

\section*{3. LINEAR OPERATORS}

A linear mapping $T$ from $C_{D}(X, \mathbb{R})$ into $C_{O}(Y, \mathbb{R})$ is called
positive (notation: $T \geqq 0$ ), if $T f$ ig a positive function whenever $f$ is positive,
a lattice homomorphism if $|T f|=T|f|$ for all $f$.
a Markov-operator if $X$ and $Y$ are compact and $T$ is a positive operator mapping $1_{X}$ to $1_{Y}$.

In the case of complex scalars $T$ can be decomposed into real and imaginary parts. We call $T$ positive in this situation if the imaginary part of $T$ is $=0$ and the real part is positive. The terms "Markov operator" and "lattice homomorphism" are defined formally in the same way as above. Note that a complex lattice homomorphism is necessarily positive, and that the complexification of a real lattice homomorphism is a complex lattice homomorphism. Positive Operators are always continuous.

Since the adjoint of a Markov operator $T$ maps positive normalized measures into positive normalized measures while the adjoint of an algebra homomorphism (lattice homomorphism) maps point measures into (multiples of) point measures, the adjoint of a Markov lattice homomorphism as well as the adjoint of an algebra homomorphism induces a continuous map $\phi$ from $Y$ (viewed as a subset of the weak dual $C(Y)$ ' $\quad$ into $X$ (viewed as a subset of $C(X)$ ' . This mapping $\phi$ determines $T$ in a natural and unique way, so that the following are equivalent assertions on a linear mapping $T$ from a space $C(X)$ into a space $C(Y)$ :
(a) $T$ is a Markov lattice homomorphism
(b) $T$ is a Markov algebra homomorphism
(c) There exists a continuous map $\phi$ from $Y$ into $X$ such $T f *$ fod for all $f \in C(X)$.

If $T$ is in addition bijective, then the mapping $\phi$ in (c) is a homeomorhism from $Y$ onto $X$. This characterization of homomorphisms carries over mutatis mutandis to situations where the conditions on $\mathrm{X}, \mathrm{Y}$ or $T$ are less restrictive. For later reference we explicitly state:
(i) Let $K$ be compact. Then $T \in L(C(K))$ is a lattice homomorphism if and only if there is a mapping $\phi$ from $K$ into $K$ and a function
$h \in C(K)$ such that $T f(s)=h(s) f(\phi(s))$ holds for all $s \in K$. $\quad$ ( $\quad$ is continuous in every point $t$ with $h(t) \neq 0$.
(ii) Let $X$ be locally compact, $T \in\left(C_{o}(X)\right)$. $T$ is a lattice isomorphism if and only if there is a homeomorhism $\phi$ from $x$ onto $X$ and a bounded continuous function $h$ on $x$ such that $h(s) \geqq \delta>0$ for all $s$ and Tf(s) $\quad$ h(s)f(申(s)) ( $s \in X)$. T is an algebraic *-isomorphism if and only if $T$ is a lattice isomorphism and the function $h$ above is $\equiv 1$.

\title{
CHARACTERTYATION OFPDOSTIVE
}

SEMIGROURS ON CG(X)
by
Wolfgang Rrendt

It lies in the very nature of the theory of one-parameter semigroups that frequently an operator $A$ is known to be a generator but the semigroup is not known explicitly. Thus, since the semigroup is uniquely determined by the generator, it is a central task in the theory to express properties of the semigroup in terms of its generator. In this chapter we do this for two properties. We characterize generators of positive semigroups and generators of lattice semigroups.

In Section 1 we consider a semigroup (T(t)) $t \geqslant 0$ on the real space $C(K)$ ( $K$ compact). It is shown that the semigroup consists of positive operators if and only if its generator satisfies a positive minimum principle (P). Even without assuming a priori that $A$ is a generator the positive minimum principle has strong conseguences. Together with a range condition it implies that $A$ is a generator (of a positive semigroupl. Moreover, we show that for a densely defined operator $A$ to be the generator of a positive semigroup it is already sufficient that the resolvent $k(\lambda, A)$ of $A$ exists and is positive for all sufficiently large real $\lambda$. For all these results it is essential to assume that $K$ is compact. Concerning the characterization of positive semigroups on $C_{o}(X)$ ( $x$ locally compact, non-compact) we follow a completely different line and will treat this case in the context of general Banach lattices in Chapter C-II.

A special class of positive semigroups are lattice semigroups; i.e., semigroups of lattice homomorphisms. We show in section 2 that (T(t)) tzo is a lattice semigroup if and only if its generator $A$ satisfies an identity $(\mathbb{K})$, the so-called Kato's equality (Theorem 2.5) . We refer to Chapter C-II for a discussion of this identity and classical analogs for the Laplacian due to Kato (1973).

After the abstract characterization in section 2 we show that every continuous semiflow on $x$ together with a cocycle defines a lattice semigroup in a canonical way, and on $C(K)$, every lattice semigroup can be so represented. This furnishes a wide class of examples. Furthermore, positive one-parameter groups on $C_{o}(x)$ (which form a particular type of lattice semigroups) are discussed. Their generators are similar to a derivation perturbated by a multiplication operator (Section 3).

\section*{1. Generators of Positive Semigroups on $C(K)$.}

Let $X$ be a locally compact space. Throughout this section we denote by $C_{o}(X)$ the space of all real-valued continuous functions on $C_{o}(X)$ which vanish in infinity. Recall that a semigroup (T(t)) tep on $C_{o}(X)$ is called positive $i f T(t) \geq 0$ for all $t \geq 0$. It is easy to describe the positivity of (T(t)) $t_{\geq 0}$ in terms of the resolvent $R(\lambda, A)$ of its generator $A$ because of the close relation between these two objects. In fact, the resolvent is expressed by the semigroup by
$$
\text { (1.1) } \quad R(\lambda, A)=\int_{0}^{+} e^{-\lambda t} T(t) d t \quad(\lambda, \dot{d}(A)) ;
$$
and conversely, the semigroup by the resolvent via the formula
$$
(1.2) \quad T(t)=\lim _{n+\infty}(n / t R(n / t, n))^{n} \quad \text { strongly }
$$
(cf. A-II, Prop.1.10). So we obtain the following.

Proposition 1.1 . Let (T(t)) tro be a semigroup with generator $A$. The semigroup is positive if and only if $R(\lambda, A) \geq 0$ for all sufficiently large real $\lambda$.

It is more difficult and more interesting to characterize the positivity of the semigroup by intrinsic conditions on the generator. This is the purpose of this section. As a first orientation we consider bounded genexators. We need the following lemma.

Lema 1.2. Let $X$ be $a$ locally compact space, $x \in X$ and $k$ a regular bounded Borel measure on $x$ such that $\mu(f x\})=0$. Then
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-137.jpg?height=66&width=1620&top_left_y=384&top_left_x=224) $f(x) \neq 0$.

We omit the easy proof.

Theorem 1.3. Let $X$ be locally compact and $A$ be bounded operator on $C_{0}(x)$. The following assertions are equivalent.
(i) $\quad e^{t A} \geq 0 \quad(t \geq 0)$.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-137.jpg?height=78&width=1620&top_left_y=1703&top_left_x=224)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-137.jpg?height=70&width=1614&top_left_y=1761&top_left_x=221)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-137.jpg?height=70&width=1505&top_left_y=1821&top_left_x=224) (iii) implies (i). We have $e^{t A}=e^{-t\| \|^{x} \|} e^{t(A+\|A\|)} \geqq e^{-t\|A\|}$ Id for all $t \geqq 0$.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-138.jpg?height=55&width=1226&top_left_y=1846&top_left_x=204)
we claim that $\lambda_{0}=s$.
In fact, if this is not true, then $\left[\lambda_{O}{ }^{\infty}\right) \subset \rho(A)$ and $R\left(\lambda_{0}, A\right) u \geq 0$ but $R\left(\lambda_{o}, A\right) u$ is not strictly positive. Consequently there exists $x \in K$ such that $\left(R\left(h_{o}, A\right) u\right)(x)=0$. Then $(P)$ implies that $A\left(R\left(\lambda_{O}, A\right) u\right)(x) \geq 0$. Hence, $0 < u(x)=\lambda_{0}\left(R\left(\lambda_{0}, A\right) u\right)(x)-$ $A\left(R\left(\lambda_{0}, A\right) u\right)(x) \subseteq 0$, a contradiction. We have shown that $R(\lambda, A) u \gg 0$ for all $u \gg 0$ and $\lambda>s$. Since $\{u \in C(K): u \geqslant>0\}$ is dense in $C(K)+$, it follows that $R(\lambda, A) \geq 0$ for all $\lambda>s$.

Remark 1.7. The proof of Theorem 1.6 shows that for the generator $A$ of a positive semigroup on $C(K), R(\lambda, A) u \gg 0$ whenever $0 \ll u \in C(K)$ and $[\lambda, \infty) \subset \rho(A)$. In particular, $R(\lambda, A)$ a 0 whenever $[\lambda, \infty)<\rho(A)$.

If $A$ is a generator, then the positivity of the resolvent $R(\lambda, A)$ for large real $\lambda$ implies the positivity of the semigroup (by Prop. 1.1). On $C(K)$ much more is true. Even if $A$ is not supposed to be a generator, the existence and positivity of $k(\lambda, A)$ for large real $\lambda$ implies that $A$ is a generator (of a positive semigroup). This is surprising, because it means that in the case when the resolvent is positive, the norm condition on the resolvent sup $\left\{\left\|(\lambda-w)^{n} R(\lambda, \bar{A}){ }^{n}\right\|\right.$ : $n \in \mathbb{N}, \lambda \geq 0\}<\infty$ which appears in the Hille-Yosida theorem $(A-I I$. Thm. 1.7) is automatically fulfilled.

Theorem 1.8. Let $K$ be compact and $A$ be a densely defined operator on $C(K)$. Suppose that there exists $w \in \mathbb{R}$ such that $[w, m)$ © $p(B)$ and $R(\lambda, A) \geq 0$ for all $\lambda \geq w$. Then $A$ is the generator of a strongly continuous positive semigroup. Moreover,
 
(1.3) #(A) S W.
 

Proof. a) Rssume that $w<0$. Denote by 1 the constant-l-function. Let $u=R(0, A) 1$. We claim that $u>0$. If not, then there exists $x \in K$ such that $u(x)=0$. Let $f \in C(K)$. Then $|f| \equiv\|f\| l$. Consequently, $|R(0, A) f| \leqq R(0, A)|f| \leqq\|f\| R(0, A) 1=\|f\| u$. Hence $(R(0, A) f)(x)=0$ for all $f \in C(K)$. Since $D(A)=R(0, A) C(K)$, it follows that $D(A)$ is not dense, a contradiction. Detine $\|f\|_{0}=$ inf $\{\lambda>0:|f| \subseteq \lambda u\} * f / u \|_{\infty}$. Then il $\|_{0}$ is an equivalent norm on $C(K)$. Moreover, $\|f\|_{0} \leq 1$ if and only if $f \in[-u, u]$. By the resolvent equation we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-139.jpg?height=43&width=1571&top_left_y=1886&top_left_x=228) $\lambda \geqq 0$. This implies that $\lambda R(\lambda, A)$ is contractive for the norm $\left\|\|_{0}\right.$. Thus by the Hille-Yosida Theorem $A$ is the generator of a semigroup which is contractive with respect to the norm $\left\|\|_{0}\right.$, and so is bounded with respect to the supremum norm on $C(K)$.
b) If $w$ is arbitrary, let $\lambda>W$ and consider $A-\lambda$. Then $[w-\lambda, \infty) \subset p(A \sim h)$ and $R(\mu, A-\lambda)=R(\ldots+\lambda, A) \geq 0$ for all $\mu \in\left[W^{-\lambda}, \infty\right)$. Thus by a), $A-\lambda$ is the generator of a bounded positive semigroup. Consequently, $A$ is a generator as well and $\omega(\hat{A}) \leq \lambda$.

In Theorem 1.8 it is enough to assume that $R(\lambda, A) \geqq 0$ for some sequence $\left(\lambda_{n}\right) G \rho(A) r \mathbb{R}$ satisfying $\lim _{n \rightarrow \infty} \lambda_{n}=$ - This follows from the following lemma.

Lemma 1.9. Let $B$ be an operator on $C(R)$ (more generally, on a
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-140.jpg?height=55&width=1497&top_left_y=338&top_left_x=231) $0 \leq R\left(\mu_{2}, B\right)$ and $\mu_{1} \in \mu_{2}$, then $\left[\mu_{1}, \mu_{2}\right] \subset \rho(B)$ and
$$
\left.0 \leqq R\left(\mu_{2}, B\right) \leqq R(\mu, B) \leqq R^{\prime} \mu_{1} ; B\right) \quad \text { for all } \mu \in\left[\mu_{1}, H_{2}\right] .
$$

Proof. Let $M:=\left\{\mu \in \rho(B) \cap\left[\mu_{1}, \mu_{2}\right]=\left[\mu, \mu_{2}\right]=\rho(B)\right.$ and $R(\lambda, B) \geq 0$ for all $\lambda \in\left[\begin{array}{l}\text { a } \\ \text { 没 }\end{array}\right]$ )
a) The set $M$ is open. In fact, let $H \in M$. Then for small $h$ o one has $\mathrm{k}\left(\beta_{3}-\mathrm{h}, \mathrm{B}\right)=\sum_{\mathrm{n}=0}^{\infty} \mathrm{h}^{\mathrm{n}} \mathrm{R}(\mu, B)^{\mathrm{nt1}} \geq 0$.
b) M is closed. In fact, by the resolvent equation one has for
$\mu \in M, R\left(\mu_{1}, B\right)-R(\mu, B)=\left(\mu-\mu_{1}\right) R\left(\mu_{1}, B\right) R(\mu, B) \geqq 0$, hence $R(\mu, B) \leqq R\left(\mu_{1}, B\right)$. Consequently, $\operatorname{dist}(\mu, \sigma(B)) \geqq 1 /\|R(\mu, B)\| \underline{2}$ $1 /\left\|_{\mathrm{R}}\left(\mu_{1}, \mathrm{~B}\right)\right\|$ for all $\mu \in M$. This implies that $M$ is closed. The assertions al and b) imply that $M=\left[\mu_{1}, H_{2}\right]$.

Remark. a) The lemma shows in particular that the resolvent of the generator $A$ of a positive semigroup is decreasing on $(s(A), \infty)$.
b) There exigts a linear operator $B$ on $\mathbb{R}^{n}$ such that $R(\mu, B) \quad(0$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-140.jpg?height=72&width=1617&top_left_y=1420&top_left_x=228) (see Greiner-Voigt-Wolff (1981)).

Remark. Theorem 1.8 does not hold in $C_{o}(X)$, in general. In fact, the operator $A$ on $C_{o}\left(0,1 i\right.$ given by $A f(x)=f^{\prime}(x)+a / x f(x)$ $\left(x \in(0,1 \mathrm{I})\right.$ with domain $\mathrm{D}(\mathrm{A})=\left\{\mathrm{f} \in \mathrm{C}^{1}\left[0,1 \mathrm{I}: \mathrm{E}^{\prime}(0)=\mathrm{f}(0)=0\right\}\right.$ where $\alpha \in(0,1)$ satisfies the following: $\rho(A)=C, R(\lambda, A) \geqslant 0$ for all $\lambda \in \mathbb{R}$. But $A$ is not the generator of a semigroup (even if more general classes than $C_{o}$-semigroups are admitted). See Arendt (1985b) for this example and a general theory of resolvent positive operators. Another example is given by Batty-Davies (1983).

Next we investigate consequences of the positive minimum principle for a densely defined operator which is not a priori assumed to be a generator. For that we will make use of the theory of halfunorms developed in $A-I I, S \in c .2$.

For $0 \ll u \in C(K)$ let
$$
\begin{equation*}
\mathrm{P}_{\mathrm{u}}(f)=\inf \left\{\lambda \in \mathbb{R}_{+}: \mathrm{f} \leq \lambda u\right\}=\sup _{x \in K} f^{+}(x) / u(x) \tag{1.4}
\end{equation*}
$$

Then $P_{u}$ is a strict half-norm on $C(K)$ (see $\left.A-I I, ~ S e c .2\right)$. Note that (1.5) $\quad P_{u}(f) u-f \geq 0 \quad(f \in C(K))$.

For $x \in K$, define $\phi_{x} \in C(K)$ by $  f_{f} \phi_{x}=f(x) / u(x)$.
Let $£ \in C(K)$ such that $-f$ is not strictly positive. Then there exists $x \in K$ such that $f(x) / u(x)=P_{u}(f)$. For such an $x$ we have (1.6) $\quad \phi_{x} \in \operatorname{dp}_{u}(f)$
(see $A-I I, S e c .2$ for the definition of the subdifferential $d_{u}$ ).
Note that for $f \in C(K)$ one has $f \geq 0$ it and only if $p_{u}(-f) \leq 0$ (i.e., the half-norm $P_{u}$ induces the given ordering on $C(K)$ (cf. A-II,Rem.2.8)). As a consequence, overy $P_{u}$-contractive bounded operator $T$ on $C(K)$ is positive.

Proposition 1.10. Let $A$ be a densely defined operator on $C(K)$. Then there exists a strictly positive $u \in D(A)$. For any such $u$ the following assertions are equivalent.
(i) A is $P_{u}$-dissipative.
(ii) $A u \leq 0$ and $A$ satisfies (P).

Proof. Since $\{u \in C(K) ; u \gg 0\}$ is open and non-empty and $D(A)$ is dense, there exists $0 \ll u \in D(A)$.
(i) implies (ii). One has $P_{u}(u)=1$. Let $x \in K$. It follows from (1.6) that $\phi_{X} \in d p_{u}(u)$. Since $D(A)$ is gense, it follows from $A-I I$, Thm. 2.7 that $A$ is strictly $P_{u}$-dissipative. Hence $\left\langle A u, \phi_{x}\right\rangle$ 丢 0 . Thus $(A u)(x) \leqq 0$. We now show (P). Let $0 \leqslant f \in D(A)$ and $x \in K$ such that $f(x)=0$. We have to show that (Af) (x) $\geq 0$. Since $f(x)$ $=0$ and $p_{u}(-f)=0$ we have by $(1.6) \quad \phi_{x} \in d p_{\mu}(-f)$. Since $A$ is strictly $P_{u}-d i s s i p a t i v e ~ w e ~ c o n c l u d e ~ t h a t ~-u(x)^{-1}(A f)(x)=\left\langle\mathcal{A}_{( }(-f), \phi_{X}{ }^{3}\right.$ $\leq 0$. Hençe (Af) (x) $\geqq 0$.
(ii) implies (i). Let $f \in D(A)$. If $\mathrm{P}_{\mathrm{u}}(\mathrm{f})=0$, then $\phi:=0 \in$ $d P_{u}(f)$ and $\langle\boldsymbol{R f}, \phi\rangle \leqq 0$. If $P_{u}(f)>0$, then there exists $x \in K$ such that $\phi_{x} \in d P_{u}(f)$. Hence, $0 \leq P_{u}(f) u-f$ and $\left(P_{u}(f) u-f\right)(x)=0$. It follows from (P) that $P_{u}(f)(A u)(x)-(A f)(x) \geqq 0$. Hence (Af) (x) $s \mathrm{P}_{\mathrm{u}}(\mathrm{f})(\mathrm{Au})(\mathrm{X}) \leqslant 0$ (by (ii)); i.e., $\in A f, \phi_{X} \leq 0$.

Corollary 1.11 . Let $A$ be a densely defined operator on $C(K)$ If A satisfies (P) then $A$ is closable and the closure of $A$ satisfies (P) as well.

Proof. Let $u \in D(A)$ be strictly positive. Then there exists $\lambda \in \mathbb{R}$ such that $A u \leqq \lambda u$. The operator $B=A-\lambda$ satisfies ( $P$ ) as well and Bu $\underset{*}{ }$. Then by Prop. 1.10 , $B$ is $\mathrm{P}_{\mathrm{u}}$-dissipative. Hence B is closable and the closure $\bar{B}$ of $B$ is Pu-dissipative as well by $A-I I$ Prop. 2.9), Then by Prop. 1.10 B satisfies (P). Thus A is closable and its closure $\bar{A}=\bar{B}+\lambda$ satisfies (P) as well.

Corollary 1.12. Let $A \quad C(K) * C(K)$ be linear. If $A$ satigfies (P) then $A$ is bounded and $A+\|A\| I \geqslant 0$.

Proof. It follows from Corollary 1.11 that $A$ is closed. Hence A is bounded. Since A satisfies (P), it follows from Thm. I. 3 that $A$ $+\| \operatorname{lil}$ Id $\geqq 0$.

The next result is a strengthened form of Theorem 2.6. It is somewhat similar to the Lumer-Phillips theorem (A-II, Thm. 2.13). Note that, however, in contrast with the condition of dissipativity, $A+w$ satisfies (P) for any $w \in \mathbb{R}$ whenever ( $P$ ) hofds for $\mathbb{A}$. Thus ( $P$ ) is not a "metric" condition; that is, it does not imply any norm estimate for the semigroup. We also point out that, if (T(t)) $t \geq 0$ is a positive semigroup on $C(K)$, then in general none of the semigroups $\left(e^{-W t} T(t)\right)_{t \geq 0}(w \in \mathbb{R})$ is contractive (see Batty-Davies (1983) or Derndinger (1983)).

Theorem 1.13. Let $A$ be a densely defined operator on $C(K)$ which gatigfies (P). Then
$$
\lambda_{0}:=\inf \{\lambda \in \mathbb{P}: A u \leq \lambda u \text { for some } 0 \ll u \in D(A)\}<\infty
$$
(a) If ( $\lambda-\bar{A}) D(A)$ is dence for some $\lambda>\lambda_{0}$, then $A$ is closable and the clogure $\bar{A}$ of $A$ is the generator of a positive semigroup. (b) If $\lambda$ - $A$ is surjective for some $\lambda>\lambda_{0}$, then $A$ is the generator of a positive semigroup.

Proof. It follows from Prop. 1.10 that $\lambda_{0} \leqslant \infty$.
Assume that $(\lambda-A) D(A)$ is dense, where $\lambda>\lambda_{0}$. Let $\lambda_{0} \leqslant \mu<\lambda$ and $B=A-\mu$. Then $B$ satisfies ( $P$ ) and Bu $\leq 0$ for some atrictly positive $u \in D(B)=D(A)$. Thus $B$ is Pu-dissipative by Prop.1.10. Moreover, $((\lambda-\mu)-B) D(B)$ is dense. Thus by A-II,Cor.2.12 the closure $B$ of $B$ generates a $P_{u}$-contraction semigroup. Hence the
closure $\bar{A}=\bar{B}+\mu$ of $A$ generates a positive semigroup of type $\mu(\bar{A}) \leqq \lambda$.
If $(\lambda-\bar{A})$ is surjective, then $A=\bar{A}$.

The proof of Theorem 1.13 yields estimates for the growth bound of a positive semigroup (see A-III, (1.3)) which we state explicitly in the next corollary.

Corollary l.14. Let $A$ be the generator of a strongly continuous positive semigroup on $C(K)$. Then
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-143.jpg?height=46&width=1306&top_left_y=968&top_left_x=232)
(1.8) $s(A)=\inf \{\lambda \in \mathbb{R}: A u \leq \lambda u$ for some $0<c \in \in D(A)\}$; and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-143.jpg?height=44&width=1443&top_left_y=1200&top_left_x=232)

Proof. Let $s=\inf \{\lambda \in R:[\lambda, \infty) \subset \rho(A)\}$, Clearly, $s \leq s(A)$. Moreover, by Remark 1.7 , $R(\lambda, A) \underline{x} 0$ for all $\lambda>s$, Hence it follows from (1.3) that $u(A) \leqq 5$. Consequently, $s=s(A)=\omega(A)$. Next we prove (1.9). Let $0<f \in D(A)$ such that $A \neq \geq f f$. Assume
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-143.jpg?height=47&width=1611&top_left_y=1547&top_left_x=231) contradiction.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-145.jpg?height=59&width=1602&top_left_y=910&top_left_x=227) $<B f, \phi_{x}>0$.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-146.jpg?height=64&width=1615&top_left_y=1667&top_left_x=209) such that $f(0)=0$. By Lemma l. 2 this implies that $\mu \geq 0$. In order to show the converse assume that $\ddagger \geq 0$.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-149.jpg?height=50&width=1623&top_left_y=2351&top_left_x=222) a and has a right derivative
(2.4) $\quad(0 \circ k)^{\prime}(a)=D_{k^{\prime}}(a)^{\rho(k(a))}$.

Proof. There exists $L \geqq 0$ such that $\|\theta(x)-\theta(y)\| \leq L\|x-y\|$ for all $x, y \in G$. Then
$\lim _{t+0}\left\|1 / t(\theta(k(a+t))-\theta(k(a)))-D_{k}(a) \theta(k(a))\right\| \varepsilon$
1 im-supt ${ }_{t+0} \| 1 / \mathrm{t}\left(\theta(k(a+t))-\theta\left(k(a)+t k^{\prime}(a)\right) \|+\right.$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-150.jpg?height=70&width=1420&top_left_y=502&top_left_x=295)
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

After these preparations we now can show that the lattice property $|T(t) f|=T(t)|f|$ of the semigroup corresponds to the identity (2.9) below for the generator, which we call Kato's equality (cf. Remark 2.7).

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-152.jpg?height=56&width=1512&top_left_y=1203&top_left_x=218)
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-153.jpg?height=55&width=1617&top_left_y=612&top_left_x=228) tion follows from the following lemma.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-154.jpg?height=73&width=1615&top_left_y=1768&top_left_x=209) satisfies Kato's equality; i.e.,
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-155.jpg?height=50&width=1617&top_left_y=2168&top_left_x=228) \{f $\left.\in C^{1}[-1,0]: f(0)=0\right\}$ which is discontinuous for the supremum norm, the space $D(A)=k e r \phi$ is dense in $F$ and consequently dense in $C_{o}[-1,0)$. It follows that (2.18) holds for all $f \in C_{o}^{[-1,0)}$. So by $B-I, S e c .2$, there exist $\beta \geqslant 0$ and $x \in[-1,0)$ such that $f=\beta \delta_{x}$. Assume that $B \neq 0$. It is easy to see that there exists a real function $f \in C^{l}[-1,0]$ satigfying $f^{\prime}(0)=\alpha f(0)+\beta f(x)$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-155.jpg?height=55&width=1386&top_left_y=2577&top_left_x=229) $(\operatorname{sign} f(0)) f^{\prime}(0)=(\operatorname{sign} f(0))(\alpha f(0)+\beta f(x))=$
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

\section*{3. SEMIFLOWS, FLOWS AND POSITIVE GROUPS}

In this section we establish a relation between generators of lattice homomorphisms and derivations. On the space $C_{0}(\mathbb{R})$, for example, this will enable us, to give a detailed description of all generators of positive groups.

At first we consider a compact space $K$ and denote by $C(K)=C(K, \mathbb{R})$ the space of all real valued continuous functions on $K$. The extension of the subsequent results to the complex spaceis obvious.

A lattice homomorphism $T$ on $C(K)$ is an algebra homomorphism if and only if $T$ l $=1$ (see B-I,Sec. 3). We start by describing semigroups of algebra homomorphisms on $C(K)$.

Definition 3.1. A mapping $\quad$ : $\left[0,{ }^{\infty}\right) \times K \rightarrow K$ is called semiflow if for each $t \geqq 0$ the mapping $\phi_{t}$ given by $\phi_{t}(x)=\phi(t, x)$ is continuous and
\begin{tabular}{ll} 
(3.1) $\phi_{s} \phi_{t}=\phi_{s+t}$ & for all $s, t \geq 0$ \\
(3.2) $\phi_{o}(x)=x$ & $(x \in K)$.
\end{tabular}

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-157.jpg?height=53&width=1617&top_left_y=2121&top_left_x=228) A . The following assertions are equivalent.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-158.jpg?height=78&width=1620&top_left_y=2674&top_left_x=212)
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
Theorem 3.7 also holds for non-commutative $c^{*}$-algebras. More precisely: Let $A$ be a $C^{*}$-algebra with unit $l$ and let $A_{h}$ be the real Banach space of all hermitian elements in $A$. Then $A_{h}$ is a real ordered Banach space and $l$ is an interior point of $\left(A_{h}\right)+$. Let $A$ be a densely defined operator on $A_{h}$.
Then $A$ is the generator of an automorphism group if and only if $1 \in D(A)$ and $A l=0 ;( \pm 1-A)(D(A))=A_{h}$ and $A$ is local in the sense that for $0 \leqq x \in D(A), 0 \leqq \phi \in\left(A_{h}\right)^{\prime}, \phi(x)=0$ implies $\phi(\mathrm{AX})=0$.
The proof of Theorem 3.7 can be carried over to this case if one notices the following. A strongly continuous group $T(t) t \in \mathbb{R}$ on $A_{h}$ is an automorphism group if and only if it is positive and $T(t) l=1$ for all $t \in \mathbb{R}$ [see Bratteli-Robinson (1979), Cor. 3.2.21].

Now we let $X$ be a locally compact space and consider positive groups on $C_{o}(X)=C_{o}(X, R)$, the space of all continuous real-valued functions on $x$ which vanish at infinity. Our aim is to describe their generators as perturbations of generators of automorphism groups; i.e., we will extend Theorem 3.6 by allowing $X$ to be noncompact but
restrict ourselves to positive groups (or equivalently semigroups of lattice isomorphisms). And in fact, it is not difficult to show by an exarmple that the corresponding result is wrong for lattice semigroups in general.
$A$ mapping $\phi: \mathbb{R} \times x+x$ ig called a flow on $X$ if the partial maps $\phi_{t}: X * X$ given by $\phi_{t}(x)=\phi(t, x)$ are continuous and satisfy
\begin{tabular}{lll}
$(3.8)$ & $\phi_{o}(x)=x$ & $(x \in x)$ \\
$(3.9)$ & $\phi_{s}^{0 \phi_{t}}=\phi_{s+t}$ & $(s, t \in \mathbb{R})$.
\end{tabular}

It follows from the definition that each $\phi_{t}$ is a homeomorphism on $X$ and $\phi_{-t}=\left(\phi_{t}\right)^{-1}$.
$A$ flow $\phi$ is called continuous if it is continuous with respect to the product topology on $\mathbb{R} \times \mathrm{x}$.
Given a flow $\phi$ a family $\left(h_{t}\right)_{t \in R} \subset c^{b}(X)$ is called a cocycle of $\phi$ if
$(3.10) \quad h_{0}=1$
(3.11) $\quad h_{t+g}=h_{t} \cdot\left(h_{s} 0 \phi_{t}\right) \quad(s, t \in \mathbb{R})$.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-168.jpg?height=84&width=1617&top_left_y=1940&top_left_x=205) then $f(x)=\int_{0}^{\infty} e^{-t} g\left(q_{n}^{-1}\left(q_{n}(x)+t\right)\right) d t=e_{n}^{(x)} \int_{q_{n}}^{\infty}(x) e^{-s_{g}^{n}\left(q_{n}^{-l}(s)\right) d s .}$ Thus $f$ is differentiable in $x$ and $f^{\prime}(x)=(1 / m(x))(f(x)-g(x))$. Consequently $E \in D\left(\delta_{m}\right)$ and $\delta_{m} \ddagger=E-g$. This shows that $A \subset \delta_{m}$. In order to show the converse inclusion, let $f \in D\left(\delta_{m}\right)$ and $g=f-$ $\delta_{m}(f) \in C_{0}(a, b) \quad$ Then $R(1, A) g(x)=f(x)$ if $m(x)=0$ and $R(1, A) g(x)=\int_{0}^{\infty} e^{-t} f(\phi(t, x)) d t-\int_{0}^{\infty} e^{-t} m(\phi(t, x)) f(\phi(t, x)) d t$ $=\int_{0}^{\infty} e^{-t_{f}}(\phi(t, x)) d t-\int_{0}^{\infty} e^{-t} \frac{\partial}{\partial t} f(\phi(t, x)) d t \quad(b y(3,23))$
$=f(x)$ by integrating by parts. Thig shows that $f=R(1, A) g \in D(A)$ and that $\delta_{m}$ is the generator of the group (T(t)) $t \in \mathbb{R}$.
Finally we show that $T(t) D_{0}\left(\delta_{m}\right) \in D_{o}\left(\delta_{m}\right)$, which implies that $D_{o}\left({ }_{m}\right)$ is a core (by $A-I I$, Cor 1.34 ). Let $t \in \mathbb{R}$. The function $\phi_{t}(\cdot)$ is
differentiable on $(a, b)$ and $m(x) \frac{\partial}{p x} \phi(t, x)=m(\phi(t, x))$ for all $x \in$ $(a, b)$. Let $f \in D_{o}\left(\delta_{m}\right)=D\left(\delta_{m}\right) C^{-}, t \in \Re$. Then $T(t) f=f o \phi_{t}$ is differentiable and so in $D_{o}\left(\delta_{m}\right)$.

Conversely, assume that $\delta_{m}$ is generator of a group (T(t)) $t \in \mathbb{R}$ on $C_{0}(a, b)$. Since $\delta_{m}$ is a derivation, there exists a continuous flow $\left(\phi_{t}\right)_{t \in i}$ on (a,b) such that $T(t) f=f o \phi_{t}$ for all $f \in C_{o}(a, b)$, $t \in \mathbb{R}$. In order to show that $m$ is admissible let $a \leq c<d \leq b$ such that $m(x) \pm 0$ for all $x \in(c, d)$ and $m(c)=0$ or $a=c=-\infty$ and $m(d)=0$ or $d=b=\infty$.
If $a<c$ then $m(c)=0$; consequently $\left(\delta_{m} f\right)(c)=0$ for all
$f \in D\left(\delta_{m}\right)$. Thus (T(t)f)(c) $\pm f(c)$ for $a l l f \in D\left(\delta_{m}\right)$ and $t \in \mathbb{R}$. This shows that $\phi(t, c)=c$ for all $t \in \mathbb{R}$. Consequently $\phi_{t}(a, c)-(a, c)$ for $a l l$ $t \in R$. Similary $\phi_{t}(d, b) \subset(d, b)$ for all $t \in \mathbb{R}$. Thus the space $E_{o}:=\left\{f \in C_{o}(a, b): f\right.$ vanishes off (c,d) $\}$ is invariant under the group $\{T(t))_{t \in i f}$. We denote the group restricted to $E_{o}$ by $\left(T_{0}(t)\right)_{t \in R}$ and by $A_{o}$ its generator. Then $D\left(A_{o}\right)=$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-169.jpg?height=66&width=1617&top_left_y=1252&top_left_x=228) obtain $\vec{R}_{O}=\delta_{m}$, where $m$ ' denotes the restriction of $m$ to (c,d) . So it follows from Prop. 3.18 that $m^{r}$ is admissible.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-170.jpg?height=67&width=1614&top_left_y=1257&top_left_x=215) injective mapping from $\mathbb{R}$ into $\left(a_{n}, b_{n}\right)$. Thus $\alpha_{n}$ is strictly monotonous. It is easy to see that $l^{\prime \prime m} t_{+\infty} \phi\left(t, x_{n}\right)$ is an element of $K$ whenever the limit exists in (a,b) ; similary for the limit as $t \rightarrow-\infty$. Consequently, $a_{n}(f)=\left(a_{n}, b_{n}\right) ; i, e ., a_{n}$ is a homeomorphism from $\mathbb{R}$ onto $\left(a_{n}, b_{n}\right)$. Define $r_{n}$ to be the inverse of $a_{n}$. Let $x \in\left(a_{n}, b_{n}\right)$. Then $\phi(t, x)=\phi\left(t, a_{n}\left(r_{n}(x)\right)\right)$
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
Next we show $\left(\mathrm{r}_{\mathrm{n}}^{-1}\right)^{\prime}(\mathrm{t}) \neq 0$ for all $\mathrm{t} \in \mathbb{F}$. In fact, let $x_{o} \in\left(a_{n}, b_{n}\right)$ and ascume that $\left(r_{n}^{-1}\right){ }^{\prime}\left(r_{n}\left(x_{0}\right)\right)=0$. Then for all $f \in D_{o}(\delta)$ one has
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-173.jpg?height=73&width=1620&top_left_y=609&top_left_x=212) $=V T(t) V^{-1} f$, where $V$ is the isomorphism on $C_{0}(a, b)$ given by $V f=f a \beta$. Consequently, $\delta=V^{-l} \delta_{m} V$.

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

\title{
CHAPTER B-III \\ SPECTRALTHEORYOR OR \\ POSITIVE SEMIGROUPS ON CO(X) \\ by \\ Günther Greiner
}

It is known that for a single operator $T \in L\left(C_{0}(x)\right)$ the positivity of $T$ has influence on the spectrum of $T$, mainly on the peripheral spectrum, i.e. the part of the spectrum containing all spectral values of maximal absolute value. This part of the spectrum is of interest because it determines the esymptotic behavior of the iterates $T^{n}$ for large $n \in \mathbb{N}$, The spectral properties indicated above were first proved by Perron (1907) and Frobenius (1909) for positive square matrices, i.e. for positive operators on the Banach lattice $c^{n}$. Later these results were extended to the infinite dimensional setting; important contributions are due to Jentzsch, Karlin, Krein, Krasnou selski'i, Lotz, Rota, Rutman, Schaefer and others (see Chapt. $V$ of Schaefer (1974)).

In this chapter we investigate the spectrum o(A) of the generator A of a positive semigroup $T \neq(T(t))_{t \geq 0}$ on the Banach space $C_{o}(X)$. Throughout this chapter we assume that $C_{0}(X)$ is the space of all complex-valued functions on the locally compact space $x$. In case we restrict to compact spaces we write $K$ instead of $X$.
1. THE SPECTRAL BOUND

One of the basic results on the spectrum of a positive operator is the fact that its spectral radius is an element of the spectrum (see V.Prop.4.1 of Schaefer (1974)). We begin the investigation of the spectrum of positive semigroups with the analogous result. To that purpose we recall that the spectral bound $s(A)$ of a generator $A$ is defined as the least upper bound of the real parts of all spectral values (cf. A-III, (1.2)).

Theorem 1.1. If $A$ is the generator of a positive semigroup on $F=C_{0}(X)$, then $s(A) \in a(A)$ unless $s(A)=-{ }^{-\infty}$ In case $X$ is compact we always have $s(A)>-\infty$.

Proof. We suppose o(A) $\neq \varnothing$ (i.e., $s(A)>-\infty)$ and assume $s(A)$ ( $\sigma(A)$. Then there exist $E>0$ and $a_{0}, \beta_{O} \in \mathbb{R}$ such that
(1.1) $[s(A)-\varepsilon, \infty) \in \rho(A), \mu_{0}:=\alpha_{0}+i \beta_{o} \in \sigma(A)$ and $\alpha_{o}>s(A)-\varepsilon$.

Now we choose $\lambda_{o} \in \mathbb{R}$ large enough such that
$(1.2)\left|\lambda_{0}-H_{0}\right|<\lambda_{0}-(S(A)-\varepsilon)$,
and, in addition, such that $\lambda_{O}>\omega(A)$. Then the resolvent $R\left(\lambda_{0}, A\right)$ is a positive bounded operator, hence its spectral radius $\left.r\left(R_{( }, A\right)\right)$ is a spectral value. From A-III, Prop. 2.5 it follows that
$(1,3) \lambda_{0}-r\left(R\left(\lambda_{0}, A\right)\right)^{-1} \epsilon \sigma(A)$ and $r\left(R\left(\lambda_{0}, A\right)\right) \geqslant\left|\lambda_{0}-\mu_{0}\right|^{-1}$.
This and (1.2) implies that $\lambda_{o}-I\left(R\left(\lambda_{o}, A\right)\right)^{-1}$ is a real spectral value which is greater than $s(A)-\varepsilon$. We have derived a contradic tion to (1.1) and thus have proved the first statement of the theorem. To establish the second statement we recall that $\lim _{\lambda \rightarrow \mathrm{m}} \lambda R(\lambda, A) f=f$ for every $f \in \mathrm{~F}$, In particular, for $\mathrm{f}=\mathrm{l}_{\mathrm{X}}$ we find a (large) $\lambda_{0} \in \mathbb{R}$ such that
(1.4) $\lambda_{O} R\left(\lambda_{O}, A\right) 1_{X} \geqq 1 / 2 \cdot 1_{X}$ hence $R\left(\lambda_{O}, A\right) 1_{X} \geqq\left(2 \lambda_{O}\right)^{-1} \cdot 1_{X}$.

We may assume $\lambda_{o}>W(A)$ then $R\left(\lambda_{0}, A\right) \geqq 0$, and iterating (1.4) we obtain
(1.5) $R\left(\lambda_{\sigma}, A\right)^{n} 1_{X} \geqq\left(2 \lambda_{O}\right)^{-n} \cdot l_{X}>0$ for every $n \in \mathbb{N}$.

It follows that $\left\|R\left(n_{0}, A\right)^{n}\right\|\left(2 \lambda_{0}\right)^{-n}$ and therefore
(1.6) $r\left(R\left(\lambda_{O^{\prime}} A\right)\right)=1 i_{n \rightarrow \infty}\left\|R\left(\lambda_{O_{0}} A\right)^{n}\right\|^{1 / n} \geq\left(2 \lambda_{O_{0}}\right)^{-1}>0$.

Thus $\left.o\left(R_{( }, A\right)\right)$ contains non-zero spectral values which in view of A-III, Prop. 2.5 is equivalent to $\sigma(A) \neq \varnothing$.

The following examples show that the spectrum may be empty in case $x$ is not compact or if the semigroup is not positive.

Examples $1.2 .(a)$ Consider $x=[0,1)$ and (T(t)) on $C_{0}(x)$ given by
(1.7) $\quad(T(t) f)(x):=\left\{\begin{array}{cc}f(x+t) & \text { if } x+t<1 \\ 0 & \text { if } x+t \geqq 1 .\end{array}\right.$

Then (T(t)) $t \geqslant 0$ is nilpotent (we have $T(t)=0$ for $t z l$ ). It follows that $\sigma(T(t))=\{0\}$ for $a l l t>0$ and $b y A-I I I, T h m .6 .2$ we have $\sigma(\mathrm{A})=\varnothing$.
(b) The operator $A$ on $E:=C_{0}[0, \infty)$ given by
(1.8) (Af) $(x)=f^{\prime}(x)-x f(x), D(A)=\left\{f \in E: E \in C^{1}, A f \in E\right\}$
has empty spectrum. It is the generator of a positive non-nilpotent semigroup which is given by
$(T(t) f)(x)=\exp \left(-\left(t^{2} / 2\right)-x t\right) \cdot f(x+t)$.
(c) Taking into account that $C_{0}([0,1))$ as well as $C_{0}([0, \infty))$ both are topologically (but not isometrically) isomorphic to c( $[0,1]$ ) (see Semadeni (1971), Sec.21.5), one obtains from (a) and (b) (non-positive) semigroups on $C([0,1 \eta)$ whose generators have empty spectrum.

The proof of Thm. 1.1 given above is based on the fact that the specw tral radius of a bounded positive operator is an element of the spec* trum. A direct proof not using this fact is given in C-III, Cor.l. A.

Corollary 1.3. Suppose $\lambda_{0} \in \rho(A)$. Then $R\left(\lambda_{0}, A\right)$ is a positive operator if and only if $\lambda_{0}>s(A)$.
For $\lambda>s(A)$ we have $r(R(\lambda, A))=(\lambda-s(A))^{-1}$.

Proof. The second statement is an immediate consequence of Thm. 1.1 and A-III, Prop.2.5.
Given $\lambda_{0}>s(A)$ we choose $\lambda_{1}>\max \left\{\lambda_{0}, A^{\prime \prime}(A)\right\}$. Since
$\left|\lambda_{1}-\lambda_{0}\right| \varepsilon\left|\lambda_{1}-s(A)\right|=r\left(R\left(\lambda_{1}, A\right)\right)^{-1}$ we have
$(1.10) R\left(\lambda_{O^{\prime}} A\right)=\sum_{n=0}^{\infty}\left(\lambda_{1}-\lambda_{O}\right)^{n} \cdot R\left(\lambda_{1}, A\right)^{n+1}$.
Since $R\left(\lambda_{1}, A\right)$ is positive, it follows that $R\left(h_{o}, A\right)$ is positive as well.
On the other hand, assuming that $R\left(\lambda_{o}, A\right)$ is a positive operator, then $\lambda_{o}$ has to be a real number (note that for $g \geqq 0$ we have $f:=R\left(\lambda_{O}, A\right) g z 0$ hence $\left.\lambda_{O} f-A f=g=\bar{g}=\overline{\left(\lambda_{O}-A\right) f}=\lambda_{O} f-A f\right)$. As we have shown above $R(\lambda, A)$ is positive for $\lambda, \max \left(\lambda_{0}, S(A)\right\}$ hence an application of the resolvent equation yields:
$$
\begin{equation*}
R\left(\lambda_{0}, A\right)=R(\lambda, A)+\left(\lambda-\lambda_{0}\right) R(\lambda, A) R\left(\lambda_{0}, A\right) \geq R(\lambda, A) \geq 0 \tag{1.11}
\end{equation*}
$$

It follows that for all $\lambda>\max \left\{\lambda_{o} s(A)\right\}$ we have
$(1.12)(\lambda-s(A))^{-1}=r(R(\lambda, A)) \leq\|R(\lambda, A)\| \leqq\left\|R\left(\lambda_{0}, A\right)\right\|$,
which can be true only if $\lambda_{0}$ is greater than $s(A)$.

Corollary 1.4. Suppose $X$ is compact and $A$ has compact resolvent. Then there exists a real eigenvalue $\lambda_{o}$ admitting a positive eigen* function such that $\operatorname{Re} \lambda \leq \lambda_{o}$ for every $\lambda \in o(A)$.

Proof. By Thm.l.l. $\lambda_{0}:=s(A)$ is a real number, contained in the spectrum and obviously Re $\lambda \leq \lambda$ for every $\lambda \in \sigma(A)$. Since $A$ has compact resolvent it follows that $\lambda_{o}$ is a pole of the resolvent. Let $k$ be its order, then the highest coefficient in the Laurent series is given by
$(1.13) \quad Q:=\lim _{\lambda \rightarrow s(A)}(\lambda \sim s(A))^{k_{R}(\lambda, A)}$.
It follows from Cor. 1.3 that $Q$ is a positive operator. Since $Q \neq 0$ there exists $g \geqq 0$ such that $h:=Q g>0$. Moreover, by $A-I I I, 3.6$. we have $\left(\lambda_{0}-A\right) h=\left(\lambda_{0}-A\right) Q g=0$.

The example of the rotation semigroup (A-III, Ex.5.6) shows that the assumptions in Cor.1.4. do not imply that $s(A)$ is dominant. Additional hypotheses ensuring this stronger property will be given below (see Cor.2.11, 2.12).

The following result is elementary. However, positivity is the crucial point in its proof. Note that it is not just a consequence of the spectral mapping theorem for the point spectrum.

Proposition 1.5. Suppose $A$ is the generator of the positive semigroup $(T(t))_{t z 0}$. Take $T>0, r>0$ and let $a:=t^{\sim}{ }^{\sim} \log (r)$.
(a) If $r$ is an eigenvalue of $T(\tau)$ with positive eigenfunction
$h_{0}$, then there is a positive $h \in D(A)$ such that $A h=a h$ and $\left\{x \in X: h_{0}(x)>0\right\} \subset\{x \in X: h(x)>0\}$.
(b) If $r$ is an eigenvalue of $T(t)^{\text {' }}$ with positive eigenvector
$\phi_{O}$, then there is a positive $\phi \in D\left(A^{*}\right)$ such that $A * \phi=a \phi$ and supp $\phi_{0}=$ supp $\phi$.

Proof. Without loss of generality we may assume $r=1$, hence $a=0$ and $T(\tau) h_{o}=h_{0}$.
(a) Defining
$(1.14) \quad h:=\int_{0}^{T} T(s) h_{0} d s$
then for $0 \leqslant t \leqslant T$ we have
$$
\begin{aligned}
T(t) h & =\int_{0}^{t} T(s+t) h_{0} d s=\int_{t}^{t} T(s) h_{0} d s+\int_{\tau}^{\tau+t} T(s u t) T(\tau) h_{0} d s= \\
& =\int_{t}^{t} T(s) h_{0} d s+\int_{0}^{t} T(s) T(t) h_{0} d s=h .
\end{aligned}
$$

It follows that $A h=1 i m t^{-1}(T(t) h-h)=0$. So far, positivity was not used. The point is that in general, $h$ may be zero. But if (T(t)) is positive and $h_{o} \geq 0$, then $s \rightarrow\left(T(s) h_{0}\right)(x)$ is a continuous positive function, hence $0<h_{0}\left(x_{0}\right)=\left(T(0) h_{0}\right)\left(x_{0}\right)$ implies $h\left(x_{0}\right)=$ $\int_{0}^{T}\left(T(s) h_{0}\right)\left(x_{0}\right) d s>0$.
(b) Defining $\phi==\int_{0}^{T} T(s)^{\prime} \phi_{o} d s$, one can proceed as in (a) to obtain the desired result.

We use Prop.l. 5 to prove an analogue of the famous Kreinmitman result. For the sake of completeness we include the proof of this classical result, which states that the spectral radius of a positive operator $\quad \mathbf{T}$ on $C(K)$ (or more generally on an order unit space) is an eigenvalue of the adjoint $T$ ' (see the corollary of Thm, 2.6 in the appendix of Schaefer (1966)).

Theorem 1.6. Suppose $K$ is compact and (T(t)) tzo is a positive semigroup with generator $A$. Then there exists a positive probability measure $\phi \in D\left(A^{+}\right)$such that $A^{\prime} \phi=\omega(A) \phi$.

Proof. Consider $T:=T(1), r:=r(T)=e^{\mu(A)}$ - In view of Prop. 1.5 it is enough to show that $r$ is an eigenvalue of $T^{\prime}$ with a positive eigenvector. Given $\lambda \in \mathbb{C},|\lambda|>r$ and $f \in C(K)$ we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-181.jpg?height=75&width=1492&top_left_y=2167&top_left_x=225)
It follows that $\|\mathrm{R}(\lambda, T)\| \leq\|R(\lambda \mid, T)\|$ and therefore
$$
\begin{equation*}
\lim _{\lambda+r}\|\mathrm{R}(\lambda, T)\|=\infty \tag{1,15}
\end{equation*}
$$

By the uniform boundedness principle there exist a sequence ( $\lambda_{n}$ ), $\lambda_{n}+r$ and a positive $\Psi \in M(K)$ such that $\| R\left(\lambda_{n}+T\right) \psi \psi+\infty$. Defining $\Psi_{n}:=\left\|R\left(\lambda_{n}, T\right)^{*}\right\|^{-1} R\left(\lambda_{n}, T\right)^{\prime} \quad$ we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-182.jpg?height=79&width=1522&top_left_y=246&top_left_x=227)
$$
=\left(r-\lambda_{n}\right) \Psi_{n}+\left\|R\left(\lambda_{n}, T\right)^{+\Psi}\right\| 1_{\Psi}+0 .
$$

Since $r-T^{r}$ is $\sigma(M(K), C(K))$-continuous, (1.16) implies that every $\sigma(M(K), C(K))$ cluster point of $\left(\Psi_{n}\right)$ is a positive eigenvector, provided that it is non~zero. Because $K$ is compact we have
$\{\phi \in M(K): \phi \geq 0,\|\phi\|=1\}=\{\phi \in M(K): \phi \geqq 0,\langle\phi, l\rangle=1\}$ which shows that the set of probability measures is $\sigma(M(K), C(K))$-compact. Therefore the sequence ( ${ }_{\mathrm{n}}$ ) has non-zero cluster points.

This theorem implies that for positive semigroups on $C(k)$ the growth and spectral bounds coincide (cf. A-III,4.4). Actually, this is true for locally compact spaces as well and can be proved directly (see B-IV,Thm.1.4). Jsing this result one can prove Thm. 1.6 by applying the classical Krein-Rutman theorem to any resolvent operator $R(h, A)$ for $\lambda \in \mathbb{R}$ sufficiently large.

The theorem ensures that $A$ ' always has eigenvalues. The generator itself may have no eigenvalue at all. Multiplication operators have no eigenvalues unless the multiplier is constant on an open subset. Thm.l.6 fails to be true for locally compact spaces as the following example shows:

Examples 1.7. Consider $E=C_{o}\left(\mathbb{R}^{n}\right)$ and the semigroup $(T(t))_{t \geqq 0}$ generated by the Laplacian (cf. A-I,2.8). From the explicit representation of $T(t)$,
(1.17) $(T(t) f)(x)=(4 \pi t)^{-n / 2} \int_{R^{n}} \exp \left(-(x-y)^{2} / 4 t\right) \cdot f(y) d y$,
it follows that $\lim _{t \rightarrow \infty} T(t) f \approx 0$ for every $f \in C_{0}\left(\mathbb{R}^{n}\right)$ (Note that $\|T(t) f\| \leqslant(4 \pi t)^{-n / 2} \int_{R^{n}}|f(y)| d y+0$ provided that $f$ has compact support and that $\|T(t)\|=1$ for all $t \geq 0)$.
If $\phi$ is an eigenvector of $A^{\prime}$ corresponding to $s(A)=\omega(A)=0$, we have $T(t) ' \phi=\phi$ for all $t \geqslant 0$, hence
$\langle\phi, f\rangle=\lim _{t+\infty}\langle T(t) f, \phi\rangle \approx 0$ for every $f, i . e ., \phi=0$.

\section*{2. THE BOUNDARY SPECTRUM}

In this section we restrict our attention to the boundary spectrum $o_{b}(A)$ of a generator $A$, which, by definition, is the intersection of $o(A)$ with the line $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda=s(A)\}$. Thus ${ }_{b}{ }_{b}(A)$ contains all spectral values of $A$ which have maximal real part. Note that in general the boundary spectrum is a proper subset of the topological boundary of $o(A)$. Our aim is to prove results ensuring that $\sigma_{b}(A)$ is a cyclic set (see Def.2.5).
While most of the results of the preceding section were obtained by transforming the problem to a resolvent operator $\mathbb{R}(\lambda, A)$ ( $\mathcal{A} \in \mathbb{R}$ large enough), this procedure fails here. The reason is that there is no onewto-one correspondence between the boundary spectrum of $A$ und the peripheral spectrum of $\mathrm{f}(\lambda, A)$. Actually, from Thm. 1.1 and $A-I I I$, Prop.2.5 it follows that the peripheral spectrum of $R(\lambda, A)(i . e .$, the set of spectral values having maximal absolute value) is trivial, since it only contains the spectral radius $r(R(A, A))=(A-s(A))^{-1}$. We begin our discussion with two lemans.

Lemita 2.1. Suppose $K$, $L$ are compact and $T: C(K)+C(L)$ is a linear operator satisfying $T 1_{\mathrm{K}}=1_{\mathrm{L}}$. Then we have $T \geq 0$ if and only if $\|T\| \leq 1$.

Proof. If $T$ is positive, then
(2.1) $|T f| \leq T|f| \leq T\left(\|f\| \cdot l_{K}\right)=\|f\| \cdot T\left(l_{K}\right), f \in C(K)$,
hence $\|T\|=\left\|T l_{K}\right\|$, whenever $T$ is positive. This shows that $T \geq 0$ implies $\|T\| \leq 1$ whenever $T 1_{\mathbb{K}}=l_{L}$.
To prove the reverse direction, we first observe that for complex numbers and hence for complex-valued functions the following equivaw lence holds:
$$
\begin{align*}
& -1 \leqq \mathrm{~m} \leq \mathrm{l} \text { if and only if } \\
& \|f-i * r \cdot 1\| \leqq \rho_{r}:=\left(1+r^{2}\right) 1 / 2 \text { For every } r \in \mathbb{K} . \tag{2.2}
\end{align*}
$$

Now suppose $f \in C(K), 0 \leqq f \leq 2 \cdot l_{K}$. Then we have $-l_{K} \leq f-1_{K} \leq l_{K}$ hence by (2.2) $\left\|f-l_{K}-i \cdot r \cdot l_{K}\right\| \leq \rho_{r}$ for every $r \in \mathbb{R}$. From $T_{K}=l_{L}$ and $\|T\|_{i} \leqslant l$ it follows that
$\| T f-l_{L}-i \cdot r \cdot I_{L} \mid \leq \rho_{r}$ for every $r \in \mathbb{R}$. Using (2.2) once again, we obtain ${ }^{-1} L_{L} \leq T f-1_{L} \leq 1_{L}$ or $0 \leq T E \leq 2 \cdot 1_{L}$.

Before we can formulate the second lemma we have to fix some notation:

Definition 2.2.(a) Given $h \in C_{0}(x)$ such that $h(x) \neq 0$ for all $x \in x$ then the operator $S_{h}$ is defined to be the multiplication operator with sign h,i,e.,
(2.3) $\quad s_{h} f=h|h|^{-1} f \quad\left(f \in C_{0}(X)\right)$.
(b) For $f \in C_{o}(X), n \in \mathbb{Z}$ we define $f^{[n]} \in C_{o}(X)$ by
$$
f^{[n]}(x)=\left\{\begin{array}{cc}
(f(x) /|f(x)|)^{n-1} \cdot f(x) & \text { if } f(x) \neq 0  \tag{2.4}\\
0 & \text { if } f(x)=0
\end{array}\right.
$$

The following assertions are immediate consequences of the definition. They will be used Erequently in the following.
(2.5) $S_{h}$ is a linear isometry satisfying $\left|S_{h} f\right|=|f|$, its inverse being $s_{\bar{h}}$ where $\bar{h}$ is the complex conjugate of $h$.
(2.6) $f^{[1]}=f, f^{[0]}=|f|, f^{[-1]}=\dot{\bar{f}}$, $\left|\mathbf{f}^{[n]}\right|=|\mathbf{f}|$ for every $\quad n \in Z$.
(2.7) If $h(x) \neq 0$ for all $x \in x$, then $h^{[n]}=s_{h}^{n}|h|=s_{h}^{n-1} h$.

Lemma 2.3. Let $T$ and $R$ be bounded linear operators on $C_{o}(X)$ and assume that $h \in C_{o}(X)$ has no zeros. Suppose we have
(2.8) $R h=h, T|h|=|h|$ and $|R f| \leqq T|f|$ for every $£ \in C_{D}(X)$.

Then $R$ and $T$ are similar, more precisely, $T=S_{h}^{-1} S_{h}$.
In particular, the spectre (and point spectra resp.) of $T$ and $R$ coincide.

Proof. We first note that the assertion $|R f| \leqq T|f|$ (f $\in \mathbb{E}$ ) implies that $T$ is a positive operator. Therefore $T|=|h|$ implies that the principal ideal $E_{h}=\left\{ \pm \in C_{o}(x):|f| \subseteq n|h|\right.$ for some $\left.n \in \mathbb{N}\right\}$ is an invariant subspace for $T$ and for $R$ as well. $E_{h}$ is isomorphic to $C^{b}(X)=C(B X)(B X$ denotes the Stone-Cech compactification of $X)$, an isomorphism is given by $f \rightarrow f|h|$. Considering the restrictions ${ }^{T} \mid E_{h}$ and ${ }^{R} \mid E_{h}$ as operators on $C(\beta X)$ and denoting them $\hat{T}$ and $\tilde{R}$ respectively, we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-184.jpg?height=62&width=1335&top_left_y=2619&top_left_x=229)

Here $\tilde{\mathrm{h}}$ denotes the continuous extension of $\mathrm{h} /|\mathrm{h}|$ to BX . Defining $T_{1}:=M_{\tilde{h}}{ }^{1} \tilde{R}_{\tilde{h}}$ we have by (2.9)
(2.10) $\quad T_{1} 1=M_{\hat{h}}^{-1} \tilde{R} \tilde{h}=1$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-185.jpg?height=72&width=1474&top_left_y=495&top_left_x=208)
Hence we have $\left\|\mathrm{T}_{1}\right\| \leqq\|\tilde{\mathrm{T}}\|=1$ (by (2.11), (2.9), (2.1)). Then it follows from Lema 2.1 that $T_{1}$ is a positive operator. Thus (2.11) implies that $0 \leqq T_{1} \leq \tilde{T}$ and therefore $\left\|\tilde{T}-T_{1}\right\|=\left\|\left(\tilde{T}-T_{1}\right) l\right\|=0$ (by (2.10), (2.9), (2.1)).

We are now able to prove a result which in some sense is the key to cyclicity results for the spectrum. These general results will be proved by reducing the problem in such a way that the following theorem can be applied.

Theorem 2.4.(a) Let $T$ be a positive linear operator on $C_{0}(x)$, let $h \in C_{0}(X)$ and $\lambda \in \mathbb{C},|\lambda|=1$. If $T h=h_{h}$ and $T|h|=|h|$, then we have $T^{[n]}=\lambda^{n_{h}}{ }^{[n]}$ for every $n \in T$ (c£. (2.4)).
If $h$ does not have zeros in $x$, then $\lambda T=S_{h}^{-1} T S_{h}$.
(b) Suppose $A$ is the generator of a positive semigroup, $h \in C_{0}(X)$, $\alpha, \beta \in \mathbb{H}$ such that $A h=(\alpha+i \beta) h$ and $A|h|=\alpha|h|$. Then we have $A h^{[n]}=(\alpha+i n \beta) h^{[n]}$ for every $n \in \mathbb{Z}$.
If $h$ does not have zeros then $S_{h} D(A) \approx D(A)$ and $i B+A=S_{h}^{-1} A S_{h}$.

Proof. (a) The closed principal ideal $\overline{E_{h}}$ which is canonically isomorphic to $C_{0}\left(X_{1}\right)$ with $X_{1} \neq\{x \in X: h(x) \neq 0\}$, is T-invariant. We give an object a tilde when we consider it as an element of $\overline{E_{h}} \cong C_{o}\left(X_{1}\right)$. Defining $\tilde{\mathbb{R}}:=\tilde{\mathrm{K}} \tilde{\mathrm{T}}$, then $\tilde{\mathbf{T}}, \tilde{\mathrm{R}}, \tilde{\mathrm{h}}$ satisfy (2.8), hence we have
(2.12) $\quad \tilde{T}=S_{\tilde{h}}^{-1} \circ \tilde{R} \circ S_{\tilde{h}}=\bar{h} \cdot S_{\tilde{h}}^{-1}+\tilde{T} \circ S_{\tilde{h}}$
which by iteration yields
(2.13) $\hat{T}=\bar{\lambda}^{n} \cdot S_{\hat{h}}^{-n} \circ \tilde{T} \circ S_{\bar{h}}^{n}$ for all $n \in \mathbb{Z}$.

It follows that
$\tilde{T}_{\tilde{h}}{ }^{[n]}=\tilde{T} t s_{\tilde{h}}^{n}|\tilde{h}|=\lambda^{n} \cdot s_{\tilde{h}}^{n} t \tilde{T}|\tilde{h}|=\lambda^{n} \cdot s_{\tilde{h}}^{n} \tilde{h}=\lambda^{n} \cdot \tilde{h}^{[n]}$
(see (2.7) and (2.12)), which is precisely $T h^{[n]}=\lambda^{n_{h}}{ }^{[n]}$ for all $n \in \mathbb{Z}$. If $h$ does not have zeros, then $\overline{E_{h}}=E$, hence $T=\tilde{T}$, $h=\tilde{h}$ and the remaining assertion follows from (2.12).
(b) This can be deduced easily from (a) as follows: If $A h=(\alpha+i \beta) h, A|h|=\alpha|h|$, then we have by $A-I I I, \operatorname{Cor} .6 .4$; $e^{-\alpha t_{T}}(t) h=e^{i \beta t_{h}}$ and $e^{-\alpha t} T(t)|h|=|h|$ for every $t \geq 0$. Hence by (a) $e^{-\alpha t^{\prime}}(t) h^{[n]}=e^{i n \beta t_{h}[n]}$ (t $\geqq=0, n \in \mathbb{Z}$ ), which is equivalent to $A h^{[n]}=(\alpha+i n \beta) h^{[n]}$. If $h$ does not have zeros, then $e^{-\alpha t_{T}(t)}=e^{-\alpha t_{e}}{ }^{i \beta t} S_{h} \mathcal{1}_{T}(t) S_{h}$ for every $t \geq 0$ which is equivalent to the final statement of (b).

Before we state a first cyclicity result we give the definition and illustrate it by some examples.

Definition 2.5. $A$ subset $M \subset \subset$ is called imaginary additively cyclic (or simply cyclic), if it satisfies the following condition: $\alpha+i \beta \in M, \alpha, \beta \in \mathbb{R}$ implies that $\alpha+i k \beta \in M$ for every $k \in \mathbb{Z}$.

Every subset of $\mathbb{R}$ is cyclic. On the other hand, if $M$ is cyclic and $M \not \subset \mathbb{R}$, then $M$ has to be unbounded.
For a subset $M$ of $i$ we give the following equivalent conditions:
(i) $\quad M$ is imaginary additively cyclic;
(ii) M is the union of (additive) subgroups of if ;
(iii) $M=U_{a \in S}$ iaZ for some set $S \subset \mathbb{R}$.

Here are some concrete cyclic subsets of $i=R$ :
$M_{1}=\{0\}, M_{2}=\mathbf{i} \mathbb{R}, M_{3}=i \alpha \mathbb{Z}(\alpha>0)$,
$M_{4}=i \alpha \mathbb{Z}+i \beta \mathbb{Z}=\{i n \alpha+i m \beta: n, m \in \mathbb{Z}\} \quad(\alpha, \beta \in \mathbb{R})$,
$M_{5}=\{0\} U\{i \lambda: \lambda \in \operatorname{in},|\lambda| \geqslant 1\}$,
$M_{6}=U_{n=0}^{\infty}\{i \lambda ; \lambda \in \mathbb{R}, n \alpha \leq|\lambda| \leqq n \beta\} \quad(0<\alpha \leq \beta, \alpha, \beta \in \mathbb{R})$.

In the following we consider the boundary spectrum of several semigroups. The letter $M_{i}$ refers to the sets just defined.

Examples 2.6.(a) For the Laplacian $A$ on $i^{n}$ or the second derivam tive on $[0,1]$ with Neumann boundary conditions the boundary spectrum is $M_{1}$.
(b) The first derivative on $\mathbb{R}$ or $\mathbb{R}_{+}$is an example where the boundary spectrum of the generator is $M_{2}$.
(c) The rotation semigroup on $C(\Gamma)$ (see $A-I I I, E x .5 .6)$ with period $2 \pi / \alpha$ has boundary spectrum $\mathrm{M}_{3}$.
(d) For the semigroup on $C(\Gamma \times r)$ given by
$(T(t) f)(z, w)=f\left(z=e^{i a t}, w \cdot e^{i \beta t}\right) \quad(f \in C(\Gamma \times \Gamma),(z, w) \in \Gamma \times \Gamma)$
we have $P \sigma(A)=M_{4}$. If $\alpha / B$ is irrational, then this is a dense subset of $i \mathbb{R}$ and $\sigma_{b}(A)=\sigma(A)=i \mathbb{R}$.
(e) Consider $D:=\{z \in \mathbb{C}:|z| \zeta 1\}=\left\{r \cdot e^{i \mu}: I \in[0,1]\right.$, 山 $\left.\in \mathbb{R}\right\}$, and a strictly positive function $k \in C[0,1]$ - The flow on $D$ governed by the differential equation $\dot{r}=0$, $\dot{\omega}=k(r)$ induces a strongly continuous semigroup on $C(D)$ (which is given by $(T(t) f)(z)=f\left(z \cdot e^{i k(|z|) t}\right)$, The boundary spectrum is $M_{5}$ with $\alpha \quad ;=\inf k(r), \beta \quad=\sup k(r)$. In particular, for $k(r)=1+r$ we obtain as boundary spectrum the set $M_{5}$.
(f) Suppose $M$ is a closed cyclic subset of $i \mathbb{R}, M=U_{\alpha \in S} i \alpha \mathbb{Z}$ for a suitable $s^{\prime}=\mathbb{R}(e . g . \quad S=M)$.
The space $E_{1}:=\left\{\left(f_{a}\right)_{a \in S}: f_{\alpha} \in C(\Gamma)\right.$, sup $\left.\left\|f_{\alpha}\right\|<\infty\right\}$ is a Banach space under the norm $\left\|\left(f_{\alpha}\right)\right\|:=$ sup $\left\|f_{\alpha}\right\|$. The closure of the linear subspace $E_{o}:=\left\{\left(f_{\alpha}\right) \in E_{1}: f_{\alpha} \neq 0\right.$ only for finitely many $\left.\alpha \in S\right\}$ is isomorphic to $C_{0}(X)$ where $x$ is the topological sum of $|S|$ copies of $\Gamma$.
Let $\left(T_{\alpha}(t)\right)_{t z 0}$ denote the rotation semigroup on $C(\Gamma)$ with period $2 \pi / a$, then we define a semigroup $(T(t))_{t \geqslant 0}$ on $E:=C_{0}(X)$ as follows:
(T(t) ( $\left.\left.f_{\alpha}\right) \quad:=\left(T_{\alpha}(t) f_{\alpha}\right) \quad\left(f_{\alpha}\right)_{\alpha \in S} \in E\right)$.
This is a positive semigroup on $E=C_{0}(X)$ whose boundary spectrum is precisely the given closed cyclic set $M$. We leave the verification as an excercise.

Our first result concerns cyclicity of the eigenvalues contained in the boundary spectrum, i.e., of the set
$P_{\sigma_{b}}(A):=P_{\sigma}(A) \cap \sigma_{b}(A)=\{\lambda \in \operatorname{P\sigma }(A): \operatorname{Re} \lambda=s(A)\}$.
It is almost a straightforward consequence of Thm. 2.4.

Proposition 2.7. Assume that for some $t_{o}>0$ there is a strictly positive measure $\phi \quad s u c h$ that $T\left(t_{0}\right)^{x} \phi=\exp \left(s(A) t_{0}\right) \cdot \phi$.
Then $P_{b}(A)$ is imaginary additively cyclic.

Proof. If ${ }^{P \sigma_{b}}(A)$ is empty there is nothing to prove. Otherwise we have $s(A)>-\infty$. In view of the rescaling procedure we may assume $s(A)=0$. By Prop.l.5(b) there exists $\Psi \gg 0$ such that $T(t){ }^{\prime} \Psi=\Psi$ for all $t \geq 0$. Given $i a \in P_{G}(A)$ then there is $h \in C_{o}(X), h \neq 0$ such that $A h=i_{a h}$ or $T(t) h=e^{i \alpha t} h$ for all $t(A-I I I, C o r .6 .4)$.

Then we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-188.jpg?height=67&width=1508&top_left_y=355&top_left_x=231)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-188.jpg?height=58&width=1280&top_left_y=436&top_left_x=228)
```
Since % is strictly positive, (2.14) and (2.15) imply that
T(t) |h| = |h| for t }\geqq0\mathrm{ or equivalently A |h| = 0.
Now Thm.2.4 implies that Ah[n] = inah[n] (n\in\mathbb{Z}).
```

Concerning the hypothesis $T\left(t_{0}\right)^{\prime} \phi=\exp \left(s(A) t_{0}\right) \cdot \phi \gg 0$ we recall that in case $X$ is compact there are always positive linear forms such that $T(t)^{\prime} \phi=e^{s(A)} t_{\phi}$ (see Thm.l.6). If the semigroup is irreducible, then one also has q >> 0 (see sec. 3 below).

In a second result we consider semigroups having compact resolvent, An important step of the proof is isolated as a lemma. Before stating it we recall that given a closed ideal I $\quad C_{o}(\mathrm{X})$ then $I$ as well as $C_{0}(X) / I$ are spaces of continuous functions on a locally compact space vanishing at infinity. More precisely, if $I=\left\{f \in C_{o}(X): f_{M}=0\right\}$ for a suitable closed subset $M \in X$, then $I=C_{o}(X, M)$ and $C_{o}(X) / I$ $\cong C_{0}(M)(C f, B-I)$. It follows that given another closed ideal $J=\left\{f \in C_{O}(X): f_{N}=0\right\}$ such that $I \subset J$ i.e., N $\subset M$, then $J / I$ can be identified with $C_{0}(M \backslash N)$. We do not use this concrete reprew sentation of $J / I$, However, this shows that we stay within our setting of Banach spaces of continuous functions on locally compact spaces.

Lemma 2.8. Suppose $A$ is the generator of a positive semigroup $T$ such that the spectral bound $s(A)$ is a pole of the resolvent of order $k$. Then there is a sequence
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-188.jpg?height=78&width=1017&top_left_y=2068&top_left_x=231)
of T-invariant closed ideals with the followirg properties:
Denoting by $A_{n}(n=0,1, \ldots, k)$ the generator of the semigroup on $I_{n} / I_{n-1}$ which is induced by $(T(t))$ we have :
(a) $s\left(A_{0}\right)<s(A) ;$
(b) If $n: 1$ then $s\left(A_{n}\right)=s(A)$ is a first order pole of the resolvent $R\left(., A_{n}\right)$. The corresponding residue is a strictly positive operator.

Proof. We can assume that $s(A)=0$ and we will denote the negative coefficients of the Laurent series of $R(., A)$ at 0 by $Q_{n}$. Thus the following relations hold (see $A-I I I, 3,6$ ),
$$
Q_{n}=\frac{1}{2 \pi i} \cdot f_{\gamma} z^{n-1} R(z, A) \quad d z \quad(n \in \mathbb{N})
$$
$$
\begin{align*}
& Q_{n} \neq 0 \text { if } n \leq k \text { and } Q_{n}=0 \text { for } n>k ;  \tag{2.17}\\
& Q_{n}=A^{n-1} Q_{1} \quad(n \in \mathbb{N}) ; Q_{k}=\lim _{z^{\prime}+0} z^{k} \cdot R(z, A) ;
\end{align*}
$$

We define $I_{n}$ as follows ( $n=0,1, \ldots, k-1$ ) :
$$
I_{n}:\left\{\text { \{f } \in E: Q_{n+1}|f|=Q_{n+2}|f|=\ldots=Q_{k}|f|=0\right\} .
$$

At first we restrict our attention to $I_{k-l}$.
Since $R(\lambda, A)$ is positive if $\lambda>0$ (Cor.1.3), it follows from (2.17) that $Q_{k}$ is a positive bounded operator, hence
$I_{k-1}=\left\{f \in E: Q_{k}|f|=0\right\}$ is a closed ideal. since $Q_{k}$ commutes with $R(\lambda, A)$ (see (2.17)i, it follows that $I_{k-1}$ is a Twinvariant ideal. By $A$-III, Cor. 4.3 the generators $A_{A_{k-1}}$ and $A_{k}$ induced by $A$ on $I_{k-1}$ and $E / I_{k-1}$ respectively have a pole at 0 . The coefficients of the Laurent series are the operators induced by $Q_{n}$ on $E / I_{k-1}$ and $I_{k-1}$ respectively.
Suppose that the pole order of $R\left(., A_{k}\right)$ is greater than 1 , say $m$. Then $o_{m /}=\lim _{z \rightarrow 0} z^{m} R\left(z, A_{k}\right.$ is a positive non-zero operator, hence we find for every $x \in E_{+}$an element $y \in I_{k-1}$ such that $Q_{m} x+y \geqq 0$. Then we have
$0 \leqq Q_{k}\left|Q_{m} x+y\right|=Q_{k} Q_{m} x+Q_{k} y=Q_{k+m-1} x+Q_{k} Y=0+Q_{k} Y \leq Q_{k}|y|=0$ hence $Q_{m} x=\left(Q_{m} x+y\right)-y \in I_{k-1}\left(x \in E_{+}\right)$- It follows that $Q_{\mathrm{H}} /=0$ which is a contratiction.
So far we know that the resolvent of $A_{k}$ has a pole of order $\leq 1$. Moreover, since $Q_{k} \mid I_{k-1}=0$, the resolvent of ${ }^{A} \mid I_{k w 1}$ has a pole of order $\leq k-1$. From A~III, Cor. 4.3 it follows that the pole order of $A_{k}$ and ${ }^{A_{k}} I_{k \sim 1}$ is precisely $\quad$ and $k-1$, respectively. The residue $Q_{1 / I_{k-1}}=\lim _{z+0} z R\left(z, A_{k}\right)$ is positive since $R\left(z, A_{k}\right) \geqslant 0$ for $z>0$ (Cor.l.3). To prove that it is strictly positive we assume $\mathrm{Q}_{1 / I_{k-1}}\left(\left|\mathrm{x}+\mathrm{I}_{\mathrm{k}-1}\right|\right)=0$ which means $\mathrm{Q}_{1}|\mathrm{x}| \in \mathrm{I}_{\mathrm{k}-1}$ hence $Q_{\mathrm{k}}|\mathrm{x}|=$ $A^{k-1} Q_{1}|x|=0$, that is, $x \in I_{k-1}$ or $x+I_{k-1}=0$. Applying what we have proved so far to $I_{k-1}$ and $\left.{ }^{A}\right|_{I_{k-1}}$ we obtain $I_{k-2}$, $A_{k-1}$, and so on, After $k$ steps ( $n=1$ ) we conclude that $I_{0}$ is Tuinvariant and that the order of the pole of $R\left(.,{ }^{A} \mid I_{o}\right)$ is 0 ,
which means that $0 \in \rho\left({ }^{A} \mid I_{o}\right)$, Since ${ }^{A} \mid I_{o}$ generates a positive semigroup and $R\left(\lambda,{ }^{A} \mid I_{0}\right)=R(\lambda, A) \mid I_{0}$ is positive for $\lambda>0$ it follows from Cor. 1.3 . that $s\left(A_{0}\right)=s\left({ }^{A} \mid I_{0}\right)<0$.

One can check the different steps of the proof by studying the following example. Consider the following matrix as generator on $\mathbb{c}^{4}$.
$$
\left(\begin{array}{cccc}
-1 & a & b & c \\
0 & 0 & d & e \\
0 & 0 & 0 & f \\
0 & 0 & 0 & 0
\end{array}\right\} \quad \text { where } \quad a, b, c, d, e, f \quad \begin{aligned}
& 0
\end{aligned}
$$

The result is summarized in the following diagram ( $\mathrm{e}_{\mathrm{j}}:=\left(\delta_{j k}\right)$ ) $=$
\begin{tabular}{|c|c|c|c|c|c|}
\hline & order & $\mathrm{I}_{0}$ & $\mathrm{I}_{1}$ & $I_{2}$ & $\mathrm{I}_{3}$ \\
\hline $\mathrm{d}>0, \mathrm{f}>0$ & 3 & $\left\langle\mathrm{e}_{1}\right\rangle$ & ${\ll e_{1}} \mathrm{E}_{2}{ }^{2}$ & $\left.\mathrm{se}_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ & $0^{4}$ \\
\hline $d=0, f>0$, & 2 & $\left\langle e_{1}\right\rangle$ & $\left\langle e_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ & $c^{4}$ & \\
\hline $d=0, \quad f=0, \quad e>0$ & 2 & $\left\langle e_{1}\right\rangle$ & $\left\langle\mathrm{e}_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ & $c^{4}$ & \\
\hline $d>0, f=0, \quad e>0$ & 2 & $\left\langle e_{1}\right\rangle$ & $\left\langle e_{1}, e_{2}\right\rangle$ & $c^{4}$ & \\
\hline $\mathrm{d}>0, \mathrm{f}=0, \mathrm{e}=0$ & 2 & $\left\langle e_{1}\right\rangle$ & $<_{1}, e_{2}, e_{4}>$ & $0^{4}$ & \\
\hline
\end{tabular}

This example also shows that the operators $Q_{k-1}, \ldots, Q_{1}$ are not necessarily positive (e.g. $a>0, b=c=0, d=e=f=2$ ) , A more general (and more interesting) example is the following:
Suppose that $A_{i}(i=1, \ldots, n)$ are generators of positive semigroups on $C_{o}(x)$ such that $s\left(A_{i}\right)=0$ is a first order pole of the resolvent. And let $A_{i j}(l \leqslant i<j \leq n)$ be positive bounded operators on $\mathrm{C}_{\mathrm{o}}(\mathrm{X})$.
Then $A \quad:=\left(\begin{array}{llll}A_{1} & A_{12} & \cdots & { }^{A}{ }_{1} n \\ 0 & A_{2} & \cdots & A_{2 n} \\ \vdots & \vdots & \cdots & \vdots \\ 0 & 0 & \cdots & A_{n}\end{array}\right)$
is the generator of a positive semigroup on
$C_{o}\left(\mathrm{X}, \mathrm{C}^{\mathrm{M}}\right)=\mathrm{C}_{\mathrm{o}}(\mathrm{X}) \times \mathrm{C}_{\mathrm{o}}(\mathrm{X}) \times \ldots \times \mathrm{C}_{\mathrm{O}}(\mathrm{X})$, and $\mathrm{s}(\mathrm{A})=0$ is a pole of the resolvent of order $k$ where $l \leqslant k \leqslant n$.

Theorem 2.9. Suppose $A$ is the generator of a positive semigroup on $C_{o}(X)$ such that every point of $\sigma_{b}(A)$ is a pole of the resolvent. Then $P \sigma_{b}(A)=\sigma_{b}(A)$ is cyclic.

Proof. If $\sigma(A)=\phi$ there is nothing to prove, thus we can assume that $s(A)=0$. In view of the lemma and $A m I I, P r o p .4 .3(i)$ we can assume that $s(A)$ is a first order pole with strictly positive resi* due, which we call $Q$. We have $A O=Q A=s(A) A=0$ (see $A-I I I$, 3.6), hence
(2.18) $\mathrm{QT}(\mathrm{t})=\mathrm{T}(\mathrm{t}) \mathrm{Q}=\mathrm{Q}$ for all $\mathrm{t} \geqslant 0$.

If $A h=i \alpha h$ for some $\alpha \in \mathbb{R}, h \neq 0$, then $T(t) h=e^{i \alpha t} h$ (by AuIII, Cor.6.4). Hence $|h|=\left|e^{i \alpha t_{h}}\right|=|T(t) h| \leq T(t)|h|$, or equivalently, $T(t)|h|-|h| \geqq 0 . B Y(2.18)$ we have $Q(T(t)|h|-|h|)=0$.
Since Q is strictly positive, it follows that $T(t)|h|=|h|$ or $A|h|=0$. Now we can apply Thm. 2.4 and obtain $A h^{[n]}=i n a h^{[n]}$ for every $n \in \mathbb{Z}$. This shows that $\mathrm{Po}_{\mathrm{b}}(\mathrm{A})=\sigma(\mathrm{A}) \cap \mathrm{i} R$ is cyclic.

If A has compact resolvent then every point of o(A) is a pole of the resolvent (see $A-I I I, 3,6$ ) hence we have:

Corollary 2.10. If $A$ has compact resolvent, then $P \sigma_{b}(A)=\sigma_{b}(A)$ is cyclic.

If it is known that the boundary spectrum of a generator is cyclic and nonvoid, the following alternative holds:
(2.19) Either $\sigma_{b}(A)=\{s(A)\}$ or else $\sigma_{b}(A)$ is an infinite unbounded set.

If one can exclude the second alternative, then there is a unique spectral value having maximal real part. A real spectral value $\lambda_{o}$ of a generator $A$ is called a dominant provided that $R e \lambda \leqslant \lambda_{0}$ for every $\lambda \in o(A)$, it is called strictly dominant if for some $\delta>0$ one has Re $\lambda \leq \lambda_{0}-\delta$ for every $\lambda \in \sigma(A), \lambda \neq \lambda_{0}$.
The assumptions of Cor. 2.10 do not imply that $s(A)$ is dominant, the rotation semigroup (AwII,Ex.5.6) is a counterexample.

Corollary 2.11. Assume that for some $t_{0}>0$ (hence for all $t>0$ ) one has $r_{\text {ess }}\left(T\left(t_{0}\right)\right) \leqslant r\left(T\left(t_{0}\right)\right), ~ e . g . r$ that $T\left(t_{o}\right)$ is compact and $r\left(T\left(t_{0}\right)\right)>0 \quad($ see $A-I I I, 3.7)$.
Then $s(A)$ is a strictly dominant eigenvalue.

Proof. If $s(A)$ is not strictly dominant, then we have by Thm. 2.9 and $A-I I I, C o r .6 .5$ that $\{\lambda \in \sigma(A): \operatorname{Re} \lambda>s(A)-r\}$ contains infiniu tely many eigenvalues for every $I>0$, From $A-I I I, C o r .6 .4$ it follows that $\{\lambda \in \sigma(T(t)):|\lambda|>r\}$ contains infinitely many eigenvalues (counted according to their multiplicities) for every $r$ exp(s (A)t) $=r(T(t))$. This contradicts the assumption $I_{\text {ess }}(T(t))<I(T(t))$ (see $\left.A-I I I, 3.7\right)$.

Corollary 2.12. Suppose $A$ has compact resolvent and non-empty spectrum. If the corresponding semigroup is eventually norm continuous (e.g., if it is holomorphic or differentiable), then there is a strictly dominant eigenvalue admitting a positive eigenfunction.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-192.jpg?height=64&width=1614&top_left_y=1076&top_left_x=227) $\operatorname{Re} \lambda \geq s(A)-r\} \quad i s$ compact for every $r>0$ (see $A-I I$, Thm, 1.20) and this set does not have accumulation points because $A$ has compact resolvent. In other words, it is a finite set. The assertion now follows from Thm. 2.9 and Cor.1.4.

We now consider some examples. The first one shows that there are positive semigroups with $P \sigma_{b}(A)$ being not cyclic. It is unknown if there are semigroups where $o_{b}(A)$ is not cyclic.

Example 2.13. Consider $E=C(\Gamma) \times C_{o}(\mathbb{R})\left(\approx C_{o}(\Gamma U \mathbb{U})\right\}$, We fix a positive function $k \in C_{0}(\mathbb{R})$ with compact support. The operator $A$ given by
$$
\begin{align*}
A(f, g) & :=\left(f^{+}, g^{\prime}+\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) d \theta \cdot k\right)  \tag{2,20}\\
D(A) & :=\left[(f, g) \in E: f, g \in C^{l}, g^{\prime} \in C_{O}(\mathbb{R})\right\}
\end{align*}
$$
generates a semigroup (T(t)) tzo which is given by
$$
\begin{align*}
& T(t)(f, g)=\left(f_{t}, g_{t}\right) \text { with } f_{t}(\theta):=f(\theta+t), \\
& g_{t}(x):=g(x+t)+\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) d \theta \cdot \int_{x}^{x+t} k(u) d u \tag{2,21}
\end{align*}
$$

Then ( $T(t))_{t \geq 0}$ is a positive semigroup and $\|T(t)\| \leqslant\left(1+\|k\|_{1}\right)$. In particular, $s(A) \leqq w(A) \leqq 0$. It is easy to see that 0 is not an eigenvalue of $A$, while all $i k, k \in \mathbb{Z}, k \neq 0$ are eigenvalues, the corresponding eigenfunctions being $\left(e_{k}, 0\right)$ with $e_{k}(\theta)=e^{i k \theta}$.

Example 2.14.(a) (One-dimensional Schrsdinger operator).
Let $X=\mathbb{R}, E=C_{0}(X)$ and $V: \mathbb{R} \rightarrow \mathbb{F}$ be a continuous function such that inf $v(x)>-\infty$.

If we define
$$
\begin{align*}
(A f)(x) & :=f^{〔}(x)-V(x) f(x) \\
D(A) & :=\left\{f \in C_{0}(X): f \in C^{2}, A f \in C_{O}^{(X)\}}\right. \tag{2.2}
\end{align*}
$$
then $A$ is the generator of a positive semigroup.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-193.jpg?height=64&width=1611&top_left_y=773&top_left_x=208) there exists a dominant real eigenvalue with corresponding positive eigenfunction. Actually, the eigenfunction is strictly positive. (In fact, if $f \in C^{2}, E \geqslant 0$ and $f\left(x_{0}\right)=0$ for some $x_{0}$, then $f^{\prime}\left(x_{0}\right)=0$. Therefore the uniqueness theorem for ordinary differential equations implies that $f$ is identically zerol.
(b) (A retarded linear differential equation).

Consider $E=C[-1,0]$ and define $A_{m}, A_{O}$ as follows:
(2.23) $A_{m} f:=f^{\prime}, E \in D\left(A_{m}\right)=C^{l}[-1,0]$
(2.24) $A_{o} f:=f, f \in D\left(A_{0}\right)=\left[f \in C^{1}[-1,0]: f^{\prime}(0)=0\right\}$.
$A_{o}$ generates a contraction semigroup $\left(T_{o}(t)\right)$ tso which is given by
(2.25)
$$
\left(T_{o}(t) f\right)(x)=\left\{\begin{array}{ccc}
f(x+t) & \text { if } x+t \leq 0 . \\
f(0) & \text { if } x+t \leq 0 .
\end{array}\right.
$$

This semigroup is positive, eventually norm continuous $\left(\mathrm{T}_{\mathrm{o}}(\mathrm{t})=\mathrm{o}_{0}\right.$ gl for $t \geq 1$ ) and has compact resolvent. Given a linear functional $\psi$ on $C[-1,0]$, we consider
(2.26) $A_{\Psi}:=A_{m} \mid D\left(A_{\Psi}\right) \quad w i t h \quad D\left(A_{\Psi}\right):=\left\{f \in C^{1}[-1,0]: f^{1}(0)=\langle f, \Psi\rangle\right\}$. Denoting the exponential function $x \rightarrow e^{\lambda x}$ by $e_{\lambda}$, we have for real $\lambda$ and $\lambda>\|\Psi\|$ :
(2.27) Id - $1 / \lambda \cdot \Psi \theta e_{\lambda}$ is a bijection of $D\left(A_{\Psi}\right)$ onto $D\left(A_{0}\right)$ and $\lambda-A_{\Psi}=\left(\lambda-A_{o}\right)\left(I d-1 / \lambda \cdot \Psi 8 e_{\lambda}\right)$.

Using the Neumann series expension of (Id - $\left.1 / \lambda \cdot \Psi \mathrm{q}_{\lambda}\right)^{-1}$ one obtains the following estimate:
$(2.28) \quad \|\left.\left(I d-1 / \lambda+\Psi b e_{\lambda}\right)^{-1}\right|_{i} \leq \lambda /(\lambda-\|Y\|) \quad$ if $\lambda>\|\Psi\|$.

It follows from (2.25) and (2.26) that for $\lambda>\|\psi\| R\left(\lambda, A_{\Psi}\right)$ exists and satisfies $\left\|R\left(\lambda, A_{\psi}\right)\right\| \leq \lambda /(\lambda \omega\|\Psi\|)+1 / \lambda=1 /(\lambda \omega\|\Psi\|)$. Then the Hille-Yosida Theorem (AmII,Thm.1.7) implies thet $A_{4}$ generates a semigroup (T(t)) satisfying $\quad\|T(t)\| \leqq \exp (\|\Psi\| t)$. Moreover, this semigroup is eventually norm continuous (see B-IV, Cor.3.3). By B-II,Ex.l. 22 we have the following equivalence:
(2.29) $A_{\psi}$ generates a positive semigroup if and only if $\Psi+r \delta_{o} \geq 0$ for some $I \in \mathbb{R}$.

Thus Cor.2.12 is applicable if $4+r_{0} \geqq 0$ for some $r \in \mathbb{R}$. Since every eigenvalue of $A_{\Psi}$ is an eigenvalue of $A_{m}$ and since ker ( $\lambda \sim A_{m}$ ) $=\left\{\alpha e_{\lambda}: \alpha \in \mathbb{C}\right\}$, the spectral bound $s\left(A_{\psi}\right)$ is determined by the (unique) real $\lambda \in \mathbb{R}$ such that $e_{\lambda} \in D\left(A_{\Psi}\right)$ or equivalently, $\lambda$ is a solution of the somalled characteristic equation
(2.30) $\lambda=\Psi\left(e_{\lambda}\right), \lambda \in \mathbb{R}$.
(The assumption $\Psi+I_{\sigma} \geqslant 0$ implies that the function $\lambda \rightarrow \Psi\left(e_{\lambda}\right)$ is
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-194.jpg?height=74&width=1617&top_left_y=1365&top_left_x=228) unless $\Psi=r_{o} \delta_{o}$ for some $r_{o} \in \mathbb{H}$.)

We conclude this section with some additional remarks related to Thm. 2.9 and its corollaries.

Remarks 2.15.(a) If $s(A)$ is a pole of the resolvent, then for generators of positive semigroups one has the following equivalences:
(i) $\quad s(A)$ is a first order pole.
(ii) For every $0<f \in \operatorname{ker}(s(A)-A)$ there exists $0 \leqslant \Psi \in \operatorname{ker}\left(s(A)-A^{*}\right)$ such that $\langle f, \Psi\rangle>0$.
(iii) For every $0<\Psi \in \operatorname{ker}\left(s(A)-A{ }^{\prime}\right)$ there exists
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-194.jpg?height=46&width=1034&top_left_y=2287&top_left_x=391)

In particular, if ker(s(A) *A) contains a strictly positive func* tion or if ker(s (A) * A') contains a strictly positive measure, then $s(A)$ is a first order pole.

We sketch the proof of (i) $\Leftrightarrow$ (ii) assuming that $s(A)=0$. If 0 is a first order pole, then the residue $P$ is a positive projection satisfying $P E=$ ker $A, P^{\prime E}=$ ker $A^{+}$(see A-III, 3.6) . Thus given
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-195.jpg?height=46&width=1617&top_left_y=448&top_left_x=205) $\left.\Psi:=P^{\prime} \phi:\langle f, \Psi\rangle=\left\langle f, P^{\prime} \phi\right\rangle=\langle P f, \phi\rangle=\langle f, \phi\rangle\right\rangle 0$. To prove the reverse direction we first observe that the highest coefficient $Q_{k}$ of the Laurent expansion is a positive operator. Thus if 0 is a pole of order $k \geqq 2$ we choose $0<h \in E$ such that $f:=Q_{k} h>0$. Then $A f=A Q_{k} h=0$ and for every $\Psi \in$ ker $A^{1}$ we have $\langle f, \Psi\rangle=\left\langle Q_{K} h, \Psi\right\rangle=\left\langle h, Q_{k}{ }^{*} \Psi\right\rangle=\left\langle h, Q_{k-1}{ }^{1} A^{\prime \Psi}\right\rangle=0$.
(b) If a linear operator $s$ on $C_{D}(X)$ is weakly compact, then $s^{2}$ is compact (see B-IV, Prop.2.4(b)). Therefore every non-zero spectral value of a weakly compact operator is a pole of the resolvent. This shows that Thm. 2.9 is applicable if either $T\left(t_{0}\right.$ ) is weakly compact for some $t_{o}$ or $R(\lambda, A)$ is weakly compact for some $\lambda \in \rho(A)$, We quote two criteria for weak compactness:
(2.31) $I f \quad T \in L(C(K)), K$ compact, is positive, then it is weakly compact if and only if its biadjoint $T$ " maps the bounded Borel functions into $C(K)$ (see B-IV,Prop. 2.4).
(2.32) A positive operator $T$ on $C_{0}(X)$ which is dominated by a finite rank operator, is weakly compact. (Actually, its adjoint $T^{\prime}$ is dominated by a finite rank opew rator as well, hence it maps the unit ball in an order interval. It follows that $T^{\prime}$ is weakly compact hence so is $\mathbf{T}$.)
(c) Stronger results than Thm. 2.9 will be proved in Chapter C-III. Actually, assuming only that $s(A)$ is a pole of finite algebraic multiplicity one can show that $\sigma_{b}(A)$ contains only poles of finite multiplicity (C-III.Thm.3.13). In C-III, Cor.2.12 we will show that $\sigma_{b}(A) i s$ cyclic whenever $s(A)$ is a pole of the resolvent.
(d) Example 2.14 (b) can be extended to systems of functional diffem rential equations even the infinite dimensional case. For details we refer to Sec. 3 of Chapter B-IV.

\section*{3. IRREDUCIBLE SEMIGROUPS}

In the case of matrices it is well known that considerably stronger results are available if one considers positive matrices which are irreducible. The concept of irreducibility can be extended to our setting and in many cases one can check easily whether a given semigroup has this property (see Ex. 3.4). We will show that irreducible semigroups have many interesting properties. For example, the spectrum $\sigma(A)$ is always non-empty, positive eigenfunctions are strictly positive and if s(A) is a pole, it is algebraically (and geometrically) simple (see Prop. 3.5). Moreover, in certain cases irreducibility ensures that $\sigma_{b}(A)$ and $\mathrm{Po}_{\mathrm{b}}(\mathrm{A})$ are not only cyclic subsets but 'subgroups" (see Thm.3.5 and Thm.3.11 for details).
We start the discussion with severbl, mutually equivalent, definitions of irreducibility.

Definition 3.1. A positive semigroup $T=(T(t))$ on $E=C_{o}(x)$, $X$ locally compact, with generator $A$ is called irreducible if one of the following mutually equivalent conditions is satisfied:
(i) There is no T-invariant closed ideal except $\{0\}$ and $E$.
(ii) Given $0<f \in E, 0<\phi \in E^{\prime}$, then $\left\langle T\left(t_{0}\right) f, \phi\right\rangle>0$ for some $t_{0} \geqq 0$.
(iii) For every $f \in E_{+}$we have $U_{t \geq 0}\{x \in X:(T(t) f)(x)>0\}=X$.
(iv) For some (every) $\lambda>s(A)$ there exists no closed ideal which is invariant under $R(\lambda, A)$ except $\{0\}$ and $E$.
(v) For some (every) $\lambda>s(A)$ we have: $R(\lambda, A) f$ is strictly positive whenever $f>0$.
(vi) $U_{t} \geq 0^{s u p p} T(t)^{\prime} \delta_{X}$ is dense in $X$ for every $x \in X$.

That these six conditions are actually equivalent can be seen as follows:
(i) $\rightarrow$ (ii): Suppose there are $0<f \in E, 0<\phi \in E^{\prime}$ (such that $\langle T(t) f, \phi\rangle=0$ for every $t z 0$. Then the ideal I generated by
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-196.jpg?height=53&width=1617&top_left_y=2278&top_left_x=228) Obviously $I$ is T-invariant.
(ii) + (iii): Given $0<f \in E, x \in X$. By (ii) there exists $t_{o}$ such that $\left(T\left(t_{D}\right) f\right)(x)=\left\langle T\left(t_{D}\right) f, \delta_{x}\right\rangle>0$.
(iii) + (vi) : Suppose that $U_{t \geqslant 0} \operatorname{supp} T(t)^{\prime} s_{y}$ is not dense for some $y \in X$. Then there exists $f_{0} \in E, f_{o}>0$ such that
$\operatorname{supp} f_{0} \cap \operatorname{supp} T(t)^{\prime} f y=\emptyset$ for every $t \geq 0$. Hence ( $\left.T(t) f_{0}\right)(y)=$ $<f_{0}, T(t)^{\prime} \delta_{y} \gg 0$, that is, $y \not U_{t \geq 0}\left(x \in X:\left(T(t) f_{0}\right)(x)>0\right\}$. (vi) $+(v):$ Given $0<f \in E, \lambda>u(A), y \in X$, there exists
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-197.jpg?height=64&width=1452&top_left_y=462&top_left_x=208) $\left(T\left(t_{o}\right)(f)(y)=\left\langle f, T\left(t_{o}\right) ' \delta\right\rangle>0\right.$ and therefore $(R(h, A) f)(y)=\int_{0}^{\infty} e^{-h t}(T(t) f)(y) d t>0$. Since $\lambda \rightarrow R(\lambda, A) f(i s$ decreasing in the interval ( $s(A), *$ ) (use the resolvent equation and the fact that $R(\lambda, A)$ is positive) we have $R(\lambda, A) f \gg 0$ for all $\lambda>S(A)$.
(V) $\rightarrow$ (vi): If $I$ is a $R(\lambda, A)$-invariant ideal and $0<f \in I$, then $g:=R(\lambda, A) f \in I$. By (v) $g$ is strictly positive thus $I$ has to be dense (it contains all functions of compact support).
(iv) $+(i): A t$ first we recall that a closed linear subspace which is invariant for $R\left(\lambda_{O}, A\right) \quad\left(\lambda_{O} \in \rho(A)\right)$, is invariant for $R(\lambda, A)$ whenever $\lambda$ and $\lambda_{\rho}$ belong to the same component of $\rho(A)$. Hence by $A-I, 3,2$ every $R\left(\lambda_{O}, A\right)$-invariant subspace where $\lambda_{O} \in P_{+}(A)$ is T-invariant and vice versa.

Remark 3.2. Obviously, irreducibility of a semigroup (T(t)) $t \geqq 0$ is implied by the following condition:
(vii) $T(t) f \gg 0$ whenever $f>0$ and $t>0$.

The rotation semigroup (see A-I,2.5) is irreducible but it does not satisfy condition (vii). However, assuming that the semigroup (T) (t) is holomorphic, then (vii) of Def. 3.1 is equivalent to irreducibility. We will give a proof of this result in the more general situation of Banach lattices (see C-III,Thm. 3.2 (b)) .

A semigroup $(T(t))_{t \geqslant 0}$ is irreducible if and only if $\left(e^{-a t} T(t)\right) t \geqslant 0$, $\alpha \in \mathbb{R}$ is. More generally, irreducibility is invariant under perturbations by multiplication operators. In fact, we have the following result:

Proposition 3.3. Suppose A generates a positive semigroup $T$ on $C_{0}(x)$ and let $h$ be a continuous, bounded realmalued function on $x$. Then the semigroup $S$ generated by $B:=A+M_{h}$ is irreducible if and only if $T$ has this property.

Proof. Since every closed ideal $\frac{1}{2} s$ of the form $\left\{f \in E: f_{\mid M}=0\right\}$ where $M \in X$ is closed subset (cf. Sec.l of $B-I$ ) it is clear that all closed ideals are invariant under the multiplication operator $\mathrm{M}_{\mathrm{h}}$ and $M_{-h}$ respectively. Thus the assertion follows from the expansions which are true for $\lambda$ sufficiently large.
$$
\begin{aligned}
& R(\lambda, B)=\left(1-R(\lambda, A) M_{h}\right)^{-1} R(\lambda, A)=\sum_{n=0}^{m} \quad\left(R(\lambda, A) M_{h}, n_{R}(\lambda, A)\right. \\
& R(\lambda, A)=\left(1-R(\lambda, B) M_{-h}\right)^{-1} R(\lambda, B)=\sum_{n=0}^{\infty} \quad\left(R(\lambda, B) M_{-h}\right)^{n_{R}(\lambda, B)}
\end{aligned}
$$

Before discussing further properties of irreducible semigroups we consider several examples.

Examples 3.4.(a) (cf. B-II.Sec.3). Suppose (T(t)) $t \geq 0$ is governed by
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-198.jpg?height=67&width=1615&top_left_y=1097&top_left_x=232) Then the following assertions are equivalent:
(i) (T(t) ${ }_{t \geq 0}$ is irreducible.
(ii) There is no closed subset of $X$ which is q-invariant except $\phi$ and $X$.
(iii) Every orbit $\left\{\phi(t, x): t \in \mathbb{R}_{+}\right\}$is dense in $x$.

More generally, these equivalences still hold if the semigroup ( $\mathbf{T}(\mathrm{t})$ ) is given by $T(t) f=h_{t}$ (fo $\phi_{t}$ ) where $h_{t}$ are suitable continuous, strictly positive, bounded functions on $X$.
(b) Suppose that the semigroup (T(t)) ${ }_{t \geq 0}$ has the following form: There exist a positive measure $\mu$ on $x$ and a positive continuous function $k:(0, \infty) \times X \times X \rightarrow \mathbb{R}$ such that
(3.1) (T(t)f) $(x)=\int_{X} k(t, x, y) f(y) d_{\mu}(y) \quad\left(t>0, f \in C_{0}(X), x \in X\right)$.
$$
\begin{aligned}
& \text { Then }(T(t))_{t \geq 0} \text { is irreducible if and only if } \\
& U_{t>0} \operatorname{supp}(k(t, x,)\} \text { is dense in } x \text { for every } x \in x .
\end{aligned}
$$
(c) We consider the first derivative $A f=f$ (cf. $A-I, 2,4$ ). If $E=C_{o}(\mathbb{R})$, then the corresponding semigroup ( $\left.T(t)\right)_{t \geq 0}$ is not irreducible. Note however, that there is no closed invariant ideal I with $\{0\} \varsubsetneqq I F E$ which is invariant under the group $(T(t)), t \in \mathbb{R}$ generated by $A$.
FOr $E=C_{0}[0, \infty)$ and $E=C_{0}(-\infty, 0)$ the corresponding semigroups are reducible (i.e. not irreducible) as well. If $E=C_{2 \pi}(\mathbb{R})$ (i.e. the 2 r~periodic functions), then $A f=f^{\prime}$ generates an irreducible semigroup on $E$. It is (isomorphic tol the semigroup of rotations on the unit circle.
(d) (cf. Ex.2.14(b)) Consider Af $=f^{\prime}$ on $E=C[\sim 1,0]$ with
$D\left(A_{\psi}\right)=\left\{f \in C^{1}: f^{+}(0)=\Psi(f)\right\}$ where the linear functional $\Psi$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-199.jpg?height=55&width=1620&top_left_y=384&top_left_x=201) corresponding semigroup is irreducible if and only if wlesupp ${ }^{\Psi}$.
(e) The second derivative $A f=f^{\prime \prime}$ generates an irreducible semigroup on $C_{o}(\mathbb{R})$ and on $C_{o}(0,1)$ (cf. A-I, 2.7). With Netmann boundary conditions (or more generally: $f^{\prime \prime}(0)=\alpha_{0} f(0), f^{\prime}(1)=\alpha_{1} f(1)$ where $\left.a_{0}, \alpha_{1} \in \mathbb{R}\right)$ the second derivative generates an irreducible semigroup on $C[0,1]$ (cf. A-I.2.7).
The operator $A f=f "$ - Vf on $C_{o}(\mathbb{R})$, where $V$ is continuous, real-valued with inf $V(x)>-\infty$ (see Example 2.14(a)) also generates an irreducible semigroup. This can be derived from the maximum prinu ciple as follows: For $\lambda>\operatorname{linf} V(x), f \in C_{o}(\mathbb{R}), G:=R(\lambda, A) f$ we have $g \in C^{2}$ and $g h-(\lambda+V) g=-f$. If $f>0$, then $g>0$, hence [Protterweinberger (196\%), Chap.I, Thm. 3] implies that $g$ is strictly positive.
(f) The Laplacian $A$ generates an irreducible semigroup on $C_{0}\left(\mathbb{R}^{n}\right)$ as can be seen easily from AwI, 2,8 . More general elliptic operators will be discussed below (see Ex.3.10(b)).

We now return to the general situation and show that irreducible semigroups possess several interesting properties.

Proposition 3.5. Suppose $A$ is the generator of a strongly continuous semigroup on $C_{0}(X)$ which is irreducible. Then the following assertions are true:
(a) $\sigma(A) \neq \varnothing$;
(b) every positive eigenfunction of $A$ is strictly positive;
(c) every positive eigenvector of $A$ ' is strictly positive;
(d) if ker (s (A) - $A^{\prime}$ ) contains a positive element (e.g., if $X$ is compact (cf. Thm.l.6)), then $\operatorname{dim}(\operatorname{ker}(s(A)-A)) \leqq 1$;
(e) if $s(A)$ is a pole of the resolvent, then it is algebraically simple. The residue has the form $P=\phi \quad u$ where $\phi \in E^{\prime}$ and $u \in E$ are strictly positive eigenvectors of $A^{\prime}$ and $A$, respectively, satisfying $\langle u, \phi\rangle$ 兹 1 .

Proof. (a) Take any $f_{o} \in C_{o}(X)$ which is positive and has compact support. If $\lambda>S(A)$, then $R(\lambda, A) f_{o}$ is strictly positive (by Def. 3.l(v)), hence there exists $\varepsilon>0$ such that $R(h, A) f_{0} \geq \varepsilon f_{0}$. It follows that $R(\lambda, A)^{n_{f}} \geq E^{n_{f}} f_{0} \geq 0$ for all $n \in \mathbb{N}$ and therefore
$r(R(\lambda, A))=1 \operatorname{im}\left\|R(\lambda, A)^{n}\right\|^{1 / n} \underline{\underline{3}} \quad>0$.
The assertion now follows from A-III, Prop.2.5.
(b) Suppose $A h=r h$ where $h \neq 0$ is positive. Then $r$ has to be real and we have $T(t) h=e^{r t h}(A-I I I, C o r .6 .4)$. For $|f| \leq n \cdot h$ ( $n \in \mathbb{N}$ ) we have
(3.2) $|T(t) f| \leqq T(t)|f| \leq n \cdot T(t) h=n \cdot e^{r t h}$.

This shows that the ideal generated by $h$ is invariant, hence dense by irreducibility. This is true if and only if $h$ is strictly positive.
(c) Suppose $A^{\prime} \phi=r \phi$ for some $0<\phi \in E^{\prime}$. Again $r$ has to be real and $T(t)^{\prime} \phi=e^{r t} \phi(t \geqq 0)$. From
$$
\begin{equation*}
\langle | T(t) f|, \phi\rangle \leqq\langle T(t)| f|, \phi\rangle=\langle | f\left|, e^{r t} \phi\right\rangle, f \in E \tag{3.3}
\end{equation*}
$$
it follows that $I:=\{f \in E: \phi(|f|)=0\}$ is an invariant ideal. We have $I \neq E$ (because $\phi \neq 0$ ), hence the irreducibility implies $I=$ (0) , i.e., $\phi$ is strictly positive.
(d) By (a) we know that $s(A)>w-m$ hence we can assume without loss of generality that $s(A)=0$. By (c) there exists a strictly positive $\psi \in E^{\prime}$ such that $A^{\prime} \Psi=0$. It follows from (2.14) and (2.15) that
(3.4) $h \in \operatorname{ker} A$ implies $|h| \in \operatorname{ker} A$.

Assuning dim(ker $A) \geq 2$, then there is an eigenfunction $h \in \operatorname{ker} A$, $h \neq 0$ which has at least one zero in $x \quad\left(h:=h_{1}\left(x_{0}\right) \cdot h_{2}-h_{2}\left(x_{0}\right) \cdot h_{1}\right.$, where $h_{1}, h_{2}$ are linearly independent, $x_{0} \in x$ ). By (3.4) $|h|$ is a positive eigenfunction but not strictly positive. This is a contradiction with (b).
(e) If $s(A)$ is a pole, then there exists a corresponding positive eigenfunction (see the proof of Cor. 1.4 ). By (b) it is even strictly positive, thus $s(A)$ is a first order pole by kem. 2.15(a) : The residue $P$ is a positive operator satisfying $P E=k e r(s(A)-A)$ and $P^{\prime} E^{\prime}=\operatorname{ker}\left(s(A)-A^{\prime}\right)$, thexefore the remaining assextion follows from (e), (b) and (d).

In the remainder of this section we focus our interest on the boundary spectrum of irreducible semigroups, more precisely, on the eigenvalues and the corresponding eigenfunctions of the boundary spectrum. In view of assertion (a) of Prop. 3.5 the assumption "s(A) $=0 \|$ is not crucial in the following theorem. However, it allows a simpler formulation.

Theorem 3.6. Suppose $T=(T(t))$ is an irreducible semigroup with generator $A$ and spectral bound $s(A)=0$. Assume that there exists a positive linear form $\psi \neq 0$ such that $A{ }^{\prime} \psi=0$. (This is automatically satisfied whenever X is compact (see Thm.l.6).)
If $P o(A) \| i \mathbb{R}$ is non-empty, then the following assertions are true:
(a) Po(A) fin is a (additive) subgroup of $i \mathbb{R}$.
(b) The eigenspaces corresponding to $\lambda \in P \sigma(A) \cap i R$ are one-dimensional.
(c) If $A h=i a h(h \neq 0, a \in \mathbb{R})$, then $h$ has no zevog in $X$. In case $\alpha=0$ then $h(x) /|h(x)|$ is constant; otherwise, $\{h(x) /|h(x)|: x \in x\}$ is a dense subset of $T$.
(d) If $A h=i a h \quad(h \neq 0, \alpha \in \mathbb{R})$, then
(3.5) $\quad S_{h}(D(A))=D(A)$ and $S_{h}^{-1}{ }_{\circ R \circ S_{h}}=(A+i \alpha)$.

In particular, spectrum and point spectrum of $A$ are invariant under translations by $i \alpha$.
(e) 0 is the only eigenvalue admitting a positive eigenfunction.

Proof. By Prop.3.5(c) the invariant linear form $\Psi$ is strictly positive and it satisfies $T(t)^{1}=\psi(t \geq 0)$ 。
(d) Supposing $A h=i \alpha h \quad(h \neq 0, a \in \mathbb{R})$ then $A|h|=0$ by (2.14) and (2.15). By Prop.3.5(b) $|h|$ is strictly positive, thus Thm. 2.4(b) implies (3.5).
(b) Assertion (d) implies that $S_{h}$ maps ker(ia $\left.+A\right)$ onto ker A whenever $i x \in \operatorname{Po}(A) \| i=1$, Moreover, we have seen in the proof of (d) that kex $A \neq\{0\}$ hence it is one-dimensional by Prop. $3.5(\mathrm{~d})$.
(a) Assume that $A h=i \alpha h, A g=i \beta g(\alpha, \beta \in \operatorname{H}, \mathrm{~h} \neq 0, \mathrm{~g} \neq 0)$. By (3.5) we have $S_{\bar{G}} A S_{G}=A+i \beta$ and $S_{h} A S_{\bar{h}}=A-i \alpha$, therefore
$$
\begin{equation*}
A+i(B-\alpha)=S_{h}(A+i B) S_{\bar{h}}=S_{h} S_{g} A S_{g}^{S-}{ }_{h} \tag{3.6}
\end{equation*}
$$

It follows that $\operatorname{ker}[A+i(\beta-\alpha)]=S_{h} S_{g}(\operatorname{kex} A) \neq\{0\}$, hence $i(\beta-\alpha) \in \operatorname{Po}(A)$.
(e) If $A f=\lambda f$ where $f>0$, then
$$
\begin{equation*}
\lambda \cdot\langle f, \Psi\rangle=\langle A f, \Psi\rangle=\left\langle f, A^{\prime} \psi\right\rangle=0 . \tag{3.7}
\end{equation*}
$$

Since $\Psi$ is strictly poritive we have $\langle f, Y\rangle\rangle 0$ hence $\lambda=0$.
(c) We already know that $A h=$ ioh implies that $A|h|=0$. It follows from Prop. 3.5 (b) that $h$ is strictly positive; i.e., h has no zeros in $X$. By Prop. 3.5 (d) ker $A$ is one-dimensional hence every
eigenfunction corresponding to 0 is the scalax multiple of a strictly positive function. If $A h=i a h, h \neq 0, a \neq 0$ we consider $\bar{h}(x):=h(x) /|h(x)|$. Assuming that $\hat{h}(X)$ is not not dense in $\quad r^{\prime}$, there exists a sequence of polynomials ( $P_{n}$ ) new such that
$$
\begin{equation*}
\mathrm{P}_{\mathrm{n}}(z)+1 / \mathrm{z} \text { uniformly in } \mathrm{z} \in \tilde{\mathrm{~h}}(\mathrm{x}) \text {. } \tag{3.8}
\end{equation*}
$$

It follows that $h(x) \cdot P_{n}(h(x)) *|h|(x)$ uniformly in $x \in X$. obvious$l y, h \cdot P_{n}(h)$ is a lineax combination of $h^{[1]}, h^{[2]}, h^{[3]}, \ldots$ that is, it is an element of span\{ $\left.U_{k=1} k e r(i k \alpha-A)\right\} \quad(c f . \operatorname{Thm.2.4)}$. By (3.7) the linesr form $\Psi$ vanishes on $k e r(\lambda-A)$ whenever $\lambda \neq 0$. Therefore $\left\langle h \cdot P_{n}(h), \psi\right\rangle=0$ and we have $\left.0<\langle | h|, \Psi\rangle=1 \lim _{n \rightarrow \infty}<h * p_{n}(h), \psi\right\rangle=0$ which is a contradiction.

The group Po(A) fik need not be discrete. For example, the semigroup described in Ex.2.6(d) satisfies the assumptions of Thm. 3.6 if $\alpha / \mathrm{s}$ is ixrational. In this case $P \sigma(A)=i \alpha Z+i \beta \neq i s$ a dense subgroup of ik . Actually one can show that for every subgroup $H$ of in there is an irreducible semigroup on $C(G), G:=\left(H_{d}\right)$, such that $P o(A)=$ $H$. Here $\left(H_{d}\right)$ denotes the dual of the abelian group $H$ equipped with the discrete topology. For details see [Greinex (1982), p.62].

An immediate consequence of assextion (d) of Theorem 3.6 is the following corollary.

Corollary 3.7. Suppose $T$ satisfies the hypotheses of Thrm.3. 6 and let $A$ be its generator. If $k$ is a bounded continuous real-valued function, $M_{k}$ the corresponding multiplication operator, then for $B:=A+M_{k}$ we have $\sigma(B)+P \sigma(A)$ तit $=\sigma(B)$.
In particular, $s(B)+P o(A) \| i \mathbb{R} \subset o(B)$.

The next two corollaries are essentially consequences of assertion (c) of Theorem 3.6. The statement of the first one can be summarized as follows: In case there are non-real eigenvalues in the boundary spectrum then the semigroup 'contains' the semigroup of rotations on $I$.

Corollary 3.8. Suppose that the hypotheses of Thm. 3.6 are satisfied and that there is an eigenvalue ia of $A$ with a $>0$.
Let $\tau:=2 \pi / \alpha$.
Then there exists a continuous injective lattice homomorphism
$j: C(\Gamma) \rightarrow C_{O}(X)$ such that the diagram
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-203.jpg?height=298&width=549&top_left_y=271&top_left_x=731)
commutes. ( $R_{\tau}(t)$ ) denotes the rotation semigroup of period $\tau$ (see A-I, 2.5).

If $x$ is compact, then $j$ is a topological embedding.

Proof. Assume that $A h=i \alpha h, c>0$, and let $\hat{h}(x):=h(x) / i h(x) \mid$. Then we define $j$ by
```
(3.9) j(f):= |h|=foĥ (i.e., (j(f)) (x) = |h(x)| f f(h(x))).
```

Obviously, j is a lattice homomorphism and because $h$ has no zeros and $h$ has a dense image in $\Gamma$ (Thm.3.G(c)), it follows that $j$ is injective. For the functions $e_{n} \in C(J)$ given by $e_{n}(z)=z^{n} \quad(n \in Z)$ one has $j\left(e_{n}\right)=h^{[n]} \quad(n \in \mathbb{Z})$ and therefore $T(t) \circ j\left(e_{n}\right)=T(t) h^{[n]}=e^{i n \alpha t} \cdot h^{[n]} \quad(C f$. Thm. 2.4) and $j \circ R_{\tau}(t)\left(e_{n}\right)=j\left(e^{i n \alpha t} e_{n}\right)=e^{i n \alpha t} \cdot h^{[n]}$.
Since $\left\{e_{n}: n \in \mathbb{Z}\right\}$ is a total subset of $C(\Gamma)$ we have $T(t) \circ j=j \circ R_{T}(t) \quad$ for every $t>0$.
If $X$ is compact, then $\hat{h}(x)$ is closed, hence $f i s$ isto, moreover, $|h| 2 \varepsilon$ for some $\varepsilon>0$ thus the definition of $j$ implies thet $\|\dot{j}(\mathrm{f})\|>\varepsilon \mathrm{f} \| \mathrm{f}$ for every $\mathrm{f} \in \mathrm{C}(\mathrm{I})$.

A consequence of Cor. 3.8 is the following: If $\{s(A)\} \bar{F}$ Po(A) $\operatorname{li} i \mathbb{R}$, then for every $E \quad>\quad 0$ there exists $g>0$ such that $T(t) g$ and $T(s) g$ have disjoint support whenever $|s-t|=E$. Another consequence is thet there exist positive functions $f_{1}$ and $f_{2}$ such that $T(t) f_{1}$ and $T(t) f_{2}$ have disjoint support for every $t \geq 0$ (consider the images under j of two disjoint functions on $C(\Gamma)$ ). This observation proveg the following corollary.

Corollary 3.9. Suppose that the hypotheses of Thm. 3.6 are satisfied and that for some $t_{0}>0$ we have $T\left(t_{0}\right) f \gg 0$ whenever $f>0$. Then $P \sigma(A)$ Miig $=\{0\}$.

Cor. 3.9 can be applied if $T\left(t_{0}\right)$ is a kernel operator with strictly positive kernel. We give some examples:

Examples 3.10. (a) We assume that the semigroup (T) (t) satisfies the hypotheses of Thm. 3.6 and that it is given by
$$
(T(t) f)(x)=\int_{X} k(t, x, y) f(y) d \mu(y)
$$
where $\mu$ is a positive measure and $k$ is a positive continuous function (see Ex. $3.4(\mathrm{~b})$ ). We will show that $\operatorname{Po}(A) \cap(s(A)+i \mathbb{R})=\{s(A)\}$. Assuming the contrary, by Thm. $3.6(\mathrm{~d})$ there exist $a \neq 0$, $h \in C_{o}(X)$ such that
(3.10) $S_{\bar{h}} \cdot T(t) \circ S_{h}=e^{i \alpha t} \cdot T(t)$ for all $t \geqslant 0$.

This implies that $k$ satisfies
(3.11) $\quad \overline{h(x)} \left\lvert\, \frac{h(y)}{|h(x)|} \cdot k(t, x, y)=e^{i \alpha t} k(t, x, y) \quad(t>0, x, y \in X)\right.$.

It follows that for $0<|s-t|<2 \pi / a k(t, \ldots)$ and $k(s, \ldots)$ have disjoint support. This is impossible if $k$ is continuous.
(b) Let $\Omega$ be a domain in $\mathbb{F}^{n}$ and define $L_{o}$ as follows:
$$
\text { (Here } f_{i}^{\prime} \text { gtands for } \partial f / \partial x_{i} \text {, thus } f_{i j}^{\prime}=\partial^{2} f / \partial x_{i} \partial x_{j} \text { ) }
$$

Suppose that $L_{o}$ is elliptic, $a_{i j}, b_{i}$, c are real-valued cofunctions with $\lambda_{o}:=\sup c<\infty$, assume further that the closure $L$ of $L_{o}$ is the generator of a positive semigroup on $C_{o}(\Omega)$ which has compact resolvent. For example this is true if $\partial \Omega$ is $c^{\infty}$ and $a_{i j} \in C^{( }(\bar{\Omega}) \quad(C f$ Thm. 4.8 .3 of Fattorini (1983)). We will show that $\operatorname{Po}(A) \|(s(A)+i R)=\{s(A)\}$. In order to apply Thm. 3.6 we have to show that the corresponding semigroup (T(t)) is irreducible:

Given $0<f \in E$ then there is $g \in D\left(L_{o}\right)$ such that $0<g \leqq f$.
$h:=R(\lambda, L) g$ is $C^{\text {© }}$ (Weyl's Lemma) and satisfies $L_{o} h-\lambda h=-g<0$. Assuming that $\lambda>\lambda$ o then $h$ is positive, even strictiy positive by the maximum principle [Protter-Weinberger (1967), Chap.2, Thm.6].
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-204.jpg?height=50&width=1617&top_left_y=2231&top_left_x=228) cible. Next we apply Thm. $3.6(\mathrm{~d})$ in oxder to show that the spectral bound is a dominant eigenvalue. We can assume that $s(L)=0$. If $s$ (L) is not dominant, then by Thm. 3.6(d) we have
(3.12) $L_{o} h=i_{\alpha h}, L_{0}|h|=0, L_{o} \bar{h}=-i_{a} \bar{h}$ for some $h \neq 0, \alpha>0$
$$
\begin{aligned}
& L_{o} f:=\sum_{i, j=1}^{n} a_{i j} f_{i j}^{i}+\sum_{i=1}^{n} b_{i} f_{i}^{i}+c i, \\
& \text { with domain } D\left(L_{0}\right):=\left\{f \in C_{O}(\Omega): f \text { is } C^{\infty}, L_{O} f \in C_{O}(\Omega)\right\} \text {. }
\end{aligned}
$$

If we define $u:=|h|$ and $w:=h /|h|$, then (3.12) readg
$$
\begin{equation*}
L_{0}(u w)=i \alpha u w, L_{0}(u)=0, I_{0}(u / w)=-i a \cdot u / w . \tag{3.13}
\end{equation*}
$$

Explicit calculation of $L_{o}(u w)$ and $L_{o}(u / w)$ using the product formula for differentation yields las above we write fi instead of $\partial f\left(\partial x_{1}\right)$ :
$$
\begin{aligned}
(3.14) & L_{o}(u w)
\end{aligned}=w L_{o}(u)+u \sum_{i, j} a_{i j} w_{i j}^{\prime}+\sum_{i}\left(u b_{i}+\sum_{j} a_{i j} u j\right) w_{i}^{\top} .
$$
observing that $(1 / w) \underset{i}{\prime}=-w^{-2} w_{i}^{\prime}$ and $(1 / w)_{i j}^{i}=w^{-3} \cdot\left(2 w_{i}^{\prime} w_{j}^{\prime}-w_{i}^{\prime} i j\right)$ we obtain:
$$
\begin{equation*}
L_{o}(u w)+w^{2} L_{o}(u / w)=2 w L_{o}(u)+2 u / w \cdot \Gamma_{i j} a_{i j} w_{i}^{\prime} w_{j}^{\prime} \tag{3,15}
\end{equation*}
$$

This identity and (3.13) implies that $2 u / w \cdot \sum_{i j} a_{i j} w_{i}{ }^{\top}{ }_{j}=0$. Since $u$ has no zeros and ( $a_{i j}$ ) is positive definite, it follows that grad $w=\left(w_{i}^{\prime}\right)=0$ in $\Omega$, hence $w=$ const. . Then by (3.13) we have iouw $=L_{o}(u w)=w L_{o}(u)=0, a$ contradiction.

The asstuption that $L_{o}$ is elliptic. i.e., that ( $a_{i j}$ ) is positive definite, is essential in ordex to show that there is only one eigenvalue in the boundary spectrum. In the following example (aji) is positive semi-definite and $P \sigma_{b}(A)=s(A)+i \alpha \mathbb{Z}$.
(c) We consider $\Omega=\left\{(x, y) \in \mathbb{R}^{2}: 1<\left(x^{2}+y^{2}\right)^{1 / 2}<2\right\}$, and the second order differential operator $L_{o}$ given by $\left(L_{o} f\right)(x, y)=1 /\left(x^{2}+y^{2}\right) \cdot\left(x^{2} f_{x x}+2 x y f_{x y}+y^{2} f_{y y}\right)+\left(x f_{y}-y f_{x}\right)$. The assertion concerning the boundary spectrum can be verified easily by using polar coordinates: $x=r \cdot \cos ^{*}, y=r^{*} \sin { }^{\omega}$. Then $L_{o}$ becomer $L_{0} f=f_{x x}+f_{u}$ on the space $C_{0}(1,2) C_{2 \pi}(R)$.

In this section we have seen that the eigenvalues in the boundary spectrum of an irxeducible semigroup form a subgroup of in (provided that $\quad s(A)=0$ ). We conclude this section mentioning an analogous statement for the whole boundary spectrum of Markov semigroups on $C(K)$, $K$ compact. It seems to be unknown if this is true for irreducible semigroups in general. To prove this result one uses the proof of the analogous result for a single operator (cf. Schaefer (1968), Thm.7) as a guideline.

Theorem 3.11. Suppose that $T$ is an irreducible semigroup of Markov operators on $C(K)$, $K$ compact. Then $\sigma_{b}(A)$ is a subgroup of $i \mathbb{R}$. Hence either $\sigma_{b}(A)=\{0\}$ or $=1 \mathbb{R}$ or $i_{\alpha} \mathbb{Z}$ for some $a>0$.

\section*{4. SEMIGROUPS OF LATTICE HOMOMORPHISMS}

As we have seen in Section 2 the boundary spectrum of a many positive semigroups is a cyclic set. However, there are hardly any restrictions on the set $\{\lambda \in \sigma(A): \operatorname{Re} \lambda<S(A)\}$, except that it is symmetric with respect to the real axis. For semigroups of lattice homomorphisms the situation is quite different. We will show that the whole spectrun is an imaginary additively cyclic subset of $\mathbb{C}$ (see Def.2.5). A complete proof of this results requires some facts of the theory of Banach lattices, therefore, we postpone it to Part $C$ (see C-III, Thm.4.2).

Theorem 4.1. If $A$ is the generator of a semigroup of lattice homomoxphisms, then $\sigma(A), A \sigma(A)$ and $P o(A)$ are cyclic subsets of $\mathbb{C}$.
$1^{\text {st }}$ part of the proof. We prove the assertion concerning $A O(A)$ and $P o(A)$. Assume that $A h=(\alpha+i \beta) h, \alpha, B \in \mathbb{R}, h \neq 0$, then $T(t) h=e^{\alpha t} e^{i \beta t} h$ for all $t \geqq 0$ (A-III, Cor.6.4). Since $T(t)$ is a lattice homomorphism we havo $T(t)|h|=|T(t) h|=e^{\alpha t}|h| \quad(t \geqslant 0)$ or $A|h|=\alpha|h|$, hence $A h^{[n]}=(\alpha+i n \beta) h^{[n]}$ for all $n \in \mathbb{Z}$ by Thm.2.4(b) . We have shown that $P \sigma(A)$ is cyclic.
To prove that $A \sigma(A)$ is cyclic as well, one considers a semigroup F-product $E_{F}^{\top}$ of $E$ (see A-III,4.5). It is easy to see that $E_{F}^{\top}$ is a Banach lattice and ( $\left.T_{F}(t)\right)$ is a semigroup of lattice homomorphisms. The proposition in A-IIT, 3.5 implies $A \sigma(A)=P \sigma\left(A_{F}\right)$. Thus the assertion follows from the cyclicity of point spectrum.

Performing a similar construction as in Ex.2.6(f) one can show that every closed cyclic subset of $\mathcal{C}$ which is contained in a left halfplane is the spectrum of a suitable semigroup of lattice homomorphisms. For details see Derndinger-Nagel (1979).
In the following we restrict ourselves to the case of compact spaces. Then a semigroup of lattice homomorphisms can be described explicitly by a semi-flow and real-valued functions $h$ and $p$ (see B-II, Thms.3.5 3.6). The function $p$ has no influence on spectral properties (cf. B-II, (3,7)). Therefore we will assume that (T (t)) has the following form (cf. B-II,Thm.3.5):
```
(4.1) T(t)f= ht.f.0\phit (t @ 0, f fC(K)) where
        \phi=(\mp@subsup{\phi}{t}{}):\mp@subsup{\mathbb{R}}{+}{+}\timesK->K is a continuous semiflow and 
        h t (x)= Exp \int {
        continuous function h : K -> i .


In the following we will describe the spectrum of the semigroup given by (4.1) in terms of $\phi$ and $h$. At first we have to fix some notation. Let $K, 4, h$ be as in (4.1).
$$
\begin{equation*}
K_{t}:=\Phi_{t}(K) \quad(t<\infty), K_{m}:=\Pi_{t<\infty} K_{t} \tag{4.2}
\end{equation*}
$$

Some properties of the sets $K$ are listed in the following lemma. The proof is not very difficult and is left as an exercise.

Lemma 4.2 . Every $K_{t}(0 \leqslant t \leqslant \infty)$ is a non-empty closed subset of $k$ which is invariant undex the semiflow $\phi$. Moreover, the following assertions are true:
(a) For $s>t$ we have $K_{s} \subset K_{t}$. In case that $K_{g}=K_{t}$ then $K_{t}=K_{m}$.
(b) $\phi_{t}\left(K_{\infty}\right) \not K_{\infty}$ for all $t \geq 0$.
(c) If one partial mapping $\phi_{t}, t>0$, is injective (surjective), then all mappings $\phi_{s}$ are injective (surjective).

We call a semiflow $q$ injective (surjective) if one and hence all of the partial mappings $\phi_{t}$ are injective (surjectivel. Studying the spectrum of the semigroup given by (4.1) we divide the complex plane into three sets:
(4.3) $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda<\underline{C}(h, \phi)\}$
$\{\lambda \in \mathbb{C} ; C(h, \phi) \leq \operatorname{Re} \lambda \leq \bar{c}(h, \phi)\}$
$\{\lambda \in \mathbb{C} ; \bar{c}(h, \phi)<\operatorname{Re} \lambda\}$.

The quantities $c(h, \phi)$ and $\bar{c}(h, \phi)$ are defined as follows:
(4.4) $\bar{c}(h, \phi):=1 \operatorname{im}_{t \rightarrow \infty} \bar{c}_{t}(h, \phi)=\inf { }_{t>0} \bar{c}_{t}(h, \phi)$ where
$\vec{c}_{t}(h, \phi): \# \sup _{x \in K}\left\{1 / t=\int_{0}^{t} h(\phi(s, x)) d s\right\}(t>0)$.
C $(h, \phi):=\lim _{t \rightarrow \infty} \underline{C}_{t}(h, \phi)=\sup _{t>0} \underline{C}_{t}(h, \phi)$ where
$c_{t}(h, \phi):=\operatorname{in} f_{x \in K}\left\{1 / t \cdot \int_{0}^{t} h(\phi(s, x)) d s\right\} \quad(t>0)$.
It is easy to see that $\vec{c}_{t}(h, \phi)=1 / t \cdot \log \|T(t)\|$, hence in the definition of $\bar{c}(h, \phi)$, both the limit and the infimum exist and coincide with the growth bound (see $A-I,(1.1))$. Furthermore, $C_{t}(h, \phi)=-\bar{c}_{t}(-h, \phi)$. Therefore, $\subset(h, \phi)$ is well defined too.

First we will describe the part of $\sigma(A)$ which is contained in the left half-plane determined by $g(h, \phi)$. It turns out that either the whole halfwplane is contained in o(A) or it has empty intergection with o(A) . This depends only on propexties of $\phi$. Essentially there
are three different cases. Before we state the general result (Thm.4.4) we give some typical examples.

Examples 4.3.(a) Consider on $K=[0, \pm]$ the semiflow defined by $\phi(t, x):=x+t(x+t=\infty)$. Then we have $K_{t}=[t, \infty]$ and $K_{m}=\{\infty\}$. The spectrum of the corresponding semigroup $T(t) f=f o \phi_{t}$ is given by $\sigma(A)=A \sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \leqq 0\}$.
(b) Consider again $K=[0, \infty]$ and define a semiflow by
$\phi(t, x)=\left\{\begin{array}{cc}x-t \quad \text { if } x \geq t \\ 0 & \text { if } x < t\end{array} \quad(\infty-t=\infty) \quad\right.$.
Then we have $K_{t}=K$ for all $t$, hence $K_{m}=K$ and $\sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \leq 0\}, \operatorname{Ro}(A)=\{\lambda \in \mathbb{C}=\operatorname{Re} \lambda<0\} \cup\{0\}$.
(c) Consider on $K_{1}:=[-1, \infty)$ the equivalence relation $\sim$ defined by " $x \sim y$ if ond only if $x, y \geqq 0$ and $x-y \in Z "$. The semiflow $\$_{1}$ on $K_{1}$ given by $\phi_{1}(t, x)=x+t$ induces a semiflow $\phi$ on the
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-208.jpg?height=70&width=1509&top_left_y=1230&top_left_x=222) $\left(K_{\infty} \not[0,1] / \ldots \cong\right.$ ) . The spectrum of the corresponding semigroup on K is given by $\sigma(\mathrm{A})=2 \pi i \mathbb{Z}$.
(d) Consider on $K=[-1,1]$ the flow $\phi$ given by
$\phi(t, x): \% \begin{cases}-1 & \text { if } x<0 \text { and } t>-\frac{x+1}{x} \\ \frac{x}{1+t} & \end{cases}$ $\frac{x}{1+t x}$ othexwise.
Then we have $K_{t}=\left[-1, \frac{1}{1+t}\right], K_{\infty}=[-1,0]$ and
$\sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \leq 0\},\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \in 0\} \notin \operatorname{Ao}(A) \cap \operatorname{Ro}(A)$.

Further examples related to ordinary differential equationg on $\mathbb{R}^{n}$ will be given after we have stated and proved the general result:

Theorem 4.4. Suppose $T$ is a semigroup of lattice homomorphisms given by (4.1) with generator $A$. Considering $H:=\{\lambda \in \mathbb{C}$ : Re $\lambda<\underline{C}(h, \phi)\}$, where $\underline{C}(h, \phi)$ is given by (4.4), we have:
(a) If $K_{t} \neq K_{\infty}$ for every $t<\infty$, then $H \subseteq A_{\sigma}(A)$.
(b) If $\left.\right|_{K_{\infty}}$ is not injective, then $H \subseteq \operatorname{Ro}_{0}(A)$.
(c) If $K_{g}=K_{m}$ for some $s<\infty$ and ${ }^{\phi} \mid K_{\infty}$ is injective, then $H \cap \sigma(A)=\emptyset$.

Propf. For $E>0$ we define $H_{E}=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda<\underline{C}(h, \phi)-\varepsilon\}$. obviously it is enough to prove assertion (a), (b) and (c) respectively for $H_{2 E}$, $\varepsilon$ arbitrary, instead of $H$.
(a) By the definition given in (4.4) there exists a $\tau>0$ such that $C_{t}(h, \phi) \quad \underset{C}{ }(h, \phi)-\varepsilon$ for all $t \geqslant i$. It follows that (4.5) $h_{t}(x) \nexists e^{(a+\varepsilon) t}$ whenever $t \geqslant \tau, x \in K, a \ll(h, \phi)-2 \varepsilon$. Now we fix $\lambda=\alpha+i \beta \in H_{2 \varepsilon} \quad(\alpha, \beta \in \mathbb{R})$ and construct an approximate eigenvector ( $g_{n}$ ) of $A$ corresponding to $\lambda$. For $n \in \tau+1$
we choose an arbitrary function $g_{n} \neq 0$. Now suppose $n>\tau+1$. We choose $x_{n} \in K_{n+1 / 2}$ ( $K_{n+1}$ (cf. Lemma $\left.4.2(a)\right)$, then there exists $y_{n} \in K$ such that $\uparrow\left(n+1 / 2, y_{n}\right)=x_{n}$. We have
$\psi\left([0, n+1 / 2], y_{n}\right) r K_{n+1}=\phi$ and the mapping $t \rightarrow \psi\left(t, y_{n}\right)$ is a continuous injection, hence a homeomorphism from $[0, n+1 / 2]$ into $K$ ithis is true because $\left.\phi\left(n+1 / 2, y_{n}\right) k K_{n+1}\right)$. By Tietze's Theorem there is $f_{n} \in C(K)$ such that
$$
\begin{align*}
& \left\|f_{n}\right\| \leqq 1, f_{n} \mid K_{n+1}=0,  \tag{4.6}\\
& f_{n}\left(\phi\left(t, y_{n}\right)\right) \Rightarrow 0 \text { for } 0 \leqq t \leqq n-(1+\delta) \text { and } n+\delta \leqq t \leqq n+1, \\
& f_{n}\left(\phi\left(t, y_{n}\right)\right)=e^{i \beta t} \text { for } n-1 \leqslant t \leqq n .
\end{align*}
$$

The constant $\delta \in(0,1 / 2)$ will be determined later. Considering $g_{n}:=\int_{0}^{n+1} e^{-\lambda t} T(t) f_{n} d t$, then $g_{n} \in D(A)$ and
$$
\begin{align*}
(\lambda-A) g_{n} & =\left(1-e^{-\lambda(n+1)} T(n+1)\right) f_{n}=  \tag{4.7}\\
& =f_{n}-e^{-\lambda(n+1)} \cdot h_{n+1} \cdot f_{n}{ }^{n} \phi_{n+1}=f_{n}
\end{align*}
$$

Moreover,
$\left\|g_{n}\right\| \sum\left|g_{n}\left(y_{n}\right)\right| \Rightarrow\left|\int_{0}^{n+l} e^{-\lambda t} h_{t}\left(y_{n}\right) f_{n}\left(\phi\left(t, y_{n}\right)\right) d t\right| \geqq$
$\left|\int_{n-1}^{n} e^{-\lambda t} h_{t}\left(y_{n}\right) e^{i \beta t} d t\right|-\left[\int_{n-(1+\delta)}^{n-1}+\int_{n}^{n+\delta} \mid e^{-\lambda t_{n}} h_{t}\left(Y_{n}\right) f_{n}\left(\phi\left(t, y_{n}\right) \mid d t\right]\right.$
$z \int_{n-1}^{n} e^{-\alpha t} e^{(\alpha+\varepsilon) t} d t-\left[\int_{n-(1+\delta)}^{n-1}+\int_{n}^{n+\delta} e^{-\alpha t}\left|h_{t}\left(y_{n}\right)\right| d t\right]$
$=1 / \varepsilon \cdot\left(e^{\varepsilon n}-e^{\varepsilon(n-1)}\right)-\left[\int_{n-(1+\delta)}^{n-1}+\int_{n}^{n+\delta} e^{-\alpha t}\left|h_{t}\left(y_{n}\right)\right| d t\right]$.
The constant $\delta$ can be chosen such that
(4.8) $\left\|g_{n}\right\| \geqq 1 / 2 E \cdot\left(e^{E n}-e^{E(n-1)}\right) \rightarrow \infty$ for $n \rightarrow \infty$.

It follows from (4.8) and (4.7) that $g_{n} /\left\|g_{n}\right\|$ is an approximate eigenvector of $A$ corresponding to $\lambda$. Thus (a) is proved. The proofs of (b) and (c) will be handled simultaneously. Fixst we show that we can restrict attention to the case where $K=K_{\infty}$.
Indeed, $K_{\infty}$ is a $\phi$-invariant subset, hence $I_{\infty}:=\left\{f \in C(K): \mathcal{E}^{f} \mid K_{c}=0\right\}$ is a $T$-invariant ideal. Identifying $C(K) / I_{\infty}$ with $C\left(K_{\infty}\right) \quad$ (cf. $B-I$, Sec.l), then $\left(T(t) / I_{s}\right)$ is the semigroup governed by $\phi \mid K_{s} \quad$ and $\left.{ }^{h}\right|_{K_{s}}$. Since one always has $R o(A)$ $E \operatorname{Ro}(A)$, assertion (b) is proved
when we can show that $H_{2 \varepsilon} \subseteq \operatorname{Ro}(A$,$) . In case (c) one has K_{s}=K_{\infty}$ for some $s<\infty$, which implies $\left.T(s)\right|_{I_{s}}=0$. Hence we have
$\sigma\left({ }^{A} \mid I_{\infty}\right)=\emptyset$ and therefore $\sigma(A)=\sigma\left(A / I_{\infty}\right)$ by $A-I I I, \operatorname{Prop} .4 .2$. Henceforth we will assume that $K=K_{\infty}$, that is, $\phi$ is surjective (cf. Lemima 4.2(b)).
We choose $\tau>0$ such that (4.5) is true. Since $\quad$ is surjective, for every $f \in C(K)$ there is $a x_{f} \in K$ such that $\|f\|_{i}=\left\|\left(\phi\left(i, x_{f}\right)\right)\right\|$ and we obtain for $\lambda \in H_{2 \varepsilon}, \lambda=\alpha+i \beta, \alpha, \beta \in \mathbb{R}$ :
(4.9) $\|\left.\left(e^{\lambda T}-T(\tau)\right) f\right|_{i} \geqq\left|h_{\tau}\left(x_{f}\right) f\left(\phi\left(\tau, x_{f}\right)\right)-e^{\lambda \tau} f\left(x_{f}\right)\right|$
$$
\begin{aligned}
& \geqq h_{T}\left(x_{f}\right)\|f\|-e^{\alpha \tau}\left|f\left(x_{f}\right)\right| \\
& \geqq e^{(\alpha+E) T}\|f\|-e^{\alpha \tau}\left\|_{i f}\right\| \\
& =e^{\alpha \tau}\left(e^{E \tau}-1\right)\|f\|
\end{aligned}
$$

It follows that the dise $D:=\{\lambda \in \mathcal{C}:|\lambda|<\exp (c(f, \phi)-2 g)\}$ has an empty intersection with $A o(T(T))$ and therefore $H_{2 \varepsilon}$ iAo(A) $=\varnothing$ by A-III, 6.2 . Since every boundary point of the spectrum is an approximate eigenvalue (A-III, Prop. 2. 2(i)) we have the following alternative:
(4.10) Either $D E(T(T))$ and $H_{2 E} G p(A)$ or else $D \subseteq \operatorname{Ro}(T(\tau))$ and $H_{2 g} \subseteq \operatorname{Ro}_{\sigma}(\mathrm{A})$.

It is not difficult to see that $0 \in \rho(T(T))$ whenever $\phi t$ is bijective and that 0 is an eigemvalue of $T(T)$ if $\phi_{\tau}$ is not injective. since we assumed that that $\phi$ is surjective, assertions (b) and (c) of the theorem are immediate consequences of (4.10).

The examples $4.3(a)$, (b) and (c) respectively are prototypes of the three different cases considered in Thm. 4.4 . Ex. 4.3 (c) also shows that there are semigroups whose spectrum is contained in a right half-plane, although they cannot be embedded in a group icompare Cor.4.5 below!). Ex.4.3(d) shows that (a) and (b) do not exclude each other.

Corollary 4.5. If $\psi$ is injective of surjective, then the following assextions axe equivalent:
(i) A is the generatox of a strongly continuous group.
(ii) o(A) is contained in a right half-plane.

Proof. (i) ${ }^{(i i)}$ holds true because $-A$ is a generator of a semigroup. (ii) $\rightarrow$ (i) : We have to show that one (hence each) opexator $T(t)$, $t \geqslant 0$ is invertible. Obviously this is true if $\phi$ is bijective. At first we assume that $\phi$ is surjective, that is, $K=K_{\infty}$. By Thm. 4.4 we have that ${ }^{\phi} \mid K_{m}$ is injective if (ii) is true. Thus $\phi$ is bijective. Now we assume that $\phi$ is injective. We have to show that $K=K_{c}$. By Thm. 4.4 we have $K_{\infty}=K_{g}$ for some $s$, whenever (ii) is true. Given $x \in K$ then by Lemma $4.2(b)$ there exists $y \in K_{\infty}$ such that $\phi(s, x)=\phi(5, y)$. If $\phi$ is injective we have $x=y \in K_{\infty}$,

In the following example we consider semiflows related to ordinary differential equations on $i^{n}$. In case there exists a corresponding global flow, it induces a group on $C_{o}\left(\mathbb{R}^{n}\right)$ in a canonical way Even if there is no global flow, one can construct semigroups governed by a semiflow, and apply Thm.4.4(a) in order to describe the spectrum. These examples can be earily extended to differential equations on manifolds (see Sec.l8. 2 of Dieudonné (1971)).

Example 4.6. Suppose $F: \mathbb{R}^{\Pi} \rightarrow \mathbb{R}^{\boldsymbol{n}}$ is continuously differentiable. We denote the maximal flow corresponding to the differential equation $y^{\prime}=F(y)$ by $\phi_{o}$. In general, $\phi_{o}$ is only defined on an open subset of $\mathbb{R} \times \mathbb{R}^{n}$ which contains $\{0\} \times \mathbb{R}^{n}$. For $x \in \mathbb{R}^{n}$ there exist $t_{x}$ and $\bar{t}_{x}$ such that
(4.11)
$$
\begin{aligned}
& -\infty \leq t_{x}<0<\bar{t}_{x} \leqq m ; \\
& \phi_{o}(t, x) \text { is defined if } t_{x}< t <\bar{t}_{x} ; \\
& i f\left(\bar{t}_{x}<m\left(\underline{E}_{x}>-\infty\right) \text { then }\left|\phi_{o}(t, x)\right| \rightarrow \infty \text { as } t+\bar{t}_{x}\left(t+t_{x}\right) .\right.
\end{aligned}
$$

For details see Sect. 18.2 of Dieudonné (1971)
(a) If $\phi_{O}$ is a global flow, i.e., if $\phi_{o}$ is defined on $\mathbb{A} \times \mathbb{F i n}^{n}$, then one has a corresponding (semi-)group on $C_{o}\left(\mathbb{R}^{n}\right)$. If $F$ is differentiable, its generator is the closure of ${ }^{A_{1}}$ which is defined as follows (cf. B-II.Ex. 3.15):
(4.12) $A_{1} f=(F \mid \operatorname{Grad} f):=\sum F_{i} \cdot{ }_{i} f$ with domain
$$
D\left(A_{1}\right):=\left\{f \in C^{l}: \operatorname{supp} f \text { is compact }\right\}
$$
$\phi_{O}$ can be uniquely extended to a flow $\tilde{\phi}_{o}$ on $\mathbb{R}^{n} u\{\infty\}$ by defining $\tilde{\phi}_{0}(t, \infty):=\infty$ for all $t \in \dot{H} \cdot \phi_{o}$ and $\tilde{\phi}_{0}$ satisfy condition (c) of Thm. 4.4 .

A global flow exists for example if $F$ is globally Lipschitz continuous or if $F$ is uniformly bounded. In case $\left\{x \in \mathbb{R}^{n}:(x \mid F(x))>0\right\}$ is bounded in $\mathbb{R}^{n}$ a global semiflow always exists (see [Deimling (1977), Sec.5.2年).
(b) We do not asstrue that $\phi_{o}$ is globally defined. Instead we consider a bounded domain $\Omega \in \mathbb{R}^{\mathrm{n}}$ with smooth boundary $a \Omega$ such that $(F(x) \mid v(x))>0$ for every $x \in \partial \Omega$. Here $v(x)$ denotes the outward normal vector.

Then for $x \in \bar{\Omega}$ we have $t_{x}=-\infty$. Moreover, either $\phi_{o}(t, x) \in \Omega$ for all $t \geq 0$ or else there exists a unique $s_{x}$ with $0 \leqq s_{x}<\bar{t}_{x}$ such that $\phi_{o}\left(s_{x}, x\right) \in \partial \Omega$. In the first case we write $s_{x}:=0$. Then we define $\phi: \mathbb{R}_{+} \times \stackrel{\pi}{\Omega} \rightarrow \overline{\bar{\Omega}}$ as follows:
$\phi(t, x):=\left\{\begin{array}{lll}\phi_{0}(t, x) & \text { if } 0 \leq t < s_{x} \\ \phi_{0}\left(s_{x}, x\right) & \text { if } & t \geq s_{x}\end{array}\right.$
$\phi$ is a continuous semiflow on the compact set $k:=\bar{\Omega}$. We have $K_{c}=K$ and ${ }^{\phi} \mid K_{\infty}$ is not injective.
In case $F$ is differentiable, the generator of the corresponding semigroup is the closure of the operator $A_{2}$ defined by
$A_{2} f:=(F \mid g r a d f), D\left(A_{2}\right):=\left\{f\left(C^{l}(\hat{\Omega}):(F \mid g r a d f)=0\right.\right.$ on $\left.\partial \Omega\right\}$.
(c) We consider $\Omega$ as in (b) and asstume that (F(x)|v(x)) $\leqslant 0$ for every $x \in \partial \Omega$. Then for every $x \in \overline{\bar{\Omega}}$ we have $\bar{t}_{x}=\infty$.
Thus $t:=\phi_{0} \mid \mathbb{R} \times \bar{\Omega}$ is a continuous semiflow on $K:=\bar{\pi}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-212.jpg?height=70&width=1617&top_left_y=1624&top_left_x=228) $t>s$ and ${ }^{\phi} \mid K_{\infty}$ is injective. For a differentiable vector field $F$ the generator of the corresponding semigroup is the closure of $A_{3}$ defined as follows: $A_{3} f:=(F \mid g r a d f), D\left(A_{3}\right):=C^{l}(\bar{\Omega})$.

We conclude the discussion of semi-flows associated with ordinary differential equations by remarking that the ideas of (b) and (c) can be combined to obtain semigroups for more general subsets $\Omega$.

We continue the discussion of the spectrum of semigroups of lattice homomoxphisms on $C(K)$ given by (4.1). Thm. 4.4 gives a good description of the part which is contained in $\{\lambda \in \mathbb{C}=\operatorname{Re} \lambda<\underline{C}(h, \phi)\}$. It is easy to see that the halfuplane $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda>\bar{c}(h, \phi)\}$ is always a subset of the resolvent set (see prop. 4.8 (a) below). The description of the remainig part $\{\lambda \in \sigma(A) ; C(h, \phi) \leqq \operatorname{Re} \lambda \leq \bar{c}(h, \phi)\}$ is more difficult. First we discuss some examples and then give a partial answer to this problem (see Prop. 4.8 (b)-(e)).

Example 4.7.(a) Consider the flow on $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ defined by $\phi(t, x):=\arctan (\tan x-t), x \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right], t \in \mathbb{R}$
(it belongs to the differential equation $y^{\prime}=-\cos ^{2} y$ ), and a continuous function $h:\left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \rightarrow \mathbb{R}$ with $h\left(-\frac{\pi}{2}\right) \leqslant h\left(\frac{\pi}{2}\right)$. Then we have $c(h, \phi)=h\left(-\frac{\pi}{2}\right)$ and $\bar{c}(h, \phi)=h\left(\frac{\pi}{2}\right)$. The spectrum of the corresponding semigroup is given by $\sigma(A)=\left\{\lambda \in \mathbb{Q}: h\left(-\frac{\pi}{2}\right) \leq \operatorname{Re} \lambda \leq h\left(\frac{\pi}{2}\right)\right\}$.
(b) Considex $\left.K=\{z \in \mathbb{C}: 1 \leq|z| \leq 2\}=f r \cdot e^{i \omega}: 山 \in \mathbb{R}, 1 \leq r \leq 2\right\}$ and a continuous function $k:[1,2] \rightarrow i{ }_{+}$.
Let $\bar{\phi}$ be the flow on $K$ governed by the differential equation ${ }_{\mu}=k(r) \quad \dot{r}=0 \quad$ (hence $\left.\bar{\phi}\left(t, r \cdot e^{i j}\right)=r^{*} e^{i(\mu+k(r) t)}\right)$.
For a continuous function $h: K \rightarrow \bar{A}$ let $h^{*}(x):=\frac{1}{2 \pi} * \int_{0}^{2 \pi} h\left(x^{*} e^{i t}\right) d t$ (1 $\leq r \leq 2$ ) . The spectrum of the semigroup corresponding to $\phi$ and h (cf. (4.1)) is given by $\sigma(A)=\left\{h^{\wedge}(x)+i k x(r): K \in \mathcal{K}, 1 \leqq r \leqq 2\right\}^{-} U\{h(z): \kappa(|z|)=0\}$.

Proposition 4.8. Suppose the semigroup ( $T(t)$ ) tzo on $C(K)$ is given by (4.1) and let $c(h, \phi), ~ c(h, \phi)$ be defined asin (4.4). Then the following assertions hold:
(a) $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda>\bar{c}(h, \phi)\} \in p(A)$;
(b) $\bar{c}(h, \phi)$ and $c(h, \phi)$ are spectral values;
(c) If $\phi\left(t, x_{0}\right)=x_{0}$ for every $t \geqq 0$, then $h\left(x_{0}\right) \in R_{0}(A)$;
(d) Assume $x_{o}$ has a finite orbit (i.e.. $\phi\left(\mathbb{R}_{+}, x_{0}\right)=\phi\left([0, T], x_{o}\right)$ for some $T<\infty)$ and $T:=\inf \left(t>0: \phi\left(T+t, x_{0}\right)=\uparrow\left(T, x_{0}\right)\right\}>0$, then $h^{\wedge}\left(x_{0}\right)+\frac{2 \pi}{\tau} i \mathbb{Z} \subset \operatorname{Ro}(A)$ where $h^{\wedge}\left(x_{0}\right):=1 / T \int_{T}^{T+\tau} h\left(\phi\left(s, x_{0}\right)\right) d s$.
(e) If $x_{0}$ has an infinite orbit and $h^{\wedge}:=1 i_{t \rightarrow \infty} h\left(\phi\left(t, x_{0}\right)\right)$ exists, then $h^{\wedge}+i \mathbb{R}$ $o(A)$.

Proof. (a) and (b): A look at (4.4) shows that $\bar{c}_{t}(h, \phi)=$ $1 / t \cdot \log \|T(t)\|$ hence $\bar{c}(h, \phi)=\omega(A) \quad(c f . A-J,(1.1))$. Consequently, we have $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda>\bar{c}(h, \phi)\} \subset \rho(A)$ and $\bar{c}(h, \phi) \in \sigma(A)$ by Thm. 1.6. To prove $\subset(h, \phi) \in o(A)$, we can assume by Thm. 4.4 that $K_{\infty}=K_{s}$ for some $s$ and that $\left.\phi\right|_{\infty}$ is injective. It is easy to see that $\mathrm{C}(\mathrm{h}, \phi)=\mathrm{c}\left({ }^{h}\left|\mathrm{~K}_{\infty}, \phi\right| \mathrm{K}_{\infty}\right)$, moreover, we have $\sigma\left(^{A} \mid I_{\infty}\right)=\phi$ hence $\sigma(\mathrm{A})=$ $\sigma\left(A / I_{\infty}\right)$ by A-III,Prop. 4.2 . This shows that we also can assume that $K=K_{\infty}$, i.e. $\phi$ is bijective or $A$ is the generator of a group. Now the assertion follows from
$\underline{C}(h, \phi)=\underline{L}\left(h, \phi^{-1}\right)=-\bar{c}\left(-h, \phi^{-1}\right)=-s(-A)$.
(c) and (d) : One can check easily that in case of (c) the Dirac functional ${ }^{\delta} x_{o}$ is an eigenvector of $A$, corresponding to $h\left(x_{0}\right)$.

A little bit more calculation is necessary to check that in case of (d) the functional $\Psi_{k}$ defined by
$\Psi_{k}(f):=\int_{T}^{T+r} \exp \left(-i \cdot \frac{2 \pi k}{T} \cdot t\right)+h_{t}\left(x_{o}\right)+i\left(\phi\left(t, x_{o}\right)\right) d t(k \in \mathcal{E}, f \in C(K))$ is an eigenvector of $A^{\prime}$ corresponding to $h^{\wedge}\left(x_{0}\right)+i \cdot \frac{2 \pi k}{7}$. (e) Given $B \in \mathbb{R}$ we will show that $h^{n}+i B \in A \sigma\left(A^{\prime}\right) E o(A)$. For $n, m \in \mathbb{N}$ we define a linear functional $\Psi_{n m}$ as follows:
$\Psi_{n m}(f):=\frac{1}{n} \cdot \int_{0}^{n} \exp \left(-\left(h^{\wedge}+i \beta\right) t\right) \cdot h_{t}\left(\phi\left(m, x_{0}\right)\right) \cdot f\left(\phi\left(m+t, x_{0}\right)\right) d t, f \in C(K)$.
For $\mathrm{f} \in \mathrm{D}(\mathrm{A})$ we have
$<\left(h^{\wedge}+i_{\beta}-A\right) f_{f} \Psi_{n}>=$
$\left.=\frac{l}{n} \cdot\left(f\left(\phi\left(m, x_{0}\right)\right)-\exp (-i \beta n) \exp ()_{m}^{m+n}\left(h\left(\phi\left(s, x_{0}\right)\right)-h \wedge\right) d s\right) f\left(\phi\left(m+n, x_{0}\right)\right)\right)$. It follows that $\phi_{n m} \in D\left(A^{\prime}\right)$ and, since $\left.\lim _{t \rightarrow \infty} h\left(\phi_{\prime_{0}}\right)\right)=h^{n}$,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-214.jpg?height=66&width=1377&top_left_y=1075&top_left_x=234)
Because the orbit is infinite we have
$$
\begin{aligned}
\left\|\Psi_{n m}\right\|_{i} & =\frac{1}{n} \cdot \int_{0}^{n}\left|e^{-\left(h^{\wedge}+i \beta\right) t} h_{t}\left(\phi\left(m, x_{o}\right)\right)\right| d t= \\
& =\frac{1}{n} \cdot \int_{0}^{n} \exp \left(\int_{m}^{m+t}\left(h\left(i\left(5, x_{o}\right)\right)-h^{n}\right) d s\right.
\end{aligned}
$$
which shows that
(4.14) $\quad \lim _{m \rightarrow \infty}\| \|_{n m} \|=1$ for every $n \in\{$.

In view of (4.13) and (4.14) it is not difficult to find a subsequence $k(n)$ of $N$ such that $\left({ }^{\psi} N, k(n)\right.$ is an approximate eigenvector of $A^{\prime}$ corresponding to $h^{\wedge}+i \beta$.

We are now going to apply the results obtained so fax to the special case where $h=0$, i.e., we consider semigroups of lattice homomorphisms which are Markov operators.

Theorem 4.9. Suppose $T$ is a semigroup of Markov lattice homomorphisms on $C(K)$ governed by the semiflow $\phi$.
(a) If ${ }^{\phi} \mid K_{\infty}$ is not injective or if $K_{t} \neq K_{m}$ for every $t<\infty$, then $\sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \leqq 0\}$.
(b) If $K_{\infty}=K_{s}$ for some $s$ and ${ }^{\phi} \mid K_{\infty}$ is injective, then $\sigma(A)$ is a cyclic closed subset of $i \mathbb{R}$. Moreover, we have o(A) $\neq \mathrm{i}$, if and only if thexe is a $T<\infty$ such that every orbit of $\phi$ has length less than $T$ (i.e., $\psi\left(R_{+}, x\right)=\phi([0, T], x)$ for every $x \in K$ ).

Proof. (a) This is an immediate consequence of Thm. 4.4 and Prop. 4.8 . (b) The first assertion follows form Thm. 4. 4 and Thm. 4.1 . Moreover, as in the proof of Thm. 4.4(b) and (c) we can assume without loss of generality that $K=K_{\text {t }}$, hence $\phi$ is bijective. If there is no upper bound for the length of the orbits, then $\sigma(A)=i \mathbb{R}$ by assertions (d) and (e) of Prop. 4, 8
Now we assume that the lengths of the orbits are bounded by $T$. Because $\phi$ is bijective, for every $x \in K$ there exists $a \quad r=r_{x}$ with $T / 2 \leqslant x \leqslant T$ such that $\phi(t, x)=\phi(t+r, x)=\phi(t+2 r, x)=\ldots=\phi(t+k r, x)\left(t \in \mathbb{R}_{+}, k \in \mathbb{N}\right)$. Therefore we have for $\lambda \in \mathbb{C}, \operatorname{Re} h>0, f \in C(K), x \in K$;
$$
\begin{align*}
& (R(\lambda, A) f)(x)=\int_{0}^{\infty} e^{-\lambda t} f(\phi(t, x)) d t=  \tag{4.15}\\
& =\sum_{k=0}^{\infty} \exp (-\lambda k r) \cdot \int_{k r}^{(k+1) x} \exp (-\lambda(t-k r) \cdot f(\phi(t-k r, x)) d t \\
& =\left(1-e^{-\lambda r}\right)^{-1} \cdot \int_{0}^{r} \exp (-\lambda t) f(\phi(t, x)) d t .
\end{align*}
$$

If $0<\beta<2 \pi / T$, then the assumption $T / 2 \leq r \leq T$ implies that there exists a neighborhood $U$ of $\lambda_{0}:=i \beta$ such that the functions $\lambda+\left(1-\exp \left(-\lambda r_{x}\right)\right)^{-1}$ are uniformly bounded on $U$, by $M$ say. Then (4.15) implies that $\|R(\lambda, A) f\| \leq M\left(\int_{0}^{r}\left|e^{-\lambda t}\right| d t\right)\|f\|_{i}$ for $\lambda \in U$, $\operatorname{Re} \lambda>0$, therefore $\lambda_{0}=i \beta \in p(A)$.

Remark 4.10. In case $\sigma(A) \neq i \mathrm{~F}$, then ${ }^{\dagger} \mid \mathrm{K}_{\infty}$ is bijective and has only finite orbits. Therefore every point $x \in K_{m}$ has a well-defined period ${ }^{\tau} x:=\inf \{i>0: \phi(\tau, x)=x\}$. A more detailed analysis yields the following description of $c(A)$ :
$(4.16) \sigma(A)=\left\{i * 2 \pi k / T_{x}: k \in \mathcal{K}, x \in K_{\infty}, \gamma_{x}>0\right\}-\cup\{0\}$.
The inclusion "드 can be derived from Thm. 4.11 which is stated below. The reverse inclusion follows from Prop.4.8(d).

In our detailed discussion of the spectrum of lattice homomorphisms we restricted ourselves to the case where the space $K$ is compact. The main reason is that there is no description as given in (4.l) of the semigroups for locally compact spaces $X$. In general, it is difficult to define a semiflow on $x$ because points may tend to infinity in a finite time. But even if one can find a flow on a suitable compactification of $C$, it may be impossible to find a multiplicator. This can be seen by studying the following example:
Suppose $\phi_{1}$ is a semiflow on a compact space $K_{1}$ and $K_{o}$ is a closed $\phi_{1}$-invariant subset, $h$ a continuous function on $K_{1}$. The
semigroup ( $\left.T_{1}(t)\right)$ on $C\left(K_{1}\right)$ corresponding to ${ }_{1}$ and $h$ leaves
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-216.jpg?height=66&width=1620&top_left_y=321&top_left_x=224) restriction a semigroup ( $T(t)$ ) on $I=C_{o}(X)$, where $x=K_{1}$ ( $K_{o}$. In this case one can construct semi-flows associated with (T(t)) on XU\{ $A$ ) or on $\bar{X}$ (closure in $K_{1}$ ), but in general one cannot find a corresponding multiplicator which is defined on one of these compactifications.

The situation is much nicer when groups of lattice homomorphisms instead of semigroups are considered. In this case there is an analogue of (4.1) (cf. B-II,Thrm.3.14) and the spectrum can be described completely. For more details and the proof of the following result we refer to Arendt-Greiner (1984).

Theorem 4.11. Suppose $X$ is a locally compact space and (T (t)) $t \in \mathbb{R}$ is a group of lattice homomorphisms governed by the flow $\phi$ and the multiplicator $h$. Then we have:
(a) $\quad \sigma(A)=\sigma_{1} \mathrm{Va}_{2} \mathrm{Vo} \sigma_{3}$ where the sets $\sigma_{i}$ are defined as follows $\sigma_{1}:=\left\{h^{\wedge}(x)+i \cdot 2 \pi k / \tau_{x}: x \in X, 0<\tau_{x}<\infty\right\}$, $\sigma_{2}:=\left\{h(x): x \in X, \tau_{x}=0\right\} \square \sigma_{3}:=\{\lambda \in \mathbb{C}: \lambda+i \mathbb{R} \subseteq \sigma(A)\}$
(b) $\quad o(T(t))=\exp (t \sigma(A))$ for every $t \geq 0$.
(c) Every isolated point of $\sigma(A)$ is a first order pole of the resolvent.

WOTES.
Spectral theory for a single positive operator is an essential cornerstone for spectral theory of positive one-parameter semigroups. Many of the results we have presented $\mathrm{In}_{\mathrm{n}}$ this chapter have analogues in the discrete case (i.e. for a single operator). This relation may serve as a gutde. However, only in few cases can the continuous version be deduced directly fron fts discrete analogue. Therefore we will not try to trace back the roots of every result to the discrete version, Instead we refer to Schaefer (1974) and the notes and references given there.
Many of the results we have presented in this chapter can be extended (more or less easily) to the more general setting of Eanach lattices, which include the very important examples of $L^{\text {p }}$-spaces. Others are typical for $C(X)$ and allow no extension. We will discuss this fact in more detail in Chapter C-III. The more general setting considered there also allows us to prove results for $C$ ( $X$ ) which we could not obtain staying within the franework of spaces of continuous $\frac{9}{1}$ unctions.

Section 1. Theorem l.l was stated by Karlin (1959), but a complete proof is given in Derndinger (1980). Propositon 1.5 is taken from Greiner (1982) and Theorem 1.6 is (implicitely) contained in Derndinger-Nagel (1979). A generalization to (nonlattice) ordered Eanach spaces can be found in Sec. 2.4 of Eatty-Robinson (1984).

Section 2, Lemma 2.3 dates back to Rota (see Schaefer (19743). Our approach follows Greiner (1981). The notion ' (imaginary) additively cyclic' was introduced by berndinger (1980) (and Schaefer (1980) respectively). Derndinger proves some fyclicity results for the boundary spectrum. A result simylar to Proposition 2.7 is given in Sec. 7.4 of Davies (1980). Lemma 2.8 in conbination with C-III, Lemma 3.13 can be used to characterize semigroups whose spectral bound is a pole of finite algebraic multiplicity (see C-III, (3.19) . The hypothesis of Theorem 2.9 can be weakened, one only needs that $s(A)$ is a pole of the resolvent (see C-III, Cor.2.12). Further results on the cyclicity of the boundary spectrum will be given in Chapter C-III. In particular we refer to $\mathrm{C}-\mathrm{III}$, Thms.2.10, 3.11 and 3.13 . The dichotomy stated in (2.19) is probably the most interesting consequence of cyclicity results. It has far reaching consequences on the asymptotic behavior of positive semigroups. Example 2.13 is due to Davies (unpublished note). Example 2.14 (b) will be discussed in more detail and more generality in Section 3 of Chapter E-IV. We return to Remark 2.15(b) in Section 2 of $\mathrm{B}-\mathrm{IV}$.

Section 3. The concept of irreducibility as defined in 3.1 is closely related to various other notions: In topological dynamics flows inducing irreducible semigroups are called 'minimal flows' (cf. Example 3,4(a)). Moreover, 'ergodicity' and 'undque ergodicity' are closely related to irreducibllity (see CornfeldwFominusinai (1982) or Krengel (19853). Irreducible semigroups are discussed to some extent ín Davies (1980). E.g. he proves a special case of Theorem 3.6. Froposition 3.3 will be generalized in C-III, Prop+3.3. Assertion (a) of Proposition 3.5 was proven by Schaefer (1983) while Theorem 3.6 is taken from Greiner (1982). Elliptic operators (more general than Example 3.10(b)) as generators on spaces of continuous functions, were investigated by wany people, e.g. Eony-Courrège-Priouret (1968), Kuhn (1985), Roth (1976) 4(1978) and Stewart (1974).

Section 4. Theorem 4.1 is due to Derndinger (1984.). The spectrum of semigroups of Markov lattice homomorphisms is investigated by Derndingerwigal (1979). In partiw cular they prove Theorem 4.4 for Markov semigroups. Earlier results are due to Scarpellini (1974). We indicated briefly in Example 4.6 that there is a relationw ship between spectral propetties of lattice semigroups and differentiable dynamics. For more details we refer to Chicone-Swanson (i981) and Sackerwsell (1978). E.g., the 'annular hull theorem' is a special case of Theorem 4.11 (b). The general result 4.11 was proven by Arendt-Greiner (1984).

ASYMPTOTICS OF

POSITIVE SFMIGROUPS ON CO(X)

In the following chapter we will examine the asymptotic behavior of positive semigroups on spaces of continuous functions.
The first section is devoted to the various "growth constants" defined in Chapter $A-I V$ and to their coincidence for positive semigroups.
In the second section we treat the asymptotic behavior of positive semigroups which do not differ "too much" from compact semigroups. Properties such as eventual compactness or quasi-compactness allow to describe the long term behavior of the semigroup by using the results from $A-I I I$ and $B w I I$ on the spectrum of the generator.
In the last section we investigate differential delay equations by semigroup methods. In particular, we characterize the spectral bound of the solution semigroups thereby finding simple conditions for stability. Numerous examples conclude the chapter.
1. STABILITY OF POSITIVE SEMIGROUPS ON C $(X)$
by Frank Neubrander

In Chapter $A-I V$ we have seen that the long term behavior of a semiw group (T(t)) $t \geqq 0$ is strongly connected with the existence (and growth) of the resolvent of the generator $A$ in a right halfplane. In particular, the exponential growth of certain semigroups is determined solely by the location of the spectrum (see $A w I V,(1,7)$ and (1.8)). In these cases spectral bound $s(A)$ and growth bound w(A) coincide and the equality
$$
\begin{equation*}
E(A)=\omega_{1}(A)=u(A) \tag{1.1}
\end{equation*}
$$
holds.

Unfortunately, (1.1) does not hold for positive semigroups in general. In A-IV, Example $1.2(2)$, we have seen that $\begin{aligned} & \text { Eor the generator } A \text { of the }\end{aligned}$ (positive) translation semigroup on the Banach lattice $C_{o}\left(R_{+}\right) \cap L^{l}\left(\mathbb{R}_{+}, o^{x} d x\right)$ the strict inequalitiy $\omega_{I}(A)<\omega_{\mu}(A)$ ig valid. For positive semigroups on certain nice Banach lattices (l.l) is true. One of these nice Banach lattices is $C_{0}(x)$. This will be proved in Theorem 1.4.

For compact $X,(1,1)$ was already proved in B-II, Cor.l.14 and B-III, Thm. 1.6 respectively. Actually much more is true and for positive semigroups on $C(K), K$ compact, all stability concepts mentioned in chapter $A-I V$ are mutually equivalent.

Theorem 1.1 . Let $A$ be the generator of a positive semigroup $(T(t))_{t \geqslant 0}$ on $C(K), K$ compact. Then
(1.2) $s(A)=\inf \{\lambda \in \mathbb{R}: A f \leq \lambda f$ for some $0<\in \in D(A)\}$

Moreover, $\quad s(A)=w(A) \in \operatorname{Ro}(A)=P \sigma\left(A^{\prime}\right)$ and the following statements are mutually equivalent:
(i) $s(A)<0$.
(ii) (T(t)) $t \geq 0$ is uniformly exponentially stable,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-220.jpg?height=56&width=1440&top_left_y=1571&top_left_x=222) for every $\ddagger \in D(A)$ and every $\mu \in C(X)^{\prime}$.

Proof. (1.2) follows directly from $A w I I, 4.4$ and the results from B-II and B-III mentioned above. It remains to show the implication (iii) $\rightarrow$ (i).

If $\in T(t) f, \mu>\rightarrow 0$ for every $\mu \in C(K)$, then, by the Uniform Boundw edness Principle, $\|T(t) f\| \quad \leq \quad M_{f}$ for every $f \in D(A) \quad$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-220.jpg?height=56&width=1620&top_left_y=2028&top_left_x=207) that $s(A) \leq 0$. Suppose $0=s(A)$. From $B-I I I, T h m .1 .6$ it follows that $g(A) \in P \sigma(A ')$, hence there is $0<\mu \in C(K)^{\prime}$ such that $T(t)^{\prime} \mu$ $=\mu$ for $t \geq 0$. Since $D(A)$ is dense, there exists $f \in D(A)$ such that $\langle f, \mu\rangle \neq 0$. Then $|\langle T(t) f, \mu\rangle|=|\langle f, \mu\rangle|\rangle 0$ which contradicts the weak stability. Therefore $s(A)<0$.

For spaces $C_{o}(X), X$ locally compact, the different stability concepts are no longer equivalent.

Examples 1.2 . (a) The left-translation semigroup on $C_{0}(\mathbb{R} f)$ or the semigroup generated by the Laplacian on $C_{o}{\left(\mathbb{R}^{n}\right), ~ s e e ~ B-I I I, E x .1 .7, ~}_{\text {, }}$, are uniformly stable but not exponentially stable.
(b) The left translations $T(t) f(x)=f(x+t)$ on $C_{o}(\mathbb{R})$ form a group of isometries. Hence (T(t)) $t \geq 0$ is not stable. However, (T(t)) $t \geqq 0$ is weakly stable. Indeed, identifying $C_{o}(\mathbb{R})^{\prime \prime}$ with the space of all bounded Borel measures on $R$, for $f \in C_{o}(\mathbb{R}), \mu \in C_{o}(R){ }^{*}$ we have
$$
\left\langle T(t) f_{f} \mu\right\rangle=\left\{\left(T(t) \frac{z}{2}\right)(x) d_{\mu}(x)\right.
$$

Obviously, $T(t) f$ tends pointwise to 0 as $t \rightarrow \infty$ and is dominated by the $\quad$-integrable function $\|f\|_{\text {n }} 1$. Thus Lebesgue's Dominated Convergence Theorem implios lim $\langle T(t) f, u\rangle=0$.
(c) Finally we give an example of a positive semigroup on $C_{0}(X)$ which is not weakly stable but satisfies Re(Po(A) $U \operatorname{Ro}(A))<0$. (Compare with A-IV,Cor.1.14).
Consider in the space Ch\{0\} a flow $\phi$ having the following properties:
- The orbits starting at $z$ with $\mid z!\neq 1$ spiral towards the unit circle $\Gamma$;
- 1 is a fixed point and $\Gamma$ ( $\{1\}$ is a homoclinic orbit (i.e. $\lim _{t \rightarrow+\infty} \phi(t, z)=1 i_{t+\infty} \phi(t, z)=1$ for every $z \in \Gamma$ ).

A concrete example of this type is tho flow governed by the following differential equations for the polar coordinates (i.e. $z=r \cdot e^{i \omega i}$ )
$$
\begin{aligned}
& \dot{I}=1-r \\
& \dot{\omega}=1+\left(r^{2}-2 r \cdot \cos \dot{\omega}\right)
\end{aligned}
$$

The locally compact set $X:=\{z \in \mathbb{C}: 0<|z|<2, z \neq 1\}$ is invariant under the flow $\phi$ and we consider on the space $C_{o}(X)$ the semigroup (T(t)) $t \geq 0$ associated with $\phi \quad$ (i.e. $T(t) f=f o \phi_{t}$, $f \in C_{o}(X)$. We claim that
(i) (T(t)) $t \geq 0$ is not weakly uniformly stable ;
(ii) $\quad P \sigma(A) \cap i \mathbb{R}=\emptyset$;
(iii) Ro(A) Ri $=\varnothing$.

Proof of (i): Given $z \in X,!z ; \neq 1$, there exist sequences $\left(t_{n}\right)$, $\left(s_{n}\right)$ both tending to $\infty$ such that $\phi\left(t_{n}, z\right)+1$ and $\phi\left(s_{n}, z\right)$ * -1 . Hence for $f \in C_{o}(X)$ we have
$\left\langle T\left(t_{n}\right) f, \delta_{z}=f\left(\phi\left(t_{n}, z\right)\right)+0\right.$,
$<T\left(s_{n}\right) f_{f} \delta_{z}>=f\left(\phi\left(s_{n}, z\right)\right) \rightarrow f(-1)$.
Thus $\lim _{t \rightarrow \infty}\left\langle T(t) f_{i} \delta_{z}\right.$ does not exist for every $f \in C_{o}(X)$. Proof of (ii) : Assume that $T(t) f=e^{i a t} f$ for every $t i o n a n d ~ s o m e$ $\alpha \in \mathbb{R}$ (cf. A-III, Cor. 6.4 ). Given $z \in X$, there exists a sequence $\left(t_{n}\right)$ such that $\phi\left(t_{n}, z\right) \rightarrow 1$, hence
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-222.jpg?height=87&width=1408&top_left_y=256&top_left_x=207)
Proof of (iii): At first we point out that for $f \in C_{0}(x)$ such that $f$ vanishes on the unit circle $\Gamma$, we have $\lim _{t \rightarrow \infty}\|T(t) f\|=0$.
Assume that $\mu$ is a bounded Borel measure such that $T(t){ }^{\prime} \mu=e^{i a t}{ }_{\mu}$ for every $t \geqslant 0$ and some $a \in \mathbb{R}$. Then $\langle f, \mu\rangle=e^{i \alpha t}\left\langle f, T(t)^{r} \mu\right\rangle=$ $=e^{i \alpha t^{*}}\langle T(t) f, \mu\rangle+0$ for every $f \in C_{o}(X)$ with $f_{!}=0$. It follows that the support of $u$ is contained in $\Gamma$. Since $\lim _{t w \infty}(t, z)=1$ for every $z \in \Gamma$, we obtain for arbitrary $f \in C_{o}(X)$ :
(T(t)f) (z) * 0 -a.e.. Lebesgue's Dominated Convergence Theorem implies $\langle f, \mu\rangle=e^{-i \alpha t}\langle T(t) f, \mu\rangle \rightarrow 0$ as $t *$ for every $f \in C_{o}(X)$. Thus $\mu=0$.

Now we are going to prove the main result of this section. At first we note that the positive part of the domain of the adjoint operator is sufficiently large. In fact, we know that $\lambda R(\lambda, A) \rightarrow I d$ strongly as $\lambda \rightarrow \infty$. It follows that $\lambda^{2} R(\lambda, A)^{2}$ tid strongly, hence $\lambda^{2} R(\lambda, A)^{\prime 2}$. Id with respect to $\sigma(E \prime, E)$-topology. If $A$ generates a positive semigroup then $\lambda^{2} R(\lambda, A)^{2} \mu \in D\left(A^{*}\right):=D\left(A^{*}\right) \cap E_{+}^{*}$ for
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-222.jpg?height=86&width=1160&top_left_y=1322&top_left_x=208) $\left.R(\lambda, A){ }^{2} E^{\prime} \subset R(\lambda, A) \quad E^{*}=D\left(A^{*}\right).\right)$
We sumarize these observations in the following lemma.

Lemma 1.3. Let $A$ be the generator of a positive semigroup on a Banach lattice $E$. Then every $\mu \in E^{\prime}$ is the $\sigma\left(E^{\prime}, E\right)-l i m i t$ of elew ments in $D\left(A^{*}\right)_{+}$; i.e., $\overline{D\left(A^{*}\right)_{+}}\left(E^{\prime}, E^{\prime}\right)=E_{+}^{\prime}$.

Theorem 1.4 Let $A$ be the generator of a positive semigroup on $C_{0}(X)$. Then
$$
s(A)=w_{1}(A)=\omega(A) \in \sigma(A)
$$

Proof. Rescaling the semigroup we may assume w(A) $=0$. (In case $\omega(A)=-\infty$, then $\sigma(A)=\emptyset$ hence $s(A)=-\infty)$
Suppose $0 \& \sigma(A)=\sigma\left(A^{*}\right)$. Then, by the holomorphy of the resolvent and by $A-I I, P r o p .1 .11$
$R\left(0, A^{*}\right) \Phi=\sum_{n=0}^{\infty} R\left(1, A^{*}\right)^{n+1} \Phi=\sum_{n=0}^{\infty} \int_{0}^{\infty} \frac{1}{n!} t^{n} e^{-t} T(t) * \phi d t$ for every $\phi \in C_{0}(X)^{*}$ - If $0 \leqslant \Phi \in C_{0}(X)^{*}$ and $0 \leqq \rho \in C_{0}(X)$ " we can interchange integration and summation by the Monotone convergence Theorem; i.e.
$$
\begin{align*}
\left\langle R\left(0, A^{*}\right) \varphi, \rho\right\rangle & =\sum_{n=0}^{\infty} \int_{0}^{\infty} \frac{1}{\Pi!} t^{n} e^{-t}\langle T(t) * \varphi, \rho\rangle d t \\
& =\int_{0}^{\infty}\langle T(t) * \Phi, \rho\rangle d t . \tag{1.3}
\end{align*}
$$
since every element of $C_{0}(x)^{*}$ and $C_{0}(X)$ " is the difference of posi-
tive elements the equation (1.3) holds for every $\Phi \in C_{o}(X) *$, $p \in C_{0}(X)^{\prime \prime}$. This means that the net $\left(\int_{0}^{r} T(t) * \Phi d t\right)_{r>0}$ converges weakly to $\mathrm{R}\left(0, \mathrm{~A}^{*}\right)$. But for positive $\Phi$ the net is monotone and therefore strongly convergent by Dini's Theorem (see Schaefer (1974), II.Thr.5.9). Hence $R\left(0, A^{*}\right) \Phi=\int_{0}^{\infty} T(t) * \Phi d t$ for every $\$ \in C_{0}(X)^{*}$. Now we make use of the special character of the space $C_{0}(X)$. For positive functions $\mathrm{F}_{1}, \mathrm{E}_{2} \in \mathrm{C}_{0}(\mathrm{X})$ we have sup $\left(\left\|\mathrm{f}_{1}\right\|,\left\|\mathrm{f}_{2}\right\|\right)=$ $\left\|\sup \left(f_{1}, f_{2}\right)\right\|$. Let $\mu_{1}, \mu_{2} \in C_{0}(X){ }_{+}$and $\varepsilon>0$. Then there are positive elements $f, g$ in the unit ball of $C_{o}(X)$ such that $\langle f, \mu\rangle \geq\|\mu\|-t$ and $\left\langle g, \mu_{2}\right\rangle \geq\left\|\mu_{2}\right\|-\varepsilon$. For $h:=\sup (f, g)$ we obtain $\|h\| \leq 1$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-223.jpg?height=72&width=1426&top_left_y=889&top_left_x=224)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-223.jpg?height=87&width=1617&top_left_y=939&top_left_x=222) Approximating the integral by Riemann sums one obtains $\left\|\int_{0}^{r} T(t) * \mu d t\right\|=\int_{0}^{r}\|T(t) * \mu\| \quad d t$ for $\mu \in C_{0}(X) *, r>0$ and therefore, for $r * \infty,\left\|R\left(0, A^{*}\right) \mu\right\|=\left\|\int_{0}^{\infty} T(t) * \mu d t\right\|=\int_{0}^{\infty}\|T(t) * \mu\| t$ $\left(\mu \in C_{o}(X) *\right)$, Given $\mu \in C_{0}(X)^{\prime}$ there is a sequence $\mu_{n} \in C_{0}(X){ }_{+}^{*}$ converging $\sigma\left(E^{\prime}, E\right)$ to $\mid \mu$ ! (Lemma 1.3 ). From $\mid\left\langle f, T(t){ }^{\prime} \mu>\right| \leqq$ $\langle T(t)| f|,!\mu|\rangle=\lim _{n^{+\infty}}\left\langle T(t)!f \mid, \mu_{n}\right\rangle$ we conclude $\left|\left\langle f, T(t){ }^{\prime} \mu\right\rangle\right| \leqq$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-223.jpg?height=72&width=1614&top_left_y=1352&top_left_x=227) ( $\mathrm{t} \boldsymbol{3}$ 0). Applying Fatou's Lemma we obtain
$\int_{0}^{\infty}\|T(t) ' u\| d t \leq \int_{0}^{\infty}(1 \operatorname{iminf}\|T(t) ' \mu\|) d t \leqq$
$\liminf \int_{0}^{\infty}\left\|T(t){ }^{\prime} \mu\right\| d t=\liminf \left\|R\left(0, A^{*}\right) \mu_{n}\right\| s\left\|R\left(0, A^{*}\right)\right\| \cdot \liminf \left\|\mu_{n}\right\|<\infty$. (observe that $t *\|T(t) \cdot \mu\|=\sup \{\langle T(t) f, \mu>:\|f\| \leq 1\}$ is lower semi-continuous and hence measurable). Using A-IV,Thm.1.10 we obtain $\omega\left(A^{*}\right)<0$. But $\omega(A)=\omega\left(A^{*}\right)$ by A-III,A.4(iii), which contradicts $w(A)=0$.

Remark 1.5. If (T(t)) is a positive semigroup on an a-directed ordered Banach space E (see Asimow-Ellis (1980),p.39), then the dual of $E$ admits a reversion of the triangle inequality;
i.e. $\quad \sum l_{i}\left\|_{i} \leqq a\right\| \sum_{i} \|$ for $u_{i} \in E_{+}^{\prime}$, and Theorem 1,4 remains valid (see Batty-Davies (1983)). The proof given above may be used with almost no modification.

At this point we close the discussion of the stability of positive semigroups on $C_{o}(X)$ and refer to section $l$ of $C-I V$ and $D-I V$ respectively, where the stability of positive semigroups on arbitrary Banach lattices and on $C^{*}$-algebras will be treated.

\section*{2. COMPACT AND QUASI-COMPACT SEMIGROUPS}
by
Gunther Greiner

Using the Riesz-Schauder Theory for compact operators (see e.g. Chapter VII. 4 of Dunford-Schwartz (1958) or Section 26 of Pietsch (2978) and the results of Chapter $A-I I I$, one can easily describe the asymptotic behavior of eventually compact semigroups. Since no positivity is involved we state the fundamental result for arbitrary Banach spaces.

Theorem 2.1. Let (T(t)) tep be a strongly continuous semigroup on a Banach space $G$ which is eventually compact (i.e., there is $t_{o}>0$ such that $T\left(t_{o}\right)$ is a compact operator). Then the spectrum of the generator $A$ is a countable set (possibly finite or empty) and contains only poles of finite algebraic multiplicity. Furthermore, the set $\{\mu \in \sigma(A): \operatorname{Re} \mu \geqq r\}$ is finite for every $r \in \mathbb{R}$. Thus $\sigma(A)=\left\{\lambda_{1}, \lambda_{2}, \lambda_{3}, \ldots\right\}$ with $\operatorname{Re} \lambda_{n+1} \leq \operatorname{Re}_{n}$ for all $n \in \mathbb{N}$ and $\lim _{n \rightarrow \infty} \operatorname{Re} \lambda_{n}=-\infty$ if o(A) is infinite. Denoting the pole order at $\lambda_{n}$ by $k(n)$ and the corresponding residue by $P_{n}$, we have for every $m \in \mathbb{N}$
$$
\begin{align*}
& T(t)=T_{1}(t)+T_{2}(t)+\ldots+T_{m}(t)+R_{m}(t) \text {, where } \\
& T_{n}(t)=\exp \left(\lambda_{n} t\right) \cdot \sum_{j=0}^{k(n)-1} \frac{l}{j!} \cdot t^{j}\left(A-\lambda_{n}\right)^{j}{ }_{0} P_{n} \quad(t \geq 0),  \tag{2.1}\\
& \left\|R_{m}(t)\right\| \leq C \cdot \exp \left(\left(\varepsilon+\operatorname{Re} \lambda_{m}\right) t\right) \text { for } t \geqq 0, \varepsilon>0 \text { and a suitable } \\
& \text { constant } C=C(\varepsilon, m) .
\end{align*}
$$

Proof. Fix $r \in \mathbb{R}$. By the Riesz-Schauder Theory we know that $\left\{z \in \sigma\left(T\left(t_{0}\right)\right) ;|z| z \exp \left(r t_{0}\right)\right\}$ is a finite set and contains only poles of finite algebraic multiplicity. Thus the first assertion follows from A-III,Cor.6.5.

To prove the remaining assertion we fix $m \in \mathbb{N}$ and apply the spectral decomposition as described in section 3 of Chapter A-III. For simplicity we assume Re $\lambda_{m+1} \leqslant \operatorname{Re} \lambda_{m}$. Let $P$ be the spectral projection $0: T\left(t_{0}\right)$ corresponding to the spectral set $\left\{z \in \sigma\left(T\left(t_{0}\right)\right)\right.$ : $\left.|z| \geqq \exp \left(\operatorname{Re}_{\mathrm{m}} \cdot \mathrm{t}_{0}\right)\right\}$. Then P reduces the semigroup and we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-224.jpg?height=61&width=1608&top_left_y=2545&top_left_x=224) ( $\Gamma$ ( $t_{o}^{\prime}$ |ker $p$ ) is less than Re $h_{m}$. Then there exists a constant $C_{o}$ such that
$\|T(t)(I d-P)\| \leqq\|T(t) \mid \operatorname{ker} P\| \cdot\|I d-P\| \leqq\|I d-P\| \cdot C_{G} \cdot \exp \left(\operatorname{Re} \lambda_{\mathrm{m}} \cdot t\right) \cdot$
We define $\mathrm{R}_{\mathrm{m}}(\mathrm{t}):=\mathrm{T}(\mathrm{t})(\mathrm{I} \mathrm{d}-\mathrm{P}), \quad \mathrm{T}_{\mathrm{n}}(\mathrm{t}):=\mathrm{T}(\mathrm{t}) \mathrm{P}_{\mathrm{n}}(\mathrm{n} \in \mathbb{N})$.
Then $R_{m}(t)$ satisfies the estimate stated in (2.1) and we have $T(t)=$ $\sum_{n=1}^{m} T_{n}(t)+R_{m}(t)$ because $P=\sum_{n=1} P_{n}$ by A-III, Cor.6.S(ii) - The family of projections $I d-P, P_{1}, P_{2}, \cdots, P_{m}$ reduces the semigroup. Thus in order to prove the representation of $T_{n}(t)$ stated in (2.1) we only have to combieter elements f $\in P_{n} E=\operatorname{ker}\left(\lambda_{n}-A\right)$. That is we can assume $E=P_{n} E, \sigma(A)=\left\{h_{n}\right\}, P_{n}=I d$ and for simplification we drop the index $n, i . e ., \lambda=\lambda, k=k(n)$. Then $A$ is a bounded operator satisfying $(h-A)^{k}=0$ and its resolvent is given by $R(\mu, A)=(\mu-\lambda)^{-1} \sum_{j=0}^{k-1}(\mu-\lambda)^{-j}(A-\lambda)^{j}$ for $\mu \neq \lambda$. It follows that $R(\mu, A)^{i}=(\mu-\lambda)^{-i} \sum_{j=0}^{k-1}\binom{\dot{j}+i-1}{i-1}(\mu-\lambda)^{-j}(A-\lambda)^{j}$. Hence we have $\left(\frac{i}{t} R\left(\frac{i}{t}, A\right)\right)^{i}=\left(1-\lambda \frac{t}{i}\right)^{-i} \sum_{j=0}^{k-1}\binom{j+i-1}{i-1}(i-\lambda t)^{-j_{t}}{ }^{j}(A-\lambda)^{j}$ for every $i \in \mathbb{N}$. Since $\lim _{i \rightarrow \infty}\left(1 \sim \frac{t}{i}\right)^{-i}=e^{\lambda t}$ and $\lim _{i \rightarrow \infty}\binom{j+i-1}{i-1}(i-\lambda t)^{-j}=\frac{1}{j!}$ for every $j \in \mathbb{N}$ the assertion follows from formula $A-I I,(1.3)$.

Combining Thm.2.l with the results of Chapter B-III one can describe the behavior of $T(t)$ as $t * m$ provided that (T(t)) $t \geq 0$ is a positive semigroup. We give a typical example.

Corollary 2.2. Let (T(t)) ${ }_{t \geqslant 0}$ be a positive semigroup on a space $C_{o}(X)$ which is irreducible and eventually compact. Then there exist a unique real number $r \in \mathbb{R}$, a strictly positive function $h$ and a strictly positive bounded Borel measure $v$ such that for suitable constants $\delta>0, M \geqq 1$ one has
(2.2) $\|\exp (-r t) \cdot T(t)-v o h\| \leq M \cdot e^{-\delta t}$ for all $t$ ह 0 .

In particular, for every $f \in C_{o}(X)$ and $t \& 0$ one has
(2.3) $\quad e^{r t}\left(\left|\int f d v\right|-M \cdot e^{-\delta t}\|f\|\right) \leq\|T(t) f\| \leq e^{r t}\left(\|f d v\|+M+e^{-\delta t}\|f\|\right)$.

Proof. We take $I:=s(A)$. By B-III,Prop. 3.5(a) we have $r>-\infty$.
Moreover, by assertion (e) of the same proposition we know that $r$ is an algebraically simple pole and the corresponding residue $p$ has the form $P=u$ for for strictly positive eigenvectors $u$ and $h$ of $A$ and A', respectively. Without loss of generality we may assume $\|h\|=1$. Corollary 2.11 of Chapter $B$-III implies that $r$ is strictly dominant, i.e., enumerating the eigenvalues as described in Thm. 2.1 we have Re $\lambda_{2}<\lambda_{1}=r$. Now (2.2) follows from (2.1) for $m=1$.

Applying the triangle inequality to $\quad T(t) f=e^{r t}\left(P f+\left(e^{-r t} T(t) f-P f\right)\right)$ and using (2.2) one easily deduces (2.3).

Let us point out the following consequence of Corollary 2.2 :
For every positive, non-zero initial value $f$ the solution $T()$. of the abstract Cauchy problem $\dot{u}=A u$ decreases or increases exponentially in norm according to the sign of $r=s(A)$.
If $s(A)=0$ then $T()$.$f tends to an equilibriurn state which is$ unique up to a constant and non-zero whenever the initial value is positive and non-zero.

In order to apply Thru. 2.l and its corollary to concrete problems one needs conditions which ensure that the semigroup is eventually compact. We discuss this problem for the spaces $C(K), K$ compact, in more detail. The crucial tool is the following characterization of weakly compact subsets in the dual space $M(K)=C(K)$ ' due to Grothendieck (1953).

Proposition 2.3. Let $K$ be a compact space. For a subset $M \subset M(K)=$ $C(K)^{\prime}$ the following assertions are equivalent:
(i) $M$ is relatively compact for the weak topology $o(M(K), M(K) '$ ) ;
(ij) for each weak null sequence ( $\mathrm{f}_{\mathrm{n}}$ ) in $\mathrm{C}(\mathrm{K})$, $\lim _{n+\infty}\left\langle\mathrm{f}_{\mathrm{n}}, v\right\rangle=0$ uniformly for $u \in M$;
(iii) Eor each sequence (U) of disjoint open subsets of $K$,
$\lim _{n \rightarrow \infty} v\left(U_{n}\right)=0$ uniformly for $v$ in $M$.

For a proof of this result see e.g. II.9.8 in Schaefer (1974). We use this proposition in order to describe weakly compact operators on spaces $C(K)$. As usual we identify in the natural way the bounded Borel functions on $K$ with a subspace $B(K)$ of $M(K)^{\prime}=C(K)^{\prime \prime}$; in
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-226.jpg?height=61&width=723&top_left_y=2123&top_left_x=204)

Proposition 2.4. Let $K$ be a compact space, $G$ be a Banach space and let $R: C(K) \rightarrow G$ be a bounded linear operator.
(a) The following assertions are equivalent :
(i) R is weakly compact;
(ii) for every bounded Borel function $g$ on $K$ we have $k$ "g $G$;
(iii) for every Borel set $C \in K$ we have $R^{\prime \prime}\left(x_{c}\right) \in G$.

In case $G=C(K)$ these conditions are equivalent to the following:
(iv) if $\left(f_{n}\right)=C(K)$ is a boundeg sequence then (Rfn) has a subseguence which converges pointwise to a continuous function.
(b) If R is weakly compact then it maps weakly convergent sequonces into norm convergent sequences. In particular, the square of a weakly compact operator $T: C(K) * C(K)$ is a compact operator.

Proof.(a) (i) (ii) follows from the following characterization of weakly compact operators (see e.g., II. Prop.9.4 of Schaefer (1974)):

An operator is weakly compact if and only if its second adjoint maps the bidual into the original space.
(ii) $\rightarrow$ (iii) is trivial and it remains to show that (iii) implies (i): On the Borel field $B$ we define $m$ by $m(C):=R^{\prime \prime}\left(x_{C}\right)$. Then $m$ is a G-valued additive set function. For $y^{\prime} \in G^{\prime}$ we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-227.jpg?height=46&width=1617&top_left_y=1162&top_left_x=228) additive set function, i.e., m is weakly countably additive. By Pettis" Theorem (see IV.Thm. 10.1 in Dunford-Schwartz (1958)) we have that $m$ is countably additive with respect to the norm. In particular, for a sequence $t n$ of mutually disjoint Borel sets we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-227.jpg?height=67&width=1617&top_left_y=1440&top_left_x=228) $y^{\prime \prime} \in G^{\prime},\left\|y^{\prime}\right\| \leq 1$. Now condition (iii) of Prop. 2.3 shows that ( $\mathrm{R}^{\prime} \mathrm{y}^{\prime}$ : $\left.y^{\prime} \in G^{\prime},\left\|Y^{\prime}\right\| \leqq I\right\}$ is rolatively weakly compact. i.e., $R^{\prime}$ is weakly compact. Thus $R$ is weakly compact as well.
In case $G=C(K)$ the equivalence of (i) and (iv) is a consequence of two results: First, Eberlein's Theorem states that for the weak topology in any Banach space compactness and sequential compactness are equivalent, Second, Lebesgue's Dominated Convergence Theorem assures that a sequence $\left(f_{n}\right)=C(K)$ converges weakly to $f \in C(K)$ if and only if it is bounded and $f_{n}(x)+f(x)$ for every $x \in K$.
(b) Suppose $\left(f_{n}\right)$ is a sequence in $C(K)$ which converges to 0 for the weak topology. Since $R$ is weakly compact the same is true for the adjoint $R^{\prime}, ~ i . e ., ~\left\{R^{\prime} Y^{\prime}=Y^{\prime} \in G^{\prime},\left\|^{\prime}\right\|_{i} \leqq l\right\}$ is relatively weakly compact in $M(K)$. From Prop. 2. 3 (i) (ii) we obtain that $\left\langle\mathrm{Rf}_{n}, \mathrm{Y}^{\prime}\right\rangle=\left\langle\mathrm{f}_{n^{\prime}} \mathrm{R}^{\prime} \mathrm{y}^{\prime}\right\rangle \rightarrow 0$ as $\mathrm{n} * \infty$ uniformly for $y^{\prime} \in G^{\prime},\left\|^{\prime}\right\|_{i} \leqslant l$. That is $\lim _{n^{+\infty}}\left\|\mathrm{Rf}_{\mathrm{n}}\right\|=0$.
The final assertion follows from the first and the characterimation of weakly compact operators stated in (iv) of (a).

The next result which is an inthediate consequence of Thm. 2.1 and Prop.2.4 is motivated by the theory of Markov processes. For a Markov operator (see B-I,sec.3) condition (ii) of Prop. $2.4(a)$ is called the strong Feller property .

Theorem 2.5. Let (T(t)) tro be semigroup of Markov operators on $C(K), K$ compact, such that one operator $T\left(t_{0}\right)$ has the strong Feller property. Then there exists a positive projection $P$ of finite rank such that $\|T(t)-P\| \leqq M \cdot e^{-\delta t}$ for suitable constants $\delta>0, M \geqq 1$.

Proof, By Prop.2.4(a) T(t.) is weakly compact. Thus by Prop, 2,4(b) $T\left(2 t_{0}\right)$ is compact, i.e., $(T(t)) t_{t} \geqslant 0$ is eventually compact. Moreover, by B-III, Cor.2.ll $s(A)=0$ is strictly dominant and a first order pole of the resolvent by B-II, Rem,2.l5(a). The assertion now follows easily from Thm. 2.1.

We close the discussion of eventually compact semigroups by describing a situation where Thm. 2.5 can be applied. A more detailed description of the relation between Markov processes and positive semigroups on $C(K)$ is given in Chap. 2 of van Casteren (1985).

Example 2.6. Let $K$ be a compact space and $\left\{P_{t}: t>0\right\}$ be a Markov transition function on $K$ which satisfies the strong Feller property and which is stochastically continuous. That is, every $P_{t}$ is a real-valued function defined on the product $K \times B$ where $B$ denotes the Borel field on $K$, such that
(a) for $x \in K$ and $t>0$ fixed, $P_{t}(x,$.$) is probability measure;$ (b) for $C \in B$ and $t>0$ fixed, $P_{t}(., C)$ is a continuous function; (c) $P_{t+s}(x, C)=\int_{K} P_{s}(y, C) P_{t}(x, d y)$ for all $s, t>0, x \in K, C \in B$; (d) $\quad l^{i m} t+0 P_{t}(x, U)=1$ for every open set $u$ containing $x$.

Condition (b) is the strong Feller property, (c) is the ChapmanKolmogorov equation and (d) expresses stochastic continuity. Given $\left\{P_{t}\right\}$ as above one defines for $f \in C(K), x \in K$ and $t>0$
(2.4) (T(t)f)(x):= $\int_{K} f(y) P_{t}(x, d y)$.

Then it is not difficult to verify that $T(t) f \in C(K)$, that $T(t)$ is a Markov operator on $C(K)$ and that (T(t)) $t \geq 0-w i t h \quad T(0)=I d-i s$ a one-parameter semigroup. In fact, the first assertion is a consequence of (a) and (b), the second follows from (a) and the semigroup property is implied by the Chapman-Kolmogorov equation.

Moreover, the semigroup $(T(t))_{t \geq 0}$ is strongly continuous. This can be seen as follows: In view of Prop. 1.23 in Davies (1980) we only have to show that $\quad l^{i m} t+0<T(t) f-f, v>=0 \quad$ for every $f \in C(K), v \in M(K)$. Due to Lebesgue's Dominated Convergence Theorem this is true whenever $\lim _{t+0}(T(t) f)(x)=f(x)$ for every $f \in C(K), x \in K$. Given $f, x$ and $\varepsilon>0$ there exists an open neighborhood $U$ of $x$ such that $|f(x)-f(y)|<\varepsilon$ for every $y \in U$. Then we have
$(T(t) f)(x)-f(x)=\int_{K} f(y) P_{t}(x, d y)-\int_{K} f(x) P_{t}(x, d y)=$
$\int_{U}(f(y) \sim f(x)) P_{t}(x, d y)+\int_{K}\left(f(f(y)-f(x)) P_{t}(x, d y) \leqslant\right.$
$\varepsilon \cdot P_{t}(x, U)+2\|f\|_{\infty} \cdot P_{t}(x, K \backslash U)$.
Since $P_{t}(x, U) \cong 1$ and $l_{i m t}{ }_{t+0} P_{t}(x, U)=1=P_{t}(x, K)$ this estimate
implies $\limsup _{t+0}((T(t) f)(x)-f(x)) \leqq \varepsilon$. Since $\varepsilon=0$ was arbitrary we have pointwise convergence hence strong continuity of the semigroup.
Finally we observe that every operator $T(t)$ defined by (2.4) has the strong Feller property since $T(t){ }^{\prime} \chi_{C}=P_{t}(, C)$ for every Borel set $C=K \quad($ see $\operatorname{Prop.2.4(a)).}$
Thus Thm. 2.5 can be applied in this situation.

We now turn our interest from eventually compact semigroups to quasicompact semigroups. While "eventually compact" means that the operators $T(t)$ with $t \geqq t_{0}$ have to be compact, "quasi-compactness" only means that $T(t)$ approaches the compact operators as $t * \infty$. To make this precise we introduce the following notations,
For a Banach space $G$ the ideal of all compact linear operators on $G$ is denoted by $K(G)$. For $T \in L(G)$ we define
$\operatorname{dist}(T, K(G)):=\inf \{\|T-K\|: K \in K(G)\}$.

Definition 2.7. A strongly continuous semigroup ( $T(t)$ ) tap on a Banach space $G$ is called guasi-compact if lim $_{t \rightarrow \infty}$ dist $(T(t), k(G))=0$.

Quasi-compactness can be characterized in different ways. Two of them are stated in the following proposition. The first one uses the notion of the essential growth bound wess $(T)$ of a semigroup $T$ which was introduced in $\mathrm{A}-\mathrm{III}, 3.7$.

Proposition 2.8. For a strongly continuous semigroup $T=(T(t))$ t $\geqslant 0$ on a Banach space $G$ the following conditions are equivalent:
(i) $T$ is quasi-compact;
(ii) ess ${ }^{(T)}<0$;
(iii) There exist $t_{O}>0, K \in K(G)$ such that $\left\|T\left(t_{O}\right)-K\right\|<1$.

Proof. (i) $\rightarrow$ (iii) is obvious by the definition of quasi-compactness.
(iii) *(ii) : Recalling the definition of the essential spectral radius from A-III, (3.6), assertion (iii) implies
$r_{e s s}\left(T\left(t_{0}\right)\right)$ 古 $\left\|_{i} T\left(t_{0}\right)\right\|_{\text {ess }}<1$. Then $\omega_{\text {ess }}(T)<0$ by $A \rightarrow I I,(3,10)$. (ii) + (i) : BY A-III, (3.IO) we have $r_{\text {ess }}(T(1))<1$. Then $A-I I I,(3.6)$ implies 1 im $_{n \rightarrow \infty}\|T(n)\|$ ess $\leqslant 1$, where $\|T\|_{\text {ess }}=\operatorname{dist(T,K(G))\text {.Thus}}$ for suitable $n_{0} \in \mathbb{N}, a<1$ we have $\|T(n)\|_{\text {ess }}<a^{n}$ for $n \geqq n_{o}$. Choosing a sequence $k_{n} \in K(G)$ such that ${ }^{\prime} T(n)-K_{n} \|<a^{n}$ for $n$ a $n_{0}$ and defining $M:=\sup _{0 \leq s \leq 1}\|T(s)\|$ we obtain for $t \in[n, n+1]$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-230.jpg?height=72&width=1617&top_left_y=792&top_left_x=205) implies that $\lim _{t \rightarrow \infty}$ dist(T(t), $\left.K(G)\right)=0$.

A typical situation where quasi-compact semigroups occur is the following. if $T=(T(t))_{t>0}$ is a strongly continuous semigroup with $\omega_{\text {ess }}(T)<\omega(T)$ then the rescaled semigroup (exp(-w(T))T(t)) tzo is quasi-compact. Obviously every semigroup with growth bound less than zoro is quasi-compact. A more interesting situation is the following: If $\left(T_{o}(t)\right)_{t \geq 0}$ is a semigroup with growth bound less than zero and $A_{o}$ is its generator, then for every compact operator $K$ the perturbed operator $A:=A A_{0}+K$ generates a quasi-compact semigroup. More generally we have the following result:

Proposition 2.9. If (T(t)) $t \geq 0$ is a quasi-compact semigroup on a Banach space $G$ with generator $A$ and $K$ is a compact operator then $A+K$ generates a quasi-compact semigroup.

Proof. If ( $T(t))_{t \geqslant 0}$ and $(S(t))_{t \geq 0}$ are the semigroups generated by $A$ and $A+K$ respectively we have $S(t)=T(t)+\int_{0}^{t} T(t-s) K s(s) d s$. In view of Prop. 2.8 (iii) it is enough to show that $\int_{0}^{t} T(t-s) K S(s) d s$ is a compact operator.
since the mapping $(t, x) \rightarrow T(t) x$ is jointly continuous on $\mathcal{F}_{+} \times G$ and since $K$ is compact the set $M:=\{T(s) K x: 0 \leqslant s \leq t,\|x\| \leq 1\}$ is relatively compact in $G$. Having in mind that
$\int_{0}^{t} T(t-s) K S(s) x d s(x \in G)$ is the norm limit of Riemann sums, one observes that $(c t)^{-1} \int_{0}^{t} T(t-s) K S(s) x$ ds $i s$ an element of the closed convex hull $\overline{\mathrm{co}} \mathrm{M}$ of M , provided that $\mathrm{c}:=\sup \{\|S(5)\|: 0 \leqq s \leq t\}$ and $\|x\| \leq 1$. Since $\overline{0} \mathrm{M}$ is compact (see II.4.3 in Schaefer (1966)) the assertion follows.

We will now show that for quasi-compact semigroups one can give a description of the asymptotic behavior similar to the one stated for eventually compact semigroups in Thm.2.1 . One obtains a representation as in (2,1) with a remainder of exponential decay but the rate of the decay cannot be chosen arbitrarily large.

Theorem 2.10. Let $T=(T(t))$ tzo be a quasi-compact semigroup on a Banach space $G$ with generator $A$. Then $(\lambda \in \sigma(A): \operatorname{Re} \lambda \geqq 0\}$ is a finite set (possibly empty) and contains only poles of finite algebraic multiplicity. Denoting the eigenvalues with nonnegative real part $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{m}$, the corresponding residues $P_{1}, P_{2}, \ldots, P_{m}$ and the orders of the poles $k(1), k(2), \ldots, k(m)$ we have
```
(2.5) $\quad T_{n}(t)=\exp \left(\lambda_{n} t\right) \cdot \sum_{j=0}^{k(n)-1} \frac{1}{j!} \cdot t^{j}\left(A-\lambda_{n} j^{j}{ }_{n} P_{n} \quad(t \geq 0) \quad\right.$ and
    $\|R(t)\| \leqslant C \cdot e^{-E t}$ for suitable constants $E>0, C \geqslant 1$.
```
            $T(t)=T_{1}(t)+T_{2}(t)+\ldots+T_{m}(t)+R(t) \quad$ where

Proof. We have wess $(T)<0$ hence $r_{\text {ess }}(T(1))<1$ (see $\left.A-I I I,(3.10)\right)$. Therefore $\{z \in \sigma(T(1)): \mid z!\geq 1\}$ is a finite set and contains only poles of finite algebraic multiplicity (cf. A-III, (3.8)). Let $P$ denote the spectral projection of $T(1)$ corresponding to $\left\{\begin{array}{c}\mathrm{z} \\ \boldsymbol{\sigma}(\mathrm{T}(1)): ~\end{array}\right.$ $|z| z 1\}$. Then A-III, Cor. 6.5 implies that $\{\lambda \in \sigma(A):$ Re $\lambda \geq 0\}$ is a finite set, it contains only poles of $k(., A)$ of finite algebraic multiplicity and $P=P_{1}+P_{2}+\ldots+P_{m}$. One can now prove the representation of $T(t)$ stated in (2.5) in the same way as statement (2.1).

In case we consider positive quasi-compact semigroups on $C_{o}(X)$ one can combine Thm.2.10 with the results of B-III . For example, B-III, Cor. 2.ll assures that, in case there is at least one eigenvalue with nonnegative real part, the generator has a strictly dominant eigenvalue $r \in \mathbb{R}$. Thus in (2.5) the operators $T_{j}(t)$ belonging to $\lambda_{j}=r$ will determine the long term behavior of (T(t)). More precisely one has the following.

Corollary 2.11. Let $T=(T(t)) t \geqslant 0$ be a positive semigroup on $C_{0}(X)$ which is quasi-compact and let $A$ be its generator.
(a) Let $r$ be an eigenvalue of $A$ admitting a stricly positive eigenfunction and satisfying ke $r \geqq 0$, Then $r=\omega(T)=s(A)$ and there is a positive projection $P$ of finite rank such that for
suitable constants $\delta>0, M \geq 1$ we have
(2.6) $\left\|e^{-r t} \cdot T(t)-P\right\| \leq M \cdot e^{-\delta t}$ for all $t \geq 0$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-232.jpg?height=58&width=1606&top_left_y=491&top_left_x=225) strictly positive function $h \in C_{o}(X)$ and a strictly positive bounded measure $v \in M(X)$ such that for suitable constants $\delta>0, M \geq 1$ one has
(2.7) $\left\|\exp (-\omega(T) t) \cdot T(t)-v h_{h}\right\| \quad s \quad M \cdot e^{-\delta t}$ for all $t \geqq 0$.

In both cases (a) and (b) the estimates (2,3) for $\| T(t) f$ hold true (in case (a) one has to replace $\left|\int f d v\right|$ by $\|p f\|$ ).

Proof. (a) By B-III, Cor. 2.11 we know that $s(A)$ is a strictly dominant eigenvalue of $A$. By Thm. 2.10 both $s:=s(A)$ and $r$ are poles of the resolvent. Moreover, there exists a positive measure $v$ such that $A^{\prime} v=s v$. Denoting the strictly positive eigenfunction corresponding to $I$ by $h$ we have $\langle h, v\rangle\rangle 0$. Hence $s\langle h, v\rangle=\left\langle h, A^{\prime} v\right\rangle=\langle A h, v\rangle=$ $=r$ rh, U m implies $\mathrm{r}=\mathrm{s}$. BY B-III,Rem. 2.15 we know that $s$ is a first order pole of the resolvent. since $s$ is strictly dominant (2.6) follows from (2.5).

Assertion (b) can be proved in the same way as cor. 2.2 . We omit the details.

Cor.2.ll can be used to describe the asymptotic behavior as t*o of certain semigroups if only the generators are known. We explain this by discussing a concrete example.

Example 2.12. Let $x:=[0, \infty)$ and define on $E:=C_{o}(x)$ the operator A as follows
(2.8) $D(A):=\left\{f \in C_{o}(X): f\right.$ is differentiable, $f^{\prime} \in C_{o}(X)$ and $\left.f^{\prime}(0)=\alpha f(0)-\int_{0}^{\infty} f(x) d v(x)\right\}$.

Here a is a real number, $v$ is a bounded positive Borel measure with $v([0\})=0$ and $m$ is a continuous function on $x$ such that $m(\infty):=1 m_{x+\infty} m(x)$ exists. It is not difficult to see that A generates a positive semigroup. Moreover, one can show that it is quasi-compact if (and only if) $m(\infty) \leqslant 0$. In order to find eigen-
values and eigenfunctions one has to solve the ordinary differential equation $f^{\prime}=m f-\lambda f$. Any solution has (up to a constant) the following form
$$
\begin{equation*}
g_{\lambda}(x)=\exp \left\{\int_{0}^{x}(m(y)-\lambda) d y\right\}=e^{-\lambda x} \cdot \exp \left\{\int_{0}^{x} m(y) d y\right\} \tag{2.9}
\end{equation*}
$$

We assume that $m(\infty)<0$ and $r \geqq 0$. Then $g_{r}$ is differentiable with $g_{r}, g_{r}^{\prime} \in C_{o}(X)$. Thus $g_{r} \in D(A)$ if and only if $g_{r}^{\prime}(0)=\alpha g(0)-\int_{0}^{\infty} g_{r}(y) d v(y)$. Inserting (2.9) this condition becomes $m(0)-r=a-\int_{0}^{\infty} e^{-r y} \cdot \exp \iint \frac{Y}{0} m(z) d z f d u(y)$.
By monotonicity this equation has a unique solution $r 20$ if and only if
$(2.10) \mathrm{m}(0)+\int_{0}^{\infty} \exp \left\{\int_{0}^{y} m(z) d z\right\} d v(y) \geqq a$.
In case $\alpha, v$ and $m$ satisfy $(2,10)$ and $m(\infty)<0$ then $g_{r}$ is a strictly positive eigenfunction of $A$ corresponding to $r$ s 0 . Thus all assumptions of Cor.2.ll(a) are satisfied. In addition, the semigroup is irreducible if (and only if) the support of $v$ is an unbounded subset of $[0, \infty)$.

Similar examples will be discussed in B-IV, Sec. 3 and C-Iv, Sec. 3 ,
We finally give a criterion for quasi-compactness of positive semigroups on spaces $C(K)$. It is based on a criterion given by Doeblin for operators on spaces of bounded measurable functions and can be easily deduced from [Lotz (1981), Prop.3〕.

Proposition 2.13. Let $T=(T(t))_{t z 0}$ be a semigroup of Markov operators on $C(K), K$ compact satisfying the following condition. (2.12) There exist $t_{0}>0,0<\mu \in M(K)$ and $\gamma \in \mathbb{R}, 0<\gamma<1$ such that $T\left(t_{0}\right) f-\mu(f) 1_{K} \leqq \gamma-l_{K}$ for all $O \leqq f \leqslant 1_{K}$.

Then $T$ is quasi-compact.

\title{
3. A SEMIGROUP APPROACH TO RETARDED DIFFERENTIAL EQUATIONS
}
by
Annette Grabosch and Ulrich Moustakas

The aim of this section is to put into evidence the connection between retarded differential equations and one-parameter semigroups. Special emphasis will lie, as the general theme of this chapter suggests, on positive solutions of such equations and on their asymptotic behavior. Scalar examples were already considered in B-III, Ex. 2.14 , B-II, Ex. 1.21 , $B-I I, E x .1 .23, B-I I, E x .2 .11$ and $B-I V, E x .2 .12$. In this section we will treat retarded differential equations, also called "delay differential equations", with values in arbitrary Banach spaces. A slight modification of the methods used in the scalar case will work in this setting, too. The main question is whether or how a time delay affects the qualitative behavior of the solution of an abstract Cauchy problem. In particular we will show in Thm. 3.7. resp. Cor. 3.8 that under certain positivity assumptions the delay has no influence on the stability.

Let $F$ be a Banach space, let $E=C([-1,0], F)$ be the Banach space of all continuous functions on $[\cdots 1,0]$ with values in $F$ normed by the supremum norm, and let $\Phi$ be a bounded linear operator from E into F. For $u \in C([-1, \infty), F)$ and $t z 0$ we define the function $u_{t} \in E$ by $u_{t}(s):=u(t+s)$ for all $s \in[-1,01$. This is the "history ${ }^{\prime \prime}$ segment of $u$ with length 1 starting at $t-1$. Furthermore, let $B$ be the generator of a strongly continuous semigroup on $F$ such that $B-w$ generates a contraction semigroup for some $w \in \mathbb{R}+$ This additional condition can always be satisfied by renorming the Banach space $F$ (see e.g. [Goldstein (1985a), thrm,2.13]).

Using this framework throughout this section it should be mentioned that in general $E=C([-1,01, F)$ is not a space of type $C(K)$ or even $C_{0}(X)$. Nevertheless, the formal appearence justifies a treatment in this chapter. Moreover, if $F=C(M)$ (M compact) it is well-known that $E$ is isomorphic to $C([-1,0] \times M)$ and thus is a space of type $C(K)$ ( $K$ compact) as well.

With the above notations we consider
$$
\begin{aligned}
\dot{u}(t) & =B u(t)+\Phi\left(u_{t}\right), t \geq 0 \\
u_{0} & =g \in E .
\end{aligned}
$$

We call (RCP) an abstract retarded Cauchy problem.
A function $u \in C([-1, \infty), F)$ is a solution of (RCP), if
(a) u is right-sided differentiable at 0 and continuously differentiable for $t>0$,
(b) $u(t) \in D(B)$ for $t \geq 0$,
(c) (RCP) is satisfied for $t \geq 0$.

To (RCP) we associate the following operator A on the Banach space E.
Let $A$ be the differential operator
$$
\begin{align*}
A f & :=f \\
D(A) & :=\left\{f \in C^{1}([-1,0], F): f(0) \in D(B), f^{\prime}(0)=B f(0)+\Phi f\right\} . \tag{3.1}
\end{align*}
$$

First we show that $A$ is a generator on $E$.

Theorem 3.1. The operator A defined in (3.1) is the generator of a strongly continuous semigroup $(T(t)){ }_{t} \geq 0$ on $E$ satisfying the "translation property"
$$
T(t) f(s)=\left\{\begin{array}{ll}
f(t+s) & \text { if } t+s \leq 0  \tag{T}\\
T(t+s) f(0) & \text { if } t+s>0
\end{array} \quad, f \in E .\right.
$$

Proof. We argue as in B-III, Example 2.14.(b) and consider the operator $A_{o} f:=f^{\prime}$ on the domain
$D\left(A_{0}\right):=\left\{f \in C^{1}\left([-1,0,7, F): f(0) \in D(B), f^{\prime}(0)=B f(0)\right\}\right.$.
If $(S(t)){ }_{t} \geq 0$ is the semigroup on $F$ generated by $B$, then $A_{o}$ generates the semigroup $\left(T_{o}(t)\right) t \geqq 0$ given by
$$
T_{0}(t) f(s)=\left\{\begin{array}{ll}
f(t+s) & \text { if } t+s \leq 0 \\
s(t+s) f(0) & \text { if } t+s>0
\end{array} \quad, f \in E\right.
$$

For $\lambda>w^{\prime}$ define the map $s_{\lambda} \in L(E)$ by $S_{\lambda} f:=f-e_{\lambda} g R(\lambda, B)$ ff where $E_{\lambda}(s)=e^{\lambda s}$ and $\left(h ⿴_{x}\right)(s):=h(s) \cdot x$ for $h \in C[-1,0], x \in F$ and $s \in\left[-1,03\right.$. Since $\|R(\lambda, B)\|(\lambda-w)^{-1}$ it follows that $S_{\lambda}$ is invertible for $\lambda>\|\phi\|+w$ and that $\left\|S_{\lambda}^{-1}\right\| \leq(\lambda-w)=\left(\lambda-\|\Phi\|_{-}^{\lambda}\right)^{-1}$. Moreover, $S_{\lambda}$ induces a bijection from $D(A)$ onto $D\left(A_{o}\right)$ such that
$$
\lambda-A=\left(\lambda-A_{0}\right) S_{\lambda}
$$
$$
\begin{equation*}
R(\lambda, A)=s_{\lambda}^{-1} R\left(\lambda, A_{0}\right) \tag{3.2}
\end{equation*}
$$

Proceeding as in the example mentioned above we obtain
$\|R(\lambda, A)\| \leqslant(\lambda-w) \cdot(\lambda-\|\Phi\|-w)^{-1} \cdot(\lambda-w)^{-1}$
$$
s(\lambda-\|\phi\|-w)^{-1} .
$$

Thus $A$ is a generator by A-II,Thm,1.7.

It suffices to show the translation property ( $T$ ) for $f \in D(A)$ only. To that purpose we treat two cases separately.
1. Let $t \geq 0, s \in[-1,0]$ and $t+s>0$. It suffices to prove $T(-s) g(s)=g(0)$ for $g=T(t+s) f$. For arbitrary $g \in D(A) \quad$ we define the map
$$
h:[-t, 0] \rightarrow F \quad b y \quad h(r)=\delta_{r} T(-r) g,
$$
where $\delta_{r}$ denotes the point evaluation $f * f(r)$ on $E$. For $\& \neq 0$ we have
$1 / \theta *(h(r+\theta)-h(r))=1 / \theta *(T(\sim r-\theta) g(r+\theta)-T(-r) g(r))$
(1)
$$
=1 / \theta \cdot(T(-r-\theta) g(r)-T(-r) g(r))
$$
(2)
(3)
$$
+1 / \theta \cdot\left(\delta_{r+\theta}-\delta_{r}\right)(T(-r-\theta) g-T(-r) g)
$$
$$
+1 / 8 \cdot(T(-r) g(r+g)-T(-r) g(r))
$$

As $\theta \rightarrow 0$, (1) converges to $-A[T(\sim r) g l(r),(2)$ converges to zero and (3) converges to A[T(~r)gi(r). Thus $h$ is continuously differentiable with derivative zero, whence $h(r)=h(0)$ for all $r \in[-t, 0]$ Taking $r=s$ yields $T(-s) g(s)=g(0)$.
2. Let $t z 0, s \in[-1,0]$ and $t+s \leq 0$. As in the first case we show that the map $k:[0, t] \rightarrow F: r \rightarrow[T(r) f](t+s-r)$ is continuously differentiable with derivative zero.
Thus $f(t+s)=k(0)=k(t)=T(t) f(s)$.

The translation property (T) enables us to specify the correspondence between the semigroup $(T(t)) t \geqslant 0$ generated by the operator in (3.l) and the solution of the retarded Cauchy problem (RCP).

Corollary 3.2. For $g \in D(A)$ define $u:[-1, \infty)+F$ by
$$
u(t):=\quad \begin{cases}g(t) & \text { if }-1 \hookrightarrow t \leqq 0 \\ T(t) g(0) & \text { if } 0<t .\end{cases}
$$

Then $u$ is the unique solution of (RCP).

Proof. Evidently $u \in C([-1, \infty), F)$ for $g \in D(A)$.
$$
\begin{array}{rl}
\text { From } A-I, P r o p .1 .6 .(i i i) ~ a n d ~ t h e ~ d e f i n i t i o n ~ o f ~ & D(A) \text { we obtain } \\
T(t) g(0)-g(0) & =E A\left(\int_{0}^{t} T(s) g d s\right) I(0) \\
& =B\left[\left(\int_{0}^{t} T(s) g d s\right)(0) ?+\Phi\left(\int_{0}^{t} T(s) g d s\right)\right. \\
& =B\left(\int_{0}^{t} T(s) g(0) d s\right)+\int_{0}^{t} \Phi T(s) g d s \\
& =B\left(\int_{0}^{t} u(s) d s\right)+\int_{0}^{t} \Phi T(s) g d s
\end{array}
$$
since $\int_{o}^{t} T(s) g d s \in D(A)$.

Since $u(t)=(T(t) g)(0) \in D(B)$ for $t \geqq 0$ the above calculation shows that $u$ is right-sided differentiable at 0 and differentiable for $t>0$; hence
$$
\dot{u}(t)=B u(t)+\Phi(T(t) g) .
$$

By the translation property (T) we have $T(t) g=u_{t}$, indeed
$u_{t}(s)=u(t+s)=\left\{\begin{array}{ll}g(t+s) & \text { if } t+s s 0 \\ T(t+s) g(0) & \text { if } t+s>0\end{array} \quad=T(t) g(s)\right.$.
Therefore $\dot{u}(t)=B u(t)+\phi\left(u_{t}\right)$, i.e. u solves (RCP).

In order to show uniqueness of the solution we take $w$ to be a solution of (RCP) satisfying $w_{o}=0$. Let $x(t):=w_{t}, t \geqslant 0 . ~ I t ~ i s$ easy to see that $x(t) \in C^{1}([-1,0], F)$; moreover, since $\dot{w}_{t}(0)=\frac{1}{w}(t)$ $=B w(t)+\Phi\left(w_{t}\right)$ we obtain $x(t) \in D(A)$. By the definition of $A$ we have $A x(t)=\dot{W}_{t}$. On the other hand, $x(\cdot) \in C^{1}([0, \infty), E)$ and $(\dot{x}(t))(s)=\lim _{h \rightarrow 0} 1 / h \cdot\left(w_{t+h}(s)-w_{t}(s)\right)$
$$
=\lim _{h \rightarrow 0} 1 / h \cdot\left(w_{t}(h+s)-w_{t}(s)\right)=\dot{w}_{t}(s) \text {, whence } \dot{x}(t)=\dot{w}_{t} \text {. }
$$

Therefore we obtain $x(t)=A x(t)$. $A s x(0)=w_{0}=0$ it follows by the well-posedness of the abstract cauchy problem corresponding to A that $x(t)=0$ for each $t \geqq 0$. This proves $w \equiv 0$.

Remarks l. By similar arguments the following can be proved. If u is a solution of (RCP) such that $u_{0} \in D(A)$, then $x$ given by $x(t)$ : $=$ $u_{t}$ is a solution of the abstract Cauchy problem associated with the operator $A$ defined in (3.1). In this sense, (RCP) and the semigroup generated by $A$ correspond to each other.
2. If additionally to the assumptions of Cor.3.2 $B \in L(F)$ then $u$ is a solution of (RCP) for every $g \in E$. [Indeed, a careful inspection shows that the proof of Cor. 3.2 can be generalized to this situation, since $u(t)=(T(t) g)(0) \in F=D(B)$ for all $g \in E$ and $t \geqslant 0 . ?$
3. For general $g \in E$ the retarded Cauchy problem (RCP) may not have a solution. Indeed, if $u$ is a solution of (RCP) then the following is valid for $0 〔 s$ ¢
$\frac{d}{d s} s(t-s) u(s)=-B S(t-s) u(s)+s(t-s) \dot{u}(s)$
$$
=-B S(t-s) u(s)+S(t-s) B u(s)+s(t-s) \Phi\left(u_{s}\right)=s(t-s) \Phi\left(u_{s}\right)
$$

Hence
$$
u(t)-s(t) u(0)=\int_{0}^{t} s(t-s) \phi\left(u_{s}\right) d s .
$$

Let (S (t)) $t$ bo be a stroncly continuous semigroup which is not differentiable (for examples see $A-I I, 1.2 B$ ). Define $g \in E$ by $g(s) ;=\vec{g}$ for all $s \in[-1,0]$ where $\tilde{q} \in F$ is chosen such that
$t * S(t) g$ is not differentiable in $t \in \mathbb{F}_{+}$
Assume that there exists a solution of (RCP). By the preceding considerations
$u(t)=s(t) g(0)+\int_{0}^{t} s(t-s) \Phi\left(u_{s}\right) d s=s(t) \tilde{g}+\int_{0}^{t} s(t-s) \Phi\left(u_{s}\right) d s$.
Thus $u$ is not differentiable in $t$, and we have a contradiction.

Corollary 3.3. Keep the above notation and let $F$ be finite dimensional. Then the solution semigroup (T(t)) $t \geqq 0$ in $E$ corresponding to (RCP) is compact for each $t>1$ and therefore is eventually norm continuous.

Proof. Let $t>1$. By the translation property (T) we have $T(t) f(s)=T(t+s) f(0)$. Whenever $t+s>0$ then Rem. 2 following Cor.3.2 shows that $(T(t) f)(s)=(T(t+s) f)(0)=u(t+s) \quad i s$ differm entiable with respect to $s \in[-1,0]$ for each $f \in E$. Since $t>1$ we thus have $T(t) f \in C^{1}([-1,0.7, F)$ for all $f \in E$. The closed graph theorem yields the continuity of $T(t)$ from $E$ into $C^{1}$. Hence $T(t)$ maps the unit ball of $E$ into a bounded set of $C^{l}([-1,0], F)$. Again we use the assertion that dim $F \ll$ and obtain by the theorem of Arzela-Ascoli that every bounded set of $C^{1}([-1,0,1, F)$ is relatively compact in $E$. Thus $T(t)$ is compact for each $t>1$.

The assertion of Cor. 3.3 remains true if (s(t)) tzo is a compact semigroup on a (not necessarily finite dimensional) Banach space $F$ (see [Travis-Webb (1974) 7).

In order to describe the asymptotic behavior of the solutions of (RCP) it is enough to examine the corresponding semigroup $(T(t))$ t $\geq 0$ on $E$. Indeed. Cor.3.2 shows that the solutions $u$ are given by $u(t)=$ $T(t) g(0)$ for all $t>0$ and thus the long term behavior of $u$ can be deduced from that one of ( $T(t)$ ) $t \geqslant 0$. Our approach is based on the characterization of the stability of the semigroup ( $T(t)$ ) $t \geqslant 0$ by the location of the spectrum o(A) of the generator $A$ as developed in A-IV, Sec.1, B-IV, Sec. 1 and C-IV, Sec.l.

We define, for $\lambda \in \mathbb{C}$, operators $\Phi_{\lambda} \in L(F)$ by
$$
\begin{equation*}
\Phi_{\lambda} x:=\Phi\left(E_{\lambda} \otimes x\right), x \in F . \tag{3.3}
\end{equation*}
$$

Since $\Phi_{\lambda}$ is bounded the operator $B+\Phi_{\lambda}$ is a generator on $F$. The spectrum of $A$ can now be characterized in terms of the spectrum of the operators $B+\Phi_{\lambda}$.

Proposition 3.4. Take the operators A , B and $\Phi$ as above. For every $\lambda \in \mathbb{C}$ the following equivalence holds:
```
\lambda\in\sigma(A) if and only if }\lambda\in\sigma(B+\Phi)
```

Proof. By definition, $\lambda \in p(A)$ if and only if for every $g \in E$ there exists a unique $f \in D(A)$ such that $h f-f=g$. This equality is satisfied if and only if there exists $x \in F$ such that
$$
f(t)=\int_{t}^{0} e^{\lambda(t-s)} g(s) d s+e^{\lambda t} \cdot x \text { for }-1 \leq t \leq 0
$$

On the other hand $f \in D(A)$ if and only if $x \in D(B)$ and $\lambda x-g(O)$ $=B x+\Phi H_{\lambda} g+\Phi_{\lambda} x$ where $H_{\lambda} g(t):=\int_{t}^{\rho} e^{\lambda(t-s)} g(s) d s$.
Thus $\lambda \in \rho(A)$ if and only if for every $g \in E$ there exists a unique $x \in D(B)$ such that $\left(\lambda-B-\Phi_{\lambda}\right) x=g(0)+\Phi H_{\lambda} g$. Notice that the map $x * x+\Phi H_{\lambda}\left(E_{\mu}(0 x) \quad(x \in F)\right.$ is surjective on $F$ if $\mu$ is chosen so large that $\left\|\frac{H_{h}}{\lambda}\left(E_{\mu} 8 x\right)\right\| \leq 1 / 2 \cdot\|x\|$ for all $x \in F$. Hence the map $g \rightarrow$ $g(0)+4 H_{\lambda} g$ is surjective from $E$ onto $F$ and this shows that $\lambda \in$ $p(A)$ if and only if $\lambda-B-\Phi_{\lambda}$ is invertible.

An immediate consequence of the proof is the following corollary.

Corollary. With the notations of the above proposition and $A_{o}$ as in the proof of Thm. 3.1 we have:
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-239.jpg?height=53&width=1577&top_left_y=1521&top_left_x=245)
(b) $R\left(\lambda, A_{o}\right) g=E_{\lambda} R R(\lambda, B) g(0)+H_{\lambda} g \quad$ for $\lambda \in \rho\left(A_{o}\right), g \in E$.

We now turn to the aspect of positivity in (RCP) and its impact on the asymptotic behavior of the solution semigroup ( $T(t)$ ) $t \geq 0$.
To this end we let $F$ be a Banach lattice which makes $E=C([-1,0], F)$ into a Banach lattice as well. Furthermore, let $(S(t))$ ta 0 be a positive semigroup with generator $B$ and let $\Phi \in L(E, F)$ be a positive operator. As before we restrict our attention to the case that $B-w$ generates a positive contraction semigroup for some $w \in f$. Indeed, if $B$ generates a bounded positive semigroup (S(t)) $t \geq 0$ on $F$, then $\|x\|:=\sup _{t \geq 0}\|S(t)\| x\| \|$ for $x \in F$ defines an equivalent lattice norm on $F$, for which $(S(t))$ t $\geq 0$ is contractive.

Proposition 3.5. If $9 \in L(E, F)$ is a positive operator and if $B$ generates a positive semigroup on $F$, then the semigroup ( $T(t)$ ) tzo on $E$ generated by $A f:=f^{\prime}$ with domain $D(A):=\left\{f \in C^{l}: f(0) \epsilon\right.$ $D(B), f^{\prime}(0)=B f(0)+$ وft is positive.

Proof. By Formula (3.2) we have $R(\lambda, A)=s_{\lambda}^{-1} R\left(\lambda, A_{o}\right)$ for $\lambda>\| d+w$, (where $S_{\lambda} f=f-E_{\lambda} \theta R(\lambda, B) \Phi f$ for $f \in E$ ). Thus the fact that $R\left(\lambda, A_{o}\right)$ is positive (C-II,Prop.4.l) reduces the problem to showing that $s_{\lambda}^{-1}$ is a positive operator for $\lambda>\|\Phi\|+w$.
Since $S_{\lambda}=I d-E_{\lambda} \theta R(\lambda, B) \Phi$ and $\left\|\varepsilon_{\lambda} g R(\lambda, B) \phi\right\| \leq(\lambda-w)-\|\Phi\|<l$ we see that $S_{\lambda}{ }^{-1}=\sum_{n=0}^{\infty}\left(E_{\lambda} 8 R(\lambda, B)\right)^{n}$ is positive. Hence $(T(t))$ teo is a positive semigroup again by C-II, Prop.4.l.

Remark. Suppose that $\Phi$ has no mass in zero (i.e., for every $\varepsilon>0$ there exists $\delta>0$ such that $\|\Phi f\| \in \in\|f\|$ for all $f \in E, \operatorname{supp}(f) \in$ $[-0,03]$. Then the positivity hypotheses in the above proposition are necessary in order to obtain positivity of (T (t)) ${ }_{t \geqslant 0}$ (cf. B-II.l. 22 for the case dim $F<\infty$ and [Kerscher (1986). for the general case).

Proposition 3.6. Let $\Phi \in(E, F)$ be positive and assume that $B$ generates a positive semigroup on $F$. The "spectral bound function" $\lambda \rightarrow s\left(B+\Phi_{\lambda}\right)$ is decreasing and continuous from the left on $R$. If, additionally, $B$ has compact resolvent and there exists $\lambda^{\prime} \in \mathbb{R}$ with $o\left(B+\Phi_{\lambda}, \neq \emptyset\right.$, then $\lambda \rightarrow s\left(B+\Phi_{\lambda}\right)$ is continuous and the spectral bound $s(A)$ is the unique solution of the equation
$$
\begin{equation*}
\lambda=s\left(B+\Phi_{\hbar}\right) \tag{3.5}
\end{equation*}
$$

Proof (cf. also C-IV, Lemma 3.4). For $\lambda \leqq \mu$ we have $0 \leq \Phi_{k} \leq \Phi_{\lambda}$ and hence $0 \subseteq R_{\mu}(t): R_{\lambda}(t), t \geqq 0$, for the respective semigroups generated by $B+\phi_{\mu}$ and $B+\Phi_{\lambda}$ (see A-II, Sec.l). This implies $s\left(B+\Phi_{\mu}\right) \leqslant s\left(B+\Phi_{\lambda}\right)$. The left-continuity follows by the semicontinuity of the spectrum (see [Kato (1976) Chap.IV, Thm.3.1]).
If $B$ has compact resolvent then $B+\Phi_{\lambda}$ has compact resolvent as well. Now C-III,Thm.l.l.(a) shows that $s\left(B+\Phi_{\lambda}\right)$ belongs to $\sigma\left(B+\Phi_{\lambda}\right)$ and, by $A-I I I, 3.6$ is a pole with residue of finite rank. This completes the proof since spectral points of compact operators depend continuously on smooth perturbations (see fDunford-Schwartz (1958), VII, 6.Thm.93).

If $\sigma(B) \neq \phi$, then $-\infty<s(B) \leqslant s\left(B+\varphi_{\lambda}\right)$ for all $\lambda \in$ iR which implies $\sigma\left(B+\Phi_{\lambda}\right) \neq \theta$. On the other hand, if $\sigma\left(B+\phi_{\lambda}\right)=\phi$ for all $\lambda \in \mathbb{R}$ then $\sigma(A)=\emptyset$ by Prop.3.4.

We are now able to characterize the spectral bound of the generator $A$ in $E$ through spectral bounds of generators in $F$.

Theorem 3.7. Let $\Phi \in \mathbb{( E , F )}$ be positive and let $B$ be the generator of a positive semigroup on $F$. The following implications are valid :
(a) If $s\left(B+\Phi_{\lambda}\right)<\lambda$, then $s(A)<\lambda$.
(b) If $s\left(B+\Phi_{\lambda}\right)=\lambda$, then $s(A)=\lambda$.
(c) Suppose that $B$ has compact resolvent and there exist $\lambda^{\prime} \in \mathbb{R}$ with $\sigma\left(B+\Phi_{\lambda}\right) \neq \emptyset$. Then
(3.6) $\quad s\left(B+\Phi_{\lambda}\right) \stackrel{\leqq}{>} \lambda$ if and only if $s(A) \leqq \lambda$.

Proof. (a) If $\lambda>s\left(B+\Phi_{\lambda}\right)$, then $\mu>s\left(B+\Phi_{\mu}\right)$ for all $\mu \geqq \lambda$ by Prop.3.6 , Therefore, $\mu \in \rho\left(B+\Phi_{\mu}\right)$ for all $\mu \geqslant \lambda$. By Prop. 3.4 this implies $\mu \in \rho(A)$ for all $\mu \geq \lambda$. Since $s(A) \in \sigma(A)$ by [C-III, Thm.1.1.(a)] we obtain $\lambda>s(A)$.
(b) If $\lambda=s\left(B+\Phi_{\lambda}\right)$, then again $\lambda \in \sigma\left(B+\Phi_{\lambda}\right)$ whence we obtain from Prop. $3.4 \lambda \in \operatorname{d}(A)$ and therefore $\lambda \leqq s(A)$. In the same way as in (a) we conclude that $\mu \in \rho(A)$ if $\mu \geqslant \lambda$; hence $\lambda=s(A)$.
(c) It suffices to prove that $s(A)>\lambda$ whenever $s\left(B+\Phi_{\lambda}\right)>\lambda$.

Assume the latter inequality. According to Prop. 3.6 there exists a unique $\mu$ satisfying $\mu=s\left(B+\Phi_{\mu}\right)$. Still by Prop. 3.6 it follows that $\lambda<\mu . A s s e r t i o n(b)$ now completes the proof.

Remark. We call (3.5) the generalized characteristic eguation corresponding to (RCP). A justification for this terminology will be given in a remark following Cor. 3.8 of Chapter C-IV.

The characterization (3.6) of $s(A)$ uses the continuity of $\lambda \rightarrow s(B$ $+\Phi_{\lambda}$. In the general case we apply the following lemma which is due to $w$. Arendt.

Lemma. Let $\Phi \in L(E, F)$ be positive and assume that $B$ generates a positive semigroup on $F$. If we define
$\mu:=\quad \begin{cases}\sup (\lambda \in \mathbb{R}: s(B+\Phi) \geqslant \lambda\} & \text { if } \sigma(B+\Phi) \neq \emptyset \text { for some } \lambda \in \mathbb{R}, \\ -\infty & \text { otherwise, }\end{cases}$
then $s(A)=\mu$.

Proof. If $\sigma(B+\Phi)=\emptyset$ for all $\lambda \in \mathbb{R}$ then $\sigma(A)=\emptyset$ by Prop. 3.4 and there is nothing to prove.
Take now $\lambda \in \mathbb{R}$ with $\sigma\left(B+\Phi{ }_{\lambda}\right) \neq \emptyset$ and show $\mu \in \sigma(B+\Phi \mu)$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-241.jpg?height=64&width=1431&top_left_y=2538&top_left_x=227)
Case 2: If $\mu<s\left(B+\Phi_{\mu}\right)$ we show $r \in \sigma\left(B+\Phi_{\mu}\right)$ for every $r \in$ $\left(\mu, s\left(B+\Phi_{\mu}\right) ?\right.$.

Let $\quad \mathrm{F}\left(\mu_{\mathrm{s}} \mathrm{s}\left(\mathrm{B}+\Phi_{\mu}\right)\right\}$ and assume $\mathrm{r} \in \rho\left(\mathrm{B}+\Phi_{\mu}\right)$. By the definition of $\mu$ we have $r \in \rho\left(B+\Phi_{\mu+\varepsilon}\right)$ for all $\varepsilon>0 . \quad B y \quad C-I I I, T h m .1 . l$ $R\left(r, B+\Phi_{\mu+\varepsilon}\right) \geq 0$ and by the assumption $R\left(r, B+\Phi{ }_{\mu}\right) \geqq 0$ as well. Now C-III,Thm.1.l implies $r>s\left(B+\Phi_{\mu}\right)$ which yields a contradiction to the choice of r. Thus $r \in \sigma\left(B+\Phi_{\mu}\right)$ for every $r \in(\mu, s(B+\Phi)]$ and hence $\mu \in \sigma\left(B+\Phi_{\mu}\right)$. Consequent ${ }^{7} y \quad s(A) \geq \mu$. Finally we assume $s(A)>\mu$. The definition of $\mu$ yields $s(A) \quad>$ $s\left(B+\Phi_{s(A)}\right)$. Hence $s(A) \in p\left(B+\Phi_{s(A)}\right)$ and thus $s(A) \in p(A)$ by Prop. 3.4 . This yields a contradiction, since $A$ generates a positive semigroup, hence $s(A)=\mu$.

An immediate consequence of the preceding lenma is the following stability criterion.

Corollary 3.8. Let $\Phi \in L(E, F)$ be positive and let $B$ be the generator of a positive semigroup. The following assertions are equivalent:
(i) The semigroup generated by $A$ is exponentially stable in $E$.
(ii) The semigroup generated by $B+\Phi_{o}$ is exponentially stable in $F$.

Proof. We can assume that there exists $\lambda \in \mathbb{R}$ with $\left.\sigma(B+\Phi)_{\lambda}\right) \neq \emptyset$. The implication "(i) $\rightarrow$ (ii)" follows inmediately from Thm. 3.7.(a), It remains to show "(ii) $\rightarrow$ (i)". Let $s\left(B+w_{o}\right)<0$. By the lemma and since $\lambda \rightarrow s\left(B+\Phi_{\lambda}\right)$ is non-increasing we have $s(A)=\mu=\sup \{\lambda$ : $\left.s\left(B+\Phi_{\lambda}\right)>\lambda\right\}<0$. Thus the semigroup generated by $A$ is exponential$\mathbf{l}_{Y}$ stable.

Remark. In the situation of Thm. 3.7(c) we have the stronger result that $s(A)$ and $s\left(B+\Phi_{0}\right)$ have the same sign.

Example 3.9 (see also C-IT,Ex.4.14). Take $E=C([-1,0], \mathbb{C}), a \in \mathbb{C}$ and $\mu \in M[-1,0]_{+}$such that $\mu(\{0])=0$. Then the operator $A$ given by $A f=f^{\prime}$ on $D(A)=\left\{f \in C^{1}([-1,0], C\}: f^{\prime}(0)=a f(0)+\langle f, \mu\rangle\right\}$ generates a strongly continuous semigroup (T(t)) ta ${ }^{\circ}$ In fact, this follows from Thm, 3.1 if we put $F=\mathbb{C}, \Phi=j$ and $B$ the multiplication by a. Moreover $\Phi_{0}$ is the multiplication by $\left\langle E_{0}, \Phi\right\rangle=\|\Phi\|$ (notice $\Phi \geq 0$ ) and $s\left(B+\Phi_{0}\right)=a+\|\Phi\|$. Since $\omega(A)=s(A)$ by B-IV, (1.1) we obtain from Cor.3.8 that $A$ generates a uniformly exponentially stable semigroup if and only if $a+\|\Phi\|<0$.

The preceding considerations remain true if we consider an (arbitrary) finite time delay $\tau$ where $0<\tau<\infty$. Clearly, (RCP) can be treated as an differential equation with corresponding generator A (see (3.1) for the definition) in $C\left(\left[-\tau, 0 \_, F\right)\right.$ (instead of $\left.C([-1,0], F)\right)$.

Example 3.10. In order to illustrate the consequences of Cor. 3.8 we consider the Cauchy problem
```
$\dot{u}(\mathrm{t})=\mathrm{Bu}(\mathrm{t})+\mathrm{Su}(\mathrm{t}-\mathrm{T}), \mathrm{t} \geqq 0$,
$u(t)=\psi(t),-\Psi \longleftarrow t \leqq 0(0 \lll \lll), \psi \in E$,
```
where $B$ is the generator of a positive semigroup on $F$, o(B) $\neq \phi$ and $S \in \mathbb{L}(F)$ is positive.

Using the above terminology, we have $\boldsymbol{f} f=S(f(-\uparrow))$ for all f $\in E$, hence $\Phi_{o}=S$. By cor. 3.8 the solution semigroup corresponding to the retarded differential equation (3.7) is exponentially stable if and only if the semigroup generated by $B+S$ is exponentially stable. But the semigroup generated by $B+S$ is the solution semigroup of the "undelayed" Cauchy problem
$$
\begin{array}{ll}
u(t)=B u(t)+S u(t) & t \geqq 0,  \tag{3.8}\\
u(0)=x, & x \in F .
\end{array}
$$

More precisely, we obtain the following corollary.
Corollary. The solution of (3.7) is exponentially stable for every $\tau>0$ if and only if the solution of (3, 8) is exponentially stable.

In other words, the corollary states that for this "positive-type" delay equations ( $(S(t))_{t \geqslant 0}$ and $\Phi$ positive) exponential stability is independent of the delay (see [Kerscher (1986) ] for a detailed analysis of this phenomenon).

This is a rather untypical behavior since even a scalar valued delay differential equation may be stable for "small" delays but unstable for ${ }^{17}$ large" delays.
We give an example and show how a stable Cauchy problem with nonpositive solutions (see the remark following Prop.3.5) can be destabilized by an increase of the time lig $\tau$
Let $0<i<\infty$ and $p, q \in \mathbb{R}$ and consider the following (RCP):
$(3.9) \tau$
$$
\begin{array}{ll}
\dot{u}(t)=p u(t)+q u(t-i), & t \leqq 0, \\
u(t)=\Psi(t), & -\tau \leqq t \leqq 0, \Psi \in C[-\tau, 0]
\end{array}
$$

The characteristic equation (in the classical sense) is:
(3.10) $\quad \lambda=p+e^{-\lambda i} q$

We consider the case where the Cauchy problem without delay
$$
\dot{u}(t)=(p+q) u(t)
$$
is asymptotically stable, i.e. we choose $0 < p <1$ and $q+p<0$.
Claim. For every $0<\lambda^{\prime} < p $ there exists $\tau>0$ such that $e^{\lambda^{\prime} t}$ is a solution of (3.9).

Consider the map $g: \mathbb{R} \times(\mathbb{R}+(0\}) \rightarrow \mathbb{R}$ defined by $g(\lambda, r)=p+e^{-\lambda t} q$. This function is continuous in $\lambda$ and $i$ and increasing in $\lambda$. Furthermore $g(0, i)=p+q<0$ for every $\quad=>0$ and $g(\lambda, i)$ iv $p$ as $T \rightarrow \infty$ for every $\lambda \in \mathbb{R}_{+}$. For $0<\lambda^{\prime} < p $ fixed we can find $\tau>0$ such that $g\left(\lambda^{\prime}, \tau\right)=\lambda^{\prime}$.
Let $\Psi(t)=e^{\lambda^{\prime}} t$ for $-\tau \leqq t \leqq 0$. If we define $u(t):=e^{\lambda^{\prime} t}$ for $t \geq 0$ then the following is valid:
$p u(t)+q u(t-\tau)=p e^{\lambda^{\prime} t}+q e^{\lambda^{\prime} t} e^{-\lambda^{\prime} t}=\left(p+q e^{-\lambda^{\prime} t}\right) e^{\lambda^{\prime} t}=\lambda^{\prime} e^{\lambda^{\prime} t}=\dot{u}(t)$. Thus $u$ is a solution of (3.9) which is exponentially increasing as $t \rightarrow \infty$. In particular (3.9) is not stable.
The precise region of stability in the scalar valued case is given, for example in [Hadeler (1978)] and [Hale (1977), 107ff].

Remark. Consider the case $F=C(M)$ (M compact).
Then $E=C([-1,0] \times M)$ and $(T(t)) t \geqq 0$ is a positive semigroup on $C(K)$ where $K=[-1,0] \times M$ is compact. Thus spectral bound and growth bound of the semigroup generator coincide (B-IV,(1.l)). This Yields a statement analogous to cor.3.8 for uniform exponential stability.

We conclude this section with two examples fitting into the above framework.

Example 3.Il. Consider the equation
$$
\frac{\partial}{\partial t} u(t, x)=\frac{\partial^{2}}{\partial}{ }^{2} x(t, x)-d(x) u(t, x)+b(x) u(t-1, x) \quad(t \geqslant 0, x \in[0,1])
$$
with boundary condition
$$
\begin{array}{r}
\text { (3.11) }\left.\frac{\partial}{\partial \mathrm{x}} \mathrm{u}(\mathrm{t}, \mathrm{x})\right|_{\mathrm{x}=0}=0=\left.\frac{\partial}{\partial \mathrm{x}} \mathrm{u}(\mathrm{t}, \mathrm{x})\right|_{\mathrm{x}=1} \quad(\mathrm{t} \geqslant 0 \\
\mathrm{and} \text { initial condition } \\
\mathrm{u}(\mathrm{~s}, \mathrm{x})=\psi(\mathrm{s}, \mathrm{x}) \quad(\mathrm{s} \in[-1,0], \mathrm{x} \in[0,1]) .
\end{array}
$$

Let $F=C[0,1], E=C([-1,0] \times[0,1])$ ard let $B$ be defined by $\tilde{B} h=h^{\prime \prime}$ with domain $D(\tilde{B}):=\left\{h \in C^{2}[0,1]: h^{\prime}(0)=h^{\prime}(1)=0\right\}$. Denote by $M_{b}$ and $M_{d}$ the respective multiplication operators for $0 \leqq b, d \in F$. Then (3.11) takes the abstract form
$$
\begin{aligned}
\dot{u}(t) & =\ddot{B} u(t)-M_{d} u(t)+M_{b} u(t-1) \\
u_{o} & =\dot{\psi} \in E .
\end{aligned}
$$

It is well-known that $B$ generates a positive contraction semigroup and has compact resolvent (see $A-I, 2.7$ ). The same is true for the operator $B:=\hat{B}-M_{d}(s e e ~ A-I I, ~ T h m .1 .29$ and Thm.1.30). Thus by the above results the solution semigroup of (3.11) is positive and its asymptotic behavior can be investigated by the "undelayed" equation
$$
\dot{u}(t)=\left(\ddot{B}+M_{h}\right) u(t) \text {, where } h:=b-d \text {. }
$$

Let $h(x)<0$ for all $x \in[0,1]$.
Then $s\left(\vec{B}+M_{h}\right) \leqq \max \{h(x): x \in[0,1 \eta\}<0$. Hence the solutions of (3.11) are uniformly exponentially stable.

Interpretation. The solution $u$ of (3.ll) can be interpreted as the density of a population, distributed over an "area" $[0,1]$.
The operator $\frac{\partial^{2}}{\partial^{2} X}$ describes the internal migration of the population and the functions $b$ and $d$ are the "place specific" birth- resp. death rate of the population members. The time delay 1 stands for the gestation period. The stability condition $h(x)<0$ for all $x \in$ $[0,1]$ means that the death rate has to majorize the birth rate in each spatial point to lead to extinction of the population, no matter whether the equation with or without delay is considered.

Example 3.12. An interesting example from cell biology is given by Gyllenberg-Heijmans (1985). They investigate a balance equation for the size distribution of a cell population which is structured by size. To point out the main ideas we will restrict the complex situation to the simple case of linear cell growth and refer to the original paper for details and the more general case.
Let $0 < r <1$ and let $a=r$ be the minimal cell size. Furthermore let $F=L^{1}([a, 1])$ and $E=C([-r, 0], F)$. The retarded differential equation of interest is the following,
$$
\begin{align*}
\frac{d}{d t} u(t) & =B u(t)+L u(t-r)  \tag{3.12}\\
u & =\Psi \in E .
\end{align*}
$$

Here $B f:=-f^{\prime}$ on $D(B)=\left\{f \in L^{1}[\alpha, I]: f \in A C[\alpha, I], f(\alpha)=0\right\}$ and L : F $\rightarrow \mathrm{F}$ is defined by
$$
L f(x)= \begin{cases}k(x) f(2 x-r) & \text { if } x \in[a, 1 / 2(r+1)], \\ 0 & \text { if } x \in(1 / 2(r+1), 1],\end{cases}
$$
where $k \in c[a, 1]$.
It is easy to verify that $I$ is positive and bounded, and that $B$ is the generator of the positive semigroup $(s(t))$ tso defined by
$$
\left[S(t) f(x)=\left\{\begin{array}{ll}
f(x-t) & \text { if } x-t \geqslant a \\
0 & \text { if } x-t<a
\end{array} \quad(x \in[\alpha, 1])\right.\right.
$$

Furthermore $B$ has compact resolvent. Define $\Phi f:=L(f(-r))$ for $f \in E$ such that (3.12) can be written as retarded Cauchy problem (RCP) .

As before (see Formula (3.3)) $\Phi_{\lambda}$ is defined by $\Phi_{\lambda} x:=\Phi_{\lambda}\left(\varepsilon_{\lambda} x_{x}\right)$ for $x \in F$. GyIlenberg and Heijmans have shown that $s\left(B+\Phi_{\lambda}\right)>-\infty$. Thus we can apply Thm. 3.7 and obtain that $s(A)=\lambda$ if and only if $\lambda=$ $s\left(B+\Phi_{\lambda}\right)$.

NOTES.

Section 1 , The coincidence of spectral bound and growth bound for positive semigroups on $C(K)$ was first observed by Derendinger (1980) and then generalized to C (X) and non-commutative $\mathrm{C}^{*}$-algebras by Batty-Davies (1982) and Groh-Neubrander (9981). The stability theorem 1. I is a continuous version of a result of choquetFoias (see Schaefer (1974), V.8.8).

Section 2. For the Riesz-Schauder Theory of compact operators we refer to DunfordSchwartz (1958), Sec.VII. 4 and Pietsch (1978), Sec. 26 . Theorem 1.1 sems to be folklore. Prop 2.3 is due to Grothendieck (1953) and can be found in Sec. II. 9 of Schaefer (1974). Proposition 2.4 is due to Dieudonne (see $\$ 3$ of Grothendieck (1953) and Schaefer (1974), II،Exc. 27). The notion 'strong Feller property' used in Theorem 2.5 is due to Girsanov (see Dynkin (1965)) while the theorem itself was proven by Davies (1982). It is well known that there is a close relationship between Markov processes and Markov semigroups. A description of this relation more derailed than Example 2.6 can be found e.g. In Dynkin (1965), in Chap. 2 of van Casterent (1985) or in Chap. 7 of Lamperti (1977). The notion "quasi-compact" for a single operator dates back to Eberlein (1949) (see also Yosida-Kakutani (1941) and Sec. 26.4 of Pietsch (1978)). Quasi-compactness for strongly continuous semigroups and its relationship to unifort ergodicity is invest fated in Lin (1975). Proposition 2.9 is due to Voigt (1980), a special case was proven by Vidav (1970). Corollaries 2.2 and 2.11 can be found in Greiner (1984). The criterion stated in (2.12) is known as 'Doeblin's condition' (see e.g. Yosida-Kakutani (1941)). It is sufficient and
necessary for quasi-compactness of the semigroup. A new proof of this result is given in lotz (1981).

Section 3. The standard reference to retarded differential equations is Hale (1977), where it is shown that the solutions of (RCP), with values in a finite dimensional space $F$, yield an operator semigroup. The extension to arbitrary Banach spaces $F$ was first made by Travis-Webb (1974). Plant (1977) showed the translation property ( $T$ ) for the solution semigroup. Among the many papers pursuing this functional analytic investigation of partial differential equations with delay we quote DiBlasio-Kunisch-Sinestrari (1984) and Kurisch-Schappacher (1983).
Our approach is essentially dae to $W$. Kerscher. We show that the first derivative with an appropriate domain is the generator of a one-parameter semigroup on an abstract function space. Due to the translation property this semigroup yields the solutions of (RCP).
The aspect of positivity in (RCP) and its influence on the stability of the solutions was first studied in Section 4 of Kerscher-Nagel (1984). In Kerscher (i986) this is pursued by showing how Theorem 3.7 in combination with the domination of semigroups (see G-II, Section 4) can be uged to derive many of the known "stability independent of the delay" - realts (e.g. Cooke-Ferreira (1983)).




Abraham, R.; Marsden, J.E.
[1978] Foundations of Mechanics. London-Amsterdam: Benj̧amin / Cummings 1978.

Abramovich. Y.A.
[1983] Multiplicative representation of disjointness preserving operators. Indag. Math. 45 (1983), 265-279.

Akemann, C.A.; Dodds, P.G.; Gamlen, J.L.B.
[1972] Weak compactness in the dual space of a wt-algebra. J. Funct. Anal. 16 (1972), 446-450.

Ando, T .
[1961] Convergent sequences of finitely additive measures. Pactfic J. Math. 11 (1961) * 395-404.

Albeverio, S.; Hoegh-Krohn, R.
[1978] Frobenius theory for positive maps on von Neumann algebras. Corm, Math. Phys. 64 (1978), 83-94,

Amann,
[1976] Fixed point equations and nonlinear eigenvalue problems in ordered Banach spaces. SIAM Rev. 18 (1976), 620-709.
[1983] Dual semigroups and second order linear elliptic boundary value problems. Israel J. MatK. 45 (1983), 225-254.

Arendt, W.
[1982] Kato's equality and spectral decomposition for positive $C_{o}$-groups. Manuscripta Math. 40 (1982), 277-298.
[1983] Spectral properties of Lamperti operators. Indiana Univ. Math. J. 32 (1983), 199-215.
[1984a] Generators of positive semigroups.
In: F. Kappel; W. Schappacher (eds.): Infinite-dimensional Systems, Retahof 1983. Lecture Notes in Math. 1076, 1-15. Berlin-HeidelbergNew York: Springer 1984.
[1984b] Kato's inequality. A characterization of generators of positive semigroups. Proc. Roy. Irish Acad. Sect. A 84 (1984), 155-174.
[1984c] Resolvent positive operators and integrated semigroups. Semesterbericht Funktionalanalysis, Ttibingen, Sommersemester 1984, 73-101.
[1985] Resolvent positive operatora. Universität Tibingen, Preprint 1985.

Arendt, $W_{.}$; Chernoff, P.; Kato, T.
[1982] A generalization of dissipativity and positive semigroups. J. Operator Theory 8 (1982), 167-180.

Arendt, W.: Greiner, G.
[1984] The spectral mapping theorem for one-parameter groups of positive operators on C (X).
Semigroup Forum 30 (1984), 297-330.

Arino, O.; Kimutuel, M.
[1985] Asymptotic analysis of a cell-cycle model based on unequal division. Preprint 1985.

Asimow, L.; Ellis, A.J.
[1980] Convexity Theory and its Applications in Functional Analysis. London-New York-San Trancisco: Academy c Press 1980.

Axmann, D.
[1980] Struktur- und Ergodentheorie irreduzibler Operatoren auf Banachverbänden. Dissertation, Tabingen 1980.

Baras $P_{+}$; Pierre M.
[1985] Critère d'existence de solutions positives pour des équations semi-linéaires non monotones.
Preprint. Nancy 1985.

Bart, f .
[1977] Periodic strongly continuous semigroups. Ant. Mat. Pura Appl. 115 (1977), 311-318.

Batty, C.J.K.
[1978] Dissipative mappings and well-behaved derivations.
J. London Math. Soc. 18 (1978), 527-533.
[1981] Derivations on compact spaces. Proc. London Math. Soc. 42 (1981), 299-330.

Batty, C.J.K+; Davies, E.B.
[1982] Positive semigroups and resolvents, J. Operator Theory 10 (1982), 357-363.

Batty, C.J.K.; Robinson, D.W.
[1984] Positive one-parameter semigroups on ordered spaces. Acta. Appl. Math. 2 (1984), $221-296$.
[1985] The characterization of differential operators by locality: abstract derivations.
Ergodic Theory Dynamical Systems 5 (1985), 171-183.
```
Bawer, H.
[1966] Garmonische Räume und ihre Potentialtheorie.
    Berlin-Heidelberg-New York: Springer 1966.
Beals, R.
[1972] On the abstract Gauchy problem.
    J. Funct. Ana1. 10 (1972), 281-299.
Belleni-Morante, A.
[1979] Applied Semigroups and Evolution Equations.
    Oxford: Oxford University Press 1979.
Bellmann, R.; Cooke, K.L.
[1963] Differential-Difference Equations.
    London-New York: Academic Press 1963.
Belyi, A.G.; Semenov, Y.A.
[1975] Kato's inequality and semigroup product-formulas.
    Functional Anal. Appl. 9 (1975), 320-32l.
Benchimol, C.D.
[1978a] A note on weak stabilizability of contraction semigroups.
    SIAM J. Control Optim. 16 (1978), 373-379.
[1978b] Feedback stabilizability in Hilbert spaces.
    App1. Math. Optim. 4 (1978), 223-248.
Benilan, P.; Picard, C.
[1979] Quelques aspects non lineaires du princtpe du maximum.
        In: S'minaire de Thëorie du Potentiel. Lecture Notes in Math. 713. Springer
        1979.
Berg, C.; Forst, G.
[1975] Potential Theory on Locally Compact Abelian Groups.
    Berlin-Heidelberg-New York: Springer 1975.
Berger, C.A.; Coburn, L.A.
[1970] One-parameter semigroups of isometries.
    Bul1. Amer. Math. Soc. 76 (1970), 1125-1129.
Beurling, A.
[1970] On analytic extensions of semigroups of operators.
    J. Funct. Anal. 6 (1970), 387-400.
Beurling, A.; Deny, J.
[1948] Espaces de Dirichlet I: Le cas èlëmentaire. Acta Math. 99 (1948), 203-224.
```

Di Blasio, G.; Kunisch, E.; Sinestrari, E.
[1983] The solution operator for a partial differential equation with delay. Acti Accad. Naz. Lincei Rend. C1. Sci. Fis. Mat. Natur. 74 (1983), 228-233.
[1984] Stability for abstract linear functional equations. To appear in: Israel J. Math.

Bony, J.-M.; Courrège, P.; Priouret, P.
[1968] Semi-groups de Feller sur une variété a bord compact et problèmes aux limites intégro-différentiels du second ordre donnant lieu au principe du max fumb.
Ant. Inst. Fourier (Grenoble) 18 (1968), 369-521.
Bourbaki, N.
[1955] Eléments des Mathématiques, Intégration, Chapitre 5: Intégration des Mesures.
Paris: Hermann 1955.

Bourgain, J.
[1980] Propriétés de rèlevement et projections dans les espace $L^{1} / H_{o}^{1}$ et $H^{00}$. C. R. Acad. Sci. Paris Sér. A-Math. 291 (1980), 607-609.
[1985] Some new properties of the Banach spaces $L / H_{o}^{1}$ and $H^{\infty}$ (Part II). Preprint 1985.

Boyadzhiev, $\mathrm{H} . \mathrm{N}$.
[1984] Characterization of the generators of $C_{o}$ semigroups which leave a convex set invariant. Cotmen. Math. Univ. Carolin. 25 (1984), 159-170.

Bratteli, O.; Digernes, T.; Robinson, D.W.
[1983] Fositive semigroups on ordered Banach spaces. J. Operator Theory 9 (1983), 371-400.

Bratteli, O.; Jorgensen, F.E.T.
[1984] Fositive Semigroups of Operators and Applications. Special issue of Acta Appl. Math. 2 (1984), Dordrecht / Boston: Reidel 1984.

Bratteli, O.; Kishimoto, A.; Robinson, D.W.
[1980] Positivity and monotonity properties of $C_{o}$-semigroups, I. Conm. Math. Phys. 75 (1980), 67-84.

Bratteli, O.; Robinson, D.W.
[1975] Unbounded derivations of C*-algebras. Corm. Math. Phys. 42 (1975), 253-268.
[1979] Operator Algebras and Quantum Statistical Mechanics I. New York-Heidelberg-Berlin: Springer 1979; II, ibid. 1981.
[1981] Positive C -semigroups on $\mathrm{C}^{*}$-algebras. Math. Scand. 49 (1981), 259-274.

Calvert, B.D.
[1970] Nonlinear evolution equations in Banach lattice. Bull. Ager. Math. Soc. 76 (1970), 845-850.
[1971a] Nonlinear equations of evolution.
Pacific J. Math. 39 (1971). 293-350.
[197lb] Semigroups on an ordered Banach space.
J. Math. Soc. Japan 23 (1971), 311-319.
[1972] On T-accretive operators.
Ann. Mat. Pura Appl. 94 (1972), 291-314.
Calvert, B.D.; Picard, C.
[1975] Opérateurs accrétifs et $\Phi$-accrétifs dans tu espace de Banach. Hiroshima Math. J. 5 (1975), 363-370.
van Casteren, J.
[1984] Invariant subsets of strongly continuous semigroups. Integral Equations Operator Theory 7 (1984), 884-892.
[1985] Generators of Strongly Continuous Semigroups. Boston-London-Melbourne: Pitman 1985.

Chicone, C.; Swanson, R.C.
[1981] Spectral theory for linearizations of dynamical sygtems. J. Differential Equations. 40 (1981), 155-167.

Choi, M, -D .
[1974] A Schwarz inequality for positive linear maps on ©*-algebras. Illinois J. Math. 18 (1974), 565-574.

Choquet, G.; Foias, C.
[1975] Solution d'un problème sur les itérés d"un operateur positif sur C(K) et propriétés des moyennes associées.
Ant. Inst. Fourier (Grenoble) 25 (1975), 109-125.
Coffman, C.V.; Grover, C.L.
[1980] Obtuse cones in Hilbert spaces and application to partial differential equations.
J. Funct. Anal. 35 (1980). 369-396.

Collatz, P.
[1942] Efnschließungssatz fir die charakteristischen Zahlen von Matrizen. Math. Z. 48 (1942), 221-226.

Combes, F.; Delaroche, C.
[1978] Representations des groupes localement compacts et applications aux algèbres d'opérateurs. Astërisque (Séminaire d'Orleans) 55 (1978).

Cooke, K.L.; Ferreira, J.M.
[1983] Stability conditions for linear retarded differential equations. J. Math. Anal. App1. 96 (1983), 480-504.

Coulhon, T.
[1984] Suites d'opérateurs sur un espace $C(K)$ de Grothendieck.
C. R. Acad. Sci. Paris Sér. I-Math. 298 (1984), I 3 -15.

Cornfeld, I.P.; Fomin, S.V.; Sinai, Ya,G.
[1982] Ergodic Theory. Berlin-Heide berg-New York: Springer 1982.

Crandall, M.G.; Tartar, L.
[1980] Some relations between nonexpansive and order preserving mappings. Proc. Amer. Math. Soc. 78 (1980), 385-390.

Datko, R.
[1970] Extending a theorem of A.M. Liapunov to Hilbert space. J. Math. Aral. App1. 32 (1970), 610-616.
[1972] Uniform asymptotic stability of evolutionary processes in a Banach space. SIAM J. Math. Anal. 3 (1972), 428-445.
[1983] An example of an unstable neutral differential equation. Internat. J. Control 38 (1983), 263-267.

Davies, E.B.
[1972] Some contraction semigroups in quantum probability. Z. Wahrsch. Verw. Gebiete 23 (1972), 261-273.
[1976] Quantum Theory of Open Systems. London-New York-San Francisco: Academic Press 1976.
[1979] Generators of dynamical semigroups. J. Funct. Ana1. 34 (1979), 421-431.
[1980] One-parameter Semigroups. London-New York-San Francisco: Academic Press 1980.
[1982] The harmonic functions of mean ergodic semigroups. Math. Z. 181 (1982), 543-552.
[1986] Spectral properties of some second order elliptic operators on $\mathrm{L}^{\mathrm{P}}$-spaces. In: R. Nagel; U. Schlotterbeck; M.P.H. Wolff (eds.): Aspects of Positivity in Functional Analysis. Austerdam: North Folland 1986.

Deimling, K.
[1977] Ordinary Differential Equations in Banach Spaces. Berlin-Heidelberg-New York: Springer 1977.

DeLeeuw, K.; Glicksberg, I.
[1961] Applications of almost periodic compactifications. Acta Math. 105 (1961), 63-97.

Derndinger, R .
[1980] Utber das Spektrum positiver Generatoren. Math. Z. 172 (1980), 281-293.
[1984] Betragshalbgruppen normstetiger Operatorhalbgruppen. Areh. Math. 42 (1984), 371-375.

Derndinger, R.; Nage1, R.
[1979] Der Generator starkstetiger Yerbandshalbgruppen auf $C(X)$ und dessen Spektrum.
Math. Ann. 245 (1979), 159-177.
Desch, W.; Schappacher, W.
[1983] Spectral properties of finite-dimensional perturbed linear semigroups. Universitat Graz, Preprint 1983.
[1984] On relatively bounded perturbations of linear $G$-semigroups. Ann. Scuola Norn. Sup. Pisa 11 (1984), 327-341.

Diekmann, O.; Heljmans, H.J.A.M.: Thieme, H.R.
[1984] On the stability of the cell size distribution.
J. Math. Bio1. 19 (1984), 227-248.

Dieudonnè, J.
[1971] Elements d'Analyse (Tome IV). Parts: Gauthier-Villars 1971.

Doetsch, $G$.
[1950] Gandbuch der Laplace Transformation, Band I , Basel: Birkhauser 1950.

Dorroh, J.R.
[1966] Contraction semi-groups in a function space. Pacific J. Math. 19 (1966), 35-38.

Dunford, N.; Schwartz; J.T.
[1958] Linear Operators, Part I: General Theory. New York: Wiley 1958.

Dynkin, E.B.
[1965] Markov Processes I , II. Berlin-Gbttingen-fieidelberg: Springer 1965.

Dyson, J.; Villella-Bressan R.
[1979] Semigroups of translations associated with functional and functional differential equations Proc. Roy. Soc. Edinburgh Sect. A 82 (1979), 171-188.

Eberlein, W.F.
[1948] Abstract ergodic theorems and weak almost periodic functions. Trans. Aner. Math. Soc. 67 (1948), $217-240$.

Elliot, G.
[1972] Convergence of automorphisms on certain C*-algebras.
J. Funct. Anal. 11 (1972), 204-206.

Evans, D.E.
[1976.1 On the spectrum of a one-parameter strongly continuous representation. Math. Scand. 39 (1976), 80-82.
[1977] Irreducible quantum dynamical semigroups. Conm. Math. Phys. 54 (1977), 293-297.
[1984] Quantum dynamical semigroups, symmetry groups, and locality. Acta. Appl. Math 2 (1984), 333-352.

Evans, D.E.; Hanche-Olsen, H.
[1979] The generators of positive semigroups. J. Funct. Anal. 32 (1979), 207-212.

Fattorini, H.O.
[1969a] Ordinary differential equations in linear topological spaces, $I$. J. Differential Equations 5 (1969), 72-105.
[1969b] Ordinary differential equations in linear topological spaces, II.
J. Differential Equations 6 (1969) , 50-70.
[1983] The Cauchy Problem.
Reading (Mass.): Addison-Wesley 1983.
Feller, w.
[1952] The parabolic differential equation and the associated semigroups of transformations.
Ann. of Math. 55 (1952), 468-519.
[1953a] On the generation of unbounded semigroups of bounded linear operators. Antr. of Math. 58 (1953), 166-174.
[1953b] On positivity preserving semigroups of transformations on $C\left[r_{1}, r_{2}\right]$. Ant. Soc. Math. Polon. 25 (1953), 85-94.
[1954a] The general diffusion operator of positivity preserving semigroups in one difmension.
Ann. of Math. 60 (1954), 417-436.
[1954b] Diffusion processes in one dimension.
Trans. Amer. Math. Soc. 77 (1954), 1-31.
[1955] On second order differential operators. Antr. of Math. 61 (1955), 90-105.
[1956] Boundaries induced by non-negative matrices. Trans. Amer. Math. Soc. 83 (1956), 19-54.
[1957] On boundaries defined by stochastic matrices. Applied probability. Froceedings of Symposia in Applied Mathematics, Vol. VII, 35-40, New York: McGraw Hill 1957.
[1959] Differential operators with the positive maximum property. Ilifnois J. Math. 3 (1959), 182-186.

Fisher, S.D.
[1983] Function Theory on Planar Domains. New York: Wiley 1983.

Foias, C .
[1973] Sur une question de M. Reghis. An. Univ. Timispoara Ser. Stint. Mat. 11 (1973), lll-114.

Frigerio, A.: Verri, M.
[1982] Long-time asymptotic properties of dynamical semigroups on $\mathrm{W}^{*}$-algebras. Math. Z. 180 (1982), 275-286.

Frobenius, $G$.
[1909] tiber Matrisen aus positiven Elementen. Sitzungsber. Preuß. Akad. Wiss., Physikal.-Math. Kl. (1908). 47l-476; 1bid. (1909), 514-518.

Fukushima, M.
[1982] Dirichlet Forms and Markov Frocesses. London: North Holland 1980.

Gearhart, L.
[1978] Spectral theory for contraction semigroups on hilbert spaces. Trans. Amer. Math. Soc. 236 (1978), 385-394.

Gilbarg, D.; Trudinger, N.S.
[1977] E111ptic Partial Differential Equations of Second Order. Berlin: Springer 1977.

Goldstein, J.A.
[1981] Some developments in semigroups since Hille Fhillips. Integral Equations Operator Theory 4 (1981), 350-365.
[1985a] Semigroups of Operators and Applications. Onford University Press 1985.
[1985b] A (more-or-less) complete bibliography of semigroups of operators through 1984. Preprints and Lecture Notes in Mathematics. Tulane University 1985.
[1986] Asymptotics for bounded semigroups in filbert spaces. In: R. Nagel; t. Schlotterbeck; M.P.K. Wolff (eds.): Aspects of Positivity in Functional Analysis. Ansterdam: North folland 1986.

Greiner: G.
[1981] Zur Ferron-Frobenius Theorie stark stetiger Halbgruppen. Math. Z. 177 (1981), 401-423.
[1982] Spektrum und Asymptotik stark stetiger Halbgruppen positiver Operatoren. Sitzungsber. Heidelb. Akad. Wiss., Math.-Naturwiss. K1. (1982) 55-80.
[1984a] A typical Perron-Frobenfus theorem with applications to an age-dependent population equation.
In: F. Kappel; W. Schappacher (eds.): Infinite-dimensional Systems, Retzhof 1983. Lecture Notes in Math. 1076, 86-100. Berlin-HeidelbergNew York: Springer 1984.
[1984b] Spectral properties and asymptotic behavior of the linear transport equation. Math. Z. 185 (1984), 167-177.
[1984c] A spectral decomposition of strongly continuous groups of positive operators.
Quart. J. Oxford (2) 35 (1984), 37-47.
[1984d] An irreducibility criterion for the linear transport equation. Semesterbericht Funktionalanalysis, Tubingen, Sommersemester 1984, 1-8.
[1985] Some applications of Fejer's theorem to one-parameter semigroups. Preprint 1985.
[1986] Perturbing the boundary conditions of a generator. To appear in: fouston J. Math.

Greiner, G.; Nagel, R.
[1982] La loi "zero ou deux" et ses conséquences pour le comportement asymptotique des opérateurs positifs. J. Math. Pures App1. 9 (1982), 261-273.
[1983] Of the stability of strongly continuous semfgroups of positive operators on $L^{2}(\mu)$.
Ann. Scuola Norm. Sup. Pisa 10 (1983), 257-262.
Greiner, G.; Voigt, J.; Wolff, M.P.K.
[1981] On the spectral bound of the generator of semigroups of positive operators. J. Operator Theory 5 (1981), 245-256.

Groh, T,
[1981] The peripheral point spectrum of Schwarz operators on $\mathrm{C}^{*}$-algebras Math. Z. 176 (1981), 311-318.
[1982a] Some observations on the spectra of positive operators on finite dimensional $C^{*}$-algebras.
Linear Algebra Appl. 42 (1982), 213-222.
[1982b] Asymptotic behavior of dynamical systems on w*-algebras. Semesterbericht Funktionalanalysis, Tübingen, Sonnersemester 1982, 15-25.
[1984a] Uniformly ergodic maps on $\mathrm{C}^{*}$-algebras. Israe1 J. Math. 47 (1984), 227-235.
[1984b] Uniform ergodic theorems for identity preserving Schwarz maps on W*-algebras.
J. Operator Theory 11 (1984), 395-404.
[1984c] Spectrum and asymptotic behaviour of completely positive maps on $B(i)$. Math. Japonica 29 (1984), 395-402.

Groh, U.; Kimmerer, B.
[1982] Bibounded operators on $W^{*}$-algebras. Math. Scand. 50 (1982), 269-285.

Groh, U.; Netubrander, F.
[1981] Stabilitht starkstetiger positiver Operatorhalbgruppen auf $C^{*}$-Algebren. Math. Ann. 256 (1981), 129-173.

Grothendieck, A.
[1953] Sur les applications linéaires faiblement compactes d"espaces du type $C(K)$. Canadian J. Math, $\underline{5}$ (1953), 129-173.

Gustafson, K ; Lumer, G .
[1972] Multiplicative perturbation of semigroup generators. Pacific J. Math. 41 (1972), 731-742.

Gyllenberg, M.; Heijanans, H.J.A.M.
[1985] An abstract delay equation modelling size dependent cell growth and division. Preprint 1985.

Hadeler, K.-P.
[1978] Delay-equations in biology.
In: H. -0 . Peitgen; H.-O. Walther (eds.) Functional Differential Equations and Approximation of Fixed Points, Bonn 1978. Lecture Notes in Math. 730, 136-156. Berlin-Heidelberg-New York 1978.

Hale, J.
[1977] Theory of Functional Differential Equations.
New York-Heidelberg-Berlin: Springer 1977.
Hamel, G.
[1905] Eine Basis aller Zahlen und die unstetigen Lösungen der Funktionalgleichung: $f(x+y)=f(x)+f(y)$.
Math. Ann. 60 (1905), 459-462.

Hasegawa, M.
[1966] On contraction semigroups and (di)-operators. J. Math. Soc. Japan $18(1966)$, $290-302$.

Heijmans, H.J.A.M.
[1985a] Structured populations, linear semigroups and positivity. To appear in: Math. Z.
[1985b] An eigenvalue problem related to cell growth. J. Math. Anal. App1. 111 (1985), 253-280.
[1986] The dynamical behavior of the agemsize distribution of a cell population. In: J.A.J. Metz; O. Diekmann (eds.) Dynamics of Physiologically structured Population. Springer Lecture Notes Biomathematics (to appear).

Hempel, R.: Voigt, J.
[1985] The spectrumt of a Schrodinger operator in $L_{p}\left(P^{v}\right)$ is $p$-independent. Preprint. Minchen 1985.

Herbst, I.W.
[1982] Contraction semigroups and the spectrum of $A_{1} I+I_{2} A_{2}$.
J. Operator Theory 7 (1982), 61-78.
[1983] The spectrum of Hilbert space semigroups. J. Operator Theory 10 (1983), 87-94.

Herbst, I.W.; Sloan, A.D.
[1978] Pertprbation of translation invariant positivity preserving semigroups on $L^{2}\left(\mathbb{R}^{k}\right)$.
Trans. Amer. Math. Soc. 236 (1978), 325-360.
Hess, H.; Kato, T.
[1980] On some linear and nonlinear eigenvalue problems with an infinite weight function.
Cotum. Partiell Differential Equations 5 (1980), 999-1030.
Hess, H.; Schrader, R+; Uh1enbrock. D.A.
[1977] Domination of semigroups and generalization of Kato's inequality. Duke Math. J. 44 (1977), 893-904.

Hewitt, E.; Ross, K.A.
[1963] Abstract Harmonic Analysis I. Berlin-Heidelberg-New York: Springer 1963.

Hiai, F.
[1978] Weakly mixing properties of semigroups of linear operators. Kodai Math, J. 1 (1978), 376-393.

Hille, E,
[1948] Functional Analysis and Semigroups.
Amer. Math. Soc. Coll. Pub1. 31, Providence (R.I.) 1948.
[1952] Une généralisation du probleme de Cauchy. Ann. Inst. Fourier (Grenoble) 4 (1952), 31-48.

Gille, E.; Phillips, R.S.
[1957] Functional Analysis and Semigroups. Amer. Math. Soc. Co11. Pub1. 31, Providence (R.I.) 1957.

Hirsch, M.W.; Smale, S.
[1974] Differential Equations, Dynamical Systems and Linear Algebra. New York: Academic Press 1974.

Howland, J.S.
[1984] On a theorem of Gearhart. Integral Equations Operator Theory 7 (1984), 138-142.

D'Jacenko, S.V.
[1976] Semfgroups of almost negative type and their applications. Soviet Math. Dok1. 17 (1976), 1189-1193.

Jacobs, K.
[1972] Gleichverteilung mod 1 . Selecta Math. IV, 57-93, Berlin-Heidelberg-New York: Springer 1972.

Jameson, G.J.0.
[1974] Topology and Normed Spaces. London: Chapman / Hall 1974.

Jorgensen, P.T.
[1980] Monotone convergence of operators semigroups and the dynamics of infinite particle systems. Aarhus Universitet, Preprint 1980.

Junghenn, H. D.
[1971] Almost periodic compactifications and applications to one parameter semigroups. Doctoral Dissertation, The George Washington Universtity 1971.

Kadison, R.V.
[1965] Transformations of states fin operator theory and dynamics. Topology 3 (1965), 177-198.

Ka11man, R.R.
[1969] Unitary groups and automorphisms of operator algebras. Amer. J. Math. 91 (1969), 785-806.

Kamke, E.
[1932] Zur Theorie der Systeme gewönlicher Differentalgleichungen II. Acta Math. 58 (1932) , 57-85.

Kaper, H.G.; Lekkerkerker, C.G.; Hejtmanek. J.
[1983a] Spectral Methods in Linear Transport Theory. Basel: Birkhäuser 1982.
[1983b] Recent progress on the reactor problem of linear transport theory. Argonne National Laboratory. Preprint 1983.

Karlin, S.
[1959] Positive operators.
J. Math. Mech. 8 (1959), 907-937.

Kato, T.
[1966] Perturbation Theory for Linear Operators 1966.
$2^{\text {nd }}$ printing: Berlin-heidelberg-New York: Springer 1976.
[1973] Schrödinger operators with singular potentials. Israel J. Math. 13 (1973), 135-148.
[1982] Superconvexity of the spectral radius, and convexity of the spectral bound and the type.
Math. Z. 180 (1982), 265-273.
[1986] $\mathrm{L}^{\text {P }}$-Theory of $\mathrm{Schrödinger} \mathrm{operators} \mathrm{with} \mathrm{a} \mathrm{singular} \mathrm{potential}$.
In: R. Nagel; U. Schlotterbeck; M.P.H. Wolff (eds.): Aspects of Positivity in Functional Analysis. Amsterdam: North Folland 1986.

Katznelson, Y.; Tzafriri, L.
[1984] On power bounded operators. Hebrew University, Jerusalett, Preprint 1984.

Kerscher, $W$.
[1986] Retardierte Cauchy Probleme: Ordnungseigenschaften und Stabilität unabhägig von der Verz: 名erung. Dissertation, Universităt Tübingen 1986.

Kerscher, W.; Nagel, R.
[1984] Asymptotic behavior of one-parameter semigroups of positive operators. Acta Appl. Math. 2 (1984), 297-309.

Kipnis, C.
[1974] Majoration des semi-groupes de contractions de $\mathrm{L}^{\mathrm{l}}$ et applications. Ann. Inst. F. Poincaré (Sect. B) 10 (1974), 369-384.

Kishimoto, A.; Robinson, D. W.
[1980] Fositivity and monotonicity properties of $C_{o}$-semigroups, II. Comm. Math. Phys. 75 (1980), 85-101.
[1981] Subordinate semigroups and order properties. J. Austral. Math. Soc. Ser. A 31 (1981), 59-76.

Kleìn, A.; Landau, L.J.
[1975] Singular perturbations of positivity preserving semigroups via path space techniques.
J. Funct. Anal. 20 (1975), 44-82.

Klein, I.
[1984] Zur Spektraltheorie positiver Halbgruppen auf geordneten Banachraumen. Dissertation, Universitat Tibingen 1984.

Komatsu, H.
[1969] Fractional powers of operators III, Negative powers. J. Math. Soc. Japan 21 (1969), 205-228.

Konishi, Y.
[1971] Nonlinear semigroups in Banach lattices. Froc. Japan Acad. Ser. A Math. Sci. 47 (1971), 24-28.

Krasnose1'skit, M. A.
[1964] Positive Solutions of Operator Equations. Groningen: Noordhoff 1964.

Krein, S.G.
[1971] Linear Differential Equations in Banach Spaces. Amer. Math. Soc. Trans1. 29, Providence (R.I.) 1971.

Krein, S.G.; Khazan, M.I.
[1985] Differential equations in a Banach space. J. Soviet Math. 30 (1985), $2154-2239$.

Kreiss, H.O.
[1958] Uber sachgemăsse Cauchyprobleme fir Systeme von linearen partiellen Differentialgleichungen.
TRITA-NA, Roy. Inst. Technol., Stockholm 127 (1958).
[1959] tber Matrizen die beschraznkte Halbgruppen erzeugen. Math. Scand. 7 (1959), 71-80.

Krengel, ©.
[1985] Ergodic Theorems. Berlin, New York: de Gruyter 1985.

Kubokawa, Y.
[1975] Ergodic theorems for contraction semigroups. J. Math. Soc. Japan 27 (1975), 184-193.

Kümmerer, B.; Nage1, R.
[1979] Mean ergodic semigroups on $\mathrm{W}^{*}$-algebras. Acta Sci. Math. 41 (1979), 151-159.

Kuhn, K.
[1984] Elliptische Differentialoperatoren als Generatoren auf C( $\Omega$ ). Semesterbericht Funktionalanalysis, Tïbingen, Wintersemester 1984/1985, 125-142.

Kunisch, K.; Schappacher, W.
[1983] Necessary conditions for partial differential equations with delay to generate C -semigroups.
J. Differential Equation 50 (1983), 49-79.

Kunita, 포.
[1969] Sub-Markov semi-groups in Banach lattices. Proc. of the Conference on Funct. Anal. and Related Topics, 332-343. Tokyo Press 1969.

Kurose, H.
[1981] An example of a non quasi well-behaved derivation on $C(I)$. J. Funct. Anal. 43 (1981), 193-201.
[1982] On a closed derivation in $\mathrm{C}(\mathrm{I})$.
Mem. Fac. Sci. Kyushu Univ. Ser. A Math. 36 (1982), 193-198.
[1983] Closed derivations in $C(I)$. Tohoku Math. J. 35 (1983), 341-347.

Lamperti, J.
[1977] Stochastic Processes. Berlin-Heidelberg-New York: Springer 1977.
de Laubenfels, R.
[1984] Well behaved derivation on c[0,1].
Pacific J. Math. 115 (1984), 73-80.

Leader, s.
[1954] On the infinitesimal generators of a semigoups of positive transformations with local character condition.
Proc. Aner. Math. Soc. 5 (1954), 401-406.
Lin, M.
[1974] On the uniform ergodic theorem II. Proc. Amer. Math. Soc. 46 (1974), 217-225.
[1975] Quasicompactness and uniform ergodicity of Markov operatore. Ann. Inst. H. Poincaré (Sect. B) 11 (1975), 345-354.

Lin, M.; Montgomery, J.; Sine R.
[1977] Change of velocity and ergodicity in flows and in Markov semi-groups. Z. Wahrsch. Verw. Gebiete 39 (1977), 197-2fl.

Lindblad, G.
[1976] On the generators of quantum dynamical semigroups. Comm. Math. Phys. 48 (1976), 119-130.

Lindenstrauss, J.; Tzafriri, L.
[1979] Classical Banach Spaces II, Function Spaces. Berlin-Heidelberg-Now York: Springer 1979.

Lotz, H.P.
[1981] Uniform ergodic theorems for Markov operators on $C(X)$. Math. Z. 178 (1981), 145-156.
[1982] Uniform convergence of operators on $L^{\infty}$. Semesterbericht Funktionalanalysis, Tübingen, Wintersemester 19882/1983.
[1984] Tauberian theorems for operators on $L^{\infty}$ and similar spaces. In: K.D. Bierstedt; E. Fuchssteiner (eds.) Functional Analysis, Surveys and Recent Results III. Amsterdam: North Holland 1984.
[1985] Uniform convergence of operators on $L^{\text {m }}$ and similar spaces. Math. Z. 190 (1985), 207-220.
[1986] Positive linear operators on $L^{\mathrm{P}}$ and the Doeblin condition. In: R. Nage1; U. Schlotterbeck; M.P.H. Wolff (eds.): Aspects of Positivity in Functional Analysis. Arsterdam: North Holland 1986.

Lumer, G .
[1974a] Perturbations de générateurs infinitesimaux du type "changement de temps". Ann. Inst. Fourier (Grenoble) 23 (1974), 271-279.
[1974b] Problème de Cauchy pour opérateurs locaux et "changement de temps". Ann. Inst. Fourier (Grenob1e) 23 (1974), 409-466.

Lumer, G.; Phillips, R.s.
[1961] Dissipative operators in a Banach space. Pacific J. Math. 11 (1961), 679-698.

Lumemburg, W.A.J.
[1979] Some Aspects of the Theory of Riest Spaces. The Undversity of Arkansas Lecture Notes in Mathematics 4, Fayetteville 1979.

Majewski, A.; Robinson, D.W.
[1983] Strictly positive and strongly positive semigroups.
J. Austra1. Math. Soc. Ser. A 34 (1983), 36-48.

Miller, J.; Strang, G.
[1966] Matrix theorems for partial differential and difference equations. Math. Scand. 18 (1966), 113-133.

Miller, R.K.
[1974] Linear Volterra integro-differential equations as semigroups. Funke 1a1, Ekvac. 17 (1974), 39-55.

Mil'stein, G.N.
[1975] Exponential stability of positive semigroups in a linear topological space I,II. Soviet. Math. 19 (1975), 35-42, 51-61.

Miyadera, I.
[1952] Generation of a strongly continuous semigroup of operators. Tôhoku Math. J. 4 (1952), 109-114.

Miyajima, $s$.
[1986] Generators of positive $C_{0}$-semigroups. In: R. Nage1; U. Schlotterbeck; M.P.H. Wolff (eds.) : Aspects of Positivity in Functional Analysis. Amsterdam: North Holland 1986.

Miyajima, S.; Okazawa, N.
[1984] Generators of positive $C_{0}$-semigroups on Banach lattices. Preprint 1984.

Montgomery, D.; Zippin, L.
[1955] Topological Transformation Groups.
New York: Interscience Publishers 1955.

Moreau, J.J.
[1966] Fonctionelles convexes.
Séminaire sur les équations aux derivées partielles. Collège de France 1966-67.

Nage1, R.
[1973] Mittelergodische Halbgruppen 1inearer Operatoren. Ann. Inst. Fourier (Grenoble) 23 (1973), 75-87.
[1983] Sobolev Spaces and Semigroups. Semesterbericht Funktionalanalysis, Tübingen, Sommersemester 1984, 1-19.
[1984] What can positivity do for stability?
In: K.D. Blerstedt: B. Fuchssteiner (eds.): Functional Analysis, Surveys and Recent Results III. Amsterdam: North Holland 1984.
[1985] Well-posedness and positivity for systems of linear evolution equations. Conferenze del Seminario di Matematica dell'Universita di Bari 203 (1985), 1-29.

Nage1, R.; Derndinger, R.; Palm, G.
[1982] Ergodic Theory in the Functional Analytic Perspective. Titbingen 1982.

Nagel, R.; Uhlig, H.
[1981] An abstract Kato inequality for generators of positive semigroups on Banach 1attices.
J. Operator Theory 6 (1981) . 113-123.

Nakano, H .
[1950] Modern Spectral Theory. Tokyo Mathematical Book Series. Vol. II. Maruzen Co.: Tokyo 1950.

Neubrander, F.
[1984a] Well-posedness of abstract Cauchy problems. Semigroup Forum 29 (1984), 75-85.
[1984b] We11-posedness of higher order abstract Cauchy problems. Dissertation, Universitat Tubingen 1984.
[1985a] Laplace transform and asymptotic behavior of strongly continuous semigroups. To appear in: Houston J. Math.
[1985b] Asymptotic behavior of solutions of inhomogeneous abstract Cauchy problems. In: Froc. Conf. Physical Math. and Nonlinear Fart. Differential Equatfons, Morgantown 1983, 157-73. Marcel Dekker 1985.
[1986] We11-posedness of higher order abstract Cauchy problems. To appear in: Trans. Amer. Math. Soc.

Nussbaum, R.D.
[1984] Fositive operators and elliptic eigenvalue problems. Math. Z. 186 (1984), 247-264.

Okazawa, N.
[1984] An Letheory for $^{\text {P }}$-hrodinger operators with nonnegative potentials. J. Math. Soc. Japan 36 (1984), 675-688.

Olesen, D.; Federsen, G.K. Takesaki, M.
[1980] Ergodic actions of compact Abelian groups. J. Operator Theory 3 (1980), 237-269.

Oseledets, V.I.
[1984] Completely positive linear maps, non Hamiltonfan evolution and quantum stochastic processes.
J. Soviet Math. 25 (1984), 1529-1557.
de Pagter, B.
[1984] A note on disjointness preserving operators. Proc. Auer. Math. Soc. 90 (1984), 543-550.
[1986] Irreducible compact operators. To appear In: Math. Z.

Pazy, A.
[1968.] On the differentiability and compactness of linear operators. J. Math. Mech. 17 (1968), I131-1142.
[1983] Semigroups of LInear Operators and Applications to Partial Differential Equations. Berlin- Heidelberg-New York-Tokyo: Springer 1983

Pedersen, G.K.
[1979] C*-Algebras and their Automorphism Groups. London, New York, San Francisco: Academic Press 1979.

Peetre, J.
[1959] Une charactérisation abstraite des opérateurs differentiels. Math. Scand. 7 (1959), 211-218; et: Rectification à 1'article précédent. Math. Scand. $\overline{8}$ (1960), E16-120.

Perron. 0.
[1907] Zur Theorie der Matrices.
Math. Ann. 64 (1907), 248-263.
Phillips, R.s.
[1954. A note on the abstract Caschy problem. Proc. Nat. Acad. Sci. U.S.A. 40 (1954), 244-248.
[1962] Semigroups of positive contraction operators. Czechoslovak Math. J. 12 (1962), 294-313.
[1974] Perturbation theory for semi-groups of 1inear operators. Trans. Amer. Math. Soc. 74 (1974), 343-369.

Picard, C.
[1972] Opérateurs $\phi$-accretifs et gënération des semi-groupes non linéaíres. C. R. Acad. Sci. Paris Sér. I-Math. 275 (1972), 639-641.

Fietsch, A.
[1978] Operator Ideals. Berlin: VEB Deutscher Verlag der Wissenschaften 1978.

Plant, A.T.
[1977] Nonlinear semigroups of linear operators and applications tn Banach spaces. J. Math. Anal. Appl. 60 (1977), 67-74.

Protter, M.H.; Weirberger, H.F.
[1967] Maximu Principles in Differential Equations.
New York-Berlin-Heidelberg: Springer 1984.

Prǘn, J.
[1981] Equilibrium solutions of age-specific population dynamics of several species.
J. Math. Bio1. 11 (1981) ) 65-84.
[1984] On the spectrum of $\mathrm{C}_{0}$-semigroups. Trans. Amer. Math. Soc. 284 (1984), $847-857$.

Rao, A.S.; Hengartner, W.
[1974] On the existence of a unique almost periodic solution of an abstract differential equation.
J. London Math. Soc. $\underline{8}(1974), 577-581$.

Reed, M. ; Simon. B.
[1975] Methods of Modern Mathematical Fhysics II. Fourier Analysis, Self-Adjointness.
New York: Academic Press 1975.
[1978] Methods of Modern Mathematical Physics IV. Analysis of Operators. New York: Academic Press 1978.
[1979] Methods of Modern Mathematical Physics III. Scattering Theory. New York: Academic Press 1979.

Reich, S.
[1981] A characterization of nonlinear $\phi$-accretive operators. Manuscripta Math. $3 \underline{6}$ (1981), 163-178.

Robinson, D.W.
[1977] The approximation of flows. J. Funct. Ana1. 24 (1977), 280-290.
[1982] Strongly positive semigroups and faithful invariant states. Comm. Math. Fhys. 85 (1982), 129-142.
[1983] Continuous semigroups on ordered Banach spaces.
J. Funct. Anal. 51 (1983), 268-284.
[1984] On positive semigroups.
Publ. Res. Inst. Math. Sct. 20 (1984), 213-224.
[1985] Differential operators on C*-algebras. Preprint, Canberra 1985.

Robinson, D. W.; Yamamuro, S.
[1983] The canonical half-norm, dual half-norms, and monotonic norms. Tôhuku Math. J. 35 (1983), 375-386.
[1984] Hereditary cones, order ideals and half-norms. Pacific J. Math. 110 (1984), 335-343.

Roth, J. P.
[1976] Opérateurs dissipatifs et semigroupes dans les espaces de fonctions continues.
Ann. Inst. Fourter (Grenoble) 26 (1976), 1-97.
[1978] Les operateurs elliptiques comme générateurs infinitésimaux de semigroups de Feller.
In: F.Hirsch; G.Mokobodzki (eds.): Séminaire de Théorie du Potential, Paris No. 3 . Lecture Notes in Math. 681, 234-251. Berlin-Iteidelberg-New York: springer 1978.

Sacker,R.J.; Sell, G.R.
[1978] A spectral theory for linear differential systems. J. Differential Equations 27 (1978), 320-358.

Sakai, S.
[1971] C*-Algebras and $W^{*}$-Algebras. Berlin-Heiderberg-New York: Springer 1971.

Sato, K.I.
[1968] On the generators of non-negative contraction semigroups in Banach lattices. J. Math. Soc. Japan 20 (1968) , 423-436.
[1970a] On dispersive operators in Banach lattices. Pacific J. Math. 33 (1970), 429-443.
[1970b] Positive pseudo-resolvents in Banach lattices. J. Fac. Sci. Univ, Tokyo Sect. I A Math. 17 (1970), 305-313.

Sawashima, I.
[1964] On spectral properties of some positive operators.
Natur. Sci. Rep. Ochanomizu Univ. 15 (1964), 53-64.
Scarpellini, B.
[1974] On the spectra of certain semigroups. Math. Ann. 2Il (1974), 323-336.

Schaefer, H. H ,
[1966] Topological Vector Spaces 1966.
$4^{\text {th }}$ printing: New York-Heidelberg-Berlin: Springer 1980.
[1968] Invariant ideals of positive operators in C(X), II. Illinois J. Math. 12 (1968), 525-538.
[1974] Banach Lattices and Positive Operators. New-York Heidelberg-Berlin: Springer 1974.
[1980] Ordnungsstrukturen in der Operatorentheorie. Jahresber. Deutsch. Math,-Verein. 82 (1980), 33-50.
[1982] Some recent results on positive groups and semi-groups. In: C.R. Huijsmans; M.A. Kaashoek; W.A.J. Luxemburg; W.K. Vietsch (eds.): From A to Z, Proc. Symp. In Honour of A.C. Zaanen, Leiden 1982. Mathematical Centre Tracts 149, 69-79, Amsterdam: 1982.
[1985] Existence of spectral values for irreducible $\mathrm{C}_{0}$-semigroups. Tübingen, Preprint 1985.

Schaefer, H. H.; Wolff, M.P.H.; Arendt, W.
[1978] On lattice isomorphisms with positive real spectrum and groups of positive operators.
Math. Z. 164 (1978), 115-123.
Schep, A.R.
[1985] Weak Kato-inequalities and positive semigroups.
Math. Z. 190 (1985), 305-314.

Seever, G.L.
[1973] Measures on F-spaces.
Trans. Amer. Math. Soc. 133 (1973), 267-280.
Semadeni, Z.
[1971] Banach Spaces of Continuous Functions.
Warszawa: Polish Scientific Publishers 1971.

Simon, B.
[1973] Ergodic semigroups and positivity preserving self-adjoint operators. J. Funct. Ana1. 12 (1973), 335-339.
[1977] An abstract kato's inequality for generators of positivity preserving semigroups.
Indiana Univ. Math. J. 26 (1977), 1067-1073.
[1979] Kato's inequality and the comparison of semigroups. J. Funct. Ana1. $32(1979)$, 97-101.
[1982] Schrodinger semigroups. Bull. Amer. Math. Soc. 7 (1982), 447-526.

Slemrod, M.
[1976] Asymptotic behavior of $C_{o}$-semigroups as determined by the spectrum of the generator.
Indiana Univ. Math. J. 25 (1976), 783-892.

Stern, R.J.
[1982] A note on positively invariant cones. Appl. Math. Optim. 9 (1982), 67-72.

Stewart, H.B.
[1974] Generation of analytic semigroups by strongly elliptic operators. Trans. Amer. Math. Soc. 199 (1974), 141-162.
stormer, E .
[1972] On projection maps on von Neumann algebras.
Math. Scand. 50 (1972), 42-50.

Takesaki, M.
[1979] Theory of Operator Algebras I.
New York-Heidelberg-Berlin: Springer 1979.

Travis, C.; Webb, G.F.
[1974] Existence and stability for partial functional differential equations. Trans. Amer. Math. Soc. 200 (1974), 395-418.

Triggiani, R.
[1975a] Pathological asymptotic behavior of systems in Banach spaces.
J. Math. Anal. App1. 49 (1975), 411-429.
[1975b] On the stabilizability problem in Banach spaces.
J. Math. Anal. App1. 52 (1975), 383-403.

Trotter, H. F.
[1974] Approximation and perturbation of semigroups. In: Butzer, Sz.-Nagy: Lineare Operatoren und Approximation II, Proceedings on a Conference in Oberwolfach 1974. Birkhäuser 1974.

Uh1ig, 보․
[1979] Derivationen und Yerbandshalbgruppen. Dissertation, Tübingen 1979.

Vidav, I.
[1970] Spectra of perturbed semigroups with applications to transport theory. J. Math. Anal. Appl. 30 (1970), 264-279.

Villella-Bressan R.
[1985] Functional equation of delay type in $L^{1}$-spaces. Ann. Polon. Math. 45 (1985), 93-104.

Voigt, J.
[1980] A perturbation theorem for the essential spectral radius of strongly continuous semigroups. Monatsh. Math. 90 (1980) , 153-161.
[1982] On the abszissa of convergence for the Laplace transform of vector valued measures.
Arch. Math. (Basel) 39 (1982), 455-462.
[1984a] Positivity in time dependent linear transport theory. Acta Appl. Math. 2 (1984), $31 \mathrm{l}-331$.
[19846] Spectral properties of the neutron transport equations. To appear in: J. Math. Anal. Appl.
[1984c] Absorption semigroups, their generators and Schredinger semigroups. Preprint 1984.
[1984d] On substochastic C -semigroups and their generators. Semesterbericht Funktionalanalysis, Tibingen, Wintersemester 1984/1985, 71-85.
[1985] Interpolation for positive $C$-semigroups on $L^{\text {Prospaces. }}$ Math. Z. 188 (1985), 283-286.

Watanabe, S.
[1982] Asymptotic behaviour and eigenvalues of dynamical semigroups on operator algebras.
J. Math. Anal. Appl. 86 (1982), 411-424.

Webb, G.F.
[1977] Woltera integral equations and nonlinear semigroups. Nonlinear Analysis $\underline{1}$ (1977), 415-427.
[1984] A semigroup approach to the Sharpe-Lotka theorem. In: F. Kappe1; W. Schappacher (eds.): Infinitemimensional Systems, Retzhof 1983. Lecture Xotes in Math. 1076, 254-268. Berlin-HeidelbergNew York: Springer 1984.
[1985a] Theory of Nonlinear Age-Dependent Population Dynamics. New York: Marcel Dekker 1985.
[1985b] An operator-theoretic formulation of asynchronous exponential growth. Preprint 1985.

Widder, D.V.
[1946] The Laplace Transform. Princeton (d.J.): Frinceton University Press 1946.
[1971] An Introduction to Transform Theory. New York: Academic Press 1971.
[1971] An Introduction to Transform Theory. New York: Academic Press 1971.

Wielandt H .
[1950] Unzerlegbare, nicht-negative Matrizen. Math. Z. 52 (1950), 642-648.

Winkler, $W$.
[1973] A note on continuous one-parameter zero-two law. Ann. Prob. 1 (1973), 341-344.

Wolff, M.P.H.
[1978] On $C_{0}$-semigroups of lattice homomorphisms on a Banach lattice. Math. 2. 164 (1978), 69-80.
[1981] A remark on the spectral bound of the generator of a semigroup of positive operators with application to stability theory.
In: P.L. Butzer, B. SZ.-Nagy, E. Gorlich (eds.): Functional Analysis and Approximation. Proc. Conf. Oberwolfach 1980, 39-50. Basel-Boston-Stuttgart Btrkhひuser 1981.

Yamanturo, S.
[1984] A note on positive semigroups. Preprint, Canberra 1984.
[1985] Absolute values in orthogonally decomposable spaces. Bull. Australian Math. Soc. 31 (1985), 215-233.

Yosida, K.
[1948] On the differentiability and representation of one-parameter semi-groups of 1inear operators.
J. Math. Soc. Japan 1 (1948), 15-21.
[1965] Functional Analysis 1965.
$6^{\text {th }}$ printing: Berlin-Heidelberg-New York: Springer 1980.
Yosida, K.; Kakutani, S.
[1941] Operator-theoretical treatment of Markoff's process and mean ergodic theorem.
Ant. of Math. 42 (1941), 188-228.

Zaanen, A.C.
[1983] Riesz Spaces II.
Groningen: North Holland 1983.

Zabezyk. J.
[1975] A note on $C_{0}$-semigroups. Bull. Acad. Polon. Sci. 23 (1975), 895-898.
[1979] Stabilization of boundary control systems.
Int. Symp. Systems Opt. Anal. 1978, Lecture Notes Control Theory Inform. Berlin-Hejdelberg-New York: Springer 1979.

Zaidman, S.D.
[1979] Abstract Differential Equations. London: Pitman 1979.

TABLE OF SYMBOLS
\begin{tabular}{|c|c|}
\hline $\mathrm{E}_{\mathbb{R}}, \mathrm{E}_{\mathbb{C}}=\mathrm{E}$ & real, complex Banach lattice \\
\hline $\mathrm{E}_{+}$ & positive cone \\
\hline $E^{\prime}$ & dual \\
\hline E* & semigroup dual \\
\hline $E_{F}^{\top}$ & F-product of $E$ with respect to the semigroup $T$ \\
\hline $\mathrm{E}_{F}$ & $F$-product of $E$ \\
\hline $\mathrm{E}_{\mathrm{f}}$ & see C-I, 4 \\
\hline ( $\mathrm{E}, \phi$ ) & see C-I, 4 \\
\hline EgF & tensor product \\
\hline L(E) & bounded linear operators on E \\
\hline 2(E) & center of E \\
\hline $\mathrm{E}_{\mathrm{n}}$ & n-th Sobolev space \\
\hline B (H) & $W^{*}$-algebra of all bounded 1 inear operators on H \\
\hline S(M) & state space of a $\mathrm{C}^{+}$-algebra M \\
\hline $\mathrm{M}_{+}$ & positive cone of the $C^{*}$-algebra $M$ \\
\hline $M_{*}^{*}$ & predual \\
\hline $\mathrm{M}^{\text {sa }}$ & self-adjoint part \\
\hline $\mathrm{M}_{\mathrm{n}}$ & C*-algebra of all nxn-matrices \\
\hline AC & absolutely continuous functions \\
\hline BV & functions of bounded variation \\
\hline K & compact topological space \\
\hline X & locally compact topological space \\
\hline $\mathrm{C}(\mathrm{K}), \mathrm{C}(\mathrm{K}, \mathrm{E})$ & continuous functions (with values in E) \\
\hline $C_{0}(X), C_{0}(X, E)$ & continuous functions vanishing in infinity with values in E \\
\hline $\mathrm{C}^{\text {b }}$ ( X$)$ & bounded continuous functions \\
\hline $\mathrm{C}_{\mathrm{bu}}(\mathrm{X})$ & uniformly continuous functions \\
\hline $c^{1}, c^{(n)}$ & continuous differentiable functions (n-times) \\
\hline $C_{c}^{\infty}\left(\mathbb{F}^{\mathbf{R}}\right)$ & infinitely differentiable functions with compact support \\
\hline $L^{p}(\mu)$ & P-integrable functions \\
\hline $S\left(\pi^{n}\right)$ & Schwartz space \\
\hline M (K) & regular Borel measures \\
\hline $M_{b}(X)$ & bounded regular Borel measures \\
\hline $T=(T(t))_{t \geq 0}$ & (one-parameter) semigroup \\
\hline ${ }^{T}$ & subspace (reduced) semigroup \\
\hline ${ }^{T} /$ & quotient semigroup \\
\hline Fix (T) & fixed space of $T$ \\
\hline
\end{tabular}
\begin{tabular}{|c|c|}
\hline A & generator \\
\hline $A^{\prime}$ & adjoint \\
\hline $A^{*}$ & adjoint generator \\
\hline $\sigma(A)$ & spectrum \\
\hline $\rho(A)$ & resolvent set \\
\hline $\sigma_{\text {ess }}(\mathrm{A})$ & essential spectrum \\
\hline $\sigma_{b}(A)$ & boundary spectrum \\
\hline Po(A) & point spectrum \\
\hline $\mathrm{P}_{\sigma_{b}}(\mathrm{~A})$ & boundary point spectrum \\
\hline $\mathrm{Ag}_{\mathrm{O}}(\mathrm{A})$ & approximate point spectrum \\
\hline $\mathrm{R}_{0}(\mathrm{~A})$ & residual spectrum \\
\hline $\omega=\omega(A)=\omega(T)=\omega(T(t))$ & growth bound \\
\hline 5 (A) & spectral bound \\
\hline $\omega_{\mathrm{L}}(\mathrm{A})$ & growth bound of the solution of the (ACP) \\
\hline $\omega(f)$ & growth bound of $T(\cdot)$ f \\
\hline r (T) & spectral radius \\
\hline $w_{\text {ess }}$ (A) & essential growth bound \\
\hline $\mathrm{ress}^{(T)}$ & essential spectral radius \\
\hline $\mathrm{R}(\lambda, A)$ & resolvent operator \\
\hline $I^{d},\left(I^{d}\right)^{\text {d }}=I^{\text {dd }}$ & orthogonal band of $I$ (of $I^{\text {d }}$ ) \\
\hline - & infimum \\
\hline $\checkmark$ & supremumt \\
\hline |T| & modulus of a regular operator \\
\hline 宔, 気 & Fourier (inverse Fourier) transformation \\
\hline $\mathrm{d} p$ (f) & subdifferential of $p$ in $f$ \\
\hline dN(f) & subdifferential of the norm in $f$ \\
\hline $\mathrm{dm}^{+}$(f) & subdifferential of the canonical half-norm in f \\
\hline im & range \\
\hline ker & nu11-space \\
\hline Im & Imaginary part \\
\hline Re & real part \\
\hline Ref, Imf & see C-Is 7 \\
\hline Ret, ImT & see $\mathrm{CmI}, 7$ \\
\hline $\overline{\mathrm{f}}$ & complex conjugate of f \\
\hline $S_{\text {E }}$ & signum operator with respect to f \\
\hline $\operatorname{sign~f}$ & signum of f \\
\hline sign f & see C-II, 2.2 \\
\hline $\mathrm{f}^{[\mathrm{n}]}$ & B-III,2.2 ; C-III, 2.1 \\
\hline |f & absolute value of $f$ \\
\hline $\mathrm{f}^{+}$ & positive part of $f$ \\
\hline $\mathrm{f}^{-}$ & negative part of $f$ \\
\hline
\end{tabular}
\begin{tabular}{|c|c|}
\hline Id & identity operator \\
\hline $\mathrm{M}_{\mathrm{p}}$ & multiplication operator \\
\hline 1 & function identically 1 \\
\hline ${ }^{1} \mathrm{C}$ & characteristic function of the set $C$ \\
\hline $\delta_{\text {r }}$ & Dírac measure in x \\
\hline tr & trace \\
\hline ${ }^{5}$ pan M & 1nnear subspace generated by M \\
\hline $S(\alpha)$ & sector in the complex plane \\
\hline (ACP) & abstract Cauchy problem \\
\hline (P) & positive minimum principle \\
\hline ( ${ }^{\prime}$ ') & B-II, 1.21 \\
\hline (K) & Kato's (equality) inequality \\
\hline (RCP) & retarded Cauchy problem \\
\hline (RE) & retarded equation \\
\hline (T) & translation property \\
\hline
\end{tabular}

\section*{SUBJECT INDEX}

Abelian group 390 f
locally compact -- $390 f$
solenoidal -- 391
abscissa
- of absolute convergence 703 f
- of simple convergence 103
- of holomorphy 101
absolute value 235, 239
abstract Cauchy problem
$4,26_{\mathrm{ff}}, 98_{\mathrm{ff}}, 336$
adjoint $16 \mathrm{f}, 400$
- generator 17 f
- operator $16,64 \mathrm{f}, 77,141$
- semigroup 16ff
admissible function 154ff
algebra homomorphism 143 ff
algebraic multiplicity 73
AL-space 239
AM-space 239
approximation theorems 32f, 44, 81, 116
asymptotics $98 \mathrm{ff}, 204 \mathrm{ff}, 342 \mathrm{ff}, 352,406 \mathrm{ff}$
automorphism group 146 ff

Banach lattice 235
complex -- $843,260,288$
real -- 243
band 236
- projection 237
boundary spectrum 169 ff ,
$296 \mathrm{ff}, 302 \mathrm{ff}, 305,379 \mathrm{ff}, 387$

C*-algebra 117:369
Calkin algebra 73
Cauchy problem 4, 26 ff
abstract -- $4,26 \mathrm{ff}, 98 \mathrm{ff}, 336$
autonomous -- $4,26 \mathrm{ff}$
homogeneous -- 4, 88 ff
inhomogeneous -- 112ff, 340ff
retarded -- $219 \mathrm{ff}, 356 \mathrm{ff}$
well-posed -- 26£f
center 246, 272, 279f, 288
Cesaro
- mean 346, 406, 408
- sumable $93 f$

Chapman-Kolmogorov equation 213f
characteristic equation $780,229,362$
generalized -- 226,362
characterization
- of generators
$124 \mathrm{ff}, 247 \mathrm{ff}, 260 \mathrm{ff}, 376 \mathrm{ff}$
chain rule 136
closable $5 \mathrm{f}, 52,128$
closure $5 \mathrm{f}, 52,128$
cocycle 148ff
cone
positive - $51,234,369$
conditional expectation
normal -- 417f, 416
core $5 \mathrm{f}, 46 \mathrm{f}$
cyclic 169, 172ff, 192ff, $302 \mathrm{ff}, 305,379 \mathrm{ff}, 388 \mathrm{ff}$
imaginary additively 172ff, 192ff, 302ff

Datko's theorem 10gf
decomposition $68 \mathrm{ff}, 325 \mathrm{ff}, 351 \mathrm{ff}$
delay
- differential equation E19ff
- equation 356ff
derivation 143ff
derivative
first order - $9 \mathrm{ff}, 146,184 \mathrm{f}$, $220,265,276,308 \mathrm{f}, 357$
higher order - 267 f
second order - 11f, 34f, 179, $185,249 \mathrm{f}, 308 \mathrm{f}$
differential equation
homogeneous -- 4 , 98 f
inhomogeneous -- $172 \mathrm{ff}, 340 \mathrm{ff}$
ordinary -- 158f, 197f, 219ff
partial -- 26
retarded -- $134 \mathrm{f}, 142,179 \mathrm{f}, 219 \mathrm{ff}$
system of -- 365
differential operator $9 f \mathrm{f}, 11 \mathrm{ff}$, $34 \mathrm{f}, 146,179,195,220,259 \mathrm{f}$, $265,267 \mathrm{f}, 276,308 \mathrm{f}, 357$
disfointness preserving
-- operator 281
-- semigroup 281 ff
dispersive 249 ff
strictly - $249_{f f}$
dissipative 47ff
p- 48 ff , 128 ff
strictly - 48 ff
Doeblin's condition 218, 345
domain $3,9,4 \mathcal{E f}$
Fredholm - 73 f
domain of uniqueness 46 f
```
dominant spectral value
    177ff, 304, 318ff
    strictly ---
        177ff, 210, 217, 318ff
domination 269ff, 371
dual 16
    semigroup - 16f
Dunford-Pettis property 56
```
```
eigenspace 64, 86
eigenvalue 64, 387
    approximate - 64,314
    simple - 73, 305, 310,388
    norme11zed - 389
eigenvector 64,387
    approximate - 64,314
elliptic differential operator
                185, 1905, 260, 305, 312
equation
    differential - 4
    heat - 13
    population - 229, 344f, 354f, 364ff
    retarded - 356ff
    transport - 309f,320
example
    counter -
        3,61ff, 105, 131, 265ff,311
    standard - 7ff, 9, 10, 11, 12.
        42ff, 100f, 124, 280, 416
exponential estimate &f
```
F-product $20 \mathrm{f}, 298 \mathrm{ff}, 314 \mathrm{ff}$
F-product with respect to a semigroup
        $20 \mathrm{f}, 74 \mathrm{ff}, 192$
face $38 B$
    Invariant - 388,410
faithful subset 380
Fejer's theorem 93 f
Feller property
    strong -- 213
fixed space $343 \mathrm{ff}, 374 \mathrm{ff}$, $380 \mathrm{ff}, 414$
flow 143 ff
    continuous - $148,192 \mathrm{ff}, 330$
    semi - $143 \mathrm{ff}, 328 \mathrm{ff}$
    seperately continuous - 149 f
forcing term 112ff, 340£f
    periodic - 116
    p-periodic -- 113ff
Fourier transformation 12f, 91, 252
    1nverse -- 13,91
    coefficient 80
Fredholm
    - domain 73f
    - operator 73 f

Gateaux-derivative $50,736,257,283$
generalized solution 99,112
generator $3 f f$
adjoint - 16
bounded - $2,7,54 \mathrm{ff}, 129,247$, 255, 288, 376ff
weak* - 16
geometric multiplicity 73
graph 5
graph norm 5
Grothendieck space 55 ff
group $1,6,9,34,66,146 \mathrm{fx}$, $326 \mathrm{f}, 352 \mathrm{ff}, 390 \mathrm{f}$
automorphism - 146ff
lattice homomorphism 202
one-parameter - $1,6,31$
positive - $146,148 \mathrm{ff}, 295,326 \mathrm{f}$
rotation - 10,89 , 352ff
unitary - 13
growth bound $2,6,60 \mathrm{ff}$
-- of a semigroup $2,6,60 \mathrm{f}, 74$, $99 \mathrm{ff}, 130,168,204 \mathrm{ff}, 295$, $334 \mathrm{ff}, 343,400 \mathrm{ff}$
-- of mild solutions of a Cauchy problem $99 f \mathrm{f}$
-- of solutions of a Cauchy problem 99ff, 204ff, 336ff
essential -- 74, 343
half-norm 57ff, 127ff
canonical - $51 \mathrm{ff}, 127 \mathrm{ff}, 255 \mathrm{ff}$
strict - 57ff. 127ff
heat equation 13
Hilbert space $13,62,94 \mathrm{ff}, 105,403$
Hille-Yosida theorem 32
ideal 236
algebraic - 118
closed - 118,236
Invariant - 782 f f, 303, $306 \mathrm{ff}, 317$
lattice - 236
imaginary additively cyclic subset 172ff, 198£f, 297
inhomogeneous differential equation 112ff, 340£f
integral equation 363
interpolation $335,348,352$
invariant
- ideals 182ff, 303, 306ff, 317
- subset 24,346
irreducible $138 \mathrm{ff}, 256 \mathrm{ff}, 414$
- semigroup $130,182 \mathrm{ff}, 210,306 \mathrm{ff}$, 311ff, 315ff, 409ff
W*- $\quad 388$
Jordan decomposition $384,399,420$

Kakutani-Krein theorem $\quad 240,297$,
313,334
Kato's
- equality $138 \mathrm{ff}, 285 \mathrm{ff}, 325 \mathrm{f}$
- inequality $139,256 \mathrm{ff}, 258 \mathrm{ff}, 285$
$\quad$ classical - $139 \mathrm{f}, 258 \mathrm{f}$
distributional - 259 f
Krein-Rutman theorem $\quad 130,167,334$

Laplace transform 101, 107
Laplacian $13,34 \mathrm{f}, 100,110,139$, $168,185,205,250 \mathrm{f}, 258,338$
lattice
- homomorphism $120,243,244,281$
- norm 235
locality 146f, 268f, 282, 287
long term behavior $98 \mathrm{ff}, 204 \mathrm{ff}$, 342ff, 352, 406ff
Lumer-Phillips theoremt 53 f

Markov
- algebra homomorphism 143 ff
- lattice homomorphism 120 , 192ff, 200f
- operator 120. 191
- process 213 f
- semigroup 144, 191
- transition function $213 \mathrm{f}, 347 \mathrm{f}$
matrix semigroup 7
maximum principle 195, 190
mild solution 99,112
modulus $136,257,278 \mathrm{ff}, 291$
multiplication
- operator $7 \mathrm{f}, 89_{\mathrm{f}}, 246$
- semigroup $7 \mathrm{f}, 42 \mathrm{ff}, 65 \mathrm{f}, 287 \mathrm{ff}$
multiplicity $73 f f$
algebraic - 73f, 209, 310
- as a pole 73
geometric - 73,310
negative part 235
norm
graph - 5
Sobolev - 18 ff
normal linear functional 369
```
operator
    closable - 5f
```
```
population equation 229ff, 344f,
    354f, 364ff
positive part 235
positive minimum principle
    125ff, 133ff, 253ff, 268
positive subeigenvector 201
positivity 118, 119, 120,
        123ff, 238, 242, 244, 370
    n- 370,403
    strict - 118, 119, 120,
        238, 242, 310, 316
predual 369
profection 72, 209ff, 343ff,
        410ff, 423
    ergodic - 410ff, 484
    recurrent - $07
    semigroup -
        209ff, 310, 343ff, 411
    spectral - 68ff
pseudo-resolvent 298ff, 314ff,
        372ff, 383ff, 392ff, 419ff
    positive - 299ff
```
quasi-compact 214ff, 343ff
quasi-interior point 238, 306
range condition $53 \mathrm{f}, 146 \mathrm{f}, 249,270$
regular mapping $242,272,279 \mathrm{f}$
regularity $242,272,279 f$
residue $67 \mathrm{f}, 78 \mathrm{ff}, 309 \mathrm{ff}$, 395ff
resolvent 63ff, 370
compact - 40, 73, 130, 166, 177, 305, 318, 336
positive - 183ff
pseudo - $298 \pm \mathrm{f}, 314 \mathrm{ff}, 372 \mathrm{ff}$, $383 \mathrm{ff}, 398 \mathrm{ff}, 419 \mathrm{ff}$
slowly growing - 301 ff
resolvent 6, 63ff. 370
- equation 127, 298
- integral representation $6,293 £ f$
- positive 127
- set 63ff, 75
retarded
- differential equation 219ff
- equation 356£f

Riesz Decomposition theorem 237
Riesz Schauder theory 72f

Schrödinger operator 273f, 278f, 336
Schwarz map 370ff, 379ff, 381ff, 407ff identity preserving -- $370 \mathrm{ff}, 379 \mathrm{ff}$, 381ff, 408ff
```
Schwarz inequality 370
Schwartz space 72, 250
self-adjoint part 369
semiflow $143_{\mathrm{ff}}, 328_{\mathrm{ff}}$
    continuous - $144 \mathrm{f} \mathrm{f}, 192$
    injective - 193
    surjective - 193
semigroup $1_{f f}$
    adjoint - $16 \mathrm{ff}, 77,400$
    analytic - $\quad 33_{\mathrm{ff}} \mathrm{f}$
    bounded - 3
    bounded holomorphic (of angle a) -
        $33 \mathrm{ff}, 1.10$
    compact - 40 ff
    commuting - 24
    contraction - $\quad 3,47 \mathrm{ff}, 247 \mathrm{ff}$,
        $297_{\mathrm{f}}, 397$
    convolution - 12
    differentiable - $37 \mathrm{f}, 41$
    diffusion - 11ff
    disfointress preserving - $\quad 81 \mathrm{ff}$
    eventually compact -
    $40 \mathrm{ff}, 209,217,214$
    eventually differentiable - 37, 41
    eventually norm cont inuous -
        $3 g_{\mathrm{ff}}, 41,87_{\mathrm{ff}}, 106,178,304_{\mathrm{f}}$,
        $318,337,345$
    F-product - $20 \mathrm{f}, 74 \mathrm{ff}, 792$
    holomorphic (of angle $\alpha$ ) - $33_{\mathrm{ff}}, 41$,
        $100,183,305 \mathrm{f}$, 311 ff
    1dentity preserving - $370_{\mathrm{f}} \mathrm{f}, 379_{\mathrm{ff}} \mathrm{f}$,
        $389_{\mathrm{ff}}, 408_{\mathrm{f}} \mathrm{f}, 424_{\mathrm{f}}$
    implemented - 403
    induced - $14 \mathrm{f}, 74 \mathrm{ff}, 298,374$
    irreducible - 188ff, 210, 315ff,
        $388_{\mathrm{f}} \mathrm{f}, 409_{\mathrm{ff}}$
    lattice homomorphism - $135 \mathrm{ff}, 143 \mathrm{ff}$,
        $392 \mathrm{ff}, 285,320 \mathrm{ff}$
    Markovian - $144 \mathrm{ff}, 191$
    matrix - 7
    mean-ergodic - 346
    modulus - $278_{\mathrm{ff}}, \quad 282_{\mathrm{ff}}$
    multiplication - $7 \mathrm{f}, 42 \mathrm{ff}$, $65 \mathrm{f}, 287_{\mathrm{ff}}$
    nilpotent - 11, 41f, 74ff
    norm continuous - $38_{\mathrm{f}} \mathrm{f}, 41$
    - of Schwarz type $370 \mathrm{ff}, 379 \mathrm{ff}$,
        $408_{\mathrm{ff}}, 484 \mathrm{f}$
    one-parameter - 1
    partially periodic - 352ff, 416ff
    periodic - 79ff, 85, 313, 416
    positive - 123ff
    preadjoint - 414
    quasi-compact - 214 ff , 343 ff
    quotient - 15, 74
    reduced - 374, 407
    rescaled - 14
    rotation - $10,69,189,313,352 \mathrm{ff}$
    similar - 13f
    Sobolev - $18_{\text {ff }}$
    strongly continuous - $\sum_{\text {ff }}$
    strongly ergodic - $406,409_{\mathrm{ff}}, 424 \mathrm{f}$
    subspace - $14 \mathrm{f}, 74$
```
```
tensor product - 21 ff , 88 f
    translation - $\quad 9 \mathrm{f}, 11,25,18,41$,
        66£f, 205
    uniformly continuous - 2, 7, 54ff,
        129, 247, 255, 288, 376ff
    uniformly ergodic - 391ff, 416,
        $419,484 \mathrm{f}$
    weakly continuous - 2
    weak* continuous - 16, 370ff, 403
    weak*-irreducible - 388, 414, 484f
semigroup dual 16f, 77
signum 137ff, 256ff, 276, 296f
    - operator $170 \mathrm{ff}, 245,256 \mathrm{ff}, 296$
singularity
    1solated - 78ff
Sobolev space 18 ff
    classical -- 19
solit subset 236
solution of a Cauchy problem 4, 27ff
    generalized - 99 , 112ff
    mild - 99 , 11Zff
    P-periodic - 113 ff
    strong - $27 \mathrm{ff}, 99$, 112ff,
        $219 \mathrm{ff}, 356 \mathrm{ff}$
spectral
    - decomposition 68 ff , 325 ff , 351 f
    - projection 69f, 79
    - theorem 60ff, 82 ff
spectral bound $60 \mathrm{ff}, 101 \mathrm{f}, 105 \mathrm{ff}$,
        130, 163, $168,204 \mathrm{ff}, 225,292 \mathrm{ff}$,
        316, 334ff, 361, 379, 400ff
    essential -- $73 \mathrm{f}, 814 \mathrm{ff}$, 318
spectral inclusion theorem 84 f
spectral mapping theorem
        $60 \mathrm{ff}, 67,89_{\mathrm{ff}} \mathrm{f}, 106$
    weak --- $65 \mathrm{f}, 83 \mathrm{f}, 89 \mathrm{ff}$
    --- for the resolvent $\quad 67 \mathrm{f}$
spectral radius 60
    essential -- $73 \mathrm{f}, 177,214 \mathrm{ff}, 318$
spectral value
    dominant - $\quad 177 \mathrm{ff}$
    strictly dominant - $177 \mathrm{ff}, 210,217$
spectrum $60 f f$
    approximate point - 64f, 394
    boundary - $169 \mathrm{ff}, 296 \mathrm{ff}, 302 \mathrm{ff}$,
        $305,379 \mathrm{ff}, 387$
    cyc11c - $169,172 \mathrm{ff}, 302 \mathrm{ff}$,
        305, 379 ff , 388 ff
    essential - 73f
    point - 64f, 394
    residual - 64 f
stability
        $99_{\mathrm{ff}}, 267,337_{\mathrm{ff}}, 361,402_{\mathrm{ff}}$
    exponential - $9 \theta_{\mathrm{ff}}, 227$
    uniform - $99_{\mathrm{f}}, 339$, 402ff
    unfform exponential - $\boldsymbol{g Q}_{\mathrm{f}}$,
        $205,402 \mathrm{ff}$
    weak uniform - 117 f
state space 369,400
stationary point 156
stochastic continuity $213_{f}$
```
    weak - 111f, 205f, 402 ff Zero-Two 1aw ( $0-2$ 1aw) 347ff
strictly positive
        118, 119, 120. 238, 242, 261
-- element 261
-- functional 238, 261
-- operator 242
-- subset 261 ff
subdifferential $4 \delta f f, 12 g f f$
subeigenvector 261
positive - 261
subinvariant subset 380
sublattice 236
sublinear function 47 f
```
tensor product
    -- of Banach spaces 21ff
    -- of operators 21ff
    -- of semigroups 2Iff, 8Bf
translation property 220, 358
translation semigroup 9F, 15, 18,
        67f, 66ff, 75, 205
    nilpotent -- 11, 41f, g3, 164f
    periodic -- 66
transformation
    Fourier - 12f
    Laplace - 101, 107
    transport equation 300f,320
type of a semigroup 2
u1trapower 345, 377, 394, 420
unimodular function 3IJ
unitary 390
```
vector
    - lattice 235
    - sublattice $\quad 236$
W**algebra 369
$W^{*}$-dynamical system 414 ff
    irreducible -- 414 ff
weakly sequentially compact 242, 322
well-posedness 26ff