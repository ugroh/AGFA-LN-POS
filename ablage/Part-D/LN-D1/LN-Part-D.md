CHAPTER D-I

BASIC RESUTTS ON SEMIGRQUPS
$$
A N D \quad O P E R A T O R \quad A L G E B R A S
$$

This is not a systematic introduction into the theory of strongly continuous semigroups on $C^{*}$ and $W^{*}$-algebras. For that we refer to Bra-tteli-Robinson (1979), Davies (1976) and the survey article of Oseledets (1984). We only prepare for the subsequent chapters on spectral theory and asymptotics by fixing the notations and introducing some standard constructions.

\section*{1. NOTATIONS}
1. By $M$ we shall denote a e*-algebra with unit 1 . $M^{\text {sa }}:=(x \in M$ : $\left.x^{*}=x\right\}$ is the selfmadjoint part of $M$ and $M_{+}:=\left\{x^{*} x: x_{M}\right\}$ the positive cone in $M$, If $M^{\prime \prime}$ is the dual of $M^{\prime}$, then $M^{\prime}{ }^{\prime}=\left\{\psi^{\prime} M^{\prime}\right.$ : $\left.\psi(x) \nless 0, x^{G_{M}}\right\}$ is a weak*-closed generating cone in $M^{\prime}$. $S(M):=$ $\left\{\psi M_{+}{ }^{r} \psi(1)=I\right\}$ is called the state space of $M$. For the theory of $C^{*-a l g e b r a s ~ a n d ~ r e l a t e d ~ n o t i o n s ~ w e ~ r e f e r ~ t o ~[P e d e r s e n ~(1979)] . ~}$ $M$ is called a $W^{*}$-algebra, if there exists a Banach space $M_{*}$, such that its dual $\left(M_{*}\right)^{\prime}$ is (isomorphic to) $M$. We call $M_{*}$ the predual of $M$ and $\psi \in M_{*}$ a normal linear functional. It is known that $M_{*}$ is unique 「Sakai (1971), 1.13.3.]. For further properties of $\mathrm{M}_{*}$ we refer to [Takesaki (1979), Chapter III].

\footnotetext{
*) This is the main part of my "Habilitationsschrift" (accepted by Mathematische Fakultät, Unfversitat Tibingen, 1984). I wish to thank Frofessor T. Ando for his warm hospitality during a one year stay at the Institute of Applied Electricity, Hokkaido University, Sapporo. My thanks go also to the Alexander von Humboldt Stiftung and to NIHON GAKUJITSU SHENEOKAE, whose support made this stay possible.
}
2. A map $T \in L(M)$ is called positive (in symbols $T \geq 0$ ) if $T\left(M_{+}\right) \leq$ $M_{+} . T \in L(M)$ is called $n$-positive ( $n \in \mathbb{N}$ ) if $T$ id $n$ is positive from $M \& M_{n}$ in $M M_{n}$, where $I_{n}$ is the identity map on the $c^{*}$ algebra $M_{n}$ of all n×n-matrices. obviously, every n-positive map is positive. We call $T \in L(M)$ a Schwarz map if $T$ satisfies the inequality
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

Definition 2.4. We call a semigroup $T$ on the predual $M_{*}$ of a W*-algebra $M$ identity preserving and of Schwarz type, if its adjoint weak*-semigroup has these properties. Likewise, a pseudoresolvent $R$ on $D=\{\lambda \in \mathcal{C}: \operatorname{Re}(\lambda)>0\}$ with values in $M_{*}$ is called identity preserving and of schwarz type, if $R$ ' has these properties.

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

\title{
CHARACTERIZATIONOFOPOSITIVE \\ ![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-395.jpg?height=44&width=1066&top_left_y=503&top_left_x=506)
}
since the positive cone of a c*algebra has non-empty interior many results of Chapter B-II can be applied verbatim to the characterization of the generator of positive semigroups on $c^{* * a l g e b r a s . ~ O n ~ t h e ~}$ other hand a concret and detailed representation of such generators has been found only in the uniformly continupus case (see Lindblad (1976)).

A third area of active research has been the following: Which maps on $C^{*}$-algebras (in particular, which derivations) commuting with certain automorphism groups are automatically generators of strongly continuous positive semigroups. For more informations we refer to the survey article of Evans (1984).

\section*{1. POSITIVE SEMIGROUPS ON PROPERLY INFINITE W*-ALGEBRAS}

The aim of this section is to show that strongly continuous semigroups of schwarz maps on properly infinite $W^{*}$-algebras are already uniformly continuous. In particular, our theorem is applicable to such semigroups on $B(H)$. It is worthwhile to remark, that the result of Lotz (1985) on the uniformly continuity of every strongly continuous semigroup on $L^{m}$ (see A-II, sec.3) does not extend to arbitrary $W^{*}$ algebras. For example, take $M=B(H), H$ infinite dimensional, and choose a projection $p \in M$ such that $M p$ is topologically isomorphic to $H$. Therefore $M=H \oplus M_{o}$, where $M_{o}=k e r(x \rightarrow x p)$. Next take a strongly, but not uniformly continuous, semigroup $S$ on $H$ and consider the strongly continuous semigroup $S \oplus \mathrm{Id}$ on M .
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-395.jpg?height=50&width=1615&top_left_y=2288&top_left_x=232) our approach we refer to [Sakai (1971), 2.2] and [Takesaki (1979), V.1].

Theorem 1.l. Every strongly continuous one-parameter semigroup of Schwarz type on a properly infinite $W^{*}$-algebra $M$ is uniformly contí nuous.

Proof, Let $T=\left(T(t)_{*}{ }^{\prime}{ }_{t \geq 0}\right.$ be strongly continuous on $M$ and suppose $T$ not to be uniformly continuous. Then there exists a sequence ( $T_{n}$ ) $c T$ and $E>0$ such that $\left\|T_{n}-I d\right\| \geqslant \varepsilon$ but $T_{n} \rightarrow I d$ in the strong operator topology. We claim that for every sequence ( $p_{k}$ ) of mutually orthogonal projections and all bounded sequences $\left(x_{k}\right)$ in $M$
$$
1 i m m_{n}\left\|\left(\mathrm{~T}_{\mathrm{n}}-\mathrm{Id}\right)\left(\mathrm{P}_{\mathrm{k}} \mathrm{x}_{\mathrm{k}} \mathrm{P}_{\mathrm{k}}\right)\right\|=0
$$
uniformly in $k \in \mathbb{N}$. This follows from an application of the Lemma of Phillips and the fact that the sequence ( $P_{k} x_{k} P_{k}$ ) is sumable in the $\mathrm{s}^{*}\left(\mathrm{M}, \mathrm{M}_{*}\right)$-topology (compare Elliot (I972)).

Let ( $p_{k}$ ) be a sequence of mutually orthogonal projections in $M$ such that every $P_{k}$ is equivalent to 1 via some $u_{k} \in M$ [Sakai (1971), 2.2].

Without loss of generality we may assume $\left\|\left(T_{n}-r d\right)\left(u_{n}\right)\right\| \leqq n^{-1}$ since the semigroup $T$ is strongly continuous. Thus we obtained the following:
(1) $\quad 1 i m{ }_{n}\left\|\left(T_{n}-I d\right)\left(P_{k} X_{k} P_{k}\right)\right\|=0$ uniformily in $k \in \mathbb{N}$ for every bounded sequence $\left(x_{k}\right)$ in $M$.
(2) Every projection $P_{k}$ is equivalent to 1 via some $u_{k} \in M$.
(3) $\left\|\left(T_{n}-1 d\right) u_{n}\right\| n^{-1}$ for all $n \in \epsilon^{2}$.

For the following construction see $A-1,3,6$ and $D-I I, S e c .2$.

Let $\hat{M}$ be an ultrapower of $M, \operatorname{let} P:=\left(p_{k}\right)^{\wedge} \hat{M}, T:=\left(T{ }_{n}\right) \wedge \in(\hat{M})$ and $u:=\left(u_{k}\right)^{\wedge} \in \hat{M}$. Then $T$ is identity preserving and of schwarz type on $\hat{M}$. Since $u^{*} u=p$ and $u^{*}=1$, it follows pu* $=u *$ and (un*) $x\left(u^{*}\right)=x$ for all $x \in \hat{M}$. Finally, $T(p x p)=$ pxp for all $x \in \hat{M}$, which follows from (I), and $T\left(u^{*}\right)=T\left(p u^{*}\right)=p u^{*}=u^{*}$ and $T(u)=u$, which follows from (3). Using the schwarz inequality we obtain
$$
T\left(u u^{*}\right)=T(1) \leq 1=u u^{*}=T(u) T(u)^{*} .
$$

Using $D-I I T$, Lemma 1.1 . we concIude $T(u x)=u T(x)$ and $T\left(x u^{*}\right)=$ $T(x) u^{*}$ for all $x \in \hat{M}$. Hence
$T(x)=T\left(u u^{*} x u u^{*}\right)=u T\left(u^{*} x u\right) u^{*}=u T\left(p u^{*} x u p\right) u^{*}=$
$=u p u^{*} x u p u^{*}=u u^{*} x u u^{*}=x$
for all $x(\bar{M}$. From this we obtain that for every bounded sequence
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-397.jpg?height=61&width=1611&top_left_y=678&top_left_x=234) and of the $x_{k}{ }^{\prime} s$. This conflicts with our assumption at the beginning, hence the theorem is proved,

\title{
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-399.jpg?height=47&width=1232&top_left_y=388&top_left_x=412) \\ SEMIGROUPSOMN \\ ![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-399.jpg?height=49&width=1369&top_left_y=615&top_left_x=338)
}

Motivated by the classical results of Perron and Frobenius one expects the following spectral properties for the generator $A$ of a positive semigroup: The spectral bound $s(A):=s u p(\operatorname{Re}(\lambda) ; \lambda \in q(A)\}$ belongs to the spectrum $\sigma(A)$ and the boundary spectrum
$$
\sigma_{b}(A):=\sigma(A) \cap\left\{s(A)+i^{\mathbb{R}}\right\}
$$
possesses a certain symmetric structure, called cyclicity.

Results of this type have been proved in Chapter Brifl for positive semigroups on commutative $c^{*-a l g e b r a s, ~ b u t ~ i n ~ t h e ~ n o n-c o m m u t a t i v e ~ c a s e ~}$ the situation is more complicated. While 's(A) Go(A)' still holds (see Greiner-Voigt-Wolff (1980)) the cyclicity of the boundary specm trum $\sigma_{b}(A)$ is true only under additional assumptions on the semigroup (e.g., irreducibility, see Section $I$ below).

For technical reasons we consider mostly strongly continuous semigroups on the predual of a $W^{*}$-algebra $M$ or its adjoint semigroup which is a weak*-continuous semigroup on $M$.
1. SPECTRAL THEORY FOR POSITIVE SEMIGROUPS ON PREDUALS

The aim of this section is to develop a Perron-Frobenius theory for identity preserving semigroups of Schwarz type on $W^{*}$-algebras. But as we will show in the example preceding Theorem 1.1 below the boundary spectrum is no longer cyclic. The appropriate hypothesis on the semigroup implying the desired results seems to be the concept of irreducibility.

Let us first recall some facts on normal linear functionals. If $\phi$ is a normal linear functional on a $W^{*}$-algebra $M$ then there exists a partial isometry $u \in M$ and a positive linear functional | $\mid \in \mathrm{M}_{\star}$ such that
$$
\begin{gathered}
\phi(x)=|\phi|(x u)=:(u|\phi|)(x), x \in M \\
u^{*} u=s(|\phi|)
\end{gathered}
$$
where $s(|\phi|)$ denotes the support projection of $|\phi|$ in $M$. We refer to this as the polar decomposition of $\phi$ [Takesaki (1979), Theorem III.4.2]. In addition, $|\phi|$ is uniquely determined by the following two conditions [Takesaki (1979), Proposition III.4.6]:
$$
\|\phi\|=\||\&|\| .
$$
(*)
$$
|\phi(x)|^{2} \leqq|\phi|\left(x x^{\star}\right) \quad(x \in M)
$$

For the polar decomposition of $\phi^{*}$, where $\phi^{*}(x)=\phi^{*}\left(x^{*}\right)^{*}$, we obtain
$$
\phi^{*}=\mathrm{u}^{*}\left|\phi^{*}\right|,\left|\phi^{*}\right|=u|\phi| u^{*} \text { and } u u^{*}=s\left(\left|\phi^{*}\right|\right)
$$

It is easy to see that $u * \in s(|\phi|) M$.

If $\Psi$ is a subset of the state space of a C*-algebra $M$, then $\Psi$ is called faithful if $0 \leqq x \in M$ and $\psi(x)=0$ for all $\psi \in \Psi$ implies $x=0$. $\Psi$ is called subinvariant for a positive map $T \in(M)$ (resp., positive semigroup $T$ ) if $T^{\prime} \psi \leqq \Downarrow$ for all $\psi \subset \psi$ (resp.r $T(t) ' \psi \leq \psi$ for all $T(t) \in T$ and $\psi \in \Psi$ ). Recall that for every positive map $T \in L(M)$ there exists a state $\phi$ on $M$ such that $T^{\prime \prime} \phi=$ $r(T) \phi \quad[G r o h(1981)$, Theorem 2.1], where $r(T)$ denotes the spectral radius of $T$.

Let us start our investigation with two lemmas. Recall that fix(T) is the fixed space of $T$, i.e. the set $\{x \in M: T x=x\}$.

Lemma 1.1. Suppose $M$ to be a $C^{*-a l g e b r a ~ a n d ~} T \in L(M)$ an identity preserving schwarz map.
(a) Let b: $M \times M \rightarrow M$ be a sesquilinear map such that for all m ( m $b(z, z) \geq 0$. Then $b(x, x)=0$ for some $x \in M$ if and only if $b(x, y)=0$ and $b(y, x)=0$ for all $y \in M$.
(b) If there exists a faithful family $\Psi$ of subinvariant states for $T$ on $M$, then $F i x(T)$ is a $c *-s u b a l g e b r a$ of $M$ and $T(x y)=x T(y)$ for all $x \in F i x(T)$ and $Y \in M$.

Proof. (a) Take $0 \leqq \psi \in M^{*}$ and consider $f:=\psi o b$. Then $f$ is a positive semidefinite sesquilinear form on $M$ with values in $\mathbb{C}$. From the Cauchy-Schwarz inequality it follows that $f(x, x)=0$ for some $x \in M$ if and only if $f(x, y)=0$ and $f(y, x)=0$ for all $y \in M$. Since the positive cone $M^{*}{ }_{+}$is generating, assertion (a) is proved.
(b) Since $T$ is positive it follows $T(x)^{*}=T\left(x^{*}\right)$ for all $x \in M$. Hence Fix(T) is a self adjoint subspace of $M$, i.e. invariant under the involution on $M$. For every $x, y \in M$ let
$$
\mathrm{b}(\mathrm{x}, \mathrm{y}):=\mathrm{T}\left(\mathrm{x} y^{*}\right)-\mathrm{T}(\mathrm{x}) \mathrm{T}(\mathrm{y})^{*} .
$$

Then $b$ satisfies the assumptions of (a). If xfFix(T) then
$$
0 \leqq X^{*}=(T x)(T x)^{*} \leqq T\left(x^{*}\right)
$$
hence
$$
0 \leqq \psi\left(T\left(x x^{*}\right)-x x^{*}\right) \leqq 0 \text { for all } \psi \in \Psi
$$

But this implies $T\left(x x^{*}\right)=T(x) T(x)^{*}=x x^{*}$. Consequently, $b(x, x)=0$. Hence $T\left(X Y^{*}\right)=X T(y)^{*}$ for all $y \in M$ and (b) is proved.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-401.jpg?height=56&width=1620&top_left_y=1948&top_left_x=207) Schwarz map on $M$ and $S \in L(M)$ such that $S(x)(S X)^{*} \leqq T\left(x x^{*}\right)$ for every $x \in M$.
(a) If $v \in M$ such that $S\left(v^{*}\right)=v^{*}$ and $T\left(v^{*} v\right)=v^{*} v$, then $T(x v)=$ $S(x) v$ for all $x \in M$.
(b) suppose there exists $\phi \in M_{*}$ with polar decomposition $\phi=u|\phi|$ such that $S_{*} \phi=\phi$ and $T_{*}|\phi|=|\phi|$. If the closed subspace $s||\phi|) M$ is $T$-invariant, then $s u^{*}=u^{*}$ and $T\left(u^{*} u\right)=u^{*} u$.

Proof. (a) Define a positive semidefinite sesquilinear map $b: M \times M \rightarrow M$ by
$$
b(x, y):=T\left(x y^{*}\right)-S(x) S(y)^{*} \quad(x, y \in M)
$$

