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

## The Abstract Cauchy Problem

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

## One-parameter groups

Generators of one-parameter groups can be characterized similarly by existence and uniqueness of the solutions of the associated Cauchy problem. However, here the assumption of continuous dependence on the initial values can be relaxed (in fact, one has no longer to assume that the continuous dependence is uniform in $t$ ).

Theorem 1.6. Let $A$ be a closed densely defined operator. The following assertions are equivalent.
(i) A is generator of a strongly continuous one-parameter group.
(ii) For every $f \in D(A)$ there exists a unique function
$u(\cdot, f) \in \mathbb{C}^{1}(\mathbb{R})$ satisfying $u(t, f) \in D(A)$ for all $t \in \mathbb{R}$ and $u(0, f)=f$ such that $\frac{d}{d t} u(t, f)=A u(t, f)$; and if $f_{n} \in D(A)$ such that $\lim _{n \rightarrow \infty} f_{n}=0$, then $\lim _{n \rightarrow \infty} u\left(t, f_{n}\right)=0$ for all $t \in R$

Proof. It is clear that (i) implies (ii). If (ii) holds then there exist operators $T(t) \in L(E)$ such that $u(t, f)=T(t) f \quad(t \in \mathbb{R}$, $f \in D(A))$. It follows from the uniqueness of the solutions that $T(t+s)=T(t) T(s) \quad(s, t \in \mathbb{R})$. Let $\mathcal{E} \in E$. There exist $f_{n} \in D(A)$ such that $\lim _{n \rightarrow \infty} f_{n}=f_{\text {. }}$
Then $\lim _{n \rightarrow \infty} T(t) f_{n}=T(t) f$ for all $t \in \mathbb{R}$. Since $T(\cdot) f$ is continuous, it follows that $T$ (.)f is measureable. Hence by
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-07.jpg?height=64&width=1617&top_left_y=2418&top_left_x=208) interval $J \subset(0, \infty)$. Because of the group property this implies that $T(\cdot)$ is norm bounded on bounded subsets of $\mathbb{R}$. $T(\cdot) f$ is continuous if $f \in D(A)$. Since $D(A)$ is dense this implies the strong continuity of (T( t$)_{t \in \mathbb{R}}$.

## The Hille-Yosida theorem

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
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-09.jpg?height=72&width=1406&top_left_y=404&top_left_x=211)

```
for all f & E and t }\geqq0\mathrm{ .
```


## Holomorphic semigroups

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
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-11.jpg?height=52&width=1617&top_left_y=1756&top_left_x=205) $\left\|\xi \mathrm{R}\left(\mathrm{i}_{\boldsymbol{\eta}, \mathrm{A}} \mathrm{A}\right)\right\|_{\boldsymbol{j}} \leqslant \mathrm{M} /|\eta| \leqslant \mathrm{C}, \mathrm{M}=1 / 2$.
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
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-12.jpg?height=53&width=986&top_left_y=1844&top_left_x=227)
Let $\alpha \in(0, \pi / 2)$. There exist $r_{0} \leqslant 0$ and $\beta \in(0, \pi / 2)$ such that $S(\alpha+\pi / 2) \backslash B\left(r_{0}\right) \measuredangle\left\{z^{2}: z \in S(B)+w\right\}$.
[In fact, the line $\{w+r(\cos \beta+i \sin \beta)=r \geq 0\}$ can be para-
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-12.jpg?height=47&width=1617&top_left_y=2078&top_left_x=228) on B). Then $z(t)^{2}=(w+t)^{2}-t^{2} / e^{2}+i 2 t(w+t) / E$.
Thus $\lim _{t \rightarrow \infty} \operatorname{Imz}(t)^{2} / \operatorname{Rez}(t)^{2}=2 \varepsilon /\left(\varepsilon^{2}-1\right)$. Choose $\beta \in(\pi / 4, \pi / 2)$ such that $\tan (\alpha+\pi / 2)>2 \varepsilon /\left(\varepsilon^{2}-1\right) .1$
Now let $\lambda \in S(\alpha+\pi / 2) \backslash B\left(r_{0}\right)$. Then there exist $\theta \in(-B, \beta)$ and $r \geq 0$ such that $h=\left(r e^{i \theta}+w\right)^{2}$. Thus $\left(\lambda-A^{2}\right)=\left(r e^{i \theta}+w-A\right)\left(r e^{i \theta}+w-A\right)$. Hence $\lambda \in \rho\left(A^{2}\right)$ and $R\left(\lambda, A^{2}\right)=R\left(r e^{i \theta}, A-w\right) R\left(r e^{i \theta},-A-w\right)$. We conclude that $|\lambda| \cdot\left\|R\left(\lambda, A^{2}\right)\right\| \leqq|\lambda| \cdot M^{2} /(\cos \theta)^{2} r^{2} \leqq\left(|\lambda| / r^{2}\right) \cdot M^{2} /(\cos \beta)^{2}$. Thus $|\lambda| \cdot R\left(\lambda, A^{2}\right)$ is uniformly bounded for $\lambda \in S(a+\pi / 2)=B\left(r_{0}\right)$.

