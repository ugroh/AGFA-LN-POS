Motivated by the classical results of Perron and Frobenius one expects the following spectral properties for the generator $A$ of a positive semigroup: The spectral bound $s(A):=s u p(\operatorname{Re}(\lambda) ; \lambda \in q(A)\}$ belongs to the spectrum $\sigma(A)$ and the boundary spectrum

\[
\sigma_{b}(A):=\sigma(A) \cap\left\{s(A)+i^{\mathbb{R}}\right\}
\]

possesses a certain symmetric structure, called cyclicity.

Results of this type have been proved in Chapter Brifl for positive semigroups on commutative $c^{*-a l g e b r a s, ~ b u t ~ i n ~ t h e ~ n o n-c o m m u t a t i v e ~ c a s e ~}$ the situation is more complicated. While 's(A) Go(A)' still holds (see Greiner-Voigt-Wolff (1980)) the cyclicity of the boundary specm trum $\sigma_{b}(A)$ is true only under additional assumptions on the semigroup (e.g., irreducibility, see Section $I$ below).

For technical reasons we consider mostly strongly continuous semigroups on the predual of a $W^{*}$-algebra $M$ or its adjoint semigroup which is a weak*-continuous semigroup on $M$.

1. SPECTRAL THEORY FOR POSITIVE SEMIGROUPS ON PREDUALS

The aim of this section is to develop a Perron-Frobenius theory for identity preserving semigroups of Schwarz type on $W^{*}$-algebras. But as we will show in the example preceding Theorem 1.1 below the boundary spectrum is no longer cyclic. The appropriate hypothesis on the semigroup implying the desired results seems to be the concept of irreducibility.

Let us first recall some facts on normal linear functionals. If $\phi$ is a normal linear functional on a $W^{*}$-algebra $M$ then there exists a partial isometry $u \in M$ and a positive linear functional | $\mid \in \mathrm{M}_{\star}$ such that

\[
\begin{gathered}
\phi(x)=|\phi|(x u)=:(u|\phi|)(x), x \in M \\
u^{*} u=s(|\phi|)
\end{gathered}
\]

where $s(|\phi|)$ denotes the support projection of $|\phi|$ in $M$. We refer to this as the polar decomposition of $\phi$ [Takesaki (1979), Theorem III.4.2]. In addition, $|\phi|$ is uniquely determined by the following two conditions [Takesaki (1979), Proposition III.4.6]:

\[
\|\phi\|=\||\&|\| .
\]



\[
|\phi(x)|^{2} \leqq|\phi|\left(x x^{\star}\right) \quad(x \in M)
\]

For the polar decomposition of $\phi^{*}$, where $\phi^{*}(x)=\phi^{*}\left(x^{*}\right)^{*}$, we obtain

\[
\phi^{*}=\mathrm{u}^{*}\left|\phi^{*}\right|,\left|\phi^{*}\right|=u|\phi| u^{*} \text { and } u u^{*}=s\left(\left|\phi^{*}\right|\right)
\]

It is easy to see that $u * \in s(|\phi|) M$.