Since $b\left(v^{*}, v^{*}\right)=0$ we obtain $b\left(x^{*} v^{*}\right)=0$ for all $x \in M$ (Lemma 1.1.a), hence $T(x v)=S(x) v$.
(b) since $s(|\phi|) M$ is a closed right ideal, the closed face $\mathbf{F}:=s(|\phi|)\left(M_{+}\right) s(|\phi|)$ determines $s(|\phi|) M$ uniquely, i.e.,
$$
s(|\phi|) M=\left\{x \in M: X x^{*} \in F\right\}
$$
[Pedersen (1979), Theorem 1.5.2]. Since $T$ is a Schwarz map and $s(|\phi|) M$ is $T$-invariant, it follows $T F=F$. On the other hand, if xes (| $\mid \boldsymbol{\|} \|$ then $x x^{*} \in F$. Consequently,
$$
0 \leqq S(x) S(x)^{*} \leqq T\left(x x^{*}\right) \in F,
$$
whence $s(x) \in s(|\phi|) M$.

Next we show $T\left(u^{*} u\right)=u^{*} u$ and $S u^{*}=u^{*}$. For this recall that $\mathrm{u}^{*} \epsilon_{s}(|\phi|) M$. First of all
$$
\begin{gathered}
0 \leqq\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right)^{*} \leqq \\
\leqslant T\left(u^{*} u\right)-u^{*} S\left(u^{*}\right)^{*}-\left(S u^{*}\right) u+u^{*} u .
\end{gathered}
$$
since $S_{*} \phi=\phi, T_{*}|\phi|=|\phi|$ and $\phi=u|\phi|$ it follows
$$
\begin{gathered}
0 \leqq|\phi|\left(\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right)^{*}\right) \leqq \\
\leq 2|\phi|\left(u^{*} u\right)-|\phi|\left(S\left(u^{*}\right) u\right)^{*}-|\phi|\left(S\left(u^{*}\right) u\right)= \\
=2|\phi|\left(u u^{*}\right)-\phi\left(u^{*}\right)^{*}-\phi\left(u^{*}\right)= \\
=2\left(|\phi|\left(u^{*} u\right)-|\phi|\left(u^{*} u\right)\right)=0 .
\end{gathered}
$$

Since $\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right) \in F$ and $|\phi|$ is faithful on $F$ we obtain su* $=u^{*}$. Consequently,
$$
0 \leq u * u=\left(S u^{*}\right)\left(S u^{*}\right) * \leq T\left(u^{*} u\right)
$$

Hence $T\left(u^{\star} u\right)=u^{*} u$ by the faithfulness and $T$-invariance of $|\phi|$.

Remark 1.3. Take $S$ and $T$ as in Lemma 1.2 (b) If $V_{u * ~(r e s p . ~}^{\text {. }}$ ( $V_{u}$ ) is the map $\left(x \rightarrow x^{*}\right) \quad(r e s p .(x \rightarrow x u))$ on $M$, then $V_{u *}$ is a continuous bijection from Ms (| $\phi \mid)$ onto $M s(\mid \phi \|)$ with inverse $v_{u}$ (because $V_{u}{ }^{\circ V_{u}}{ }^{*}=I d_{M s}(|\phi|)$ and $V_{u} *{ }^{*} V_{u}=I d_{M s}(|\phi *|)$. Let $x \in M$. From $T(x u)=S(x) u$ we obtain $T(x u) u^{*}=S(x) u^{*}$. In particular, if Ms (| $\left.\phi^{*} \|\right)$ is $S$-invariant, then
$$
\left(V_{u^{*}}{ }^{\circ} T^{\circ} V_{u}\right)(x)=T(x u) u^{*}=S(x)
$$
for every $x \in M s\left(\left|\phi^{*}\right|\right)$. Let $T \mid \quad$ (resp. $S \mid$ ) be the restriction of $T$ to Ms (| $\mid$ ) (resp. of $s$ to Ms (| $\left.\phi^{*} \mid\right)$ ) . Then the following diagram is commutative :
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-403.jpg?height=415&width=977&top_left_y=1089&top_left_x=525)

In particular, o(S $)=\sigma(T \mid$ ) Therefore we may deduce spectral properties of ${ }^{s}$ from $T$ and vice versa. More concrete applications of Lemma 1.2. will follow.

We now investigate the fixed space $F i x(R):=F i x(\lambda R(\lambda)), \lambda \in D, o f a$ pseudo-resolvent $R$ with values in the predual of a w*-algebra M.

Proposition 1.4. Let $R$ be a pseudoresolvent on $D=\{\lambda \in \mathbb{C}$ : Re ( $\lambda)>0\}$ with values in the predual $M_{*}$ of a $W^{*}$-algebra $M$ and suppose $R$ to be identity preserving and of Schwarz type.
(a) If $\alpha \in R$ and $\psi \in M_{*}$ such that $(\gamma-i \alpha) R(\gamma) \psi=\psi$ for some $\gamma \in D$, then $\lambda R(\lambda)|\psi|=|\psi|$ and $\lambda R(\lambda)|\psi *|=|\psi *|$ for all $\lambda \in D$.
(b) Fix(R) is invariant uncer the involution in $M_{*}$. If $\psi \in F i x(R)$ is self adjoint, then the positive part $\psi^{+}$and the negative part $\psi^{-}$of $\psi$ are elements of $F i x(R)$.

Proof. If ( $\gamma$ - ia)R(y) $\psi=\psi$ then $(\lambda-i a) R(\lambda) \psi=\psi$ for all $\lambda \in D$. In particular, $\mu \mathrm{R}(\mu+\mathbf{i} a) \psi=\psi\left(\mu \in \mathbb{R}_{+}\right)$. For all $x \in M$ we obtain
$$
\begin{gathered}
|\psi(x)|^{2}=\mid\left\langle\mu R(\mu+i \alpha)^{\prime} x, \psi>\left.\right|^{2} \leq\right. \\
\leqq\|\psi\|<\left(\mu R(\mu+i \alpha x)^{\prime} x\right)\left(\mu R(\mu+i \alpha x)^{\prime} x\right)^{*}, \psi>\leqq \\
\leqq\|\psi\|<\mu R(\mu)^{*}\left(x x^{*}\right), \mid \psi \|^{\prime}>
\end{gathered}
$$
(D-I, Corollary 2.2). Since
$$
\begin{gathered}
\|\psi\|=\||\psi|\|=|\psi|(I)= \\
=\left\langle\mu \mathrm{R}(\mu)^{\prime} 1,\right| \psi| \rangle=\|\mu \mathrm{R}(\mu)|\psi|\|,
\end{gathered}
$$
we obtain $\mu \mathrm{R}(\mu)|\psi|=|\psi|$ by the uniqueness theorem (*) mentioned at the beginning. Therefore $|\psi| \epsilon F i x(\mathrm{~F})$. Since
$$
0 \leq\left(\mu \mathrm{R}(\mu)^{\prime} \mathrm{x}\right)\left(\mu \mathrm{R}(\mu)^{\prime} \mathrm{x}\right)^{*} \leqq \mu \mathrm{R}(\mu)^{\prime} \mathrm{XX} \mathrm{x}^{*}
$$
the map $R(\mu)$ is positive. Consequently ( $\mu+i \alpha) R(\mu) \psi^{*}=\psi *$ from which $|\psi *| \epsilon F i x(R)$ follows.
If $\quad$ ffix (R) is selfadjoint with Jordan decomposition $\phi=\phi^{+}{ }^{+} \phi^{+}$, then $|\phi|=\phi^{+}+\phi^{-}$[Takesaki (1979), Theorem III.4.2.]. From this we obtain that $\phi^{+}$and $\phi^{-}$are in Fix (R).

Corollary I.5. Let $T$ be an identity preserving semigroup of Schwarz type on $M_{*}$ with generator $A$ and suppose $P o(A) \cap i \mathbb{R} \neq \emptyset$.
(a) If a¢GR and $\psi \in \operatorname{ker}(i \alpha-A)$, then $|\psi|$ and $|\psi *|$ are elements of $\operatorname{Fix}(T)=\operatorname{ker}(A)$.
(b) Fix(T) is invariant under the involution of $M_{*}$. If $\psi \in F i x(T)$ is self adjoint, then the positive part $\psi^{+}$and the negative part $\psi{ }^{-}$of $\psi$ are elements of $F i x(T)$.

The proof follows immediately from D-I, Corollary 2.2 and the fact that $\operatorname{ker}(A)=\operatorname{Fix}(\lambda R(\lambda, A))$ for all $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda)>0$.

