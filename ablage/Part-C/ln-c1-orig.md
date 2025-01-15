# POSITIVE SEMIGROUPS ON BANACH LATTICES 

CHAPTER C-I<br>![](https://cdn.mathpix.com/cropped/2025_01_15_0c41216426f36f11df27g-01.jpg?height=44&width=1454&top_left_y=820&top_left_x=298)<br>AND POSITIVE OPERATORS<br>by<br>Rainer Nagel and U1f Schlotterbeck

This introductory chapter is intended to give a brief exposition of those results on Banach lattices and ordered Banach spaces which are indispensable for an understanding of the subsequent chapters. We do not want to give proofs of the results we are going to present, since these can easily be found in the literature (e.g., in Schaefer 1974). We rather want to give the reader who is unfamiliar with these results or with the terminology used in this book the necessary informatjon for an intelligent reading of the main discussions. Since relatively few general results on ordered Banach spaces are needed, we will primarily talk about Banach lattices. The scalar field will be $\mathbb{R}$ except for the last three sections, where complex Banach lattices will be discussed.

The notion of a Banach lattice was devised to get a common abstract setting within which one could talk about phenomena related to positivity that had previously been studied in various types of spaces of real-valued functions, such as the spaces $C(K)$ of continuous functions on a compact topological space $K$, the Lebesgue spaces $L^{l}(\mu)$ or more generally the spaces $L^{P}(\mu)$ constructed over a measure space ( $\mathrm{X}, \mathrm{F}, \mu$ ) for $\mathrm{l} \leq \mathrm{p} \leq \infty$. Thus it is a good idea to think of such spaces first in order to get a feeling for the concrete meaning of the abstract notions we are going to introduce. Later we will see that the connections between abstract Banach lattices and the "concrete" function lattices $C(K)$ and $L^{1}(\mu)$ are closer than one might think at first. We will use without further explanation the terms order relation (orderingl, ordered set, majorant, minorant, supremum, infimum.

By definition, a Banach lattice is a Banach space (E,\| \|) which is endowed with an order relation, usually written $\leqq$, such that ( $\mathrm{E}, \mathrm{S}$ ) is a lattice and the ordering is compatible with the Banach space structure of $E$. We are going to elaborate this in more detail now.

The axioms of compatibility between the linear structure of $E$ and the order are as follows:
![](https://cdn.mathpix.com/cropped/2025_01_15_0c41216426f36f11df27g-02.jpg?height=124&width=1505&top_left_y=783&top_left_x=224)

Any (real) vector space with an ordering satisfying ( $\mathrm{LO}_{1}$ ) and (LO ) is called an ordered vector space. The property expressed in (Lo, is sometimes called translation invariance and implies that the ordering of an ordered vector space $E$ is completely determined by the positive part $E_{+}=\{\dot{f} \in E \ddagger \neq 0\}$ of $E$. In fact, one has $f \leqq g$ if and only if $g-f \in E_{+} .\left(L O_{1}\right)$ together with ( $L_{2}$ ) furthermore imply that the positive part of $E$ is a convex set and a cone with vertex 0 (often called the positive cone of $E$ ) . It is easily verified that conversely any proper convex cone $C$ with vertex 0 in $E$ is the positive part of $E$ with respect to a uniquely determined compatible ordering.

An ordered vector space $E$ is called a vector lattice if any two elements $f$, $g$ in $E$ have a supremum, which is denoted by sup(f,g) or by $f \vee g$, and an infimum, denoted by inf(f,g) or by fag. It is obvious that the existence of, e.g., the supremum of any two elements in an ordered vector space implies the existence of the supremum of any finite number of elements in $E$ and, since fsg is equivalent to $-g \leqq-f$ this automatically implies the existence of finite infima. However, suprema (infima) of infinite majorized subsets need not exist in a vector lattice. If they do, then the vector lattice is called order complete (countably order complete or ororder complete if suprema of countable majorized subsets exist). At any rate, the binary relations sup and inf in a vector lattice automatically satisfy the (infinite) distributive laws

$$
\begin{aligned}
& \inf \left(\sup _{\alpha} f_{\alpha}, h\right)=\sup _{\alpha}\left(\inf \left(f_{\alpha}, h\right)\right) \\
& \sup \left(\inf f_{\alpha} f_{\alpha}, h\right)=\inf f_{\alpha}\left(\sup \left(f_{\alpha}, h\right)\right)
\end{aligned}
$$

whenever one side exists and give rise to the following definitions:

$$
\begin{aligned}
& \sup (f,-f)=|f| \text { is called the absolute value of } f \\
& \sup (f, 0)=f^{+} \text {is called the positive part of } f \\
& \sup (-f, 0)=f^{-} \text {is called the negative part of }
\end{aligned}
$$

Note that the negative part of $f$ is positive.

We call two elements $f, g$ of a vector lattice orthogonal or lattice disjoint and write $f \pm g$, if $\inf (|f|,|g| J=0$. Apart from this, the above definitions allow us to formulate the axiom of compatibility between norm and order requested in a Banach lattice in the following short way:

$$
\begin{equation*}
|f| \leq|g| \text { implies }\|f\| \leq\|g\| \tag{LN}
\end{equation*}
$$

A norm on a vector lattice is called a lattice norm, if it satisfies (LN), and with these notations we can now give the definition of a Banach lattice as follows: A Banach lattice is a Banach space E endowed with an ordering $s$ such that ( $E, \leq$ ) is a vector lattice and the norm on $E$ is a lattice norm. By a normed vector lattice we understand a vector lattice endowed with a lattice norm.

There is a number of elementary, but very important formulas valid in any vector lattice, such as

$$
\begin{aligned}
f & =f^{+}-f^{-} & |f+g| \leqq|f|+|g| \\
|f| & =f^{+}+f^{-} & f+g=\sup (f, g)+\inf (f, g)
\end{aligned}
$$

etc.

Let us note in passing the following consequences:
(i) The Iattice operations $(f, g) \rightarrow s u p(f, g)$ and $(f, g) \rightarrow$ inf(f,g) and the mappings $f \rightarrow f^{+}, f \rightarrow f^{-}, f \rightarrow|f|$ are uniformiy continuous.
(ii) The positive cone is closed.
(iii) order intervals, i.e. sets of the form $[f, g]=\{h \in E: f \leqq h \leqq g\}$ are closed and bounded.

Instead of dwelling upon a detailed discussion of the above equalities and inequalities let us rather formulate the following principle,
which allows us to verify any of them and to invent, prove or disprove new ones whenever necessary:

Any general formula relating a finite number of "variables" to each other by means of lattice operations and/or linear operations is valid in any Banach lattice as soon as it is valid in the real number system.

In fact, we are going to see below that any Banach lattice $E$ is, as a vector lattice, "locally" of type $C(x)$, more exactly: Given any finite number $x_{1}, \ldots, x_{n}$ of elements in $E$ there is a compact topological space $X$ and a vector sublattice $J$ of $E$ which is isomorphic to $C(X)$ and contains $x_{1}, \ldots, x_{n}$ (see Section 4). The above principle is an easy consequence of this: In a space $C(x)$ it is clear that a formula of the type considered need only be verified pointwise, i.e. in $\mathbb{R}$.

The reader may now be prepared to follow a concise presentation of the most basic facts on Banach lattices.

1. SUBLATTICES, IDEALS, BANDS

The notion of a vector sublattice of a vector lattice $E$ is selfexplanatory, but it should be pointed out that a vector subspace $F$ of E which is a vector lattice for the ordering induced by $E$ need not be a vector sublattice of $E$ (formation of suprema may differ in $E$ and in $F$ ), and that a vector sublattice need not contain (or may lead to different infinite suprema and infima. The following are necessary and sufficient conditions on $a$ vector subspace $G$ of $E$ to be a vector sublattice:

| (i) | $\|h\| \in G$ for all |
| :--- | :--- |
| (ii) | $h^{+} \in G$ |
| (iii) | $h^{-} \in G$ for all |
| ( | $h \in G$ all |
|  | $h \in G$. |

A subset $B$ of $a$ vector lattice is called solid if $f \in B,|g| \leq|f|$ implies $g \in B$. Thus a norm on a vector lattice is a lattice norm if and only if its unit ball is solid. A solid linear subpace is called an ideal. Ideals are automatically vector sublattices since |sup(f,g)| $\leq|f|+|g|$. On the other hand, a vector sublattice $F$ is an ideal in $E$ if $g \in F$ and $0 \leqq f \leqq g$ imply $f \in F$. A band in a vector Iattice $E$ is an ideal which contains arbitrary suprema, more ex-
actly: $B$ is a band in $E$ if $B$ is an ideal in $E$ and sup $M$ is contained in $B$ whenever $M$ is contained in $B$ and has a supremum in $E$. Since the notions of sublattice, ideal, band are invariant under the formation of arbitrary intersections there exists, for any subset $B$ of $E$, a uniquely determined smallest sublattice (ideal, band of $E$ containing $B$ : the sublattice (ideale band) generated by B.
If we denote by $B^{d}$ the set $\{h \in E: \inf (|h|,|f|)=0$ for all $f \in B\}$, then $B^{d}$ is a band for any subset $B$ of $E$, and $\left(B^{d}\right)=B^{d d}$ is a band containing $B$. If $E$ is a normed vector lattice (more generally, if $E$ is archimedean ordered, see e.g. Schaefer (1974)), then $\mathrm{B}^{\mathrm{dd}}$ is the band generated by B .

If two ideals $I$, $J$ of a vector lattice $E$ have trivial intersection $\{0\}$, then $I$ and $J$ are Iatticedisjoint, i.e, $I \in J^{d}$. Thus if $E$ is the direct sum of two ideals $I$, J then one has automatically $I=J^{d}$ and $J=I^{d}$, hence $I=I^{d d}$ and $J=J^{d d}$ must be bands in this situation. In general, an ideal $I$ need not have a complementary ideal $J$, even if $I=I d$ is a band. This amounts to the same as saying that even if $I=I^{d d}$ (which is always true if I is a band in a normed vector lattice) one need not necessarily have $E=I+I^{d}$. An ideal $I$ is called a projection band if it does have a complementary ideal, and in this case the projection of $E$ onto I with kernel $I^{d}$ is called the band projection belonging to I . An example of a band which is not a projection band is furnished by the subspace of $C([0,1])$ consisting of the functions vanishing on [0.1/23 . The Riesz Decomposition Theorem asserts that in an order complete vector lattice every band is a projection band. As a consequence, if $E$ is order complete and $B$ is an arbitrary subset of $E$, then $E$ is the direct sum of the complementary bands $B^{d}$ and $B^{d d}$. This Theorem, which is quite easy to prove, is widely used in Analysis and gives an abstract background to, e.g., the decomposition of a measure into atomic and diffuse parts (the atomic measures being those contained in the band generated by the point measures, the diffuse measures those disjoint to the latter) or, more specifically, to the well-known decomposition of a measure on $[a, b]$ into an atomic part and a diffuse part, which latter can in turn be decomposed into the sum of a measure which is absolutely continuous (which means, contained in the band generated by Lebesgue measure) and a singular measure (which means, a diffuse moasure disjoint to lebesgue measure).

A band in a normed vector lattice is necessarily closed. By contrast, an ideal need not be closed, but the closure of an ideal is again an ideal. The situation where every closed ideal is a band will be briefly discussed in Section 5 .
2. ORDER UNITS, WEAK ORDER UNITS, QUASI-INTERIOR POINTS

An element $u$ in the positive cone of a vector lattice $E$ is called an order unit, if the ideal generated by u is all of $E$. If the band generated by $u$ is all of $E$ (which is equivalent to $\{u\}=0$ whenever $E$ is archimedean, hence in particular if $E$ is a normed vector latticel then $u$ is called a weak order unit of $E$. If $E$ is a Banach lattice, then any order unit in $E$ is an interior point of the positive cone $E_{+}$, and conversely any interior point of $E_{+}$must be an order unit of $E$. Every space $C(K)$ has order units fnamely, the strictly positive functions), and conversely by the Kakutani-Krein Representation Theorem (see Section 4) every Banach lattice with an order unit is isomorphic to a space $C(K)$. If an element $u$ in the positive cone of a Banach lattice $E$ has the property that the closed ideal generated by $u$ is all of $E$, then $u$ is called a guasi-in= terior point of $E_{+}$. Quasi-interior points of the positive cone exist, e.g., in any separable Banach lattice. If $E=C(K)$, then the quasi-interior points and the interior points of $E_{+}$coincide, while the weak order units of $E$ are the (positive) functions vanishing on a nowhere dense subset of $K$. If $E$ is a space $\mathrm{L}^{\mathrm{P}}(\boldsymbol{\mu})$ with o-finite $\mu$ and $1 \leqq p<\infty$, then the weak order units and the quasi-interior points of $E_{+}$coincide with the functions strictly positive u-a.e., while $E_{+}$does not contain any interior point.

## 3. LINEAR FOXMS AND DUALTTY

A Inear functional $\phi$ on a vector lattice $E$ is called

```
order-bounded, if ф is bounded on order intervals of E ,
positive, if }\phi(f) \geqq 0 for al1 f \geqq 0
strictly positive, if }\phi(f)>0 for all f>>0.
```

Any positive linear functional is order bounded, and the positive functionals form a proper convex cone with vertex 0 in the linear space $E^{\#}$ of all order bounded functionals, thus defining a natural
ordering (given by $\phi \leq \psi$ if and only if $\phi(f) \leqq \psi(f)$ for all $f \in E_{+}$) under which $E^{\#}$ is an order complete vector lattice. In particular, positive part, negative part and absolute value exist for any order bounded functional on $E$, the absolute value of $\phi \in E^{\#}$ being given by

$$
|\phi|(f)=\sup \{\phi(h):|h| \leqq f\} \quad\left(f \in E_{+}\right)
$$

As a consequence, one has $|\phi(f)| \leq|\phi|(|f|)$ for all $f$ in $E$ whenever $\phi$ is order bounded, and $|\phi(f)| \leqq \phi(|f|)$ if and only if $\phi$ is positive. An order bounded linear functional $\phi$ is called order continuous (g-order-continuous) if both positive and negative part of $\phi$ have the property that they transform any decreasing net dany decreasing sequencel with infimum 0 into a net (sequence) converging to 0 in $\mathbb{R}$. The order-continuous (o-order-continuous) functionals form a band in $E^{\#}$. In general, a vector lattice $E$ need not admit any non-zero order-bounded linear functional. However, if $E$ is a normed lattice, then any continuous functional is order-bounded, and if $E$ is a Banach lattice then one has coincidence between $E^{\#}$ and E' $^{\prime}$ Still, order-continuous functionals $\neq 0$ need not exist on a Banach lattice. Situations where every order-bounded functional is order-continuous will be briefly discussed in Section 5.

If $E$ is a Banach lattice, then the dual norm on $E^{1}=E^{\#}$ is a lattice norm, hence $E^{1}$ is an order-complete Banach lattice under the natural norm and order. The evaluation map from $E$ into the second dual $E^{\prime \prime}$ is a lattice homomorphism (for the definition see Section 6) into the band of order-continuous functionals on E'. In particular, every dual Banach lattice $E$ admits sufficiently many order-continuous functionals to separate the points of $E$.

## 4. AM- AND AL-SPACES

If the norm on a Banach lattice $E$ satisfies

$$
\begin{equation*}
\|\sup (f, g)\| \Rightarrow \sup (\|f\|,\|g\|) \text { for } f, g \in E_{+} \tag{M}
\end{equation*}
$$

then $E$ is called an abstract M-space or an $A M-s p a c e$. If in addition the unit ball of $E$ contains a largest element $u$, then $u$ must be an order unit of $E$ and $E$ is then called an (AM)-space with unit. Condition (M) in $E$ implies that in the dual of $E$ one has

$$
\begin{equation*}
f_{\|}^{\prime} f+g\|=\| f\|+\| g \| \text { for } f, g \geq 0 . \tag{L}
\end{equation*}
$$

Any Banach lattice satisfying (L) is called an abstract L-space or an AL-space. Thus the dual of an AM-space is an AL-space. It is quite easy to verify that on the other hand the dual of an AL-space is an AM-space with unit, the unit being the uniquely determined linear functional that coincides with the norm on the positive cone. putting this together, one gets that the second dual of an AM-space $E$ is an AM-space with unit. If $E$ already has a unit $u$, then $u$ is also the unit of $E^{\prime \prime}$, so that the ideal of $E^{\prime \prime}$ generated by $E$ is all of $E^{n}$. By contrast, if $E$ is an AL-space, then $E$ is an ideal (even a band) in E". Infinite-dimensional AL- or $A M-s p a c e s$ are never reflexive.

The importance of AL- and AM-spaces in the general theory of Banach lattices is due to the fact that these spaces have very special concrete representations as function lattices and that, on the other hand, any general Banach lattice $E$ is in a very intimate way connected to certain families of AL- and AM-spaces canonically associated with $E$. Let us first discuss the natural representations of AM- and AL-spaces.

If $E$ is an $A M-s p a c e$ with unit $u$, then the set $K$ of latice homomorphisms (cf. Section 6) from $E$ into $\mathbb{R}$ taking the value 1 on $u$ is a non-empty, compact subset of the weak dual of $E$ and the natural evaluation map from $E$ into $R^{K}$ maps $E$ isometrically onto the continuous real-valued functions on $K$. This is the KakutaniKrein Representation Theorem, which is an order-theoretic counterpart to the Gelfand Representation Theorem in the theory of commatative $C^{*}$-algebras. If $E$ is an $A M-s p a c e$ without unit, then the second dual of $E$ has a unit and thus gives a representation of $E$ as a closed sublattice of a space $C(K)$. If $E$ is an AL-space, then the representation of the dual of $E$ as a space $C(K)$ leads to an interpretation of the elements of $E^{*}$ as Radon measures on $K$. If $E_{+}$has a quasi-interior point $h$, then in this interpretation $E$ consists exactly of the measures absolutely continuous with respect to (the measure corresponding to) $h$, thus by the Radon-Nikodym Theorem $E=L^{l}(K, h)$. In general, a similar argument leads to a representation of $E$ as a space $L^{1}(X, \mu)$ constructed over a locally compact space X .

If $E$ is an arbitrary Banach lattice, $f \in E_{+}$, then the ideal I generated by $f$ in $E$ (which is the union of the positive multiples of the interval [-f,f]) can be made into an AM-space with unit f
by endowing it with the gauge function $P_{f}$ of $[-f, f]$. We denote ( $I_{f} P_{f}$ ) by $E_{f}$. On the other hand, if $f$ is a positive linear functional on $E$, then the mapping $q_{f}, f \rightarrow\langle | f\left|, f^{*}\right\rangle$ is a semi-norm on $E$. The kernel $J$ of $\mathcal{G}_{f}$ is an ideal in $E$, and the completion of $E_{J}$ with respect to the norm canonically derlved from $\mathcal{f}_{f}$, becomes an AL-space which we denote by (E, $x^{\prime}$ ) . A good lllustration for these constructions is the following: If $E=C(K)$ and if $\mu$ is a positive linear form (Radon measure) on $E$, then ( $E, H$ ) is just $L^{1}(K, \mu)$; if $E=L^{P}(\mu) \quad(1 \leqq P<\infty, \mu$ finite $)$ then $E_{1_{X}}=L^{\infty}(\mu)$.
5. SPECIAL CONNECTIONS BETWEEN NORM AND ORDER

If an increasing net ( $\left.x_{\alpha}\right)_{a \in A}$ in a normed vector lattice is convergent, then its limit must be the supremum: this is a consequence of the closedness of the positive cone. On the other hand, if $\left\{x_{a}: \alpha \in A\right\}$ has a supremum, the net ( $x_{\alpha}$ ) $\in A$ need not converge. A Banach lattice is said to have order-continuous norm (o-order-continuous norm) if any increasing net (sequence) which has a supremum is automatically convergent. This is of course equivalent to saying that any decreasing net (sequence) with an infimum is convergent, and since infimum and limit must coincide, the order continuity fo-order continuity) of the norm in a Banach lattice is also equivalent to the following:

Any decreasing net (sequence) with infimum 0 converges to 0 .

A Banach lattice with order-continuous norm must be order complete, but o-order-continuity of the norm need not imply order completeness. At any rate, one has the following characterization:

A Banach lattice $E$ has order-continuous norm if and only if any one of the following equivalent assertions holds:
(a) E is o-order complete and has o-order-continuous norm.
(b) Every order interval in $E$ is weakly compact.
(c) E is (under evaluation) an ideal in $E "$.
(d) Every continuous IInear form on $E$ is order continuous.
(e) Every closed ideal in $E$ is a projection band.

An even more stringent condition than order-continuity of the norm is
that any increasing norm-bounded net be convergent. This condition is satisfied if and only if any one of the following equivalent assertions holds:
(a) $E$ is (under evaluation) a band in $E^{\prime \prime}$.
(b) E is weakly sequentially complete.
(c) Every order-continuous linear form on $E^{\prime}$ belongs to $E$.
(d) No closed sublattice of $E$ is isomorphic to $c_{o}$ *

The most important examples of non-reflexive Banach lattices with this property are the AL-spaces.
6. POSITIVE OPERATORS, LATTICE HOMOMORPHISMS

A linear mapping $T$ from an ordered Banach space $E$ into an ordered Banach space $F$ is called positive (notation: $T \geqq 0$ ) if Tf $\boldsymbol{f}_{\boldsymbol{f}} \mathrm{F}_{\mathrm{f}}$ for all $f \in E_{+} ; T$ is called strictly positive if $T \geqq 0$ and $\{f \in E: T|f|=0\}=\{0\}$. The set of all positive linear mappings is a convex cone in the space $L(E, F)$ of all linear mappings from $E$ into $F$ defining the natural ordering of $L(E, F)$. The linear subspace of $L(E, F)$ generated by the positive maps (i.e. the space of linear maps that can be written as differences of positive mapsl is denoted by $L^{r}(E, F)$ and its elements are called reqular mappings. If $E$ and $F$ are Banach lattices, then any regular mapping from $E$ into $F$ is continuous, but $L^{r}(E, F)$ is in general a proper subspace of the space L(E,F) of all continuous 1 inear mappings. One has coincidence of $L^{r}(E, F)$ and $L(E, F)$ e.g. when $E=F$ is an order complete $A M-s p a c e$ with unit or an AL-space. At any rate, if $F$ is order complete, then $L^{r}(E, F)$ under the natural ordering is an order-complete vector Iattice, and a Banach Iattice under the norm

$$
T \rightarrow\|T\|_{\mathrm{r}}=\||T|\|^{\prime}
$$

the right hand side denoting the operator norm of the absolute value of $T$. The absolute value of $T \in L^{r}(E, F)$, if it exists, is given by

$$
|T|(f)=\sup [T h:|h| \leqq f\} \quad\left(f \in E_{+}\right)
$$

Thus $T$ is positive if and only if $|T| \leqq T|f|$ holds for any $f$ in $E$.
$T \in L(E, F)$ is called a lattice homomorphism if $|T f|=T|f|$ holds for all $f \in E$. Lattice homomorphisms are alternatively characterized by any one of the following conditions:
(a) $(T f)^{+}=T\left(f^{+}\right)$
(f $\in E$ )
(a') (Tf) ${ }^{-}=T\left(f^{-}\right)$
(f $\in E$ )
(b) $T(f \cup g)=T f \vee T g$
(f $\in E$ )
(b') $T\left(f_{n} g\right)=T f_{\wedge} T g$
(f $\in E$ )
(c) $T\left(f^{+}\right) \wedge T\left(f^{+}\right)=0$
(f $\in \mathrm{E}$ ).

The kernel of a lattice homomorphism is an ideal. If $T$ is bijective, then $T$ is a lattice homomorphism if and only if $T$ and $T^{-1}$ are positive.

## 7. COMPLEX BANACH LATTICES

Although the notion of a Banach lattice is intrinsically related to the real number system, it is possible and often desirable to extend discussions to complexifications of Banach lattices in such a way that the order-related terms introduced in the real situation essentially retain their meaning. Thus we define a complex Banach lattice $E$ to be the complexification of a real Banach lattice $E_{R}$ in the sense that

$$
E=E_{\mathbb{R}} \oplus i E_{\mathbb{R}}
$$

which means more exactly $E=E_{\mathbb{R}} \times E_{\mathbb{R}}$ with scalar multiplication $(\alpha+i \beta)(x, y)=(\alpha x-\beta y, \beta x+\alpha y)$, $E_{\mathbb{R}}$ will sometimes be called the underIying real Banach Iattice or the real part of E . The classical complex Banach spaces $C(X), L^{P}(\mu)$ are complex Banach lattices in this sense, the underlying real Banach lattices being the corresponding (real) subspaces of real-valued functions. We want to extend the formation of absolute values, which is a priori defined only in the real part of $E$, in such a way that in the classical situation $E=C(X)$ or $E=L^{P}(\mu)$ the usual absolute value of a function is obtained. This is in fact possible by putting, for $h=f+i g$ in $E$

$$
|h|=\sup \left(\operatorname{Re}\left(e^{i e} h\right): 0 \leqq \theta \leqq 2 \pi\right\},
$$

the only problem with this definition being the existence of the right hand side without the assumption of order-completeness on $E_{\mathbb{R}}$
(the set in brackets is an order bounded subset of $E_{\mathbb{R}}$ ). But for this we just have to observe that the set $M=\left\{\operatorname{Re}\left(e^{i \theta} h\right): 0 \leq \theta \leqq 2 \pi\right\}$ is contained and order bounded in the ideal generated in $E_{\mathbb{R}}$ by $|f|+|g|$, which in turn is by the Kakutani-Krein Representation Theorem isomorphic to a space $C_{\mathbb{R}}(x)$ under the pointwise ordering. Now the pointwise supremum of $M$ in $i^{X}$ is readily seen to be a continuous function (namely, the modulus of the complex valued continuous function corresponding to $f+i g$ ) so that $M$ has a supremum in $C_{R}(X)=\left(E_{\mathbb{R}}\right)|f|+|g|$.

Since the mapping $f \rightarrow|f|$ now has a meaning in $E$, the definition of an ideal can be extended formally unchanged to the complex situation. We observe that $|f+i g|=|f-i g| \leqq|f|+|g|$ implies that any ideal J in a complex Banach lattice is conjugation invariant and itself the complexification of the ideal $J \cap E_{i f}$ of the real part of $E$. Suffice it now to say that the meaning of most of the terms introduced for real Banach lattices above can be extended to the complex situation under retention (mutatis mutandis) of the corresponding results valdd in the real case by elther using the complex modulus or else, if the formation of suprema or infima is involved, by relating them to real parts. For example $f \in E$ is called positive if $f=|f|$ which means that $f$ is a positive element of $E_{\mathbb{R}}, E$ is called order complete if $E_{R}$ is order complete, and an ideal $J$ is called a band if the real part of $J$ is a band. We refer to Chapter II, Section 11 of Schaefer (1974) for a detailed discussion of this and restrict ourselves to a short discussion of linear mappings.

Let $E$ and $F$ be complex Banach lattices with real parts $E_{\text {lf }}$ and $F_{F}$. Then a linear mapping $T$ from $E$ into $F$ is determined by its restriction $T_{O}$ to $E_{\mathbb{R}}$, and $T_{o}$ can be written in the form $T_{0}=T_{1}+\mathrm{iT}_{2}$ with real-linear mappings $\mathrm{T}_{\mathrm{j}}$ from $\mathrm{E}_{\mathbb{R}}$ into $\mathrm{F}_{\mathrm{R}}$ * Thus $L(E, F)$ is the complexification of the real linear space $L\left(E_{\mathbb{R}^{\prime}} F_{\mathbb{R}}\right)$, With the above notation, $T$ is called real if $T_{2}$ is $=0$, positive if $T$ is real and $T_{1}$ is positive, and a lattice homomorphism if $T$ is real and $T_{1}$ is a lattice homomorphism. Lattice homomorphisms are characterized by the equality $|T h|=T|h|$ as in the real case.

## 8. THE SIGNUM OPERATOR

We discuss in some detail how a mapping of the form

$$
g \rightarrow(\operatorname{sign} f) g
$$

which has an obvious meaning, depending on $f$, in spaces $C(K)$, can be defined in an abstract complex Banach lattice. We prove the following:

Let $E$ be a complex Banach lattice and let $f \in E$. If either $E$ is order-complete or $|f|$ is a quasi-interior point in $E_{+}$, then there exists a unique linear mapping $S_{f}$, called the signum operator with respect to $f$, with the following properties:
(i) $S_{f} \bar{f}=\{$, where $\bar{f}=$ Re $f-i=I m f$
(ii) $\left|S_{f} G\right| \leqq|g|$ for every $g$ in $E$
(iii) $s_{f} g=0$ for every $g$ in $E$ orthogonal to $f$.

In fact, if $E=C(K)$ and if $|f|$ is a quasi-interior point in $E$, then $|f|$ is a strictly positive function and multiplication with the function sign $f=f \cdot|f|^{-1}$ has the desired properties. Uniqueness follows from Zaanen (1983) Chap. 20. We reduce the general situation to the case just considered in the following way:

1. If $|f|$ is quasi-interior to $E_{+}$, then $E|f|$ is a dense subspace of $E$ isomorphic to a space $C(K)$, and with the above arguments one gets a uniquely determined operator $s_{o}$ on $E|f|$ with the desired properties. Since (ii) implies the continuity of $s_{o}$ for the norm induced by $E, S_{o}$ can be extended to $E$.
2. If $f$ is arbitrary, then as above one gets an operator $S_{o}$ on $E|f|$ with (i) - (ii). If $E$ is order complete, an extension $S_{f}$ of $S_{o}$ to $E$ satisfying (i) (iii) is possible as soon as $S_{o}$ can be extended to the band $\{x\}^{d d}$ of $E$ : on the complementary band $\{x\}$ one has necessarily the values $\because 0$ for $s_{f}$. The extension to $\{x\} d$ is obtained as follows:
If $S_{o}$ is positive (which means $f \geqq 0$ ) then

$$
s_{f} h=\sup \left\{S_{f} g: g \in[0, h] n E|f|\right\} \quad(h \quad \text { द } 0)
$$

will do. In general, the problem can be reduced to this situation by decomposing $S_{0}$ into a sum of the form $S_{o}=\left(S_{1}-S_{2}\right)+i\left(s_{3}-s_{4}\right)$
with positive operators $S_{j}$. Such a decomposition of $S_{o}$ exists since the order completeness of $E$ implies the order completeness of ${ }^{E}|f|=C(K)$ and since every continuous Iinear operator on a space $C(K)$ is necessarily order-bounded.

## 9. THE CENTER OF L(E)

We give a short description of a special, but important class of operators.
Let $E$ be a (complex) Banach lattice. For $T \in \mathbb{E}(E)$ the following conditions are equivalent:
(a) f $\perp \mathrm{g}$ implies $\mathrm{Tf} \perp \mathrm{g} \quad(\mathrm{f}, \mathrm{g} \in \mathrm{E})$
(b) $\pm T \leq\|T\| I d$
(c) $T J \subset J$ for every ideal $J$ in $E$.

If $E$ is countably order complete, then this is equivalent to:
(d) $T J \subset J$ for ervery projection band $J$ in $E$.

The last assertion also means that $T$ commutes with every band projection.
The set of all $T \in L(E)$ satisfying the above conditions is called the center of $L(E)$ and denoted $Z(E)$. $Z(E)$ is under the natural ordering, the operator norm and the composition product isomorphic to a Banach lattice algebra $C(K)$ ( $K$ compact). The following examples may illustrate the situation and explain why the term "multilication operator" is often used for operators in $Z(E)$.
(i) If $E=L^{P}(X, \Sigma, \mu) \quad(1 \leqq p \leqq \infty)$ with $\sigma$-finite $\mu$, then $Z(E)$ is isomorphic to $L^{\infty}(\mu)$ via the natural identification of a function $f \in L^{\infty}(\mu)$ with the multiplication operator $g * f * g$ on $E$.
(ii) If $X$ is Iocally compact, $E=C_{o}(X)$ then similarly $Z(E) \cong C^{b}(X)$ via the identification of $f \in C^{b}(X)$ with the mapping

$$
g \rightarrow f \cdot g \quad\left(g \in C_{o}(X)\right)
$$

