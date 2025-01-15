# CHAPTER B-III <br> SPECTRALTHEORYOR OR <br> POSITIVE SEMIGROUPS ON CO(X) <br> by <br> Günther Greiner 

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-05.jpg?height=75&width=1492&top_left_y=2167&top_left_x=225)
It follows that $\|\mathrm{R}(\lambda, T)\| \leq\|R(\lambda \mid, T)\|$ and therefore

$$
\begin{equation*}
\lim _{\lambda+r}\|\mathrm{R}(\lambda, T)\|=\infty \tag{1,15}
\end{equation*}
$$

By the uniform boundedness principle there exist a sequence ( $\lambda_{n}$ ), $\lambda_{n}+r$ and a positive $\Psi \in M(K)$ such that $\| R\left(\lambda_{n}+T\right) \psi \psi+\infty$. Defining $\Psi_{n}:=\left\|R\left(\lambda_{n}, T\right)^{*}\right\|^{-1} R\left(\lambda_{n}, T\right)^{\prime} \quad$ we have
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-06.jpg?height=79&width=1522&top_left_y=246&top_left_x=227)

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

## 2. THE BOUNDARY SPECTRUM

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-08.jpg?height=62&width=1335&top_left_y=2619&top_left_x=229)

Here $\tilde{\mathrm{h}}$ denotes the continuous extension of $\mathrm{h} /|\mathrm{h}|$ to BX . Defining $T_{1}:=M_{\tilde{h}}{ }^{1} \tilde{R}_{\tilde{h}}$ we have by (2.9)
(2.10) $\quad T_{1} 1=M_{\hat{h}}^{-1} \tilde{R} \tilde{h}=1$ and
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-09.jpg?height=72&width=1474&top_left_y=495&top_left_x=208)
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-12.jpg?height=67&width=1508&top_left_y=355&top_left_x=231)
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-12.jpg?height=58&width=1280&top_left_y=436&top_left_x=228)

```
Since % is strictly positive, (2.14) and (2.15) imply that
T(t) |h| = |h| for t }\geqq0\mathrm{ or equivalently A |h| = 0.
Now Thm.2.4 implies that Ah[n] = inah[n] (n\in\mathbb{Z}).
```

Concerning the hypothesis $T\left(t_{0}\right)^{\prime} \phi=\exp \left(s(A) t_{0}\right) \cdot \phi \gg 0$ we recall that in case $X$ is compact there are always positive linear forms such that $T(t)^{\prime} \phi=e^{s(A)} t_{\phi}$ (see Thm.l.6). If the semigroup is irreducible, then one also has q >> 0 (see sec. 3 below).

In a second result we consider semigroups having compact resolvent, An important step of the proof is isolated as a lemma. Before stating it we recall that given a closed ideal I $\quad C_{o}(\mathrm{X})$ then $I$ as well as $C_{0}(X) / I$ are spaces of continuous functions on a locally compact space vanishing at infinity. More precisely, if $I=\left\{f \in C_{o}(X): f_{M}=0\right\}$ for a suitable closed subset $M \in X$, then $I=C_{o}(X, M)$ and $C_{o}(X) / I$ $\cong C_{0}(M)(C f, B-I)$. It follows that given another closed ideal $J=\left\{f \in C_{O}(X): f_{N}=0\right\}$ such that $I \subset J$ i.e., N $\subset M$, then $J / I$ can be identified with $C_{0}(M \backslash N)$. We do not use this concrete reprew sentation of $J / I$, However, this shows that we stay within our setting of Banach spaces of continuous functions on locally compact spaces.

Lemma 2.8. Suppose $A$ is the generator of a positive semigroup $T$ such that the spectral bound $s(A)$ is a pole of the resolvent of order $k$. Then there is a sequence
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-12.jpg?height=78&width=1017&top_left_y=2068&top_left_x=231)
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