If $T$ is the semigroup of translations on $L^{l}(\mathbb{R})$ and $A^{\prime}$ the gene-
rator of the adjoint weak*-semigroup, then $P o(A) \quad$ i $A=\varnothing$, while Po(A') $\cap$ i $=$ iR , For that reason we cannot expect a simple connection between these two sets. But as we shall see below, if a semigroup on the predual of a $\mathrm{W}^{*}-\mathrm{algebra}$ has sufficiently many invariant states, then the point spectra of $A$ and $A^{\prime}$ contained in iR are identical. Helpful for these investigations will be the next lemma.

Lemma 1.6. Let $R$ be a pseudo-resolvent on $D=\{\lambda \in \mathbb{C} ; \operatorname{Re}(\lambda)>0\}$ with values in a Banach space $E$ such that $\|\mu \mathrm{R}(\mu+i \alpha)\| \leq I$ for all $(\mu, \alpha) \in \mathbb{R} \times \mathbb{R}$. Then
```
dim Fix(\lambdaR(\lambda + i\alpha)) 仓 dim Fix(\lambdaR(\lambda + i\alpha|')
```
for all $\lambda \in D$.

Proof. Let $(\mu, \alpha) \in \mathbb{R}_{+} \times \mathbb{R}$ and $S:=\mu R(\mu+i \alpha)$. since $s$ is a contraction, its adjoint $S^{\prime}$ maps the dual unit ball $E^{\prime}$ i into itself. Let $u$ be a free ultrafilter on $\left[1,{ }^{\infty}\right)$ which converges to 1 . Since $E^{\prime}{ }^{\prime}$ is $\sigma\left(E^{\prime}, E\right)$-compact,
$$
\psi_{o}:=\operatorname{Iim} U^{(\lambda-1) R(\lambda, S)^{\prime} \psi}
$$
exists for all $\psi \in E^{\prime}$, Since $S^{\prime}$ is $\sigma\left(E^{\prime}, E\right)$-continuous and since $S^{\prime} R(\lambda, S)^{\prime}=\lambda R\left(\lambda, S^{\prime}\right)-I d$ we conclude $\psi_{o} \in F i x\left(S^{\prime}\right)$.

Take now $0 \neq x_{0} \in F 1 x(S)$ and choose $\psi \in E^{*}{ }_{I}$ such that $\psi\left(x_{0}\right)$ is different from zero. From the considerations above it follows
$$
\psi_{0}\left(x_{0}\right)=\operatorname{Iim} U(\lambda-1) \psi\left(R(\lambda, S) x_{0}\right)=\psi\left(x_{0}\right) \neq 0
$$
hence $0 \neq \psi_{o} \in F i x(S)$. Therefore Fix(s') separates the points of Fix (S) . From this it follows that
```
dim Fix(S) S dim Fix(S') .
```

Since $R$ and $R^{\prime}$ are pseudo-resolvents, the assertion is proved.

Corollary 1.7. Let $T$ be a semigroup of contractions on a Banach space $E$ with generator A . Then
```
dim ker(i\alpha - A) \leqq dim ker(i\alpha - A')
```
for all $\alpha \in R$.

This follows from Lemma 1.6 because $F i x(\lambda \mathrm{f}(\lambda+i \alpha))=\operatorname{ker}(i a-A)$.

Proposition 1.8 . Let $T$ be an identity preserving semigroup of Schwarz type with generator $A$ on the predual of a $W^{*}$-algebra and suppose that there exists a faithful family $\Psi$ of T-invariant states. Then for all $a \in \mathbb{R}$ we have
```
dim ker(i\alpha - A) = dim ker(ia - A')
```
and
$$
\operatorname{Po}(A) \cap i \mathbb{P}_{1}=P \sigma\left(A^{r}\right) \cap \mathbf{i} R .
$$

Proof. The inequality dim ker(ia - A) $\leqslant$ dim ker (io - $\left.A^{\mp}\right)$ follows from Corollary 1.7 .

Let $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ and $R$ the pseudo-resolvent induced by $R(\lambda, A)$ on $D$. Then $R$ is identity preserving and of Schwarz type. Take $i \alpha \in P o(A)(\alpha \in R)$ and choose $0<\mu \in \mathbb{R}$. If $\psi_{\alpha} \in M_{*}$ is of norm one with polar decomposition $\psi_{a}=u_{a}\left|\psi_{\alpha}\right|$ such that $\psi_{a}=(\mu-i \alpha) R(\mu) \psi_{a}$ then $\mu \mathrm{R}(\mu)\left|\psi_{\alpha}\right|=\left|\psi_{a}\right| \quad$ (Proposition 1.4.a). Since
$$
\mu R(\mu)^{\prime}\left(1-s\left(\left|\psi_{\alpha}\right|\right)\right) \leqq 1-s\left(\left|\psi_{\alpha}\right|\right)
$$
we obtain $\mu R(\mu)^{\prime} s\left(\left|\psi_{a}\right|\right)=s\left(\left|\psi_{\alpha}\right|\right)$ by the faithfulness of $\Psi$. Hence the maps $S:=(\mu-i \alpha) R(\mu)^{\prime}$ and $T:=\mu R(\mu)^{\prime}$ fulfil the assumptions
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-406.jpg?height=50&width=1615&top_left_y=1894&top_left_x=232) implies $u_{\alpha}^{*} \in D\left(A^{\top}\right)$ and $A^{\prime} u_{\alpha}^{*}=i a u_{\alpha}^{*}$.

If $\operatorname{ia\in Po(A'),~} \alpha \in \mathbb{R}$, choose $0 \neq v_{0}$ such that
$$
v_{\alpha}=(\mu-i \alpha) R(\mu)^{\prime} v_{\alpha} \quad\left(\mu \in \mathbb{R}_{+}\right)
$$
and $\psi \in \Psi$ such that $\psi\left(v_{\alpha} v_{\alpha}^{*}\right) \neq 0$. since
$$
\begin{gathered}
0 \leqslant v_{\alpha} v_{a}^{*}=\left((\mu-i \alpha) R(\mu)^{\prime} v_{\alpha}\right)\left((\mu-i \alpha) R(\mu)^{\prime} v_{\alpha}\right)^{*} \leq \\
\leq \mu R(\mu)^{\prime}\left(v_{\alpha} v_{\alpha} *\right),
\end{gathered}
$$
we obtain $\mu R(\mu)^{\prime}\left(v_{\alpha} v_{\alpha}^{*}\right)=v_{\alpha} v_{\alpha}{ }^{*}$ because $\Psi$ is faithful.

Hence from Lemma 1.2.a it follows
$$
\mu \mathrm{R}(\mu)^{\prime}\left(x v_{\alpha}^{*}\right)=\left(\left(\mu-i_{\alpha}\right) \mathrm{R}(\mu)^{\prime} x\right) v_{a}^{*}
$$
for all $x \in M$. Let $\psi_{a}$ be the normal inear functional $\left(x \rightarrow \psi\left(x v_{a}^{*}\right)\right)$ on $M$ and note that $\psi_{\alpha}\left(v_{\alpha}\right) \neq 0$. Then
$$
\begin{gathered}
\left.<x,(\mu-i \alpha) R(\mu) \psi_{\alpha}\right\rangle=\left\langle\left(\left(\mu-i_{\alpha}\right) R(\mu)^{*} x\right) v_{\alpha}^{*}, \psi\right\rangle= \\
\left.<\mu R(\mu)^{\prime}\left(x v_{\alpha}^{*}\right), \psi\right\rangle=\psi\left(x v_{\alpha}^{*}\right)=\psi_{\alpha}(x)
\end{gathered}
$$
for all $x \in M$. Consequently $i_{a} \in \mathrm{P}_{\sigma}(A)$ and
```
dim ker(ia - A') s dim ker(ia - A) ,
```
which proves the assertion.

Remark 1.9. From the above proof we obtain the following: If $0 \neq \psi_{\alpha}$ ker ( $\left.i_{\alpha}-A\right)$ with polar decomposition $\psi_{\alpha}=u_{\alpha}\left|\psi_{\alpha}\right|(\alpha \in \mathbb{R})$ then $A^{\prime} u_{a}=i_{a} u_{a}$. Conversely, if $0 \neq v_{a} \in k e r\left(i_{a}-A^{\prime}\right)$, then there exists $\psi \in \Psi$ such that $\psi\left(v_{a} v_{a}^{*}\right) \neq 0$ and the normal linear form
$$
\psi_{\alpha}:=\left(x \rightarrow \psi\left(x v_{\alpha}^{*}\right)\right)
$$
is an eigenvector of $A$ pertaining to the eigenvalue $i o$.

If $T$ is a $C_{o}$-semigroup of Markov operators on a commutative $C^{*}-a 1-$ gebra with generator $A$, it has been shown in B-III, that the boundary spectrum $\sigma(A) \quad n \quad i \mathbb{R}$ of its generator is additively cyclic. This is no longer true in the non commutative case:

For $0 \neq \lambda \in i \mathbb{R}$ and $t \in \mathbb{R}$ let
$$
u_{t}:=\left(\begin{array}{ll}
1 & 0 \\
0 & e^{\lambda t}
\end{array}\right) \quad \in M_{2}(c)
$$

The semigroup of *-automorphisms $\left(x+u_{t} x_{t}{ }^{*}\right)$ on $M_{2}(c)$ is identity
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-408.jpg?height=47&width=1617&top_left_y=336&top_left_x=228) $\left[0, \lambda, \lambda^{*}\right\}$ hence is not additively cyclic.

It turns out that, in order to obtain a non conmutative analogue of the Perron-Frobenius theorems, one has to consider semigroups which are irreducible. Recall that a semigroup $S$ of positive operators on an ordered Banach space ( $E, E_{+}$) is called irreducible if no closed face of $E_{+}$, different from $\{0\}$ and $E_{+}$, is invariant under $S$. Here a face $F$ in $E$ is a subcone of $E_{+}$such that the conditions $0 \leqq x \leqq y$, $x \in E$, $y \in F$ imply $x \in F$ (compare Definitions 3.1 in $B-I I I$ and $C-I I I)$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-408.jpg?height=50&width=1623&top_left_y=1026&top_left_x=225) maps on $M$ weak* -irreducible, if no $\sigma\left(M_{*}\right)$-closed face of $M_{+}$is S-invariant. Since the norm closed faces of $M_{*}$ and the o(M, $M_{*}$ )closed faces of $M$ are related by formation of polars with respect to the dual system $M_{*} M_{*}$ (see [Pedersen (1979), Theorem 3.6.11 and Theorem 3.10.7.7) a semigroup $S$ is (norm) irreducible on $M_{*}$ if and only if its adjoint semigroup is weak*-irreducible.

Theorem I.10. Let $T$ be an irreducible, identity preserving semigroup of schwarz type with generator $A$ on the predual of a $W^{*}-a I-$ gebra and suppose $P_{g}(A)$ i i $\neq \varnothing$.
(a) The fixed space of $T$ is one dimensional and spanned by a faithful normal state.
(b) Po(A) $\cap$ iR is an additive subgroup of $i \mathbb{R}$,
$$
\sigma(A)=\sigma(A)+(\operatorname{Po}(A) \cap i \mathbb{R})
$$
and every eigenvalue in if is simple.
(a)* The fixed space of the adjoint weak*-semigroup T* is onedimensional.
(b)* $P_{\sigma}\left(A^{\prime}\right) \| i \mathbb{R}=P_{o}(A) \quad$ $\quad i$ f for the generator $A^{\prime}$ of the adjoint semigroup, and every y€po(A') $\quad$ i ir $i s$ simple.

Proof. Since $\mathrm{P}_{\sigma}(\mathrm{A}) \quad \mathrm{C}$ iR $\neq \emptyset$ there exists $\psi \in \mathrm{Fix}(T)+$ of norm one (Corollary 1.5 ). If $F:=\left\{X \in M_{+} ; \psi(x)=0\right\}$ then $F$ is a o( $M_{*} M_{*}$ ) closed, $T^{\prime}$-invariant face in $M$, hence $F=\{0\}$. Therefore every $0 \neq \psi \in F i x(T)+i s$ faithful. Let $\psi_{1}, \psi_{2} \in F i x(T){ }_{+}$be states such that
$f:=\psi_{I}-\psi_{2}$ is different from zero. If $f=f^{+}-f^{-}$is the Jordan decomposition of $f$, then $f^{+}$and $f^{-}$are elements of $F i x(T)$, whence faithful. since the support projections of these two normal linear functionals are orthogonal, we obtain $f^{+}=0$ or $f^{-}=0$ which implies $\psi_{1} \leqslant \psi_{2}$ or $\psi_{2} \leqslant \psi_{I}$. Consequently $\psi_{2}=\psi_{1}$. Since Fix(T) is positively generated (Corollary 1.5), Fix (T) $=\mathbb{C}_{\phi}$ for some faithful normal state $\phi$.

Let $\mu \in \mathbb{R}+$ and $\alpha \in \mathbb{R}$ such that $i \alpha \in P o(A)$. If $\psi_{\alpha}=u_{\alpha}\left|\psi_{\alpha}\right|$ is a normalized eigenvector of $A$ pertaining to $i \alpha$, then $\phi=\left|\psi_{0}\right|=\left|\psi_{a}{ }^{*}\right|$ by Corollary 1.5 and the above considerations. Hence $u_{\alpha} u_{\alpha}{ }^{*}=u_{\alpha}^{*} u_{\alpha}=$ $s(\phi)=1$. Since
$$
(\mu-i \alpha) R(\mu, A) \psi_{a}=\psi_{a}
$$
and
$$
\mu \mathrm{R}(\mu, \mathrm{~A})\left|\psi_{a}\right|=\left|\psi_{\alpha}\right|
$$
we obtain by Lenma I. 2.b that
(1) $\mu \mathrm{R}(\mu, \mathrm{A})=\mathrm{V}_{a} \rho \mu \mathrm{R}\left(\mu+\mathrm{i}_{a}, \mathrm{~A}\right)=\mathrm{V}_{a}^{-1}$
where $V_{a}$ is the map $\left(x+x_{\alpha}\right)$ on $M$. Similarly for i $\beta \in P(A)$, we find $V_{\beta}$ such that $1=u_{\beta} u_{\beta}^{*}=\mathrm{u}_{\beta} \mathrm{u}_{\beta}{ }^{*}$ and
(2) $\mu R(\mu, A)=V_{\beta}^{o \mu R}(\mu+i \beta, A) \circ V_{\beta}^{-I}$.

Hence
$$
\begin{equation*}
\mu \mathrm{R}(\mu, A)=V_{\alpha \beta} \mu \mathrm{R}(\mu+i(\alpha+\beta), A)=V_{\alpha \beta}^{-1} \tag{3}
\end{equation*}
$$
where $V_{a \beta}:=V_{a} V_{\beta}$. Since $u_{a}$ is unitary in $M$, it follows from (1) that ia is an eigenvalue which is simple because Fix(T)= Fix ( $\mu \mathrm{R}(\mu, A)$ is one dimensional. From (3) it follows that $i(\alpha+\beta) \in \operatorname{Po}(A)$ since $0 \in \operatorname{Po}(A)$ and $V_{\alpha \beta}$ is bijective. From the identity (I) we conclude that $\sigma(R(\mu, A))=\sigma(R(\mu+i \alpha))$, which proves
$$
\sigma(A)+(P \sigma(A) \cap i \mathbb{R}) \subseteq \sigma(A)
$$

The other inclusion is trivial since $0 \in P(A)$.

Remarks I.Il. (a) Let $\quad$ be the normal state on m such that $\operatorname{Fix}(T)=\mathbb{C}$ and let $H:=\operatorname{Po}(A) \cap i . R$. From the proof of Theorem l.IU it follows that there exists a family $\left\{u_{\eta}: \eta \in H\right\}$ of unitaries in $M$ such that $A^{r} u_{\eta}=-\eta u_{\eta}$ and $A\left(u_{\eta} \phi\right)=\eta\left(u_{\eta} \phi\right)$ for all $\eta \in H$.
(b) If the group $H$ is generated by a single element, $i, e ., H=i \gamma \mathbb{Z}$ for some $\gamma \in R$ then the family $\left\{u_{\gamma}^{k}: k \in \mathbb{Z}\right\}$ is a complete family of eigenvectors pertaining to the eigenvalues in $H$, where $u_{Y} \in M$ is unitary such that $A^{\prime} u_{Y}=i_{Y} u_{Y}$.

Proposition 1.12 . Suppose that $T$ and $M$ satisfy the assumptions of Theorem 1.10, and let $N_{*}$ be the closed Iinear subspace of $M_{*}$ generated by the eigenvectors of $A$ pertaining to the eigenvalues in $i \mathbb{R}$. Denote by $T_{0}$ the restriction of $T$ to $N_{*}$. Then
(a) $G:=\left(T_{0}\right)^{-} \underline{C} L_{S}\left(N_{*}\right)$ is a compact, Abelian group.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-410.jpg?height=64&width=1238&top_left_y=1307&top_left_x=232)

Proof. For $\eta \in H:=\operatorname{Po}(A)$ in iR let
$$
U(\mathrm{r}):=\left\{\psi \in \mathrm{D}(\mathrm{~A}): A_{\psi}=\mathrm{n} \psi\right\}
$$
and $U=\{U(\pi): \pi \in H\}$. Then $\left(\operatorname{span}[J)^{-}=N_{*}\right.$. For each $\psi \in U$ there exists $\eta \in H$ such that
$$
\left\{\mathbb{T}_{0}(t) \psi: t \in \mathbb{R}_{+}\right\}=\left\{\mathrm{e}^{-\pi t} \psi: t \in \mathbb{R}_{+}\right\}
$$

Consequently this set is relatively compact in $L_{s}\left(\mathbb{N}_{*}\right)$. From [Schaefer (1966),III.4.5] we obtain that $G$ is compact.

Next choose $\psi_{1}$, $\cdots \psi_{n} \in \mathbb{J}$, $0<\operatorname{set}$ and $\delta>0$. Since $T_{0}(t) \psi_{i}=$ $e^{\pi_{i}} \psi_{i}(l s i s n)$ for some $\eta_{i} \in H$, it follows from a theorem of Kronekker (see, [Jacobs (1976), satz 6.1., p.77]) that there exists $s$ \& $t$ such that
$$
\left|(1,1, \ldots, 1)-\quad\left(e^{\pi} 1^{t}, \quad e^{\pi} 2^{t}, \ldots, \quad e^{\pi} n^{t}\right)\right|<\delta,
$$
hence
$$
\sup \left\{\left\|\psi_{i}-T_{0}(t) \psi_{i}\right\|: 1 \leq i \leqq n\right\}<\delta
$$
or $I d \mid N_{*} \in\left\{T_{o}(t): t>5\right\}^{-} G_{s}\left(N_{*}\right)$.

Finally we prove the group property of $G$. Let $v$ be an ultrafilter on $\mathbb{R}_{\text {such that }}$ lim $V_{o}(t)=I d$ in the strong operator topology. For positive $s \in \mathbb{R}$ let $S:=\lim _{V} T(t-s)$. Then $S T_{0}(s)=T_{o}(s) S=I d$, hence $T_{o}(s)^{-1}$ exists in $G$ for all $s \in \mathbb{R}_{+}$. From this it follows that $G$ is a group.

Remark I.I3. (a) Let $k: \sqrt[R]{ } \rightarrow G$ be given by
$$
k(t)= \begin{cases}T_{0}(t) & \text { if } 0 \leq t \\ T_{0}(t)^{-1} & \text { if } t \leqq 0\end{cases}
$$

Then $k$ is a continuous homomorphism with dense range, i.e. ( $k, k$ ) is solenoidal (see [Hewitt-Ross (1963)]).
(b) The compact group $G$ and the discret group $P o(A) \quad \cap i \mathbb{R}$ are dual in the sense of locally compact Abelian groups.
(c) Let (G,k) be a solenoidal compact group and let $N_{*}=L^{I}(G)$. Then the induced lattice semigroup $T=(\kappa(t))_{t \geq 0}$ fulfils the assertions of Theorem l. 10 . For example, if $G$ is the dual of $\mathbb{R}_{\mathrm{a}}$, then $\operatorname{Po}(A) \quad \cap \mathrm{i} R=\mathrm{i} R$. Since the fixed space of $k(t)$ is given by
$$
F i x(k(t))=\left(\operatorname{span} \cup k \in T \operatorname{ker}\left(\frac{2 \pi i k}{t}-A\right)\right)^{--}
$$
no $T(t) \in T$ is irrecucible.
(d) If $T$ is the irreducible semigroup of schwarz type on the predual of $B(H)$ given in [Evans (I977)] then Po(A) $\cap$ i $\mathbb{R}=\varnothing$.

\section*{2. SPECTRAL PROPERTIES OF UNIFORMLY ERGODIC SEMIGOUPS}

The aim of this section is the study of spectral properties of semigroups which are uniformly ergodic, identity preserving and of Schwarz type. For the basic theory of uniformly ergodic semigroups on Banach spaces we refer to Dunford-Schwartz (1958).

Our first result yields an estimate for the dimension of the eigenspaces pertaining to eigenvalues of a pseudo-resolvent.

Proposition 2.1. Let $R$ be an identity preserving pseudo-resolvent of Schwarz type on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ with values in the predual of a $W^{*}$-algebra $M$. If Fix( $\lambda$ R( $\left.\lambda\right)$ ) is finite dimensional for some $\lambda \in D$, then
```
dimFix((Y - ia)R(y)) = dim Fix(\lambdaR(\lambda))
```
for all $Y \in D$ and $a \in \mathbb{P}$.

Proof. By D-IV, Remark 3.2.c we may assume without loss of generality that there exists a faithful family of R -invariant normal states on $M$. In particular the fixed space $N$ of the adjoint pseudoresolvent $R^{\prime}$ is a $W^{*}$-subalgebra of $M$ with $1 \in \mathbb{N}$ (by Lemma l.1.b). Since $N$ is finite dimensional there exist a natural number $n$ and a set $P:=\left\{p_{1}, \ldots, p_{n}\right\}$ of minimal, mutually orthogonal projections in ${ }^{N}$ such that $\sum_{k=1} P_{k}=1$. These projections are also mutually orthogonal in $M$ with sum 1 .

Let $R_{j}$ be the $o\left(M, M_{*}\right)$-closed right ideal $p_{j}^{M}$ and $L_{j}$ the closed left invariant subspace $M_{*} P_{j}(I \leqq j \leqq n)$. The map $\mu R(\mu)^{\prime}, \mu \in R_{+}$is an identity preserving Schwarz map . From Lemma I.l.b we therefore obtain that for all $x \in N$ and $y \in M$,
$$
\mu R(\mu)^{\prime}(x y)=x\left(\mu R^{\top}(\mu) y\right) .
$$

In particular, $R_{j}$, resp., $L_{j}$ are invariant under $R^{\prime}$, respectively, $R$. Furthermore, if $\psi \in L_{j}$ with polar decomposition $\psi=u|\psi|$, then $u^{*} u=s(\mid \psi!) \leqq p_{j}$. Consequentiy, $|\psi| \in L_{j}$. Let now $\alpha \in \mathbb{R}$ and suppose that there exists $\psi_{\alpha} \in L_{j}$ of norm $I, \psi_{\alpha}=u_{\alpha}\left|\psi_{\alpha}\right|$, such that
$$
\psi_{a} \in \mathrm{Fix}((\lambda-\mathbf{i} a) \mathrm{R}(\lambda)), \lambda \in \mathrm{D} .
$$
since $\lambda R(\lambda)\left|\psi_{a}\right|=\left|\psi_{\alpha}\right| \quad$ (Proposition 1.4), we obtain
$$
\mu R(\mu)^{\prime}\left(1-s\left(\left|\psi_{\alpha}\right|\right)\right) \leqq\left(1-s\left(\left|\psi_{\alpha}\right|\right), \mu \in R_{+} .\right.
$$

From the existence of a faithful family of $R$-invariant normal states and since $R^{r}$ is identity preserving it follows that
$$
\mu R(\mu) ' s\left(\left|\psi_{\alpha}\right|\right)=s\left(\left|\psi_{\alpha}\right|\right) .
$$

Thus $s\left(\left|\psi_{\alpha}\right|\right) \leqq p_{j}$ and even $s\left(\left|\psi_{\alpha}\right|\right)=p_{j}$ by the minimaity property of $P_{j}$. On the other hand, $\psi_{a} \epsilon_{F i x}((\lambda+i a) R(\lambda))$. As above we obtain
$$
\mu R(\mu)^{\prime} s\left(\left|\psi_{\alpha} *\right|\right)=s\left(\|_{\alpha} * \mid\right) .
$$

Consequently, the closed left ideals $M s\left(\left|\psi_{a} *\right|\right)$ and $M s\left(\left|\psi_{a}\right|\right)$ are R'-invariant.

Next fix $\mu \operatorname{cin}_{+}$, let $\mathcal{S}:=(\mu-i \alpha) R(\mu)^{\prime}$ and $T=\mu \mathrm{R}(\mu)^{\prime}$. Then $(S X)(S X)^{*} \leqq T\left(x x^{*}\right), S_{*}\left(\psi_{\alpha}^{*}\right)=\psi_{\alpha}{ }^{*}, T_{*}\left(\left|\psi_{\alpha}^{*}\right|\right)=\left|\psi_{\alpha}^{*}\right|$, and $T$ is an identity preserving schwarz map. Since $s\left(\|_{a} * \mid\right) M$ is $T$-invariant, the assumptions of Lenma 1.2 are fulfilled and we obtain for every $x \in M$
$$
S(x) u_{\alpha} *=T\left(x u_{\alpha} *\right) .
$$

Since the closed left ideal $\mathrm{Mp}_{\mathrm{j}}$ is S -invariant it follows
$$
S(x)=T\left(x u_{a}^{*}\right) u_{\alpha} \quad, x \in M p_{j},
$$
(see Remark 1.3). Since $u_{\alpha}$ does not depend on $\mu \in \mathbb{R}_{+}$we obtain for all $\mu \in \mathbb{R}_{+}$
$$
\mu \mathrm{R}(\mu+i \alpha)^{\prime} \mathrm{x}=\mu \mathrm{R}(\mu)^{\prime}\left(x u_{\alpha}^{*}\right) \mathrm{u}_{\alpha} .
$$

Consequently, the holomorphic functions $\left(\mu \rightarrow \mu R(\mu){ }^{\prime}\left(x u_{\alpha}\right) u_{\alpha}{ }^{*}\right)$ and $\left(\mu \rightarrow \mu R(\mu+i \alpha)^{\prime} x\right)$ coincide on $R_{+}$from which we conc1ude
$$
\lambda \mathrm{R}(\lambda+i \alpha)^{\prime} \mathrm{x}=\lambda \mathrm{R}(\lambda)^{\prime}\left(\mathrm{xu}_{\alpha}^{*}\right) \mathrm{u}_{\alpha}
$$
for every $x \in D$ and all $x \in M p_{j}$. Since the map $\left(y \rightarrow y u_{a}\right)$ is a continuous bijection from $M\left(u_{\alpha} u_{a}{ }^{*}\right)$ onto $M p_{j}$ and its inverse is the map ( $\mathrm{y} \rightarrow \mathrm{yu}_{\alpha}{ }^{*}$ ), we can deduce that
$$
\begin{aligned}
\operatorname{dim} \operatorname{Fix}\left((\lambda-i \alpha) R(\lambda) \cdot \mid M p_{j}\right) & =\operatorname{dim} \operatorname{Fix}\left(\lambda R(\lambda), \mid!M\left(u_{\alpha} u_{\alpha}^{*}\right) \leq\right. \\
& \leqq \operatorname{dim} F i x\left(R^{\prime}\right) .
\end{aligned}
$$

Since $\oplus_{j=I}^{n} M P_{j}=M$ and $\oplus_{j=1}^{n} L_{j}=M_{*}$ we obtain
$$
\begin{gathered}
\operatorname{dim} F i x((\lambda-i \alpha) R(\lambda) ')) \cdots \operatorname{dim} F i x(\lambda R(\lambda) ')= \\
=\operatorname{dim} F i x(\lambda R(\lambda))
\end{gathered}
$$
and the assertion follows from Lemma 1.6.

Before going on let us recall the basic facts of the ultrapower $\hat{E}$ of a Banach space $E$ with respect to some free ultrafilter $U$ on $N$ (compare A-I, 3.6). If $Q^{\infty}(E)$ is the Banach space of all bounded functions on $k$ with values in $E$, then
$$
c_{U}(E):=\left\{\left(x_{n}\right) \in Q^{\infty}(E): \operatorname{iim}_{U}\left\|x_{n}\right\|=0\right\}
$$
is a closed subspace of $\ell^{\circ}(E)$ and equal to the kernel of the seminorm
$$
\left\|\left(x_{n}\right)\right\|:=1 \lim _{u}\left\|x_{n}\right\|_{i}^{1},\left(x_{n}\right) \epsilon_{i}^{\infty}(E)
$$

By the ultrapower $\hat{E}$ we understand the quotient space $\ell^{\infty}(E) / C U(E)$ with norm
$$
\|\hat{x}\|=\operatorname{Iim}_{U}\left\|x_{n}\right\|, \quad\left(x_{n}\right) \in \hat{x} \in \hat{E}
$$

Moreover, for a bounded Iinear operator $T \in(E)$, we denote by $\hat{T}$ the well defined operator $\hat{T} \hat{x}:=\left(T x_{n}\right)+c_{U}(E),\left(X_{n}\right) \in \hat{x}$. It is clear by virtue of $\left(x \rightarrow(x, x, \ldots)+c_{U}(E)\right)$ that each $x \in E$ defines an element $\hat{x} \in \hat{E}$. This isometric embedding as well as the operator map $(T \rightarrow T)$ are called canonical. In particular, if $R:(D \rightarrow L(E))$ is a pseudo-resolvent, then
$$
\hat{R}:=(\lambda \rightarrow R(\lambda) \hat{}): D \rightarrow L(\hat{E})
$$
is a pseudo-resolvent, too. Recall that the approximative point spectrum $A \circ(T)$ is equal to the point spectrum Po( $\hat{T}$ ) (see, e.g., [Schaefer (1974), Chapter V, SIJ). This construction gives us the possibility to characterize uniformly ergodic semigroups with finite dimensional fixed space.

Lemma 2.2. Let $R$ be a pseuco-resolvent on $D=\{\lambda \in \mathbb{C} \operatorname{Re}(\lambda)>0\}$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-414.jpg?height=55&width=1340&top_left_y=2394&top_left_x=232)
$$
0<\text { dimpix }\left(\left(\lambda-i_{a}\right) \hat{R}(\lambda)\right)<\infty \text { for some } \lambda \in D, \alpha \in R
$$
and the canonical extension $\hat{\mathrm{R}}$ on some ultrapower $\hat{\mathrm{E}}$.

Then the following assertions hold:
(a) $(\lambda-i a)^{-1}$ is a pole of the resolvent $R(\ldots R(\lambda))$ for all $\lambda \in D$. (b) dim Fix( ( $\lambda-i \alpha) \mathrm{R}(\lambda))=\operatorname{dim} \operatorname{Fix}((\lambda-i \alpha) \mathrm{R}(\lambda))$ for all $\lambda \in \mathrm{D}$.
(c) ia is a pole of the pseuco-resolvent $R$ and the residue of $R$ and $R(., R(\lambda))$ in $i \alpha$ respectively $(\lambda-i a)^{-1}$ are identical.

Proof. Take a normalized sequence $\left(X_{n}\right)$ in $E$ with
$$
\lim _{n}\left\|(\lambda-i \alpha) R(\lambda) x_{n}-x_{n}\right\|=0
$$

The existence of such a sequence follows from the fact that the fixed space of $(\lambda-i \alpha) R(\lambda)$ is non trivial. suppose ( $x_{n}$ ) is not relatively compact. Then we may assume that there exists $\delta>0$ such that
$$
\left\|x_{n}-x_{m}\right\|>\delta \text { for } n \neq m
$$

Take $k \in \mathbb{N}$ and let $\hat{x}_{k}$ be the image of $\left(x_{n+k}\right)$ in $\hat{E}$. Since
$$
1 m_{n}\left\|(\lambda-i \alpha) R(\lambda) x_{n+k}-x_{n+k}\right\|=0,
$$
the so defined $\hat{x}_{k}{ }^{\prime} s$ belong to $\left.F i x(\lambda-i a) \hat{R}(\lambda)\right)$. Since this space is finite dimensional there exist $j<d$ such that
$$
\left\|\hat{x}_{j}-\hat{x}_{Q}\right\| \leqq \frac{\delta}{2}
$$

From the definition of the norm in $\hat{E}$ it follows that there are natural numbers $n<m$ such that
$$
\left\|x_{n}-x_{m}\right\| \leq \frac{\delta}{2}
$$
which leads to a contradiction. Therefore every approximate eigenvector of $(\lambda-i \alpha) R(\lambda)$ pertaining to $I$ is relatively compact. In particular it has a convergent subsequence from which it follows that the fixed space of $(\lambda-i \alpha) R(\lambda)$ is non trivial.
obviously
```
dim Fix((\lambda-ia)R(\lambda)) E dim Fix((\lambda - ial庳(\lambda)).
```

If the last inequality is strict, then there exists $\gamma>0$ and $a$ normalized $\hat{x} \in F i x(\lambda-i \alpha) \hat{R}(\lambda))$ such that
$$
\gamma \leqslant \| \hat{y}-\left.\hat{x}\right|_{i} ^{n}
$$
for all $y \in F i x((\lambda-i G) R(\lambda))$. Take a normalized sequence ( $\left.x_{n}\right) \in \hat{X}$. Then $\left(x_{n}\right)$ has a convergent subsequence whence we may assume that Iim $_{n} x_{n}=z$ exists in $E$. Thus $0 \neq z \in F i x((\lambda-i \alpha) R(\lambda))$. From this we obtain the contradiction
$$
\gamma \leq\|\hat{z}-\hat{x}\|_{j}=\lim \left\|z-x_{n}\right\|=0
$$

Consequently
$$
\operatorname{dim} F i x((\lambda-i a) R(\lambda))=\operatorname{dim} F i x(\lambda-i a) \operatorname{R}(\lambda))
$$

Let $\left\{x_{1}, \ldots x_{n}\right\}$ be a base of Fix( $\lambda$ - ialR(X)) and choose $\left\{\phi_{1} \ldots \phi_{n}\right\}$ in Fix( $\lambda$ - ia)R(i) $\left.{ }^{\prime}\right)$ such that $\phi_{k}\left(x_{j}\right)=\delta_{k, j}$ (Lemma 1.6). Then
$$
E=\operatorname{Fix}((\lambda-i \alpha) R(\lambda)) \quad \oplus \quad\left(\cap \underset{j=1}{n} \operatorname{ker}_{j}\right)
$$
where both subspaces on the right are ( $A$ - ia)R(A)-invariant and I is a pole of $(\lambda-i \alpha) R(\lambda) \mid F i x((\lambda-i a) R(\lambda))$ by the finite dimensionality of $F i x((\lambda-i a) R(\lambda))$. Suppose $I$ belongs to the spectrum of $S$ where $S$ is the restriction of ( $\lambda$-io) R( $\lambda$ ) to $n_{j=1}^{n}$ ker ${ }_{j}$. Then there
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-416.jpg?height=87&width=1423&top_left_y=1781&top_left_x=217)
$$
\lim _{n}\left\|(\lambda-i \Omega) R(\lambda) Y_{n}-Y_{n}\right\|=0 .
$$

Therefore $\left(y_{n}\right)$ has an accumulation point different from zero in
$$
\text { Fix }(\lambda-i a) R(\lambda)) \quad \Gamma\left(n_{j=1}^{n} \operatorname{ker}_{j}\right)
$$

