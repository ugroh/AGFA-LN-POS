# SPECTRALTHEORY OFP P O S I T I V E S E M I G R O U P ON BANACH LATTICES <br> by <br> Günther Greiner 

In Chapter $B-I I I$ we have shown that positive semigroups on spaces $C_{o}(X)$ possess several interesting spectral properties. Now we are going to extend many of the results obtained there to the more general setting of Banach lattices. We will improve some of the results of B-III considerably and give the complete proof of B-III.Thm. 4.1 . Throughout this chapter we will assume that $E \neq\{0\}$ is a complex Banach Iattice.

## 1. THE SPECTRAL BOUND

The fact that the spectral bound of a positive semigroup is always contained in the spectrum (provided that the spectrum is non-empty) is also true in the general setting of Banach lattices. The proof given in B-III, Thm, 1,1 for spaces $C_{o}(X)$ works in the general case too. Another proof is given below (cf. Cor.1.4). Furthermore, Cor, I. 3 and Prop.I. 5 of $B-I I I$ are true in the setting of Banach lattices and their proofs can be carried over to the general case. For the sake of completeness we sumarize these results in the following theorem.

Theorem 1.I. Let $A$ be the generator of a positive semigroup $(T(t))_{t \geq 0}$ on a Banach lattice $E$.
(a) $s(A) \in \sigma(A)$ unless $\sigma(A)=\varnothing$.
(b) For $\lambda_{o} \in \rho(A)$ we have:
$\mathrm{R}\left(\lambda_{\mathrm{O}^{\prime}} \mathrm{A}\right)$ is positive if and only if $\lambda_{\mathrm{O}_{1}}>\mathrm{s}(\mathrm{A})$.
In this case $r\left(R\left(A_{0}, A\right)\right)=\left(\lambda_{0}-s(A)\right)^{O_{1}}$.
(c) If $T(I)$ has a positive fixed vector $h_{o}$, then ker $A$ contains a positive element $h$ such that $h_{o} \in \overline{E_{|h|}}$.
(d) If $T(1)^{\prime} \phi_{o}=\phi_{O}$ for some $\phi_{o} \in E_{+}^{*}$ then there exists $\phi \in D\left(A^{*}\right)+w i t h \quad\{f \in E=\langle | f|, \phi\rangle=0\} \subseteq\left\{f \in E:\langle | f\left|, \phi_{0}\right\rangle=0\right\}$ such that $\mathrm{A}^{*} \boldsymbol{\phi}=0$.

The fact that $s(A)$ is always an eigenvalue of the adjoint (cf. B-III Thm. 1.6 ) is characteristic for spaces $C(K), K$ compact, as can be seen considering the Iraplacian on $L^{P}\left(\mathbb{R}^{n}\right)$ where $I<p<\infty$ or on $C_{o}\left(\mathbb{R}^{n}\right)$ (see B-III, Ex.I.7). Another result which cannot be extended to arbitrary Banach lattices is that spectral bound and growth bound coincide (cf. B-IV, Thm.l.4); an example is given in A-III, Ex.l.3. Despite of this the resolvent $R(\lambda, A)$ of a positive semigroup is given as the Laplace transform of the semigroup in the half-plane $\{z \in \mathbb{C}: \operatorname{Re} z>s(A)\}$ (even in case that $\omega(A)>s(A)$ ). Note however that the integral exists only as an improper Riemann integral. By Datko's Theorem (A-IV,Thm. 1.11) the function $t+e^{-\lambda t} \cdot T(t) f$ cannot be Bochner integrable for all $f \in E$ in case Re $\lambda \leqq \omega(A)$.

Theorem 1.2. Suppose $A$ is the generator of a positive semigroup (T (t) ) $t \geq 0$. For $\operatorname{Re} \lambda>s(A)$ we have:
(1.1) $R(\lambda, A) f=\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s) f d s$ for all $f \in E$.

Moreover, the operators $\int_{0}^{t} e^{-\lambda s} T(s) d s$ tend to $R(\lambda, A)$ with respect to the operator norm as $t \rightarrow \infty$.

Proof. We fix $\lambda_{o}>w(A)$. Then by $A-I, P r o p .1 .11$

$$
\begin{equation*}
R\left(\lambda_{o}, A\right)^{n+1} f=\frac{1}{n!} \int_{0}^{\infty} s^{n} \exp \left(-\lambda_{o} s\right) T(s) f d s \quad\left(n \in \mathbb{N}_{o}, f \in E\right) \tag{1.2}
\end{equation*}
$$

Given $\mu$ such that $s(A)<\mu<\lambda_{O}, f \in E_{+}, \phi \in E_{+}^{\prime}$ then
(1.3) $\langle R(\mu, A) f, \phi\rangle=\sum_{n=0}^{\infty}\left(\lambda_{0}-\mu\right)^{n}\left\langle R\left(\lambda_{O}, A\right)^{n+1} f, \phi\right\rangle=$
$=\sum_{n=0}^{\infty} \int_{0}^{\infty} \frac{1}{n!}\left(\left(\lambda_{0}-\mu\right) s\right)^{n} \exp \left(-\lambda_{o} s\right)<T(s) f, \phi>d s=$
$=\int_{0}^{\infty} \sum_{n=0}^{\infty} \frac{1}{n!}\left(\left(\lambda_{o}-\mu\right) s\right)^{n} \exp \left(-\lambda_{o} s\right)<T(s) f, \phi>d s=$
$=\int_{0}^{\infty} \exp \left(\left(\lambda_{0}-\mu\right) s\right) \exp \left(-\lambda_{0} s\right)<T(s) f, \phi>d s=$
$=\int_{0}^{\infty} \exp (-\mu s)\left\langle T(s) f, \phi>d s=1 i m_{t \rightarrow \infty}<\int_{0}^{t} \exp (-\mu s) T(s) f d s, \phi\right\rangle$
Note that one can interchange sumation and integration because all the integrands are positive functions.
It follows from (1.3) that the net ( $\left.\int_{0}^{r} \exp (-\mu s) T(s) f d s\right) r \geq 0$ converges weakly to $R(\mu, A) f$ for $r \rightarrow \infty$. Because it is monotone increasing (f $z 0$ ), we have strong convergence (see the corollary to II.Thm.5.9 in Schaefer (1974)).

If $\lambda=\mu+i v$ with $\mu, v$ real and $\mu>e\{A)$ we have for arbitrary $f \in E, \phi \in E^{\prime}:$
$\left|<\int_{r}^{t} e^{-\lambda s} T(s) f d s, \phi\right\rangle\left|\leqq \int_{r}^{t} e^{-\mu s}<T(s)\right| f|,|\phi|>d s \quad$ hence
$\left\|<\int_{r}^{t} e^{-\lambda s} T(s) f d s\right\| \leqq\left\|\int_{r}^{t} e^{-\mu s} T(s)|f| d s\right\| \quad$ which shows that
$\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s) f d s \quad$ exists.
Thus $R(\lambda, A) f=\int_{0}^{\infty} e^{-\lambda s} T(s) f d s$ by $A-I, P r o p .1 .11$.
It remains to prove that the net $\left.\int_{0}^{r} \exp (-\mu s) T(s) d s\right) r \geq 0$ converges with respect to the operator norm. We fix $k$ such that
$s(A)<\mu<\operatorname{Re} \lambda$. As we have seen above the map $s \rightarrow e^{-\mu s<T(s) f, \phi\rangle \text { is }, ~}$ Lebesgue integrable for every $(f, \phi) \in E \times E \cdot$, thus defining a bilinear map $\left.b: E \times E^{\prime} \rightarrow L^{1}(\mathbb{R})_{+}\right)$. Using the closed graph theorem it is easy to see that $b$ is separately continuous, hence jointly continuous by [Schaefer (1966), III.Thm.5.1.]. Thus there is a constant $M$ such that
(1.4) $\quad \int_{0}^{\infty} e^{-\mu s}|\langle T(s) f, \phi\rangle| d s=\|b(f, \phi)\| \leq M\|f\|_{i}^{\prime}\|\phi\| \quad\left(f \in E, \phi \in E^{\prime}\right)$

Given $0 \leq t<r$ and setting $E:=$ Re $\lambda-\mu$ we have:
$\left|\int_{t}^{r} e^{-\lambda s}\langle T(s) f, \phi\rangle d s\right| \leq \int_{t}^{r} \exp (-(\operatorname{Re\lambda }-\mu) s) e^{-\lambda s}|\langle T(s) f, \phi\rangle| d s$
$s e^{-\varepsilon t_{t} r} e^{-\lambda s}|<T(s) f, \phi\rangle \mid d s \leq e^{-E t} M\|f\|\| \| \|$.
It follows that $\left\|\int_{t}^{r} e^{-\lambda s} T(s) d s\right\|_{j} \leqq M e^{-\varepsilon t}$, hence
$\left(\int_{0}^{t} e^{-\lambda s} T(s) d s\right) t \geqslant 0$ is a Cauchy net with respect to the operator norm.