|  | order | $\mathrm{I}_{0}$ | $\mathrm{I}_{1}$ | $I_{2}$ | $\mathrm{I}_{3}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{d}>0, \mathrm{f}>0$ | 3 | $\left\langle\mathrm{e}_{1}\right\rangle$ | ${\ll e_{1}} \mathrm{E}_{2}{ }^{2}$ | $\left.\mathrm{se}_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ | $0^{4}$ |
| $d=0, f>0$, | 2 | $\left\langle e_{1}\right\rangle$ | $\left\langle e_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ | $c^{4}$ |  |
| $d=0, \quad f=0, \quad e>0$ | 2 | $\left\langle e_{1}\right\rangle$ | $\left\langle\mathrm{e}_{1}, \mathrm{e}_{2}, \mathrm{e}_{3}\right\rangle$ | $c^{4}$ |  |
| $d>0, f=0, \quad e>0$ | 2 | $\left\langle e_{1}\right\rangle$ | $\left\langle e_{1}, e_{2}\right\rangle$ | $c^{4}$ |  |
| $\mathrm{d}>0, \mathrm{f}=0, \mathrm{e}=0$ | 2 | $\left\langle e_{1}\right\rangle$ | $<_{1}, e_{2}, e_{4}>$ | $0^{4}$ |  |

This example also shows that the operators $Q_{k-1}, \ldots, Q_{1}$ are not necessarily positive (e.g. $a>0, b=c=0, d=e=f=2$ ) , A more general (and more interesting) example is the following:
Suppose that $A_{i}(i=1, \ldots, n)$ are generators of positive semigroups on $C_{o}(x)$ such that $s\left(A_{i}\right)=0$ is a first order pole of the resolvent. And let $A_{i j}(l \leqslant i<j \leq n)$ be positive bounded operators on $\mathrm{C}_{\mathrm{o}}(\mathrm{X})$.
Then $A \quad:=\left(\begin{array}{llll}A_{1} & A_{12} & \cdots & { }^{A}{ }_{1} n \\ 0 & A_{2} & \cdots & A_{2 n} \\ \vdots & \vdots & \cdots & \vdots \\ 0 & 0 & \cdots & A_{n}\end{array}\right)$
is the generator of a positive semigroup on
$C_{o}\left(\mathrm{X}, \mathrm{C}^{\mathrm{M}}\right)=\mathrm{C}_{\mathrm{o}}(\mathrm{X}) \times \mathrm{C}_{\mathrm{o}}(\mathrm{X}) \times \ldots \times \mathrm{C}_{\mathrm{O}}(\mathrm{X})$, and $\mathrm{s}(\mathrm{A})=0$ is a pole of the resolvent of order $k$ where $l \leqslant k \leqslant n$.

Theorem 2.9. Suppose $A$ is the generator of a positive semigroup on $C_{o}(X)$ such that every point of $\sigma_{b}(A)$ is a pole of the resolvent. Then $P \sigma_{b}(A)=\sigma_{b}(A)$ is cyclic.

Proof. If $\sigma(A)=\phi$ there is nothing to prove, thus we can assume that $s(A)=0$. In view of the lemma and $A m I I, P r o p .4 .3(i)$ we can assume that $s(A)$ is a first order pole with strictly positive resi* due, which we call $Q$. We have $A O=Q A=s(A) A=0$ (see $A-I I I$, 3.6), hence
(2.18) $\mathrm{QT}(\mathrm{t})=\mathrm{T}(\mathrm{t}) \mathrm{Q}=\mathrm{Q}$ for all $\mathrm{t} \geqslant 0$.

