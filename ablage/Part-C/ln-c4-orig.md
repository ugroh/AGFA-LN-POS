## A S Y MPTOTICS

OF POSITIVE SEMIGROUPS

ON BANACH UATTICES

In this chapter we describe the long term behavior of positive semigroups and discuss some concrete examples in more detail.

The first section is devoted to the stability of positive semigroups, and we give sufficient and necessary conditions which ensure that the semigroup (and the solution of the abstract Cauchy problem, respectively) converges to zero as $t \rightarrow \infty$. It is shown that for positive semigroups stability is determined fairly well by spectral properties of the generator.

In the second section we describe conditions ensuring convergence of the sertigroup (as $t \rightarrow \infty$ ) to an equilibrium point or to a periodic solution. Again we are interested in spectral conditions ensuring such a behavior.

In the final section a series of examples is discussed in more detail. In particular we consider semigroups related to retarded equations and discuss existence of solutions, spectral properties and asymptotic behavior. Most of the examples are motivated by biological models.

# 1. STABILITY OF POSITIVE SEMIGROUPS ON BANACH LATTICES 

by<br>Ginther Greiner and Frank Neubrander

In Section 1 of $B$-IV we have seen that the growth bound of a positive semigroup on spaces $C_{o}(X)$ coincides with the spectral bound of the generator $A$, which is - for positive semigroups - an element of the spectrum of $A$. Now, using the results of $A-I I I, A-I V, B-I V, S e c .1$ and C-III, it can be shown that this is valid for positive semigroups on AM- , AL- and Hilbert spaces.

Theorem 1.1. Let $A$ be the generator of a positive semigroup (T(t)) ${ }_{t \geqslant 0}$ on a Banach lattice $E$ such that $s(A)>-\infty$. Each of the subsequent conditions implies

$$
s(A)=w_{I}(A)=\omega(A) \in \sigma(A)
$$

(a) Either $E$ is an $A M$-space or ari $L^{2}-s p a c e$ or an $L^{1}$-space.
(b) There exist $T>0, h \in E_{+}$such that $T(\tau) E \subset E_{h}$.
(c) There exist $x>0, \phi \in E_{+}^{\prime}$ such that $\left.\|T(\tau) f\| \leqslant<f\right\rangle$ for all $\pm \in E_{+}$.