Theorem 1.2 has many consequences. In particular, we can conclude that $s(A) \in \sigma(A)$ whenever $s(A)>-\infty$ (without using the analogous result for bounded operators, cf. Cor.l.4 belowl. In each of the following corollaries we assume that $A$ is the generator of a positive semigroup $(T(t)){ }_{t \geqslant 0}$ on a Banach lattice $E$.

Corollary 1.3. If $\operatorname{Re} \lambda>s(A)$ then we have
(1.5) $|R(\lambda, A) f| \leqslant R(\operatorname{Re} \lambda, A)|f| \quad(f \in E)$.

The proof is an immediate consequence of Thm.1.2.

Corollary 1.4. We have $s(A) \in o(A)$ unless $s(A)=-\infty$.

Proof. Assume that $s(A)>-\infty$ and $s(A) \notin(A)$, then it follows from (1.5) that $\{R(\lambda, A): \operatorname{Re} \lambda>s(A)\}$ is uniformiy bounded in $L(E)$,
by $M$ say. Then $\{z \in \mathbb{C}: \operatorname{Re} z=s(A)\} \in p(A)$ and $\|R(z, A)\| \leq M$ for $z$ with $\operatorname{Re} z=s(A)$. It follows that $\left\{z \in \mathbb{C}:|\operatorname{Re} z-s(A)|<M^{-1}\right\}$ $\subseteq \rho(A)$, which is absurd by the definition of $s(A)$.

Corollary 1.5. Suppose that $s(A)$ is a pole of order $m$ of the resolvent $R(\lambda, A)$. Then $m$ is a majorant for the order of any other pole on the line $s(A)+i \mathbb{R}$.

Proof. Without loss of generality we may assume that $s(A)=0$. By (1.5) we have $\|R(E+i \beta, A)\| \in R(E, A) \|$ for every $B \in \mathbb{R} \| \in>0$, Therefore $\lim _{E \rightarrow 0}\left\|_{\mathrm{E}}^{\mathrm{k}} \mathrm{R}(E+i \beta, A)\right\| \leq \lim _{\varepsilon \rightarrow 0} \|_{i} k_{R}(E, A)\{=0$ for $k>m$.

The spectrum of a positive semigroup may be empty (see B-III, Ex.1.2(a)) and the spectrum of a general group may be empty as well (see [Hille-Phillips (1957), Sec.23.16i). However, for positive groups this cannot occur. More precisely, we have the following result:

Corollary I.6. If $A$ is the generator of a positive group then $\sigma(A) \cap R \neq \phi$.

Proof. Both $A$ and $-A$ are generators of positive semigroups, hence if $\sigma(A)=\emptyset$, then $s(A)=s(-A)=-\infty$ and (1.5) implies that $\{R(\lambda, A): \operatorname{Re} \lambda \geqq 0\} \quad L\{R(\lambda,-A): \operatorname{Re} \lambda \geqq 0\}$ is bounded in $[(E)$, i.e., $\{R(\lambda, A): \lambda \in C\} \quad i s$ bounded. By Liouville's Theorem the function $\lambda \rightarrow R(\lambda, A)$ is constant, hence identically zero because ]imation $R(\lambda, A)=0$. Thus we arrive at a contradiction.

We conclude this section by indicating possible extensions and further consequences of the results stated above.

Remarks 1.7.(a) Many of the results of this section remain true for positive semigroups on ordered Banach spaces more general than Banach Iattices. The interested reader is referred to Greiner-Voigt-Wolff (1981)
(b) From Thm. 1.2 one can easily deduce that for positive semigroups on $L^{1}$-spaces, spectral bound and growth bound coincide. To prove the analoguous result for $L^{2}$-spaces one makes use of cor.1.3. For details we refer to $\mathrm{C}-\mathrm{IV}, \mathrm{Thm} .1 .1$.

## 2. THE BOUNDARY SPECTRUM

In Chapter B-III we have seen that under suitable assumptions the boundary spectrum $\sigma_{b}(A)$, which consists of all spectral values with maximal real part, is a cyclic set $\left\{\begin{array}{c}\text { f.f. } B-I I I, ~ D e f .2 .5) . ~ I n ~ t h e ~ m a i n ~\end{array}\right.$ theorem of this section we prove a result which is more general and which is true for arbitrary Banach lattices.
We first want to extend some of the notions used in B-III to the more general setting considered here. If $E$ is a Banach Jattice and $f, g \in E$ such that $g \in E|f|$, then (sign f)g is well-defined (cf. Sec. 8 of $C-I$ ). Thus the following definition makes sense:

Definition 2.1. If $E$ is a Banach lattice then for $f \in E$, $\in \mathbb{Z}$ we define $f^{[n]}$ recursively as follows:

$$
\mathrm{f}^{[0]}:=|\mathrm{f}|
$$

$$
\begin{align*}
& f^{[n]}:=(\operatorname{sign} f) f^{[n-1]}  \tag{2.1}\\
& f^{[n]}:=(\operatorname{sign} \bar{f}) f^{[n+1]} \\
& \text { if } n>0 \\
& n<0
\end{align*}
$$

Obviously, for $E=C_{0}(X)$ this amounts to the same as B-III, Def.2.2. Moreover, in case $E$ is an $L^{P}$-space, then $f^{[n]}$ is the function given $b_{Y}$

$$
f^{\lceil n]}(x)=\left\{\begin{array}{cc}
(f(x) / \mid f(x)!\}^{n-1} f(x) & \text { if } f(x) \neq 0  \tag{2,2}\\
0 & \text { otherwise }
\end{array}\right.
$$

The following properties are immediate consequences of Def. 2.1 :
(2.3) $f^{[0]}=|f|, f^{[1]}=f, f^{[-1]}=\overline{\mathrm{f}},\left|f^{[n]}\right|=|f| \quad\left(\begin{array}{ll}n \in \mathbb{Z}\end{array}\right)$
(2.4) $f^{[n]}=(\operatorname{sign} f) f^{[n-1]}=(\operatorname{sign} \bar{f}) f^{[n+1]}$ for all $n \in \mathbb{Z}$;
(2.5) (af) $[n]-\alpha(\alpha /|\alpha|)^{n-1} f^{[n]}$ for $n \in \mathbb{Z}, \alpha \in \mathbb{E}, a \neq 0$.

Next we show that B-III, Thm. 2.4 is true for arbitrary Banach lattices. For defintion and simple properties of the signum operator $S_{h}$ see C-I, sec. 8.

Theorem 2.2. Let $(T(t))_{t \geqslant 0}$ be a positive semigroup on a Banach lattice $E$ with generator $A$ and suppose that for $h \in E$, $\alpha, \beta \in i k$ we have
(2.6) $A h=(\alpha+i \beta) h, A|h|=\alpha|h|$.

Then the following holds true:
(2.7) $\mathrm{Ah}^{[n]}=(\alpha+i n \beta) h^{[n]}$ for all $n \in \mathbb{Z}$.

In case $|h|$ is a quasi-interior point of $E_{+}$, then $s_{h} D(A)=D(A)$ and $A+i \beta \neq S_{h}^{-1} A S_{h}$.

Proof. Without loss of generality we may assume that $a=0$.
Then the assumption (2.6) implies that $T(t)|h|=|h|$ and
$T(t) h=e^{i \beta t} h$ for $t \geqq 0$ (see $\left.A-I I I, C o r .6 .4\right)$. In particular, the principal ideal $E_{|h|}$ is invariant under every operator $T(t)$. By the Kakutani-Krein Theorem (C-I,Sec.4) we can identify $E|h|$ with a space $C(K), K$ compact. Then the restrictions $\tilde{T}(t):=T(t)|E| h \mid$ are positive operators on $C(K)$ satisfying $\tilde{T}(t) ; \tilde{h}\left|=|\widetilde{h}|\right.$ and $\tilde{T}(t) \tilde{h}=e^{i \beta t} \tilde{h}$. From B-III,Thm.2.4(a) we conclude $\tilde{T}(t) \tilde{h}^{[n]}=e^{i \beta t} \tilde{h}^{[n]}$ for $a 11$ $t \geq 0, n \in \mathbb{Z}$. Translating this back to $\mathbb{T}(t)$ and $E$ this means precisely $T(t) h^{[n]}=e^{i n \beta_{h}[n]} \quad(n \in \mathbb{Z})$, hence $h^{[n]} \in D(A)$ and $A h^{[n]}=\operatorname{inqh}^{[n]}$.
Moreover, by B-III,Thm. $2.4(a)$ we have $e^{i \beta t_{\tilde{T} f}(t)}=s_{\tilde{h}}^{-1 \tilde{T}(t) S_{\tilde{h}}}$. If |h| is a quasi-interior point this relation extends by continuity from the dense subspace ${ }^{E}|h|$ to the whole space $E$, i.e., we have $e^{i \beta t} T(t)=s_{h}^{-1} T(t) s_{h}$ for all $t \geq 0$.

In the proof above we could not apply assertion (b) of B-III, Thm.2.4 because the semigroup $(\tilde{T}(t))$ on $E|h| \cong C(K)$ need not be strongly continuous with respect to the sup-norm.
As a first application of Thm.2.2 we prove a cyclicity result for the point spectrum of contraction semigroups on a class of Banach lattices which includes the $\mathrm{L}^{\mathrm{P}}$-spaces.

Corollary 2.3. Suppose $E$ is a Banach lattice such that the norm is strictly monotone on $E_{+}$(i.e., $\left.0 \leqq f<g \quad=>\|f\|_{i} \leqslant \|\right)$.
If ( $T(t)$ ) is a positive contraction semigroup with $s(A)=0$, then $P_{\sigma_{b}}(A)=P o(A) \quad \cap$ ik is imaginary additively cyclic.

Proof. Suppose that $A h=i \beta h\{\beta \in \mathbb{R}, h \in E)$. Then we have $T(t) h=$ $e^{i \beta t_{h}}(t \geqq 0)$ and $|h|=|T(t) h| \leqslant T(t)|h|$ since $T(t)$ is positive. Moreover, $\|h\| \leqq\|T(t)|h|\| \leqq\|h\|$ since $\|T(t)\| \leq 1$. The assumption on the norm of $E$ implies that $T(t)|h|=|h|$ for all $t \geqq 0$, equivalent1y $A|h|=0$. Now we can apply $T h m .2 .2$ in order to obtain the desired result.

A more general result on cyclicity of the eigenvalues in the boundary spectrum will be proved in sect. 4 (see Cor.4.3). In the remaining part of this section we focus our interest on the entire boundary spectrum. We will prove that it is cyclic provided that the resolvent $R(\lambda, A)$ does not grow too fast as $\lambda+s(A)$. We start with some preparations. An important tool in the proof are pseudo-resolvents.

Definition 2.4. Let $D$ be an open (non-empty) subset of $\mathbb{C}$ and let $G$ be a Banach space. A mapping $R$ : $D+L(G)$ which satisfies
$(2.8) \quad R(\lambda)-R(\mu)=-(\lambda-\mu) R(\lambda) R(\mu) \quad(\lambda, \mu \in D)$
is called a pseudo-resolvent on $G$.

An equivalent (often quite useful) version of (2.8) is the following:
(2.9) (1-( $1-\mu) R(\lambda))(1-(\mu-\lambda) R(\mu))=1 \quad(\lambda, \mu \in D)$

Obviously, the resolvent of a closed linear operator $A$ on $G$ is a pseudo-resolvent on $D=p(A)$. In general a pseudo-resolvent need not be the resolvent of an operator. Further information can be found in Hille-Phillips (1957), Pazy \{1983) or Yosida (1974). For our purposes the following examples are of particular interest:

Example 2.5. (a) Suppose $A$ is a densely defined linear operator on $G$ with $\rho(A) \neq \emptyset$ and let $G_{F}$ be an F-product of $G(c f . A-I, 3.6)$. Then the canonical extensions $R(\lambda, A) F$ of $R(\lambda, A)$ form a pseudoresolvent $R_{F}$ on $G_{F}$ with $\rho(A)$ as domain of definition. If $A$ is unbounded, then $0 \in A o(R(\lambda, A))$ hence $0 \in P_{0}\left(R_{F}(\lambda, A)\right)$ (cf. A-III, 4.5). It follows that $R_{F}$ is not the resolvent of an operator on $G$. (b) If $\{R(\lambda)\}_{\lambda \in D}$ is a pseudo-resolvent on $G$, then $\left\{R(\lambda)^{\prime}\right)_{\lambda \in D}$ is a pseudo-resolvent on $G^{r}$. Moreover, if $H$ is a closed linear subspace of $G$ which is $\{R(\lambda)\}, D_{G}$-invariant $(R(\lambda) H \subset H$ for all $\lambda \in D)$, then the operators on $H$ and $G_{H}$ induced by $R(\lambda)$ in the canonical way form a pseudo-resolvent on $H$ and ${ }^{G} / H$ respectively.

In the following we list several simple properties. We assume that $R: D \quad L(G)$ is a pseudo-resolvent on a Banach space $G$.
(2.10) Given $\lambda_{0} \in D, \mu \in \mathbb{C}$ there exists at most one operator $S \in L(G)$ such that
$R\left(\lambda_{0}\right)-S=-\left(\lambda_{0}-\mu\right) R\left(\lambda_{0}\right) S=-\left(\lambda_{0}-\mu\right) S R\left(\lambda_{0}\right)$.
In case such an operator exists we have $R(\lambda)-S=-(\lambda-\mu) R(\lambda) S=-(\lambda-\mu) S R(\lambda)$ for all $\lambda \in D$
(2.11) Given $\lambda_{O} \in D$ then for $\mu \in D$ with $\left|\mu-\lambda_{o}\right|<\left\|R\left(\lambda_{o}\right)\right\|^{-1}$ we have $R(\mu)=\sum_{n=0}^{\infty}\left(\lambda_{o}-\mu\right)^{n} R\left(\lambda_{0}\right)^{n+1}$
(2.12) $\lambda \rightarrow R(\lambda)$ is a locally holomorphic function defined on $D \subseteq \mathbb{C}$ with values in $L(G)$.

We only sketch the proof of these assertions: (2.12) follows from (2.11) and the latter is a consequence of (2.10). The identity stated in (2.10) can be rewritten as follows:
$\left(1-\left(\lambda_{0}-\mu\right) R\left(\lambda_{0}\right)\right)\left(1-\left(\mu-\lambda_{0}\right) S\right)=1=\left(1-\left(\mu-\lambda_{O}\right) S\right)\left(1-\left(\lambda_{0}-\mu\right) R\left(\lambda_{0}\right)\right)$ Thus $S=\left(\mu-\lambda_{O}\right)^{-1}\left(1-\left(I-\left(\lambda_{\circ}-\mu\right) R\left(\lambda_{O}\right)\right)^{-1}\right)$ has to be unique.
It follows from (2.11) and (2.12) that every pseudo-resolvent has a unique maximal estension.
Further properties of pseudo-resovents are given in the following two propositions.

Proposition 2.6. Suppose $G$ is a Banach space, $D \subseteq \mathbb{C}$ and $R: D+L(G)$ is a pseudo-resolvent.
(a) Given $a \in C, x \in G$ one has $(\lambda-\alpha) R(\lambda) x=x$ either for all $\lambda \in D$ or for none.
(b) Suppose $\mu \in \bar{D} \backslash \bar{D}$. Then $R$ can be extended to an open set containing $\mu$ if and only if there exists a sequence $\left(\lambda_{n}\right) \subset D$ converging to $\mu$ such that $\left\|R\left(\lambda_{n}\right)\right\|$ is bounded.

Proof. (a) Suppose that $(\lambda-\alpha) R(\lambda) x=x$ for some fixed $\lambda \in D, x \in G$. Then using (2.8) we have for $\mu \in D:(\mu-\lambda) R(\mu) x=(\lambda-\alpha)(\mu-\lambda) R(\mu) R(\lambda) x$ $=(\lambda-\alpha)(R(\lambda) x-R(\mu) x)=x-(\lambda-\alpha) R(\mu) x$.
It follows that $(\mu-\alpha) R(\mu) x=x$ for all $\mu \in D$.
(b) If there exists an extension, then $\left\|R\left(\lambda_{n}\right)\right\|$ is bounded for every sequence $\left(\lambda_{n}\right)$ converging to $\mu$ by (2.12). On the other hand assuming that $\left\|R\left(\lambda_{n}\right)\right\|$ is bounded by $M$ for a fixed sequence $\left(\lambda_{n}\right) \in D$ with $\lambda_{n} \rightarrow \mu(M \leq 0)$, we have
$\left\|R\left(\lambda_{n}\right)-R\left(\lambda_{m}\right)\right\|=\left|\lambda_{n}-\lambda_{m}\right|\left\|R\left(\lambda_{n}\right) R\left(\lambda_{m}\right)\right\| \leqq M^{2}\left|\lambda_{n}-\lambda_{m}\right|$
which shows that $\left(R\left(\lambda_{n}\right)\right)$ is a Cauchy sequence in $L(G)$, hence $S:=1 m_{n+\infty} R\left(\lambda_{n}\right)$ exists. The assertion now follows from (2.10) and (2.11) .

In the next proposition we consider a positive pseudo-resolvent $R$ on a Banach lattice $E$; i.e.. we assume that the domain $D$ of $R$ contains the positive real axis and that $R(\mu)$ is a positive operator for every $\mu>0$. Applying Pringsheim's Theorem (see Thm. 2.1 in the appen-
dix of Schaefer (1966)) to the expansion given in (2.11) one can conclude that $R$ has an extension to the halfplane $\{z \in \mathbb{E}: \operatorname{Re} z>0\}$. This shows that without loss of generality one can assume that the domain of a positive pseudo-resolvent contains the halfplane $\{z \in \mathbb{C}$ : $\operatorname{Re} \mathrm{z}>0$.

Proposition 2.7. Suppose $R: A \rightarrow$ (E) is a positive pseudo-resolvent on a Banach lattice $E$ and $A:=\{z \in \mathbb{C}: \operatorname{Re} z>0\}$. If for some $\xi \in \mathbb{R}, h \in E$ we have
$\lambda_{R}(\lambda+i \beta) h=h$ and $\lambda_{R}(\lambda)|h|=|h| \quad(\lambda \in A)$, then $\lambda R(\lambda+i n \beta) h^{[n]}=h^{[n]}$ for all $n \in \mathbb{Z}, \lambda \in A$.

Proof. At first we prove the following domination property which is the extension of (1.5) to pseudo-resolvents.
(2.13) $|R(\lambda) f| \leqslant R(R e \lambda)|f|$ for every $\lambda \in A, f \in E$.

To do this we fix $\lambda \in \Delta$. Then there exists $r_{0}>0$ such that $|r-\lambda|<r$ whenever $r>r_{o}$. Therefore $R(\lambda)=\sum_{n=0}^{\infty}(r-\lambda)^{n}{ }_{R(r)}^{n+1}$ for $r>r_{o}$, which implies for $f \in E$
$|R(\lambda) f| \leqq \sum_{n=0}^{\infty}|r-\lambda|^{n_{R}(r)^{n+1}|f|=\sum_{n=0}^{\infty}(r-(r-|r-\lambda|))^{n} R(r)^{n+1}|f|}$
$=R(r-|\lambda-r|)|f|$. Since $\lim _{r \rightarrow \infty}(r-|\lambda-r|)=\operatorname{Re} \lambda$, we obtain (2.13). As a consequence of (2.13) and the assumption $r R(r)|h|=|h|$ we have that the principal ideal $E|h|$ is $\{R(\lambda)\}_{\lambda \in A}$-invariant. Identifying, according to the Kakutani-Krein Theorem $E|h|$ with a space $C(K), K$ compact, and by restricting the operators $R(\lambda)$ to $E|h| \cong C(K)$ we obtain a positive pseudo-resolvent $\widetilde{R}: A \rightarrow L(C(K))$. Then we have for every $a>0$ and $f \in E$ :
$\alpha \widetilde{R}(\alpha+i \beta) h=h \quad, \quad \alpha \tilde{R}(\alpha)|h|=|h|=1_{K}, \alpha|\tilde{R}(\alpha+i \beta) f| \leqq \alpha \tilde{R}(\alpha)|f|$.
Applying $B-I I I$, Lema 2.3 we obtain $\tilde{R}(\alpha)=S_{\hat{h}}-\mathcal{I}_{\tilde{R}}(\alpha+i \neq) S_{\hat{h}}$ for every a $>0$ and using the uniqueness theorem for holomorphic functions we get $\tilde{\mathrm{R}}(z)=S_{\tilde{h}}-1_{\tilde{R}}(z+i \beta) S_{\tilde{h}}$ for every $z \in \Delta$. Iterating this identity we obtain:
(2.14) $\hat{R}(z)=S_{\tilde{h}}^{-n}{ }^{-n}(z+i n \beta) S_{\tilde{h}}^{n}$ for all $z \in A, n \in \neq$

In particular, $S_{\tilde{h}}^{n}|h|=S_{h}^{-n} z \widetilde{R}(z)|h|=z \tilde{R}(z+i n \beta) S_{\bar{h}}^{n}\left|h_{h}\right|$.
In temms of the initial space this means precisely
$h^{[n]}=z R(z+i n \beta) h^{[n]}$, and the propositon is proved.

We will prove cyclicity of the boundary spectrum under a growth condition which is stated in the following definition.

Definition 2.8. Let $A$ be the generator of a positive semigroup (T(t)) tı0 with spectral bound $s(A)>-\infty$. The resolvent is said to grow slowly if one of the following (equivalent) conditions is satisfied:
(2.15a) $\{(\lambda-s(A)) R(\lambda, A): \lambda>S(A)\}$ is bounded in $[(E)$.
$(2.15 b) \quad\left\{\frac{1}{t} \int_{0}^{t} \exp (-\tau s(A)) T(\tau) d \tau: t>0\right\}$ is bounded in $L(E)$.

Before proving the equivalence of the two assertions we make some remarks.
(a) Since one always has $\lambda R(\lambda, A) \rightarrow$ Id for $\lambda \rightarrow \infty$ $\{(\lambda-s(A)) R(\lambda, A): \lambda>s(A)+E\}$ is bounded for every $E>0$. Thus in (2.15a) the essential fact is boundedness near $s(A)$. On the other hand, $\left\{\frac{1}{t} \int_{0}^{t} \exp (-\tau s(A)) T(\tau) d \tau: 0 \leqq t \leqq T\right\}$ is bounded for every $T \geq 0$, hence in (2.15b) the boundedness for $t \rightarrow \infty$ is important.
(b) By Cor.1.4 we have $\|R(\lambda, A)\| \geqq r(R(\lambda, A))=(\lambda-s(A))^{-1}$. Hence $\|R(\lambda, A)\|$ grows at least as fast as $(\lambda-s(A))^{-1}$. Thus if (2.15a) is satisfied the resolvent grows as slowly as it possibly can for $\lambda+s(A)$.
(c) We do not assume in Def.2.8 that spectral bound and growth bound coincide. A slight modification of $A-I I I$ Example 1.3 shows that there are semigroups with slowly growing resolvent and $s(A)<w(A)$.

To prove equivalence of (2.15a) and (2.15b) we assume $s(A)=0$ and write $c(t):=\frac{1}{t} \int_{0}^{t} T(\tau) d t$.
$(2.15 a) \rightarrow(2.15 b):$ Consider $\lambda>0, t>0$ such that $\lambda t=1$.
Then we have

$$
\lambda \cdot \exp (-\lambda s) \geqslant\left\{\begin{array}{cc}
(e t)^{-1} & \text { if } s \leqq t \\
0 & \text { if } s>t
\end{array}\right.
$$

Now (1.1) implies $\lambda R(\lambda, A)=\int_{0}^{\infty} \lambda \exp (-\lambda s) T(s) d s \geq e^{-1} C(t)=e^{-1} \cdot C\left(\frac{1}{\lambda}\right)$ $\geq 0$. Thus $C(t)$ is bounded for $t+\infty$ whenever $\lambda R(\lambda, A)$ is bounded for $\lambda \neq 0$.
$(2.15 b) \rightarrow(2.15 a): \operatorname{Let} M:=\sup \{\|C(t)\|: t>0\}$. Given $f \in E$, $\lambda>0, r>0$ then integration by parts yields :
$\lambda \int_{0}^{r} e^{-\lambda s} T(s) f d s=\lambda e^{-\lambda r} \int_{0}^{r} T(\sigma) f d \sigma+\lambda^{2} \int_{0}^{r} s e^{-\lambda s}\left(\frac{1}{s} \int_{0}^{s} T(\sigma) f d \sigma\right) d s$ It follows that $\left\|\lambda \int_{0}^{r} e^{-\lambda s} T(s) f d s\right\| \leq\left(r \lambda e^{-r}+\lambda^{2} \int_{0}^{r} s e^{-\lambda s} d s\right) M\|f\|_{1}$
$=\left(1-e^{-\lambda r}\right) M\|f\|$. Letting $r \rightarrow \infty$ we obtain by (1.1) $\|\lambda R(\lambda, A) f\| \leqq M\|f\| \quad(f \in E, \lambda>0)$ hence $\|\lambda R(\lambda, A)\| \leqq M$

Two sufficient conditions for a resolvent to grow slowly are stated in the following proposition. Its simple proof is omitted.

Proposition 2.9. Suppose $(T(t))_{t \geq 0}$ is a positive semigroup with generator A. Each of the following conditions guarantees that the resolvent grows slowly.
(a) $(T(t))_{t \geq 0}$ is bounded and $s(A)=0$;
(b) $s(A)$ is a first order pole of the resolvent.

In case $s(A)$ is a pole of order greater than 1 , the resolvent does not grow slowly. We will treat this case in Cor.2.12.

Theorem 2.10. The boundary spectrum of a positive semigroup with slowly growing resolvent is cyclic.

Proof. Without loss of generality we can assume that $s(A)=0$. Given $i \beta \in \alpha(A)(B \in R)$, then $i \beta \in A \sigma(A)$ ( $A-I I I, P r o p, 2.2)$ and $(\lambda-i \beta)^{-1} \in \operatorname{Ao}(\mathrm{R}(\lambda, A))(A-I I I, P r o p .2 .5)$. We consider an F-product $E_{F}$ of $E$ and for convenience write $E_{1}$ instead of $E_{F}$. The canonical extensions of $R(\lambda, A)$ to $E_{1}$ form a positive pseudo-resolvent $\left\{\left(R_{1}(\lambda)\right\}_{R e} \lambda>0\right.$ on $E_{1}$. $B_{Y}$ Prop.2.6(a) and $A-I I I, 4.5$ there exists $h_{1} \in E_{1}, h_{1} \neq 0$ such that
(2.16) $\quad \lambda R_{1}(\lambda+i \beta) h_{1}=h_{1}$ for $\operatorname{Re} \lambda>0$.

By (2.13) we have

$$
\begin{equation*}
\left|h_{1}\right|=\left|r R_{1}(r+i \beta) h_{1}\right| \leqq r R_{1}(r)\left|h_{1}\right| \quad(r>0) . \tag{2.17}
\end{equation*}
$$

Next we choose any $\phi \in E_{1}{ }^{\prime}$ such that $\left\langle h_{1}, \phi\right\rangle \neq 0$. Since $\left\|R_{1}(\lambda)\right\|_{i}=$ $\left\|R_{1}(\lambda)\right\|=\|R(\lambda, A)\|$, the assumption of slow growth implies that $\left\{\lambda R_{1}(\lambda) \prime|\phi|: \lambda>0\right\}$ is bounded in $E_{1}{ }^{\prime}$, hence $\sigma\left(E_{1}{ }^{\prime}, E_{1}\right)$-relatively compact by AlaogIu's Theorem. Thus there exist
$\phi_{1} \in \cap_{e>0}\left\{r_{1}(r) \cdot|\phi|: 0<r<\varepsilon\right\}^{-\sigma}$.
Using the resolvent equation (2.8) we get for $r>0, \varepsilon>0$ :
$\left(1-r R_{1}(r)^{\prime}\right) \varepsilon R_{1}(\varepsilon)^{\prime}|\phi|=\varepsilon(r-\varepsilon)^{-1}\left(r R_{1}(r)^{\prime}|\phi|-\left.\varepsilon R_{1}(\varepsilon)^{\prime}\right|_{\phi} \mid\right)$.
since the right hand side tends to 0 as $\varepsilon \rightarrow 0$, we have (1-rR $\left.R_{1}(r)^{\prime}\right) \phi_{1}=0$ or
(2.18) $\quad \lambda R_{I}(\lambda)^{\prime} \phi_{1}=\phi_{1} \quad(\operatorname{Re\lambda }>0)$.

Moreover, from $0<\left|\left\langle h_{1}, \phi\right\rangle\right| \leqq\langle | h_{1}|,|\phi|\rangle \leqslant\left\langle r R_{1}(r)\right| h_{I}|,|\phi|\rangle=$ $<\left|h_{1}\right|, r R_{1}(r)^{+}|\phi|>\quad$ it follows that
(2.19) $\langle | h_{1}\left|, \phi_{1}\right\rangle>0$.

For arbitrary $f_{1} \in E_{1}$, Re $\lambda>0$ we have $<\left|R_{1}(\lambda) f_{1}\right|, \phi_{1}>$ $\left.<R_{1}(\operatorname{Re} \lambda)\left|f_{1}\right|, \phi_{1}\right\rangle^{\prime}=\langle | f_{1}\left|, R_{1}(\operatorname{Re} \lambda)^{\prime} \phi_{1}\right\rangle=(\operatorname{Re} \lambda)^{-1}\langle | f_{1}\left|, \phi_{1}\right\rangle$.
Therefore the ideal $I:=\left\{f_{1} \in E_{1}:\langle | f_{1}\left|, \phi_{1}\right\rangle=0\right\}$ is invariant under $\quad\left(\mathcal{R}_{1}(\lambda)\right\}_{\text {Re } \lambda>0}$. Furthermore we have (see (2.17), (2.18)), $\langle | r R_{1}(r)\left|h_{1}\right|-\left|h_{1}\right|\left|, \phi_{1}\right\rangle=\left\langle r R_{1}(r)\right| h_{1}\left|-\left|h_{1}\right|, \phi_{1}\right\rangle$ $=\langle | h_{1}\left|, r R_{1}(r)^{\prime} \phi_{1}-\phi_{1}\right\rangle=0$ for $r>0$
which implies

$$
\begin{equation*}
r R_{1}(r)\left|h_{1}\right|-\left|h_{1}\right| \in I \quad(r>0) \tag{2,20}
\end{equation*}
$$

Denoting by $E_{2}$ the quotient space $E_{1} / I$ and by $\left\{\left(R_{2}(\lambda)\right\}_{\text {Re } \lambda>0}\right.$ the pseudo-resolvent on $E_{2}$ induced by $\left\{\left(R_{1}(\lambda)\right\}_{\text {Re } \lambda>0}\right.$ in the canonical way, then $h_{2}:=h_{1}+I \neq 0$ (by (2.19)). Moreover, $\lambda R_{2}(\lambda+i \beta) h_{2}=h_{2}$ (by (2.16) and $\lambda R_{2}(\lambda)\left|h_{2}\right|=\left|h_{2}\right|$ (by (2.20) and prop.2.6(a)). Now we apply Prop. 2.7 (b) and obtain

$$
\begin{equation*}
\lambda R_{2}\left(\lambda+i n_{\beta}\right) h_{2}^{[n]}=h_{2}^{[n]} \text { for } \operatorname{Re} \lambda>0, n \in \mathbb{Z} . \tag{2.21}
\end{equation*}
$$

In particular, we have $\left\|R_{2}(r+i n \beta)\right\|_{i}^{i} \frac{1}{r}$, thus $\|R(r+i n \beta, A)\|=\left\|R_{1}(r+i n \beta)\right\| \geqslant \| R_{2}(r+i n \beta) \geqslant \frac{1}{r}$ for $r>0$. This finally implies that in $\in \sigma(A)$ for $n \in \mathbb{Z}$.

To prove cyclicity of the boundary spectrum in case s(A) is a pole (of arbitrary order) one applies $B-I I I, L e m m a 2.8$ to reduce the problem to the case of first order poles. Actually, B-III, Lemma 2.8 is true for arbitrary Banach lattices and the proof given in chapter B-III works in the general case as well. For completeness we recall this result.

Proposition 2.11. Let $A$ be the generator of a positive semigroup $T$ on a Banach lattice $E$ and suppose that the spectral bound $s(A)$ is a pole of the resolvent of order $k$. Then there is a sequence (2.22)

$$
I_{-1}:=\{0\}=I_{0} \varsubsetneqq I_{1} \varsubsetneqq \ldots I_{k}:=E
$$

of $T$-invariant closed ideals with the following properties:
If $A_{n}$ is the generator of the semigroup induced by $T$ on the quotient $I_{n} / I_{n-1}$, then we have
(a) $s\left(A_{0}\right)<s(A) ;$
(b) If $n \geq 1$ then $s\left(A_{n}\right)=s(A)$ is a first order pole of the resolvent $R\left(., A_{n}\right)$. The corresponding residue is a strictly positive operator.

Combining Thm,2.10 and Prop.2.11 one obtains the following generalization of $B-I I I, T h m .2 .9$. Tn contrast with the former result we do not assume that every point of ${ }_{0}(A)$ is a pole.

Corollary 2.12. If A is the generator of a positive semigroup such that $s(A)$ is a pole of the resolvent then $g_{b}(A)$ is cyclic.

Proof. Considering the sequence of ideals as described in Prop. 2.11 and the corresponding generators $A_{n}(0 \leqq n \leqslant k)$, then we have by $A$-III, $\operatorname{Prop} .4 .2 \quad \sigma_{b}(A)=i_{n=1}^{k} \quad \sigma_{b}\left(A_{n}\right)$.
By Thm. 2.10 each set ${ }_{0}{ }_{b}\left(A_{n}\right)$ is cyclic hence so is ${ }_{0}{ }_{b}(A)$.

The proof of the preceding corollary indicates a possible generalization of Thm.2.10. Instead of assuming that the resolvent grows slowly one merely needs that there exist a finite chain of closed T-invariant ideals as described in (2.22) such that the semigroups induced on the corresponding quotient spaces have slowly growing resolvents.

Knowing that $\sigma_{b}(A)$ is cyclic one has the alternative (cf. B-III, (2.19) ):

Either $\sigma_{b}(A)=\{s(A)\}$ or else $a_{b}(A)$ is an unbounded set.
Obviously one can use this fact to prove the existence of a dominant spectral value (cf. the explanation preceding B-III,Cor.2.11). We give a typical example.

Corollary 2.13. Let $A$ be the generator of a positive, eventually norm-continuous semigroup. Suppose either that the resolvent grows slowly or that $s(A)$ is a pole of the resolvent. Then $s(A)$ is a dominant spectral value.

Proof. The boundary spectrum $\sigma_{b}(A)$ is cyclic (Thm. 2.10 and Cor. 2.12 resp.) and compact (A-II,Thm.1.20). Hence $\sigma_{b}(A)=\{s(A)\}$.

A situation in which Cor. 2.13 can be applied is described in the folIowing example. For more details and proofs we refer to Amann (1983)

Example 2.14. Let $a$ be a bounded domain in $\mathbb{R}^{n}$ of class $c^{2}$. Assume that $a \Omega=F_{o}^{L i} 1$ where $F_{o}$ and $F_{1}$ are disjoint open and
closed subsets of $3 \Omega$. on $E=L^{P}(\Omega)(1 \approx p<\infty)$ we consider a differential operator $L_{p, 0}$ which is defined as follows:
(2.23) $L_{p, 0} f:=\sum_{i, j=1}^{n} a_{i j} f_{i j}^{\prime}+\sum_{i=1}^{n} b_{i} f_{i}^{\prime}+c f$, with domain
$D\left(L_{p, 0}\right):=\left\{f \in c^{2}(\bar{a}): f(x)=0 \quad\right.$ for $x \in \Gamma_{0}$ and

$$
\left.\partial f / \partial v(x)+\gamma(x) f(x)=0 \quad \text { for } x \in \Gamma_{1}\right\}
$$

Here $f i$ stands for $\partial f / \partial x_{i}$, thus $f_{i j}^{i}=\partial^{2} f / \partial x_{i} \partial H_{j}$. We assume that $L_{p, o}$ is elliptic and that all coefficients are real-valued satisfying $a_{i j} \in C^{2}(\bar{\Omega}), b_{i} \in C^{1}(\bar{\Omega}), \gamma \in C^{1}(\bar{\Omega}), C \in C^{1}(\bar{\Omega})$.
Then $L_{p, o}$ is closable and its closure $L_{p}$ is the generator of a holomorphic semigroup of positive operators. Moreover, the resolvent is compact. Thus cor. 2.13 is applicable and one obtains that $s(A)$ is strictly dominant provided that $\sigma(A) \neq \emptyset$. Using the results of Section 3 one can show that $\sigma(A) \neq \varnothing$ and that $s(A)$ is an algebraically simple eigenvalue (see Thm. 3.7 and Prop.3.5).

We conclude with some remarks.

Remarks 2.15. (a) In the proof of Thm. 2.10 we did not use the assumption that $R$ is the resolvent of a semigroup. In fact one can state this theorem for closed operators having positive resolvent. In this case one has to assume that $\{(\lambda-s(A)) R(\lambda, A): s(A)<\lambda<s(A)+1\}$ is bounded in $L(E)$.
One can go even further and consider positive pseudo-resolvents $\{R(\lambda)\}_{\lambda \in D}$. This is also possible with respect to Cor. 2.12 .
(b) If $s(A)$ is a pole, then the criteria stated in B-III, Rem. 2.15 (a) for $s(A)$ to be a first order pole are valid in the setting of arbitrary Banach lattices as well. In particular, one has a first order pole provided that ker (s $(A)$ - A) contains a quasi-interior point or in case that ker (s (A) - A') contains a strictly positive Iinear form.
(c) It is not difficult to give examples of semigroups whose resolvent does not grow slowly or cannot be reduced by a finite chain of invariant ideals as described after cor. 2.12 . E.g., one can take a bounded positive operator $A$ which is not nilpotent and satifies $\sigma(A)=\{0\}$. However, the following question is still unanswered:

[^0]
## 3. IRREDUCIBLE SEMIGROUPS

The concept of irreducibility is very natural in the general setting of Banach lattices. However, some of the (equivalent) assertions stated in B-III, Def. 3.1 do not ma e sense here, others need a slightiy different formulation.

Definition 3.1. A positive semigroup ( $T(t))_{t \geqslant 0}$ on a Banach lattice $E$ with generator $A$ is called irreducible if one of the following (mutually equivalent) conditions is satified:
(i) There is no (T(t))-invariant closed ideal except $\{0\}$ and $\mathbf{E}$.
(ii) Given $f \in E, \phi \in E^{\prime}$ such that $f>0, \phi>0$ then $\left\langle T\left(t_{0}\right) f, \phi \gg 0\right.$ for some $t_{0} \& 0$.
(iii) For arbitrary $f, g \in E_{+}, f>0, g>0$ there exists $t_{o}$ such that inffT(tof frg\} $>0$.
(iv) For some (every) $\lambda>s(A)$ there is no closed ideal other than (0) or $E$ which is invariant under $R(\lambda, A)$.
(v) For some (every) $\lambda>\mathrm{s}(\mathrm{A})$ we have:
$R(\lambda, A) f$ is a quasi-interior point of $E_{+}$whenever $f>0$.

Equivalence of the five conditions above is obtained by a slight modification of the arguments given in B-III, Def. 3.1. since there are no difficulties we mit a detailed proof. obviously, a semigroup is irreducible if one single operator $T\left(t_{0}\right)$ is irreducible. In general the converse does not hold (see p. 65 in Greiner (1982)). The situation is different when holomorphic semigroups are considered. Then an even stronger assertion holds: In fact irreducibility of a holomorhic semigroup implies that every single operator maps the positive elements onto quasi-interior points. This is the second statement of the following theorem (see also B-III, Rem. 3.2).

Theorem 3.2.(a) If (T(t)) $t \geqq 0$ is an irreducible semigroup then every operator $T(t)$ is strictly positive.
I.e., given $f>0, t \geqq 0$, then $T(t) f>0$.
(b) Suppose (T(t)) $t \geqq 0$ is a holomorphic positive semigroup.

If (T(t)) is irreducible then $T(t) f$ is a quasi-interior point of $E_{+}$whenever $f>0$ and $t>0$. Equivalently, given $f \in E$, $\in \in E^{\prime}$ such that $f>0, \phi>0$, then $\langle T(t) f, \phi\rangle>0$ for all $t>0$.

Proof. (a) Given $t>0$ and $f>0$ such that $T(t) f=0$ and $\lambda>s(A)$ then we have $T(t)(R(\lambda, A) f)=R(\lambda, A) T(t) f=0$. since $R(\lambda, A) f$ is a quasi-interior point it follows that $T(t)=0$. Thus for fixed $t \in \mathbb{R}_{+}$we have either $T(t)$ is strictly positive or else $T(t)=0$. Then strong continuity and $T(0)=I \neq 0$ implies that there exists $\tau \quad>0$ such that $T(t)$ is strictly positive for $0 \leq t \leq T$. For arbitrary $t \in \mathbb{V}_{+}$we find $n \in \mathbb{N}$ such that $\frac{t}{n} \leq T$. Then $T(t)=T\left(\frac{t}{n}\right)^{n}$ is also strictly positive.
(b) We will prove that for an arbitrary holonorphic positive semigroup (T(t)) t; 0 the following holds:

Given $f>0, \phi>0$ then either $\langle T(t) f, \phi\rangle=0$ for $a 11 \quad t \geq 0$ or $\langle T(\mathrm{t}) \mathrm{f}, \phi\rangle>0$ for all $t>0$.
Then it follows from Def. $3.1(i i)$ that for irreducible semigroups always the second case occurs.
Assume that $\left\langle T\left(t_{0}\right) f, \phi\right\rangle=0$ for some $t_{0}>0$.
We consider a null sequence $\left(t_{n}\right), 0<t_{n}<t_{o}$ such that
$\left\|T\left(t_{n}\right) f-f\right\| \leq 2^{-n}$ and define $f_{n}:=T\left(t_{n}\right) f, g_{n}:=f-\sum_{k=n}^{m}\left(f-f_{k}\right)^{+}$. Then we have $g_{p} \leqq f, f=\lim _{n \rightarrow \infty} g_{n}$ and for $m \geqq n$ :
$g_{n} \leq f-\left(f-f f_{m}\right)^{+}=\inf \left\{f, f(f) \leqq f_{m}\right.$.
For $n \in \mathbb{N}$ fixed and $m \geq n$ we obtain
$0 \leq\left\langle T\left(t_{0}-t_{m}\right) g_{n}+\phi\right\rangle \leq\left\langle T\left(t_{0}-t_{m}\right) f_{m}, \phi\right\rangle=\left\langle T\left(t_{0}\right) f, \phi\right\rangle=0$.
Thus the function $t \rightarrow\left\langle T(t) g_{n}{ }^{+}, \phi\right\rangle$ is identically zero by the uniqueness theorem for analytic functions. since $f=\lim _{n \rightarrow \infty} g_{n}{ }^{+}$we have $\langle T(t) h, \phi\rangle=0$ for all $t \in \mathbb{R}_{+}$.

The next result can be used to check irreducibility for a semigroup whose generator is a bounded perturbation of a known semigroup. It is a generalization (and an extension to Banach lattices) of B-III, Prop. 3.3.

Proposition 3.3. Suppose that $A$ is the generator of a positive semigroup $T$, further assume that $K$ is a bounded positive operator and $M$ is a bounded real multiplier (cf. C-I, Sec.8). Let $S$ be the semigroup generated by $B:=A+K+M$.
For a closed ideal $I \subset E$ the following assertions are equivalent:
(i) I is S-invariant.
(ii) I is invariant both under $T$ and $K$.

Proof. We recall that a closed subspace $I=E$ is invariant for a semigroup generated by $C$ if and only if $C(D(C) \cap I)=I$ and the restriction $C_{\mid I}$ of $C$ with domain $D_{\mid}:=D(C) \cap I$ generates a semi-
group on $I$ (see $A-1,3,2$ ). Now let $I$ be a closed ideal of E. (ii) $\rightarrow$ (i). If $I$ is T-invariant then $\left.A\right|_{I}$ generates a semigroup on $I$. The restrictions $K \mid I$ and $M \mid I \quad O f \quad K$ and $M$ respectively are bounded linear operators on $I$. (Note that each closed ideal is
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-17.jpg?height=64&width=1615&top_left_y=502&top_left_x=232) with domain $D(A \mid I)=D(A) \| I=D(B) \cap I$ is the generator of a semigroup on I . It follows that $I$ is invariant for the semigroup generated by B.
(i) $+(i i)$. Without Loss of generality we assume $M \geq 0$. Then we have $0 \leq T(t) \leq S(t)$ for all $t \geqslant 0$. It follows that $I$ is T-invariant. Thus for $x \in D(A) \cap I=D(B) \cap I$ we have $K x=B x-A x-M x$. This shows that $K(D(B) \cap I) \subset I$. Since $B / I$ is a generator $D(B) \cap I$ is dense in I . Then by continuity we have $K I \subset I$; i.e., I is K-invariant.

Next we consider some concrete examples.

Examples 3.4. (a) Suppose that on $E=L^{P}(\mu)(1 \leqslant p<\infty)$ the semigroup (T(t)) $1 s$ given by

$$
\begin{equation*}
(T(t) f)(x)=\int_{X} k(t, x, y) f(y) d_{\mu}(y) \quad(x \in X, t>0) \tag{3.1}
\end{equation*}
$$

for some measurable function $k: \mathbb{R}_{+} \times x \times X \rightarrow \mathbb{F}_{+}=$ Then (T(t)) is irreducible if and only if for any two measurable sets $M$ and $N$ with $0<\mu(M)<\infty, 0<\mu(N)<\infty, \mu(M / N)=0$ there exist $t_{O}>0$ such that $\int_{M} \int_{\mathbb{N}} k\left(t_{O}, x, y\right) d_{\mu}(x) d_{\mu}(y)>0$
(b) Consider the first derivative on $\mathbb{R}, \mathbb{R}_{+}$or $\mathbb{R}_{2 \pi} \cong \mathbb{F}$ as operator on the corresponding $L^{p}$-space (with respect to the Eebesgue measure.) Then the statements made in B-III, Ex. 3.4 (c) are true. The same is true for B-III, Ex. $3.5(\mathrm{e})$ and (f) (second order differential operator) when the corresponding $L^{P}$-spaces are considered.
(c) Let $E=L^{1}[-1,0]$ and for $g \in L^{\infty}$ consider the operator $A_{g}$ given by

$$
\begin{equation*}
A_{g} f:=f, D\left(A_{g}\right):=\left\{f \in W^{1}[-1,0]: f(0)=\int_{-1}^{0} f(x) g(x) d x\right\} \tag{3.2}
\end{equation*}
$$

If $g \geqq 0$ then $A_{g}$ generates a positive semigroup. In case there exist $E>0$ such that $g$ vanishes a.e. on $[-1,-1+\varepsilon]$, then $I:=\left\{f \in L^{l}: f_{[r-1+\varepsilon, 0}[=0\}\right.$ is a non-trivial closed ideal which is invariant under the semigroup. It is not difficult to see that the condition on $g$ stated above is also necessary for (T(t)) to be reducible (i.e., not irreducible.)
(d) Let $E=L^{1}([0,1] \times[-1,17)$ and consider the semigroup (T(t))tz0 defined as follows:
(3.3) $(T(t) f)(x, v):=\left\{\begin{array}{cl}f(x-v t, v) & \text { for } 0 \leqq x-v t \leqq 1 \\ 0 & \text { otherwise }\end{array}\right.$
(T(t)) $t \geqslant 0$ is a positive semigroup on $E$ and
$D_{O}:=\left\{f \in C^{1}\left([0,1] \times[-1,1 \mathrm{i}): f(0, v)=f_{i t}(0, v)=0 \quad i f \quad v \geqq 0\right.\right.$, $f(1, v)=f_{X}(1, v)=0$ if $\left.v \leqq 0 \quad\right\}$
is a core for its generator $A$ (cf. A-I, Cor.1.34). We have

$$
\begin{equation*}
\text { (Af) }(x, v)=-v \cdot \frac{\partial f}{\partial x}(x, v) \quad\left(f \in D_{o}\right) \tag{3.4}
\end{equation*}
$$

The Laplace transform of (T(t)) is the resolvent of A An explicit calculation yields:
(3.5) (R( $\lambda, A) f(x, v)=\int_{0}^{1} r_{\lambda}\left(x, x^{t}, v\right) f\left(x^{\prime}, v\right) d x^{\prime} \quad(\lambda>0)$

$$
\text { where } r_{\lambda}:[0,1] \times[0,1] \times[-1,1] \rightarrow \mathbb{R} \text { is given by }
$$ $r_{\lambda}\left(x, x^{\prime}, v\right)=\left\{\begin{array}{cl}|v|^{-1} \exp \left(-\lambda\left(x-x^{\prime}\right) v^{-1}\right) & \text { if either } v>0 \text { and } x^{+} \leq x \\ \text { or } v<0 \text { and } x^{\prime} \exists x ; \\ 0 & \text { otherwise. }\end{array}\right.$

Let $\sigma:[0,1] \times[-1,1] \rightarrow \mathbb{R}_{+}$and $\kappa$ : $[0,1] \times[-1,1] \times[-1,1] \rightarrow \mathbb{R}_{+}$be measurable functions and consider the operators $M$ and $K$ given by (3.6) Mf $:=\sigma f, \quad \mathrm{Kf}:=\int_{-1}^{1} k\left(\ldots, v^{\prime}\right) f\left(\ldots v^{i}\right) d v^{\prime}$.

Then $B:=A-M+K$ with domain $D(B):=D(A)$ is the generator of a positive semigroup.
Using Prop. 3. 3 we can prove the following irreducibility criterion for the semigroup ( $S(t))_{t \geq 0}$ generated by $B$ :
(3.7) If $\kappa$ is strictly positive then (s( $t$ ) tz0 is irreducible.

Actually, in view of Prop. 3.3 we have to show that a closed ideal which is invariant under $R(\lambda, A)$ and $K$ has to be $\{0\}$ or $E$.

We recall that closed ideals of $E$ are uniquely determined $u p$ to sets of measure zero) by measurable subsets $Y$ of $[0,1] \times[-1,1]$; i.e., every closed ideal has the form
$I_{Y}=\{f \in E: f$ vanishes (a.e.) on $[0,1] \times[-1,1$.$] Y\}.$
Since we assumed that $k$ is strictly positive, $I_{Y}$ is K-invariant if and only if $Y=X \times[-1,1]$ for some measurable set $X \subset[0,1.1$. If we assume that $X$ has positive measure and define $\alpha:=\sup \{x \in[0,1]$ : $\left.\int_{0}^{x} 1_{X}(s) d s=0\right\}$ and $\beta:=\inf \left\{x \in[0,1]: \int_{X}^{1} l_{X}(s) d s=0\right.$ then we have $\alpha<\beta$ and the support of the function $h:=R(\lambda, A) 1_{Y}$
( $\mathrm{Y}:=\mathrm{X} \times[-1,1]$ ) is given by supp $h=[0,1] \times[0,1] \cup[0, \beta] \times[-1,0]$. Since we assumed that $I_{Y}$ is $R(\lambda, A)$-invariant we have $h \in I_{Y}$, i.e., $\operatorname{supp} h=Y=X \times[-1,1]$. Obviously, this is true only if $Y=[0,1] \times[-1,1] \quad$ or $\quad I_{Y}=E$. A weaker condition than (3.7) entailing irreducibility is the following.
(3.8) There exists $\delta>0$ such that $\kappa$ is strictly positive on the sets $[0, \delta] \times[-1,1]$ and $[1-\delta, 1] \times[-1,1]$.

For details we refer to Greiner (1984d).

In the following proposition we list some properties which are consequences of irreducibility, This extends B-III, Prop. 3.5 to the setting of Banach lattices. The first assertion of the latter proposition is no longer true in the general setting (see Ex.3.6 and Thm.3.7).

Proposition 3.5. Suppose A is the generator of an irreducible, positive semigroup on a Banach lattice $E$. Then the following assertions are true:
(a) Every positive eigenvector of $A$ is a quasi-interior point.
(b) Every positive eigenvector of $A^{\prime}$ is strictly positive.
(c) If $\operatorname{ker}\left(s(A)-A^{\prime}\right)$ contains a positive element, then $\operatorname{dim}(\operatorname{ker}(s(A)-A)) \leqq I$.
(d) If $s(A)$ is a pole of the resolvent, then it has algebraic (and geometric) multiplicity 1 .
The corresponding residue has the form $P=\phi$, where $\phi \in E^{\prime}$ is a positive eigenvector of $A^{\prime}, u \in E$ is a positive eigenvector of $A$ and $\langle u, \phi\rangle=1$.

Proof. To prove (a), (b) and (d) one can proceed as in the case $C_{o}(X)$ (see B-III, Prop. 3.5). We only prove (c) and assume $s(A)=0$. By assumption and by assertion (a) there exists $q 300$ such that $T(t){ }^{\prime} \phi=\phi(t \geqslant 0)$. Given $f \in \operatorname{ker} A$ then $T(t) f=f$ hence $|f|=$ $|T(t) f| \leqq T(t)|f|$. Since $\phi$ is strictly positive and $\langle | f|, \phi\rangle \leqslant\langle T(t)| f|, \phi\rangle=\langle | f|, \phi\rangle$ it follows that $|f|=T(t)|f|$. We have shown that ker $A$ is a sublattice. Then for $f \in$ ker $A, f$ real, i.e., $f=\overline{\mathbf{f}}$, we have that $f^{+}$and $f^{-}$are elements of ker $A$. Hence the principal ideals generated by $f^{+}$and $f^{-}$are T-invariant. Since these ideals are orthogonal the irreducibility of $T$ implies that either $\mathrm{f}^{+}$or $\mathrm{f}^{-}$is zero.

We have shown that ker $A \cap E_{\mathbb{R}}$ is totally ordered, hence at most onedimensional (see Prop, 3.4 of Schaefer (1974)).

In arbitrary Banach lattices it is no longer true that an irreducible semigroup has necessarily nonvoid spectrum. We indicate how an irreducible semigroup having empty spectrum can be constructed.

Example 3.6. Consider the Banach lattice $E=L^{P}(F \times \Gamma)$. For (fixed) positive numers $\alpha, \beta$ such that $\frac{\alpha}{\beta}$ is irrational we define a positive semigroup $\left(T_{0}(t)\right) t \geq 0$ as follows:

$$
\begin{equation*}
\left(T_{0}(t) f\right)(z, w):=f\left(z \cdot e^{i \alpha t}, w \cdot e^{i \beta t}\right) \quad(z, w \in F=\{\xi \in \mathbb{C}:|\xi|=1\}) \tag{3.9}
\end{equation*}
$$

Next we define for a positive function $m: \Gamma \times F \rightarrow \mathbb{R}$ which is continuous on $\Gamma \times \Gamma(1,1)$ functions $m_{t}, t \geq 0$, as follows:

$$
\begin{equation*}
m_{t}(z, w):=\exp \left(-\int_{0}^{t} m\left(z \cdot e^{i \alpha s}, w \cdot e^{i \notin s}\right) d s\right) \tag{3.10}
\end{equation*}
$$

Then (T(t)) $t \geq 0$ defined by
(3.11) $T(t) f:=m_{t} \cdot\left(T_{o}(t) f\right)$
is a strongly continuous semigroup of positive contractions on E. Since $\frac{\alpha}{\beta}$ is irrational the semigroup $\left(T_{o}(t)\right)$ is irreducible. Moreover, each $m_{t}$ is strictly positive (i.e.. $m_{t}>0$ a.e.) thus (T(t)) is irreducible as well. If one chooses min such that m(z,w) tends to $+\infty$ sufficiently fast as $(\mathrm{z}, \mathrm{w}) \rightarrow(1,1)$, one can get
$\|T(t)\|_{i}=\left\|m_{t}\right\|_{\infty} \leqq \exp \left(-t^{2}\right)$ for all $t \geq 0$.
obviously such an estimate of $\|T(t)\|$ implies $w(A)=-\infty$, hence $\sigma(A)=\varnothing$.

In the following theorem we collect some hypotheses which in combination with irreducibility guarantee that $\sigma(A) \neq \phi$. For the sake of completeness we include B-III,Prop.3.5(a).

Theorem 3.7. Suppose that $(T(t))_{t \geq 0}$ is an irreducible, positive semigroup on the Banach lattice $E$. Each of the following conditions on $E$ and $(T(t))$, respectively, implies that $\sigma(A) \neq \phi$.
(a) $E=C_{0}(X)$ where $X$ is locally compact;
(b) $E=\mathbb{e}^{P} \quad(1 \leq p<\infty)$ (more generally, $E$ contains atoms);
(c) either $T\left(t_{0}\right)$ is compact for some $t_{o}$ or $R\left(\lambda_{o}, A\right)$ is compact for some $\lambda_{0} \in p(A) ;$
(d) $E$ has order continuous norm and either $T\left(t_{0}\right)$ or $R\left(\lambda_{o}, A\right)$ is a kernel operator for some $t_{o} \geqq 0\left(\lambda_{0} \in p(A)\right)$. (For a precise definition of a kernel operator we refer to Sec.IV. 9 of Schaefer (1974) or Chap. 13 of Zaanen (1983)).
(e) $E$ is reflexive and there exist $t_{o}>0, h \in E_{+}$such that $T\left(t_{o}\right) E \subset E_{h}$;

Proof. (a) is proved in B-III, Prop. 3.5(a).
Assertion (b)-(f) will be proved utilizing the analoguous results for a single operator. In view of $A-I I I, P r o p .2 .5$ we have to show that $r(R(\lambda, A))>0$ for some $\lambda \in p(A)$. Moreover, from $A-I,(3.1)$ we deduce
$T(t) R(\lambda, A)=e^{\lambda t} R(\lambda, A)-e^{\lambda t} \int_{0}^{t} e^{-\lambda s} T(s) d s \leq e^{\lambda t} R(\lambda, A) \quad(t \geqslant 0, \lambda>s(A))$. Since the spectral radius is an isotone function on the cone of positive operators, it is enough to show that

```
(3.12) r(T(t)R(\lambda,A))>0 for some t 2 0, \lambda > s(A).
```

Using Thm. 3.2(a) it is easy to see that $T(t) R(\lambda, A)=R(\lambda, A) T(t)$ is irreducible.

The assertions (b); (d) and (e) now follow from the corresponding results for a single operator as presented in Sect.v. 6 of schaefer (1974) (see Prop.6.1, Thm.6.5 Cor. and Thm.6.5 1.c.). (c) follows from the recent result of de Pagter (1986) which ensures that every positive operator on a Banach lattice which is compact and irreducible has positive spectral radius.

The theorem can be used to prove that elliptic operators as described in Ex. 2.14 have non-empty spectrum. It is shown in Amann (1983) that these operators have compact resolvent and generate irreducible semigroups. Thus the assumption of (c) is satisfied.

Concerning the eigenvalues of an irreducible semigroup which are contained in $\sigma_{b}(A)$ all statements established for spaces $C_{0}(X)$ in B-III.Thm. 3.6 are true in the setting of Banach lattices. The proof can be translated without difficulties and will be omitted (see also [Greiner (1982), Thm.2.6]).

Theorem 3.8. Suppose $T$ is an irreducible semigroup on the Banach lattice $E$ and let $A$ be its generator. Assume that $s(A)=0$ and that there exists a positive linear form $\psi \in D\left(A^{\prime}\right)$ with $A^{\prime} \psi \leqq 0$.

If $P o(A) \cap i \mathbb{R}$ is non-empty, then the following assertions are true:
(a) Po(A) fi尺 is a (additive) subgroup of $i \mathbb{R}$.
(b) The eigenspaces corresponding to $\lambda \in P o(A)$ iliR are onedimensional.
(c) If $A h=i \alpha h(h \neq 0, \alpha \in \mathbb{R})$ then $|h|$ is a quasi-interior point and the following holds:
(3.13) $S_{h}(D(A))=D(A)$ and $S_{h}^{-1} \operatorname{DOD}_{h}=(A+i \alpha)$.
(d) 0 is the only ejgenvalue of $A$ adnitting a positive eigenvector.

One can apply the theorem in order to prove that the rotation semigroup on $F$ (cf. $A-I, 2.5)$ is the only positive periodic somigroup which is irreducible.

Corollary 3.9. Let (T(t)) te0 be a positive irreducible semigroup on a Banach lattice $E$ which is periodic of period $\tau$.

Assume that dim $E=1$. Then there exist
continuous lattice homomorphisms
$i: C(\Gamma)+E$ and $j: E \rightarrow L^{l}(\Gamma)$, both injective with dense range, such that the diagramm commutes for

$$
C(\Gamma) \xrightarrow[i]{ } E \xrightarrow[j]{l} L^{1}(\Gamma)
$$ canonical inclusion of $C(\Gamma)$ in $L^{1}(\Gamma)$.

Proof. By Thm. 3.8 and $A-I I I, T h m .5 .4$ we have $\operatorname{Ro}(A)=\operatorname{Po}(A)=\sigma(A)=$ ioZ with $\alpha:=\frac{2 \pi}{n \tau}$ for suitable $n \in \mathbb{N}$. We fix $h \in k e r(i a-A)$, $h \neq 0$. Then $|h| \in \operatorname{ker} A$ and there exists $\phi \in$ ker $A^{\prime}$ such that $\langle | h \mid, \phi=1$. According to the Kakutani-Krein Theorem we identify $E|h|$ with $C(K)$. Then $h$ is a unimodular function onto $r$ (use the argument given in the proof of B-III, Thm. 3.6(c)).
We define $i=C(\Gamma) \rightarrow E$ by $i(f):=f o h \in C(K) \cong E_{h} \subset E$, then $i$ is injective. For the monomials $e_{n}(z):=z^{n}$ ( $n \in \mathbb{Z}$ ) we have $i\left(e_{n}\right)=h^{[n]}$ thus $i$ has dense image in $E$ (by AuIII,Thm.5.4). Moreover, $2 \pi \cdot \delta_{n 0}=\left\langle h^{[n]}, \phi\right\rangle=\left\langle i\left(e_{n}\right), \phi\right\rangle=\int_{0}^{2 \pi} e_{n}\left(e^{i t}\right) d t$ for all $n \in T$, hence $\int_{0}^{2 \pi} f\left(e^{i t}\right) d t=\langle i(f), \phi\rangle$ for all $f \in C(r)$. It follows that $(E, \phi) \approx L^{1}(\Gamma)$ and we dofine $j$ to be the canonical mapping from $E$ into $(E, \phi)=L^{1}(F)$ (see $\left.C-I, S e c .4\right)$. Then $j$ has dense image and is injective since $\phi$ is strictly positive (cf. Prop. $3.5(b)$ ) One easily verifies that the diagramm commutes.

Now we are going to prove the main result of this section. As in the proof of Thm.2.10 we will utilize pseudo-resolvents on a suitable F-product of the Banach lattice. To simplify the proof we isolate two lemmas.

Lemma 3.10. Let $F$ be a filter on ${ }^{*}$ which is finer than the Frechet filter and let $E_{F}$ be the F-product of the Banach lattice $E$. Given $R \in\left[(E)\right.$ and denoting its canonical extension to $E_{F}$ by $R_{F}$ the following is true:

If $\alpha \in A \sigma(R) \backslash P \sigma(R)$ then $k e r\left(\alpha-R_{F}\right)$ is infinite dimensional.

Proof: Let ( $f_{n}$ ) $n \geqq 1$ be a normalized approximate eigenvector of $R$ corresponding to $a$, since every accumulation point of ( $f_{n}$ ) is an eigenvector of $R$, the assumption $Q \in P o(A)$ implies that ( $f_{n}$ ) does not have any accumulation points. Then there exist an $\varepsilon>0$ and a subsequence $\left(g_{n}\right)$ of ( $\left.f_{n}\right)$ such that (3.14) $\| g_{n}-g_{m} l^{\prime} \geqslant \varepsilon$ whenever $n \neq m$.

Obviously, ( $g_{n}$ ) is a normalized approximate eigenvector of $R$ and so is every subsequence of $\left(g_{n}\right)$. In particular for $k \in \mathbb{N}$ the sequence $\left(g_{n+k}\right){ }_{n \geq 1}$ is a normalized approximate eigenvector of $R$. Then the elements $\hat{g}^{k} \in E_{F}$ given by $\hat{g}^{k}:=\left(\left(g_{n+k}\right)_{n>1}+c_{F}(E)\right)$ are normalized eigenvectors of $R_{F}$ corresponding to $a$. As a consequence of (3.14) we obtain
$\left\|\hat{g}^{k}-\hat{g}^{m}\right\|=F-1 i m$ sup\| $g_{n+k}-g_{n+m} \|^{\prime} \geqq E \quad$ provided that $k \neq m$.
This shows that the unit ball in ker (a - $R_{F}$ ) is not relatively compact, hence ker (a - $R_{F}$ ) has to be infinite dimensional.

Lemma 3.11. Let $E$ be a Banach Iattice and let $M$, L be two linear subspaces of $E$.
Assume that $f \in M$ implies $|f| \in L$, then dimL $\xi$ dimM.

Proof. Let $\left\{g_{1}, g_{2}, \ldots, g_{m}\right\}$ (mel) be any (finite) subset of M which is linearly independent. For $u:=\sum_{n=1}^{m}\left|g_{n}\right|$ all vectors $g_{n}$ are contained in the principal ideal $E_{u}$ which (by the Kakutani-Krein Theorem) is isomorphic to a space $C(K)$. Considering $g_{1}, g_{2}, \ldots$, $g_{m}$ as continuous functions on $K$, there exist points $x_{1}, x_{2}, \ldots$, $x_{m i} \in K$ and functions $h_{1}, h_{2}, \ldots, h_{n t} \in \operatorname{span}\left\{g_{1}, g_{2}, \ldots, g_{m}\right\}$ such that $h_{i}\left(x_{j}\right)=\delta_{i j}$. Then $\left|h_{i}\right|\left(x_{j}\right)=\delta_{i j}$ hence $\left\{\left|h_{j}\right|: 1 \leqq j \leqq m\right\}$
is a subset of $m$ Iinearly independent vectors which (by assumption) is contained in L.

The surprising fact in the following theorem is the conclusion that every point in the boundary spectrum is a simple algebraic pole if only $s(A)$ is supposed to be a pole.

Theorem 3.12. Let $T$ be an irreducible semigroup on a Banach lattice and let $A$ be its generator.
If $s(A)$ is a pole of the resolvent then there existr a $\geq 0$ such that $\sigma_{b}(A)=s(A)+i a \mathbb{Z}$. Moreover, $\sigma_{b}(A)$ contains only algebraically simple poles.

Proof. We will assume that $s(A)=0$. Assuming first that every element of $\sigma_{b}(A)$ is an eigenvalue of $A$ one can conclude as follows: By Thm. 3.8(a) we know that $\sigma_{b}(A)$ is an additive subgroup of i.R . Since it is a closed subset and 0 is an isolated point it follows that $\sigma_{b}(A)=$ iay for some $\alpha \geqslant 0$. Moreover as a consequence of (3.13), for every $k \in \mathbb{Z}$ we obtain

$$
\begin{equation*}
R(\lambda+i k \alpha, A)=S_{h}^{-k} o R(\lambda, A) \cdot s_{h}^{k} \quad(\lambda \in p(A), k \in \mathbb{Z}) . \tag{3.15}
\end{equation*}
$$

By Prop.3.5(d) 0 is an algebraically simple pole. Then (3.15) implies that every point ika has the same property. We now show that every element iß is an eigenvalue of A . By Prop.3.5(d) the residue of $R(., A)$ in $\lambda=0$ has the form $P=\phi 0$ with $\phi(u)=1$. Given an ultrafilter $U$ on $\mathbb{N}$ which is finer than the Frechet filter, then $\lim _{W}$ 中 ( $_{\mathrm{f}}$ ) exists for every bounded sequence ( $f_{n}$ ) $\sim E$. Using this fact $1 t$ is easy to see that the canonical extension $P_{U}$ of $P$ to the $U$-product $E_{U}$ of $E$ has the following form:
(3.16) $p_{u}=\hat{\phi} \hat{\theta} \hat{u} \quad$ where $\hat{u}:=(u, u, u, \ldots)+c_{u}(E) \in E_{U}$ and $\hat{\phi} \in\left(E_{U}\right)^{\prime}$ is given by $\hat{\phi}\left(\left(f_{n}\right)+c_{U}(E)\right):=1 m_{U} \phi\left(f_{n}\right) \quad\left(\left(f_{n}\right)+c_{U}(E) \in E_{U}\right)$.

Given $i \beta \in \sigma_{b}(A)$ then $i \beta \in A_{\sigma}(A)$ hence $1 \in A \sigma(\lambda R(\lambda+i \beta, A))$. Assuming $i \beta \notin \operatorname{Po}(A)$, then $1 \nmid \operatorname{Po}(\lambda R(\lambda+i \beta, A))$. Then Lemma 3.10 implies that $M:=k e r(1-\lambda R(\lambda+i \beta, A)$ is infinite dimensional (and independent of $\lambda$ by Prop. 2. b(a).) For $\hat{f} \in M$ we have
$|\hat{f}|=|\gamma R(\gamma+i \beta, A) \hat{f}| \leqq \gamma R(\gamma, A),|\hat{f}|$ for every $\gamma>0$.
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-24.jpg?height=89&width=1386&top_left_y=2537&top_left_x=209)
Thus considering the closed ideal $I:=\left\{\hat{f} \in E_{U}: \hat{\phi}(|\hat{f}|)=0\right\}$ we have
(3.17) $\hat{\phi}(|\hat{f}|)-|\hat{f}| \in I$ for every $\hat{f} \in M$.

This implies that $M \cap I=\{0\}$. Hence the canonical image $M /$ of $M$ in the quotient space $E_{U} / I$ is infinite dimensional as well. By (3.16) and (3.17) the absolute value of an element $\mathcal{F} \in M$ is a scalar multiple of $\ddot{u}:=\hat{u}+I$. This is a contradiction by Lemma 3.11.

In view of $A-I I I, P r o p .4 .2$ the result above has consequences for semigroups which can be reduced (by considering restrictions to invariant ideals or guotients) to semigroups which satisfy the hypothesis of Thm. 3.12. Semigroups having this property are precisely those for which $s(A)$ is a pole of the resolvent of finite algebraic multiplicity. The latter claim is a consequence of Prop. 2.11 and the following lemma.

Lenna 3.13. Suppose that $T=(T(t))_{t \geq 0}$ is a positive semigroup such that $s(A)$ is a first order pole of the resolvent. Moreover assume that the corresponding residue is a strictly positive operator of finite rank.

Then there are closed (T(t))-invariant ideals $J_{1}, J_{2}, \ldots J_{m}$ which are mutually orthogonal such that the following is true:
(We denote the restriction of $T$ to $T_{k}$ by $T_{k}$ and set $J:=J_{1} \oplus J_{2}{ }^{\oplus} \cdots \oplus \mathrm{J}_{\mathrm{m}}$ )
(a) $T_{k}$ is irreducible and has spectral bound $s(A)$;
(b) $s(A / J)<s(A)$.

Proof. We assume $s(A)=0$. Since $P$ is a strictly positive projection $P E=k e r A$ is a sublattice of $E$. Actually, if $x \in P E$ i.e., $P x=x$, then $P|x| \geqq|P x|=|x|$. Hence $P(|P| x|-|x||)=$
$P^{2}|x|-P|x|=0$ which implies that $P|x|-|x|=0$ or $|x| \in P E$. Thus we know that ker $A$ is a finite dimensional sublattice of $E$ hence it is isomorphic to a space $\mathbb{C}^{m}$ for some $m \in \mathbb{N}$ (see Sec.II. 4 of schaefer (1974)). Then there exist vectors $e_{j} \in E_{+}(1 \leq j \leqq m)$ such that the following holds:
(3.18) ker $A=\operatorname{span}\left\{e_{1} * e_{2}, \ldots, e_{m}\right\}$ and $\inf \left\{e_{i}, e_{j}\right\}=0$ for $i \neq j$.

We have $T(t) e_{k}=e_{k}$ hence the closed ideal generated by $e_{k}$ is
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-25.jpg?height=64&width=1617&top_left_y=2515&top_left_x=214) $J$ is closed (see [Schaefer (1974), III.Thm. 1.2]). T-invariant and we have $P E=$ ker $A \subset J$. Then $P / J=0$ hence the spectral bound $s(A / J)$
is strictly less than zero (by Thm.1.1(a)). Moreover, the residue corresponding to the resolvent of $T_{k}$, we denote it $P_{k}$, is the restriction of $P$ to ${ }^{\top} k$.
$\mathrm{P}_{\mathrm{k}}$ is strictly positive and $\mathrm{P}\left(\mathrm{T}_{\mathrm{k}}\right)=\operatorname{span}\left\{e_{\mathrm{k}}\right\}$. To show that $\mathrm{T}_{\mathrm{k}}$ is irreducible we consider an invariant ideal I . Then we have
$R\left(\lambda, A_{k}\right) I \subset I$ for $\lambda>0$ hence $P_{k}=1 m_{\lambda \rightarrow 0} \lambda R\left(\lambda, A_{k}\right)$ leaves $\quad T$. invariant. If $I \neq\{0\}$ then $P_{k} I \neq\{0\}$ since $P_{k}$ is strictly positive. Then $e_{k} \in P_{k} J \subset I$ which implies that $J_{k} \simeq I$.

Combining the lemma with Prop, 2.11 one obtains the following:
If $s(A)$ is a pole of finite algebraic multiplicity then there exists a finite chain of $T$-invariant ideals $I_{-1}:=\{0\} \subset I_{o} \subset \ldots \in I_{N}:=E$ ( $N \in \mathbb{N}$ ) such that the following is true:
(3.19) For the semigroup $T_{n}$ on $I_{n} / I_{n-1}(0 \leq n \leq N)$ which is induced by $T$ we have either $s\left(A_{n}\right)=s(A)$ and $T_{n}$ is irreducible or $s\left(A_{n}\right)<s(A)$.

The following theorem is an immediate consequence of (3.19), Thm. 3.12 and A-III, Prop.4.2.

Theorem 3.14. Let $T$ be a positive semigroup on a Banach lattice with generator $A$. If $s(A) \quad i s$ a pole of finite algebraic multiplicity then $\sigma_{b}^{(A)}$ is a finite union of discrete subgroups (i.e., $\sigma_{b}(A)=s(A)+L_{k=1}^{N} i a_{k} \boldsymbol{Z} \quad$ with $\left.\alpha_{k} \in R\right)$. Moreover, $\sigma_{b}$ contains only poles of finite algebraic multiplicity.

Here the assumption that the multiplicity of $s(A)$ is finite is essential as can be seen from the following example.

Example 3.15. Consider $x:=\left\lceil 0.17 \times v, V:=\left\{v \in \mathbb{V}: v_{1}<|v|<v_{2}\right\}\right.$ $\left(0<v_{1}<v_{2}<\infty\right)$. The flow in the phase space $x$ which describes the free motion in the interval [0.1.] with velocities in $V$ assuming that the particles are reflected at the endpoints generates a positive semigroup on $L^{P}(X, \mu)$ ( $\mu$ the Lebesgue measure). For the spectrum of the generator $A$ one obtains $\sigma(A)=\left\{i \gamma: n \gamma_{1} \leq|\gamma| \leq n \gamma_{2}\right.$ for some $n \in \mathbb{N}_{0}{ }^{\prime}$ with $\gamma_{1}:=\pi v_{1}^{-1}, \gamma_{2} \neq \pi v_{2}^{-1}$. Moreover, 0 is a first order pole of the resolvent, obviously the only pole in $\sigma_{b}(A)=o(A)$. These statements can be verified by calculating the resolvent explicitely. This can be done using the integral representation. The semi-
group is given as follows :

$$
(T(t) f)(x, y)=\left\{\begin{array}{cc}
f(x-v t+k, v) & i f \quad k-1 \leqslant v t-x \leqq k  \tag{3.20}\\
f(1-(x-v t+k),-v) & \text { and } k \text { even; } k-1 \leqq v t-x \leqslant k \text { and } k \text { odd. }
\end{array}\right.
$$

obviously one can apply Thm. 3.12 and Thm. 3.14 respectively, in order to prove existence of strictly dominant eigenvalues. We consider two typical cases in the following corollaries. The meaning of $r_{\text {egs }}(T(t))$ and $\omega_{e s s}(T)$ is explained in AwIII, 3.7.

Corollary 3.16. Suppose that $T$ is a positive semigroup such that ${ }^{w} \operatorname{ess}^{(T)}<\omega(T)$. Then $s(A)=m(T)$ is a strictly dominant eigenvalue. If in addition there exists an eigenfunction which is a quasi-interior point of $E_{+}$(e.g.. if $T$ is irreducible) then $s(A)$ is a first order pole of $\mathrm{R}(., \mathrm{A})$.

Proof. There exist $\varepsilon>0$ such that for every $t>0$ the set $\{\lambda \in \sigma(T(t)):|\lambda| \geq \exp ((s(A)-\varepsilon) t)\}$ contains only (finitely many) poles of $R(., T(t))$ each being of finite algebraic multiplicity. In view of $A m I I, C o r .6 .5$ the set $\{\lambda \in \sigma(A) ; \operatorname{Re} \lambda>s(A)-E\}$ is finite and contains only poles of $R(., A)$. Thus we can apply Thm.3.14. It follows that $s(A)$ is strictly dominant. For the final assertion we refer to Rem. 2.15 (b).

Corollary 3.17. Suppose that $T$ is an irreducible, eventualy norm continuous semigroup having compact resolvent.
Then $s(A)=w(T)$ is an algebraically simple pole and a strictiy dominant eigenvalue.

Proof. By Thm.3.7(c) we know that $s(A)>-\infty$. Thm. 3.12 is applicable since we assumed that $T$ is irreducible and has compact resolvent. Thus $s(A)$ is an algebraically simple pole and $\sigma_{b}(A)=s(A)+i a \mathbb{Z}$ for some $\alpha \geqslant 0$. In addition $\{\lambda \in \sigma(A)$ : Re $\lambda, 2-1\}$ is compact since $T$ is eventually norm-continuous (see A-II,Thm.1.20). It follows that $s(A)$ is strictly dominant. By A-III, Thm. 6.6 we have $s(A)=\omega(T)$.

In the following proposition we give a condition which ensures that for certain perturbations Thm, 3.14 can be applied. Moreover, we state a criterion ensuring existence of a dominant eigenvalue.

Proposition 3.18. Suppose that $A$ is the generator of a positive semigroup and that $K \in L(E)$ is a positive linear operator.
If $K$ is $A$-compact (i.e., if $K R\left(\lambda_{o}, A\right)$ is compact for some $\lambda_{o} \in(A)$ ) and if $s(A+K) \geqslant s(A)$ then $B:=A+K$ satisfies the assumptions of Thm. 3.14.

If, in addition, $K$ is irreducible then $s(B)$ is a dominant eigenvalue and the semigroup generated by $B$ is irreducible.

Proof. The resolvent equation $R(\lambda, A)=R\left(\lambda_{0}, A\right)\left(1-\left(\lambda-\lambda_{0}\right) R(\lambda, A)\right)$ implies that $K R(\lambda, A)$ is a compact operator for every $\lambda \in \rho(A)$ - For $\lambda>s(A)$ we have $\lambda-B=(1-\operatorname{KR}(\lambda, A))(\lambda-A)$ and $(1-K R(\lambda, A))^{-1}$ exists for $\lambda>s(B)$. Therefore Thm.XIII. 13 of Reed-Simon (1979) implies that $R(\lambda, B)=R(\lambda, A)(1-K R(\lambda, A))^{-1}$ has only poIes of finite
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-28.jpg?height=46&width=1617&top_left_y=1025&top_left_x=205) first claim. In order to prove the second, we denote the semigroup corresponding to $A$ and $B$ by ( $T(t)$ ) and (S(t)) respectively. It follows from Prop. 3.3 that (S(t)) is irreducible and we have $S(t)=T(t)+\int_{0}^{t} T(t-s) K S(s) d s \quad$ (see A-II, (1.9)). Iterating this identity we obtain for every $m \in \mathbb{N}, t \geqq 0:$

$$
\begin{align*}
s(t) & =\sum_{n=0}^{m-1} T_{n}(t)+R_{m}(t) \text { where }  \tag{3.21}\\
T_{0}(t) & :=T(t), T_{n}(t) ; \int_{0}^{t} T(t-s) K T_{n-1}(s) d s \quad(n \in N), \\
R_{m}(t) & :=\int_{0}^{t_{0}} \int_{0}^{t_{1}} \cdots \int_{0}^{t_{m-1}} T\left(t-t_{1}\right) K T\left(t_{1}-t_{2}\right) K \ldots K s\left(t_{m-1}-t_{m}\right) d t_{m} \cdot d t_{1}
\end{align*}
$$

We fix $0<f \in E, 0<\phi \in E^{\prime}, t>0$. By Thm. $3.2(a), S(t) f>0$. Since $K$ is irreducible there exists $m \in \mathbb{N}$ such that $\left\langle K^{I T} S(t) f, \phi\right\rangle>0$. Thus the integrand appearing in the the representation (3.21) of $\left\langle R_{m}(t) f, \phi>\right.$ is non-zero at $t_{1}=t_{2}=\ldots=t_{m-1}=t, t_{m}=t$. Since the integrend is positive and continuous we conclude
(3.22) $\langle S(t) f, \phi\rangle \geqq\left\langle R_{m}(t) f, \phi\right\rangle>0$ for $0<f, 0<\phi, t \geqslant 0$

It follows that $\left(e^{-t s(B)} S(t)\right)_{t \geq 0}$ cannot contain the rotation semigroup on $F$. On the other hand, assuming that $s(B)$ is not dominant, then $\operatorname{dim}\{\operatorname{ker}(\exp (\tau \cdot s(B))-s(\tau)) \geqslant 1$ for some $\tau>0$. Hence the restriction $\left(\left.e^{-t s(B)} S(t)\right|_{F}\right)_{t \geq 0}$ where $F:=\operatorname{ker}(\exp (t * s(B))-s(t))$, contains the rotation semigroup by Cor.3.9.

We conclude this section considering once again Example $3.4(\mathbb{d})$.
The generator considered there is $B=(A-M)+K$, where $K$ is
positive Iinear. From (3.5) and (3.6) one deduces that
$(K R(\lambda, A) f)(x, v)=\int_{0}^{t} \int_{0}^{t} k\left(x, v, x^{\prime}, v^{\prime}\right) f\left(x^{\prime}, v^{\prime}\right) d x^{\prime} d v^{\prime}$
where the kernel $k$ is given by $k\left(x, v, x^{7}, v^{\prime}\right):=k\left(x, v, v^{F}\right) r_{\lambda}\left(x, x^{\prime}, v^{\prime}\right)$ (cf. (3.5), (3.7)). Using this representation of $K R(\lambda, A)$ it follows that $K$ is $A$-compact. Moreover for $\lambda$ sufficiently large one has $R(\lambda, A-M)=R(\lambda, A)\{1-M R(\lambda, A))^{-1}$ which shows that $K$ is also $(A-M)$-compact. In order to apply Thm, 3.14 one needs $s(B)>s(A-M)$ (see Prop.3.17) which is difficult to verify. In case the function $\sigma$ is continuous one can state a sufficient condition as follows:

There exist $r \in \mathbb{R}$ and $g \in L^{1}([0,1] \times[-1,1]), g>0$ such that
$r<\inf \{\sigma(x, 0): x \in[0,1]\}$ and $B g>-r g$.
The additional assumption made in the second part of prop. 3.17 is not satisfied in this example. Nevertheless one can show that $s(B)$ is strictly dominant in this situation (provided that $s(B) \quad s(A))$. For details we refer to Greiner (1984d) or Voigt (1985) where the Iinear transport equation in higher dimensional spaces is discussed.

## 4. SEMIGROUPS OF LATTICE HOMOMORPHISMS

In Section 2 we proved that the boundary spectrum of certain positive semigroups is a cyclic set. For semigroups of lattice homomorphisms much more can be said: The whole spectrum is an imaginary additively cyclic subset of $\mathbb{C}$ (cf. Thm. 4.2 ). This result can be used to derive cyclicity results for the eigenvalues in the boundary spectrum of positive semigroups (cf. Cor. 4.3). In the last part of this section we discuss a spectral decomposition of positive groups (cf. Thm.4.10).

Lemma 4.I. Suppose that $(T(t)) t \geq 0$ is a semigroup of lattice homorphisms on a Banach lattice $E$ with generator A.
In case $i \alpha \in \operatorname{Ro}(A), \alpha \in \mathbb{R}$, then one of the following assertions is true:
(a) $i a \mathbb{Z} r^{-} R(A)$;
(b) $\quad\{\lambda \in \mathbf{C}: \operatorname{Re} \lambda<0\}=\operatorname{Ro}(\mathrm{A})$.

Proof. There exists $\phi \in E^{\prime}, \phi \neq 0$ such that $T(t)^{\prime} \phi=e^{i \alpha t} \phi$ ( $t \geq 0$ ). Then we have $|\phi|=\left|T(t)^{\prime} \phi\right| \leqq T(t)^{\prime}|\phi|(t \geqslant 0)$. If we fix $r>w(T)$ and define $\psi:=r R(r, A) \quad|\phi|$, we have
$(4.1) \quad T(t)^{*} \psi \leqq e^{r t_{\psi}}, T(t)^{\top} \psi \geqq \psi(t \geqq 0)$ and $|\phi| \leqslant \psi$.

In fact, $A-I,(3.1)$ implies $\left(e^{r t}-T(r)\right) R(r, A) \geqslant 0$ hence $T(t)^{r} \psi=r R(r, A)^{\prime} T(t)^{\prime}|\phi| \leqq r+e^{r t} R(r, A)^{\prime}|\phi|=e^{r t} \psi$.
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-30.jpg?height=52&width=1300&top_left_y=391&top_left_x=201) $T(t)^{\prime} \psi=r R(r, A)^{7} T(t)^{\prime}|\phi| \geqslant r R(r, A)^{r}|\phi|=\psi \quad$ and
$\psi=\operatorname{rR}(r, A)^{\prime}|\phi|=r \int_{0}^{\infty} e^{-r t_{T}(t)^{\prime}|\phi| d t \geqslant r \int_{0}^{\infty} e^{-r t}|\phi| d t=|\phi| .}$
Considering the $A L-s p a c e(E, \psi)$ (see $C-I$, sec. 4 ) the first inequality of $(4,1)$ implies that $(T(t)) t \geqslant 0$ induces a strongly continuous semigroup $\left(T_{1}(t)\right)_{t \geq 0}$ on $(E, \psi)$.
That is we have

$$
\begin{equation*}
T_{1}(t) \circ q_{\psi 1}=q_{\psi} \circ T(t) \quad(t \geq 0) \tag{4.2}
\end{equation*}
$$

Denoting by $A_{1}$ the generator of $\left(T_{1}(t)\right)$ we have $\operatorname{Ro}\left(A_{1}\right) \subset \operatorname{Ro}(A)$.
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-30.jpg?height=358&width=412&top_left_y=746&top_left_x=1256)

Indeed, $A_{1}{ }^{*} X=\lambda x$ implies $T_{1}(t)^{\prime} X=e^{\lambda t} X$ hence by (4.2) $T(t)^{\prime} q_{\psi}^{\prime}(x)^{\prime}=e^{\lambda t} q_{\psi}^{\prime}(x)$ or equivalent $y_{Y} A^{*}\left(q_{\psi}^{\prime}(x)\right)=q_{\psi}^{\prime}(x)$ - Thus it remains to show that either $i_{\alpha} Z$ or $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda<0 \quad$ is contained in $\mathrm{R}_{\mathrm{g}}\left(\mathrm{A}_{1}\right)$, obviously, $\left(\mathrm{T}_{1}(\mathrm{t})\right)$ is a semigroup of lattice homomorphisms as well. The second inequality of (4.1) implies

$$
\begin{equation*}
\left\|T_{1}(t) f\right\|_{\psi}=\langle | T_{1}(t) f|, \psi\rangle=\langle | f\left|, T_{1}(t)^{\prime} \psi\right\rangle \geqq\langle | f|, \psi\rangle=\|f\|_{\psi} . \tag{4.3}
\end{equation*}
$$

Then for $\lambda \in \mathbb{C}$ with $\operatorname{Re} \lambda<0$ we have
$\left\|\left(e^{\lambda t}-T_{1}(t)\right) f\right\|_{\psi} \xi\left\|T_{1}(t) f\right\|_{\psi}-\left\|_{i} e_{i t}^{\lambda t} \geqslant \quad\left(1-\left|e^{\lambda t}\right|\right)\right\| f \|_{\psi} \quad(f \in(E, \psi))$
and we obtain for the corresponding generator

$$
\begin{align*}
& \left\|\left(\lambda-A_{1}\right) f\right\|_{\psi}=1 i m t_{t \rightarrow 0}\left\|\frac{1}{t}\left(e^{-\lambda t} T_{1}(t) f-f\right)\right\|_{\psi} \geqq \lim _{t \rightarrow 0} \frac{1}{t}\left(e^{-t \operatorname{Re\lambda }}-1\right)\|f\|_{\psi}  \tag{4.4}\\
& =-\operatorname{Re} \lambda \cdot\| \|_{\psi} \quad \text { for } \operatorname{Re} \lambda<0 \text { and } f \in(E, \psi) .
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-30.jpg?height=61&width=1620&top_left_y=1951&top_left_x=207) and $A \sigma\left(A_{1}\right) \cap\{\lambda \in \mathbb{C}$ : Re $\lambda<0\}=\phi$. Since the toplogical boundary of the spectrum is always contained in the approximate point spectrum (see A-III, Prop.2.2) and $\operatorname{Ro}(T(t)) \backslash(0)=\exp (t R o(A))$ (see $A-I I I$, Thm.6.3), precisely one of the following two cases occurs :
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-30.jpg?height=61&width=1583&top_left_y=2260&top_left_x=219)
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-30.jpg?height=58&width=1605&top_left_y=2318&top_left_x=217)

We mentioned above that $R_{0}\left(A_{1}\right) \subset R_{o}(A)$. Thus we only have to analyze case (A). In this case each operator $T_{1}(t)$ is an invertible lattice homomorphism hence a lattice isomorphism. It follows that $\mathrm{T}_{1}(\mathrm{t})$ ' is a lattice isomorphism as well. The third inequality in (4.1) implies that $\phi$ can be considered as an element of ( $E, \psi)^{\prime}$ and $T(t)^{\prime} \phi=$ $e^{i_{\alpha} t_{\phi}}\left(t_{\geq} 0\right)$ implies $T_{1}(t)^{\prime}{ }_{\phi}=e^{i_{\alpha} t}{ }_{\phi}$. Furthermore, we have
$T_{1}(t)^{\prime}|\phi|=\left|T_{1}(t)^{\prime} \phi\right|=\left|e^{i \phi t}{ }_{\phi}\right|$ or equivalently $A_{1} *|\phi|=0$.
Now we can apply Thm. 2.2 and obtain $\left.i a Z \subset \operatorname{Po}^{\left(A_{1}\right.}{ }^{*}\right)=R o\left(A_{1}\right)$.

Theorem 4.2. Let $A$ be the generator of a semigroup ( $T(t)$ ) $t \geq 0$ of lattice homomorphisms on a Banach lattice $E$. Then $\sigma(A), A \sigma(A)$ and Po (A) are imaginary additively cyclic subsets of $C$.

Proof. We first consider the point spectrum. If $\lambda \in \operatorname{Po}(A)$, $\lambda=a+i \beta(a, \beta \in R)$, then there exists $f \in E, f \neq 0$ such that $A f=\lambda f$. It follows that $T(t) f=e^{\lambda t} f(t \quad 3 \quad 0)$ hence $T(t)|f|=$ $|T(t) f|=e^{\alpha t_{i} f \mid}(t \leq 0)$, or equivalently, $A|f|=a|f|$. Now Thm. 2.2 is applicable and we obtain $A\left(f^{[n]}\right)=(\alpha+i n \beta) f^{[n]}$ for a]! $n \in \mathbb{Z}$.

To prove the assertion for $A o(A)$ we consider an F-product semigroup in order to reduce the problem to the point spectrum. We use the notation of $A-I, 3.6$. Obviously the space m(E) is a Banach lattice and every operator $T(t)$ is a lattice homomorphism. We have $|T(t)| f|-|f||=||T(t) f|-|f|| \leq|T(t) f-f| \quad(f \in E) \quad$ f hence $\left(\left|f_{n}\right|\right) \in m^{\top}(E)$ whenever $\left(f_{n}\right) \in m^{\top}(E)$. This proves that $m^{\top}(E)$ is a sublattice, hence a Banach lattice as well. Obviously, $C_{F}$ (E) $\cap \mathrm{m}^{\top}$ (E) is an order ideal. Thus $E_{F}^{\top}$ is a Banach lattice and ( $T_{F}(t)$ ) is a semigroup of lattice homomorphisms. It follows that Po $\left(A_{F}\right)$ is cyclic hence $A \sigma(A)$ is cyclic by A-III, 4.5 .

Cyclicity of the entire spectrum now follows from the cyclicity of Ao (A) and Lemra 4.1 .

One can use Thm. 4.2 in order to prove cyclicity for the eigenvalues in the boundary spectrum of positive semigroups. We list some typical cases in the following corollary.

Corollary 4.3. Let $T=(T(t))_{t \geq 0}$ be a positive semigroup on a Banach lattice $E$ which is bounded. Each of the following conditions implies that Po(A) nir is imaginary additively cyclic.
(a) E is weakly sequentially complete (e.g. $\left.E=L^{\mathrm{P}}(\mu), 1 \leqslant \mathrm{p}<\infty\right)$;
(b) Every operator $T(t)$ is mean ergodic (i.e. the cesaro means $\frac{1}{n} \sum_{k=0}^{n-1} T(t) \quad$ converge $s t r o n g 1 Y$ as $n \rightarrow \infty$;
(c) There is a strictly positive linear form which is T-invariant.

Proof. We will show that each of the conditions (a), (b) , (c) implies that ker (1 - $T(s)$ ) is a Banach lattice (not necessarily a sublattice of E) for every $s \geqslant 0$. Then one argues as follows: Given $i \alpha \in \operatorname{Po}(A), \alpha \in \mathbb{R}$ then $T(t) g=e^{i a t} g$ for suitable $g \neq 0$. For $\tau==2 \pi|a|^{-1}$ we have $g \in F=\operatorname{ker}(1-T(\tau))$. Then the restriction $\left(T(t) \perp F^{\prime}\right) t \geq 0$ is a $\quad$-periodic positive semigroup on $F$. Since $\left.T(t)\right|^{-1}=T(n \tau-t) \mid$ s 0 it follows that $(T(t) \mid$ ) is a semigroup of lattice isomorphisms. Since $g \in F$ we have io $\in P_{o}(A)$ hence $\operatorname{Ia}_{a} \in \operatorname{Po}(A) \subset \mathrm{Po}_{\mathrm{g}}(\mathrm{A}) \quad$ by Thm. 4.2 .
Now we show that ker (1 - $T(s)$ ) is a vector lattice for the induced order and a Banach lattice for an equivalent norm.
In case (c), ker(l-T(s)) is even a sublattice of $E$. Indeed, assume $T(t){ }^{\prime} \phi=\phi$ and $\phi \gg 0(t \geqslant 0)$ then $T(s) f=f$ implies $T(s)|f| \geqslant|f|$. Thus from $\langle T(s)| f|-|f|, \phi\rangle=\langle | f\left|, T(s)^{r} \phi-\phi\right\rangle=0$ it follows that $T(s)|f|=|f|$.
Now we assume that $E$ is weakly sequentially complete, which is equivalent to (cf. Sec. 5 of C-I):
(4.5) Every increasing norm-bounded net of $E_{+}$converges.

We fix $s>0$ and define $F:=\operatorname{ker}(1-T(s)), T:=T(s)$ obviously $f \in F$ implies $\bar{f} \in F$ hence $F=F \cap E_{R}+i F \cap E_{R}$. Thus we have to show that $F_{R}=F \cap E_{R}$ is a sublattice. Given $f \in F_{R}$ then $T f=f$ hence $|f| \leqq T|f|$. Iterating this inequality we obtain
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-32.jpg?height=75&width=1615&top_left_y=1639&top_left_x=209) exists and we have $T|f|_{o}=\lim _{n \rightarrow \infty} T^{n+1} ;\left.f\left|=|f|_{o}\right.$, i.e. $| f\right|_{O} \in F_{\mathbb{R}}$. For $g \in F_{\mathbb{R}}$ satisfying $4 f \leqslant g$ we have $|f|_{0} \leq g$ thus $|f|_{O}=\sup _{F}\{f,-f\}$. Moreover, $\|f\|_{O}:=\left\||f|_{o}\right\| \quad(f \in f)$ is an equivalent norm on $F$ such that $(F,\|\cdot\|)$ is a Banach lattice.
(b) If $T(s)$ is mean-ergodic then we have ker (1-T(s)) $=P E$ where $P$ is the mean-ergodic projection, i.e. Pf $\left.=\lim _{n \rightarrow \infty} \sum_{k=0}^{n-1} T^{T}\right)^{k} f$. Obviously $P$ is positive, hence II.l1.5 of schaefer (1974) implies that $P E$ is a Banach lattice (for the induced order and an equivalent norm).

The assumptions made in Cor. 4.3 can be weakened slightly (cf. Greiner (1982)). However, one cannot prove cyclicity of $P_{\sigma_{b}}$ (A) for arbitrary positive semigroups.

Example 4.4. At first we recall Ex. 2.13 of Chapter B-III. There we constructed a bounded semigroup on the space $C(\Gamma) \times C_{0}(\mathbb{R})$ such that $\mathrm{Po}_{\mathrm{b}}(\mathrm{A})=\{\mathbf{i k}: k \in \mathbb{Z}, k \neq 0\}$.

Let us perform the same construction on the Hilbert space $H:=L^{2}(\Gamma) \times L^{2}(R)$. For a fixed positive, nonzero function $k \in C_{c}(\mathbb{R})$ we define $T(t)$ on $H$ as follows:

$$
T(t)(f, g)=\left(f_{t}, g_{t}\right) \quad \text { with }
$$

$$
\begin{align*}
& f_{t}(z):=f\left(z * e^{i t}\right) \quad(z \in \Gamma) \text { and }  \tag{4,6}\\
& g_{t}(x):=g(x+t)+\frac{1}{2 \pi} * \int_{0}^{2 \pi} f\left(z \cdot e^{i s}\right) d s \cdot \int_{x}^{x+t} k(u) d u .
\end{align*}
$$

Then $(T(t)) t \geqslant 0$ is a positive semigroup on $H$ and for the spectrum of the generator we obtain olA) $=\mathbf{i R}, \operatorname{Po}(A)=i \mathbb{Z} \backslash\{0\}$. In view of Cor.4.3(a) the semigroup cannot be bounded. (The explicit representtation (4.6) only allows the estimate $\left.\|T(t)\| \leqq \sqrt{2}+t \cdot\|k\|_{2}(t \geq 0).\right)$

In the next proposition we show that for semigroups of lattice homomorphisms on $L^{l}-s p a c e s$ there is a spectral mapping theorem for the real part of the spectrum,

Proposition 4.5. Let $(T(t)) t \geq 0$ be a strongly continuous semigroup of lattice homomorphisms on an $L^{l}$-space and denote by $A$ its generater. Then we have

$$
\begin{equation*}
\exp (t \sigma(A) \cap \mathbb{R})=\sigma(T(t)) \cap(0, \infty) \text { for every } t \geq 0- \tag{4.7}
\end{equation*}
$$

Proof. In view of A-III, 6.2 it is enough to prove that the left hand side contains the set on the right.
Fix $t>0$ and assume $r \in \sigma(T(t)), r>0$ and let $\alpha:=\frac{1}{t} \log r-$ At first we assume $r \in R(\sigma(T(t))$. Then by A-III, Tho. 6.3 there exists $B \in \mathbb{R}$ such that $\alpha+i \beta \in \operatorname{Ro}(A)$. By Lemma 4.1 either $\alpha+i \beta \mathbb{Z} \subset \operatorname{Ro}(A)$ or $\{\lambda \in \mathcal{C}: \operatorname{Re} \lambda<\alpha\}=\operatorname{Rg}_{\mathrm{g}}(\mathrm{A})$. In both cases we have a $\in(\mathrm{A})$.
Now we assume $r \in A_{o}(T(t))$. Then there exists a normalized sequence $\left(f_{n}\right)=E$ such that $\lim _{n \rightarrow \infty}\left\|T(t) f_{n}-r f_{n}\right\|=0$. Since we have $|T(t)| f|-r| f||=||T(t) f|-r| f|| \leq|T(t) f-r f|(f \in E) \quad$ we may assume that $\left(f_{n}\right)$ is a sequence in $E_{+}$.
Defining $g_{n}:=\int_{0}^{t} e^{-a s} T(s) f_{n} d s$ we have $g_{n} \in D(A)$ and $(A-\alpha) g_{n}=(A-\alpha) \int_{0}^{t} e^{-\alpha s_{T}(s) f_{n}} d s=e^{-\alpha t_{T}(t) f_{n}-f_{n}=\frac{1}{r}\left(T(t) f_{n}-r f_{n}\right) .}$
It follows that $1 \lim _{n \rightarrow \infty}\left\|(A-\alpha) g_{n}\right\|=0$ and it remains to show that Imine $n_{n \rightarrow \infty}\left\|g_{n}\right\|>0$. The later assertion is a consequence of the following facts:

- Since $f_{n}$ is positive and the norm is additive on $E_{+}$, we have $\left\|g_{n}\right\|=\int_{0}^{t} e^{-\alpha s}\left\|T(s) f_{n}\right\| d s$.
- The inequality $\|T(t) f\| \leqq\|T(t-s)\|\|(s) f\| \quad$ implies $\|T(s) f\| \geq M^{-1}\|T(t) f\|$ for $0 \leq s \leq t, f \in E$ and $M:=\sup _{0 \leq s \leq t} T(s) \|$.
- Since $\lim n_{n \rightarrow \infty}\left\|T(t) f_{n}-r f_{n}\right\|=0$ anc $\left\|f_{n}\right\|=1$ we have $1 \operatorname{im}_{n \rightarrow \infty} \mid T(t) f_{n} \|_{j}=r>0$.

For semigroups satisfying the assumption of Prop.4.5 o(A) is additively cyclic (by Thm.4.2) and ofT(t)) is multiplicatively cyclic (by Schaefer (1974), V.Thm.4.4). Then the relation (4.7) implies that decompositons of the spectrum by vertical lines allow a spectral decomposition of the semigroup (cf. A-III, Def.3.l). (One simply performs a spectral decomposition of a single operator $T(t)$ ). In the following we will show that for positive groups (on arbitrary Banach lattices) spectral decompositions of this type always exist. Moreover, it will turn out that the decomposition is compatible with the lattice structure. The proof of this result uses Kato's equality (see sec. 5 of C-II). As a consequence of $C-T$, Cor. 5.8 we have the following:

Let $E$ be a Banach lattice with order continuous norm and (T(t)) tef be a group of positive operators on $E$ with generator $A$.
Then the domain $D(A)$ is a sublattice of $E$ and
(4.8) $A \mid f]=\operatorname{Re}[(s i g n$ fiff $]$ for every $f \in D(A)$.

For real $\mu$ one has $\mu|f|=\operatorname{Re}[(\operatorname{sign} \bar{f}) \mu f]$, hence
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-34.jpg?height=47&width=1323&top_left_y=1530&top_left_x=224)
The relations $f^{+}=\frac{1}{2}(f \mid+f) \quad f^{-}=\frac{1}{2}(|f|-f) \quad$ yield
$(\mu-A) f^{+}=\frac{1}{2}((\operatorname{sign} f)(\mu-A) f+(\mu-A) f) \quad$ and
$(\mu-A) f^{-}=\frac{1}{2}((\operatorname{sign} f)(\mu-A) f-(\mu-A) f) \quad$,
in case $f$ is contained in the underlying real Banach lattice $\mathbf{E}_{\mathbb{R}}$. For $\mu \in \rho(A) \cap R$, we can apply $R(\mu, A)$ on both sides and the substitution $f=R(\mu, A) g$ finally leads to

$$
\begin{align*}
& (R(\mu, A) g)^{+}=\frac{1}{2} R(\mu, A)((\operatorname{sign} R(\mu, A) g) g+g) \\
& (R(\mu, A) g)^{-}=\frac{1}{2} R(\mu, A)((\operatorname{sign} R(\mu, A) g) g-g)
\end{align*} \quad \text { for all } g \in E_{\mathbb{R}}+
$$

If we set $g_{1}:=\frac{1}{2},(g+(\operatorname{sign} R(\mu, A) g) g)$ and

$$
g_{2}:=\frac{1}{2} \cdot(g-(\operatorname{sign} R(\mu, A) g) g)
$$

then obviously $g=g_{1}+g_{2}$. Moreover, $g$ is positive if and only if both. $g_{1}$ and $g_{2}$ are positive. We sumtarize these considerations in the following lemma.

Lemma 4.6. Let $A$ be the generator of a positive group on a Banach lattice $E$ which has order continuous norm, Given $\mu \in \rho(A) \cap \mathbb{R}$ then every $g \in E_{R}$ is representable as sum of two elements $g_{1}$ and $g_{2}$ such that
(a) $g \geq 0$ if and only if both $g_{1}$ and $g_{2}$ are positive;
(b) $R(\mu, A) g_{1}=(R(\mu, A) g)^{+}$;
(c) $\quad R(\mu, A) g_{2}=-(R(\mu, A) g)^{-}$.

We need another lema. It can be formulated for arbitrary positive semigroups on Banach lattices.

Lemma 4.7. Let (T(t)) t又0 be a positive semigroup on a Banach lattice $E$ with generator $A$. Given $\mu \in p(A) \cap \mathbb{R}$ and $h \in E_{+}$then the following assertions are equivalent:
(i) $\mathrm{R}(\mu, \mathrm{A}) \mathrm{h} \geqslant 0$;

$$
\begin{equation*}
\left\{\int_{0}^{t} e^{-\mu s} T(s) h d s: t \in \mathbb{R}_{+}\right\} \text {is bounded in } E . \tag{ii}
\end{equation*}
$$

Proof. (i) $\rightarrow$ (ii): We have
$\int_{0}^{t} e^{-\mu s} T(s) h d s=\left(I d-e^{-\mu t} T(t)\right) R(\mu, A) h \quad(s e e A-I,(3.2))$.
Since $R(\mu, A) h \geqq 0$ and $T(t)$ is a positive operator we obtain
$\int_{0}^{t} e^{-\mu s} \mathbf{T}(s) h \mathrm{ds}=\mathrm{R}(\mu, A) \mathrm{h}-\mathrm{e}^{-\mu \mathrm{t}} \mathrm{T}(\mathrm{t}) \mathrm{R}(\mu, A) \mathrm{h} \leq \mathrm{R}(\mu, \mathrm{A}) \mathrm{h}$ which implies assertion (ii).
(ii) $+(i):$ The assumption implies that $\int_{0}^{\infty} e^{-v s} T(s) h \mathrm{ds}:=$ $\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-v s^{\prime}} \mathbf{T}(s) h$ ds exists for $v>\mu$. Using that $A$ is a closed operator it follows that $(v-A)\left(\int_{0}^{\infty} e^{-v S} T(s) h \quad d s\right)=h$. For $v$ sufficiently close to $\mu$ such that $v \in \rho(A) \cap R$ we have $R(v, A) h=$ $\int_{0}^{\infty} e^{-v s} T(s) h d s \geq 0$. By continuity we conclude $R(\mu, A) h \geqq 0$.

By now we are prepared to prove the spectral decomposition for positive groups. Before we formulate the theorem we recall the following consequence of Thm. 4.2 : For any $\mu \in \rho(A)$ IR the line $\mu+i f i$ is a subset of the resolvent set and divides o(A) into disjoint sets. Both sets will be unbounded in general.

Theorem 4.8. Let $\{T(t))_{t \in \mathbb{R}}$ be strongly continuous group of positive operators on a Banach lattice $E$ with order continuous norm.

If $A$ is the generator and $\mu \in p(A) \cap f \quad$ then
$I_{\mu}:=\{f \in E: R(\mu, A)|f| \geq 0\}$ and $J_{\mu}:=\{f \in E: R(\mu, A)|f| \leq 0\}$
are $\left(T(t){ }_{t \in \mathbb{R}^{-i n v a r i a n t ~}}\right.$ profection bands, the direct sum of them
is $E$, and the spectra of the restrictions satisfy
$\sigma\left(A \mid I_{H}\right)=\sigma(A) \cap\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda<\mu\}$,
$\sigma\left(A \mid J_{\mu}\right)=\sigma(A) \cap[\lambda \in C: \operatorname{Re} \lambda \geqslant \mu\}$.

Proof. At first we consider $I_{\mu}$. Obviously it is a closed subset. From Lemma 4.7 we deduce that it is a lattice ideal. Moreover, $I_{\mu}$ is $R(\mu, A)$-invariant and $(T(t)) \in_{t \in \mathbb{R}^{-i n v a r i a n t ~}}$ as well (use Lemma 4.7 again).
Since -A is the generator of the positive group (T(-t)) $t \in \mathbb{R}$ and $J_{\mu}=\{f \in E: R(-\mu,-A)|f| \geq 0\}, J_{\mu}$ has the same properties.
If $f \in I_{\mu} \cap J_{\mu}$ then $R(\mu, A)|f|=0$ hence $f=0$ which shows that $I_{\mu} \cap J_{\mu}=\{0\}$, on the other hand, decomposing $0 \leqq h=h_{1}+h_{2} \in E_{+}$ according to Lemma 4.6 , then assertion (b) of this lemma implies that $h_{1} \in I_{\mu}$, while assertion (c) ensures that $h_{2} \in J_{\mu}$. Since the positive cone $E_{+}$is generating we have $E=I_{\mu} \oplus J_{\mu}$ and the first part of the theorem is proved.
Since $I_{\mu}$ is $R(\mu, A)$-invariant we have $\mu \in p\left(A \| I_{\mu}\right)$ and $\mathrm{R}\left(\mu, \mathrm{A} \mid \mathrm{I}_{\mu}\right)=\mathrm{R}(\mu, \mathrm{A}) \mid \mathrm{I}_{\mu} \mathrm{Z}$. $\mathrm{C}-\mathrm{III}$, Thm, $1,1(\mathrm{~b})$ then implies
$o\left(A \| I_{\mu}\right) \in\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda<\mu\}$. The same argument applied to $-A$ and $-\mu$ yields $\sigma\left(A \mid J_{\mu}\right) \subset\{\lambda \in \mathbb{L}: \operatorname{Re} \lambda>\mu\}$. Now the assertion follows from A-III, Prop.4.2.

The spectral projections corresponding to the spectral decomposition described above have the expected representation as an integral 'around' the spectral sets, see Corollary 3 in Greiner (1984c).

Corollary 4.9. Assume that the assumptions of the theorem are satisfied, $\mu \in \rho(A) \cap R \quad B>s(A), \alpha<-s(-A)$. If we denote the projections corresponding to the decomposition $E=I_{\mu} \oplus J_{\mu} \quad b y \quad P_{\mu}$ and $Q_{\mu}$ (i.e., $P_{\mu} E=\operatorname{ker} Q_{\mu}=I_{\mu}, Q_{\mu} E=\operatorname{ker} P_{\mu}=J_{\mu}$, then for $f \in D\left(A^{2}\right)$ we have

$$
\begin{align*}
& P_{\mu} f=\frac{1}{2 \pi} * \int_{-\infty}^{\infty} R(\mu+i \tau, A) f d \tau-\frac{1}{2 \pi} \cdot \int_{-\infty}^{\infty} R(\alpha+i \tau, A) f d \tau, \\
& Q_{\mu} f=\frac{1}{2 \pi} * \int_{-\infty}^{\infty} R(E+i \tau, A) f d \tau-\frac{1}{2 \pi} \cdot \int_{-\infty}^{\infty} R(\mu+i \tau, A) f d \tau . \tag{4.10}
\end{align*}
$$

(The integrals appearing in (4.10) are improper Riemann integrals.)

We mention another consequence of Thm.4.8. Like Prop.4.5 it is a spectral mapping theorem for the real part of the spectrum.

Corollary 4.10. If $(T(t))_{t \in \mathbb{R}}$ is a positive group on a space $L^{2}$ or $C_{0}(x)$ with generator $A$, then
(4.11) $\sigma(T(t)) \cap_{+}=\exp (t o(A) \cap R)$ for every $t \geqq 0$.

Proof. We borrow from the next chapter that for positive semigroups on spaces $L^{1}, L^{2}$ or $C_{o}(X)$ spectral bound and growth bound coincide (see C-IV,Thm-1.1).
We only have to show that $\exp \left(t p(A) n_{i}\right) \subset p(T(t)) \cap A+$
If we consider a positive semigroup on an $L^{2}$-space, Thm. 4.8 can be applied directly: Given $\mu \in \rho(A) \cap \Pi$, then $E=I_{\mu} \not \operatorname{TO}_{\mu}$ according to Thm.4.8 - The result mentioned above implies $r\left(T(t) \mid I_{\mu}\right) \& e^{\mu t}$ and $r\left(T(-t) \mid J_{\mu}\right)<e^{\mu t}$. Hence $\sigma\left(T(t) \mid I_{\mu}\right) \in\left\{\lambda \in \mathbb{C}:\left\{\lambda \mid<e^{\mu t}\right\}\right.$ and $\sigma\left(T(t) \mid J_{\mu}\right)=\left(\sigma\left(T(-t) \mid J_{\mu}\right)\right)^{-1}:\left\{\lambda \in \mathbb{G}:|\lambda|>e^{\mu t}\right\}$.
Thus $\quad(T(t))=\sigma\left(T(t) \mid I_{\mu}\right) \cup \sigma\left(T(t) \|_{\mu}\right)$ does not contain $e^{\mu t}$.
In case ( $T(t)$ ) is a positive group on $C_{o}(X)$ then the adjoint group ( $T(t)^{r}$ ) is a group of lattice homomorphisms on $E^{r}$. It follows that $E^{*}$ is a sublattice of $C_{o}(X)^{r}=M_{b}(X)$ hence a $L^{l}$-space. The argument given for the $L^{2}$-space yields
$\sigma(T(t) *) \cap \mathbb{R}_{+}=\exp \left(t o\left(A^{*}\right) \cap_{i}\right)$ for every $t \geqq 0$, Thus the assertion follows from A-III,4.4.

We conclude by describing a general situation where lattice semigroups occur. In Section 4 of $B$-III we constructed semigroups of lattice homomorphisms on $C_{0}(X)$ starting with a continuous (semi-lflow on the locally compact space $X$ and a multiplication operator. one can perform similar constructions on spaces $L^{P}(\mu)$ for $1 \approx p<\infty$ under certain conditions on the flow. We consider an example which shows where the problems are.
Define the semiflow $\phi$ on $\mathbb{F}_{+}$as follows: $\phi(t, x):=x-t$ for $x \geqslant t$ and $\phi(t, x):=0$ for $x \leq t$. For $f \in L^{P}(\mu)$ one has difficulties to define fo中t properly since the preimage of the zeromset $\{0\}$ does not have measure zero. This problem does not arise in case every transformation $\phi_{t}$ is measure preserving, i.e. $\mu\left(\phi_{t}{ }^{-1}(C)\right)=\mu(C)$ for every Borel set $C$. A more general criterion is stated in the following proposition.

Proposition 4.11. Let $x$ be a locally compact space and let $\mu$ be a regular, positive Borel measure on $X$. Assume that the continuous semiflow $\phi: \mathbb{R}_{+} \times X \rightarrow X$ satisfies the following condition:
$(4,12) \quad \phi_{t}{ }^{-1}(\mathrm{~K})$ is compact for every compact set $K \subset \mathrm{X}, \mathrm{t} \geqq 0$,
（a）For every $p, 1 \leqslant p<\infty$ the following assertions are equivalent．
（i）The operators $T(t)$ defined by $T(t) f ;=f o \phi t$ for $f \in L^{P}(\mu)$ ， $t \geqq 0$ ，are well－defined as bounded linear operator on $L^{P}(\mu)$ and $(T(t))_{t \geq 0}$ is a strongly continuous semigroup．
（ii）There exist constants $t_{0}>0, M>0$ such that $\mu\left(\phi_{t}{ }^{-1}(C)\right) \leqq M * \mu(C)$ for every open（compact）set $C=X$ and every $t \leq t_{0}$ ．
（b）In case the conditions（i）and（ii）are fulfilled then（T（t））t》0 is a semigroup of lattice homomorphisms on $L^{P}(\mu)$ and $C_{c}(X) \cap D(A)$ is a core of the generator．

Proof．（a）since $\mu$ is assumed to be regular，the inequality stated in（ii）holds true for all Borel sets provided it is true for all open sets（compact sets，respectively）．
$(i) \rightarrow(i i):$ Assume that（ $T(t)$ is a strongly continuous semigroup on $L^{P}(\mu), 1 \leqq p<\infty$ ．For $t_{0}>0$ we define $\left.M:=\left(\sup \|T(t)\|: 0 \leq t \leq t_{0}\right\}\right)^{1 / P}$ ． Given a Borel set $C=X$ we write $C(t):=\phi_{t}^{-1}(C)$ ． Then we have $T(t) X_{C}=X_{C(t)}$ ，hence
$\mu\left(\phi_{t}^{-1}(C)\right)=\left\|x_{C}(t)\right\|_{\mathrm{P}}^{P}=\left\|T(\mathrm{t}) X_{\mathrm{C}}\right\|_{\mathrm{P}}^{\mathrm{P}} \leqq \mathrm{M} \cdot\left\|\mathrm{X}_{\mathrm{C}}\right\|_{\mathrm{P}}^{\mathrm{P}}=\mathrm{M} \cdot \mu(\mathrm{C})-$
（ii）$\rightarrow$（i）：Since the inequality in（ii）holds for all Borel sets， $\phi_{t}{ }^{-1}$（C）is a $\mu-n u 11$ set whenever $C$ is a $\mu=n u 11$ set．Thus given Borel functions $f, g$ such that $f=g \mu-a, e$ ．then fo中 $t=g o \phi_{t}$ $\mu-a . e ., M o r e o v e r, ~ f o r ~ 0 \leq f \in L^{P}(\mu)$ ，there exists an increasing sequence（ $h_{n}$ ）of simple functions converging pointwise to $f$ ．Then （ $h_{n}{ }^{\circ} \phi_{t}$ ）is a monotone sequence converging pointwise to fo中t ．Using the fact that $X_{C}{ }^{\circ} \phi_{t}=X_{C}(t), C(t)$ as above，and the assumption $\mu(C(t)) \leq M \cdot \mu(C) \quad$ it is easy to see that $\left\|_{i} h_{n} \phi_{t}\right\|_{\mathrm{P}}^{\mathrm{P}} \leqq \mathrm{M} \cdot\left\|_{\|} h_{n}\right\|_{\mathrm{P}}^{\mathrm{P}} \leqq \mathrm{M} \cdot\|\mathrm{f}\|_{\mathrm{P}}^{\mathrm{P}}$ Thus by the Monotone Convergence Theorem we have fo申t $\in L_{(\mu)}^{P}$ ）and $\| f{ }_{f} t_{p} \leqq M^{1 / P\|f\|_{p}}$ ．It follows that $T(t)$ is a bounded Iinear operator on $L^{P}(\mu)$ and $f T(t) \| M^{l / P}$ for $0 \leq t \leq t_{o}$ ．Since $\phi$ is semiflow we have $T(0)=I d$ and $T(t+s)=T(s) T(t)(0 \leq s, t<\infty)$ ．It remains to prove strong continuity．Since $\phi \quad$ is continuous and（4．12） holds，we know that $T(t)\left(C_{c}(X)\right)=C_{c}(X)$ and that $T(t) f$ tends to $f$ uniformly as $t \rightarrow 0$ provided that $f \in C_{C}(X)$ ．It follows that $\lim _{t \rightarrow 0}\|T(t) f-f\|_{p}=0$ for $f \in C_{C}(X)$ ．Since $C_{C}(X)$ is dense in $L^{P}(\mu)$ and $\|T(t)\| \leqslant M^{1 / P}$ for $0 \leqq t \leqq t_{0}$ ，the semigroup is strongly continuous．
（b）Obviously every operator $T(t)$ defined in assertion（i）of（a） is a lattice homomorphism．Above we pointed out that $C_{C}(X)$ is
invariant under (T(t)), then $D(A) C_{C}(X)$ is invariant as well. It is dense because the elements of the form $\int_{0}^{r} T(s) f d s, f \in C_{C}(X)$, $r>0$, belong to $C_{c}(X)$ and to $D(A)$. Hence $D(A) C_{C}(X)$ is a core (by A-I, Cor. 1, 34).

Prop. 4.11 can be used to prove that flows corresponding to certain ordinary differential equations on $\mathbb{R}^{n}$ generate strongly continuous semigroups on $L^{P}\left(R^{n}\right)$ (where $R^{n}$ is equipped with the Lebesgue measure). One has to impose conditions on the corresponding vector field. Note that for continuous flows condition (4.12) is automatical$I_{Y}$ satisfied because for a compact $\mathbb{K} \subset X$ the set $\phi_{t}{ }^{-1}(K)=\phi_{-t}(K)$ is compact as the continuous image of a compact set,

Example 4.12. Let $F=\mathbb{R}^{n}+A^{n}$ be a $C^{1}$-vector field and assume that the derivative $D F$ is unitormly bounded on $\mathbb{N}^{n}$. Then the ordinary differential equation $Y^{\prime}=F(y)$ possesses a global flow $\phi: q \times i^{n}+\mathbb{R}^{n}$ which is $C^{I}$. Moreover, we have (4.13) $\left\|D_{t}(x)\right\| s e^{M|t|}$ for all $x \in \operatorname{Bit}^{n}, t \in \mathbb{R}$, where $M:=\sup \left\{\|D F(x)\|: x \in \|^{n}\right\}$.

All these properties were proven in Ex. 3.15 of $B-I I$.
We will show that $\phi$ satisfies condition (ii) of Prop.4.ll(a). Hence it induces a strongly continuous (semi-)group of lattice homomorphisms
![](https://cdn.mathpix.com/cropped/2025_01_15_bba15162fec278e19e93g-39.jpg?height=72&width=969&top_left_y=1623&top_left_x=227)
This $1 s$ done using the change of variables formula as follows: Let $U$ be an open subset of $i i^{n}$, then $\phi_{t}{ }^{-1}(U)=\phi_{-t}(U)=: U(-t)$. If $\lambda$ denotes the Lebesgue measure then

$$
\begin{align*}
& \lambda\left(\phi_{t}^{-1}(J)\right)=\int_{U(-t)} I d x=\int_{U} l_{0 \phi_{-t}}(x) \cdot\left|d e t D \phi_{-t}(x)\right| d x=  \tag{4.14}\\
& \int_{U}\left|\operatorname{det} D_{\phi_{-}}(x)\right| d x \leqq \int_{U} e^{n M|t|} d x=e^{n M|t|} \cdot \lambda(J) .
\end{align*}
$$

Here we used (4.13) and the fact that the determinant of an $n \times n-m a t r i x$ B satisfies $\mid$ det $B \mid \leqq\|B\|^{n}$.

In general, existence of a global flow does not ensure that one can associate a semigroup of bounced 11 near operators on $L^{P}\left(\mathbb{R}^{n}\right)$, even if the vector field is $c^{\infty}$. For example the differential equation $Y^{*}=\sin \left(Y^{2}\right)$ does not induce a semigroup on $L^{P}(\mathbb{R})$. There is another important class of differential equations which do induce semigroups of lattice homomorphisms on $L^{\text {P }}$-spaces: Hamiltonian differential equations. In fact, Liouville's Theorem states that the
flow corresponding to a Hamiltonian vector field preserves the volume (see Abraham-Marsden (1970, Sec.3.3). Thus assertion (ii) of proposition 4 . Il (a) is trivially satisfied.
Further examples of flows which are measure preserving and therefore induce semigroups of lattice homomorphisms on $L^{P}$-spaces are billiard flows on compact convex subsets of $i^{n}$ and geodesic flows on Riemannian manifolds (see Cornfeld-Fomin-Sinai (1982)).

NOTES.
Spectral theory for a single positve operator as developed in Chapter $V$ of Schaefer (1974) is an essential tool for this chapter. Various results on the spectral theory of positive one-parameter semjgroups can be found in Chapter 7 of Davies (1980) and in the second part of Batty-Robinson (1984).

Section l. That the spectral bound ts always an elenent of the spectrum was stated by Karlin (1959), but a valid proof was giveti by Derndinger (1980). This assertion as well as assertion (b) of Theorem l. I allow generalizations In varinus directions: They are valid for ordered Banach spaces (see Greiner-Voigt-Wolff (1981) and Klein (1984)) and one only needs that $A$ has positive resolvent (see Kato (1982) or Nussbaum (1984)). Theorem 1.2 as well as its coroliartes are also valid in ordered Banach spaces. For the analogue in the theory of the laplace transform we refer to Sec. 10.5 in Whder (1971) and Voigt (1982).

Sectlon 2. Theorem 2.2 is the basis for the subsequent cyclicfty results. Pseudoresolvents are dłscussed e.g. in Hille-Phillips (1957) or Yosida (1965). For nonpositive semfroups the two assertions stated in Def. 2.8 are no longer equivalent. A special cage of Theorer 2.10 was proven by Derrdinger (1980) white the general result is due to Greiner (1981). Instead of psendo-resolvents on the whole F-product Derndinger works whth the semigroup on the semtgroup F-product. Therefore he can only consider eigenvalues. Ellyptic differential operators as generators of posittve semigroups are discussed by many authors, e.g., Amann (1983), Fattorini (1983), Friedmann (1972) or Pazy (1983).

Section 3. There exfst various notions which are (more or less closely) related to irreducibility, e.g. 'positivity improving' in Reed-Simon (l979), (1-positivity in Krasnosel'skii (1964) or 'quasi-strictly posttive' in Karlin (1959)). Sawashima (1964) uses 'non-support' instead of irreductble. She also djscusses several modifications (semi-non-support, strictly non-support, strongly positive) and the interrelationship between these notions. The rotion of freducibility can be extended to the (non-lattyce) ordered setting (see Ratty-Robinson (1984)). Assertion (b) of Theorem 3.2 is due to Majewski-Robinson (1983) while special cases can be found in Sec. XIL . 12 of Reed-Simon (1979) and in Kishimoto-Robinson (1981). Proposition 3.3 is due to Voigt (1984). Retarded equations as dicussed in Example 3.4(c) will be discussed in more detail in Section 3 of C-IV. Example 3.4(d) is a one-dimenstonal versfon of the linear transport equation. The higher dimensional equation is more delicate but can be treated similarly (see e.g. Greiner (1984), Kaper-LekkerkerkerHejtmanek (1983), or Voigt (1984b)). A special case of Propositlon 3.5 can be found
in Davies (1980). Theorem 3.7 and Example 3.6 are taken from Schaefer (1985). The most interesting criterion of Thm. 3.7 seems to be condition (c), since it gives a sufficient condition for the existence of efgenvalues for a sufficiently large class of semigroups. For semigroups induced by measure-preserving flows Theorem 3.8 and Corollary 3.9 are proven in Cornfeld-Fomfn-Stnat (1982). Corollary 3.9 is a special case of the Halmos-von Neumann Theorem which classlfies irreducible semigroups having discrete spectrum (see Cornfeld-Fomin-Sinai (1982), Greiner (1982) and Schaefer (1974) for the general result). Lemma 3.10 ss taken from Groh (1984b) and Theorems 3.12 and 3.14 can be found (with slightly different proofs) in Greiner (1981).

Section 4. It was Derndinger (1980) who proved Theorem 4.2. In Cor.4.3 one can replace boundedness of the semigroup by the assumption that the resolvent grows slowly (see Greiner (1982)). Example 4.4 is due to Davies and Proposition 4.5 to Kellermann (both umpublished). The spectral decomposition for positive groups as described in Theorem 4.8 is valid in arbitrary Banach lattices (see Arendt (1982) and Greiner (1984c)). This also holds for Corollaries 4.9 and 4.10 = Proposition 4.11 and Example 4.12 indtcate the relationship of posity ge groups to dynamical systems. For example, the 'Annular Hull Theorem' (see Chicone-Swanson (1981)) is closely related to the results of this section.


[^0]:    (2.23) Does every positive semigroup have cyclic boundary spectrum?

