# positive semigroups on $C^{*}$ - And $W^{*}$-Algebras 

by<br>Ulrich Groh *)

CHAPTER D-I

BASIC RESUTTS ON SEMIGRQUPS

$$
A N D \quad O P E R A T O R \quad A L G E B R A S
$$

This is not a systematic introduction into the theory of strongly continuous semigroups on $C^{*}$ and $W^{*}$-algebras. For that we refer to Bra-tteli-Robinson (1979), Davies (1976) and the survey article of Oseledets (1984). We only prepare for the subsequent chapters on spectral theory and asymptotics by fixing the notations and introducing some standard constructions.

## 1. NOTATIONS

1. By $M$ we shall denote a e*-algebra with unit 1 . $M^{\text {sa }}:=(x \in M$ : $\left.x^{*}=x\right\}$ is the selfmadjoint part of $M$ and $M_{+}:=\left\{x^{*} x: x_{M}\right\}$ the positive cone in $M$, If $M^{\prime \prime}$ is the dual of $M^{\prime}$, then $M^{\prime}{ }^{\prime}=\left\{\psi^{\prime} M^{\prime}\right.$ : $\left.\psi(x) \nless 0, x^{G_{M}}\right\}$ is a weak*-closed generating cone in $M^{\prime}$. $S(M):=$ $\left\{\psi M_{+}{ }^{r} \psi(1)=I\right\}$ is called the state space of $M$. For the theory of $C^{*-a l g e b r a s ~ a n d ~ r e l a t e d ~ n o t i o n s ~ w e ~ r e f e r ~ t o ~[P e d e r s e n ~(1979)] . ~}$ $M$ is called a $W^{*}$-algebra, if there exists a Banach space $M_{*}$, such that its dual $\left(M_{*}\right)^{\prime}$ is (isomorphic to) $M$. We call $M_{*}$ the predual of $M$ and $\psi \in M_{*}$ a normal linear functional. It is known that $M_{*}$ is unique 「Sakai (1971), 1.13.3.]. For further properties of $\mathrm{M}_{*}$ we refer to [Takesaki (1979), Chapter III].

[^0]2. A map $T \in L(M)$ is called positive (in symbols $T \geq 0$ ) if $T\left(M_{+}\right) \leq$ $M_{+} . T \in L(M)$ is called $n$-positive ( $n \in \mathbb{N}$ ) if $T$ id $n$ is positive from $M \& M_{n}$ in $M M_{n}$, where $I_{n}$ is the identity map on the $c^{*}$ algebra $M_{n}$ of all n×n-matrices. obviously, every n-positive map is positive. We call $T \in L(M)$ a Schwarz map if $T$ satisfies the inequality
$$
T(x) T(x)^{*} \varsubsetneqq T\left(x x^{*}\right) \quad, x \in M
$$

Note that such $T$ is necessarily a contraction. It is well known that every $n$-positive contraction, $n \geq 2$ and that every positive conm traction on a commutative $c^{*}$-algebra is a Schwarz map EPakesaki (1979), Corollary IV. 3.8.]. As we shall see, the Schwarz inequality is crucial for our investigations.
3. If $M$ is a $C^{*-a l g e b r a}$ we assume $T=(T(t))_{t \geqslant 0}$ to be a strongly continuous semigroup (abbreviated semigroup) while on w*-algebras we consider weak*-semigroups, i.e. the mapping ( $t \rightarrow T(t) x$ ) is continuous from $\pi_{+}$into $\left(M, o\left(M, M_{*}\right)\right), M_{*}$ the predual of $M$, and every $T(t) \in$ $T$ is o( $\left.M_{,} M_{*}\right)$-continuous. Note that the preadjoint semigroup

$$
T_{*}=\left\{T(t)_{*}: T(t) \in T\right\}
$$

is weakly, hence strongly continuous on $M_{*}$ (see e.g., Davies (1980), Prop.1.23). We call $T$ identity preserving if $T(t) 1=1$ and of Schwarz type if every $T(t) \in T$ is a schwarz map,

For the notations concerning one-parameter semigroups we refer to part A. In addition we recommend to compare the results of this section of the book with the corresponding results for commutative ${ }^{*}$ *algebras, i.e. for $C_{o}(X), C(K)$ and $L^{\infty}(\mu)$ (see Part B).
2. A FUNDAMENTAF INEQUALITY FOR THE RESOLVENT