Remark. In Theorem 1.15 the assumption that $\pm A$ are generators can be relaxed. In fact, the proof shows the following. If $A$ is a dencely defined operator such that $\{\lambda \in C \quad \operatorname{Re} \lambda>0\} \subset \rho( \pm A-w)$ and $\|R(\lambda, \pm A-w)\| \leq M / R e \lambda$ for some $M \geqq 0$, w $\geqslant 0$, then $A^{2}$ generates a holomorphic semigroup of angle $\pi / 2$.

Next we consider semigroups satisfying a less restrictive smoothness condition.

## Differentiable semigroups

Let $(T(t))_{t \geq 0}$ be a strongly continuous semigroup with generator A. Let $t_{o} \geqq 0$ and $f \in E$. Then the function $t \rightarrow T(t) f$ is right sided differentiable in $t_{o}$ if and only if $T\left(t_{o}\right) f \in D(A)$; and in that case it is differentiable in every $s>t_{o}$ and the derivative is AT (s)f (this followg from A-I, Prop. 1.6(ii)).

Definition 1.16 . A strongly continuous semigroup ( $T(t)$ ) t¥o on a Banach space $E$ is called eventually differentiable if there exists $t_{0} \geqq 0$ such that the function $t \rightarrow T(t) f$ from ( $\left.t_{0}, \infty\right)$ into $E$ is differentiable for every $f \in E$. The semigroup is called differentiable if $t_{o}$ can be chosen 0 .

It is not difficult to see that if (T(t)) $t \geqq 0$ is differentiable for $t>t_{o}$, then it is n-times differentiable in all $s>n t_{o}$ and $T(s) E \subset D\left(A^{n}\right) \quad(n \in \mathbb{N})$. $I f \quad(T(t))_{t \geq 0} \quad i s$ differentiable, then the function $t \rightarrow T(t) f$ from $(0, \infty)$ into $E$ is infinitely often differentiable for every $f \in E$.

Generators of (eventually) differentiable semigroups can be characterized similarly as those of holomorphic semigroups by the spectral behavior of the resolvent. Whereas the spectrum of the generator of a holomorphic semigroup is included in a sector, the spectrum of the generator of an eventually differentiable semigroup is limited by a function of exponential growth (instead of a line).

Theorem l.17. A strongly continuous semigroup (T(t)) t¥0 is eventually differentiable if and only if its generator $A$ satisfies the following; there exist constants $c>0, b>0$, M>0 such that