Proof. We know that $s(A) \leqslant \omega_{1}(A) \leqq \omega(A)$ (see A-IV,Cor.I.5) and $s(A) \in g(A)$ (see C-III, Cor.l.4). Thus we have to show $s(A)=m(A)$. (a) For AM-spaces the proof given in section 1 of $B-I V$ works (cf. B-IV, Rem.1.5.) .
Since for positive semigroups we always have $\|R(\lambda, A)\| \leq\|R(R e \lambda, A)\|$ (Re $\lambda>s(A)$ ) (see $C-I I I, C o r . I .3)$ the assertion for $L^{2}$-spaces follows from A-III, Cor.7.10.
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-02.jpg?height=58&width=1358&top_left_y=2041&top_left_x=229)
(b) We identify $E_{h}$ according to the Kakutani-Krein Theorem with a space $C(K), K$ compact. Considering $T(t)$ as operator from $E$ into $c(K)$, we denote it by $T_{o}$. Then $T_{o}$ is positive hence continuous (see Schaefer (1974), II.Thm.5.3). Let $j: C(K) \cong E_{h} \rightarrow E$ be the canonical inclusion. The spectral radii of $T(T)=j \circ T_{o}$ and $T_{o}{ }^{\circ} j$ coincide and are given by $\rho:=\exp (\tau+4(A))$ - By the Krein-Rutman Theorem (cf. the Corollary to Thm. 2.6 in the Appendix of schaefer (I966) there exists $0<\mu \in C(K)^{r}$ such that ( $\left.\mathcal{P}_{\circ}{ }^{\circ}\right)^{*} \mu=\rho \cdot \mu$. Then $\phi:=T_{\circ}^{\prime} \mu$ is an eigenvector of $\left(j_{>} T_{\rho}\right)^{\prime}$ with eigenvalue $p$. Thus $p \in \operatorname{Ro}(T(T))$ and hence $s(A) \geqq \omega(A)$ by A-III,Thm,6,2.
(c) For $a>s(A), r>\tau, f \in E_{+}$we have
$\int_{0}^{r} e^{-\alpha s}\|T(s) f\| d s=\int_{0}^{\tau} e^{-\alpha s}\|T(s) f\|_{i}^{d} d x+e^{-\alpha \tau} \int_{0}^{r-\tau} e^{-\alpha s}\|T(\tau) T(s) f\| d s \leq$ $\leq \int_{0}^{T} e^{-\alpha s}\|T(s) f\| d s+e^{-a \tau} \int_{0}^{r-\tau} e^{-\alpha s}\langle T(s) f, \phi\rangle d s \leq$ $\leq \int_{0}^{T} e^{-\alpha S}\|T(s) f\| d s+\|R(a, A) f\|$
(the last inequality follows from C-riI, Thm.l.2). Now Datko ${ }^{\text { }} 5$ Theorem (A-IV,Thm.1.11) implies $\omega(A)<\alpha$

For $L^{P}$-spaces, $p \neq 1,2$, $\quad$, it is not known whether spectral- and growth bound of an arbitrary positive semigroup coincide. Using interpolation techniques and Thm.l.1 one can treat some special cases. Before doing this we have to recall some facts on interpolation. For details we refer to [Dunford-Schwartz (1958), VI.10] or [Reed-Simon (1975) , IK.4.3.

Let $(\mathrm{X}, \mathrm{\Sigma}, \mu)$ be a $\sigma$ finite measure space, $1 \leqq p<q<a$ and suppose that $T_{0}: L^{P(\mu)} \cap L^{q}(\mu)+L^{P}(\mu) \cap L^{q}(\mu) \quad$ is a Iinear operator which
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-03.jpg?height=75&width=1617&top_left_y=1270&top_left_x=205) $r \in[P, q], T_{0}$ has a (unique) continuous extension $T_{r}: L^{r}(\mu) \rightarrow L^{r}(\mu)$. Moreover ,
(1.1) $u \rightarrow \log \left\|_{1 / u}\right\|^{i}$ is a convex function on the interval $\left[\frac{1}{q^{\prime}}{\underset{p}{2}}^{-}\right.$.

Applying this result to the powers $T_{r}^{n} \quad(n \in N$ ) and using the fact that the pointwise limit of conver functions is convex, we obtain that the logarithm of the spectral radius is convex, i.e.,
(1.2) $u \rightarrow \log \left(r\left(T_{I / u}\right)\right)=\lim _{n \rightarrow \infty} \frac{1}{n} \log \left\|T_{1 / u}^{n}\right\|^{H}$ is convex on $\left[\frac{1}{q}, \frac{1}{p}\right]$.

In the following we suppose that for every $r \in[p, q]$ we have a strongly continuous semigroup $\left(T_{r}(t)\right)$ t $\geq 0$ on $L^{r}(\mu)$ such that

$$
\begin{equation*}
T_{r}(t)\left|L^{r} \cap L^{s}=T_{s}(t)\right| L^{r} \cap L^{s} \text { for all } r, s \in[p, q], t \geqq 0 \tag{1.3}
\end{equation*}
$$

Let $A_{r}$ be the generator of $\left(T_{r}(t)\right), \omega(r)$ its type and $s(r)$ the spectral bound of $A_{r}$. In this situation we have the following corollary of Thm.1.1.

Corollary 1.2. Suppose that the semigroups $\left(T_{r}(t)\right){ }_{t} \equiv 0$ are positive.
(a) In case $p<2<q$ and $w(r)$ independent of $r \in[p, q]$, one has $s(r)=\omega(r)$ for all $r \in[p, q]$.
(b) If $p=1, q \geq 2$ and $s(r)$ independent of $r \in[p, q]$ then $s(r)=w(r)$ for $r \in[1,2]$.

Proof. Once it is shown that both functions $u \rightarrow s(I / u)$ and $u+\omega(1 / u)$ are convex on $\left[\frac{1}{q}, \frac{1}{\mathrm{p}} \mathrm{c}\right.$, the assertion follows from Thm.I.l and the relation $s(r) s w(r)$ for every $r$. since $\omega(u)=$ $\log r\left(T_{u}(1)\right)(s e e A-I I I,(I .4)),(1.2)$ implies that $u \rightarrow \omega(1 / u)$ is a convex function. By C-III,Thm. 1.1 we have $r\left(R\left(k, A_{u}\right)\right)=(k-s(u))^{-1}$ for $k \in \mathbb{N}$ sufficiently large. The assumption (1.3) implies that
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-04.jpg?height=70&width=1620&top_left_y=616&top_left_x=229) with Re $\lambda$ large enough. Hence by (I. 2 ) $u \rightarrow \log \left[r\left(R\left(k, A_{1 / u}\right)\right)\right.$ is a convex function for large $k \in \mathbb{N}$. We have $\log \left[\left(1-\frac{1}{k} s(1 / u)\right)^{-k} \underset{\sim}{f}=k \cdot \log k+k \cdot \log [k-s(1 / u)]^{-1}=\right.$ $=k \cdot \log k+k \cdot \log \left[r\left(R\left(k, A_{I} / u_{0}\right)\right]^{-1}\right.$,
ons $u \rightarrow \log \left[\left(I-\frac{1}{s}(1 / u)\right)^{-1}\right]$,
hence all the functions $u \rightarrow \log \left[\left(1-\frac{1}{k}(1 / u)\right)^{-k}\right], k \in \mathbb{k}$, are convex. It follows that $u+s(1 / u)=1 \lim _{k \rightarrow \infty}\left(\log \left[\left(1-\frac{1}{k} s(1 / u)\right)^{-k}\right)\right)$ is convex as well.

One can apply the corollary to schrödinger operators on the spaces $L^{P}\left(\mathbb{R}^{n}\right)$, i.e., operators $A=\Delta+V$ where $A$ is the Laplacian and $V$ is a multiplication operator, see simon (1982) for details. In Thm. B.5.I (1.c.) it is shown that for certain potentials $V$ the type is independent of $p \in[I, \infty)$. Thus the assumptions of (a) are satisfied. Part (b) can be applied if $q>2$ and if $A_{1}$ has compact resolvent. Then all operators $A_{r}, 1 \leqq r<q$ have compact resolvent and therefore their spectra coincide. In particular, $s\left(A_{r}\right)$ is independent of $r \in[1, q]$.

As shown in $A-T V, E x .1 .2(2)$, the equality $s(A)=\omega(A)$ may not hold for positive semigroups on arbitrary Banach lattices. However, the knowledge of $s(A)$ is still sufficient to determine the growth bound ${ }^{4}$ (A) of the strong solutions of the abstract Cauchy problem. In fact, combining Theorems 1.1 and 1.2 of $C-I I I$ with Theorem 1.4 of A-IV we obtain the following fundamental result for the stability of positive semigroups.

Theorem l.3. Let $A$ be the generator of a positive semigroup $(T(t))_{t \geq 0}$ on a Banach 1attice. Then $s(A)=\omega_{1}(A) \in \sigma(A)$.

Recalling the definition of $\omega_{1}(A)$ (see $A-I V, D e f . I .1$ ) and the fact that $s(A)$ is always an element of $\sigma(A)$, we can reformulate the statement of Thm.1.3 as follows.

Corollary 1.4. Let (T't)) $t \geq 0$ be a positive semigroup on a (real or complex) Banach lattice with generator $A$. Each of the following conditions implies that the solutions of the abstract Cauchy problem are exponentially stable, i.e., there is $\delta>0$ such that $\lim _{t \rightarrow \infty} e^{\delta t} T(t) f=0$ for every $f \in D(A)$.
(a) $\lambda-A$ is invertible for every $\lambda \geqq 0$;
(b) $A$ is invertible and $A^{-1} \leqq 0$.

Proof. In case of a real Banach lattice we consider the complexification (see sec. 7 of $\mathrm{C}-\mathrm{I}$ ). Note that both, the hypotheses and the satement remain preserved.
Since $s(A) \in \sigma(A)$ assertion (a) implies s(A) \& 0 . If (b) is satisfied then $R(0, A) \geq 0$, hence $s(A)<0$ by C-III,Thm. $1,1(b)$. It follows from Thm. 1.3 that $\sup \{\omega(f): f \in D(A)\}={ }_{t}(A)<0$.

In the following we give a spectral characterization of stability for eventually norm-continuous positive semigroups. An important tool in the proof is the following result on power bounded operators due to Katznelson-Tzafriri (1984):

Let $R$ be a linear operator on a Banach space
(1.4) such that $\sup _{n \in \mathbb{N}} \| R_{\|}^{n}<\infty$. Then one has

$$
\sigma(R) \cap \Gamma \subseteq\{I\} \text { if and only if } \lim _{n \rightarrow \infty}\left\|R^{n}-R^{n+1}\right\|=0
$$

Theorem 1.5. Let $(T(t)) t \geqslant 0$ be a positive semigroup on a Banach lattice $E$ which is bounded and eventually norm-continuous. The following two assertions are equivalent:
(i) ( $\mathrm{T}(\mathrm{t}))_{\mathrm{t} \geqq 0}$ is uniform1y stable;
(ii) $0 \notin \operatorname{Rg}(A) \quad\left(i . e ., \operatorname{ker} A^{\prime}=\{0\}\right)$.

In case $E$ is reflexive (i) and (ii) are equivalent to
(iiii) 0 ( $P_{G}(A)(i, e ., \operatorname{ker} A=\{0\})$.

Proof. (i) $\rightarrow$ (ii) was proven in $A-I V, T h m .1 .12$ in a more general setting.
(ii) $\rightarrow$ (i) In case $u(A)<0$ one trivially has (i). Therefore we can assume $\omega(A)=0$. By Cor. 2.13 and Prop. 2.9 of $C-I I I$ we have $\sigma(A) \cap i R=\{0\}$, Since the spectral mapping theorem holds (cf. Thm. 6.6
and Thm. 6.3 of $A-I I I$ ) we have

```
(1.5) a(T(1)) \capI = {1} and I F Re(T(1)).
```

From (1.4) it follows that $\lim _{n \rightarrow \infty}\|T(n)-P(n+1)\|_{i}=0$ and therefore $\operatorname{Iim}_{t \rightarrow \infty}\|T(t)-T(t+1)\|=0$. Thus given $g \in \operatorname{im}(I d-T(1))$ then $g=f-T(1) f$ for some $f \in F$ hence $\|T(t) g\|=\|(T(t)-T(t+1)) f\|_{i}^{i} \leq$ $H(T(t)=T(t+1))\left\|\|f\|^{\prime} \rightarrow 0\right.$. The second assertion of (1.5) ensures that im(Id - T(1)) is dense in E. Since the semigroup is bounded we have $\lim _{t \rightarrow \infty}\|T(t) f\|=0 \quad$ for every $f \in \overline{\operatorname{Lm}(I d-T(1))}=E$, i.e., (T(t)) is uniformly stable.
(i) $\rightarrow$ (ifí) is always true and follows from $A-I V, T h m .1 .13$.
(iii) - (ii) : The adjoint semigroup (T(t)') $t \geqq 0$ is eventually norm-continuous and bounded and we have $\mathbb{R o}^{\left(A^{\prime}\right)}=\operatorname{Po}\left(A^{\prime \prime}\right)=\operatorname{Po}(A)$. Thus the implication "(ii) $+(i)^{\prime \prime}$ can be applied and we obtain that (T(t) ${ }^{\prime}$ ( $\geq 0$ is stable. Then $A-I V, T h m .1 .13$ yields $0 \& P_{C}\left(A^{\prime}\right)=R o(A)$.

As an application of Thm. 1.5 we consider the Japlacian as generator on $L^{p}\left(R^{n}\right), 1 \leqq p<\infty,($ see $A-I, 2.8)$. For $P=I$ the constant functions are eigenvectors of the adjoint operator, hence $0 \in R G(\Delta)$. Thus the semigroup is not stable on $L^{1}\left(\mathbb{R}^{n}\right)$. On the other hand, for $1 \leqq p<\infty$ there does not exist a non-zero function $h \in L^{P}\left(\mathbb{R}^{n}\right)$ with $\Delta h=0$. Hence $A$ generates a stable semigroup on $L^{p}\left(\mathbb{R}^{n}\right)$ for $1<p<\infty$.
(That ker $B=\{0\}$ can be deduced from the following two facts:

- since the semigroup consists of contractions and since the norm is strictly monotone on $E_{+}$it follows that ker $A$ is a sublattice. Thus irreducibility of the semigroup (see A-I,2.8 and C-III,Fx. 3.4(a)) implies that dimker $A \leqq 1$;
- The semigroup commutes with the translations on $\mathbb{R}^{n}$, hence ker $A$ is invariant under translations.)

In the next results we give conditions on the range of the generator which ensure stability. We begin with a generalization of cor.l. 4 (b) *

Propositon 1.6. Let A be the generator of a positive semigroup on a (real or complex) Banach lattice, $D(A)$ : $\left.=-\operatorname{l}(A) \cap E_{+}\right)$.
Then $\omega_{1}(A)<0$ if and only if $\left.F_{+} \leq i m A(D(A))^{\prime}\right)$.

Proof. If ${ }^{\omega}(A)<0$ then $s(A)<0$ (A-IV, Cor.1.5), hence $\overline{A^{-1}}=-R(0, A) \leqslant 0$ by $C-I I I, T h m .1 . I$.
If $F_{+} \subset$ im $A\left(D(A){ }_{-}\right)$, then, for every $f \in E_{+}$, there exists $g \in D(A)+$ such that $A g=-f$. We have $0 \leq T(t) g=g+\int_{0}^{t} T(s) A g d s$
$=g-\int_{0}^{t} T(s) f d s$, hence $0 \leqq \int_{0}^{t} T(s) f d s \leq g$ for every $t \geq 0$. For $a>0$ we have $\int_{0}^{t} e^{-\alpha s} T(s) f d s \leqq \int_{0}^{t} T(s) f$ ds $\leqq f$. Using C-III,Thm. 1.2 we conclude that $P(a, A) f \leq g$ for $a>\max \{0, s(A)\}$. By the Uniform Boundedness Principle we know that $\{R(a, A)$ : $\alpha>\operatorname{man}\{0, s(A)\}\}$ is uniformly bounded. Since $t_{1}(A)=s(A) \in \sigma(A)$ (see Thm.1.3) it follows that $\omega_{1}(A)<0$.

Next we show that weak uniform stability implies uniform stability provided that $E$ is weakly sequentially complete (see C-I, Sec.5) and (im $A)_{+}:=A(D(A)) \quad E_{+}$is a total subset of $E$. The left translations on $L^{2}\left(\mathbb{R}_{+}\right)$are stable. Hence, by A-IV, Rem. 1.17 (a), im $A=\left\{f \in L^{2}\left(R_{+}\right): \int_{0}^{\infty} f(x)\right.$ da exists\} and we see that (im $\left.A\right)+$ is a total subset of $L^{2}\left(R_{+}\right)$. On the other hand, (im $\left.A\right)_{+}=\{0\}$ for the generator of the non stable, but weakly stable semigroup of left translations on $L^{2}(\mathbb{i})$.

Proposition 1.7. Let $A$ be the generator of a positive semigroup $(T(t))_{t \geqslant 0}$ on a weakly sequentially complete Banach lattice $E$, such that (im $A)+$ is total in $E$. Then $(T(t))_{t \geq 0}$ is uniformly stable if and only if it is weakly uniformly stable.

Proof. If (T(t)) teo is weakly uniformiy stable, then (T(t)) is bounded by the Uniform Boundedness Principle. Using the weak version of $A-I V, T h m . \operatorname{In} 4, \int_{0}^{\infty}\langle T(t) f, \phi\rangle d t$ exists for every $f \in(i m A)+$ and $\phi \in E_{+}^{*}$. It follows that the net $\left(\int_{0}^{r} T(t) f d t\right)_{r \geq 0}$ is weakly cauchy Hence $\quad \sigma\left(F^{\prime}, E\right)-1 m_{r \rightarrow \infty} \int_{0}^{r} T(t) f d t$ exists for every $f \in(i m A)+$ Since the net is monotone one obtains convergence in norm by Dini's Theorem [Schaefer (1974), II.Thm.5.9]. Now uniform stability follows from A-IV, Thm. 1.16.

In A-IV,Thm. 1.13 we have seen that a generator $A$ of a stable semigroup satisfies necessarily $s(A) \leq 0$, Re $\lambda<0$ for all
$\lambda \in \operatorname{Po}(A) \quad \mathrm{L} \sigma(\mathrm{A}) \quad$ and, by $\lambda R(\lambda, A) f=R(\lambda, A) A f+f$, that $\lim _{\lambda \rightarrow 0+} R(\lambda, A) g$ exists for all $g \in \operatorname{Im} A$. For positive semigroups similar properties are even sufficient for stability.

Lemma 1.8. Let $A$ be the generator of a positive semigroup (T(t)) tıo on a Banach lattice $F$ with $s(A) \leq 0$. Given $f \in E_{+}$then $\lim _{\lambda \rightarrow 0+} R(\lambda, A) f$ exists if and only if $l_{\text {int }} t_{\rightarrow \infty} \int_{0}^{t} T(s) f d s$ exists.

Proof. In view of C-III,Thm. 1.2 we have for $\phi \in \mathrm{E}_{+}^{\prime}$ : $\left.\lim _{\mathrm{t} \rightarrow \infty}<\int_{0}^{\mathrm{t}} \mathrm{T}(\mathrm{s}) \mathrm{f} \mathrm{ds}, \phi\right\rangle=\mathrm{sup}_{\mathrm{t}>0} \int_{0}^{\mathrm{t}}<\mathrm{T}(\mathrm{s}) \mathrm{f}, \phi>\mathrm{d} s=$ $=s u P_{t>0} s u P_{\lambda>0} \int_{0}^{t} e^{-\lambda s}\langle T(s) f, \phi\rangle d s=s u P_{\lambda>0} s u P_{t>0} \int_{0}^{t} e^{-\lambda s}\langle T(s) f, \phi\rangle d s=$
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-08.jpg?height=61&width=992&top_left_y=449&top_left_x=229)
Thus either both limits exist with respect to o(玉臤)-topology or none. Since both nets are monotonically increasing, the assertion follows from Dini's Theorem (see Schaefer (1974), II.Thm.5.9).

Proposition I.9. Let $A$ be the generator of a positive, bounded semigroup (T(t)) ${ }_{t \geq 0}$ on a Banach lattice $E$. If there is a subset $D=E_{+}$which is total in $E$ such that $\lim _{\lambda \rightarrow 0+} R(\lambda, A) f$ exists for every $f \in D$, then $(T(t))_{t \leq 0}$ is uniformly stable.

Proof. By Lemma $1.8 \quad \int_{0}^{\infty} T(t) f$ dt exists for every f in the Iinear hull of $D$. But $D$ is total, (T(t)) $t \geqslant 0$ is bounded and hence, by A-IV, Thm. 1.16 , uniformly stable.

Remark 1.10. If $A$ is the generator of a positive semigroup, then for every $n \in \mathbb{N}, D\left(A^{n}\right)+$ and $D_{+}^{\infty}=\left(n_{n=0}^{\infty} D\left(A^{n}\right)\right)_{+}$are total subsets of $F$. This follows from $f \in D\left(A^{n}\right), f=R(\lambda, A)^{n} g=R(\lambda, A)^{n}\left(g_{1}-g_{2}\right)$ $=f_{1}-f_{2}$ where $f_{1}, f_{2} \in D\left(A^{n}\right)_{+}$and Thm. 1.43 in Davies (1980).

In the rest of this section we discuss the long term behavior of the solutions of the inhomogeneous equation

$$
\begin{equation*}
\dot{u}(t)=A u(t)+F(t), u(0)=u_{0} \in D(A) \tag{1,6}
\end{equation*}
$$

where the forcing term $F(t)$ converges to some $f_{0} \in F$ as $t+\infty$. In case that $A$ generates a positive semigroup the assumption $r^{4}(A)<0^{\prime}$, which is needed to prove the next proposition for arbitrary generators (see [pazy (1983), Thm.4.4.4]), can be replaced by the 'stability' of the semigroup. We recall that some important generators as, for example, the Laplacian on $L^{P}\left(\mathbb{R}^{n}\right), 1<p<\infty$, generate positive, stable semigroups which are not uniformly exponentially stable. Therefore, the weakening of the assumptions on $A$ mentioned above $*$ i.e., replacing $\quad$ w $(A)<0^{\prime}$ by ${ }^{\prime}$ positive and stable' widens the class of equations (1.6) for which the following stability result is applicable. For additional results of this kind see Neubrander (1985b).

Proposition 1.Il. Let $A$ be the generator of a positive, stable semigroup ( $T(t)$ ) $t \geq 0$ on a Banach lattice $E$. Let $F(\cdot)$ be a locally integrable function from $\mathbb{R}_{+}$into $\mathbb{F}$. If there are $G(\cdot) \in \mathcal{C}_{\mathrm{O}}\left(\mathbb{F}_{+}, \mathbb{R}_{+}\right)$, $f_{0} \in \operatorname{im} A$ and $g_{o} \in \operatorname{im} A_{+}$such that $\left|F(s)-f_{o}\right| \leqq G(s) g_{0}$ for every $s \geqq 0$, then every mild solution u(*) of (1.6) converges as $t \rightarrow \infty$ and $\operatorname{Iim}_{t \rightarrow \infty} u(t)=-h$ where $h \in D(A)$ with $A h=-f_{0}$.

Proof. Recall that every solution of (1.6) satisfies

$$
\begin{equation*}
u(t)=T(t) f+\int_{0}^{t} T(t-s) f_{0} d s+\int_{0}^{t} T(t-s)\left(F(s)-f_{o}\right) d s \tag{1.7}
\end{equation*}
$$

By the stability of the semigroup and $f \in D(A)$, the first term converges to zero as $t+\infty$. since $f_{0} \in$ im $A$, the second term converges to $h:=\int_{0}^{\infty} T(s) f_{0} d s \in$ im $A(A-I V, T h m .1 .16)$ and $A h=-f_{0}$. Define $H(s):=F(s)-f_{O}=H_{+}(s)-H_{-}(s)$. We have to show that $\int_{0}^{t} T(t-s) H_{\dot{L}}(s) d s \rightarrow 0$ as $t \rightarrow \infty$. Again, the assumption $g_{0} \in$ im $A$ is equivalent to the existence of $\int_{0}^{\infty} T(t) g_{0}$ dt . Choose
(i) a constant $M$ such that

$$
0 \leq H_{ \pm}(s) \leqq H_{+}(s)+H_{-}(s)=\mid H(s)!\subseteq(s) g_{0} \leq M g_{0}
$$

(ii) a constant $t^{\prime}$ such that $\left\|\int_{t}^{a r}, T(s) g_{O} d s\right\| \leqq e /(2 M)$ and $G(s) \leqq c / 2\left\|\int_{0}^{\infty} T(s) g_{0} d s\right\|$ for every $s \geqq t^{1}$.
Then, for $t>2 t^{\prime}$,
$0 \leqq \int_{0}^{t} T(t) H_{ \pm}(s) d s \leq \int_{0}^{t} T(t) G(s) g_{0} d s$
$=\int_{0}^{t \prime} T(t) G(s) g_{0} d s+\int_{t}^{t} T(t) G(s) g_{0} d s$
$s M \int_{t-t^{1}}^{t} T(t) g_{0} d s+c / 2\left\|\int_{0}^{\infty} T(t) g_{0} d s\right\|^{-1} \int_{0}^{t-t^{\prime}} T(t) g_{0} d s$
$\leqq M \int_{t}^{\infty} T(t) g_{0} d s+c / 2\left\|\int_{0}^{\infty} T(t) g_{0} d s\right\|_{1}^{-1} \int_{0}^{\infty} T(t) g_{0} d s$.
Hence $\left\|\int_{0}^{t} T(t) H_{\dot{\Sigma}}(s) d s\right\| \leqq t$ for every $t>2 t^{\prime}$.

We conclude with a result similar to the previous proposition. Instead of uniform stability we now require $s(A)<0$ while the assumption on the forcing term is weaker than in Prop.1.11.

Proposition 1.12 . Let $(T(t))_{t \geqslant 0}$ be a positive semigroup with $s(A)<0$. Assume that the forcing term $F$ has values in $D(A)$, that it is continuous with respect to the graph norm and that $f_{o}:=\left\|_{A}\right\|^{-1 i m_{t \rightarrow \infty}} F(t)$ exists.
Then for every solution $u(\cdot)$ of (1.6) we have limt $u(t)=-A^{-1} f_{o}$.
(Note, that the assumptions imply that (1.6) has a unique strong solution, see [Pazy (1983), Thm.4.2.4].)

Proof. The solution of (I.6) is given by
$(I .8) u(t)=T(t) u_{0}+\int_{0}^{t} T(s) f_{0} d s+\int_{0}^{t} T(s)\left(F(t-s)-f_{0}\right) d s$
The first term tends to zero by Cor.1.4. The second term tends to $R(0, A) f_{O}=-A^{-I} f_{O}$ by C-III,Thm.1.2. By assumption we have $1 i_{s+\infty}\left\|A\left(F(s)-f_{0}\right)\right\|=0$ and from Thm. 1.3 and $A-I V,(1.3)$ we deduce that $\|T(s) R(0, A)\| M e^{-c s}$ for $s \geqq 0$ and suitable constants $M \geq I$, $\varepsilon>0$. Thus for the third term we have

$$
\begin{aligned}
\left\|\int_{0}^{t} T(s)\left(F(t-s)-f_{0}\right) d s\right\| & \leqslant \int_{0}^{t} \int_{0}^{t} T(s) R(0, A)\left\|_{1}^{1}\right\| A\left(F(t-s)-f_{0}\right) \|_{i} d s= \\
& =\int_{0}^{t / 2} \cdots d s+\int_{t / 2}^{t} \cdots d s .
\end{aligned}
$$

The first integral can be estimated by
$\sup \left\{\left\|A\left(F(s)-f_{o}\right)\right\| ; s \in\left[\frac{t}{\lambda}, t\right]\right\} \cdot \int_{0}^{\infty} M+e^{-c s}$ ds while the second integral
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-10.jpg?height=67&width=1478&top_left_y=1029&top_left_x=229)
It follows that the third term in (I. 8 ) tencs to zero.

## 2. CONVERGENCE OF POSITIVE SEMIGROUPS <br> by <br> Günther Greiner and Rainer Nagel

The considerations in this section are motivated by the following guideline:

The asymptotic behavior of a strongly continuous semigroup (T(t)) $t \geqslant 0$ is determined by the (structure, location of the) spectrum $\sigma(A)$ of the generator $A$.

Unfortunately this principle does not hold in general, e.g., there are semigroups with spectral bound less than zero and growth bound greater than zero (see A-III, Ex. $1.3 \& 1.4$ ). In order to prove results in the above direction we have to assume additional hypotheses on the senigroup. Positivity may serve to this purpose. For example, the norm convergence to zero, i.e. $\lim _{t \rightarrow \infty}\|T(t)\|=0$, for a positive semigroup on certain Banach lattices is characterized by the condition $s(A)<0$ (see Thm.I.I). Thus in this case the location of the spectrum determines the norm convergence of the semigroup.
Here we concentrate on the case $s(A)=0$. At first we observe that
$\lim _{t \rightarrow \infty} T(t)$ - if it exists in some operator topology - is always a projection $P$ onto the fixed space of (T(t)) $\underset{t}{ } \geq 0$ which coincides with the kernel of $A$. In case $P=0$ we have stability which was discussed in Sec. 1 . In this section we mainly consider the case $s(A)=0 \in P_{G}(A)$ and show that the symmetric structure of the boundary spectrum of the generator of a positive semigroup yields interesting results.

We begin our discussion by considering quasi-compact semigroups. Using the general results presented in Sec. 2 of B-IV and the spectral theoretical result of chapter C-III we obtain the following.

Theorem 2.1. Let (T(t)) $t_{t} 0$ be a positive semigroup on a Banach lattice $E$ which is bounded, quosi-compact and has spectral bound zero. Then there exists a positive projection $p$ of finite rank and suitable constants $\delta>0, M \geqslant 1$ such that

```
(2.1) |T(t)-P|}\leqqM\cdot\mp@subsup{\textrm{E}}{}{-\deltat}\quad\mathrm{ for alI t 2 0.
```

Proof. By Thra. 2.9 of B-IV the set $\{\lambda \in q(A): \operatorname{Re} \lambda=0\}$ is finite and by Thm. 2.10 of $C-I I I$ imaginary additively cyclic. Thus it contains only the value $s(A)=0$. Then by $B-I V,(2,5)$ we have

$$
T(t)=\sum_{j=0}^{k-1} \frac{I}{j 1} \cdot t^{j} A_{o}^{j} P+R(t) \quad(t \geq 0)
$$

where $P$ is the residue of $R(., A)$ at $0, k$ is the pole order and $\| R(t) \leq M * e^{-\delta t}$ for suitable constants $\delta>0, M \geqslant 1$. Since we assumed that $(T(t)){ }_{t \geq 0}$ is bounded, the pole order $k$ has to be 1 .

Before discussing a concrete trample we formulate some remarks related to Theorem 2.1.

Remarks 2.2. (a) If one has a positive semigroup $T=(T(t))_{t \geq 0}$ satisfying $\omega_{\text {ess }}(T)<m(T)$ then the rescaled semigroup with $\tilde{T}(t):=\exp (-\omega(T)) T(t) \quad$ is quasi-compact and has spectral bound zero. In order to apply Theorem 2.I we still need the boundedness of (T̃(t)) ${ }_{t \geqslant 0}$ (see the following remarks).
(b) Without assuming boundedness of the semproup one can conclude that $T(t)-\sum_{j=0}^{k-1} \frac{1}{j}!\cdot t^{j_{A}}{ }_{o P}$ tends to zero exponentially.
(c) In the proof of Theorem 2.1 we saw that a quasi-compact semigroup of positive operators having spectral bound zero is bounded if and only if the pole order at zero is one. This is automatically true
whenever there exists a fined vector which is a quasi-interior point of $E_{+}$. Indeed, if $k$ is the order of the pole at $s(A)=0$ then we have $0 \neq A^{k-1} P=1 i m \lambda \rightarrow 0 \quad \lambda^{k}(\lambda, A)$. Thus $A^{k-1} P$ is a positive operator. Assuming $k>I$ and denoting the quasi-interior fixed vector by $u$ we have $A u=0$ hence $A^{k-1} P u=P A A_{u}=1$. Since $A^{k-1} P$ is positive it vanishes on the principal ideal generated by $u$. since this ideal is dense we obtain $A^{k-1} P=0$ which is a contradiction.
(d) $\quad$ f $T=(T(t))_{t \geqq 0}$ is an irreducible semigroup with $\left.s!A\right)=0$, then quasi-compactness implies boundedness of $T$ (This follows from (c) and C-III, Prop.3.5). Moreover, in this case the projection $P$ has the form $P=$ фفh where $u$ is a quasi-interior point of $F_{+}$and $\phi$ is a strictly positive linear form on $F$. This also is a consequence of © CII , Prop. 3.5 .
(e) If $T=(T(t)) \quad t \geq 0$ is irreducible and eventually compact then the rescaled semigroup (exp (-w (T)t)T(t)) satisfies the assumptions of Thm.2.1. Indeed, by C-III, Thm.3.7 we know that m(T) $>-\infty$, while ${ }^{\omega}{ }^{\text {ess }}(T)=-\infty$. It follows that the rescaled semigroup is quasi-compact hence (d) is applicable.

The following example has a biological background, and the semigroup considered describes the time evolution of an age-structured population. For more details we refer to Greiner (1984a) or Webb (1984).

Example 2.3. On the Banach lattice $E=L^{I}([0, \infty))$ we consider the operator A defined by

$$
\begin{aligned}
& \text { Af }:=-f^{\prime}-\mu f \text { with domain } \\
&(2.2) \quad D(A):=\left\{f \in E: f \text { absolutely continuous, } f^{\prime} \in f,\right. \\
&\left.f(0)=\int_{0}^{\infty} \&(a) f(a) \text { da }\right\},
\end{aligned}
$$

Here we assume that $\mu$ and $\beta$ are positive, measurable, bounded functions on $[0, \infty)$, One can show that $A$ generates a strongly continuous semigroup $T$ of positive operators. Assuming that $\mu(\infty):=\lim _{a \rightarrow \infty} \mu(a)$ exists we obtain ${ }_{j} \operatorname{ess}^{(T)}=-\mu(m)$, We suppose in addition that $\beta$ and $\mu$ satisfy
(2.3) $\quad \int_{0}^{\infty} \beta(a)\left(\exp \left(-\int_{0}^{a} \mu(x) d x\right)\right) d a=1$ and $\mu(\infty)>0$.

The function $h$ with $h(a):=\exp \left(-\int_{0}^{a} \mu(s) d s\right) \quad i s$ differentiable, $h \in f$ and $h^{\prime}=-\mu h$. Moreover, (2.3) implies $\int_{0}^{\infty} \beta(a) h(a) d a=1=$ $h(0)$. Thus $h \in D(A)$ and $A h=0$. It follows that $s(A)=0$. Indeed, since $s(A)$ is a pole of the resolvent there exists a positive eigenvector $w$ of $A^{\prime}$ corresponding to $s(A)$. Since $h$ is
strictly positive we have $\langle h, w\rangle>0$ hence $s(A)\langle h, w\rangle=\langle h, A\rangle w\rangle=$ $\langle A h, W\rangle=0$ which implies $s(A)=0$.
Consequently the semigroup generated by $A$ satisfies ali the assumptions of Thm.2.1 provided that $\mu$ and $\beta$ satisfy (2.3) (The boundedness of the semigroup follows from Rem. 2.2 (c)). It is not difficult to see that (up to a constant) $h$ is the unique eigenfunction of $A$ corresponding to 0 . Thus the projection $P$ has the form $P=v e h$ for a suitable positive $v \in L^{\infty}([0, \infty))$.

For more general generators of the type (2.2) we refer to C-IV, Section 3.

Clearly, quasi-compactness was essential in the above example as well as in Thm.2.l. For spaces $C_{o}(X)$ we proved in B-IV,Thm. 2.12 that Doeblin's condition is sufficient for quasi-compactness. Actually this is true in $L^{P}$-spaces with $1<p<\infty$ as well. We quote the result from Lotz (1986).

Proposition 2.4. Let ( $T(t))_{t}$ ( 0 be a bounded positive semigroup on $E=L^{P}(\mu), 1<p<\infty$.
Assume that there exist $t_{0} \neq 0, \phi \in E_{+}^{1}, b<1$ such that
(2.4) $\left\|T\left(t_{0}\right) f\right\| \leqq\langle f, \phi\rangle+b\left\|_{i} f\right\|$ for all $f \geqq 0$.

Then $(T(t))_{t \geqslant 0}$ is quasi-compact.

In the following result we replace quasi-compactness by eventual norm-continuity of the semigroup.

Theorem 2.5. Let $T=(T(t))_{t \geq 0}$ be a bounded, eventually normcontinuous positive semigroup with gererator $A$ on a reflexive Banach Iattice $E$. Then $P f:=\lim _{t \rightarrow \infty} T(t) f$ exists for every $f \in \mathbb{E}$. $P$ is a positive projection onto the fixed space Fix (T) $=$ ker $A$.

Proof. In view of Thm. 1.5 it suffices to consider the case
$s(A)=0 \in \operatorname{PG}(A)$, We define $F:=\left\{f \in E: \lim _{t \rightarrow \infty} T(t) f\right.$ exists $\}$. $F$ is closed since $(T(t))_{t \geqslant 0}$ is bounded and obviously ker $A \subset F$. Since $G(A)$ AiR is cyclic and bounded (see C-III,Thm. 2.10 and $A-I I, T h m .1 .20$ resp. $)$ we have $G(A)$ iin $=\{0\}$. Since the spectral mapping theorem holds (cf. A-III,Thm.6.6) we conclude $\sigma(T(t)) \cap \Gamma=\{1\}$ for all $t \geqslant 0$. Then (1.4) implies $\operatorname{Iim}_{n \rightarrow \infty}\|T(n)-T(n+1)\|=0$ hence $\lim _{t \rightarrow \infty}\|T(t)-T(t+1)\|=0$. Take $f=g-T(1) g$. Then $\|T(t) f\|=$
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-13.jpg?height=70&width=1615&top_left_y=2555&top_left_x=206) Thus
(2.5) $\quad \lim _{t \rightarrow \infty} T(t) f=0$ for every $f \in \operatorname{im}(I d-T(I))$.

That is, im(Id $-T(1))=F$. Since ker $A=f_{t \geqslant 0} \operatorname{ker}(I d-T(t))=$ ker(Id - T(1)) (cf. A-III, Cor. 6.4 ) we have
im(Id - T(1)) $+\operatorname{ker}(I d-T(1)) \subset F$.
since power bounded operators on a reflexive Banach space are mean ergodic (e.g., see Krenge1 (1985), Chap. 2,Thm. I. 2) we obtain that im (Id - $T(1)$ ) + ker (Id $-T(1)$ is dense in $E$, hence $F=E$.

Strong convergence of the semigroup $T=(T(t))_{t \geqslant 0}$ implies strong convergence of the Césaromeans $C(t) f:=\frac{1}{t} \cdot \int_{0}^{t} T(s) f d s, f \in E$ which (by definition) is mean ergodicity of the semigroup $T$ (see Davies (1980), Chap.5.1). On the other hand an inspection of the proof of Thm. 2.5 shows that reflexivity of the underlying space can be replaced by the assumption that $T$ is a mean ergodic semigroup.
This remark also shows where to look for examples of semigroups not converging as $t \rightarrow \infty$ : Consider the positive contraction $R$ defined by (Rf)(x) $:=f(x+I)$ on $\left.E=L^{l}(f)\right)$. Then $T(t):=e^{t(R-I d)}$ defines a positive norm-continuous semigroup on $F$. Since $\operatorname{ker}(R-I d)=F i x R=\{0\}$ but $\|T(t) f\|=e^{-t} \sum_{n=0}^{\infty}\left\|R^{n} f\right\| t^{n} / n!=\|f\|>0$ for every $0<f \in E$ we see that $\lim _{t \rightarrow \infty} T(t)$ does not exist for the strong operator topology.
Finally we remark that in Thm.2.5 'eventual norm-continuity' is crucial as well. This can be seen by considering the translation (semi-) groups on $L^{P}(R)$.

In the next few results we study semigroups which are not necessarily eventually normmontinuous, but restrict our attention to positive
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-14.jpg?height=52&width=1620&top_left_y=1916&top_left_x=224) following '0-2 law' which we quote from Greiner (1982), Thm. 3.7.

If (X, $\Sigma, \mu)$ is a measure space and (T(t)) tzo is a positive semigroup on $L^{P}(\mu)$ then we call a subset $C \in \Sigma$ (T(t))-invariant if the principal ideal generated by the characteristic function ${ }^{I_{C}}$ is (T(t))-invariant in the usual sense.

Theoren 2.6. Let (T(t)) te 0 be a positive contraction semigroup on $L^{P}(\mu), 1 \leqslant P<\infty$, and assume that there exists a strictly positive fixed function $e \in \operatorname{ker} A$. Then the following holds:
(a) For every $\tau>0$ there exists a disjoint decomposition $x=X_{o} \downharpoonleft X_{2}$ into $(T(t))$-invariant measurable subsets such that
(0) $\quad|T(t)-T(t+r)| e_{0}+0$ for $e_{0}=e=l_{X_{0}} a s t \rightarrow \infty$,
(2) $\mid T(t)-T(t+\tau)!e_{2}=2 e_{2}$ for $e_{2}=e \cdot l_{X_{2}}$ and all $t \geqslant 0$.
(b) In case the semigroup is irreducible then for every $\tau ; 0$ one has the alternative
(0) $\quad|T(t)-T(t+T)| e+0$ as $t \rightarrow \infty$ or
(2) $|T(t)-T(t+\tau)| e=2 e$ for all $t$ 亿 0 .

This '0-2 law' can be used in order to obtain results on convergence of positive semigroups.

Coro1lary 2.7. Assume that (in addition to the assumptions made in Thm. 2, 6) $P G(A) \cap i \mathbb{R}=\{0\}$, If we decompose $X=X_{o} U_{2} X_{2}$ for some $\tau>0$ according to assertion (a), then $1 i_{t \rightarrow \infty} T(t) f$ exists for every $f \in L^{P}(\mu)$ vanishing $u-a . e . o n X_{2}$.

Proof. From $T(t) e_{j} T(t) e=e$ we obtain $T(t) e_{j} \leqslant e_{j}$ since $X_{0}$ and $X_{2}$ are (T(t))-inveriant. Then $T(t) e_{0}+T(t) e_{2}=T(t) e=e$ implies $T(t) e_{j}=e_{j}(j \neq 0,2)$. Thus we can assume $X=X_{o}, e=e_{o}$. Given $g \in L^{P}(\mu)$ such that $\mid g i \leqq e$ we have $|T(t)(I d-T(T)) g| \leqq|T(t)-T(t+T)| e+0$ for $t \rightarrow \infty$. Since $\left\{g \in L^{P}(\mu):|g| \leq e\right\}$ is a total subset of $玉$ (e is strictly positive) and ( $T(t))_{t \geq 0}$ is bounded we conclude
(2.6) $\lim _{t \rightarrow \infty} T(t) f=0$ for every $f \in \overline{i m(I d-T(T))}$.
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-15.jpg?height=58&width=1612&top_left_y=1756&top_left_x=202) A-III, Cor. 6.4), hence we have convergence on ker (Id -T(t)). Since $T(\tau)$ is a contraction on a reflexive Banach space we have
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-15.jpg?height=64&width=1600&top_left_y=1921&top_left_x=202) finally proves the convergence on the whole space.