If $\left.T=(T(t))_{t}\right\} 0$ is a strongly continuous semigroup of schwarz maps on a C*-algebra $M$ (resp. a weak*-semigroup of schwarz type on a $W^{*}$-algebra $M$ ) with generator $A$, then the spectral bound $s(A) \leq 0$. Then for $\lambda \in C$, $\operatorname{Re}(\lambda)>0$, there exists a representation for the resolvent $R(\lambda, A)$ given by the formula

$$
R(\lambda, A) x=\int_{0}^{\infty} e^{-\lambda t} T(t) x d t \quad x \in M
$$

where the integral exists in the norm topology.

In [Bratteli-Robinson (1979)] it is shown that $T$ is a semigroup of schwarz type if and only if $\mu$ ( $\mu, A$ ) is a schwarz map for every $\mu \in \mathbb{R}+$. Here we relate the domination of two semigroups to an inequality for the cotresponding resolvent operator. This inequality will be needed later.

Theorem 2.1. Let $T=(T(t))_{t \geqslant 0}$ be a semigroup of schwarz type and $T=(S(t))_{t \geq 0}$ a semigroup on a $C^{*}$-algebra $M$ with generators $A$ and $B$, respectively. If

$$
\begin{equation*}
(S(t) x)(S(t) x)^{*} \leq T(t) x x^{*} \tag{*}
\end{equation*}
$$

for all $x \in M$ and $t \in \mathbb{R}_{+}$, then

$$
(\mu R(\mu, B) x)(\mu R(\mu, B) x)^{*} \leqslant \mu R(\mu, A) x x^{*}
$$

for all $x \in M$ and $山 \in \mathbb{R}_{+}$. The same result holds if $T$ is a weak*-semigroup of schwarz type and $S$ is a weak*-semigroup on a w*algebra M such that (*) is fulfilled.

Proof. From the assumption (*) it follows that

$$
\begin{aligned}
0 \leqq(S(r) x- & S(t) x)(S(r) x-S(t) x)^{*}= \\
= & (S(r) x)(S(r) x)^{*}-(S(r) x)(S(t) x)^{*}- \\
- & (S(t) x)(S(r) x)^{*}+(S(t) x)(S(t) x)^{*} \leqq \\
\leqq T(r) x x^{*} & +T(t) x^{*}-(S(r) x)(S(t) x)^{*}- \\
- & (S(t) x)(S(r) x)^{*}
\end{aligned}
$$

for every $r, t \in \mathbb{R}_{+}$. Hence

$$
(S(r) x)(S(t) x)^{*}+(S(t) x)(S(r) x)^{*} \leqslant T(r) X x^{*}+T(t) X x^{*}
$$

Obviously, $\|$ 's ( $t$ ) $\| \leq 1$ for all $t \in \mathbb{R}_{+}$. Then for all $\mu \in \mathbb{R}_{+}$and $x \in M$ :
$(R(\mu, B) x)(R(\mu, B) x)^{*}=\left(\int_{0}^{\infty} e^{-\mu r} S(r) x d r\right)\left(\int_{0}^{\infty} e^{-\mu t} S(t) x d t\right)^{*}=$

$$
\begin{aligned}
& =\frac{1}{2}\left(\int_{0}^{\infty} \int_{0}^{\infty} e^{-\mu(r+t)}(S(r) x)(S(t) x)^{*}\right. \\
& \left.\quad+(S(t) x)(S(r) x)^{*}\right) d r d t \\
& \leq \frac{1}{2}\left(\int_{0}^{\infty} \int_{0}^{\infty} e^{-\mu(r+t)}\left(T(r) x x^{*}+T(t) x x^{*}\right) d r d t\right. \\
& =\left(\int_{0}^{\infty} e^{-\mu s} d s\right)\left(\int_{0}^{\infty} e^{-\mu t} T(t) \times x^{*} d t\right)=\mu^{-1} R(\mu, A) \times x^{*}
\end{aligned}
$$

where the handing of the integral is justified by SBourbaki (1955), G8, $\mathrm{n}^{\circ} 4$, Proposition 9].

Corollary 2.2. Let $T$ be a semigroup of Schwarz maps (resp., weak*semigroup of schwarz maps). Then for all $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda)>0$ :

$$
(\operatorname{R}(\lambda, A) x)(R(\lambda, A) x)^{*} \leq(\operatorname{Re} \lambda)^{-1} R(\operatorname{Re} \lambda, A) x x^{*}, \quad x \in M
$$

In particular for all $(\mu, \alpha) \in \mathbb{R}_{+} \times \mathbb{R}, x \in M:$

$$
(\mu R(\mu+i \alpha, A) x)(\mu R(\mu+i \alpha, A) x) * \leq \mu R(\mu, A)\left(x x^{*}\right)
$$