If $\Psi$ is a subset of the state space of a C*-algebra $M$, then $\Psi$ is called faithful if $0 \leqq x \in M$ and $\psi(x)=0$ for all $\psi \in \Psi$ implies $x=0$. $\Psi$ is called subinvariant for a positive map $T \in(M)$ (resp., positive semigroup $T$ ) if $T^{\prime} \psi \leqq \Downarrow$ for all $\psi \subset \psi$ (resp.r $T(t) ' \psi \leq \psi$ for all $T(t) \in T$ and $\psi \in \Psi$ ). Recall that for every positive map $T \in L(M)$ there exists a state $\phi$ on $M$ such that $T^{\prime \prime} \phi=$ $r(T) \phi \quad[G r o h(1981)$, Theorem 2.1], where $r(T)$ denotes the spectral radius of $T$.

Let us start our investigation with two lemmas. Recall that fix(T) is the fixed space of $T$, i.e. the set $\{x \in M: T x=x\}$.

Lemma 1.1. Suppose $M$ to be a $C^{*-a l g e b r a ~ a n d ~} T \in L(M)$ an identity preserving schwarz map.
(a) Let b: $M \times M \rightarrow M$ be a sesquilinear map such that for all m ( m $b(z, z) \geq 0$. Then $b(x, x)=0$ for some $x \in M$ if and only if $b(x, y)=0$ and $b(y, x)=0$ for all $y \in M$.
(b) If there exists a faithful family $\Psi$ of subinvariant states for $T$ on $M$, then $F i x(T)$ is a $c *-s u b a l g e b r a$ of $M$ and $T(x y)=x T(y)$ for all $x \in F i x(T)$ and $Y \in M$.

Proof. (a) Take $0 \leqq \psi \in M^{*}$ and consider $f:=\psi o b$. Then $f$ is a positive semidefinite sesquilinear form on $M$ with values in $\mathbb{C}$. From the Cauchy-Schwarz inequality it follows that $f(x, x)=0$ for some $x \in M$ if and only if $f(x, y)=0$ and $f(y, x)=0$ for all $y \in M$. Since the positive cone $M^{*}{ }_{+}$is generating, assertion (a) is proved.
(b) Since $T$ is positive it follows $T(x)^{*}=T\left(x^{*}\right)$ for all $x \in M$. Hence Fix(T) is a self adjoint subspace of $M$, i.e. invariant under the involution on $M$. For every $x, y \in M$ let

\[
\mathrm{b}(\mathrm{x}, \mathrm{y}):=\mathrm{T}\left(\mathrm{x} y^{*}\right)-\mathrm{T}(\mathrm{x}) \mathrm{T}(\mathrm{y})^{*} .
\]

Then $b$ satisfies the assumptions of (a). If xfFix(T) then

\[
0 \leqq X^{*}=(T x)(T x)^{*} \leqq T\left(x^{*}\right)
\]

hence

\[
0 \leqq \psi\left(T\left(x x^{*}\right)-x x^{*}\right) \leqq 0 \text { for all } \psi \in \Psi
\]

But this implies $T\left(x x^{*}\right)=T(x) T(x) *=x x^{*}$. Consequently, $b(x, x)=0$. Hence $T\left(x y^{*}\right)=x T(y)^{*}$ for all $y \in M$ and (b) is proved.
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-03.jpg?height=56&width=1620&top_left_y=1948&top_left_x=207) Schwarz map on $M$ and $S \in L(M)$ such that $S(x)(S X)^{*} \leqq T\left(x x^{*}\right)$ for every $x \in M$.
(a) If $v \in M$ such that $S\left(v^{*}\right)=v^{*}$ and $T\left(v^{*} v\right)=v^{*} v$, then $T(x v)=$ $S(x) v$ for all $x \in M$.
(b) suppose there exists $\phi \in M_{*}$ with polar decomposition $\phi=u|\phi|$ such that $S_{*} \phi=\phi$ and $T_{*}|\phi|=|\phi|$. If the closed subspace $s||\phi|) M$ is $T$-invariant, then $s u^{*}=u^{*}$ and $T\left(u^{*} u\right)=u^{*} u$.

Proof. (a) Define a positive semidefinite sesquilinear map $b: M \times M \rightarrow M$ by

\[
b(x, y):=T\left(x y^{*}\right)-S(x) S(y)^{*} \quad(x, y \in M)
\]

Since $b\left(v^{*}, v^{*}\right)=0$ we obtain $b\left(x^{*} v^{*}\right)=0$ for all $x \in M$ (Lemma 1.1.a), hence $T(x v)=S(x) v$.
(b) since $s(|\phi|) M$ is a closed right ideal, the closed face $\mathbf{F}:=s(|\phi|)\left(M_{+}\right) s(|\phi|)$ determines $s(|\phi|) M$ uniquely, i.e.,

\[
s(|\phi|) M=\left\{x \in M: X x^{*} \in F\right\}
\]

[Pedersen (1979), Theorem 1.5.2]. Since $T$ is a Schwarz map and $s(|\phi|) M$ is $T$-invariant, it follows $T F=F$. On the other hand, if xes (| $\mid \boldsymbol{\|} \|$ then $x x^{*} \in F$. Consequently,

\[
0 \leqq S(x) S(x)^{*} \leqq T\left(x x^{*}\right) \in F,
\]

whence $s(x) \in s(|\phi|) M$.

Next we show $T\left(u^{*} u\right)=u^{*} u$ and $S u^{*}=u^{*}$. For this recall that $\mathrm{u}^{*} \epsilon_{s}(|\phi|) M$. First of all

\[
\begin{gathered}
0 \leqq\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right)^{*} \leqq \\
\leqslant T\left(u^{*} u\right)-u^{*} S\left(u^{*}\right)^{*}-\left(S u^{*}\right) u+u^{*} u .
\end{gathered}
\]

since $S_{*} \phi=\phi, T_{*}|\phi|=|\phi|$ and $\phi=u|\phi|$ it follows

\[
\begin{gathered}
0 \leqq|\phi|\left(\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right)^{*}\right) \leqq \\
\leq 2|\phi|\left(u^{*} u\right)-|\phi|\left(S\left(u^{*}\right) u\right)^{*}-|\phi|\left(S\left(u^{*}\right) u\right)= \\
=2|\phi|\left(u u^{*}\right)-\phi\left(u^{*}\right)^{*}-\phi\left(u^{*}\right)= \\
=2\left(|\phi|\left(u^{*} u\right)-|\phi|\left(u^{*} u\right)\right)=0 .
\end{gathered}
\]