If $A h=i \alpha h$ for some $\alpha \in \mathbb{F}, h \neq 0$, then $T(t) h=e^{i \alpha t_{h}}$ (by AuIII, Cor.6.4). Hence $|h|=\left|e^{i \alpha t_{h}}\right|=|T(t) h| \leq T(t)|h|$, or equivalently, $T(t)|h|-|h| \geqq 0 . B Y(2.18)$ we have $Q(T(t)|h|-|h|)=0$.
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-16.jpg?height=64&width=1614&top_left_y=1076&top_left_x=227) $\operatorname{Re} \lambda \geq s(A)-r\} \quad i s$ compact for every $r>0$ (see $A-I I$, Thm, 1.20) and this set does not have accumulation points because $A$ has compact resolvent. In other words, it is a finite set. The assertion now follows from Thm. 2.9 and Cor.1.4.

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-17.jpg?height=64&width=1611&top_left_y=773&top_left_x=208) there exists a dominant real eigenvalue with corresponding positive eigenfunction. Actually, the eigenfunction is strictly positive. (In fact, if $f \in C^{2}, E \geqslant 0$ and $f\left(x_{0}\right)=0$ for some $x_{0}$, then $f^{\prime}\left(x_{0}\right)=0$. Therefore the uniqueness theorem for ordinary differential equations implies that $f$ is identically zerol.
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-18.jpg?height=74&width=1617&top_left_y=1365&top_left_x=228) unless $\Psi=r_{o} \delta_{o}$ for some $r_{o} \in \mathbb{H}$.)

We conclude this section with some additional remarks related to Thm. 2.9 and its corollaries.

Remarks 2.15.(a) If $s(A)$ is a pole of the resolvent, then for generators of positive semigroups one has the following equivalences:
(i) $\quad s(A)$ is a first order pole.
(ii) For every $0<f \in \operatorname{ker}(s(A)-A)$ there exists $0 \leqslant \Psi \in \operatorname{ker}\left(s(A)-A^{*}\right)$ such that $\langle f, \Psi\rangle>0$.
(iii) For every $0<\Psi \in \operatorname{ker}\left(s(A)-A{ }^{\prime}\right)$ there exists
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-18.jpg?height=46&width=1034&top_left_y=2287&top_left_x=391)

In particular, if ker(s(A) *A) contains a strictly positive func* tion or if ker(s (A) * A') contains a strictly positive measure, then $s(A)$ is a first order pole.

We sketch the proof of (i) $\Leftrightarrow$ (ii) assuming that $s(A)=0$. If 0 is a first order pole, then the residue $P$ is a positive projection satisfying $P E=$ ker $A, P^{\prime E}=$ ker $A^{+}$(see A-III, 3.6) . Thus given
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-19.jpg?height=46&width=1617&top_left_y=448&top_left_x=205) $\left.\Psi:=P^{\prime} \phi:\langle f, \Psi\rangle=\left\langle f, P^{\prime} \phi\right\rangle=\langle P f, \phi\rangle=\langle f, \phi\rangle\right\rangle 0$. To prove the reverse direction we first observe that the highest coefficient $Q_{k}$ of the Laurent expansion is a positive operator. Thus if 0 is a pole of order $k \geqq 2$ we choose $0<h \in E$ such that $f:=Q_{k} h>0$. Then $A f=A Q_{k} h=0$ and for every $\Psi \in$ ker $A^{1}$ we have $\langle f, \Psi\rangle=\left\langle Q_{K} h, \Psi\right\rangle=\left\langle h, Q_{k}{ }^{*} \Psi\right\rangle=\left\langle h, Q_{k-1}{ }^{1} A^{\prime \Psi}\right\rangle=0$.
(b) If a linear operator $s$ on $C_{D}(X)$ is weakly compact, then $s^{2}$ is compact (see B-IV, Prop.2.4(b)). Therefore every non-zero spectral value of a weakly compact operator is a pole of the resolvent. This shows that Thm. 2.9 is applicable if either $T\left(t_{0}\right.$ ) is weakly compact for some $t_{o}$ or $R(\lambda, A)$ is weakly compact for some $\lambda \in \rho(A)$, We quote two criteria for weak compactness:
(2.31) $I f \quad T \in L(C(K)), K$ compact, is positive, then it is weakly compact if and only if its biadjoint $T$ " maps the bounded Borel functions into $C(K)$ (see B-IV,Prop. 2.4).
(2.32) A positive operator $T$ on $C_{0}(X)$ which is dominated by a finite rank operator, is weakly compact. (Actually, its adjoint $T^{\prime}$ is dominated by a finite rank opew rator as well, hence it maps the unit ball in an order interval. It follows that $T^{\prime}$ is weakly compact hence so is $\mathbf{T}$.)
(c) Stronger results than Thm. 2.9 will be proved in Chapter C-III. Actually, assuming only that $s(A)$ is a pole of finite algebraic multiplicity one can show that $\sigma_{b}(A)$ contains only poles of finite multiplicity (C-III.Thm.3.13). In C-III, Cor.2.12 we will show that $\sigma_{b}(A) i s$ cyclic whenever $s(A)$ is a pole of the resolvent.
(d) Example 2.14 (b) can be extended to systems of functional diffem rential equations even the infinite dimensional case. For details we refer to Sec. 3 of Chapter B-IV.