Typical examples for which Thm. 2.6 and Cor. 2.7 can be applied occur in the theory of stochastic processes (see also B-IV, Ex. 2.6). We briefly describe this situation and remind that in this context the sets $X_{o}$ and $X_{2}$ have a probabilistic meaning (see Greiner-Nagel (1982) or the supplement in Krengel (1985)).

Example 2.8. Let $X$ be a set and $\Sigma$ be a qulgebra of subsets of $X$. We consider a Markov transition function $\left(P_{t}\right)_{t} \neq 0$ on ( $\mathrm{X}, \Sigma$ ), i.e. each $P_{t}$ is a real-valued function on $X \times \Sigma$ such that
$(2.7 a) P_{t}(x, \ldots)$ is a probability measure for $x \in X, t>0 ;$
$(2.7 b) P_{t}(, C)$ is a measurable function for $C \in \Sigma, t>0 ;$
$(2.7 c) P_{t+s}(x, C)=\int_{K} P_{s}(y, C) P_{t}(x, d y)$ for all $S, t>0, x \in K, C \in \Sigma$ We assume that ( $\mathrm{P}_{\mathrm{t}}$ ) possesses an invariant probability measure $u$, i.e. we assume
$(2.7 d) \mu(C)=\int P_{t}(x, C) d_{\mu}(x)$ for every $C \in \Sigma$.
Finally we assume that the following continuity condition holds true.
(2.7e) For every $C \in \Sigma$ one has $\operatorname{Iim}_{t \rightarrow 0} P_{t}(x, C)=I_{C}(x) \quad \mu-a . e$. .