This contradiction implies that $I$ does not belong to the spectrum of $S$. Since Fix ( $\lambda$ - ialR( $\lambda]$ ) is finite dimensional, it follows from general spectral theory that $(\lambda-i \alpha)^{-1}$ is a pole of $R(. r R(\lambda))$ for every $\lambda$. Thus (a) and (b) are proved. Assertion (c) follows from the resolvent equality as in the proof of [Greiner (198I), Proposition I.2].

Proposition 2.3. Let $T$ be a semigroup of contractions on a Banach space $E$ with generator $A$. Then the following assertions are equivalent:
(a) Each io, a $\in \mathbb{R}$, is a pole of the resolvent $R(., A)$ such that the corresponding residue has finite rank.
(b) dim Fix ( $\lambda-\operatorname{ial} \hat{\mathrm{R}}(\lambda, A))<\infty$ for some (hence all) $\lambda \in \mathbb{C}$, Re $(\lambda)>0$ and the canonical extensions $\hat{R}(\lambda, A)$ of $R(\lambda, A)$ to some ultrapower.

Proof. Let $P_{a}$ be the residue of the resolvent $R(\ldots A)$ in ia. Then $P_{\alpha}=\operatorname{Iim}_{\lambda \rightarrow i \alpha}(\lambda-i \alpha) R(\lambda, A)$ in the operator norm of $L(E)$. Since the canonical map $(T \rightarrow \hat{T})$ is isometric and since $\hat{E}$ is an ultrapower, we obtain
$$
\hat{\mathrm{P}}_{\alpha}=1 \mathrm{im}_{\lambda \rightarrow i \alpha}(\lambda-i \alpha) \hat{\mathrm{R}}(\lambda, A)
$$
in $\left[(\hat{E})\right.$ and $\operatorname{rank}\left(\mathrm{P}_{\mathrm{o}}\right)=\operatorname{rank}\left(\hat{\mathrm{P}}_{\mathrm{a}}\right)$. Because of
$$
\hat{P}_{a}(\hat{\mathrm{E}})=F \operatorname{Fix}((\lambda-\mathrm{i} \alpha) \hat{\mathrm{R}}(\lambda))
$$
one part of the corollary is proved. The other follows from Lemma 2.2.

Remarks 2.4. (a) By the results in [Lin (1974)] a semigroup of contractions on a Banach space is uniformly ergodic if and only if 0 is a pole of the generator with order $\leq 1$. The resicue of the resolvent in 0 and the associated ergodic projection are identical.
(b) Let $M$ be a $W^{*-a l g e b r a ~ w i t h ~ p r e d u a l ~} M_{*}$, $U$ a free ultrafilter on $N$ and $M$ (resp. $\left.\left(M_{*}\right)^{\wedge}\right)$ the ultrapower of $M$ (resp. $M_{*}$ ) with respect to $U$. Then it is easy to see that $c_{U}(M)$ is a two sided
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-417.jpg?height=61&width=1623&top_left_y=2168&top_left_x=208) $W^{*-a l g e b r a . ~ N o t e ~ t h a t ~ t h e ~ u n i t ~ o f ~} \hat{M}$ is the canonical image of 1 . For $\hat{x} \in \hat{M}$ and $\hat{\phi} \in\left(M_{*}\right)$ - Iet $J:\left(M_{*}\right) \cdots \rightarrow \hat{M r}$ be defined by
$$
\langle\hat{x}, y(\hat{\phi})\rangle:=\lim _{U^{\phi}}\left(x_{n}\right),\left(x_{n}\right) \in \hat{x},\left(\phi_{n}\right) \in \hat{\phi} .
$$
$J$ is well defined and is an isometric embedding. It turns out that $\left.J\left(M_{*}\right)^{n}\right)$ is a translation invariant subspace of (M')~. Hence there exists a central projection $z \in \mathcal{M}^{+\prime}$ such that $\left.J\left(M_{k}\right)^{\prime}\right)=\hat{M}^{\prime \prime} z \quad$ [Groh (1984), Proposition 2.2].

Below we identify ( $M_{*}$ ) via $J$ with this translation invariant subspace. From the construction the following is obvious: If $T$ is an identity preserving schwarz map with preadjoint $T_{*} \in L\left(M_{*}\right)$, then $T$ is an identity preserving Schwarz map on $M$ such that ( $\left.T_{*}\right)^{\wedge}=$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-418.jpg?height=55&width=253&top_left_y=492&top_left_x=222)

Theorem 2.5. Let $T$ be an identity preserving semigroup of schwarz type with generator $A$ on the predual of a $W^{*}-a l g e b r a \quad M$. If $T$ is uniformly ergodic with finite dimensional fixed space, then every $\gamma \in \sigma(A) \cap i R$ is a pole of the resolvent $R(\ldots, A)$ and dim ker $(\gamma-A) \leqq$ dim Fix( ${ }^{T}$ ).

Proof Let $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ and $R$ the $M_{*}$-valued pseudoresolvent of Schwarz type induced by $R(., A)$ on $D$. Then
$$
P=\lim _{\mu \neq 0} \mu \mathrm{R}(\mu)
$$
exists in the uniform operator topology and rank $(P)=\operatorname{dim} F i x(T)<\infty$. From this we obtain rank $(P)=\operatorname{rank}(\hat{P})<\infty$ where $\hat{P}$ is the canonical extension of $P$ onto $\left(M_{*}\right)^{n}$. Since $\hat{P}=1$ im $_{\mu+0} \mu R(\mu)^{n}$ it follows that
$$
\operatorname{dim} \operatorname{Fix}((\lambda-i a) \hat{R}(\lambda)) \leq \operatorname{rank}(\hat{P})<\infty
$$
(Proposition 2.1) for all $\alpha \in \mathbb{R}$. Therefore the assertion follows from Lemma 2.2.

The consequences of this result for the asymptotic behavior of one-parameter semigroups will be discussed in D-IV, Section 4 .

WOTES.
Section 1. The Perron-Frobenius theory for a aingle positive operator on a non-commutative operator algebra is worked out in Albeverio-H\&egh-Krohn (1978) and Groh (1981). The limitations of the theory (in the continuous as fin the discrete case)
are explained by the example following Remark 1.9 (see also Groh (1982a)). Therefore we concentrate on irreducible semigroupa. Our main result (Theorem 1.10 ) extends B-III, Thm. 3.6 to the non-commutative aetting.

Section 2. Theorem 2.5 has its roots in the Niiro-Sawashima Theorem for a single irreducible positive operator or a Banach lattice (see Schaefer (1974), V.5.4). The analogous semigroup result on Banach lattices is due to Greiner (1982). The ultrapower technique in our proof is developed in Groh (1984b).

\section*{1. STABITITY OF POSITIVE SEMIGROUPS}

As explained in $A-I I I, ~ S e c t i o n ~ l, ~ i t ~ i s ~ p o s s i b l e ~ t o ~ d e d u c e ~ u n i f o r m ~$ exponential stability of strongly continuous semigroups from the location of the spectrum of its generator if the spectral bound s(A) and the growth bound w coincide. In this section we prove $' s(A)=\omega^{\prime}$ for positive semigroups on $C^{*}$-algebras anc preduals of $W^{*}$-algebras. A more general discussion of the "s $(A)=\omega$ " problem can be found in [Greiner-Voigt-Wolff (1981)]. For the results of this section the existence of a unit is essential.

Theorem 1.1. Let $M$ be a $C^{\star}$-algebra with unit and $T=(T(t)) t \geq 0$ a positive semigroup on $M$. Then
$$
-\infty<g(A)=\omega \in O(A) \text {. }
$$

Proof. For every $t * 0$ there exists $\phi_{t}$ in the state space $S(M)$ of $M$ such that
$$
T(t){ }^{\prime} \phi_{t}=r(T(t)) \phi_{t}=\exp (\omega t) \phi_{t}
$$
(see, e.g., [Groh (I981), 2.I]). Let $n \in \mathbb{M}$ and
$$
E_{n}:=\left\{\phi \in S(M): T\left(2^{-n}\right) \cdot \phi=\exp \left(\omega 2^{-n}\right) \phi\right\}
$$

Then $\emptyset \neq E_{n+1} \subseteq E_{n} \quad(n \in \mathbb{N})$. Since $S(M)$ is o(M, $\left.M^{\prime}\right)$-compact there exists $\phi \epsilon_{n \in \mathbb{N}} E_{n}$ and $T(t)^{\prime} \phi=\exp (\omega t) \phi$ follows because the adjoint semigroup ( $\left.T(t)^{\prime}\right)$ t $\geq 0$ is a weak*-semigroup on $M$ ' Suppose $\rightarrow \infty=\omega$. Then for $t>0 \quad r(T(t))=0 \quad(A-I I I, P r o p .1 . I)$ or $T(t)^{\prime} \phi=$ 0 , in particular $\phi(T(t) 1)=0$. From this we obtain the contra-
diction $\phi(1)=0$. Hence $-\infty<\omega$ and $\exp (\omega t) \in P \sigma\left(T(t)^{\prime}\right)$ for every $\mathrm{t} \in \mathbb{R}_{+}$. Thus $\quad \omega \in(\mathrm{A})$ or $\omega=s(\mathrm{~A})$.