Since $\left(S u^{*}-u^{*}\right)\left(S u^{*}-u^{*}\right) \in F$ and $|\phi|$ is faithful on $F$ we obtain su* $=u^{*}$. Consequently,

\[
0 \leq u * u=\left(S u^{*}\right)\left(S u^{*}\right) * \leq T\left(u^{*} u\right)
\]

Hence $T\left(u^{\star} u\right)=u^{*} u$ by the faithfulness and $T$-invariance of $|\phi|$.

Remark 1.3. Take $S$ and $T$ as in Lemma 1.2 (b) If $V_{u * ~(r e s p . ~}^{\text {. }}$ ( $V_{u}$ ) is the map $\left(x \rightarrow x^{*}\right) \quad(r e s p .(x \rightarrow x u))$ on $M$, then $V_{u *}$ is a continuous bijection from Ms (| $\phi \mid)$ onto $M s(\mid \phi \|)$ with inverse $v_{u}$ (because $V_{u}{ }^{\circ V_{u}}{ }^{*}=I d_{M s}(|\phi|)$ and $V_{u} *{ }^{*} V_{u}=I d_{M s}(|\phi *|)$. Let $x \in M$. From $T(x u)=S(x) u$ we obtain $T(x u) u^{*}=S(x) u^{*}$. In particular, if Ms (| $\left.\phi^{*} \|\right)$ is $S$-invariant, then

\[
\left(V_{u^{*}}{ }^{\circ} T^{\circ} V_{u}\right)(x)=T(x u) u^{*}=S(x)
\]

for every $x \in M s\left(\left|\phi^{*}\right|\right)$. Let $T \mid \quad$ (resp. $S \mid$ ) be the restriction of $T$ to Ms (| $\mid$ ) (resp. of $s$ to Ms (| $\left.\phi^{*} \mid\right)$ ) . Then the following diagram is commutative :
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-05.jpg?height=415&width=977&top_left_y=1089&top_left_x=525)

In particular, o(S $)=\sigma(T \mid$ ) Therefore we may deduce spectral properties of ${ }^{s}$ from $T$ and vice versa. More concrete applications of Lemma 1.2. will follow.

We now investigate the fixed space $F i x(R):=F i x(\lambda R(\lambda)), \lambda \in D, o f a$ pseudo-resolvent $R$ with values in the predual of a w*-algebra M.

Proposition 1.4. Let $R$ be a pseudoresolvent on $D=\{\lambda \in \mathbb{C}$ : Re ( $\lambda)>0\}$ with values in the predual $M_{*}$ of a $W^{*}$-algebra $M$ and suppose $R$ to be identity preserving and of Schwarz type.
(a) If $\alpha \in R$ and $\psi \in M_{*}$ such that $(\gamma-i \alpha) R(\gamma) \psi=\psi$ for some $\gamma \in D$, then $\lambda R(\lambda)|\psi|=|\psi|$ and $\lambda R(\lambda)|\psi *|=|\psi *|$ for all $\lambda \in D$.
(b) Fix(R) is invariant uncer the involution in $M_{*}$. If $\psi \in F i x(R)$ is self adjoint, then the positive part $\psi^{+}$and the negative part $\psi^{-}$of $\psi$ are elements of $F i x(R)$.

Proof. If ( $\gamma$ - ia)R(y) $\psi=\psi$ then $(\lambda-i a) R(\lambda) \psi=\psi$ for all $\lambda \in D$. In particular, $\mu \mathrm{R}(\mu+\mathbf{i} a) \psi=\psi\left(\mu \in \mathbb{R}_{+}\right)$. For all $x \in M$ we obtain

\[
\begin{gathered}
|\psi(x)|^{2}=\mid\left\langle\mu R(\mu+i \alpha)^{\prime} x, \psi>\left.\right|^{2} \leq\right. \\
\leqq\|\psi\|<\left(\mu R(\mu+i \alpha x)^{\prime} x\right)\left(\mu R(\mu+i \alpha x)^{\prime} x\right)^{*}, \psi>\leqq \\
\leqq\|\psi\|<\mu R(\mu)^{*}\left(x x^{*}\right), \mid \psi \|^{\prime}>
\end{gathered}
\]

(D-I, Corollary 2.2). Since

\[
\begin{gathered}
\|\psi\|=\||\psi|\|=|\psi|(I)= \\
=\left\langle\mu \mathrm{R}(\mu)^{\prime} 1,\right| \psi| \rangle=\|\mu \mathrm{R}(\mu)|\psi|\|,
\end{gathered}
\]

we obtain $\mu \mathrm{R}(\mu)|\psi|=|\psi|$ by the uniqueness theorem (*) mentioned at the beginning. Therefore $|\psi| \epsilon F i x(\mathrm{~F})$. Since

\[
0 \leq\left(\mu \mathrm{R}(\mu)^{\prime} \mathrm{x}\right)\left(\mu \mathrm{R}(\mu)^{\prime} \mathrm{x}\right)^{*} \leqq \mu \mathrm{R}(\mu)^{\prime} \mathrm{XX} \mathrm{x}^{*}
\]

the map $R(\mu)$ is positive. Consequently ( $\mu+i \alpha) R(\mu) \psi^{*}=\psi *$ from which $|\psi *| \epsilon F i x(R)$ follows.
If $\quad$ ffix (R) is selfadjoint with Jordan decomposition $\phi=\phi^{+}{ }^{+} \phi^{+}$, then $|\phi|=\phi^{+}+\phi^{-}$[Takesaki (1979), Theorem III.4.2.]. From this we obtain that $\phi^{+}$and $\phi^{-}$are in Fix (R).

Corollary I.5. Let $T$ be an identity preserving semigroup of Schwarz type on $M_{*}$ with generator $A$ and suppose $P o(A) \cap i \mathbb{R} \neq \emptyset$.
(a) If a¢GR and $\psi \in \operatorname{ker}(i \alpha-A)$, then $|\psi|$ and $|\psi *|$ are elements of $\operatorname{Fix}(T)=\operatorname{ker}(A)$.
(b) Fix(T) is invariant under the involution of $M_{*}$. If $\psi \in F i x(T)$ is self adjoint, then the positive part $\psi^{+}$and the negative part $\psi{ }^{-}$of $\psi$ are elements of $F i x(T)$.

The proof follows immediately from D-I, Corollary 2.2 and the fact that $\operatorname{ker}(A)=\operatorname{Fix}(\lambda R(\lambda, A))$ for all $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda)>0$.