$$
\Sigma:=\left\{\lambda \in \varepsilon ; c e^{-b \cdot \operatorname{Re} \lambda} \leqq\left|I_{\operatorname{m} \lambda}\right|\right\rangle \subset \rho(A)
$$

![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-14.jpg?height=52&width=1518&top_left_y=542&top_left_x=229)

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
$R(\lambda, A)^{n+1}=1 / n!\int_{0}^{m} e^{-\lambda t_{t} n^{n} T(t) d t} \quad(n \in W)$. Let $t^{\prime \prime}>0$ such that $t \rightarrow T(t)$ is norm continuous on $\left[t^{\prime}, \infty\right)$. Let $w \in(\omega(A)$, a). There exists $M \geq 1$ such that $\|T(t)\| \leq M e^{w t}$ for all $t a 0$. Let $\mathbb{N}:=M \cdot \int_{0}^{t^{\prime}} e^{-a t_{e} w t} d t$. Since $\lim _{n \rightarrow \infty} c^{n} / n!=0 \quad$ for $a l l$ $c=0$, there exists $n \in \mathbb{N}$ such that $N \cdot\left(t^{n}\right)^{n} / n!<\varepsilon^{n+1} / 3$. Choose $T \geqq t^{\prime}$ such that $1 / n!\cdot \int_{T}^{\infty} t^{n} e^{-a t}\|T(t)\| d t<E^{n+1} / 3$.
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

Definition 1.23. Let $A$ be an operator and $p(A) \neq \emptyset$. We say, $A$ has a compact resolvent if $R(\lambda, A)$ is compact for one (and hence all) $\lambda \in \rho(A)$.

Proposition 1.24 . Let (T(t)) tき0 be a strongly continuous semigroup and agsume that its generator has a compact resolvent. If $t \rightarrow T(t)$ is norm continuous in $t_{0}$, then $T(t)$ is compact for all $t \geqq t_{0}$.

Proof. Considering $\left(e^{-w t} T(t)\right)$ tzo for some $w>0$ if necessary, we can assume that $s(A)<0$. Let $S(t) \epsilon L(E)$ be given by $S(t) f=\int_{0}^{t} T(s) f d s(t \geq 0)$. Then $A S(t) f=T(t) f-f$ for all $f \in E$, and so $S(t)=R(0, A)(I d-T(t))$ is compact for all $t \geqslant 0$. since $t \rightarrow T(t)$ is norm continuous for $t \geqq t_{o}$, one has $\lim _{h \downarrow 0} \frac{1}{h}\left(S\left(t_{o}+h\right)-S\left(t_{0}\right)\right)=T\left(t_{o}\right)$ in the operator norm. Thus $T\left(t_{o}\right)$ is compact as limit of compact operators.

Theorem 1.25. A strongly continuous semigroup (T(t)) tı0 is compact if and only if it is norm continuous and its generator $A$ has compact resolvent.

Proof. Assume that (T(t)) $t \geq 0$ is compact. Then $T(-)$ is norm continuous on ( $0, \infty$, and so $\int_{0}^{t} e^{-w s} T(s) d s$ is compact as the norn limit of linear combinations of compact operators, where $w>w(A)$.
Since $R(w, A)=1 i m t \rightarrow \infty \quad \int_{0}^{t} e^{-w s} T(s) d s$ in the operator norm, it follows that $R(w, A)$ is compact. This proves one implication. The other follows from Proposition 1.24.

Remark 1.26.a) Generatorg of eventually compact semigroups do not necessarily have compact resolvent. Consider the nilpotent translation semigroup $(T(t))_{t \geqslant 0}$ on $F:=L^{1}[0,1]$ (see $\left.A-I, E x .2 .6\right)$. Let $E=F{ }_{0} F=L^{1}([0,1] \times[0,1.7)$ and $S(t)=T(t)$ oId (tצ0). Then (S (t)) tz0 is a strongly continuous semigroup (see A-I, 3.7). Denote by $B$ its generator. $(S(t))$ t30 is a nilpotent semigroup (so it is eventually compact), but $R(\lambda, B)=R(\lambda, A)$ Id is not compact.
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
By hypothesis, the set $H:=\{m(x): x \in X, \operatorname{Re}(m(x)) \geqq b\}$ in the case $E=C_{0}(X)$ and $H:=\{m(x): R e \lambda \geqq b$ and for all $n>0$ $\mu(f x \in X:|m(x)-\lambda|<\eta\}) \neq 0)$ in the case $E=L^{P}(X, \Sigma, \mu)$ is a bounded subset of C .
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

## Perturbation of Generators

A useful way to construct new semigroups out of a given one is by additive perturbation.

Theorem 1.29. Let $A$ be the generator of a strongly continuous semigroup (T(t)) tzo and let $B \in L(E)$. Then $A+B$ with domain $D(A+B)=D(A)$ is the generator of a strongly continuous semigroup $(S(t))_{t \geqslant 0^{*}}$

It is possible to express the new semigroup $(S(t))_{t \geq 0}$ by known objects. The product formula
(1.8) $S(t) f=\lim _{n \rightarrow \infty}\left(T(t / n) e^{t / n \cdot B}\right)_{f}^{n_{f}}$
holds for all $t \geqslant 0$ and $f \in E$.
Moreover, $S(t)$ is the solution of the following integral equation (1.9) $s(t) f=T(t) f+\int_{0}^{t} T(t-s) B S(s) f d g \quad(t \geqq 0, f \in E)$.

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
Since $K$ is compact it follows that the limit exists uniformly in £ $\in K$; i.e. $\quad \lim _{h \rightarrow 0}\|(T(t+s-h)-T(t-s)) B S(s)\|=0$. It follows from the dominated convergence theorem that
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

## Domains of Uniqueners

Given a semigroup (T(t)) tzo frequently it is frequently difficult to determine the precise domain of its generator $A$. So it is important to know which (possibly strict) subspaces of $D(A)$ determine the semigroup uniquely. This can be formulated more precisely in the following way. Let $D_{0}$ be a subspace of $D(A)$ and consider the restriction $A_{o}$ of $A$ to $D_{o}$ Under which condition on $D_{o}$ is $A$ the only extension of $A_{o}$ which is a generator? one obvious condition is that $D_{o}$ is a core. [In fact, in that case, $A$ is the closure of $A_{o}$. Since every generator $B$ extending $A_{o}$ is closed, it follows that $A \subset B$ and hence $A=B$ since $P(A) \cap(B) \neq 07$.

We now show that cores are the only domains of uniqueness.

Theorem 1.33. Let $A$ be the generator of a semigroup and $D_{o} a$ subspace of $D(A)$. Consider the restriction $A$ of $A$ to $D_{0}$. If $D_{o}$ is not a core of $A$, then there exists an infinite number of extensions of $A_{o}$ which are generators.

Proof. If $D$ f $f$ not dense in $D(A)$ with respect to the graph norm, then there exigts a non-zero linear form $\phi$ on $D(A)$ which is continuous for the graph norm such that $\phi(f)=0$ for all $f \in D_{o}$. Let $u \in D(A)$ and $B: D(A)+D(A)$ be given by $B f=\phi(f) u$ for all $f \in D(A)$. Then $B$ is continuous for the graph norm. So by Theorem 1.31 the operator $A+B$ with domain $D(A)$ is a generator. Clearly, $A+B \neq A$ if $u \neq 0$ but $A f+B f=A f$ for all $f \in D_{0}$. It is obvious that an infinite number of generators can be constructed in that way.

Corollary 1.34 . Let ( $T(t))_{t \geqslant 0}$ be a strongly continuous semigroup with generator $A$. Let $D_{o}$ be a dense subspace of E. Assume that $D_{0} \subset D(A)$ and $T(t) D_{0} \in D_{0}$ for all $t \geqslant 0$. Then $D_{o}$ is a core.

Proof. Let $(S(t)) t \geq 0$ be a semigroup with generator $B$ such that ${ }^{B}\left\|_{D O}={ }^{A}\right\|_{D_{0}}$ Let $f \in D_{o}$. Then $u(t):=T(t) f$ satigfies $u(0)=f$ and $\quad \dot{u}(t)=A T(t) f=B T(t) f=B u(t) \quad(t \geq 0)$. Since $\quad v(t)=s(t) f$ (tzo) also is a solution of the Cauchy problem defined by $B$ with initial value $f$ it follows that $s(t) f=T(t) f(t \geq 0)$. Since $D_{0}$ is dense in $E$, it follows that $S(t)=T(t)(t \geq 0)$.

## 2. CONTRACTION SEMIGROUPS AND DISSIPATIVE OPERATORS

by
Wolfgang Arendt

The Hille-Yosida theorem gives a characterization of generatorg in terms of the resolvent of the operator. However, given an operator $A$, frequently it is difficult to compute the resolvent (and its powers). So it is desirable to find conditions more immanent on $A$. This is possible for generators of contraction semigroups. For later purposes (see B-II and C-II) it will be useful not only to consider semigroups which are contractive with respect to the norm but to consider more general sublinear functionals than the norm as well.
So our setting is the following. By $E$ we denote a real Banach space throughout, and $p=E \rightarrow \mathbb{R}$ is a continuous sublinear function; i.e., $p$ satisfies

| (2.1) | $p(f+g) \leqq p(f)+p(g)$ |
| :--- | :--- |
| $(2.2)$ | $p(\lambda f)=\lambda p(f)$ |$\quad(f \in g \in E)$.

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
(2.5) $d p(f)=\left\{\phi \in E^{\prime}:\langle g, \phi\rangle<p(g)\right.$ for all $g \in E$,

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
$\left.=\lim _{t \rightarrow 0} 1 / t(<T(t) f, \phi\rangle-p(f)\right)$
$\leqq \limsup _{t \rightarrow 0} 1 / t(p(T(t) f)-p(f)) \leqq 0$.
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

Proposition 2.9. Let $A$ be a $p$-dissipative operator where $p$ is a half-norm. If $D(A)$ is dense, then $A$ is closable (and the closure of $A$ is p-dissipative as well (by Cor. 2.5)).

Proof. Let $f_{n} \in D(A), \lim _{n^{+\infty}} f_{n}=0, \lim _{n^{* \infty}} A f_{n}=g$. We have to show that $g=0$. To this end let $h \in D(A)$. Then (2.7) gives
$p\left(f_{n}+t h\right) \leqq p\left(f_{n}+t h-t A\left(f_{n}+t h\right)\right) \quad(t>0)$. Letting $n \rightarrow \infty \quad$ we obtain $p(t h) \cong p\left(t h-t g-t^{2} A h\right) \quad(t>0)$.
Hence $p(h) \leq p((h-g)-t A h) \quad(t>0)$ by positive homogeneity. Letting $t+0$ finally we obtain $p(h) \leqslant p(h-g)$ for all $h \in D(A)$. since $D(A)$ is dense by hypothesis, we can approximate $g$ by $h \in$ $D(A)$ and conclude that $P(g) \leqslant P(0)=0$. Since $\lim _{n+\infty} A\left(-f_{n}\right)=-g_{\text {r }}$ we have $p(-g) \leqq 0$ by symmetry. Hence $p(g)+p(-g) \leq 0$ which implies $g=0$ by (2.ll).

Lemma 2.10. Let $p$ be a half-norm and $A$ a p-dissipative operator. Then
(2.14) $\quad \lambda\|f\|_{\mathrm{p}} \leqq\|(\lambda-A) f\|_{\mathrm{p}} \quad$ for all $f \in D(A), h>0$.

In particular, ( $\lambda-A)$ is injective for all $h>0$.
If $p$ is strict and $A$ is closed, then im( $-A$ ) is closed for all $\lambda>0$.

Proof. Let $\lambda>0, f \in D(A)$. Then by (2.7), $\left.\lambda_{p(t f)}^{f} p(\lambda-A)( \pm f)\right)$. Hence $\lambda\left\|_{i f}\right\|_{p}=\lambda p(f)+\lambda p(-f) \leq p((\lambda-A) f)+p(-(h-A) f)=\|(\lambda-A) f\|_{p} *$ Thus (2.14) is proved. Now suppose that $p$ is strict. Then $\|$. ${ }^{2}$ is equivalent to the given norm, Let $\lambda>0$ and $g \in(i m(\lambda-A))$. Then $g=\lim _{n \rightarrow \infty}(\lambda-A) f_{n}$ for some seguence $\left(f_{n}\right){ }_{n \in \mathbb{N}} G D(A)$. It followr from (2.14) that ( $\left.f_{n}\right)_{n \in \mathbb{N}}$ is a Cauchy sequence. Let $f=\lim _{n \rightarrow \infty} f_{n}$. Then $\lim _{n \rightarrow \infty} A f_{n}=\lambda l i m_{n \rightarrow \infty} f_{n}-\lim _{n \rightarrow \infty}(\lambda-A) f_{n}=\lambda f-g$ exista. If $A$ is closed, this implies that $f \in D(A)$ and $A f=\lambda f-g$. Hence $g \neq(\lambda-A) f \in \operatorname{im}(\lambda-A)$. We have shown that im( $h \rightarrow A$ ) is closed.

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
$f \in D(A)$ there exists $\phi \in \operatorname{dp}(f)$ such that Re<Af, $\boldsymbol{f}\rangle \leq 0$.
The arguments given above show that also in the situation considered here $A$ is p-dissipative if and only if

$$
p((1-t A) £) \geqq p(f)
$$

for all f € $\mathrm{D}(\mathrm{A})$, t 亿 0 .

The results of this section carry over if they are appropriately modified. We explicitly state the most important result for the case when $P$ is the norm. A linear operator $A$ is simply called dissipative if it is $N$-dissipative where $N(f)=\|f\| \quad(f \in E)$.

Theorem 2.13 (Lumer-Phillipa). Let $A$ be a densely defined operator on a complex Banach space $E$. The following assertions are equivalent.
(i) A is closable and the closure of $A$ is the generator of a contraction semigroup.
(ii) $A$ is dissipative and ( $\lambda$ - A) has dense range for some $\lambda>0$.
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-30.jpg?height=232&width=689&top_left_y=1706&top_left_x=638)

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
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-32.jpg?height=73&width=1615&top_left_y=1594&top_left_x=229) finite. By Lemma 3.1 it suffices to show that $\lim _{t \rightarrow 0}\left\|(T(t) \sim I d)^{2}\right\|=$ 0 . Let $t_{n} \geq 0$ with lim $t_{n}=0$ be given. Then there exists a bounded sequence $\left(x_{n}\right)$ in $E$ and a bounded sequence ( $x_{n}^{\prime}$ ) in $E$ ' such that $\left\|\left(T\left(t_{n}\right)-I d\right)^{2}\right\|_{i}=\left\{\left(T\left(t_{n}\right)-I d\right) x_{n},\left(T\left(t_{n}\right)-I d\right)^{s} x_{n}^{\prime}\right\rangle$. since $T$ and $T "$ are strongly continuous, Lemma 3.2 implies that $\left(\left(T\left(t_{n}\right)-I d\right) x_{n}\right)$ and $\left.\left.\left(T_{(1}\right)-I d\right)^{\prime} x_{n}^{\prime}\right)$ converge weakly to zero. since $E$ has the Dunford-Pettis property, lim $\left\|\left(T\left(t_{n}\right)-I d\right)^{2}\right\|=0$. Consequently, $\quad \lim _{t \rightarrow 0}\left\|(T(t)-I d)^{2}\right\|=0$.

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
![](https://cdn.mathpix.com/cropped/2025_01_15_3b8b9ab483e2146bf6a8g-33.jpg?height=50&width=1615&top_left_y=1985&top_left_x=209) complete AM-spaces with unit and therefore by l) Grothendieck spaces with the Dunford-Pettis property.
4) and 5) These spaces are order complete vector lattices. This follows from [Bauer (1966) pp. 18-22, Standardbeispiele 1 and 2 p.55]. Since these spaces contain the constant functions on 0 they are complete for the supremum-norm. Indeed if ( $f_{n}$ ) is a Cauchy-sequence for this norm, it is easily seen that ( $f_{n}$ ) converges in norm to $\inf f_{n} \sup \left(f_{k}: n<k\right)$. Therefore these spaces are o-order complete AM-spaces with unit and so as before Grothendieck spaces with the Dunfordupettis property.
6) Bourgain [(1980), Cor. 3] proves that $H^{\infty}$ (D) has the DunfordPettis property and in [ (1984), Proposition III.1], that $H^{*}(D)$ is a