## 3. IRREDUCIBLE SEMIGROUPS

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-20.jpg?height=53&width=1617&top_left_y=2278&top_left_x=228) Obviously $I$ is T-invariant.
(ii) + (iii): Given $0<f \in E, x \in X$. By (ii) there exists $t_{o}$ such that $\left(T\left(t_{D}\right) f\right)(x)=\left\langle T\left(t_{D}\right) f, \delta_{x}\right\rangle>0$.
(iii) + (vi) : Suppose that $U_{t \geqslant 0} \operatorname{supp} T(t)^{\prime} s_{y}$ is not dense for some $y \in X$. Then there exists $f_{0} \in E, f_{o}>0$ such that
$\operatorname{supp} f_{0} \cap \operatorname{supp} T(t)^{\prime} f y=\emptyset$ for every $t \geq 0$. Hence ( $\left.T(t) f_{0}\right)(y)=$ $<f_{0}, T(t)^{\prime} \delta_{y} \gg 0$, that is, $y \not U_{t \geq 0}\left(x \in X:\left(T(t) f_{0}\right)(x)>0\right\}$. (vi) $+(v):$ Given $0<f \in E, \lambda>u(A), y \in X$, there exists
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-21.jpg?height=64&width=1452&top_left_y=462&top_left_x=208) $\left(T\left(t_{o}\right)(f)(y)=\left\langle f, T\left(t_{o}\right) ' \delta\right\rangle>0\right.$ and therefore $(R(h, A) f)(y)=\int_{0}^{\infty} e^{-h t}(T(t) f)(y) d t>0$. Since $\lambda \rightarrow R(\lambda, A) f(i s$ decreasing in the interval ( $s(A), *$ ) (use the resolvent equation and the fact that $R(\lambda, A)$ is positive) we have $R(\lambda, A) f \gg 0$ for all $\lambda>S(A)$.
(V) $\rightarrow$ (vi): If $I$ is a $R(\lambda, A)$-invariant ideal and $0<f \in I$, then $g:=R(\lambda, A) f \in I$. By (v) $g$ is strictly positive thus $I$ has to be dense (it contains all functions of compact support).
(iv) $+(i): A t$ first we recall that a closed linear subspace which is invariant for $R\left(\lambda_{O}, A\right) \quad\left(\lambda_{O} \in \rho(A)\right)$, is invariant for $R(\lambda, A)$ whenever $\lambda$ and $\lambda_{\rho}$ belong to the same component of $\rho(A)$. Hence by $A-I, 3,2$ every $R\left(\lambda_{O}, A\right)$-invariant subspace where $\lambda_{O} \in \rho_{+}(A)$ is T-invariant and vice versa.

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-22.jpg?height=67&width=1615&top_left_y=1097&top_left_x=232) Then the following assertions are equivalent:
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-23.jpg?height=55&width=1620&top_left_y=384&top_left_x=201) corresponding semigroup is irreducible if and only if wlesupp ${ }^{\Psi}$.
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-27.jpg?height=298&width=549&top_left_y=271&top_left_x=731)
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-28.jpg?height=50&width=1617&top_left_y=2231&top_left_x=228) cible. Next we apply Thm. $3.6(\mathrm{~d})$ in oxder to show that the spectral bound is a dominant eigenvalue. We can assume that $s(L)=0$. If $s$ (L) is not dominant, then by Thm. 3.6(d) we have
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