If $T$ is the semigroup of translations on $L^{l}(\mathbb{R})$ and $A^{\prime}$ the gene-
rator of the adjoint weak*-semigroup, then $P o(A) \quad$ i $A=\varnothing$, while Po(A') $\cap$ i $=$ iR , For that reason we cannot expect a simple connection between these two sets. But as we shall see below, if a semigroup on the predual of a $\mathrm{W}^{*}-\mathrm{algebra}$ has sufficiently many invariant states, then the point spectra of $A$ and $A^{\prime}$ contained in iR are identical. Helpful for these investigations will be the next lemma.

Lemma 1.6. Let $R$ be a pseudo-resolvent on $D=\{\lambda \in \mathbb{C} ; \operatorname{Re}(\lambda)>0\}$ with values in a Banach space $E$ such that $\|\mu \mathrm{R}(\mu+i \alpha)\| \leq I$ for all $(\mu, \alpha) \in \mathbb{R} \times \mathbb{R}$. Then

\[
dim Fix(\lambdaR(\lambda + i\alpha)) 仓 dim Fix(\lambdaR(\lambda + i\alpha|')
\]

for all $\lambda \in D$.

Proof. Let $(\mu, \alpha) \in \mathbb{R}_{+} \times \mathbb{R}$ and $S:=\mu R(\mu+i \alpha)$. since $s$ is a contraction, its adjoint $S^{\prime}$ maps the dual unit ball $E^{\prime}$ i into itself. Let $u$ be a free ultrafilter on $\left[1,{ }^{\infty}\right)$ which converges to 1 . Since $E^{\prime}{ }^{\prime}$ is $\sigma\left(E^{\prime}, E\right)$-compact,

\[
\psi_{o}:=\operatorname{Iim} U^{(\lambda-1) R(\lambda, S)^{\prime} \psi}
\]

exists for all $\psi \in E^{\prime}$, Since $S^{\prime}$ is $\sigma\left(E^{\prime}, E\right)$-continuous and since $S^{\prime} R(\lambda, S)^{\prime}=\lambda R\left(\lambda, S^{\prime}\right)-I d$ we conclude $\psi_{o} \in F i x\left(S^{\prime}\right)$.

Take now $0 \neq x_{0} \in F 1 x(S)$ and choose $\psi \in E^{*}{ }_{I}$ such that $\psi\left(x_{0}\right)$ is different from zero. From the considerations above it follows

\[
\psi_{0}\left(x_{0}\right)=\operatorname{Iim} U(\lambda-1) \psi\left(R(\lambda, S) x_{0}\right)=\psi\left(x_{0}\right) \neq 0
\]

hence $0 \neq \psi_{o} \in F i x(S)$. Therefore Fix(s') separates the points of Fix (S) . From this it follows that

\[
dim Fix(S) S dim Fix(S') .
\]

Since $R$ and $R^{\prime}$ are pseudo-resolvents, the assertion is proved.

Corollary 1.7. Let $T$ be a semigroup of contractions on a Banach space $E$ with generator A . Then

\[
dim ker(i\alpha - A) \leqq dim ker(i\alpha - A')
\]

for all $\alpha \in R$.

This follows from Lemma 1.6 because $F i x(\lambda \mathrm{f}(\lambda+i \alpha))=\operatorname{ker}(i a-A)$.

Proposition 1.8 . Let $T$ be an identity preserving semigroup of Schwarz type with generator $A$ on the predual of a $W^{*}$-algebra and suppose that there exists a faithful family $\Psi$ of T-invariant states. Then for all $a \in \mathbb{R}$ we have

\[
dim ker(i\alpha - A) = dim ker(ia - A')
\]

and

\[
\operatorname{Po}(A) \cap i \mathbb{P}_{1}=P \sigma\left(A^{r}\right) \cap \mathbf{i} R .
\]

Proof. The inequality dim ker(ia - A) $\leqslant$ dim ker (io - $\left.A^{\mp}\right)$ follows from Corollary 1.7 .

Let $D=\{\lambda \in \mathbb{C}: \operatorname{Re}(\lambda)>0\}$ and $R$ the pseudo-resolvent induced by $R(\lambda, A)$ on $D$. Then $R$ is identity preserving and of Schwarz type. Take $i \alpha \in P o(A)(\alpha \in R)$ and choose $0<\mu \in \mathbb{R}$. If $\psi_{\alpha} \in M_{*}$ is of norm one with polar decomposition $\psi_{a}=u_{a}\left|\psi_{\alpha}\right|$ such that $\psi_{a}=(\mu-i \alpha) R(\mu) \psi_{a}$ then $\mu \mathrm{R}(\mu)\left|\psi_{\alpha}\right|=\left|\psi_{a}\right| \quad$ (Proposition 1.4.a). Since

\[
\mu R(\mu)^{\prime}\left(1-s\left(\left|\psi_{\alpha}\right|\right)\right) \leqq 1-s\left(\left|\psi_{\alpha}\right|\right)
\]

we obtain $\mu R(\mu)^{\prime} s\left(\left|\psi_{a}\right|\right)=s\left(\left|\psi_{\alpha}\right|\right)$ by the faithfulness of $\Psi$. Hence the maps $S:=(\mu-i \alpha) R(\mu)^{\prime}$ and $T:=\mu R(\mu)^{\prime}$ fulfil the assumptions
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-08.jpg?height=50&width=1615&top_left_y=1894&top_left_x=232) implies $u_{\alpha}^{*} \in D\left(A^{\top}\right)$ and $A^{\prime} u_{\alpha}^{*}=i a u_{\alpha}^{*}$.

If $\operatorname{ia\in Po(A'),~} \alpha \in \mathbb{R}$, choose $0 \neq v_{0}$ such that

\[
v_{\alpha}=(\mu-i \alpha) R(\mu)^{\prime} v_{\alpha} \quad\left(\mu \in \mathbb{R}_{+}\right)
\]

and $\psi \in \Psi$ such that $\psi\left(v_{\alpha} v_{\alpha}^{*}\right) \neq 0$. since

\[
\begin{gathered}
0 \leqslant v_{\alpha} v_{a}^{*}=\left((\mu-i \alpha) R(\mu)^{\prime} v_{\alpha}\right)\left((\mu-i \alpha) R(\mu)^{\prime} v_{\alpha}\right)^{*} \leq \\
\leq \mu R(\mu)^{\prime}\left(v_{\alpha} v_{\alpha} *\right),
\end{gathered}
\]

we obtain $\mu R(\mu)^{\prime}\left(v_{\alpha} v_{\alpha}^{*}\right)=v_{\alpha} v_{\alpha}{ }^{*}$ because $\Psi$ is faithful.

Hence from Lemma 1.2.a it follows

\[
\mu \mathrm{R}(\mu)^{\prime}\left(x v_{\alpha}^{*}\right)=\left(\left(\mu-i_{\alpha}\right) \mathrm{R}(\mu)^{\prime} x\right) v_{a}^{*}
\]

for all $x \in M$. Let $\psi_{a}$ be the normal linear functional $\left(x \rightarrow \psi\left(x v_{a}^{*}\right)\right)$ on $M$ and note that $\psi_{\alpha}\left(v_{\alpha}\right) \neq 0$. Then

\[
\begin{gathered}
\left. < x,(\mu-i \alpha) R(\mu) \psi_{\alpha}\right\rangle=\left\langle\left(\left(\mu-i_{\alpha}\right) R(\mu)^{*} x\right) v_{\alpha}^{*}, \psi\right\rangle= \\
\left.<\mu R(\mu)^{\prime}\left(x v_{\alpha}^{*}\right), \psi\right\rangle=\psi\left(x v_{\alpha}^{*}\right)=\psi_{\alpha}(x)
\end{gathered}
\]

for all $x \in M$. Consequently $i_{a} \in \mathrm{P}_{\sigma}(A)$ and

\[
dim ker(ia - A') s dim ker(ia - A) ,
\]

which proves the assertion.

Remark 1.9. From the above proof we obtain the following: If $0 \neq \psi_{\alpha}$ ker ( $\left.i_{\alpha}-A\right)$ with polar decomposition $\psi_{\alpha}=u_{\alpha}\left|\psi_{\alpha}\right|(\alpha \in \mathbb{R})$ then $A^{\prime} u_{a}=i_{a} u_{a}$. Conversely, if $0 \neq v_{a} \in k e r\left(i_{a}-A^{\prime}\right)$, then there exists $\psi \in \Psi$ such that $\psi\left(v_{a} v_{a}^{*}\right) \neq 0$ and the normal linear form

\[
\psi_{\alpha}:=\left(x \rightarrow \psi\left(x v_{\alpha}^{*}\right)\right)
\]

is an eigenvector of $A$ pertaining to the eigenvalue $i o$.

If $T$ is a $C_{o}$-semigroup of Markov operators on a commutative $C^{*}-a 1-$ gebra with generator $A$, it has been shown in B-III, that the boundary spectrum $\sigma(A) \quad n \quad i \mathbb{R}$ of its generator is additively cyclic. This is no longer true in the non commutative case:

For $0 \neq \lambda \in i \mathbb{R}$ and $t \in \mathbb{R}$ let

\[
u_{t}:=\left(\begin{array}{ll}
1 & 0 \\
0 & e^{\lambda t}
\end{array}\right) \quad \in M_{2}(c)
\]

The semigroup of *-automorphisms $\left(x+u_{t} x_{t}{ }^{*}\right)$ on $M_{2}(c)$ is identity
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-10.jpg?height=47&width=1617&top_left_y=336&top_left_x=228) $\left[0, \lambda, \lambda^{*}\right\}$ hence is not additively cyclic.

It turns out that, in order to obtain a non conmutative analogue of the Perron-Frobenius theorems, one has to consider semigroups which are irreducible. Recall that a semigroup $S$ of positive operators on an ordered Banach space ( $E, E_{+}$) is called irreducible if no closed face of $E_{+}$, different from $\{0\}$ and $E_{+}$, is invariant under $S$. Here a face $F$ in $E$ is a subcone of $E_{+}$such that the conditions $0 \leqq x \leqq y$, $x \in E$, $y \in F$ imply $x \in F$ (compare Definitions 3.1 in $B-I I I$ and $C-I I I)$.
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-10.jpg?height=50&width=1623&top_left_y=1026&top_left_x=225) maps on $M$ weak* -irreducible, if no $\sigma\left(M_{*}\right)$-closed face of $M_{+}$is S-invariant. Since the norm closed faces of $M_{*}$ and the o(M, $M_{*}$ )closed faces of $M$ are related by formation of polars with respect to the dual system $M_{*} M_{*}$ (see [Pedersen (1979), Theorem 3.6.11 and Theorem 3.10.7.7) a semigroup $S$ is (norm) irreducible on $M_{*}$ if and only if its adjoint semigroup is weak*-irreducible.

Theorem I.10. Let $T$ be an irreducible, identity preserving semigroup of schwarz type with generator $A$ on the predual of a $W^{*}-a I-$ gebra and suppose $P_{g}(A)$ i i $\neq \varnothing$.
(a) The fixed space of $T$ is one dimensional and spanned by a faithful normal state.
(b) Po(A) $\cap$ iR is an additive subgroup of $i \mathbb{R}$,

\[
\sigma(A)=\sigma(A)+(\operatorname{Po}(A) \cap i \mathbb{R})
\]

and every eigenvalue in if is simple.
(a)* The fixed space of the adjoint weak*-semigroup T* is onedimensional.
(b)* $P_{\sigma}\left(A^{\prime}\right) \| i \mathbb{R}=P_{o}(A) \quad$ $\quad i$ f for the generator $A^{\prime}$ of the adjoint semigroup, and every y€po(A') $\quad$ i ir $i s$ simple.

Proof. Since $\mathrm{P}_{\sigma}(\mathrm{A}) \quad \mathrm{C}$ iR $\neq \emptyset$ there exists $\psi \in \mathrm{Fix}(T)+$ of norm one (Corollary 1.5 ). If $F:=\left\{X \in M_{+} ; \psi(x)=0\right\}$ then $F$ is a o( $M_{*} M_{*}$ ) closed, $T^{\prime}$-invariant face in $M$, hence $F=\{0\}$. Therefore every $0 \neq \psi \in F i x(T)+i s$ faithful. Let $\psi_{1}, \psi_{2} \in F i x(T){ }_{+}$be states such that
$f:=\psi_{I}-\psi_{2}$ is different from zero. If $f=f^{+}-f^{-}$is the Jordan decomposition of $f$, then $f^{+}$and $f^{-}$are elements of $F i x(T)$, whence faithful. since the support projections of these two normal linear functionals are orthogonal, we obtain $f^{+}=0$ or $f^{-}=0$ which implies $\psi_{1} \leqslant \psi_{2}$ or $\psi_{2} \leqslant \psi_{I}$. Consequently $\psi_{2}=\psi_{1}$. Since Fix(T) is positively generated (Corollary 1.5), Fix (T) $=\mathbb{C}_{\phi}$ for some faithful normal state $\phi$.

Let $\mu \in \mathbb{R}+$ and $\alpha \in \mathbb{R}$ such that $i \alpha \in P o(A)$. If $\psi_{\alpha}=u_{\alpha}\left|\psi_{\alpha}\right|$ is a normalized eigenvector of $A$ pertaining to $i \alpha$, then $\phi=\left|\psi_{0}\right|=\left|\psi_{a}{ }^{*}\right|$ by Corollary 1.5 and the above considerations. Hence $u_{\alpha} u_{\alpha}{ }^{*}=u_{\alpha}^{*} u_{\alpha}=$ $s(\phi)=1$. Since

\[
(\mu-i \alpha) R(\mu, A) \psi_{a}=\psi_{a}
\]

and

\[
\mu \mathrm{R}(\mu, \mathrm{~A})\left|\psi_{a}\right|=\left|\psi_{\alpha}\right|
\]

we obtain by Lenma I. 2.b that
(1) $\mu \mathrm{R}(\mu, \mathrm{A})=\mathrm{V}_{a} \rho \mu \mathrm{R}\left(\mu+\mathrm{i}_{a}, \mathrm{~A}\right)=\mathrm{V}_{a}^{-1}$
where $V_{a}$ is the map $\left(x+x_{\alpha}\right)$ on $M$. Similarly for i $\beta \in P(A)$, we find $V_{\beta}$ such that $1=u_{\beta} u_{\beta}^{*}=\mathrm{u}_{\beta} \mathrm{u}_{\beta}{ }^{*}$ and
(2) $\mu R(\mu, A)=V_{\beta}^{o \mu R}(\mu+i \beta, A) \circ V_{\beta}^{-I}$.

Hence

\[
\begin{equation*}
\mu \mathrm{R}(\mu, A)=V_{\alpha \beta} \mu \mathrm{R}(\mu+i(\alpha+\beta), A)=V_{\alpha \beta}^{-1} \tag{3}
\end{equation*}
\]

where $V_{a \beta}:=V_{a} V_{\beta}$. Since $u_{a}$ is unitary in $M$, it follows from (1) that ia is an eigenvalue which is simple because Fix(T)= Fix ( $\mu \mathrm{R}(\mu, A)$ is one dimensional. From (3) it follows that $i(\alpha+\beta) \in \operatorname{Po}(A)$ since $0 \in \operatorname{Po}(A)$ and $V_{\alpha \beta}$ is bijective. From the identity (I) we conclude that $\sigma(R(\mu, A))=\sigma(R(\mu+i \alpha))$, which proves

\[
\sigma(A)+(P \sigma(A) \cap i \mathbb{R}) \subseteq \sigma(A)
\]

The other inclusion is trivial since $0 \in P(A)$.

Remarks I.Il. (a) Let $\quad$ be the normal state on m such that $\operatorname{Fix}(T)=\mathbb{C}$ and let $H:=\operatorname{Po}(A) \cap i . R$. From the proof of Theorem l.IU it follows that there exists a family $\left\{u_{\eta}: \eta \in H\right\}$ of unitaries in $M$ such that $A^{r} u_{\eta}=-\eta u_{\eta}$ and $A\left(u_{\eta} \phi\right)=\eta\left(u_{\eta} \phi\right)$ for all $\eta \in H$.
(b) If the group $H$ is generated by a single element, $i, e ., H=i \gamma \mathbb{Z}$ for some $\gamma \in R$ then the family $\left\{u_{\gamma}^{k}: k \in \mathbb{Z}\right\}$ is a complete family of eigenvectors pertaining to the eigenvalues in $H$, where $u_{Y} \in M$ is unitary such that $A^{\prime} u_{Y}=i_{Y} u_{Y}$.

Proposition 1.12 . Suppose that $T$ and $M$ satisfy the assumptions of Theorem 1.10, and let $N_{*}$ be the closed Iinear subspace of $M_{*}$ generated by the eigenvectors of $A$ pertaining to the eigenvalues in $i \mathbb{R}$. Denote by $T_{0}$ the restriction of $T$ to $N_{*}$. Then
(a) $G:=\left(T_{0}\right)^{-} \underline{C} L_{S}\left(N_{*}\right)$ is a compact, Abelian group.
![](https://cdn.mathpix.com/cropped/2025_01_15_b69631a699405f4b7869g-12.jpg?height=64&width=1238&top_left_y=1307&top_left_x=232)

Proof. For $\eta \in H:=\operatorname{Po}(A)$ in iR let

\[
U(\mathrm{r}):=\left\{\psi \in \mathrm{D}(\mathrm{~A}): A_{\psi}=\mathrm{n} \psi\right\}
\]

and $U=\{U(\pi): \pi \in H\}$. Then $\left(\operatorname{span}[J)^{-}=N_{*}\right.$. For each $\psi \in U$ there exists $\eta \in H$ such that

\[
\left\{\mathbb{T}_{0}(t) \psi: t \in \mathbb{R}_{+}\right\}=\left\{\mathrm{e}^{-\pi t} \psi: t \in \mathbb{R}_{+}\right\}
\]

Consequently this set is relatively compact in $L_{s}\left(\mathbb{N}_{*}\right)$. From [Schaefer (1966),III.4.5] we obtain that $G$ is compact.

Next choose $\psi_{1}$, $\cdots \psi_{n} \in \mathbb{J}$, $0<\operatorname{set}$ and $\delta>0$. Since $T_{0}(t) \psi_{i}=$ $e^{\pi_{i}} \psi_{i}(l s i s n)$ for some $\eta_{i} \in H$, it follows from a theorem of Kronekker (see, [Jacobs (1976), satz 6.1., p.77]) that there exists $s$ \& $t$ such that

\[
\left|(1,1, \ldots, 1)-\quad\left(e^{\pi} 1^{t}, \quad e^{\pi} 2^{t}, \ldots, \quad e^{\pi} n^{t}\right)\right|<\delta,
\]

hence

\[
\sup \left\{\left\|\psi_{i}-T_{0}(t) \psi_{i}\right\|: 1 \leq i \leqq n\right\}<\delta
\]

or $I d \mid N_{*} \in\left\{T_{o}(t): t>5\right\}^{-} G_{s}\left(N_{*}\right)$.

Finally we prove the group property of $G$. Let $v$ be an ultrafilter on $\mathbb{R}_{\text {such that }}$ lim $V_{o}(t)=I d$ in the strong operator topology. For positive $s \in \mathbb{R}$ let $S:=\lim _{V} T(t-s)$. Then $S T_{0}(s)=T_{o}(s) S=I d$, hence $T_{o}(s)^{-1}$ exists in $G$ for all $s \in \mathbb{R}_{+}$. From this it follows that $G$ is a group.

Remark I.I3. (a) Let $k: \sqrt[R]{ } \rightarrow G$ be given by

\[
k(t)= \begin{cases}T_{0}(t) & \text { if } 0 \leq t \\ T_{0}(t)^{-1} & \text { if } t \leqq 0\end{cases}
\]

Then $k$ is a continuous homomorphism with dense range, i.e. ( $k, k$ ) is solenoidal (see [Hewitt-Ross (1963)]).
(b) The compact group $G$ and the discret group $P o(A) \quad \cap i \mathbb{R}$ are dual in the sense of locally compact Abelian groups.
(c) Let (G,k) be a solenoidal compact group and let $N_{*}=L^{I}(G)$. Then the induced lattice semigroup $T=(\kappa(t))_{t \geq 0}$ fulfils the assertions of Theorem l. 10 . For example, if $G$ is the dual of $\mathbb{R}_{\mathrm{a}}$, then $\operatorname{Po}(A) \quad \cap \mathrm{i} R=\mathrm{i} R$. Since the fixed space of $k(t)$ is given by

\[
F i x(k(t))=\left(\operatorname{span} \cup k \in T \operatorname{ker}\left(\frac{2 \pi i k}{t}-A\right)\right)^{--}
\]

no $T(t) \in T$ is irrecucible.
(d) If $T$ is the irreducible semigroup of schwarz type on the predual of $B(H)$ given in [Evans (I977)] then Po(A) $\cap$ i $\mathbb{R}=\varnothing$.