Proof. Let $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda)>0$. Then the semigroup

$$
S:=\left(e^{-i \operatorname{Im}(\lambda) t^{T}} T(t)\right)_{t \geq 0}
$$

fulfils the assumption of Thm 2.I. and $B$ : $=A-i \lambda$ is the generator of $S$. Consequently $R(\lambda, A)=R(R e \lambda, B)$ and the corollary follows from Theorem 2.1.

As in section C-III the following notion will be an important tool for the spectral theory of semigroups.

Definition 2.3. Let $E$ be a Banach space and $\phi \neq \mathrm{D}$ an open subset of $C$ A family $R: D \rightarrow L(E)$ is called a pseudo-resolvent on $D$ with values in $E$ if

$$
R(\lambda)-R(\mu)=-(\lambda-\mu) R(\lambda) R(\mu)
$$

for all $\lambda$ and $\mu$ in $D$.

If $R$ is a pseudo-resolvent on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda) ; 0\}$ with values in a $C^{*}$ - or $W^{*}$-algebra, then $R$ is called of schwarz type if

$$
(R(\lambda) x)(R(\lambda) x) * \leq(\operatorname{Re} \lambda)^{-1} R(\operatorname{Re} \lambda) x x^{*}
$$

for all $\lambda \in D$ and $x \in M, R$ is called identity preserving if $\lambda R(\lambda) I=1$ for all $\lambda \in D$.

For examples and properties of a pseudo-resolvent see C-III, 2.5. We state what will be used without further reference.
(a) If $a \in C$ and $x \in E$ such that $(a-\lambda) R(\lambda) x=x$ for some $\lambda \in D$, then $(\alpha-\mu) R(\mu) x=x$ for all $\mu \in D$ (use the "resolvent equation").
(b) If $F$ is a closed subspace of $E$ such that $R(\lambda) F E F$ for some $\lambda \in D$, then $R(\mu) F F$ for all $\mu$ in a neighbourhood of $\lambda$. This follows from the fact that for all $\mu \in D$ near $\lambda$ the pseudo-resolvent in $\mu$ is given by

$$
R(\mu)=\sum_{n}(\lambda-\mu)^{n} R(\lambda)^{n+1}
$$

Definition 2.4. We call a semigroup $T$ on the predual $M_{*}$ of a W*-algebra $M$ identity preserving and of Schwarz type, if its adjoint weak*-semigroup has these properties. Likewise, a pseudoresolvent $R$ on $D=\{\lambda \in \mathcal{C}: \operatorname{Re}(\lambda)>0\}$ with values in $M_{*}$ is called identity preserving and of schwarz type, if $R$ " has these properties.

Since for a semigroup of contractions on a Banach space

$$
\begin{aligned}
& \operatorname{Fix}(T)=\cap_{t \geqq 0} \operatorname{ker}(I d-T(t))= \\
& =\operatorname{ker}(I d-\lambda R(\lambda, A))=\operatorname{Fix}(\lambda R(\lambda, A))
\end{aligned}
$$

for all $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda)>0$, it follows that a semigroup of conm tractions on $M$ is identity preserving if and only if the (pseudo)resolvent on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ given by

$$
\mathrm{R}(\lambda):=\mathrm{R}(\lambda, A) \mid \mathrm{D}
$$