## 4. SEMIGROUPS OF LATTICE HOMOMORPHISMS

As we have seen in Section 2 the boundary spectrum of a many positive semigroups is a cyclic set. However, there are hardly any restrictions on the set $\{\lambda \in \sigma(A): \operatorname{Re} \lambda<S(A)\}$, except that it is symmetric with respect to the real axis. For semigroups of lattice homomorphisms the situation is quite different. We will show that the whole spectrun is an imaginary additively cyclic subset of $\mathbb{C}$ (see Def.2.5). A complete proof of this results requires some facts of the theory of Banach lattices, therefore, we postpone it to Part $C$ (see C-III, Thm.4.2).

Theorem 4.1. If $A$ is the generator of a semigroup of lattice homomoxphisms, then $\sigma(A), A \sigma(A)$ and $P o(A)$ are cyclic subsets of $\mathbb{C}$.
$1^{\text {st }}$ part of the proof. We prove the assertion concerning $A O(A)$ and $P o(A)$. Assume that $A h=(\alpha+i \beta) h, \alpha, B \in \mathbb{R}, h \neq 0$, then $T(t) h=e^{\alpha t} e^{i \beta t} h$ for all $t \geqq 0$ (A-III, Cor.6.4). Since $T(t)$ is a lattice homomorphism we havo $T(t)|h|=|T(t) h|=e^{\alpha t}|h| \quad(t \geqslant 0)$ or $A|h|=\alpha|h|$, hence $A h^{[n]}=(\alpha+i n \beta) h^{[n]}$ for all $n \in \mathbb{Z}$ by Thm.2.4(b) . We have shown that $P \sigma(A)$ is cyclic.
To prove that $A \sigma(A)$ is cyclic as well, one considers a semigroup F-product $E_{F}^{\top}$ of $E$ (see A-III,4.5). It is easy to see that $E_{F}^{\top}$ is a Banach lattice and ( $\left.T_{F}(t)\right)$ is a semigroup of lattice homomorphisms. The proposition in A-IIT, 3.5 implies $A \sigma(A)=P \sigma\left(A_{F}\right)$. Thus the assertion follows from the cyclicity of point spectrum.

Performing a similar construction as in Ex.2.6(f) one can show that every closed cyclic subset of $\mathcal{C}$ which is contained in a left halfplane is the spectrum of a suitable semigroup of lattice homomorphisms. For details see Derndinger-Nagel (1979).
In the following we restrict ourselves to the case of compact spaces. Then a semigroup of lattice homomorphisms can be described explicitly by a semi-flow and real-valued functions $h$ and $p$ (see B-II, Thms.3.5 3.6). The function $p$ has no influence on spectral properties (cf. B-II, (3,7)). Therefore we will assume that (T (t)) has the following form (cf. B-II,Thm.3.5):