Grothendieck space, where $D$ is the open unit disc $\{z:|z|<1\}$. If $O$ is a finitely connected domain and $H^{*}$ does not only contain the constant functions, then $H^{(0)}(O)$ is isomorphic to a finite direct sum of copies of $H^{\infty}$ (D). (Note that $H^{(0}$ (D) is isomorphic to $\left\{f \in H^{\infty}(D) ; f(0)=0\right\}$ via the map $f \rightarrow z f$. Then uge [Grothendieck (1953), p. 77 and Prop.4.4.1]). Hence $H^{\infty}(0)$ is a Grothendieck space with the Dunford-Pettis property.

Final Remark. It follows from Theorem 3.6 that on $L^{\infty}$ the infinitesimal generator of a strongly continuous semigroup is necessarily bounded. It is not obvious that on $L^{\text {º }}$ ([0, 1$]$ ) there exist ciosed densely defined unbounded operators. To see this let $A$ be a closed densely defined unbounded operator form $\ell^{2}$ into $L^{\infty}([0,1])$ with donain $D$ (such operators can easily be constructed) . By the khintchine inequality, the map $R:\left(a_{n}\right)+\sum_{n} r_{n}$ where $r_{n}$ denotes the $n^{\text {th }}$ Rademacher function, from $t^{2}$ into $L^{1}([0,1])$ is a topological isomorphism. Hence $T=R^{\prime} \operatorname{maps} L^{+}([0,1])$ onto $\ell^{2}$. Banach's homomorphism theorem implies that $T^{-1}(D)$ is dense in $L^{\circ}([0,1])$ and that $A T$ is a closed densely defined unbounded operator on $L^{\text {º }}([0,1])$ with domain $T^{-1}(D)$. This solves a problem raised by R.Kaufman.
H. Porta and the author have shown that if a Banach space $E$ has an infinite dimensional separable quotient space and $F$ is an infinite dimensional Banach space then there always exists a closed densely defined unbounded operator from $E$ into $F$.

## NOTES.

Section l. The abstract Cauchy problem is treated systematically in the monographs of Krein (1971) and Fattoríni (1983). We refer to these books for more detajls and historical notes. One implication of Theorem $1 . l$ is proved in Krein (1971) (Thin.2.11).
The Hille-Yosida theorem has been proved independently by Hille (1948) and Yosída (1948) for contraction semigroups. The extenston to arbitrary strongly continuous semigroups is independently due to Feller (1953), Miyadera (1952) and Phillips (1953). Thus our termfnology is sifghtly incorrect, some authors refer to the general version as the Hille-Yosida-Phillips theorem which is slightly more correct. Holomorphic semigroups belong to the standard material of the theory of oneparameter semigroups. Our Theorem 1.14 deviates from the usual presentation since the condition on the resolvent is merely required on a half-plane.
Differentiable semigroups are treated in detail in the book of Pazy (1983) who discovered Theorem 1.17 and 1.18 .

The spectral property of eventually norm contintous semigroups given in Theorem 1.20 is contalned in Hille-Phillips (1957) (Thn. 16.4.2) with a proof depending on Gelfand theory. For norm continuous semigroups it is contained in Fazy (1983) with a simpler proof. The elementary proof we give here is due to $C$. Greiner.
Theorem 1.29 on the perturbation by bounded operators is due to Phjlifips (1953) who also investigated permanence of smoothness properties by this kind of perturbation, We also refer to Pazy (1983) (Sec.3.1). The observation that eventually norm continuity is preserved by perturbation by a compact operator (see Thm. 1,30 ) seems to be new.
The perturbation by continuous operators on the graph of the generator is due to Desch-Schappache: (1984). The short proof we give here is due to G. Greiner and has the advantage to yfeld the same permanence for smoothness properties as in the classical case (Cor.1.32).
The characterization of a core as "domein of uniqueness" (Thm.l.33) seems to be new. In this section we have presented part of the standard theory of one-parameter semigroups fincluding some new aspects. A very elegant brief introduction to oneparameter semigroups is given in the treatise of Kato (1966) where one can also find all the results on perturbation theory going beyond the elementary facts we discuss here. A complete information on the general theory can be obtajned by consulting the books of Davies (1980), Goldstein (1985a) and Pazy (1983). The monograph of Goldstein (1985a) in particular contains a variety of examples and applications.

Section 2. Dissipative operators were introduced by Lumer-Philifps (1961). The analogous notion of dispersiveness is due to Phillips (1962), Our approach follows closely Arendt-Chernoff-Kato (1982) where half-noms were introduced. Related previous results were obtained by Calvert (1971), Hasegawa (1966), Sato (1968), Bentlan-Picard (1979) and Pfocard (1972), where the two last consider non-linear semigroups. A further investigation of half-norms can be found in Batty-Robinson (1983) who consider ordered Banach spaces other than Banach lattices in great detafl. We also refer to the historical notes given there.

Section 3. It had been proved by Kishimoto-Robfnson (1981) that every generator of $a_{\text {ap }}$ positive semigroup on L is bounded. That every strongly continuous semigroup on $L^{\text {L }}$ is uniformly continuous was first shown by Lotr (1982), (1984), (1985). The proof of Lerma 3.1 was communicated to the author by $T$. Couihon, who independently obtained a particular case (Coulhon (1984)).