Remark $I+2$. (a) If we consider the nilpotent translation semigroup on the $C^{\star}$-algebra $C_{0}([0,1))$ then $\sigma(A)=\varnothing$ and $\omega=-\infty$. This shows that the existence of a unit is essential.
(b) 's(A) $=$ 'w' still holds for positive semigroups on commutative C*-algebras without unit (see B-IV, Rem.l.2.b).

Theorem 1.3. Let $M$ be a $W^{*}$-algebra with predual $M_{*}$ and let $(T(t)){ }_{t} \geq 0$ be a positive semigroup on $M_{*}$. Then $s(A)=\omega$.

Proof. For all $\lambda>s(A)$ and $\phi \mathrm{Em}_{*}$
$$
R(\lambda, A) \phi=\int_{0}^{\infty} e^{-\lambda t} T(s) \phi d s
$$
which follows as in C-III, Section 1 or [Greiner-Voigt-wolff (1981), Theorem 3]. Since $\|\phi\|=\phi(1)$ for every $\phi \in M_{*}{ }^{+}$and since the norm is additive on the positive cone of $M_{*}$ the integral
$$
\int_{0}^{\infty} e^{\lambda t}\|T(s) \phi\| d s
$$
exists for all $\phi \epsilon^{\prime} M_{*}$ and all $\lambda>s(A)$. From this the assumption follows by A-IV,Thm.l.11.

Corollary 1.4. Let $M$ be a $C^{*}$-algebra and (T(t)) $t \geqslant 0$ a positive semigroup on $M^{\prime}$. Then $s(A)=\omega$ holds.

This follows from the fact that the bidual of a $C^{*}$-algebra is a $\mathbb{N}^{*}$ algebra (see [Takesaki (1979), Theorem III. 2.4.]).

