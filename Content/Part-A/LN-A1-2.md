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

for every $f$ in the "maximal" domain $D\left(M_{G}\right):=\{g \in E: G * G \in \in\}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_6f16a93a078af94335ecg-2.jpg?height=69&width=1617&top_left_y=1025&top_left_x=228) for $1 \leqq p<{ }^{c}$. Moreover, $\left(M_{q}, D\left(M_{q}\right)\right)$ is a closed operator. This is easy in case $E=C_{0}(X)$. For $E=L^{P}(k), 1 \leqq p<a$, we consider a sequence $\left(f_{n}\right)=E$ such that $\lim _{n \rightarrow \infty} f_{n}=f \in E$ and $\lim _{n \rightarrow \infty} q_{n}=: g$ $\epsilon E$. Choose a subsequence $\left(f_{n(k)}\right)_{k \in \mathbb{N}}$ such that $\lim _{k \rightarrow \infty} f_{n(k)}(x)=$ $f(x)$ and $\lim _{k+\infty} g(x) f_{n(k)}(x)=g(x)$ for $w-a l m o s t$ every $x \in X$. Then $g=q \cdot f$ and $f \in D\left(M_{q}\right)$, i.e. $M_{q}$ is closed.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_6f16a93a078af94335ecg-5.jpg?height=47&width=1615&top_left_y=1501&top_left_x=209) fact, if $f \in D(A)$ then $f$ is absolutely continuous with $f^{\prime} \in E$. By Prop.l.6.i it follows that $T(t) f$ is absolutely continuous and hence $\mathrm{f}(\mathrm{T})=0$.

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

## 3. STANDARD CONSTRUCTIONS

Starting with a semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$ it is possible to construct new semigroups on spaces naturally associated with $E$. Such constructions will be important technical devices in many of the subseguent proofs. Although most of these constructions are rather routine, we present in the sequel a systematic account of them for the convenience of the reader.
We always start with a semigroup ( $T(t)$ ) $t \geq 0$ on a Banach space $E$, and denote its generator by $A$ on the domain $D(A)$.

### 3.0. Similar Semigroups

There is an easy way how to obtain different (but isomorphic) semi-