```
(4.1) T(t)f= ht.f.0\phit (t @ 0, f fC(K)) where
        \phi=(\mp@subsup{\phi}{t}{}):\mp@subsup{\mathbb{R}}{+}{+}\timesK->K is a continuous semiflow and
        ht (x)= Exp \int {
        continuous function h : K -> i .
```

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
$\phi(t, x)=\left\{\begin{array}{cc}x-t \quad \text { if } x \geq t \\ 0 & \text { if } x<t\end{array} \quad(\infty-t=\infty) \quad\right.$.
Then we have $K_{t}=K$ for all $t$, hence $K_{m}=K$ and $\sigma(A)=\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda \leq 0\}, \operatorname{Ro}(A)=\{\lambda \in \mathbb{C}=\operatorname{Re} \lambda<0\} \cup\{0\}$.
(c) Consider on $K_{1}:=[-1, \infty)$ the equivalence relation $\sim$ defined by " $x \sim y$ if ond only if $x, y \geqq 0$ and $x-y \in Z "$. The semiflow $\$_{1}$ on $K_{1}$ given by $\phi_{1}(t, x)=x+t$ induces a semiflow $\phi$ on the
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-32.jpg?height=70&width=1509&top_left_y=1230&top_left_x=222) $\left(K_{\infty} \not[0,1] / \ldots \cong\right.$ ) . The spectrum of the corresponding semigroup on K is given by $\sigma(\mathrm{A})=2 \pi i \mathbb{Z}$.
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
& \phi_{o}(t, x) \text { is defined if } t_{x}<t<\bar{t}_{x} ; \\
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
$\phi(t, x):=\left\{\begin{array}{lll}\phi_{0}(t, x) & \text { if } 0 \leq t<s_{x} \\ \phi_{0}\left(s_{x}, x\right) & \text { if } & t \geq s_{x}\end{array}\right.$
$\phi$ is a continuous semiflow on the compact set $k:=\bar{\Omega}$. We have $K_{c}=K$ and ${ }^{\phi} \mid K_{\infty}$ is not injective.
In case $F$ is differentiable, the generator of the corresponding semigroup is the closure of the operator $A_{2}$ defined by
$A_{2} f:=(F \mid g r a d f), D\left(A_{2}\right):=\left\{f\left(C^{l}(\hat{\Omega}):(F \mid g r a d f)=0\right.\right.$ on $\left.\partial \Omega\right\}$.
(c) We consider $\Omega$ as in (b) and asstume that (F(x)|v(x)) $\leqslant 0$ for every $x \in \partial \Omega$. Then for every $x \in \overline{\bar{\Omega}}$ we have $\bar{t}_{x}=\infty$.
Thus $t:=\phi_{0} \mid \mathbb{R} \times \bar{\Omega}$ is a continuous semiflow on $K:=\bar{\pi}$.
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-36.jpg?height=70&width=1617&top_left_y=1624&top_left_x=228) $t>s$ and ${ }^{\phi} \mid K_{\infty}$ is injective. For a differentiable vector field $F$ the generator of the corresponding semigroup is the closure of $A_{3}$ defined as follows: $A_{3} f:=(F \mid g r a d f), D\left(A_{3}\right):=C^{l}(\bar{\Omega})$.

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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-38.jpg?height=66&width=1377&top_left_y=1075&top_left_x=234)
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
![](https://cdn.mathpix.com/cropped/2025_01_15_f36dcadc2e84a4ddaaadg-40.jpg?height=66&width=1620&top_left_y=321&top_left_x=224) restriction a semigroup ( $T(t)$ ) on $I=C_{o}(X)$, where $x=K_{1}$ ( $K_{o}$. In this case one can construct semi-flows associated with (T(t)) on XU\{ $A$ ) or on $\bar{X}$ (closure in $K_{1}$ ), but in general one cannot find a corresponding multiplicator which is defined on one of these compactifications.

The situation is much nicer when groups of lattice homomorphisms instead of semigroups are considered. In this case there is an analogue of (4.1) (cf. B-II,Thrm.3.14) and the spectrum can be described completely. For more details and the proof of the following result we refer to Arendt-Greiner (1984).

Theorem 4.11. Suppose $X$ is a locally compact space and (T (t)) $t \in \mathbb{R}$ is a group of lattice homomorphisms governed by the flow $\phi$ and the multiplicator $h$. Then we have:
(a) $\quad \sigma(A)=\sigma_{1} \mathrm{Va}_{2} \mathrm{Vo} \sigma_{3}$ where the sets $\sigma_{i}$ are defined as follows $\sigma_{1}:=\left\{h^{\wedge}(x)+i \cdot 2 \pi k / \tau_{x}: x \in X, 0<\tau_{x}<\infty\right\}$, $\sigma_{2}:=\left\{h(x): x \in X, \tau_{x}=0\right\}, \sigma_{3}:=\{\lambda \in \mathbb{C}: \lambda+i \mathbb{R} \subseteq o(A)\}$
(b) $\quad o(T(t))=\exp (t \sigma(A))$ for every $t \geq 0$.
(c) Every isolated point of $\sigma(A)$ is a first order pole of the resolvent.

WOTES.
Spectral theory for a single positive operator is an essential cornerstone for spectral theory of positive one-parameter semigroups. Many of the results we have presented $\mathrm{In}_{\mathrm{n}}$ this chapter have analogues in the discrete case (i.e. for a single operator). This relation may serve as a gutde. However, only in few cases can the continuous version be deduced directly fron fts discrete analogue. Therefore we will not try to trace back the roots of every result to the discrete version, Instead we refer to Schaefer (1974) and the notes and references given there.
Many of the results we have presented in this chapter can be extended (more or less easily) to the more general setting of Eanach lattices, which include the very important examples of $L^{\text {p }}$-spaces. Others are typical for $C(X)$ and allow no extension. We will discuss this fact in more detail in Chapter C-III. The more general setting considered there also allows us to prove results for $C$ ( $X$ ) which we could not obtain staying within the franework of spaces of continuous $\frac{9}{1}$ unctions.

Section 1. Theorem l.l was stated by Karlin (1959), but a complete proof is given in Derndinger (1980). Propositon 1.5 is taken from Greiner (1982) and Theorem 1.6 is (implicitely) contained in Derndinger-Nagel (1979). A generalization to (nonlattice) ordered Eanach spaces can be found in Sec. 2.4 of Eatty-Robinson (1984).

Section 2, Lemma 2.3 dates back to Rota (see Schaefer (19743). Our approach follows Greiner (1981). The notion ' (imaginary) additively cyclic' was introduced by berndinger (1980) (and Schaefer (1980) respectively). Derndinger proves some fyclicity results for the boundary spectrum. A result simylar to Proposition 2.7 is given in Sec. 7.4 of Davies (1980). Lemma 2.8 in conbination with C-III, Lemma 3.13 can be used to characterize semigroups whose spectral bound is a pole of finite algebraic multiplicity (see C-III, (3.19) . The hypothesis of Theorem 2.9 can be weakened, one only needs that $s(A)$ is a pole of the resolvent (see C-III, Cor.2.12). Further results on the cyclicity of the boundary spectrum will be given in Chapter C-III. In particular we refer to $\mathrm{C}-\mathrm{III}$, Thms.2.10, 3.11 and 3.13 . The dichotomy stated in (2.19) is probably the most interesting consequence of cyclicity results. It has far reaching consequences on the asymptotic behavior of positive semigroups. Example 2.13 is due to Davies (unpublished note). Example 2.14 (b) will be discussed in more detail and more generality in Section 3 of Chapter E-IV. We return to Remark 2.15(b) in Section 2 of $\mathrm{B}-\mathrm{IV}$.

Section 3. The concept of irreducibility as defined in 3.1 is closely related to various other notions: In topological dynamics flows inducing irreducible semigroups are called 'minimal flows' (cf. Example 3,4(a)). Moreover, 'ergodicity' and 'undque ergodicity' are closely related to irreducibllity (see CornfeldwFominusinai (1982) or Krengel (19853). Irreducible semigroups are discussed to some extent ín Davies (1980). E.g. he proves a special case of Theorem 3.6. Froposition 3.3 will be generalized in C-III, Prop+3.3. Assertion (a) of Proposition 3.5 was proven by Schaefer (1983) while Theorem 3.6 is taken from Greiner (1982). Elliptic operators (more general than Example 3.10(b)) as generators on spaces of continuous functions, were investigated by wany people, e.g. Eony-Courrège-Priouret (1968), Kuhn (1985), Roth (1976) 4(1978) and Stewart (1974).

Section 4. Theorem 4.1 is due to Derndinger (1984.). The spectrum of semigroups of Markov lattice homomorphisms is investigated by Derndingerwigal (1979). In partiw cular they prove Theorem 4.4 for Markov semigroups. Earlier results are due to Scarpellini (1974). We indicated briefly in Example 4.6 that there is a relationw ship between spectral propetties of lattice semigroups and differentiable dynamics. For more details we refer to Chicone-Swanson (i981) and Sackerwsell (1978). E.g., the 'annular hull theorem' is a special case of Theorem 4.11 (b). The general result 4.11 was proven by Arendt-Greiner (1984).