Remark 1.5. A simple modification of A-iIT, Example l.4 (take $C_{0}$ instead of $\mathbb{x}^{2}$, shows that Theorem 1.3 is no longer true for nonpositive semigroups (for details see [Groh-Neubrander (1981), Beispiel 2.53).

While the growth bound $\omega$ characterizes uniform exponential stability of the semigroup there are other (and weaker) stability concepts (cf, A-IV, Section 1).

Definition 1.6 . Let $E$ be a Banach space and ( $T(t))_{t \geqslant 0}$ a semigroup on $E$. We call the semigroup
1. uniformiy exponentially stable, if $\|T(t)\|_{i}^{l} \leq e^{-w t}$ for some $w$, $M>0$ and all $t \geqslant 0$.
2. uniformly stable, if lim $_{t \rightarrow \infty} T(t)=0$ in the strong operator topology.
3. weakly stable, if $\lim _{t \rightarrow \infty} T(t)=0$ in the weak operator topology.

Surprisingly all these properties coincice for positive semigroups on $c^{*}-a l g e b r a s$ with unit.

Theorem 1.7. Let $M$ be a $C^{*-a l g e b r a ~ w i t h ~ u n i t ~ a n d ~(T(t)) ~ t ⿺ 0 ~ a ~}$ positive semigroup on $M$. Then the following assertion are equivalent.
I. $s(A)<0$.
2. The semigroup (T(t)) $t \geqslant 0$ is uniformly exponentially stable.
3. The semigroup $(T(t))_{t \geqslant 0}$ is uniform1y stable.
4. The semigroup $(T(t))_{t \geqslant 0}$ is weakly stable.

Proof. Since ${ }^{\prime} s(A)=\omega^{\prime}$ by Theorem 1.3, it suffices to show that 4. implies 1. . For $t>0$ there exists $\phi \in S(M)$ such that
$$
T(t)^{\prime} \phi=r(T(t)) \phi
$$

Then for $x \in M$
$$
\phi\left(T(t)^{n} x\right)=(r(T(t)))^{n} \phi(x) \rightarrow 0
$$
as $n \rightarrow \infty$. Therefore $r(T(t))<1$ or $\omega<0$. Since $s(A) \leq$ ithe assertion follows.

Remark 1.8. If we consider the translation semigroup ( $T(t)$ ) $t \geqslant 0$ on $C_{0}\left(R_{+}\right)$, then $\|T(t)\|=1$, hence $s(A)=1$, but $(T(t))_{t \geq 0}$ is uniformiy stable. The same holds for the translation semigroup on $L^{1}\left(\mathbb{R}_{+}\right)$. Thus Theorem 1.7 is not true for semigroups on $c^{*}$-algebras with unit or on preduals of $W^{*}$-algebras. For the discussion of the commative situation we refer to $B-I V$, Section 1.

\section*{2. STABILITY OF IMPLEMENTED SEMIGROUPS}

Let $H$ be a Hilbert space, $U=(J(t)) t \geq 0$ a strongly continuous semigroup on $H$ with generator $B$ and $M E(H)$ be a $W^{*}$-algebra, where $B(H)$ is the $W^{*}$-algebra of all bounded linear operators on $H$. Suppose $J(t) M J(t) * \subseteq M$. Then one can define a weak*-continuous semigroup $T=(T(t)) t \geq 0$ on $M$ by $T(t) x:=U(t) x U(t) *$ ( $\left.t \in \mathbb{R}^{\prime}, x \in M\right)$. We call $T$ an implemented semigroup. Every map $T(t)$ of an implemented semigroup is weak*-continuous and n-positive for every $n \epsilon^{*}$.

Remarks 2.1. (a) Because of
$$
\|T(t)\|=\|T(t) 1\|=\|U(t) U(t) *\|=\|U(t)\|^{2}
$$
it follows that $\mathrm{m}(\mathrm{T})=2 \mathrm{w}(\mathrm{W})$.
(b) If (T(t)) $\mathrm{t}_{\mathrm{t}} \mathrm{f}$ is an implemented semigroup, then the preadjoint semigroup is strongly continuous on $M_{*}$. Therefore $s(A)=w$ for (T(t)) ${ }_{t ¥ 0}$ by Theorem 1.3.
(c) Since (u(t)) $t \geq 0$ is a (strongly continuous) semigroup the same is true for the adjoint semigroup ( $u(t)^{*}$ ) t $\geqslant 0$ and its generator is given by $\mathrm{B}^{*}$. In analogy to [Bratteli-Robinson (1979), 3.2.55] the following assertions for $x \in M$ are equivalent:
(i) $x \in D(A)$.
(ii) For $\xi \in D(B)$ it follows $x \xi \in D(B *)$ and the linear mapping
$(*) \quad\left(\xi \rightarrow \mathrm{X}(\mathrm{B} \xi)+\mathrm{B}^{*}(\mathrm{x} \xi)\right): \mathrm{D}(\mathrm{B}) \rightarrow \mathrm{H}$
has a continuous extension to $H$.

Then $A x$ is given as the continuous extension of (*) . We shortly write $A x=x B+B^{*} x$.

In the next theorem we give some equivalent conditions for the uniform exponential stability of an implemented semigroup. As we shall see, the operator equality
$$
y B+B^{*} y=-x \quad\left(x, y \in M_{+}\right)
$$
is necessary and sufficient, which is in complete analogy to the classical Liapunov stability result.

Theorem 2.2. Let $M$ be a $W^{*}$-algebra on a Hilbert space $H$ and let $T=(T(t))_{t \geqq 0}$ be a weak*-semigroup on $M$ with generator $A$ implemented by the semigroup $(U(t))_{t \geqq 0}$ on $H$ with generator $B$. Then the following assertions are equivalent.
(a) $u(T)=s(A)<0$.
(b) The semigroup ( $\mathrm{J}(\mathrm{t}))_{\mathrm{t}}^{\mathrm{t}} \mathrm{0}$ is uniformly exponentially stable.
(c) There exists $0 \leq x \in D(A)$ such that $A x=-1$.
(d) There exists $0 \leqq x \in D(A)$ such that $x(D(B)) \subseteq D\left(B^{*}\right)$ and $\mathrm{xB}+\mathrm{B}^{*} \mathrm{x}=-1$.
(e) For every $0 \leq x \in D(A)$ there exists $0 \leq y \in D(A)$ such that $A y=-x$.
(f) For every $0 \leq x \in D(A)$ there exists $0 \leq y \in D(A)$ such that $y(D(B)) \underset{C}{C}\left(B^{*}\right)$ and $Y B+B^{*} y=-x$.
(g) $\quad \int_{0}^{\infty}\|J(s) \xi\|^{2} d s$ exists for all $\xi \in H$.
(h) $\int_{o}^{\infty}((T(s) x) \xi \mid \xi) d s$ exists for all $\xi, \zeta \in H$ and all $x \in M$.

Proof. The equivalence of (a) and (b) follows from Remark 2.l.(a) whereas (c) and (d), resp., (e) and (f) are equivalent by the Remark 2.1.(c).
$(a) \rightarrow(c): \quad$ Since $s(A)<0$ the resolvent $R(0, A)$ exists and is a positive map on $M$. Therefore $R(0, A) 1 \in D(A)+$ or $A x=-I$ for some $x \in D(A)+\cdot$
$(c) \rightarrow$ (e): Let $x \in D(A)+$ such that $A x=-1$. Then
$$
T(t) x-x=\int_{0}^{t} T(s) A x d s=-f_{0}^{t} T(s) 1 d s \quad(t \geqq 0)
$$
hence
$$
0 \leqq \int_{0}^{t} T(s) I d s \leqq x \quad\left(t \in R_{+}\right)
$$

Since the family ( $\left.\int_{0}^{t} T(s) l d s\right)_{t} \geq 0$ is increasing and bounded,
$$
1 i m_{t \rightarrow \infty} \int_{o}^{t} T(s) 1 d s
$$
exists in the weak operator topology on $B(H)$. Since on bounded sets of $M$ the weak operator topology is equivalent to the $\sigma\left(M_{*} M_{*}\right)-$ topology, [Sakai (1971), 1.15.2.] , for every $\boldsymbol{q}_{\mathrm{G}}^{\mathrm{G}} \mathrm{A}_{\mathrm{*}}$ the integral $\int_{0}^{\infty} \phi(T(s) I) d s$ exists. Take $x^{\in} M_{+}$and $\phi \in \mathbb{N}_{*}^{+}$. Then $x \leqslant\|x\| I$ and therefore
$$
\phi(T(s) x) \leqq\|x\| \phi(T(s) 1) \quad\left(s \in R_{+}\right) .
$$

Hence $\int_{0}^{\infty} \phi(T(s) x) d s$ exists. Since the positive cones of $M$ and $M_{k}$ are generating, $\int_{o}^{\infty} \phi(T(s) x) d s$ exists for every $x \in M$ and $\phi \in M_{*}$. Therefore $R(0, A)$ exists and is positive which proves (e).
$(c) \rightarrow(g)$ From the last paragraph we obtain that for all $\xi \in H$
$$
\int_{0}^{\infty}\|U(s)\|^{2} d s=\int_{0}^{\infty}(T(s) I \xi \mid \xi) d s
$$
exists.
$(g) \rightarrow(h):$ It follows from the polarization identity that the integral
$$
\int_{0}^{\infty}(U(s) \xi \mid U(s) \zeta) d s
$$
exists for all $\xi, \xi \in H$. Using [Takesaki (1979), Theorem III. 4.2 and Theorem II. 2.6$]$ we conclude as in the implication from (c) to (e) that for all $\xi, \zeta \in H$ the integral
$$
\int_{0}^{\infty}(((T(s) x) \xi \mid \xi) d s \quad(x \in M)
$$
is finite.
$(g) \rightarrow(a):$ Since the vector states are dense in the predual of $M$ (iTakesaki (1979), Theorem II.2.6]) and since the preadjoint semigroup of $T$ is strongly continuous, it is easy to see that the integra1
$$
\int_{0}^{\infty} \phi(T(s) x) d s
$$
exists for all $x \in M$ and $\phi \in M_{*}$. Therefore, the resolvent $R(0, A)$ exists and is positive, hence $s(A)<0$.
3. CONVERGENCE OF POSITIVE SEMIGROUPS

In this section the asymptotic behavior of positive semigroups (T(t)) ${ }_{t \geq 0}$ will be described in more detail. Essentially we distinguish three cases:
1. The cesaro means $\frac{1}{s} \int_{0}^{s} T(t) d t$ converge strongly to a projection $P$ onto the fixed space of $(T(t))_{t} \neq 0$ (see Proposition 3.3 and 3.4)
2. The maps $T(t)$ converge strongly to $P$ (see Proposition 3.7, 3.8 and 3.9).
3. The maps $T(t)$ behave asymptotically as a periodic group (Theorem 3.11).

Much of the following is based on the theory of weakly compact operator semigroups. Therefore the following compactness criterium is quite useful.

Proposition 3.1. Let $M$ be a $W^{*}$-algebra, $T$ a bounded semigroup of positive maps on $M_{*}$ and suppose that there exists a faithful family $\Phi$ of $T$-subinvariant states in $M_{*}$. Then $T$ is relatively compact in the weak operator topology of $L\left(M_{*}\right)$. In particular, $T$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-427.jpg?height=87&width=1600&top_left_y=2332&top_left_x=222) in $M$ and yields a projection onto Fix(T) .

Proof. Since the positive cone of $M_{*}$ is generating, it is enough to show that for every $0 \leq \psi \subseteq M_{*}$ the orbit $\left\{T(t) \psi: t \in \mathbb{R}_{+}\right\}$is relatively weak compact. For this we use [Takesaki(1979), Theorem III.5.4.(iii)].

Let ( $\left.P_{n}\right)_{n \in N}$ be a decreasing sequence of projections in $M$ such that $\inf _{n} P_{n}=0$. Then $\operatorname{Iim}_{n} \phi\left(P_{n}\right)=0$ for every $\phi \in \Phi$. Since
$$
\left(T(t) P_{n}\right)^{2} \leqq T(t) P_{n}, t \in R_{+}
$$
we obtain by a classical inequality of Kadison that
$$
0 \leqq \phi\left(\left(T(t) P_{n}\right)^{2}\right) \leq \phi\left(T(t) P_{n}\right) \leq \phi\left(P_{n}\right)
$$
hence $\lim _{n} \phi\left(T(t) P_{n}\right)=0$ uniformly in $t \in \mathbb{R}_{+}$. Since the family . is faithful on $M$, it follows from [Takesaki (1979), Proposition III.5.3] that $\left(T(t) p_{n}\right)$ converges to zero in the $s\left(M, M_{*}\right)$-topology uniformly in $t \in \mathbb{R}_{+}$. Since this topology is finer than the weak*topology on $M$ we obtain the relative compactness of $T$ which implies the strong ergodicity.

Let $T$ be an identity preserving semigroup of schwarz type on the predual of a $W^{*}$-algebra $M$. We call
$$
P_{r}:=\sup \{s(|\phi|): \phi \in F i x(T)\}
$$
the recurrent projection associated with $T$. For a motivation of this definition compare, e.g., [Davies (1976), Section 6.3].

Since $T(t)|\phi|=|\phi|$ for all $\phi \in F i x(T)$ (D-III, Cor. 1.5) we obtain $T(t) ' P_{r} \geqq P_{r}$ (see $D-I, S e c .3 .(c)$ ). Let $T(r)$ be the reduced semigroup on $P_{r} M_{\star} P_{r}$ with generator $A(r)$. Then $T^{(r)}$ is identity preserving and of Schwarz type. Similarly, if $R$ is a pseudo-resolvent on $D=\{\lambda \in \mathbb{C}$ : Re( $\lambda$ ) $\quad 0\}$ with values in $M_{*}$ such that $R$ is identity preserving and of Schwarz type, then the recurrent projecton associated with $R$ is defined using $F i x(R)$.

Remark 3.2. (a) Let $\phi \in M_{*}$ and aGR such that
$$
\left(\mu-i_{\alpha}\right) R(\mu)_{\phi}=\phi \text { for some } \mu \in R_{+} \text {. }
$$

Since s(| $\left\|\|\right.$ and $s\left(\left|\phi^{*}\right|\right)$ are majorized by $P_{r}$ (D-III,Prop.1.4) it follows that $\phi$ and $\phi^{*}$ are in $P_{r} M_{*} P_{r}$.
(b) From (a) and the observation that the famsly $\{|\phi|$ : $\phi \in \operatorname{Fix}(T)\}$ is
faithful on $P_{r} P_{r}$ and consists of $T^{(r)}$-invariant elements, it follows that:
(i) $\quad \operatorname{Po}(A) \cap i R=\operatorname{Po}\left(A^{(r)}\right) \cap i \|$.
(ii) ker (ia - A) $C_{r} \mathrm{P}_{\star} \mathrm{Pr}_{r}$ for all $a \in \mathbb{R}$.
(iii) The semigroup $T^{(r)}$ is relatively compact in the weak operator topology and therefore strongly ergodic.
(c) Similarly, let $R$ be an identity preserving pseudo-resolvent with values in $M_{*}$ on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ which is of Schwarz type. It follows as in (b) that Fix( $\lambda$ - ia)R(A)) is contained in $P_{r} M_{*} P_{r}$ for all $\lambda \in D$ and $a \in \mathbb{R}$, where $P_{r}$ is the associated recurrent projection.

We now give a characterization of strong ergodicity of semigroups which are identity preserving and of schwarz type. For this we need that the Cesaro means $C(s)$, where
$$
C(s) X=\frac{1}{s} \int_{o}^{s} T(t) x d t \quad(x \in M, 0<s \in \mathbb{R})
$$
are Schwarz maps. We omit the simple calculation (compare D-I.Thm. 2.1 ).

Proposition 3.3. Let $T$ be an identity preserving semigroup of Schwarz type on the predual of a $w^{*-a l g b r a} M$. Then the following assertions are equivalent:
(a) $T$ is strongly ergodic on $M_{*}$.
(b) $\quad o\left(M, M_{*}\right)-1 i m_{s+\infty} C(s)^{\prime} P_{r}=I$.
(c) $\quad s^{*}\left(M_{*} M_{*}\right)-1 i m_{s+\infty} C(s)^{\prime} P_{r}=1$.

Proof. Suppose that (a) holds. Since Fix(T) separates Fix(T') (see [Krenge1 (1985), Chap. 2 ,Thm. 1.4]), the fixed space of T' is non trivial, hence $\mathrm{P}_{\mathrm{r}} \neq 0$. Let $0 \leqq \psi \in \mathrm{M}_{*}$, then
$$
\psi_{0}:=1 \mathrm{im}_{s \rightarrow \infty} C(s) \psi \in \operatorname{Fix}(T)
$$
and $s\left(\psi_{o}\right) s p_{r}$.

Therefore
$$
\begin{aligned}
& 1 i m_{s+\infty} \psi\left(C(s)^{1} P_{r}\right)=\operatorname{Iim}_{s \rightarrow \infty}(C(s) \psi)\left(P_{r}\right)= \\
& =\psi_{o}\left(P_{r}\right)=\psi_{o}(1)=1 i m_{s+\infty}(C(s) \psi)(I)=\psi(I)
\end{aligned}
$$
which proves (b).

Suppose that (b) is satisfied. since $C(s)^{\prime} P_{r} \leqq 1$ for all sfrt we obtain (c). (Use that for $\left(x_{\alpha}\right) \in_{+}$we have $\lim _{\alpha} x_{a}=0$ in the weak*-topology if and only if lim $_{\alpha} x_{\alpha}=0$ in the $s^{*}\left(M, M_{*}\right)$-topology.)

Suppose that (c) holds. Since each $C(s)$ ' is an identity preserving Schwarz map we obtain for all $x \in M$ :
$$
\begin{aligned}
& \left(C(s)^{\prime}\left(\left(1-P_{r}\right) x\right)\right)\left(C(s)^{\prime}\left(\left(1-P_{r}\right) x\right)^{*}\right) \leqq \\
& \underset{=}{C}(s)^{1}\left(\left(1-P_{r}\right) \times X *\left(1-p_{r}\right)\right) \leq \\
& \leftrightarrows\|x\|^{2} C(s)^{r}\left(I-P_{r}\right),
\end{aligned}
$$
hence
$$
s^{*}\left(M_{,} M_{*}\right)-1 i m_{s+\infty} C(s)^{\prime}\left(\left(I-P_{r}\right) x\right)=0
$$

In particular we obtain for all $x \in F i x\left(T^{\prime}\right)$ that
$$
x=\sigma\left(M, M_{*}\right)-1 i_{s+\infty} C(s)^{\prime} x=\sigma\left(M, M_{*}\right)-\lim _{s \rightarrow \infty} C(s)^{\prime}\left(p_{r} x\right)
$$

Especially for $0 \geq x \in F i x(T)$ we obtain $p_{r} x_{r} \neq 0$. Since the $W^{*}$-algebra $P_{r} \mathrm{MP}_{r}$ is the dual of $P_{r} M_{*} P_{r}$ and since $T(r)$ is strongly ergodic, it follows that the fixed space of $T$ separates the points of $F i x\left(T^{\prime}\right)$. Thus $T$ is strongly ergodic ([Krengel (1985), Chap. 2, Thm. 1.43).

It follows from the result above that the semigroup in [Evans (1977)] cannot be strongly ergodic on $B(H)$ * since the associated recurrent projection is zero. But for irreducible semigroups we have the following result.

Proposition 3.4. Let $T$ be an identity preserving semigroup of Schwarz type on the precual of a $W^{*}$-algebra $M$. Then the following assertions are equivalent.
(a) $T$ is irreducible and $\operatorname{Po}(A) \cap i \mathbb{R} \neq \emptyset$.
(b) $T$ is relatively compact in the weak operator topology and the fixed space of $T$ is generated by a faithful state.
(c) $T$ is strongly ergodic and the fixed space of $T$ is generated by a faithul state.
(d) The fixed space of $T$ is generated by a faithful state.

Proof. Suppose (a) is satisfied. Since Fix(T) $\neq\{0\}$ there exists a faithful normal state $\phi$ on $M$ such that $F i x(T)=\phi C \quad$ (D-III, Thm.l.lo.l. Therefore $T$ is relatively compact in the weak operator topology by proposition 3.1., whence (b) holds.

The implications from (b) to (c) and (c) to (d) are trivial.

Suppose that ( C ) holds. Let $\phi$ be a faithful normal state on $M$ such that Fix $(T)=\phi \mathbb{C}$. By Proposition 3.1 the semigroup $T$ is strongly ergodic. Therefore the fixed space of $T$ separates the points of Fix(T') . Consequently Fix(T) $=\mathbb{C l}$. Thus the ergodic projection associated with $T$ is given by $P=1 \$ \phi$, i.e. $P \psi=\psi(I) \phi$ for all $\psi \in M_{*}$. Let $F$ be a closed $T$-invariant face of $M_{*}^{+}$. If $0 \neq \psi \in \mathrm{F}$ then
$$
\operatorname{Iim}{ }_{s+\infty} C(s) \psi=\psi(1) \phi \in F .
$$

Hence $\phi \in F$ and therefore $F=M_{*}^{+}$by the faithfulness of $\phi$ which proves (a).

The next theorem is an extension of D-III,Thm.l.10 and shows the usefulness of the theory of semitopological semigroups. Assume $T \subseteq L\left(M_{*}\right)$ to be relatively compact in the weak operator topology. since $T$ is commutative its closure $S=(T)^{-} \subseteq L_{W}\left(M_{*}\right)$ contains a unique minimal ideal $K$, called the kernel of $S$, which is a compact Abelian group ([DeLeeuw-Glicksberg (I96l); wunghenn (197l); Krengel (1985), $\$ 2.4]$. The identity $Q$ of $K$ is a projection onto
the closed linear span of all eigenvalues of $A$ pertaining to the eigenvalues in $i \mathbb{R}$. Moreover, the dual group of $K$ can be identified with the subgroup of in generated by Po(A) if in . We call $Q$ the semigroup projection associated with $T$. On the other hand, $T$ is always strongly ergodic with projection $P$ onto Fix (T) . Obviously, the relation
$$
O \leqslant P \leqslant Q \leqslant I d
$$
holds, where the order relation is defined by the inclusion of the range spaces.

There are two extreme cases: First $Q=I d$ and rank $(P)=1$. This corresponds to the Halmos-von Neumann Theorem in commutative ergodic theory and is discussed, at least for irreducible semigroups, in [Olesen-Pedersen-Takesaki (1980)]. Second, Id $>Q=P$, in particular rank $(P)=I$. This latter case will be investigated in detail for $M=B(H)$, the $W^{*}$-algebra of all bounded linear operators on a Hilbert space $H$. But we first need some preparations.

Theorem 3.5. Let $T$ be an identity preserving semigroup of schwarz type on the predual of a $W^{*}$-algbra $M$ and suppose there exists a faithful family of $T$-invariant states on $M$. Let $N$ be the o( $\mathrm{M}_{\mathrm{M}} \mathrm{M}_{\mathrm{t}}$-closed linear span of all eigenvectors of $\mathrm{A}^{\prime}$ pertaining to the eigenvalues in i.R . If $Q$ is the semigroup projection associated with $T$ the following holds:
(a) The adjoint of $Q$ is a faithful normal conditional expectation from $M$ onto the $W^{*}$-subalgebra $N$.
(b) The restriction of $T$, to $N$ can be embedded into a $\sigma\left(M_{,} M_{*}\right)$ continuous, one-parameter group of *-automorphisms.
(c) If, in addition, $\quad$ is irreducible and if $q$ is the normal state generating the fixed space of $T$, then ${ }^{\$} \mid N$ is a faithful normal trace.

Proof. Consider $H:=\operatorname{Po}(A)$ it $i \mathbb{R}$ which is not empty by assumptions. From Proposition 3.1 it follows that $T$ is relatively compact in the weak operator topology, Let $K$ be the semigroup kernel of $T^{-}$ㄷ $L_{W}\left(M_{*}\right)$ and $Q$ the unit of $K$. Recall that $Q \psi_{T}=\psi_{\eta}$ for all $\psi_{\eta_{1}} \in M_{*}$ such that $A \psi_{\Pi}=\eta_{\eta} \quad(\eta \in H)$. Let $U$ be the family of all
eigenvectors of $A^{\prime}$ pertaining to the eigenvalues in $H$. Then $J$ is closed with respect to the multiplication in $M$ and the formation of adjoints. Thus $N$ is a $W^{*}$-subalgebra of $M$ [sakai (1971), Corollary 1.7 .9.$]$ and $T_{o}(t)^{\prime}:=T(t)^{\prime} \mid N$ is multiplicative (for this see D-III, Lenma 1.1).
since $Q \in T^{-} \underset{\sim}{L} L\left(_{W}\left(M_{*}\right)\right.$ there exists an ultrafilter $U$ on $\mathbb{R}_{+}$such
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-433.jpg?height=52&width=1597&top_left_y=679&top_left_x=224) $\psi_{\Gamma_{1}} \epsilon_{M_{*}}$ such that $A \psi_{\eta_{0}}=\eta \psi_{\eta_{\eta}}$, then for all $x \epsilon_{M}$ :
$$
\left\langle\psi_{\eta} x\right\rangle=:\left\langle Q_{\eta} \psi_{\eta} x\right\rangle=\lim \left\langle\left\langle T(t) \psi_{\eta}, x\right\rangle=\left(\operatorname{Iim}{ }_{U} e^{n t}\right)\left\langle\psi_{\eta}, x\right\rangle\right.
$$
hence lim $_{u} e^{\eta t}=1$. From this it follows that for all $\psi \mathrm{M}_{*}$ we have
$$
\begin{aligned}
& \left\langle\psi, Q^{\prime}\left(u_{\eta}\right)\right\rangle=1 i m m_{U}\left\langle\psi, T(t)^{\prime} u_{\eta}\right\rangle= \\
& =\left(1 i m_{U} e^{\pi t}\right)\left\langle\psi, u_{n}\right\rangle=\left\langle\psi_{r} u_{n}\right\rangle
\end{aligned}
$$

Hence $N \in Q^{\prime}(M)$.

For $y$ in the dual group of $K$ and $x \in M$ we define $x_{\gamma}$ by
$$
\psi\left(x_{Y}\right):=\int_{K}<S \psi_{r} x><\beta, \gamma>* d m(\beta) \quad\left(\psi \in M_{*}^{+}\right)
$$

Then $x_{\gamma} \in M$ and $T(t)^{\prime} x_{Y}=\left\langle Q T(t), Y>X_{\gamma}\right.$. Therefore $x_{Y} \in N$. Thus the inclusion $Q^{\prime} M$ ㄴ $N$ is proved if we can show that Q'M belongs to $^{\prime}$ the $o\left(M_{A} M_{*}\right)$-closed linear span of $\left\{x_{\gamma}: \gamma \in K, x \in M\right\}$. For this it is enough to show that every linear form $\psi \in M_{*}$ such that $\psi\left(x_{\gamma}\right)=0$ for all $\quad \gamma \in K$ satisfies $\psi(Q x)=0$ for all $x \in M$. But if $\psi\left(X_{\gamma}\right)=0$ then
$$
\int_{K}<S \psi, x><S, \gamma>* \operatorname{dm}(S)=0, Y \in K .
$$

Since the map $(S \rightarrow \psi(S x))$ is continuous on $K$ and since the elements of $K$ form a complete orthonormal basis in $L^{2}\left(K, d_{m}\right)$, we obtain $\psi(S X)=0$ for all $S \in K$, in particular $\psi(Q X)=0$ as desired.

Since the range of $Q^{*}$ is a $W^{*}$-subalgebra of $M$ it follows from [Takesaki (1979), Theorem III.3.4] that $Q$ ' is a completely positive, normal conditional expectation. $Q^{\prime}$ is faithful, i.e. ker ( $Q^{\prime}$ ) $\cap M_{+}=\{0\}$ since $Q \phi=: \phi$ for the faithful linear form $\phi$.

Let $\phi$ be the faithful normal state generating fix(T) and let U be a family of unitary eigenvectors of $A$ pertaining to the eigenvalues in $H$ (see D-III, Remark I.II). If $u_{1}, u_{2} \in \mathbb{J}$ then
$$
\phi\left(u_{1} u_{2}^{*}\right)=\phi\left(T_{0}(t)^{\prime}\left(u_{1} u_{2}^{*}\right)\right)=e^{\left(\eta_{1}-\eta_{2}\right) t} \phi\left(u_{1} u_{2}^{*}\right)
$$

\section*{Therefore}
$$
\phi\left(u_{1} u_{2}^{*}\right)=\left\{\begin{array}{l}
0 \\
\text { if } \eta_{1} \neq \eta_{2} \\
1
\end{array} \quad \text { if } \eta_{I}=\pi_{2},\right.
$$

Hence $\phi\left(\mathrm{u}_{1} \mathrm{u}_{2}{ }^{*}\right)=\phi\left(\mathrm{u}_{2}{ }^{*} \mathrm{u}_{\mathrm{I}}\right)$ from which it follows that $\tau:=\phi \mid N$ is a faithful normal trace.

Remarks 3.6. (a) Since $\mathrm{QM}_{*}=\mathrm{N}_{*}$ and $Q^{\prime} \mathrm{M}=\mathrm{N}$, where $\mathrm{N}_{*}$ is as in D-III, Proposition 1.12 , it follows from general duality theory that $\left(N_{*}\right)^{\prime}=\mathrm{N}$.
(b) If $\psi \mathbb{N}_{*}$ then $|\psi| \epsilon \mathbb{N}_{*}$. To see this note that $Q \psi=\psi$ and $Q$ is an identity preserving schwarz map. Then the assertion follows from D-III, Proposition 1.4 .
(c) If $\psi \in N_{*}$, then $\left|T_{o}(t) \psi\right|=T_{o}(t)|\psi|$ for all $t \in \|_{i}$. This follows immediately from the fact that $T_{o}(t)^{\prime}$ is a *-automorphismus on $N$.
(d) Let us add a few words concerning the structure of $N: I f \quad T$ is irreducible and $K$ is the semigroup kernel of $T^{-} \underline{L_{w}}\left(M_{k}\right)$, then
$$
\left(S \rightarrow S^{1}\right): K \rightarrow I\left(\left(N, O\left(N, N_{*}\right)\right)\right.
$$
is a representation of the compact, Abelian group $K$ as group of *-automorphism such that the fixed space is one dimensional. Therefore we are able to apply the results of Colesen-Pedersen-Takesaki (1980) 7. There are three possibilities for $N$ :
(i) $N \cong L^{\infty}(\mathbb{K}, \mathrm{dm})$ and $\mathrm{T}_{\mid \mathrm{N}}$ is the translation group on N .
(i.i) $N \equiv R$ where $R$ is the (unique) hyperfinite factor of typ $I_{1}$. In that case (the image of) $K$ is approximately inner on $R$ [l.c., Theorem 5.83.
(iii) There exists a closed subgroup $G$ of $K$ such that
$$
\mathrm{N}=\mathrm{L}^{\infty}\left(K_{\mathrm{G}^{\prime}}, \operatorname{dm} /\right) \Leftrightarrow \mathrm{R}
$$
where $R$ is as in (ii) and dm, the normalized Haar measure on ${ }^{K} / \mathrm{G}$ [I.c.. Theorem 5.15].

So far we have studied weak*-semigroups on general w*algebras. We now want to apply the results of this section to weak*-semigroup on B(H). This is of interest in view of the results in [Davies (1976)]. To do this we call a triple ( $M, \Phi, T$ ) a $W^{*}$-dynamical system if $M$ is
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-435.jpg?height=47&width=1591&top_left_y=910&top_left_x=227) on $M$ and $\Phi$ a faithful family of T-invariant normal states. We call ( $M, \Phi, T$ ) irreducible, if the preadjoint semigroup is irreducible (alternatively, if the fixed space of $t$ is one dimensional).

Proposition 3.7. Let ( $B(H), \Phi, T)$ be a $W^{*}$-dynamical system on the $W^{*}$-algebra $B(H)$ of all bounded linear operators on a Hilbert space $H$. Then the following assertions are equivalent:
(a) $\operatorname{Po}(A)$ 白 $\mathrm{i} R=\{0\}$.
(b) $\lim { }_{s+\infty} T(s)_{*}=P_{*}$ in the strong operator topology on $L\left(B(H)_{*}\right)$.

Proof. Obviously (b) implies (a). Suppose that (a) is fulfilled. Then the ergodic projection $P_{*}$ of the preadjoint semigroup is equal to the associated semigroup projection. Consequently there exists an ultrafilter $W$ on $\mathbb{R}_{+}$such that $\lim _{U} T(t)=P$ in the weak operator topology. We claim that the convergence holds even in the strong operator topology. Taking this for granted it follows, since for every $t \xi_{+}{ }_{+} T(t)$ is a contraction, that
$$
\lim _{t \rightarrow \infty}\left\|T(t)_{\star} \phi\right\|=0
$$
for all $\phi \in \operatorname{ker}\left(P_{*}\right)$. Since $T(t)_{*} \psi=\psi$ for every $\psi \in i m\left(P_{*}\right)$ and because
$$
\mathrm{B}(\mathrm{H})_{*}=\operatorname{im}\left(\mathrm{P}_{*}\right) \oplus \operatorname{ker}\left(\mathrm{P}_{*}\right)
$$
the assertion is proved.

It remains to show that lim $U^{T(t)}{ }_{*}=P_{*}$ in the strong operator topology. Choose $0 \leq \phi \in B(H)_{*},\|\phi\| \leq I$, let $\phi_{t}:=T(t) \neq \phi(t>0)$,
$\phi_{o}:=P_{*} \phi$ and let $\left\{P_{i}: i \in A\right\}$ be an increasing net of projections of finite rank in $B(H)$ with strong limit 1 . Since the set $K:=\left\{\phi_{t}\right.$ : $t \geq 0$ ) is relatively compact in the $0\left(B(H){ }_{*}, B(H)\right.$-topology, there exists for every $\delta>0$ an index $i_{0} \in \Delta$ such that
$$
\left\|\left(1-p_{i}\right) \psi\left(1-p_{i}\right)\right\| \leqslant \delta
$$
for every $\psi \in K$ and $i \geq i$ [Takesaki (1979), Theorem III.5.4.(vi)]. In particular
$$
\left|\psi\left(1-P_{i}\right)\right| \leqslant \delta \quad, \psi \in K, \quad i(0) \leqslant i
$$

Let $p:=p(i(o))$. Then for all $x$ in the unit ball of $M$ it follows that
$$
\begin{aligned}
& \left|\left(\phi_{t}-\phi_{o}\right)(x)\right| \leqq \\
& \leqq\left|\left(\phi_{t}-\phi_{o}\right)(p \times p)\right|+\left|\left(\phi_{t}-\phi_{o}\right)((1-p) x p)\right|+ \\
& +\left|\left(\phi_{t}-\phi_{o}\right)(x(1-p))\right| \leqq \\
& \leqq\left|\left(\phi_{t}-\phi_{o}\right)(p x p)\right|+4 \sqrt{\delta} .
\end{aligned}
$$

Since the $W^{*}-a l g e b r a \quad p(H) p$ is finite dimensional, there exists $U \in U$ such that
$$
\left|\left(\phi_{t}-\phi_{0}\right)\right| \mathrm{pB}(H) p \mid \leqslant \delta
$$
for all $t \in U$. Consequently
$$
\left\|\left(\phi_{t}-\phi_{o}\right)\right\| \leq(\delta+4 / \bar{\delta})
$$
for all $t \in U$. Therefore $\operatorname{Iim}_{U} T(t)_{*} \phi=P_{*} \phi$ in the strong operator topology. since the positive cone of $B(H) *$ is generating, the as* sertion is proved.

For irreducible $W^{*}$-dynamical systems on $B(H)$ the above properties always hold.

Theorem 3.B. Let ( $B(H), \Phi, T)$ be an irreducible $W^{*}$-dynamical system. Then
$$
\operatorname{Po}(A) \cap i \mathbb{R}=\{0\}
$$

Proof. Let $N$ be the $W^{*}$-subalgebra of $M=B(H)$ generated by the eigenvectors of $A$ pertaining to the eigenvalues on if and let $Q$ be the faithful normal conditional expectation from $M$ onto $N$ (Theorem 3.7.). Since $M$ is atomic, $N$ is atomic [stormer (1972)]. $N$ is finite since there exists a finite, faithful normal trace on $\mathbb{N}$. In particular the center of $\mathbb{N}$ is isomorphic to $\&^{\infty}$. Let $S$ be the restriction of $T$ to the center. Then $S$ is a weak*-semigroup such that every $s(t) \in S$ is $\sigma\left(\varepsilon^{\infty}, l^{l}\right)$-continuous and a *-automorphism. From this it follows that $S(t)$ is induced by some continuous flow $\kappa_{t}: \mathbb{N} \rightarrow \mathbb{N}$. Indeed, if $\delta_{n}\left(\left(\xi_{m}\right)\right)=\xi_{n} \quad\left(n \in \mathbb{N},\left(\xi_{m}\right) \in i^{\infty}\right)$, then $\delta_{n}$ os $(t)$ is a normal scalar valued * whomomorphism hence of the form $\delta_{m}$ for some m $m k_{t}(n)$. But the function ( $t \rightarrow k_{t}$ ) is continuous from ir into $N$, whence constant. Hence $S(t)=I d$. But the semigroup $S$ is weak*-irreducible on the center. Consequently the center is one dimensional. Using [Takesaki, Theorem V.l.27] we obtain $N=B\left(H_{n}\right)$ where $H_{n}$ is a finite dimensional Hilbert space. But if 0 if
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-437.jpg?height=53&width=1594&top_left_y=1204&top_left_x=228) infinite dimensional. Therefore $P o(A) \cap$ in $:\{0\}$ as desired.

An immediate and interesting consequence of Theorem 3.8 and Proposition 3.7 is the following.

Corollary 3.9. If ( $B(H), \phi, T)$ is an irreducible $W^{*}$-dynamical system, then
$$
\lim _{s \rightarrow \infty} T(s)=I \phi
$$
in the strong operator topology on $L\left(B(H)_{\star}\right)$, where $\phi$ is the unique normal state generating the fixed space of $T_{*}$.

We are now going to discuss the asymptotic behavior of positive semigroups whose generator has boundary point spectrum different from 0 . The standard example is the following:

If $\Gamma$ is the unit circle, m the normalized Haar measure on $\Gamma$ and $0<\tau \in R$, then we define the maps $R_{\tau}(t), t \in \mathbb{R}+$, on $L^{1}(T, m)$ by
$$
\left(R_{\tau}(t) f\right)(\xi)=f\left(\xi \exp \left(\frac{2 \pi i}{\tau} t\right)\right) \quad\left(f \in L^{I}(\Gamma, m), \xi \in \Gamma\right)
$$

Then $R=\left(R_{T}(t)\right) t z 0$ forms a strongly continuous one parameter semigroup which is identity preserving and of Schwarz type. since $R$
is periodic of period $\tau$ it follows that 0 is a pole of the resolvent of its generator $B$ with residum $\quad P=181$ and $\left\{\frac{2 \pi i}{\tau} k: k \in \mathbb{Z}\right\}$ $=$ (B) Thus $R$ is irreducible and uniformiy ergodic on $L^{l}(\Gamma, m)$ (see A-II, Section 5).

Now let $T$ be a semigroup on $M_{*}$. It is called partially periodic, if there exists a projection $Q \in L\left(M_{*}\right)$ reducing $T$ such that $Q\left(M_{*}\right)$ $\cong L^{1}(T, m)$ and $T / i m(Q)$ is conjugate to a periodic semigroup on $L^{I}(\Gamma, m)$. In the main result we present a non commutative version of [Nagel (1984)] showing that certain dynamical systems converge to partially periodic semigroups.

Proposition 3.10. Let $T$ be an irreducible, identity preserving semigroup of schwarz type with generator $A$ on the predual of a w*algebra $M$. If $T$ is uniformly ergodic, then $\sigma(A) \quad \cap \quad i \mathbb{R}=$ $P \sigma(A) \cap i \mathbb{R}=i \alpha \mathbb{Z}$ for some $a \in \mathbb{R}$. If additionally o(A) $\cap i \mathbb{R} \neq\{0\}$, there exists a strictly positive projection $Q$ on $M_{*}$ which is identity preserving and completely positive such that:
(a) $Q$ reduces $T$ and $Q\left(M_{*}\right) \cong L^{1}(\Gamma)$, $\Gamma$ being the one dimensional torus.
(b) The restriction $T_{0}$ of $T$ to im(Q) is irreducible and conjugate to a rotation semigroup of period $T=\frac{2 \pi}{a}$ on $T$.
(c) The spectral bound $s\left(\left.A\right|_{k e r(Q)}\right)$ is strictly smaller than 0 .

Proof. By D-III,Thm.1.Il and D-III,Thm. 2.5 it follows that
$$
\sigma(A) \cap i \mathbb{R}=\operatorname{Po}(A) \quad \cap i R=i a \mathbb{Z}
$$
for some $\alpha \in \mathbb{R}$. Suppose $a \neq 0$. Since $\sigma(A)+i \alpha \mathbb{Z}=\sigma(A)$ and since every $n \in i a \mathbb{Z}$ is isolated, it follows that there exists $\delta>0$ such that
$$
o(A) \text { i } \dot{\operatorname{cog}} \underline{G}\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda) \leqq \delta\} .
$$

Let $\left\{u_{\alpha}^{k}\right.$ : $\left.k \in \mathbb{Z}\right\}$ be a family of unitary eigenvectors of $A^{\prime}$ pertaining to the eigenvalues in $i \mathbb{R}$. Then $Q^{\prime}(M)$ is a commutative $\mathbb{N}^{*}-a l-$ gebra. Let $T:=\frac{2 \pi}{\alpha}$. Then $T(\tau)^{\prime} u_{\alpha}^{k}=u_{\alpha}^{k}$, hence $T \mid \operatorname{im}(Q)$ is periodic. From the Halmos-von Neumann theorem (see [Schaefer (1974),

Thm. III. 7.11 J$)$ it follows that $\quad{ }^{T}(\mathrm{im}(\mathrm{Q})$ is conjugate to the
rotation semigroup of period $T$ on $L^{I}(\Gamma, m)$.

Using this proposition we obtain

Theorem 3.11. Let $T=(T(t))_{t \geqslant 0}$ be a uniformly ergodic, identity preserving semigroup of Schwarz type on the predual of a w*algebra $M$ and suppose o (A) $\cap \mathrm{i} \mathbb{A} \neq\{0\}$. Then there exists a partially periodic, identity preserving semigroup $S=(S(t))_{t \geq 0}$ of Schwarz type on $M_{*}$ such that
$$
\lim _{t \rightarrow \infty}(T(t)-s(t))=0
$$
in the strong operator topology.

Proof. Let $\phi$ be the normal state on $M$ generating the fixed space of $T$. Let $S=(S(t)) t \geqslant 0$ where $S(t):=T(t) \circ Q$ and $Q$ is as in 2.6. Obviously, $S$ is partially periodic and $\phi \in F i x(S)$. Let $H_{\phi}$ be the GNS-Hilbert space pertaining to $\phi$. Since $\phi$ is fixed under $T$, $S$ and $Q$ these objects have a canonical extension to $H_{q}$ (in the following denoted by the same symbols). If $H_{o}:=k e r(Q)=H_{\phi}$ then it is easy to see that $H_{o}$ is invariant under the extension to $H_{\phi}$ of the multiplication maps we defined in D-III, Remark l.3. Consequently, using the results in Groh-Kümmerer (1982) it follows that there exists $c \in \mathbb{R}$ such that for all y near 0 and all $\beta \in \mathbb{R}$ :
$$
\begin{equation*}
\left\|R\left(Y+i B, A_{o}\right)\right\| \leqslant c \tag{*}
\end{equation*}
$$
where $A_{o}:=A \mid k e r(Q) \quad$ (the norm taken in $L\left(H_{\phi}\right)$ ). Using the result in A-III, Cor.7.11 it follows that
$$
\lim _{t \rightarrow \infty}\left\|T(t) \mid H_{o}\right\|=0
$$

Since the $s\left(M_{*} M_{*}\right)$-topology on the unit ball of $M$ is nothing else than the restriction of the norm topology on $H_{\phi}$, we obtain
$$
s\left(M, M_{*}\right)-\lim _{t \rightarrow \infty}\left(T(t)^{\prime}-s(t)^{\prime}\right)(x)=0
$$
uniformiy on $M_{1}$. From this the assertion follows.

As we have seen, uniformly ergodic semigroups have nice spectral properties. In this section we study sufficient conditions which imply uniform ergodicity thereby generalizing results the results of Groh (1984b). We first need some preparations.

Lemma 4.1 . Let $R$ be an identity preserving pseudo-resolvent of Schwarz type on $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ with values in the predual of a W*-algebra $M$. If the fixed space of $R$ is infinite dimensional, then there exists a sequence of states in Fix(R) such that the corresponding support projections are mutually orthogonal in M.

Proof. Let $\Phi=\{\phi \in F i x(R): \phi$ state on $M\}$ and let $P=\sup \{s(\phi)$ $: \phi \in \Phi\}$. Since $\lambda R(\lambda) \phi=\phi$ for $a l l$ and $\lambda \in D$ it follows $\mu R(\mu)(1-s(\phi)) \leq(1-s(\phi))$. Hence $\mu R(\mu)(1-p) \leqslant(1-p)$ for all $\mu \in \mathbb{R}_{+}$* Let $R_{\|}$be the induced pseudo-resolvent on $\mathrm{PM}_{*} \mathrm{P}$ ( $\mathrm{D}-\mathrm{I}$, section 3. (c)). Then the family $\Phi$ is faithful on $M_{p}$ and contained in the fixed space of $R_{\mid}$. The adjoint $\mu R_{\mid}(\mu)$ ' is an identity preserving Schwarz map. Consequently it follows from D-III, Lemma 1.1. (b) and the $\quad\left(M_{P},\left(M_{p}\right){ }^{\prime}\right)$-continuity of $H R_{\mid}(\mu)^{\prime}$, that $F i x\left(R^{\prime}\right)^{\prime}$ is a W*-subalgebra of $M_{p}$ and by D-III, Lemma 1.5 it follows that dim $F i x(R) \leq \operatorname{dim} F i x(R \mid '$. If $F i x(R)$ is infinite dimensional, let $\left(P_{n}\right)$ be a sequence of mutually orthogonal projections in Fix(R|') $M_{p}$ and choose a sequence $\left(\phi_{n}\right)$ in $\Phi$ such that $\phi_{n}\left(P_{n}\right) \neq 0$. For $n \in \mathbb{N}$ let $\psi_{n}$ be the normal state
$$
\psi_{n}(x)=\phi_{n}\left(P_{n}\right)^{-1} \phi_{n}\left(P_{n} x P_{n}\right)
$$
on $M$. Because of $s\left(\psi_{n}\right) \leqq p_{n} \leqq P$, the support projections of the $\psi_{n}$ 's are mutually orthogonal in $M$. For $\mu \in f+$ and $x \in M$ we obtain:
$$
\begin{aligned}
& \left\langle x, \mu R(\mu) \psi_{n}\right\rangle=\phi_{n}\left(P_{n}\right)^{-1}\left\langle\mu P_{n}\left(R(\mu)^{\prime} x\right) P_{n} \cdot \phi_{n}\right\rangle= \\
& =\phi_{n}\left(p_{n}\right)^{-1}<\mu p_{n} p\left(R(\mu) P^{\prime} x\right) P_{n} r \phi_{n}>= \\
& =\phi_{n}\left(p_{n}\right)^{-1}<\mu \rho_{n}\left(p R \mid(\mu)^{\prime} x p\right) p_{n}, \phi_{n}>= \\
& =\phi_{n}\left(p_{n}\right)^{-1}<\mu\left(p_{n}^{R} \mid(\mu){ }^{\prime} x p_{n}\right), \phi_{n}>= \\
& =\phi_{n}\left(p_{n}\right)^{-1} \phi_{n}(x)=\psi_{n}(x) \text {. }
\end{aligned}
$$

Therefore $\psi_{n} \in F i x(R)$ for all $n \in N$.

Remark 4.2. (a) If dim Fix(R) $\geqq 2$ then it follows from the Jordan decomposition of self adjoint linear functionals, that there are at least two states in $F i x(R)$ which have orthogonal support (compare the proof of D-III, Theorem 1.10 . (a)).
(b) If $R$ is a pseudo-resolvent with values in a w*algebra such that $F i x\left(R^{\prime}\right)$ is contained in $M_{*}$, then it follows from the proof of D-III, Lemma l. 2 that there exists a sequence of normal states in Fix(R') whith orthogonal supports in $M$.

Lemma 4.3. Let $R$ be an identity preserving pseudo-resolvent of Schwarz type on $D:\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)$ o 0 with values in the predual of a $W^{*}$-algebra $M$. If the fixed space of the canonical extension $\hat{R}$ of $R$ to some ultrapower of $M_{*}$ is infinite dimensional, then there exists a sequence $\left(z_{n}\right)$ in $M_{I}{ }^{+}$and a sequence of states $\left(\phi_{n}\right)$ in $M_{*}$ such that:
(a) $\lim _{n} \mathrm{z}_{\mathrm{n}}=0$ in the $\mathrm{s}^{*}\left(\mathrm{M}, \mathrm{M}_{*}\right)$-topology.
(b) $\quad \lim _{n}\left\|(I d-\lambda R(\lambda))_{\phi_{n}}\right\|=0$ for all $\lambda \in D$.
(c) $\phi_{n}\left(z_{n}\right) \geqq \frac{1}{2}$ for all $n \in \mathbb{N}$.

Proof. Let $\left(M_{*}\right)$, be the ultrapower of $M_{*}$ with respect to some free ultrafilter $U$ on $\mathbb{N}$. Since ( $M_{*}$ ) is the predual of a W*-subalgebra of $\hat{M}^{\prime \prime}$ (see D-III, Remark 2.4.(b)), there exists a sequence of states $\left(\hat{\psi}_{n}\right)$ in $F i x(\hat{R})$ such that the corresponding support projections are mutually orthogonal in $\hat{M}^{\prime \prime}$ (Lemma 4.1). For every $n \in \mathbb{N}$ let $\left(\psi_{n, k}\right) \hat{\epsilon} \hat{\psi}_{n}$ be a representing sequence of states, let
$$
\phi:=\sum_{n, k} 2^{-(n+k+I)} \psi_{n, k}
$$
and let
$$
P:-\sup \left(s\left(\psi_{n, k}\right): n, k=1, \ldots\right\}
$$
in $M$. Then $\phi$ is a normal state on $M$ which is faithful on the W*-algebra $\mathrm{M}_{\mathrm{P}}$. Since
$$
I=\left\langle\psi_{n, k} s\left(\psi_{n, k}\right)\right\rangle=\psi_{n, k}(p) \quad(n, k \in N)
$$
it follows $\hat{\psi}_{n}(\hat{p})=1$ where $\hat{p}$ is the canonical image of $p$ in $\hat{M}$.

But this implies $s\left(\hat{\psi}_{n}\right) \leqq \hat{p}$ in $\hat{M}^{\prime \prime}$. Since $\hat{M}_{1}^{+}$is o( $\left.\hat{M}^{\prime \prime}, \hat{M}^{\prime}\right)-$ dense in $\left(\hat{M}{ }^{\prime \prime}\right)_{1}{ }^{+}$(Kaplanskys density theorem [Sakai (1971), 1.9.I] in combination with [Sakai (1971), 1.8.9 and 1.8.12]), there exists for all $n \in \mathbb{N}$ a net $\left(\hat{z}_{n, \gamma}\right)$ in $\hat{M}_{1}+$ such that
$$
\sigma\left(\hat{M}^{\prime}, \hat{\mathrm{M}}^{\prime}\right)-\operatorname{Iim}_{\gamma} \hat{z}_{n, \gamma}=s\left(\hat{\psi}_{n}\right)
$$

From [sakai (1971), 1.7.8] and the considerations above we obtain that the net $\left(\hat{p} \hat{z}_{n, \gamma} \hat{p}\right)$ converges to $s\left(\hat{\psi}_{n}\right)$ in the $\sigma\left(\hat{M}^{\prime} '^{\prime}, \hat{M}^{\prime}\right)$-toplogy. Therefore we may assume $z_{n, Y} \in\left(M_{p}^{\sim}\right)^{+}$. In the following we denote by $\hat{\phi}$ the canonical image of ${ }_{\phi}{ }_{\phi}$ in $\left(M_{\star}\right)$. .

Since the projections $s\left(\hat{\psi}_{n}\right)$ are mutually orthogonal, there exists a real sequence $\left(r_{n}\right), 0 < r _{n}<1,1 i m_{n} r_{n}=0$ and $\hat{\phi}\left(s\left(\psi_{n}\right)\right) \leq \frac{1}{2} r_{n}$. For all $n \in \mathbb{N}$ choose $z_{n} \in\left(\hat{M}_{\hat{p}}^{\hat{\prime}}{ }_{1}{ }^{+}\right.$such that
$$
\begin{aligned}
& \left\lvert\,\left\langle\hat{\phi}, s\left(\hat{\psi}_{n}\right)-\hat{z}_{n}>\dot{j} \leqq \frac{1}{2} r_{n},\right.\right. \\
& \left|<\hat{\psi}_{n} s\left(\hat{\psi}_{n}\right)-\hat{z}_{n}>\right| \leqq \frac{1}{2} r_{n} .
\end{aligned}
$$

Hence $\hat{\phi}\left(\hat{z}_{n}\right) \leqq r_{n}$ and $\hat{\psi}_{n}\left(\hat{z}_{n}\right) \geqq \frac{1}{2}$ for all $n \in \mathbb{N}$. For every $n \in \mathbb{N}$ let $\left(z_{n, k}\right) \epsilon_{\mathrm{z}}$ be a representing sequence in $\left(M_{p}\right)_{1}{ }^{+}=p\left(M_{1}{ }^{+}\right)_{p}$ (note that $\left.M_{p}^{\wedge}=\left(M_{p}\right)^{\wedge}\right)$ and fix $\mu \in R_{+}$. Since $\mu R(\mu)^{\wedge} \hat{\psi}_{n}=\psi_{n}$, $\hat{\phi}\left(\hat{z}_{n}\right) \leqq r_{n}$ and $^{P} \hat{\psi}_{n}\left(\hat{z}_{n}\right) \geqq \frac{1}{2}$ there exists for all $n \in \mathbb{N}$ an element $U_{n} \in U$ such that for all $k \in J_{n}$ :
$$
\begin{aligned}
& \text { (i) } \quad \phi\left(z_{n, k}\right) \leq r_{n}, \\
& \text { (ii) }\left\|(I d-\mu R(\mu)) \psi_{n, k}\right\| \leqq r_{n}, \\
& \text { (iii)' } \psi_{n, k}\left(z_{n, k}\right) \geqq \frac{l}{2} .
\end{aligned}
$$

Inductively we find a sequence $\left(\mathrm{z}_{\mathrm{n}}\right)$ in $\left(\mathrm{M}_{\mathrm{p}}\right)_{1}{ }^{+}$and a sequence of states $\left(\phi_{n}\right)$ in $M_{*}$ such that for all $n \in \mathbb{N}$ :
$$
\begin{aligned}
& \text { (i) ' } \quad \operatorname{Iim}_{n} \phi_{n}\left(z_{n}\right)=0, \\
& \text { (ii) '" } \lim _{n}\left\|(I d-\mu R(\mu)) \phi_{n}\right\|=0, \\
& \text { (iii) ' ' } \phi_{n}\left(z_{n}\right) \geqq \frac{1}{2} .
\end{aligned}
$$

Since $\phi$ is faithful on $M_{p}$, condition (i)" implies that $1 . m_{n} z_{n}=$ 0 in the $s^{*}\left(\mathrm{M}_{\mathrm{p}},\left(\mathrm{M}_{\mathrm{p}}\right)_{*}\right)$-topology [Takesaki (1979), Proposition III.5.4].

Since $s^{*}\left(M_{p},\left(M_{p}\right)^{*}\right)=\left.s^{*}\left(M_{k} M_{*}\right)\right|_{p}$ (a) follows immediately from (i)' '. Using the resolvent equation for $R$ it is easy to see that (ii)" implies
$$
\lim _{n}\left\|(\operatorname{Id}-\lambda R(\lambda)) \phi_{n}\right\|=0
$$
for all $\lambda \in D$ and the proof is complete.

Without further comments we will make use of the following facts in the rest of this section :
(1) A sequence $\left(\phi_{n}\right)$ in $M^{\prime}+$ converges in the $\sigma\left(M^{\prime}, M\right)$-topology if and only if it converges in $\sigma\left(M^{\prime \prime}, M^{\prime \prime}\right)-t o p o l o g y ~[A k e m a n-D o d d s-G a m i e n$ (1972) 3.
(2) We can decompose $\phi \in M_{+}$into its normal and singular part $\phi=$ $\phi^{(n)}+\phi^{(s)}, 0 \leqq \phi^{(n)} \in M_{*}, 0 \leqq \phi^{(s)} \in M_{*}^{\perp}$ and $\left\|_{i}\right\|=\|\phi(n)\|\left\|_{i}^{(s)}\right\|$ [Takesaki (1979), Theorem III.2.14].
(3) If ( $\phi_{n}$ ) is a sequence in $M_{*}$ which converges to zero in the $\sigma\left(M_{*} M\right)-t o p o l o g y ~ a n d ~ i f ~\left(X_{n}\right)$ is a sequence in $M$ which converges to zero in the $s^{*}\left(M_{,} M_{*}\right)$-topology, then $\lim _{n} \phi_{k}\left(x_{n}\right)=0$ uniformly in $\mathrm{k} \in \mathbb{N}$ [Takesaki (1979), Lemma III.5.5].

Theorem 4.4. Let $R$ be an identity preserving pseudo-resolvent on $\mathrm{D}=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ with values in a watalgebra $M$ which is of Schwarz type and let $R^{\prime}$ its adjoint pseudo-resolvent. Any one of the following conditions implies dim $\operatorname{Fix}(\hat{R})<\infty$ in some ultrapower of $M$.
(a) The fixed space of $R^{\prime}$ is finite dimensional.
(b) inm $_{\mu+0} \mu \mathrm{R}(\mu)=\mathrm{P}$ exists in the strong operator topology and $\operatorname{rank}(P)<\infty \quad$.
(c) The fixed space of $R^{\prime}$ is contained in $M_{*}$.
(d) Every map $\mu \mathrm{R}(\mu), \mu \in \mathcal{F}_{+}$, is irreducible on $M$.

Proof. Suppose that the dimension of the fixed space of ( $\left.\boldsymbol{R}^{\boldsymbol{r}}\right)^{n}$ in some ultrapower ( $M^{\prime}$ ) ^ of $M^{\prime \prime}$ is infinite dimensional. Since (M')
is the predual of the $W^{*}-a l g e b r a \hat{M}^{\prime \prime}$ and $R^{\prime}$ is identity preserving (since $R^{\prime \prime}=R 1=1$ ) and of Schwarz type (because $\mu \mathrm{R}^{\prime \prime}(\mu)=$ $(\mu R(\mu))^{\prime \prime}$ is a Schwarz map for all $\mu \mathcal{A R}_{+}$) we may apply Lemma 4.3.

Suppose that the fixed space of the canonical extension of $R^{\prime}$ to some ultrapower of $M^{\prime}$ is infinite dimensional. Thus we may choose a sequence of states ( $\phi_{k}$ ) in $M^{*}$ and a sequence ( $z_{k}$ ) in ( $\left.M^{*}\right)_{1}{ }^{+}$ satisfying (a) - (b) of Lemma 4.3. Remark (3) above implies that no subsequence of $\left({ }_{k}\right)$ can converge in the o(M', M')-topology.
(a) If $\phi$ is a $\sigma\left(M^{\prime}, M\right)$-accumulation point of $\left(\phi_{k}\right)$, then $\phi \in F i x\left(R^{1}\right)$. Since Fix( $\left.{ }^{r}\right)$ is finite dimensional, the set of accumulation points of the sequence $\left({ }_{\phi_{k}}\right)$ is metrizable in the $o\left(M^{\prime}, M\right)-$ topology. Hence there exists a sequence (k(n)) of natural numbers, such that $\sigma\left(M^{\prime}, M\right)-1 i m_{n} \phi_{k}(n)=\phi$. Consequent $l_{Y} \quad \phi=\sigma\left(M^{\prime}, M^{\prime \prime}\right)-1 i m_{n}$ $\phi_{k}(n)$ by Remark (I) above. But this leads to a contradiction, which proves (a).
(b) Since dim $F i x(R)=d i m f i x\left(R^{\prime}\right)=\operatorname{rank}(P)<\infty$, (b) follows from (a).
(c) Suppose that the fixed space of $R^{\prime}$ is infinite dimensional. Since $F i x\left(R^{r}\right)=M_{*}$ there exists a sequence of states ( $\psi_{n}$ ) in Fix(R') with mutually orthogonal support projections in $M$ (Lerma 4.1). Since every o(M', M) -accumulation point of the $\psi_{n}{ }^{\prime} s$ belongs to Fix (R') , hence is normal, the sequence ( $\psi_{n}$ ) is relatively o ( $\left.\mathrm{M}_{*}, \mathrm{M}\right)$-compact. BY Eberleins theorem, we may assume that this sequence is weakly convergent. By the orthogonality of the $s\left(\psi_{n}\right)^{\prime} s$ this sequence converges to zero in the $s^{*}\left(M_{*} M_{*}\right)$-topology, hence $\lim _{n} \psi_{k}\left(s\left(\psi_{n}\right)\right)=0$ uniformly in $k \in \mathbb{N}$, a contradiction. Consequently dim Fix(R) $<\infty$ and (c) is proved.
(d) We prove dim Fix(R') = 1 and apply (a) once again. Useful for this is the following observation : If $\psi$ is a faithful state on M then the normal part is faithful too. Indeed, if $0 \neq x \in M$ such that $\psi^{(n)}(x)=0$ choose a projection $0 \neq p \in M$ such that $\psi^{(n)}(p)=$ $\psi^{(s)}(p)=0$ (use [Takesaki (1979), Theorem III.3.8]), hence $\psi(p)=0$ which conflicts with the faithfulness of $\psi$.

If $2 \leq \operatorname{dim} F i x\left(R^{\prime}\right)$ there are states $\psi_{1}$ and $\psi_{2}$ in $F i x\left(R^{\prime}\right)$ such that the corresponding support projections are orthogonal in M'' (Remark 4.2). Since every $R^{\prime}$-invariant state $\psi$ is faithful on $M$, $\psi_{i}(n) \neq 0$ (otherwise the norm closed face $\left\{\psi(x)=0: X_{i} M_{+}\right\}$would
be non trivial and $\mu R(\mu)$-invariant). The support projections of the $\psi_{i}^{(n)}{ }^{(n}$ in $M^{\prime \prime}$ are orthogonal (since $\psi_{i}^{(n)} \leqq \psi_{i}$ ) and different from zero. Let $\left(z_{Y}\right)$ be a net in $M_{I}{ }^{+}$such that
$$
\sigma\left(M^{\prime}, M^{\prime}\right)-1 \mathrm{in}_{Y} z_{\gamma}=s\left(\psi_{I}^{(n)}\right)
$$

Then $\lim _{Y} \psi_{1}^{(n)}\left(z_{\gamma}\right)=1$ whereas $\lim _{\gamma} \psi_{2}^{(n)}\left(z_{\gamma}\right)=0$. Let $z_{(n)}$ be a
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-445.jpg?height=83&width=1597&top_left_y=664&top_left_x=224)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-445.jpg?height=87&width=1597&top_left_y=713&top_left_x=224) implies $z \neq 0$ whereas the second shows that $\psi_{2}(n)$ cannot be faithful. Since this is a contradiction, it follows dim Fix (R') $=1$ which proves (d).

The next corollary is an easy application of Theorem 4.4 and of D-III, Proposition 2. 3.

Corollary 4.5. Let $T$ be an identity preserving semigroup of Schwarz type on the predual of a $W^{*-a l g e b r a} M$. Then the following assertions are equivalent:
(a) $T$ is uniformly ergodic with finite dimensional fixed space.
(b) The adjoint weak*-semigroup is strongly ergodic with finite dimensional fixed space.
(c) Every Tri-invariant state is normal.

Proof. If (a) is fulfilled then the semigroup $T$ is strongly ergodic on $M_{*}$. Since
$$
\operatorname{dim} F i x(T)=\operatorname{dim} F i x\left(T^{\prime}\right)<\infty
$$
there exist normal states $\phi_{1} \ldots \phi_{n}$ in $F i x(T)$ and $x_{1}, \ldots x_{k}$ in Fix( $\left.T^{\prime}\right)$ such that $\phi_{n}\left(x_{m}\right)=\delta_{n, m} \quad(1 \leq n, m \leqq k)$ and
$$
P=\sum_{i=1}^{k} \phi_{i} 8 x_{i}
$$
is the associated ergodic projection. If (C(s)) s>0 is the family of Césaro means of $T$, then
$$
\lim _{s \rightarrow \infty} C(s)^{\prime \prime}(\psi)=\sum_{i=1}^{k} \phi_{i}(\psi) x_{i} \in_{M_{*}}
$$
for every $\psi \in M^{\prime}$. Hence Fix(T'1) $\mathrm{C}_{\mathrm{*}} \mathrm{M}_{\mathrm{*}}$ which proves (c).

If (c) is fulfilled then $F i x(T)=F i x\left(T{ }^{\prime \prime}\right)$. Therefore the fixed space of $T^{\prime}$ separates the points of Fix(T") which shows that $T^{\prime \prime}$ is strongly ergodic on $M$ (Krengel (1985), Chap.2, Thm.l.4]). If
(b) holds then
$$
P=\operatorname{Iim}_{\mu \neq 0} \mu R\left(\mu, A^{\prime}\right)
$$
exists in the strong operator topology, where $A$ is the generator of $T^{\prime}$. Therefore dim $\operatorname{Fix}\left(\mu \mathrm{R}(\mu)^{\wedge}\right)<\infty$ in some ultrapower of $M$ (Theorem 4.4.(b)). It follows from D-III, Proposition 2.3 that 0 is a pole of the resolvent of $R(\ldots A)$. Therefore $T$ is uniformly ergodic.

NOTES.
Section 1 . The stability concepts appearing in Theorem 1.7 coincide not only for positive semigroups on C*-algebras but on any order unit Banach space. We refer to Batty-Robinson (1984) for this more general setting and to B-IV, Section 1 for the analogous results on $C_{0}(X)$.

Section 2. Theorem 2.2 generalizes the Liapunov stability theorem from the matrix algebra $B\left(\mathbb{C}^{\mathrm{n}}\right)$ to arbitrary $W^{*}$-algebras. For the algebra $\mathrm{B}(\mathrm{H})$ it is due to M1'stein (1975) and in the general form to Groh-Neubrander (1981).

Section 3. From the many papers dealing more or less explicitely with the asymptotic behavior of semigroups on operator algebras we quote Frigerio-Verri (1982) and Watanabe (1982). The background for our ergodic theorems (Prop. 3.3 and Prop. 3.4) can be found best in Krengel (1985). The "automatic" convergence theorem for an irreducible $W^{*}$-dynamical system on $B(H)$ stated in Corollary 3.9 is the continuous version of a result in Groh (1984c). Finally, the characterization of convergence towards a periodic semigroup through spectral properties of the generator (Thm. 3.11) is due to Nagel (1984) in the commutative, i.e. L ( $\mu$ ), case (see also C-IV, Thm.2.14).

Section 4. Again we refer to Krengel (1985) for the (uniform) ergodic theory for a single operator or a one-parameter semfgroup on a Banach space. The characterization given in Corollary 4.5 for positive semigroups on W*-algebras is based on a sophisticated use of ultrapower techniques and has its discrete forerunners in Lotz (1981) and Groh (1984b).