Given $h \in L^{1}(\mu)$ we define a measure $P_{t} h$ on $\Sigma$ by
$P_{t} h(C):=\int P_{t}(x, C) h(x) d_{\mu}(x)$. In case $\mu(C)=0$ then by (2.7d) $P_{t}(x, C)=0$, -a.e. on $x$ hence $P_{t} h(c)=0$. That is, $P_{t} h$ is absolutely continuous with respect to $\mu$. By the Radon-Nikodym theorem $P_{t} h$ has an integrable density with respect to $\mu$. We define $T(t) h$ to be this density (which is unique as an element of $I^{I}(\mu)$ ). Thus for $h \in L^{l}(\mu), C \in \Gamma$ we have
(2.8) $\int_{C}^{(T(t) h)(x)} d_{\mu}(x)=\int P_{t}(x, C) h(x) d_{\mu}(x)$ for all C $\in \Sigma$.

It is not difficult to see that $T(t)$ is a positive linear contraction on $L^{1}(\mu)$. We have $T(t), l_{X}=I_{X}$ and $T(t) 1_{X}=l_{X}$ for all $t \geqq 0$ and $T(t) T(s)=T(t+s)$ for $t, s \geqq 0$. This follows from (2.7a) , (2.7d) and (2.7c) respectively. Moreover (2.7e) implies strong continuity of the semigroup $(T(t))_{t \geq 0}$. In fact by Prop.1.23 of Davies (1980) we only have to show weak continuity at $t=0$. Since the characteristic functions are total in $L^{\circ "}(\mu)$ this is true provided that $\lim _{t \rightarrow 0}\left\langle T(t) h, l_{C}=\left\langle h, l_{C}\right\rangle\right.$ for $h \in L^{I}(\mu), C \in E$. Given $h\left(L^{1}(\mu)\right.$, then by (2.7e) $\lim _{t \rightarrow 0} P_{t}(x, C) h(x)=l_{C}(x) h(x)$ $\mu$-a.e. By Lebesgue's Theorem $\left\langle T(t) h, l_{C}\right\rangle=\int P_{t}(x, C) h(x) d \mu(x)$ tends to $\int l_{C}(x) h(x) d_{\mu}(x)=\left\langle h_{r} 1_{C}\right\rangle a s \quad t \rightarrow 0$ and we have weak hence strong continuity.
Therefore a Markov transition function satisfying all the assumptions of (2.7) induces a strongly continuous semigroup on $L^{l}(\mu)$, and by interpolation on $L^{P}(\mu)$, which satisfies the hypotheses of Thm. 2.6.

In the following corollaries of Thm. 2.6 we give criteria which ensure convergence on the whole space. In view of cor. 2.7 it is enough to show $X_{2}=\emptyset$.

Corollary 2.9 . Let $(T(t))_{t z 0}$ be a positive semigroup of contractions on the Banach lattice $L^{I}(\mu)$ and assume that there exists a strictiy positive eigenfunction e $\in$ ker $A$.

If (T(t)) $t \geqq 0$ is eventually norm-continuous then lim $_{t \rightarrow \infty} T(t) f$ exists for every f $f L^{l}(\mu)$.

Proof. Since the semigroup is positive and eventually norm-continuous its boundary spectrum is cyciic and bounded, i.e. we have $\operatorname{Pq}(A) \cap i \sharp=\{0\}$. Moreover there exist $t_{0}>0$ and $\tau>0$ such that $\left\|I\left(t_{o}\right)-T\left(t_{o}+\tau\right)\right\|<I$.
For bounded linear operators $s \in L\left(L^{l}\right)$ one has $\left\|_{\|} s=\right\|_{i}|j|$ IV, Thm. 1.5 of Schaefer ( 1974 ) hence $\left\|\left|T\left(t_{o}\right)-T\left(t_{0}+T\right)\right| f\right\|<\|f\|$ for every $f \in L^{1}(\mu), f \neq 0$. This shows that condition (2) of Thm.2.6(a) can be true only when $e_{2}=0$, i.e., $x_{2}=\varnothing$.

Corollary 2.10. Let $(T(t))_{t \geq 0}$ be an irreducible semigroup on $L^{P}(\mu)$ satisfying the assumptions of Thm. 2.6 .
If $P o(A) f i \mathbb{R}=\{0\}$ and if there exist $0 \leq r<s$, such that inf(T $(r), T(s)\}>0$ then there exists a strictly positive function $h \in L^{q}(\mu)\left\{D^{-I}+q^{-I}=I\right\}$ such that $\lim _{t \rightarrow \infty} T(t) f=\langle f, h\rangle e$ for every $f \in L^{P}(\mu)$.

Proof. Since inf\{T(r),T(s)\}>0 we have (inf\{T(r),T(s)\})e>0 for the strictly positive fixed vector e . Since the regular operators on $L^{P}(\mu)$ form a vector Iattice it follows by [schaefer (1974), II. 1.4 , Formula (5) \& (5') $]$ that $|T(r)-T(s)| e=T(r) e+T(s) e-$ $2(\inf \{T(r), T(s)\})<2 e \quad$ consequently the first alternative of Thm. 2. $6(b)$ holds true with $\tau:=s-r$. Equivalently, we have $X_{2}=\emptyset$ and by Cor.2.7 Pf:= limt $T \rightarrow(t) f$ exists for every $f \in L^{P}(\mu)$. The limit $P$ is a positive projection, satisfying $P T(t)=T(t) P=P$ for all $t \geqq 0$. It follows that im $P \subset$ ker $A$ and im $P^{\prime}-$ ker $A^{\prime}$. Since $P \neq 0 \quad(P e=e)$ we conclude that ker $A^{r}$ contains positive elements. Now C-III, Prop. $3.5(a)-(c)$ implies that $P$ has the form $P=h$ ee for a strictly positive function $h \in L^{q}(\mu)=\left(L^{P}(\mu)\right)^{\prime}$.

In a last corollary we consider the case where one operator $T\left(t_{0}\right)$ is a kernel operator, $i, e ., T\left(t_{o}\right)$ is induced by a $\mu$ \& measurable kernel on $\mathrm{X} \times \mathrm{X}$. The corollary is of particular interest for semigroups on spaces $\ell^{p}, 1 \leqq p<m$, where every positive operator is a kernel operator. For a precise definition and fundamental properties of kerne1 operators we refer to sec.IV.9 of Schaefer (1974) or Chap. 13 of Zaanen (1983). In particular we recall that the restriction of a kernel operator to a sublattice is again a kernel operator and that
the identity on $L^{P}(\mu), I \leqslant p<\infty$, is a kernel operator if and only if the measure space $(X, L, \mu)$ is purely atomic, i.e. $L^{P}(\mu)=\& \frac{P}{I}$ for some index set $I$. Moreover, from Axmann (1980) we quote the following result (see Satz 3.5 1.c.):
(2.9) If $T$ is an irreducible kernel operator then inf\{ $\left.T^{n}, T^{m}\right\}>0$ for some $n, m \in \mathbb{N}, \mathrm{n} \neq \mathrm{m}$.

Corollary 2.Il. Let $T=(T(t)) t \geq 0$ be a semigroup on $L^{P}(\mu)$ satisfying the assumptions of $T h m .2 .6$ and assume that one operator $T\left(t_{o}\right)$ is a kernel operator. Then $1 \lim _{t \rightarrow \infty} T(t) f$ exists for every $f \in L^{P}(\mu)$.

Proof. First we note that ker $A=F i x(T)$ is a sublattice of $L^{P}(\mu)$, hence is itself an $L^{P}$-space. Since $T\left(t_{o}\right) \mid k e r A=I d$ we conclude that ker $A \cong{ }_{2} \underset{I}{P}$. Thus $L^{P}(\mu)$ contains an orthogonal system $\left\{e_{j} \in\right.$ ker $A:$ $j \in I\}$ of atoms such that $\sup _{j \in \mathcal{E}_{j}}=$ e. The closed principal ideal. ${ }^{5}$ j generated by $e_{j}$ in $L^{P}(\mu)$ is (T(t))-invariant and the restriction of $(T(t))_{t \geqslant 0}$ to this ideal yields an irreducible semigroup $\left(T_{j}(t)\right)_{t \geqslant 0}$ having generator $A_{j}$. From $C-I I I, C o r .3 .9$ we conciude that
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-18.jpg?height=70&width=1623&top_left_y=1330&top_left_x=219) operator hence by (2.9) all the assumptions of Cor.2.Io are satisfied. Thus we have convergence on the the principal ideal $E_{j}$. Since the semigroup is bounded and the union of these ideals is total in $L^{P}(\mu)$ we have convergence on the whole space.

In all the results obtained so far we had to show or to assume that $P \sigma(A) \cap i f=\{0\}$. This is not surprising since for an eigenvector $g \in E$ corresponding to $i a \neq 0, \alpha \in \mathbb{H}$, we have $T(t) g=e^{i^{i} t} g$ and limt $t \rightarrow \infty$ (t)g does not exist. Nevertheless in some cases with $\operatorname{Po}(A)$ Oif $\neq\{0\}$ one can describe the asymptotic behavior of ( $T(t)$ ) $t \geqslant 0$ for large $t$. Instead of convergence to an equilibrium point one obtains that $T(t) f$ 'converges to a periodic function'.

To that purpose we consider a bounded, irreducible semjgroup $T=$ (T(t)) t\&0 of positive operators on some Banach lattice $E$ having order continuous norm. Under the assumption that the spectral bound $s(A)=0$ is a pole of the resolvent we can apply Theorem 3.12 of Chapter C-III. In particular, if 0 is not the only point in the boundary spectrum o(A) niP we obtain that

$$
o(A) \cap i \mathbb{P}=\operatorname{Po}(A) \cap i \mathbb{R}=\text { iar for some } 0<\alpha \in \mathbb{R} .
$$

Therefore the assumptions of $C$-III, Thm. 3.8 are satisfied and formula C-III, (3.13) implies
(2.10) $\rho(A)=\rho(A)+i \alpha \mathbb{Z}$ and $\|R(\lambda, A)\|=\|R(\lambda+i \alpha k, A)\|$
for $x \in \rho(A), k \in \mathbb{Z}$.
Since 0 was supposed to be a pole of the resolvent we can decompose

$$
\sigma(\mathrm{A})=\sigma_{1} \cup \sigma_{2},
$$

where $\sigma_{I}=1 a \mathbb{Z}, 0<\alpha \in \mathbb{R}$, and $\left.\operatorname{suptRe\lambda }: \lambda \in \sigma_{2}\right\}<0$. Moreover, for small $c>0,\|R(-\varepsilon+i \lambda, A)\|$ is uniformly bounded for $\lambda \in R$. Next, we construct a spectral decomposition of $F$ and $T$ corresponding to ${ }^{\sigma}{ }_{I}$ and $\sigma_{2}$ (compare A-III, Sec.3).
since 0 is an eigenvalue of $A$ it follows that $T$ has a quasiinterior fized point $h \in F_{+}$(use C-III, Prop.3.5(a)). Hence, $\{T(t) f: t \geqq 0\}$ is contained in the weakly compact (see $C-I, S e c .5)$ order interval $[-h, h]$ whenever $|f| \leqq h$. Since $h$ is a quasiinterior point and $T$ is bounded it follows that $T$ is relatively compact for the weak operator topology on $L(F)$. Therefore the Jacobs-DeLeeuw-Glicksberg Splitting Theorem (see Krengel (1985), Chap.2,Thm.4.4 and 4.5 ) can be applied to (the weak closure of) $T$ and we obtain a projection $Q \in L(E)$ onto the closed subspace $E_{1}$ generated by the eigenvectors $h_{k}$ of $A$ corresponding to the eigenvalues $i \alpha k, k \in \mathbb{Z}$. Clearly, $Q$ splits the semigroup $T$ into the restricted semigroups $T_{1}$ on $E_{1}:=0 \mathrm{QE}$ and $T_{2}$ on $E_{2}:=$ ker $Q$. We first describe $T_{I}$ in more detail.
The projection $Q$ is positive as an element of the weak closure of $T$ and even strictly positive by the irreducibilitiy of $T$. Its range $E_{I}$ is a closed sublattice of $E$ (use Schaefer (1974), Prop.III.Il.5) on which the semigroup $\dagger_{l}$ is periodic, irreducible and positive. In fact, $T(2 w / \alpha) f=f$ for every $f=h_{k}, k \in \mathbf{Z}$, and hence for every $f \in E_{1}$, while irreducibility and positivity are inherited from $T$. It now follows from A-III, Lemma 5.2 that the generator $A_{1}={ }^{A_{1}}{ }_{1}$ of $T_{1}$ has spectrum $\sigma\left(A_{1}\right)=i \alpha \mathbb{Z}$. Moreover in view of $A-I I$, Prop. 5.2 and Cor.5.3(ii) we have $\sigma\left(\mathrm{A}_{2}\right)=\sigma(\mathrm{A}) \backslash i \alpha \mathbb{Z}$. Therefore the decomposition $E=E_{I} \oplus E_{2}$ is a spectral decomposition corresponding to ${ }^{\sigma}{ }_{1}$ and $\sigma_{2}$. This proves the first part of the following lemma.

Lenma 2.12. Under the above assumptions there exists a positive projection $Q$ with range $E_{1}:=Q E$ and kernel $F_{2}:=Q^{-1}(0)$ such that the following holds:
(a) $F=F_{1} \oplus F_{2}, T=T_{1} \oplus T_{2}$ and $A=A_{1} \oplus A_{2}$ is a spectral decomposition corresponding to the decomposition $\sigma(A)=\sigma_{1} \quad \int_{2}$ where $\sigma_{1}=\sigma\left(A_{1}\right)=i \alpha \mathbf{Z}$ and $\sigma_{2}=\sigma\left(A_{2}\right)=\sigma(A) \backslash i \alpha \mathbf{I}$.
(b) $s\left(A_{2}\right)<0$ and $\left\|R\left(\lambda, A_{2}\right)\right\|$ is uniformly bounded in each semiplane $\left\{\lambda \in \mathbb{C}, \operatorname{Re\lambda }>\mathrm{s}\left(\mathrm{A}_{2}\right)+c\right\}$ with $\leq>0$.
(c) ${ }^{F}{ }_{I}$ is a closed sublattice of $E$ and $T_{1}$ is a periodic, irreducible, positive semigroup on $F_{I}$. In particular, ( $E_{1}, T_{1}$ ) is isomorphic to $\left(L, R_{T}(t)\right)$ where $L$ is a function lattice between $C(F)$ and $L^{1}(\Gamma)$ and $R_{\tau}(t)$ is the rotation group with period $\tau=2 \pi / a$.

Proof. (a) has been derived above while (b) follows immedately from (2.10). The properties of $T_{1}$ mentioned in (c) have been stated above. Hence the representation of $T_{1}$ as a rotation group follows from C-III,Cor.3.9.

For Hilbert spaces $L^{2}(\mu)$ property (b) of the above lemma and $A-I I I$, Cor.7. Il imply that the growth bound $\mathrm{m}_{\mathrm{l}}\left(\mathrm{A}_{2}\right)$ is less than zero. Therefore we obtain the following result on the asymptotic behavior of $T$.

Proposition 2.13. Let $T=(T(t)) t \geqslant 0$ be a bounded, irreducible, positive semigroup on a Hilbert lattice $F=L^{2}(\mu)$. Assume that $s(A)=0$ is a pole of the resolvent of the generator $A$ and that ia $\in \sigma(A)$ for some $0 \neq \alpha \in \mathbb{R}$. Then $T$ behaves asymptotically as the rotation group $\left(R_{\tau}(t)\right)_{t \geqslant 0}$ with period $\tau=2 \pi n / a$ for some $n \in \mathbb{N}$ on $L^{2}(F)$.

More precisely, we can identify $L^{2}(\Gamma)$ with a sublattice of $E$, which is the range of a strictly positive projection $Q$ and we find constants $\varepsilon>0$ and $M \geqq 1$ such that for every $f \in F$ we have (2.1I) $\left\|T(t) f-R_{\tau}(t) g\right\| \leqq M e^{-c t}\|f\|_{\|}^{\|}$for every $t \geqq 0$ where $g:=Q f$.

For $L^{P}$-spaces the analogous statement can be shown only for a weaker type of convergence. The proof of this result uses irterpolation for operators, mainly the Riesz Convexity Theorem (see the remarks preceding Cor.1.2).

Theorem 2.14. Let $T=(T(t))$ t $\quad$ be a bounded, irreducible positive semigroup on a Banach lattice $F=L^{P}(\mu), 1 \leqq p<\infty$. Assume that $s(A)=0$ is a pole of the resolvent of the generator $A$ and that ia $\in q(A)$ for some $0 \neq a \in \mathbb{R}$. Then $T$ behaves asymptotically as the rotation group $\left(R_{T}(t)\right)_{t \geqslant 0}$ with period $\tau>0$ on $L^{P}(\Gamma)$, i.e., we can identify $L^{P}(\Gamma)$ with a sublattice of $E$ such that for every $f \in \mathcal{F}$ there exists $g \in L^{P(\Gamma)}$ satisfying

$$
\begin{equation*}
\lim _{t \rightarrow \infty}\left\|T(t) f-\mathbb{R}_{\tau}(t) g\right\|_{\|}=0 \tag{2.12}
\end{equation*}
$$

Proof. We only consider $1 \leqq p<2$. The assertion for $p>2$ then follows by duality while $p=2$ was treated in Prop.2.13.
At first we observe that without loss of generality we may assume that $\mu$ is a probability measure and that $T(t) 1=1$ for every $t \geq 0$. In fact, the assumptions imply that $T(t) h=h$ for some $h \gg 0$, $\|h\|_{p}=I$. We consider the measure $v$ which has the density $h^{P}$ with respect to $\mu$. Then $v$ is a probability measure and $M: L^{P}(y) \rightarrow L^{P}(\mu)$; defined by Mh $:=h f$, is an isometric lattice isomorphism of $L^{P}(v)$ onto $L^{P}(\mu)$. The semigroup defined by $\tilde{T}(t):=M^{-1}(t) M$ possesses the $s a m e ~ p r o p e r t i e s ~ a s ~(T(t))$ and satisfies $\underset{T}{ }(t) I=1$ for $t \geq 0$.
Now the properties $T(t) 1=1, T(t) \geq 0$ imply that $I_{1}^{\infty}(\mu)$ is an invariant subspace for every operator $T(t)$ which is contractive with respect to the $L^{\infty}-n o r m$. The Riesz Convexity Theorem [Dunforg-schwartz (1958), VI.10.11] then implies that by restricting the semigroup (T(t)) to $L^{q}(\mu) \quad(p<q<\infty)$ we obtain a strongly continuous semi-
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-21.jpg?height=93&width=1617&top_left_y=1184&top_left_x=205) $t \geqq 0, q \geqq p$.
Let $A_{q}$ be the generator of $\left(T{ }_{q}(t)\right)$. In order to apply Prop.2.13 we have to show that 0 is a pole of the resolvent of $A_{2}$. Denoting the residue of $R(., A)$ at 0 by $P$ then $P=h o 1$ for a suitable $h \in\left(L^{P}(\mu)\right)^{\prime}$. Since $\left(L^{P}(\mu)\right)^{\prime} L^{2}\left(L^{2}(\mu)\right)^{\prime}, P$ can also be considered as bounded operator on $L^{2}(\mu)$. We denote it by $P_{2}$. From $A P=P A=0$ it follows that

