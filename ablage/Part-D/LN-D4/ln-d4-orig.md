## 1. STABITITY OF POSITIVE SEMIGROUPS

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

1. uniformly exponentially stable, if $\|T(t)\|^{i} \leq \mathrm{Me}^{-\mathrm{w} t}$ for some $\mathrm{w}^{\mathrm{m}}$ $M>0$ and all $t \geqslant 0$.
2. uniformly stable, if in $_{t \rightarrow \infty} T(t)=0$ in the strong operator topology.
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

## 2. STABILITY OF IMPLEMENTED SEMIGROUPS

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
![](https://cdn.mathpix.com/cropped/2025_01_15_a2cb5878cfb251465958g-07.jpg?height=87&width=1600&top_left_y=2332&top_left_x=222) in $M$ and yields a projection onto Fix(T) .

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

Proposition 3.3. Let $T$ be an identity preserving semigroup of Schwarz type on the predual of $a w^{*-a l g b r a} M$. Then the following assertions are equivalent:
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
![](https://cdn.mathpix.com/cropped/2025_01_15_a2cb5878cfb251465958g-13.jpg?height=52&width=1597&top_left_y=679&top_left_x=224) $\psi_{\Gamma_{1}} \epsilon_{M_{*}}$ such that $A \psi_{\eta_{0}}=\eta \psi_{\eta_{\eta}}$, then for all $x \epsilon_{M}$ :

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

## Therefore

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
![](https://cdn.mathpix.com/cropped/2025_01_15_a2cb5878cfb251465958g-15.jpg?height=47&width=1591&top_left_y=910&top_left_x=227) on $M$ and $\Phi$ a faithful family of T-invariant normal states. We call ( $M, \Phi, T$ ) irreducible, if the preadjoint semigroup is irreducible (alternatively, if the fixed space of $t$ is one dimensional).

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
![](https://cdn.mathpix.com/cropped/2025_01_15_a2cb5878cfb251465958g-17.jpg?height=53&width=1594&top_left_y=1204&top_left_x=228) infinite dimensional. Therefore $P o(A) \cap$ in $:\{0\}$ as desired.

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

Since the projections $s\left(\hat{\psi}_{n}\right)$ are mutually orthogonal, there exists a real sequence $\left(r_{n}\right), 0<r_{n}<1,1 i m_{n} r_{n}=0$ and $\hat{\phi}\left(s\left(\psi_{n}\right)\right) \leq \frac{1}{2} r_{n}$. For all $n \in \mathbb{N}$ choose $z_{n} \in\left(\hat{M}_{\hat{p}}^{\hat{\prime}}{ }_{1}{ }^{+}\right.$such that

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
(a) If $\phi$ is a $\sigma\left(M^{\prime}, M\right)$-accumulation point of $\left(\phi_{k}\right)$, then $\phi \in F i x\left(R^{1}\right)$. Since Fix( $\left.{ }^{r}\right)$ is finite dimensional, the set of accumulation points of the sequence $\left(\phi_{k}\right)$ is metrizable in the $o\left(M^{\prime}, M\right)-$ topology. Hence there exists a sequence (k(n)) of natural numbers, such that $\sigma\left(M^{\prime}, M\right)-1 i m_{n} \phi_{k}(n)=\phi$. Consequent $l_{Y} \quad \phi=\sigma\left(M^{\prime}, M^{\prime \prime}\right)-1 i m_{n}$ $\phi_{k}(n)$ by Remark (I) above. But this leads to a contradiction, which proves (a).
(b) Since dim $F i x(R)=d i m f i x\left(R^{\prime}\right)=\operatorname{rank}(P)<\infty$, (b) follows from (a).
(c) Suppose that the fixed space of $R^{\prime}$ is infinite dimensional. Since $F i x\left(R^{r}\right)=M_{*}$ there exists a sequence of states ( $\psi_{n}$ ) in Fix(R') with mutually orthogonal support projections in $M$ (Lerma 4.1). Since every o(M', M) -accumulation point of the $\psi_{n}{ }^{\prime} s$ belongs to Fix (R') , hence is normal, the sequence ( $\psi_{n}$ ) is relatively o ( $\left.\mathrm{M}_{*}, \mathrm{M}\right)$-compact. BY Eberleins theorem, we may assume that this sequence is weakly convergent. By the orthogonality of the $s\left(\psi_{n}\right)^{\prime} s$ this sequence converges to zero in the $s^{*}\left(M_{*} M_{*}\right)$-topology, hence $\lim _{n} \psi_{k}\left(s\left(\psi_{n}\right)\right)=0$ uniformly in $k \in \mathbb{N}$, a contradiction. Consequently dim Fix(R) $<\infty$ and (c) is proved.
(d) We prove dim Fix(R') = 1 and apply (a) once again. Useful for this is the following observation : If $\psi$ is a faithful state on M then the normal part is faithful too. Indeed, if $0 \neq x \in M$ such that $\psi^{(n)}(x)=0$ choose a projection $0 \neq p \in M$ such that $\psi^{(n)}(p)=$ $\psi^{(s)}(p)=0$ (use [Takesaki (1979), Theorem III.3.8]), hence $\psi(p)=0$ which conflicts with the faithfulness of $\psi$.

If $2 \leq \operatorname{dim} F i x\left(R^{\prime}\right)$ there are states $\psi_{1}$ and $\psi_{2}$ in $F i x\left(R^{\prime}\right)$ such that the corresponding support projections are orthogonal in M'' (Remark 4.2). Since every $R^{\prime}$-invariant state $\psi$ is faithful on $M$, $\psi_{i}(n) \neq 0$ (otherwise the norm closed face $\left\{\psi(x)=0: X_{i} M_{+}\right\}$would
be non trivial and $\mu R(\mu)$-invariant). The support projections of the $\psi_{i}^{(n)}{ }^{(n}$ in $M^{\prime \prime}$ are orthogonal (since $\psi_{i}^{(n)} \leqq \psi_{i}$ ) and different from zero. Let $\left(z_{Y}\right)$ be a net in $M_{I}{ }^{+}$such that

$$
\sigma\left(M^{\prime}, M^{\prime}\right)-1 \mathrm{in}_{Y} z_{\gamma}=s\left(\psi_{I}^{(n)}\right)
$$

Then $\lim _{Y} \psi_{1}^{(n)}\left(z_{\gamma}\right)=1$ whereas $\lim _{\gamma} \psi_{2}^{(n)}\left(z_{\gamma}\right)=0$. Let $z_{(n)}$ be a o ( $M, M_{*}$ )-accumulation point of $\left(z_{\gamma}\right){ }_{\gamma}{ }^{i n} M_{+}$. Since every $\psi_{i}(n)$ is
![](https://cdn.mathpix.com/cropped/2025_01_15_a2cb5878cfb251465958g-25.jpg?height=87&width=1597&top_left_y=713&top_left_x=224) implies $z \neq 0$ whereas the second shows that $\psi_{2}(n)$ cannot be faithful. Since this is a contradiction, it follows dim Fix (R') $=1$ which proves (d).

The next corollary is an easy application of Theorem 4.4 and of D-III, Proposition 2. 3.

Corollary 4.5. Let $T$ be an identity preserving semigroup of Schwarz type on the predual of a $W^{*-a l g e b r a} M$. Then the following assertions are equivalent:
(a) $T$ is uniformly ergodic with finite dimensional fixed space.
(b) The adjoint weak*-semigroup is strongly ergodic with finite dimensional fixed space.
(c) Every Tri-invariant state is normal.

Proof. If (a) is fulfilled then the semigroup $T$ is strongly ergodic on $M_{*}$. Since

$$
\operatorname{dim} F i x(T)=\operatorname{dim} F i x\left(T^{\prime}\right)<\infty
$$

there exist normal states $\phi_{1} \ldots, \phi_{n}$ in $F i x(T)$ and $x_{1}, \ldots x_{k}$ in Fix( $\left.T^{\prime}\right)$ such that $\phi_{n}\left(x_{m}\right)=\delta_{n, m} \quad(1 \leq n, m \leqq k)$ and

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

Section 3. From the many papers dealing more or less explicitely with the asymptotic behavior of semigroups on operator algebras we quote Frigerio-Verri (1982) and Watanabe (1982). The background for our ergodic theorems (Prop. 3.3 and Prop. 3.4) can be found best in Krengel (1985). The "automatic" convergence theorem for an irreducible $W^{*}$-dynamical system on $B(H)$ stated in Corollary 3.9 is the continuous version of a result in Groh (1984c). Finally, the characterization of convergence towards a periodic semigroup through spectral properties of the generator (Thm. 3.11) is due to Nagel (1984) in the commutative, i.e. L ( $\mu$ ), case (see also G-IV, Thm.2.14).

Section 4. Again we refer to Krengel (1985) for the (uniform) ergodic theory for a single operator or a one-parameter semfgroup on a Banach space. The characterization given in Corollary 4.5 for positive semigroups on W*-algebras is based on a sophisticated use of ultrapower techniques and has its discrete forerunners in Lotz (1981) and Groh (1984b).