is identity preserving. By Corollary 2.2 an analogous statement holds for 'schwarz type'.
(a) If $E$ is a Banach space and $S$ ( $\leq$ (E) a semigroup of bounded operators, then a closed subspace $F$ is called S-invariant, if $S F$ 든 for all $S \in S$. We call the semigroup $S_{j}:=\left\{S_{j F}: S \in S\right.$, the reduced semigroup. Note that for a one-parameter semigroup $T$ (resp., pseudoresolvent $R$, the reduced semigroup is again strongly continuous (resp. Ry is again a pseudo-resolvent) (compare the construction in $A-1,3.2)$.
(b) Let $M$ be a $W^{*}-a l g e b r a, ~ P \in M$ a projection and $s \in L(M)$ such that $S\left(P^{\perp M}\right) \subseteq P^{\perp} M$ and $S\left(M p^{\perp}\right) \subseteq M^{\perp}$, where $P^{\perp}:=1-p$. Since for all $\mathrm{x} \in \mathrm{M}$ :

$$
p[S(x)-S(p x p)]=p\left\lceil S\left(p^{ \pm} x p\right)+S\left(x p^{\perp}\right)\right] p=0
$$

we obtain $p(S x) p=p(S(p x p)) p$. Therefore the map

$$
S_{p}:=(x \rightarrow p(S x) p): p^{M} p \rightarrow p^{M p}
$$

is well defined. We call $S_{p}$ the induced map. If $s$ is an identity preserving Schwarz map, then it is easy to see that $S_{P}$ is again a Schwarz map such that $S_{p}(p)=p$.

If $T=(T(t)) t \leq 0$ is a weak*-semigroup on $M$ which is of schwarz type and if $T(t)\left(p^{\perp}\right) \leqslant p^{\perp}$ for all $t \in \mathbb{R}_{+}$, then $T$ leaves $p^{\perp} M$ and Mp invariant. It is easy to see that the induced semigroup $T_{p}=\left(T(t)_{p} t_{\geq 0} 0\right.$ is again a weak*-semigroup.

If $R$ is an identity preserving pseudo-resolvent of Schwarz type on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ with values in $M$ such that $R(\mu) p^{\perp} \neq p^{\perp}$ for some $\mu \in \mathbb{R}_{+}$then $p^{\perp} M$ and $M^{\perp}$ are $R$-invariant. Again, the induced pseudo-resolvent $R_{p}$ is of schwarz type and identity preserving.
(c) Let $\phi$ be a positive normal linear functional on a walgebra M such that $T_{*}=\phi$ for some identity preserving schwarz map $T$ on $M$ with preadjoint $T_{*} \in L\left(M_{*}\right)$. Then $T\left(s(\phi)^{\perp}\right) \leqslant s(\phi)^{\perp}$ where $s(\phi)$ is the support projection of $\phi$. To see this let $L_{\phi}:=\left\{x \in M: \phi\left(x x^{*}\right)=0\right\}$ and $M_{\phi}:=L_{\phi} \cap L_{\phi}^{*}$. Since $\phi$ is $T_{*}$-invariant, and $T$ is a schwarz map, the subspaces $L_{\phi}$ and $M_{\phi}$ are T-invariant. From $M_{\phi}=$ $s(\phi)^{1 M s(\phi)^{1}}$ and $T\left(s(\phi)^{\perp}\right) \leqq 1$ it foIlows that $T\left(s(\phi)^{\perp}\right) \leqq s(\phi)^{\perp}$.
D-I BASICS

Let $T_{s(\phi)}$ be the induced map on $M_{s(\phi)}$. If

$$
s(\phi) M_{*} s(\phi):=\left\{\psi \epsilon_{*}: \psi=s(\phi) \psi s(\phi)\right\}
$$

where $\left\langle s(\phi) \psi s(\phi), x^{*}:=\langle\psi, s(\phi) x s(\phi)\rangle(x \in M)\right.$, and if $\psi \epsilon_{s}(\phi) M_{*} s(\phi)$, then for all $x \in M$ :

$$
\begin{gathered}
\left(T_{*} \psi\right)(x)=\psi(T x)=\langle\psi, s(\phi)(T x) s(\phi)\rangle= \\
=\langle\psi, s(\phi)(T(s(\phi) x s(\phi))) \mathrm{s}(\phi)\rangle=\left\langle T_{*} \psi, s(\phi) \times s(\phi)\right\rangle,
\end{gathered}
$$

hence $T_{*} \psi \in_{s(\phi) M_{*}}(\phi)$. Since the dual of $s(\phi) M_{*} s(\phi)$ is $M_{s(\phi)}$, it follows that the adjoint of the reduced map $T$ *| is identity preserving and of Schwarz type.

For example, if $T$ is an identity preserving semigroup of schwarz type on $M_{*}$ such that $\phi \in F i x(T)$, then the semigroup $T \mid\left(s(\phi) M_{*} s(\phi)\right)$ is again identity preserving and of Schwarz type. Furthermore, if $R$ is a pseudo-resolvent on $D=\{\lambda \in \mathbb{C} ; \operatorname{Re}(\lambda) \geqslant 0\}$ with values in $M_{\text {* }}$ which is identity preserving and of Schwarz type such that $R(\mu) \phi=$ for some $\mu \in \mathbb{R}+$, then $R \| s(\phi) M_{*} s(\phi)$ has the same properties.


[^0]:    *) This is the main part of my "Habilitationsschrift" (accepted by Mathematische Fakultät, Unfversitat Tibingen, 1984). I wish to thank Frofessor T. Ando for his warm hospitality during a one year stay at the Institute of Applied Electricity, Hokkaido University, Sapporo. My thanks go also to the Alexander von Humboldt Stiftung and to NIHON GAKUJITSU SHENEOKAE, whose support made this stay possible.