$$
\begin{aligned}
& (R(1, A)(I d-P))^{n}=R(1, A)^{n}-P \quad(n \in \mathbb{N}) \text { and } \\
& \left(R\left(1, A_{2}\right)\left(I d-P_{2}\right)\right)^{n}=R\left(1, A_{2}\right)^{n}-P_{2} \quad(n \in \mathbb{N})
\end{aligned}
$$

The Riesz Convexity Theorem yields the following estimate for the operator norm:

$$
\begin{aligned}
\left\|R\left(1, A_{2}\right)^{n}-P_{2}\right\| & \leqq\left\|R(1, A)^{n}-P\right\|^{2 / P}\left\|_{R}(1, A)_{\infty}^{n}-P_{\infty}\right\|^{1-2 / P} \\
& \leqq\left\|_{R}(1, A)^{n}-P\right\|^{2 / P}\left(1+\left\|P_{\infty}\right\|^{1-2 / P}\right.
\end{aligned}
$$

Since 0 is a pole with residue $P$, the spectral radius of the operator $R(1, A)(1-P)$ is less than 1 . Thus for the right hand side of the inequality tends to 0 as $n \rightarrow \infty$. It follows that $r_{e s s}\left(R\left(I, A_{2}\right)\right)<1$, hence $I$ is a pole of the resolvent of $R\left(I, A_{2}\right)$, or equivalently, 0 is a pole of $R\left(., A_{2}\right)$ (see A-III, Prop. 2.5). Now we can apply Prop. 2.13 and obtain a projection $Q$ such that $\lim _{t \rightarrow \infty}\left\|T(t) f-R_{T}(t) \circ Q f\right\|_{2}=0$ for every $f \in L^{2}(\mu)$. on order intervals of $L^{\infty}(\mu)$ both, $L^{2}{ }^{2}$ and $L^{2}$-norm induce the same topology (see

Schaefer (1974), V.8.3), hence $\lim _{t \rightarrow \infty}\left\|T(t) f-R_{T}(t) \circ 0 f\right\|_{P}=0 \quad$ for every $f \in L^{\infty}(\mu)$. Since (T(t)) is bounded we finally obtain convergence in the $L^{P}$-norm for every $f \in L^{P}(\mu)$.

We give an example for the situation described in Thm. 2.14. The equation we consider describes the division of a cell population. For details we refer to Diekmann-Heijmans-Thieme (1984).

Example 2.15. Let $E=L^{I}\left(\left[\frac{1}{4}, 1\right], w d x\right)$, where the density $w$ is a continuous positive function on $\left[\frac{1}{4}, I \underline{T}\right.$, vanishes at $x=1$ and is strictly positive in $\left[\frac{1}{4}, 1\right)$.
We consider the operator $C=A+B$ where $A$ is defined by (Af) $(x):=-x f^{\prime}(x)$ on the domain $D(A):=\left\{f \in A C: f\left(\frac{1}{4}\right)=0\right\}$ and $B$ is defined by

$$
B f(x):=\left\{\begin{array}{cc}
k(x) f(2 x) & \text { if } x \leqq \frac{1}{2} \\
0 & \text { if } x>\frac{1}{2} .
\end{array}\right.
$$

Here $k$ is a positive continuous function on $\left[\frac{1}{4}, 1\right.$, satisfying (2.13) $k(x)>0$ for $\frac{1}{4}<x<\frac{1}{2}$ and $\int_{1 / 4}^{1 / 2} \frac{k(y)}{Y} d y=1$.

In the following we show that under these hypotheses and for suitable $w$ the semigroup generated by $C$ fulfills the assertions of Thm. 2.14. The operator A generates the nilpotent semigroup ( $\mathrm{T}(\mathrm{t})$ ) defined by

$$
(T(t) f)(x)=\left\{\begin{array}{cl}
f\left(e^{-t} x\right) & \text { if } e^{-t} x \geqq \frac{1}{4} \\
0 & \text { otherwise }
\end{array}\right.
$$

We have $(R(\lambda, A) f)(x)=x^{-\lambda} \int_{1 / 4}^{x} Y^{\lambda-1} f(y) d y\left(f \in F, x \in\left[\frac{1}{4}, 1\right]\right)$. It follows that $A$ has compact resolvent. since $B$ is bounded and positive , $C$ is the generator of a positive semigroup (s(t)) having compact resolvent as well. Using C-III,Prop. 3.3 one can show that (S(t)) is irreducible. Indeed, the non-trivial (T(t))-ideals are of the form $I_{g}=\left\{f \in E\right.$ : $f$ vanishes on $\left[\frac{1}{4}, s j\right\}$ with $s$ satisfying $\frac{1}{4}<s<1$. Since none of these ideals is invariant under $B$, the semigroup ( $S(t)$ ) is irreducible.
A suitable choice of the weight function $w$ ensures that ( $s(t)$ ) is bounded. Take
(2.14)

$$
w(x):= \begin{cases}\frac{1}{x} & \text { for } x \leq \frac{1}{2} \\ \frac{1}{x} \cdot\left\{I-\int_{1 / 4}^{x / 2} \frac{k(y)}{y} d y\right\} & \text { for } x \geq \frac{1}{2},\end{cases}
$$

Then integration by parts yields for $f \in D(A)=D(C)$
$\langle C f, 1\rangle=\left\{\begin{array}{l}1 / 2 \\ 1 / 4\end{array}\left(-x f^{\prime}(x)+k(x) f(2 x)\right) w(x) d x-\int_{I / 2}^{I} x^{\prime} f^{\prime}(x) w(x) d x=0\right.$.
Thus $\quad 1 \in D\left(C^{1}\right)$ and $C^{\prime} 1=0$, equivalently $S(t){ }^{\prime} 1=1$ for all $t$. This shows that (S(t)) is a semigroup of contractions on $F$.
It remains to show that there is $\alpha>0$ such that $i q \in u(C)$.
In fact, considering $\alpha:=2 \pi(\log 2)^{-1}$ then $i \alpha$ is an eigenvalue of $C$. A corresponding eigenfunction is given by $\quad h_{1}(x):=x^{-i a_{h}}(x)$, where $h_{o}$ is the eigenfunction corresponding to 0 defined as

$$
h_{o}(x):=\left\{\begin{array}{cc}
x / 4 \frac{k(y)}{y} d y & \text { for } \frac{1}{4} \leqq x \leq \frac{1}{2}  \tag{2.15}\\
1 & \text { for } \frac{1}{2} \leqq x \leqq 1
\end{array}\right.
$$

The verification of these statements is left as an escercise.

In several of the above results we had to assume that the positive semigroup $(T(t))_{t \geqslant 0}$ is bounded and has spectral bound zero. In general, these conditions are difficult to verify, in particular, when only the generator is known. In the final example we described a method how to cope with this problem: If $s(A)$ is an eigenvalue of the adjoint $A^{\prime}$ with a strictly positive eigenvector $\phi$, then $(T(t))_{t \geq 0}$ induces in a canonical way a positive semigroup $\left(T{ }_{\phi}(t)\right) t \notin 0$ on the AL-space ( $\mathrm{E}, \phi$ ). This semigroup satisfies $\left\|\mathrm{T}_{\phi}(\mathrm{t})\right\| \leq \exp (\mathrm{t} \cdot \mathrm{s}(\mathrm{A})$ ) and has spectral bound $s(A)$. Hence one may apply the results of this section to the rescaled semigroup (exp (-t.s(A))T $(t))$ t>0 thus obtaining convergence of $(T(t))_{t \geq 0}$ for the weaker topology on $F$ which is induced by $(E, \phi)$.

# 3. A SEMIGROUP APPROACH TO RETARDED ECUATIONS 

by
Annette Grabosch and Ulrich Moustakas

As indicated by the above title of this section there is a close relationship to B-IV, Section 3. First, the considered Cauchy problems are "similar" to (RCP). second, there again is a correspondence to a class of semigroups generated by the first derivative.

Instead of the differertial equation in (RCP) we will study equations of the form
(RE)

$$
u(t)=\Phi\left(u_{t}\right), t \geqslant 0
$$

$$
\mathrm{u}_{0}=\mathrm{g} .
$$

We use the following setting: Let $F$ be a Banach space, consider $E:=L^{1}([-1,0], F)$ and take $\Phi \in L(E, F)$. For $u \in L_{I o c}^{I}([-I, \infty), F)$ we denote by $u_{t} \in E$ the function given by $u_{t}(s):=u(t+s), t \geq 0$, $s \in[-1,0]$.

By a solution of (RE) with initial function $g \in E$ we understand a function $u \in L^{1} l_{\text {oc }}([-1, \infty)$, F) which satisfies equation (RE).
(RE) is called well-posed if for each $g \in f$ there exists exactly one solution.
Remarks. 1. The equation

$$
\begin{gathered}
\mathrm{u}(\mathrm{t})=\mathrm{Bu}(\mathrm{t})+\Phi\left(\mathrm{u}_{\mathrm{t}}\right), \mathrm{t} \geqq 0, \\
\mathrm{u}_{\mathrm{O}}=\mathrm{g},
\end{gathered}
$$

(where $B$ is the generator of a bounded semigroup on $F$ ) is in better analogy to the retarded Cauchy problem of $B-I V$, sec. 3 and seems to be more general than the one introduced above, but can be reduced to an equation of the type ( RF ). In fact, since $1 \in \rho(B)$ we have

$$
u(t)=R(I, B) \Phi\left(u_{t}\right)
$$

Clearly, this equation is of the previous type (with a different "delay functional").
2. The choice of "L"functions" Instead of "C-functions" (as in the case of (RCP)) enforces the solutions of (RE) to yield a strongly continuous semigroup of operators (on the space $E$ of fnitial functions) as in $B-I V$, section 3.

In order to solve ( $R F$ ) we consider the differential operator $A:=\frac{d}{d x}$ on $F=L^{1}([-1,0], F)$ with domain

$$
D(A):=\left\{f \in A C([-1,0], F): f^{\prime} \in 玉 \quad \text { and } f(0)=\Phi(f)\right\} .
$$

We claim that ( $A, D(A)$ ) generates a strongly continuous semigroup (T(t)) tz0 on $E$. To this end we first consider the operator $A_{o} f:=f^{\prime}$ with domain

$$
D\left(A_{0}\right):=\{f \in E: f \in A C([-1,0.7, F), f \in E \text { and } f(0)=0\}
$$

Similarly to the special case where $F=\mathbb{R}$ (compare A-I, Ex. 2.4 (ii) ) it can be seen that the operator $A_{o}$ generates a strongly continuous semigroup $\left(T_{o}(t)\right) t z 0$ given by

$$
\left(T_{0}(t) f\right)(s)=\left\{\begin{array}{cc}
f(t+s) & \text { if } t+s \leq 0  \tag{3.1}\\
0 & \text { if } t+s>0
\end{array}\right.
$$

Notice that $\left(T_{0}(t)\right)_{t \geq 0}$ is a nilpotent semigroup.
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-25.jpg?height=58&width=1617&top_left_y=1159&top_left_x=205) $\varepsilon_{\lambda}$ denotes the function $s \rightarrow e^{\lambda s}$ as an element of $L^{1}[-1,0]$ and
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-25.jpg?height=64&width=1620&top_left_y=1259&top_left_x=207) and $s \in[-1,0]$. clearly $\left\|_{E_{\lambda}}\right\|_{i}^{i}=1 / \lambda \cdot\left(1-e^{-\lambda}\right) \rightarrow 0$ as $\lambda \rightarrow \infty$ and we have $\left\|S_{\lambda}\right\|=\|E\|_{\lambda}\|\cdot\| \Phi\left\|_{i}=1 / \lambda \cdot\left(1-e^{-\lambda}\right) \cdot\right\| \Phi\|\leq 1 / \lambda \cdot\| \Phi \|_{\|}^{\|}$.
For every $\lambda>\|\Phi\|$, (Id $\left.\|_{\lambda}\right)$ is an isomorphism of $F$ and it is not difficult to see that it induces a bijection from $D(A)$ onto $D\left(A_{0}\right)$ such that
(3.2) $(\lambda-A)=\left(\lambda-A_{0}\right)\left(I d-S_{\lambda}\right)$.

Since $A_{o}$ generates a semigroup of contractions $\lambda-A_{o}$ is invertible for each $\lambda>0$. This yields the invertibility of $\lambda-A$ for each $\lambda \geqq\|\phi\|$.
In order to obtain an estimate on $\|\mathrm{i}(\lambda, A)\|$ we use Formula (3.2).
Since $\left\|R\left(1, S_{\lambda}\right)\right\|=\left\|\sum_{n=0}^{\infty} S_{\lambda}^{n}\right\| \leqq \sum_{n=0}^{\infty}\left\|_{i} \varepsilon_{\lambda}\right\|^{n} \cdot\|\Phi\|^{n}=\left(1-\left\|\varepsilon_{\lambda}\right\| \cdot\left\|_{i}\right\|^{-1}\right.$
and $\left\|R\left(\lambda, A_{o}\right)\right\| \leq 1 / \lambda$ for $\lambda>0$ we obtain for $\lambda \geqq\|\Phi\|$
$\|R(\lambda, A)\| \leqslant\left(1-\left\|c_{\lambda}\right\| \cdot\|\Phi\|\right)^{-1} \cdot 1 / \lambda=\left(\lambda-\lambda \cdot\left\|_{\lambda} \varepsilon_{\lambda}\right\|_{1}\|\Phi\|\right)^{-1}$

$$
=\left(\lambda-\left(1-e^{-\lambda}\right) \cdot\|\Phi\|\right)^{-1} \leqq\left(\lambda-\|\Phi\|^{-1}\right. \text {. }
$$

By using $A-I I$, Cor. 1.8 we thus have proved the first assertion of the following theorem:

Theorem 3.1. The operator $A$ defined above is the generator of a semigroup ( $\mathrm{T}(\mathrm{t}))_{\mathrm{t} \geq 0}$ on E .
For every $f \in E, t z 0$ we have for $a, e, s \in[-1,0]$

$$
(T(t) f)(s)=\left\{\begin{array}{lll}
f(t+s) & \text { if } t+s \leqq 0  \tag{3,3}\\
\Phi(T(t+s) f) & \text { if } t+s>0
\end{array}\right.
$$

Moreover, if $f \in D(A)$ then the translation property (T) (see B-IV, Thm.3.1) is satisfied.

Proof. Consider $E_{1}:=D(A)$ endowed with the graph norm and $A_{1}:=A$ restricted to $D\left(A_{1}\right):=D\left(A^{2}\right)$. By $(A-I, 3.5) \quad A_{1}$ generates the semigroup $\left(T(t) \mid D(A){ }^{\prime} t z 0^{\circ} \quad O n \quad E_{1}\right.$ point evaluation is a continuous mapping and therefore the translation property can be shown as in the proof of B-IV,Thm.3.1. Hence we obtain
(3.4) (T(t)f)(s)=\{ll $\begin{array}{ll}f(t+s) & \text { if } t+s \leq 0 \\ \Phi(T(t+s) f) & \text { if } t+s>0\end{array}= \begin{cases}f(t+s) & \text { if } t+s \leq 0 \\ (T(t+s) f)(0) & \text { if } t+s>0 ;\end{cases}$
i.e. (3.3) is valid for $f \in D(A)$. It remains to show (3.3) for all $f \in E . F i x \in \in \mathbb{R}_{+}$and $s \in[-t .0]$. For $t+s>0$ the equality follows immediately by the continuity of $\Phi$ from (3.4). For the case $t+s \leq 0$ we consider $g \in L^{\omega}[-1,0]$ with supp $g[5-1,-t]$. Comparing (3.1) and (3.4) we see that $\left\langle\left(T(t)-T_{0}(t)\right) f, g\right\rangle=0$ for all $f \in D(A)$, and hence for all $f \in E$.
Consequently $\left(T(t)-T_{o}(t)\right) f=0$ a.e. on $[-1,-t]$ which shows $(T(t) f)(s)=f(t+s)$ for a.e. $s \in[-1,-t]$.

The following corollary corresponds to B-TV,Cor.3.2 and assures the well-posedness of (RE) :

Corollary 3.2. For every $f \in E$ the function $u$ defined by

$$
u(t):= \begin{cases}f(t) & \text { if }-1 \leqq t \leq 0  \tag{3.5}\\ \Phi(T(t) f) & \text { if } t>0\end{cases}
$$

is the unique solution of (RE), in particular (RE) is well-posed. If $f \in D(A)$ then $u(t)=T(t) f(0)$ for $t>0$.

Proof. As in the proof of B-IV, Cor. 3.2 we have $u_{t}=T(t) f$ for $t \geqslant 0$ since $u_{t}(s)=u(t+s)=(T(t) f)(s)$ by the definition of $u$ and by formula (3.3). Thus $u(t)=\Phi(T(t) f)=\Phi\left(u_{t}\right)$ if $t \geqq 0$. Also by the definition of $u$ we have $u_{o}=f$. It remains to show uniqueness. Let $w$ be a solution of (RE) with initial function $w_{0}=0$. Then

$$
\begin{aligned}
& =\|\Phi\| \cdot \int_{-1}^{0}\|w(t+s)\|_{F} d s=\|\Phi\| \cdot \int_{t-1}^{t}\left\|_{i}^{\prime} w(s)\right\|_{F} d s \\
& \leq\|\Phi\|_{\|} \cdot \int_{-1}^{t}\|w(s)\|_{F} d s=\|\Phi\|_{\|} \cdot \int_{0}^{t} \quad \ddot{i}_{W}(s) \|_{F} d s \quad \text { for } \quad t \geqq 0 .
\end{aligned}
$$

By Gronwall's Iemma $\|w(t)\|_{F}=0$, thus $w(t)=0$.

Now we turn to the aspect of positivity in (RE). We assume F to be a Banach lattice and let $E$ inherit the canonical ordering from $F$ making it a Banach lattice. Additionally, let $\Phi$ be positive.
The first observation is that $A$ generates a positive semigroup. Indeed, it follows from equation (3.2) that $R(\lambda, A)=R\left(1, S, R\left(\lambda, A_{0}\right)\right.$ for $\lambda>\| \|_{i}$. since $s_{\lambda}$ is a positive operator we have $R\left(1, s_{\lambda}\right) \geqq 0$. The semigroup ( $\left.T_{o}(t)\right)_{t \geqslant 0}$ generated by $A_{o}$ is positive (use (3.1)), hence $R\left(\lambda, A_{o}\right) \geqq 0$. It follows that $R(\lambda, A) \& 0$ which is equivalent to the positivity of (T(t)) $t_{00}$ (see C-II, Prop.4.1).

Proposition 3.3. If $\Phi \in[(E, F) \quad i s$ a positive operator, then the solution semigroup ( $T(t))_{t \geqslant 0}$ corresponding to (RE) is positive.

For the following considerations concerning spectral poperties of the semigroup ( $T(t))_{t \geqslant 0}$ we always suppose $\Phi$ to be positive. Furthermore we define operators $\Phi_{\lambda} \in L(F), \lambda \in R$, by
(3.6) $\Phi_{\lambda} x:=\Phi\left(c_{\lambda} 8 x\right), x \in F$.

Evidently, each $\Phi_{\lambda}$ is a positive operator on $F$ and $\lambda \leq \mu$ implies $\Psi_{\lambda} \geqq \Psi_{k}$. From this relation it follows that the spectral bound $s\left(\Phi_{\lambda}\right)$ which coincides with the spectral radius $r\left({ }_{\lambda}\right)$ is a decreasing function in $\lambda$.

Furthermore, we shall need the following properties.

Lemma 3.4. The map $h * \mathbb{R} \rightarrow \mathbb{R}_{+}: \lambda \rightarrow s\left(\Phi{ }_{\lambda}\right)$ is continuous from the left. If $\Phi_{\lambda}$ is compact for all $\lambda \in \mathbb{R}$, then $h$ is continuous.

Proof. As indicated above, $h$ is decreasing. Hence continuity from the left follows from the upper semicontinuity of the spectrum (see [Kato (1976), Chap.IV,Thm.3.17).

Now take $\lambda \in \mathbb{R}$ with $s\left(\Phi_{\lambda}\right)>0 \quad\left(\right.$ if $s\left(\Phi_{\lambda}\right)=r\left(\Phi_{\lambda}\right)=0$, then continuity in $\lambda$ is trivial by the continuity from the left and the monotonicity). Since ${ }^{\Phi} \lambda$ is positive and bounded we know that
$\left\{s\left(\Phi_{\lambda}\right)\right\}$ is the boundary spectrum $\sigma_{b}\left(\Phi_{\lambda}\right)$ (see C-III, cor.2.12) of $\Phi_{\lambda}$. Moreover, $s\left(\Phi_{\lambda}\right)$ is a pole of the resolvent with residue of finite rank. Such spectral sets vary continuously under smooth perturbations of $\Phi_{\lambda}$ (see [Dunford-Schwartz (1958), VIT.6, Thm.9]), thus $\lambda \rightarrow s\left(\Phi_{\lambda}\right)$ is continuous.

For the operators $A_{o}$ and $A$ as defined in the beginning of this section we obtain an explicit representation of their resolvents.

Lemma 3.5. For the resolvents of the operators $A_{o}$, resp. $A$, on $E$ the following statements hold.
(a) For every $\lambda \in \mathbb{C}$ we have $\lambda \in \rho\left(A_{0}\right)$ and (3.7) $\quad R\left(\lambda, A_{0}\right) g(t)=\int_{t}^{0} e^{\lambda(t-s)} g(s) d s, g \in E$.
(b) For $\lambda \in \mathbb{C}$ satisfying $1 \in \rho(\Phi \lambda$ we have $\lambda \in \rho(A)$ and

$$
\begin{equation*}
R(\lambda, A) g=R\left(\lambda, A_{O}\right) g+c_{\lambda} \otimes R\left(1, \Phi_{\lambda}\right) \Phi R\left(\lambda, A_{O}\right) g, g \in E . \tag{3.8}
\end{equation*}
$$

Proof. (a) $p\left(A_{0}\right)=\mathbb{C}$ follows directly from ( $\left.T_{o}(t)\right){ }_{t z 0}$ being nilpotent (see A-III, Prop.1.l). For $q \in E$ we obtain $R\left(\lambda, A_{o}\right) g=f$ where $f$ is a solution of $\lambda f-f^{\prime}=9$.
Thus $R\left(\lambda, A_{o} \lg (t)=\int_{t}^{0} e^{\lambda(t-s)} g(s) d s+e^{\lambda t} \cdot x\right.$ for some $x \in F$. The condition $f \in D\left(A_{0}\right)$ now implies $x=0$ and Formula (3.7).
(b) The assertion $\lambda \in \rho(A)$ means that for every $g \in E$ the equation $\lambda f-f^{\prime}=g$ has exactly one solution $f$ in $D(A)$. As in case (a) we have $f(t)=\int_{t}^{0} e^{\lambda(t-s)} g(s) d s+e^{\lambda t} \cdot x$ for some $x \in F$ and hence $R(\lambda, A) g=f=R\left(\lambda, A_{0}\right) g+\varepsilon, 8 x$. The condition $R(\lambda, A) g \in D(A)$ implies $x-\Phi_{\lambda}(x)=\Phi R\left(\lambda_{i} A_{0}\right) g$. Hence $x=R\left(1, \Phi_{\lambda}\right) \Phi R\left(\lambda_{r} A_{0}\right) g$ if $1 \in \rho\left(\Phi_{\lambda}\right)$ and thus (3.8) follows.

Proposition 3.6. For each $\lambda \in \mathbb{C}$ the following implications hold.
(a) If $\lambda \in \sigma(A)$, then $1 \in \sigma\left(\Phi_{\lambda}\right)$.
(b) If $\quad \in P_{\sigma}\left(\Phi_{\lambda}\right)$, then $\lambda \in P_{\sigma}(A)$.

If, in addition, $\Phi\left(D\left(A_{0}\right)\right)=F$ or if $\Phi_{\lambda}$ is compact for all $\lambda \in \mathcal{C}_{\text {r }}$ then the following equivalence holds:
(c) $\lambda \in \sigma(A)$ if and only if $1 \in \sigma\left(\Phi_{\lambda}\right)$.

Proof. (a) This implication follows imnediately from Lemma 3.5(b).
(b) If $x \neq 0$ satisfies $x=\Phi_{\lambda}(x)=0$, then $f:=c_{\lambda} \in \mathbb{X} \in D(A)$ and $\lambda f-f^{\prime}=0$.
(c) If $\Phi\left(D\left(A_{o}\right)\right)=F$, then the equation $x-\Phi \lambda^{x}=\Phi R\left(\lambda, A_{o}\right) g$ has $a$
unique solution for every $g \in E$ if and only if $1 \in \rho\left(\Phi{ }_{\lambda}\right)$. According to the proof of $3.5(b)$ this is equivalent to $\lambda \in \rho(A)$.
If $\Phi_{\lambda}$ is compact, then $\sigma\left(\Phi_{\lambda}\right)\{0\}=\operatorname{Po}\left(\Phi_{\lambda}\right)$. Thus the assertion follows from (a) and (b).

The previous results will now be used to characterize the spectral bound of $A$ and hence the stability of the solutions of (RE).

Theorem 3.7. Let $A:=\frac{d}{d x}, D(A):=\left\{f \in A C([-1,0], F): f^{\prime} \in L^{1}(T-t, 0], F\right)$ and $f(0)=\Phi(f)$ be the generator of the solution semigroup on $E:=$ $L^{1}([-1,0], F)$ corresponding to ( PE ). If $F$ is a Banach Iattice and $0 \leqq \Phi \in(E, F)$, then the following assertions hold for $\lambda \in \mathbb{R}$.
(a) If $s\left(\Phi \lambda_{\lambda}\right)<1$, then $s(A)<\lambda$.
(b) Let $\Phi\left(\mathrm{D}\left(\mathrm{A}_{\mathrm{o}}\right)\right)=\mathrm{F}$ or let $\Phi_{\lambda}$ be compact for all $\lambda \in \mathbb{R}$. In addition, suppose that the map $H \rightarrow s\left(\Phi_{i l}\right)$ is strictly decreasing at $\mu=s(A)$. If $s\left(\Phi_{\lambda}\right)=1$, then $s(A)=\lambda$.
(c) Let $\Phi_{\lambda}$ be compact for all $\lambda \in \mathbb{R}$ or let $\Phi\left(D\left(A_{0}\right)\right)=F$ and suppose that $\mu \rightarrow s\left(\Phi_{\mu}\right)$ is continuous from the right. If $s\left(\Phi_{\lambda}\right)>1$, then $s(A)>\lambda$.

Proof. (a) Suppose $r:=s(A) \geq \lambda$, The positivity of (T(t)) $t \geqq 0$ implies $r \in \sigma(A)$ (see C-III,Thm.1.1.(a)) and by Prop.3.6 (a) this implies $1 \in \sigma\left(\Phi_{r}\right)$ so that $s\left(\Phi_{r}\right) \quad Z l$. since $\lambda \leqq r$ this $y i e l d s$ $s\left(\Phi_{\lambda}\right) \geq s\left(\Phi_{r}\right) \geq 1$.
(b) Let $s\left(\Phi_{\lambda}\right)=1$. Since $1 \in q\left(\Phi_{\lambda}\right)$ (see G-III,Thm.l.1(a)) $\lambda \in(A)$ by Prop. $3.6(c)$ whence $s(A) \geqq \lambda$. If $r:=s(A)$ we deduce as in the proof of (a) that $s\left(\Phi_{r}\right) \geq 1$. Now $r>\lambda$ would imply $s\left(\Phi_{\lambda}\right)>s\left(\Phi_{r}\right)$ $\geq 1$ (by the strict monotonicity of $\mu \rightarrow s(\Phi)$ ), a contradiction. Hence we conclude $s(A)=r=\lambda$.
(c) The hypotheses and Lemma 3.4 imply that the map $\mu \rightarrow s(\Phi)$ is continuous. Let $s\left(\Phi_{\lambda}\right)>I$. Since $s\left(\Phi_{\mu}\right) \leq\left\|_{\mu}\right\|_{k} \leqq\|\Phi\| \cdot\| \|_{\mu} \|$ we see that $s\left(\Phi_{\mu}\right)$ tends to zero as $\mu \rightarrow \infty$. Therefore there must exist $\mu^{\prime}>\lambda$ such that $s\left(\Phi_{\mu},{ }^{\prime}=1\right.$. Now Prop.3.6.(c) implies $\mu^{\prime} \in q(A)$ whence $s(A) \geqq \mathbb{L}^{\prime}>\lambda$.

Corollary 3.8. Under the hypotheses of Thm.3.7, suppose that the mapping $h: \mu \rightarrow s(\Phi)$ is continuous from the right and strictly decreasing. Then the following equivalence holds.
(3.9) $s(A) \stackrel{<}{\lessgtr} \lambda$ if and only if $s\left(\Phi_{\lambda}\right) \stackrel{<}{j} 1$.

In particular, $\lambda=s(A)$ is the only real solution of $s(\Phi)=1$.

Proof．The first equivalence follows easily from Thm，3．7．The addi－ tional statement is a consequence of the strict monotonicity of $h$ ．

Remarks．1．We note that in Prop． 3.6 and Thm． 3.7 it actually suffices that some power of $\Phi_{\lambda}$ is compact．

2．The equivalence（3．9）reduces the problem of determining $s(A)$ to the determination of the spectral bounds of the operators $\Phi_{\lambda}$ on the ＂smaller＂Banach space $F$ ．

In particular，$s(A)<0$ if and only if $s\left(\Phi_{0}\right)<1$ ．
3．We call the identity ${ }^{s} s\left(\Phi_{\lambda}\right)=1^{14}$ a generalized characteristic equation（see also the remark following E－IV，Thm，3．7）．The usual characteristic equation（see for example 「Hale（1977），p，168ff）and ［Heijmans（1984），sec．5］）is an equation determining all eigenvalues of the generator $A$ ．In fact，if $F$ is finite dimensional the charac－ terization of the spectral values $\lambda$ of $A$ in Prop．3．6．（c）reduces to solving the complex equation $\operatorname{det}\left(I d-\Phi_{\lambda}\right)=0$ ．Obviously，there is no analogous identity characterizing o（A）for infinite dimen－ sional $F$ ．However，in order to determine the long term behavior of the solutions of（RE）it is often enough to know the spectral bound $s(A)$ ．Under the assumptions of cor． 3.8 （in particular if $\Phi$ is posi－ tivel Formula（3．9）gives a tool to reduce this problem to the deter－ mination of the real solution of $s\left(\Phi_{\lambda}\right)=1$ ．

Example 3．9．We give an example of a large class of operators $\Phi$ satisfying the above assumptions．
For $\psi \in\left(L^{1}[-1,0]\right)^{\prime}=L^{\infty}[-1,0]$ and $B \in L(F)$ we denote by $\Phi:=\psi 8 \mathrm{~B}$ the operator defined by $\Phi\left(h s_{x}\right)=\psi(h) \cdot B x$ for $h \in L^{1}[-1,0], x \in F$ ． Note that $E=L^{1}([-1,0], F)$ is isomorphic to $L^{1}\lceil-1,0]$ 白 ${ }_{\pi} \quad$（see「Schaefer（1966），Chap．III，6．57）．The operator 9 is bounded from E into $F$ ．We assume that $\psi$ and $B$ ，hence $\Phi$ are positive．

Then the following holds and is stated without proof．

Lenme（a）If $B$ is compact，then $\Phi$ is compact．If $B$ is sur－ jective，then $\Phi\left(D\left(A_{o}\right)\right)=F$ ．
（b）$\quad \sigma\left(\Phi_{\lambda}\right)=\psi\left(\varepsilon_{\lambda}\right) \cdot \sigma(B)$ for each $\lambda \in \mathbb{C}$ ．Hence the map $\mu \rightarrow s\left(\Phi_{\mu}\right)$ is continuous and strictly decreasing on $R$ ．

For this type of＂retarding functionals＂$\Phi$ we obtain a simple char－ acterization of the spectral bound．

Corollary, Let $\Phi=\psi \& B$ where $0 \leqslant \psi \in L^{\infty}[-1,0]$ and $0 \leqslant B \in L(F)$ such that $B^{n}$ is compact for some $n \in W$. Then the following holds.
$s(A) \frac{\leq}{3} \lambda$ if and only if $\psi\left(E_{\lambda}\right) \cdot s(B) \leq 1$.

Example 3.10. Jeet $F$ be a Banach lattice with the Dunford-Pettis property (see schaefer(1974), Sec.IT.9). Take for example $F=C(K)$ or $F=L^{1}(X, \Sigma, \&)$. Furthermore define $E=J^{1}([-1,0,1, F)$ as usual and Let $\{K(s): s \in[-1,0]\}$ be a family of positive, irreducible, weakly compact operators on $F$ which is bounded.
If we define $\Phi f:=\int_{-1}^{0} K(s) f(s) d s$ for all $f \in E$, then (Rt) has the form

$$
\begin{align*}
& f(t)=\int_{-1}^{0} K(s) f(s+t) d s, t \geqq 0,  \tag{3.11}\\
& f_{0}=\psi \in E .
\end{align*}
$$

By Cor. 3.2 (3.11) has a unique solution $f \in L^{1}([-1, \infty), F)$. For $\Phi_{\lambda}$ we obtain $\Phi_{\lambda} x=\int_{-1}^{0} e^{\lambda s} K(s) x d s, x \& F$. In this case we have

$$
s(A) \leqq \lambda \text { if and only if } s\left(\Phi_{\lambda}\right) \frac{\leq}{>} 1 \text {. }
$$

Proof. By Cor. 3.8 it suffices to show that the map $h ; \lambda \rightarrow s\left(\Phi_{\lambda}\right)=$ $r\left(\Phi_{\lambda}\right)$ is strictly decreasing and continuous. With the help of 「Schaefer (1966), Thm.III.11.4.] and SSchaefer (1974), Thm.II.9.9] it is easy to show that ${ }_{\|}{ }^{2}{ }^{2}$ is compact and the continuity of $h$ follows by the above remark. It remains to show that $h$ is strictly decreasing.
Assume $s\left(\Phi_{\lambda}\right)>0$ for all $\lambda \in \mathbb{R}$. Since $\Phi_{\lambda}{ }^{2}$ and $\Phi_{\mu}^{2}$ are compact, $s\left(\Phi_{\lambda}\right)$ and $s\left(\Phi_{4}\right)$ are eigenvalues of $\Phi_{\lambda}$ resp. $\Phi_{\mu}$ with corresponding eigenfunctions $x_{\lambda}$ resp. $x_{\mu}$. In the same way $s\left(\Phi_{\lambda}\right)$ and $s\left(\Phi_{\mu}\right)$ are eigenvalues of $\Phi_{\lambda}{ }^{\prime}$ resp. $\Phi_{\mu}^{\prime \prime}$ with corresponding eigenfunctions $x_{\lambda}{ }^{\prime}$ resp. $x_{\mu}{ }^{\prime}$.
For $0<x \in F$ and $0<\mu<\lambda$ we obtain,
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-31.jpg?height=78&width=1600&top_left_y=2108&top_left_x=205) since $K(s)$ are positive and irreducible operators.
Especially, $\Phi_{\mu} x_{\lambda}>\Phi_{\lambda} x_{\lambda}=r\left(\Phi_{\lambda}\right) x_{\lambda} \quad$ and by evaluation
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-31.jpg?height=58&width=1611&top_left_y=2318&top_left_x=208) Since the operators $\Phi_{\lambda}$ are irreducible for each $\lambda$ (due to the irreducibility of $K(s)$ ) $x_{\mu}$ ' is a strictly positive functional on $F$. Hence $\left\langle x_{\lambda}, X_{\mu}{ }^{\prime}\right\rangle \neq 0$ and thus $\left.r\left(\Phi_{\mu}\right)\right\rangle r\left(\Phi_{\lambda}\right)$.

Example 3.11. The next example is of a more special form and occures as a model describing the cell cycle based on unequal division of cells, (see [Arino-Kimmel (1985)]). Let $F=L^{1}[0,1], E=L^{1}([-1,0], F)$ and define an operator $\Phi: E \rightarrow F$ by
$\Phi(\psi)(x):=\int_{0}^{l} k\left(x, x^{\prime}\right) \psi(q(x))\left(x^{\prime}\right) d x^{\prime}$ for almost all $x \in[0,1]$.
Here $q$ is a continuously differentiable function with strictly positive derivative satisfying $-1 \leq q(x) \leq E<0$ for $a 11 \quad x \in[0,1]$ and $k$ is a bounded, measurable, strictly positive kernel.
Then (RE) has the form
(3.12)

$$
\begin{aligned}
& f(t)(x)=\int_{0}^{1} k\left(x, x^{\prime}\right) f(t+q(x))\left(x^{\prime}\right) d x^{\prime}, t \geq 0 \\
& f_{o}=\psi \in E .
\end{aligned}
$$

It is easy to show that $\Phi \in L(E, F)$. If we define $K \in L(F)$ by $K f(x)=\int_{0}^{1} k\left(x, x^{\prime}\right) f\left(x^{\prime}\right) d x^{\prime}$ we obtain $\Phi_{\lambda} f=e^{\lambda q(x)} K f \quad(f \in F)$. Again we have

Proof. By Cor. 3.8 it suffices to show that the map $h: \lambda \rightarrow s\left(\Phi_{\lambda}\right)$ is strictly decreasing and continuous.
Since $k$ is bounded the operator $K$ is weakly compact and so is $\Phi_{\lambda}$. Since $E$ has the Dunford-Pettis property $\left(\Phi_{\lambda}\right)^{2}$ is compact [schaefer (1974), Thm.II.9.9 and this yields continuity of $h$.

Let $\lambda>\mu>0$ and $0<f \in E_{+}$.
Then $\Phi_{\mu} f(x)=e^{\mu G(x)} K f(x)=e^{(\mu-\lambda) G(x)} e^{\lambda q(X)} K f(x)=e^{(\mu-\lambda) G(x)} \Phi_{\lambda} f(x)$.
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-32.jpg?height=92&width=1623&top_left_y=1687&top_left_x=225) and, moreover, $\left(\Phi_{\mu}\right)^{n} f \geqq e^{n(\mu-\lambda) E}\left(\Phi_{\lambda}\right)^{n} f \quad$ for every $n \in$ 前. Hence ${ }_{i 1}\left(\Phi_{\mu}\right)^{n}\left\|>e^{n(\mu-\lambda) \varepsilon_{i}}\right\|\left(\Phi_{\lambda}\right)^{n H}$ and consequently $\quad r\left(\Phi_{\mu}\right) \leq e^{(\mu-\lambda) \varepsilon_{i}} r\left(\Phi_{\lambda}\right)$.
Now $(\mu-\lambda) \varepsilon>0$ implies $r\left(\Phi_{\mu}\right)>r\left(\Phi_{\lambda}\right)$.

The theory developed so far can also be applied to certain population equations. We first notice that (ACP) is isomorphic (in an obvious manner) to the following Cauchy problem.
For some $r \in R_{+}$take $E:=L^{l}([0, r], F)$ and let $A:=-\frac{d}{d x}$ on the domain $D(A):=\left\{f \in A C([0, r], F): f^{\prime} \in E\right.$ and $\left.f(0)=\Phi(f)\right\}$ for some $\Phi \in L(E, F)$.
We adopt this setting and transform the above results; e.g., en has to be defined as $\varepsilon_{\lambda}(s): \# e^{-\lambda_{s}}$ instead of $e^{\lambda s}$. As a concrete example we consider the following.

Example 3.12. Let $F:=\mathbb{K}^{n}, E:=L^{1}([0, r], F)=\Pi_{k=1}^{n} F_{k}, F_{k}=L^{1}[0, r]$. and defíne $\Phi: E \rightarrow c^{n}$ by $\Phi=\left\langle v_{i j} j_{n \times n}\right.$ where
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-33.jpg?height=78&width=1589&top_left_y=378&top_left_x=205) As $\Phi_{\lambda}$ we obtain the scalar matrix,
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-33.jpg?height=318&width=1523&top_left_y=543&top_left_x=204)

Suppose additionally that $\Psi_{\lambda}$ is irreducible for each $\lambda$, which is, for example, satisfied if $\beta_{i j}(a)>0$ for every a $\in[0, r]$ and $1 \leq i, j \leq n$ (see also 「Bellman-Cooke (1963), p. 257ffi).

Since $\Phi$ has finite dimensional range and hence is compact it follows that the function $h: \lambda \rightarrow E\left(\Phi_{\lambda}\right)$ is continuous. Moreover one shows that $h$ is strictly decreasing by using the same arguments as in Example 3.10 and by using the fact that $\Phi_{\lambda}$ is irreducible. The system of differential equations corresponding to $A$ is

$$
\begin{aligned}
& \frac{\partial}{\partial t} u_{i}(t, \alpha)=-\frac{\partial}{\partial \alpha} u_{i}(t, \alpha) \quad(i=1, \ldots, n) \text { for } t \in R_{+}, \alpha \in[0, r] \\
& \text { with initial condition }
\end{aligned}
$$

$$
\begin{align*}
& u_{i}(0, \alpha)=v_{i}(\alpha) \quad(i=1, \ldots, n) \text { for } \alpha \in[0, r]  \tag{3.13}\\
& \text { and boundary condition } \\
& u_{i}(t, 0)=\int_{0}^{r}\left[\sum_{j=1}^{n} \beta_{i j}(\alpha) u_{j}(t, \alpha)\right] d \alpha \quad(i=1, \ldots, n) \text { for } t \in R_{+} .
\end{align*}
$$

This system has a solution for every $\left(v_{1}, \ldots, v_{n}\right) \in D(A)$ and the asymptotic behavior is determined by the identity
![](https://cdn.mathpix.com/cropped/2025_01_15_941952d0f9f50d38c08bg-33.jpg?height=547&width=1620&top_left_y=1988&top_left_x=201)
whose unique real solution $\lambda$ is $s(A)$.

The infinite dimensional problem of determining s(A) is therefore reduced to solving a real one-dimensional equation.

The differential equation (3.13) may be interpreted as follows. Consider $n$ populations and let $r$ be the maximal age of an individual. Further let $u_{i}(t, a)$ denote the density of the number of members of the population $i$ with respect to age $\alpha$ at time $t$. The birth-rate is denoted by $B$. The first equation expresses the process of growing old. The second equation defines the initial state at time zero and the last equation describes mutual dependences of birth from individuals of the $n$ populations.

Example 3.13. Take $F:=L^{1}(\Omega)$ where $\Omega \subset \mathbb{R}^{2}$ is bounded and take E $\left.:=L^{1}(\Gamma 0, r], F\right)=L^{l}(\lceil 0, r] \times \Omega)$ for some $r \in \mathbb{R}_{+}$. Furthermore, let $\Phi$ $\# \beta \otimes B$ where $0<\beta \in L^{\infty}\lceil 0, r]$ and $B \in L(F)$ is an integral operam tor with positive bounded kernel $k$.
The corresponding Cauchy problem is the following.

$$
\begin{aligned}
& \frac{\partial}{\partial t} u(t, \alpha, x)=-\frac{\partial}{\partial a} u(t, a, x) \\
& \quad \text { with initial condition }
\end{aligned}
$$

(3.14)

$$
u(0, \alpha, x)=v(a, x)
$$

and boundary condition

$$
u(t, 0, x)=\int_{0}^{r} \beta(a) \cdot \int_{a} k(x, y) \cdot u(t, a, y) d y \underset{\text { for } t \in \mathbb{R}_{+}, x \in \Omega,}{ } \quad x(\lceil 0, r]
$$

From Thm.3.1 we conclude that for every $v \in D(A)$ there exists a solution $u \in E$. The boundedness of the integral kernel $k$ yields weak compactness of $B$ (see [scheefer (1974), sec.TI.5] and thus compactness of $\mathrm{B}^{2}$ by the Dunford-Pettis-Property of $\mathrm{L}^{1}(a)$ (see「Schaefer (1974), Chap, II, Thm.9.9]).

Thus we are in the situation of Ex. 3.9 and from Formula (3.10) we obtain the equivalence

$$
s(A) \stackrel{\zeta}{\bar{s}} \lambda \text { if and only if } \int_{0}^{r} B(\alpha) e^{-\lambda \alpha} d \alpha \cdot s(B) \frac{\alpha}{>} 1 \text {. }
$$

Again we can find a biological interpretation. Let $u(t, \alpha, x)$ denote the density of the number of individuals in a given population with respect to age $a$ and position $x$ at time $t$. As in Ex. 3.12 the first equation in (3.14) corresponds to the aging process. The second equation fixes the initial state of the population and the last equation describes the dependence of newborns on the birth rate $\beta$ and the distribution of the population over the "area" 0 .

NOTES.
Section 3. Coincidence of spectral and growth bounds for Lespaces was proven by $^{l}$ Derndinger (1980). For $\mathrm{L}^{2}$-spaces the result is due to Greiner-Nagel (1983). For the result on AM-spaces we refer to Remark 1.1 of $B-I V$ and the corresponding notes. Interpolation tefhiques in order to obtain results on arbitrary ${ }^{\text {P }}$-spaces were wsed by Voigt (1985). He proved Corollary $1.2(a)$. Theorem 1.3 as well as Propositions 1.6 . 1.7 , 1.9 are taken from Neubrander (i985a). For a comprehensive discussion of the coincidence of the spectral bound $s(A)$ with other growth bounds of positive semigroups on ordered Banach spaces, see klein f1984). Similar results for finite dimensional (non-1attice) ordered spaces can be found in Stern (1982). For general results on convergence of the solutions of the inhomogeneous Cauchy problem we refer to Fazy (1983) and the references therein.

Section 2. For quasi-compact semigroups (as considered in Theorem 2.1) we refer to the notes of $\operatorname{B-IV}, S e c .2$. Example 2.3 is discussed in more detail in Webb (1984) and Greiner (1984). Further examples of this type are considered in Section 3. It was Lotz (1986) who observed that Doeblin's condition is sufficient for quasi-compactness in reflexive $\mathrm{L}^{\mathrm{p}}$-spaces. (Obviously this is false in $\mathrm{L}^{1}$-spaces since in this case the identity operator satisfies Doeblin's condition.)
The $0-2$-Law for certain bounded operators on $L$ was first established by Ornstein and sucheston. A special case of the 0-2~Law for onemarameter semfroups (Theorem 2.6) was proven by wfikler (1972) while the general result and its corollaries can be found in Greiner (1982). Corollary 2.11 remains true when the assumption 'T(t) is a kernel operator' is replaced by 'T(t, is an irreducible Harris operator' (see Lin (1983)).
It is well-known that semigroups play an important role in probability theory faee e.g, Dynkin (1965), Feller (1952) and Hille-Phillips (1957)). A more detailed discussion than the one in Example 2.8 is given in Chapter 2 of van Casteren (1985). Convergence to periodic solutions is investigated in Kerscher-Nagel (1984) and Naget (1984) where Proposition 2.13 is proved. They proved Proposition 2.13. The equation considered in Example 2.15 describes a linear model for cell division with exponential growth of individual cells. The occurxing phenomena are conjectured by Diekmann et al. (1984).

Section 3. One of the starting points in the study of retarded equations was the book of Bellmann-Cooke (1963) on differential-difference equations. Initiated by Hale's semigroup approach (see $B-I V$, sec. 3 ) to retarded differential equations, Dyson-Villella-Eressan (1979), Villella-Bressan (1985) and Webb (1977) used such methods to investigate retarded equations. These similarly apply to Volterra equations [Miller (1974), Webb (1977)], and to age-dependent population equations [Prits (1981), Webb (1984), (1985a) Z. Recently, the aspect of positivity has led to statem ments on the asymptotic behavior of solutions of retarded equations. In this context the investigation of population equations by Greiner (1984), Heijmans (1985a) and Webb (1985b) should be mentioned.

