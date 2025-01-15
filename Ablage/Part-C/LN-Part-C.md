\title{
POSITIVE SEMIGROUPS ON BANACH LATTICES
}

\author{
CHAPTER C-I \\ ![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-249.jpg?height=44&width=1454&top_left_y=820&top_left_x=298) \\ AND POSITIVE OPERATORS \\ by \\ Rainer Nagel and U1f Schlotterbeck
}

This introductory chapter is intended to give a brief exposition of those results on Banach lattices and ordered Banach spaces which are indispensable for an understanding of the subsequent chapters. We do not want to give proofs of the results we are going to present, since these can easily be found in the literature (e.g., in Schaefer 1974). We rather want to give the reader who is unfamiliar with these results or with the terminology used in this book the necessary informatjon for an intelligent reading of the main discussions. Since relatively few general results on ordered Banach spaces are needed, we will primarily talk about Banach lattices. The scalar field will be $\mathbb{R}$ except for the last three sections, where complex Banach lattices will be discussed.

The notion of a Banach lattice was devised to get a common abstract setting within which one could talk about phenomena related to positivity that had previously been studied in various types of spaces of real-valued functions, such as the spaces $C(K)$ of continuous functions on a compact topological space $K$, the Lebesgue spaces $L^{l}(\mu)$ or more generally the spaces $L^{P}(\mu)$ constructed over a measure space ( $\mathrm{X}, \mathrm{F}, \mu$ ) for $\mathrm{l} \leq \mathrm{p} \leq \infty$. Thus it is a good idea to think of such spaces first in order to get a feeling for the concrete meaning of the abstract notions we are going to introduce. Later we will see that the connections between abstract Banach lattices and the "concrete" function lattices $C(K)$ and $L^{1}(\mu)$ are closer than one might think at first. We will use without further explanation the terms order relation (orderingl, ordered set, majorant, minorant, supremum, infimum.

By definition, a Banach lattice is a Banach space (E,\| \|) which is endowed with an order relation, usually written $\leqq$, such that ( $\mathrm{E}, \mathrm{S}$ ) is a lattice and the ordering is compatible with the Banach space structure of $E$. We are going to elaborate this in more detail now.

The axioms of compatibility between the linear structure of $E$ and the order are as follows:
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-250.jpg?height=124&width=1505&top_left_y=783&top_left_x=224)

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
\begin{tabular}{ll} 
(i) & $|h| \in G$ for all \\
(ii) & $h^{+} \in G$ \\
(iii) & $h^{-} \in G$ for all \\
( & $h \in G$ all \\
& $h \in G$.
\end{tabular}

A subset $B$ of $a$ vector lattice is called solid if $f \in B,|g| \leq|f|$ implies $g \in B$. Thus a norm on a vector lattice is a lattice norm if and only if its unit ball is solid. A solid linear subpace is called an ideal. Ideals are automatically vector sublattices since |sup(f,g)| $\leq|f|+|g|$. On the other hand, a vector sublattice $F$ is an ideal in $E$ if $g \in F$ and $0 \leqq f \leqq g$ imply $f \in F$. A band in a vector Iattice $E$ is an ideal which contains arbitrary suprema, more ex-
actly: $B$ is a band in $E$ if $B$ is an ideal in $E$ and sup $M$ is contained in $B$ whenever $M$ is contained in $B$ and has a supremum in $E$. Since the notions of sublattice, ideal, band are invariant under the formation of arbitrary intersections there exists, for any subset $B$ of $E$, a uniquely determined smallest sublattice (ideal, band of $E$ containing $B$ : the sublattice (ideale band) generated by B.
If we denote by $B^{d}$ the set $\{h \in E: \inf (|h|,|f|)=0$ for all $f \in B\}$, then $B^{d}$ is a band for any subset $B$ of $E$, and $\left(B^{d}\right)=B^{d d}$ is a band containing $B$. If $E$ is a normed vector lattice (more generally, if $E$ is archimedean ordered, see e.g. Schaefer (1974)), then $\mathrm{B}^{\mathrm{dd}}$ is the band generated by B .

If two ideals $I$, $J$ of a vector lattice $E$ have trivial intersection $\{0\}$, then $I$ and $J$ are Iatticedisjoint, i.e, $I \in J^{d}$. Thus if $E$ is the direct sum of two ideals $I$, J then one has automatically $I=J^{d}$ and $J=I^{d}$, hence $I=I^{d d}$ and $J=J^{d d}$ must be bands in this situation. In general, an ideal $I$ need not have a complementary ideal $J$, even if $I=I d$ is a band. This amounts to the same as saying that even if $I=I^{d d}$ (which is always true if I is a band in a normed vector lattice) one need not necessarily have $E=I+I^{d}$. An ideal $I$ is called a projection band if it does have a complementary ideal, and in this case the projection of $E$ onto I with kernel $I^{d}$ is called the band projection belonging to I . An example of a band which is not a projection band is furnished by the subspace of $C([0,1])$ consisting of the functions vanishing on [0.1/23 . The Riesz Decomposition Theorem asserts that in an order complete vector lattice every band is a projection band. As a consequence, if $E$ is order complete and $B$ is an arbitrary subset of $E$, then $E$ is the direct sum of the complementary bands $B^{d}$ and $B^{d d}$. This Theorem, which is quite easy to prove, is widely used in Analysis and gives an abstract background to, e.g., the decomposition of a measure into atomic and diffuse parts (the atomic measures being those contained in the band generated by the point measures, the diffuse measures those disjoint to the latter) or, more specifically, to the well-known decomposition of a measure on $[a, b]$ into an atomic part and a diffuse part, which latter can in turn be decomposed into the sum of a measure which is absolutely continuous (which means, contained in the band generated by Lebesgue measure) and a singular measure (which means, a diffuse moasure disjoint to lebesgue measure).

A band in a normed vector lattice is necessarily closed. By contrast, an ideal need not be closed, but the closure of an ideal is again an ideal. The situation where every closed ideal is a band will be briefly discussed in Section 5 .
2. ORDER UNITS, WEAK ORDER UNITS, QUASI-INTERIOR POINTS

An element $u$ in the positive cone of a vector lattice $E$ is called an order unit, if the ideal generated by u is all of $E$. If the band generated by $u$ is all of $E$ (which is equivalent to $\{u\}=0$ whenever $E$ is archimedean, hence in particular if $E$ is a normed vector latticel then $u$ is called a weak order unit of $E$. If $E$ is a Banach lattice, then any order unit in $E$ is an interior point of the positive cone $E_{+}$, and conversely any interior point of $E_{+}$must be an order unit of $E$. Every space $C(K)$ has order units fnamely, the strictly positive functions), and conversely by the Kakutani-Krein Representation Theorem (see Section 4) every Banach lattice with an order unit is isomorphic to a space $C(K)$. If an element $u$ in the positive cone of a Banach lattice $E$ has the property that the closed ideal generated by $u$ is all of $E$, then $u$ is called a guasi-in= terior point of $E_{+}$. Quasi-interior points of the positive cone exist, e.g., in any separable Banach lattice. If $E=C(K)$, then the quasi-interior points and the interior points of $E_{+}$coincide, while the weak order units of $E$ are the (positive) functions vanishing on a nowhere dense subset of $K$. If $E$ is a space $\mathrm{L}^{\mathrm{P}}(\boldsymbol{\mu})$ with o-finite $\mu$ and $1 \leqq p<\infty$, then the weak order units and the quasi-interior points of $E_{+}$coincide with the functions strictly positive u-a.e., while $E_{+}$does not contain any interior point.

\section*{3. LINEAR FOXMS AND DUALTTY}

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

\section*{4. AM- AND AL-SPACES}

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

\section*{7. COMPLEX BANACH LATTICES}

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

\section*{8. THE SIGNUM OPERATOR}

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

\section*{9. THE CENTER OF L(E)}

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

\title{
CHARACTERIZATION OFPOSITIVESEMIGROUPS \\ ON BANACH LATMICES \\ by \\ Wolfgang Arendt
}

In this chapter our first goal is to find conditions on a generator A of a semigroup $(T(t)) t \geqslant 0$ which are equivalent to the positivity of the semigroup. After the preparations in $A-I I, s e c .2$ this is easy if in addition we ask that the semigroup be contractive: $T(t)$ is a positive contraction for all $t \leq 0$ if and only if A is dispersive (Section l). For arbitrary (not necessarily contractivel semigroups a condition on the generator had been found in the case when $E=C(K)$ ( $K$ compact), namely the positive minimum principle (P) (see B-II). One may easily reformulate this condition in arbitrary Banach lattices and show its necessity. However, only in special cases (for example if A is bounded (see Section 1)) the positive minimum principle is sufficient for the positivity of the semigroup. In fact, on $L^{2}(R)$ there exists a non-positive semigroup whose generator satisfies (Section 3).

Looking for another condition we consider the Laplacian $\Delta$ as a prototype. Defined on a suitable domain, 4 generates a positive semigroup on $L^{P}\left(\mathbb{F}^{n}\right)$. Kato proved the following distributional inequality for the Laplacian:
$$
(\operatorname{sign} \bar{f}) \Delta f \Delta \Delta|f|
$$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-263.jpg?height=84&width=1626&top_left_y=2157&top_left_x=221) that an abstract version of Kato's inequality for a generator $A$ together with an additional condition is equivalent to the positivity of the semigroup generated by $A$.

Domination of one semigroup by another can be characterized by an analoguous condition for the generators (Section 4). The results will be applied to schrodinger operators on $L^{P}\left(\mathbb{R}^{n}\right)$.

Finally, in Section 5 we show that $(T(t))$ teo is a lattice semigroup
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-264.jpg?height=56&width=1606&top_left_y=326&top_left_x=239) satisfies Kato's equality. This parallels the case when $E=C_{o}(X)$, but if $E$ has order continuous norm the strong form of Kato's equality can be considered (in particular, $f \in D(A)$ implies $|f| \in D(A)$ if $A$ is the generator of such a semigroupl.

\section*{1. POSITIVE CONTRACTION SEMIGROUPS AND BOUNDED GENERATORS}

In this section we first characterize generators of positive contrac* tion semigroups on a real Banach lattice E .
For that we use the results developed in A-II, section 2 for the canonical half-norm $\mathrm{N}^{+}: \mathrm{E} \rightarrow \mathbb{R}$ given by
$$
\begin{equation*}
\mathrm{N}^{+}(\mathrm{f})=\left\|\mathrm{f}^{+}\right\| \quad(\mathrm{f} \in \mathrm{E}) \tag{1.1}
\end{equation*}
$$

Remark. It is, easy to see that $N^{+}(f)=\inf \left\{\|f+g\|: g \in E_{+}\right\}=$ dist (-f.E $\left.\mathrm{E}_{+}\right)(\mathrm{cf}, \mathrm{A}-\mathrm{II}$, Rem. 2.8 ).

It is obvious that $N^{+}$is a strict half-norm (see $A-I I,(2.12)$ ). The subdifferential of $N^{+}$is given by
(1.2) $\mathrm{CN}^{+}(f)=\left\{\phi \in \mathrm{E}_{+}^{\prime}:\|\phi\| \leqq 1,\langle f, \phi\rangle=\left\|\mathrm{f}^{+}\right\|\right\}$
(this follows from the definition, see $A-I I$, (2.5)).

Examples 1.1. a) Let $E=C_{o}(X)(X \quad$ locally compact). Let $f \in E$. There exists $: \in X$ such that $f(x)=\left\|f^{+}\right\|_{\infty}$. Then $\delta_{x} \in d N^{+}(f)$.
b) Let $E=L^{P}(X, \Sigma, \mu)$, where $(X, \Sigma, \mu)$ is a ofinite measure space and $\mathbf{l}<\mathrm{p}<\infty$. Let $\mathrm{f} \in \mathrm{E}$ satisfy $\mathrm{f}^{+} \neq 0$. Let
$$
\phi(x) \quad= \begin{cases}c \cdot f(x)^{p-1} & \text { if } f(x)>0 \\ 0 & \text { if } f(x) \leqq 0\end{cases}
$$
where $c>0$ is such that $\int E(x) \phi(x) d x=\left\|f^{+}\right\|$. Then $2 \mathrm{~N}^{+}(\mathrm{f})=\{\phi\}$.
c) Let $E=L^{I}(X, \Sigma, \mu)$, where $(X, \Sigma, \mu)$ is a $\quad(X$-finite measure space, and $f \in E$. Let $\phi \in L^{\infty}(X, \Sigma, \mu)+$. Then $\phi \in d N^{+}(f)$ if and only if
$\phi(x)=1$ if $f(x)>0$,
$0 \leq \phi(x) \leqq 1$ if $f(x)=0$ and
$\phi(x)=0 \quad$ if $f(x)<0$.

An operator $A$ on $E$ is called [strictly] dispersive if $A$ is
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-265.jpg?height=64&width=1620&top_left_y=319&top_left_x=207) $\langle A f, \phi\rangle \approx 0$ for some [resp., all] $\phi \in d N^{+}(f)$ (see A-II,sec. 2). Generators of positive contraction semigroups are characterized by the following theorem which is due to Phillips (1962).

Theorem 1.2. Let $A$ be a densely defined operator on a real Banach lattice $E$. The following assertions are equivalent.
(i) A is the generator of a positive contraction semigroup.
(ii) A is dispersive and ( $\lambda-A$ ) is surjective for some $\lambda>0$.

Frequently an operator is known explicitly only on a core. In that case one can use the following result.

Corollary 1.3. Let $A$ be a densely defined dispersive operator on a real Banach lattice $E$. If (A - A)D(A) is dense in $E$ for some $\lambda>0$, then $A$ is closable and the closure $\bar{A}$ of $A$ is the generator of a positive contraction semigroup.

Theorem 1.2 and Corollary 1.3 immediately follow from A-II, Thm. 2.ll and A-II, Cor.2.l2 if one observes the following.

Lemma 1.4. A bounded linear operator $T$ on a Banach lattice $E$ is a positive contraction if and only if $\left\|_{1}(T f)^{+}\right\| \leq f^{+} \|$for all $f \in E$ (i.e., if $T$ is $\mathbb{N}^{+}$-contractive).

Proof of the Iemma- If $T$ is a positive contraction, then $0 \leqslant(T f)+$ $\leqq \mathrm{Tf}^{+}$and so $\mathrm{N}^{+}(\mathrm{Tf}) \leq\left\|\mathrm{Tf}^{+}\right\| \leq\left\|_{\Gamma^{+}}^{+}\right\|_{i}=N^{+}(f)$ for all $f \in$ E. Conversely, assume that $T$ is an $N^{+}$-contraction. Let $f$ \& 0 . Then $\left\|(T f)^{-}\right\|=N^{+}(T(-f)) \leqq N^{+}(-f)=\left\|f^{-}\right\|=0$. Hence $(T f)^{-}=0 ; i, e$, Tf $>0$. We have proved that $T$ is positive. In particular,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-265.jpg?height=61&width=1609&top_left_y=2077&top_left_x=212) $\leqq N^{+}(|f|)=\|f\|$ for all $f \in E$. So $T$ is a contraction.

Examples 1.5. a) Consider the second derivative with Dirichlet boundary condition on $E=C_{0}(0,1) ; i . e$. we let $A f=f^{\prime \prime}$ with domain $D(A)=\left\{f \in C^{2}[0,1]: f(0)=f(1)=f^{\prime \prime}(0)=f^{\prime \prime}(1)=0\right\}$.
$A$ is dispersive. In fact, let $f \in D(A)$. Then there enists
$x \in(0,1)$ such that $f(x)=\sup _{y \in[0,1]} f(y)=\left\|f^{+}\right\|_{\infty}$. Thus
$\delta_{x} \in \mathrm{dN}^{+}(f)$. But $\left\langle A f, \delta_{x}\right\rangle=f^{\prime \prime}(x) \leqq 0$ since $f$ has a maximum in $x$. Let $g \in E$. Define $f_{0}(x)=1 / 2\left[e^{x} \int_{x}^{1} e^{-Y} g(y) d y-e^{-x} \int_{x}^{I} e^{y} g(y) d y\right]$.

Then $f_{O} \in C^{2}[0, I]$ and $f_{O}-f_{O_{x}}=g$. There exist a, b $\in$ in such that $f(x)=f_{0}(x)+a e^{x}+b e^{-x}$ defines a function $f \in c^{2}[0,1]$ satisfying $f(0)=f(1)=0$. Since $f-f^{\prime \prime}=f_{0}-f_{0}^{r}=g$ this implies that $f \in D(A)$ and $f-A f=g$. We have shown that (Id - A) is surjective. It follows from Thm.l.2 that $A$ is the generator of a positive contraction semigroup.
b) Let $E=L^{P}[0,1] \quad(1 \leq p<\infty)$ and $A$ be given by $A f=f "$ on $D(A)=\left\{f \in E: f \in C^{l}[0,1], f^{\prime} \in A C[0,1], f^{\prime \prime} \in L^{P}[0,1], f(0)=\right.$ $f(1)=0\}$. Then $A$ is the generator of a positive contraction semigroup.

Proof. A is dispersive. In fact, let $f \in D(A)$. Since the set $M=\{x \in(0,1): f(x)>0\}$ is open, there exists a countable set of disjoint intervals $\left(a_{n}, b_{n}\right)$ such that $M=b_{n \in N}\left(a_{n}, b_{n}\right)$. First case: $p>1$.
Let $\phi \in d N^{+}(f)$. Then there exists $c \geqslant 0$ such that $\phi(x)=c f(x)^{p-1}$ for all $x \in M$ and and $\phi(x)=0$ if $f(x) \leqq 0$ (see Er. I.1b). Thus integration by parts yields
$$
\begin{aligned}
\langle A f, \phi\rangle & =\sum_{n} \int_{a_{n}}^{b_{n}} f^{\prime \prime}(x) \phi(x) d x \\
& =-c \sum_{n} \int_{a_{n}}^{b_{n}} f^{\prime}(x) f^{\prime}(x)(p-1) \neq(x)^{p-2} d x \\
& \leqq 0 .
\end{aligned}
$$

Second case: $p=1$.
Let $\phi(x)=1$ for $x \in M$ and $\phi(x)=0$ for $x \& M$. Then
$\phi \in \mathrm{CN}^{+}(\mathrm{f})$ and
$\langle A f, \phi\rangle=\sum_{n} \int_{a_{n}}^{b_{n}} f^{\prime \prime}(x) d x=\sum_{n}\left(f^{\prime \prime}\left(b_{n}\right)-f^{\prime}\left(a_{n}\right)\right) \leq 0$
since $f^{\prime}\left(b_{n}\right) \leqq 0$ and $f^{\prime \prime}\left(a_{n}\right) \geqq 0$ for all $n$.
We have shown that $A$ is dispersive. As in al one shows that
(Id - A) is surjective. Now the claim follows from Thm.1.2,
c) Consider $E=C_{0}\left(\mathbb{R}^{n}\right)$. Let $D(A)=S\left(\mathbb{R}^{n}\right)$ (the Schwartz space of all infinitely differentiable rapidly decreasing functions) and Af $=A f$ (f $\in D(A))$. Then $A \quad 1 s$ closable and the closure of $A$ generates a positive contraction semigroup on $E$.

Remark. In addition one can show that the closure $\overline{\mathrm{A}}$ of A is given by $\bar{A} f=\Delta f$ with domain $D(\bar{A})=\{f \in E: \Delta f \in E\}$ where for
$f \in C_{0}\left(\mathbb{R}^{n}\right)$ the expression $\Delta f$ is understood in the sense of distributions. Moreover, the space $C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ (of all infinitely differentiable functions with compact support) is a core of $\bar{A}$ (cf. d).

Proof. $A$ is dispersive. In fact, let $f \in D(A)$. If $f^{+}=0$, then $\phi:=0 \in \mathrm{CN}^{+}(\mathrm{f})$. So assume that $\mathrm{f}^{+} \neq 0$. Then there exists $\mathrm{x} \in \mathbb{R}^{\mathrm{n}}$ such that $f(x)=\|f\|_{\infty}=\sup \left(f(y) \quad ; y \in \mathbb{R}^{n}\right\}$. Thus $\delta_{z} \in d N^{+}(f)$, Since $f$ has a maximum in $x$ it follows that
$\left\langle A f, \delta_{x}\right\rangle=(\Delta f)(x)=\operatorname{tr}\left(\partial^{2} f / \partial x_{i} \partial x_{j}\right)(x) \leq 0$. Moreover,
(I.3) (Id - 4) is an isomorphism from $S\left(\mathbb{R}^{n}\right)$ onto $S\left(\mathbb{R}^{n}\right)$.

In fact, the Fourier transform $f \quad \hat{f}$ is a bijection from $S\left(\mathbb{R}^{n}\right)$ onto $S\left(\mathbb{R}^{n}\right)$.
But $[(I C-\Delta) f]^{\wedge}=M \hat{f}$ where $(M g)(y)=\left(1+\sum_{i=1}^{n} y_{i}^{2}\right) g(y)$
$\left(g \in S\left(\mathbb{R}^{n}\right)\right.$ ). It follows from (I. 3) that (Id - A)D(A) is dense in $E$. So the claim follows from cor. 1.3 .
d) Let $E=L^{P}\left(\mathbb{R}^{n}\right) \quad(1 \leqq p<\infty)$ and $A$ be given by $A f=A f$ with comain $D(A)=\left\{f \in L^{P}\left(\mathbb{R}^{n}\right): \Delta f \in L^{P}\left(\mathbb{R}^{n}\right)\right\}$ where for $f \in L^{P}\left(\mathbb{R}^{n}\right)$ the expression $\Delta f$ is understood in the sense of distributions. Then $A$ is the generator of a positive contraction semigroup. Moreover, the space $C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ is a core of $A$.

Proof. It is easy to see that $A$ is closed. Let $A_{o}$ denote the restriction of $A$ to $S:=S\left(R^{n}\right)$. Then $A_{o} f=A f$ in the classical sense for all $f \in S$. One can show in an analogous way as in b) that Ao is dispersive. Moreover, it follows from (I. 3 ) that
$\left(I d-A_{o}\right) D\left(A_{o}\right)$ is dense. Hence by Cor. 1.3 the closure $\bar{A}_{o}$ of $A_{o}$ is the generator of a positive contraction semigroup.
By construction one has $\bar{A}_{o} G A$. We prove that $\bar{A}_{o}=A$. For that it is enough to show that
(I.4) (Id - A) is injective.

In fact, since the restriction (Id - $\bar{A}_{\mathrm{o}}$ ) of (Id - A) is bijective from $D\left(\bar{A}_{o}\right)$ onto $E$ it follows from (1.4) that $D\left(\bar{A}_{o}\right)=D(A)$. so let us show (I.4). Assume that there is f $\in E$ such that $f-A f=0$. Let $\phi \in C_{C}^{\infty}\left(R^{n}\right)$. Then
$$
\begin{equation*}
\langle\phi-\Delta \phi, f\rangle=0 . \tag{1.5}
\end{equation*}
$$
since $C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ is dense in $S$ for the topology of $S$, it follows from (1.3) that (Id - 4) $C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ is dense in $S$. Hence (1.3) implies
that $\langle\phi, f\rangle=0$ for all $\phi \in S$. Consequently, $f=0$.

Remark. Using the Fourier transform one can show that the semigroups in example c) and d) are given by
$$
\begin{equation*}
(T(t) f)(x)=(4 \pi t)^{-n / 2} \int_{\mathbb{R}^{n}} \exp \left(-(x-y)^{2} / 4 t\right) f(y) d y \tag{1.6}
\end{equation*}
$$
$(f \in E)$, where $z^{2}:=\sum_{i=1}^{n} z_{i}^{2} \quad\left(z \in \mathbb{R}^{n}\right)$.
e) The following example is the analog of a) for higher dimension. Let $\Omega \in \mathbb{R}^{n}$ be a bounded open and connected set and $E=C_{0}(\Omega)$. We assume that the Dirichlet problem
$$
\begin{array}{ll}
u(x)-\Delta u(x)=0 & (x \in a) \\
u(x)=b(x) & (x \in a \Omega) \tag{1.7}
\end{array}
$$
has a solution $u \in C^{2}(\Omega)$ п $C(\bar{\Omega})$ for every $b \in C(\partial \Omega)$ - For example, this is the case if the boundary $a \Omega$ is $c^{2}$ (see fGilbarg-Trudinger (1977), Thm. 6.13]).

Let $A$ be given by $A f=\Delta f$ on
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-268.jpg?height=80&width=924&top_left_y=1388&top_left_x=226)
Then $A$ is closable and the closure of $A$ is the generator of a positive contraction semigroup.

Proof. D(A) is clearly dense in $E$. Moreover, one can show as in c) that $A$ is dispersive. It remains to prove that (Id - A)D(A) is dense in $E$. The space $C_{c}^{\infty}(\Omega)$ of all infinitely differentiabel functions on $a$ with compact support contained in $\Omega$ is dense in $E$. Let $g \in C_{c}^{\infty}(\Omega)$. We show that there exists $f \in D(A)$ satisfying $(I d-A) f=g$. Let $\bar{g}: \mathbb{R}^{n} \rightarrow \mathbb{R}$ be given by $\bar{g}(x)=g(x)$ if $x \in \Omega$ and 0 if $x \notin \Omega$. Then $\bar{g} \in S\left(R^{n}\right)$. By (I.3) there exists $\bar{f} \in S\left(\mathbb{R}^{n}\right)$ such that $\bar{f}-\Delta \bar{f}=\bar{g}$. Consider the function $b \in C(a \Omega)$ given by $b(x)=\bar{f}(x)$ for all $x \in a \Omega$. Then by our hypothesis there exists $u \in C(\bar{a}) \quad \mathcal{O}^{2}(\Omega)$ satisfying (1.7). Let $f(x)=\bar{f}(x)-u(x)$ $(x \in \bar{\Omega})$. Then $f \in C^{2}(\Omega) \cap C_{0}(\Omega)$ and $(f-\Delta f)(x)=g(x) \quad(x \in \bar{\Omega})$. Thus $A f=f-g$ vanishes on $\partial \Omega$. Hence $f \in D(A)$ and $f-A f=g$.
f) Let $\Omega \in \mathbb{R}^{n}$ be as in el and $E=L^{\mathrm{P}}(\Omega)$. Define $A f=A f$ on $D(A)=\left\{f \in C^{2}(\Omega) \cap C_{0}(\Omega): \Delta f \in C_{o}(\Omega)\right\}$. Then $A$ is closable and the closure of $A$ is the generator of a positive contraction semigroup on E.

Proof. D(A) is dense and one can show in an analoguous manner as in b) that $A$ is dispersive. We know from $d$ ) that $C_{C}^{\infty}(\Omega) \subset(I d-A) D(A)$. Thus (Id - A)D(A) is dense in $E$ and the claim follows from Cor.1.3.

We now turn to the problem to characterize generators of arbitrary (not necessarily contractive) positive semigroups. of course, as in B-II, Sec.l one sees that a semigroup $(T)(t))$ teo is positive if and only if $R(\lambda, A) \geq 0$ for all $\lambda>\omega(A)$ where $A$ denotes the generator of (T(t)) $t \geqq 0$. We are looking for an intrinsic condition on $A$.

The positive minimum principle which is characteristic for generators of strongly continuous semigroups on $C(K)$ (see $B-I I, T h m .1 .6)$ can be reformulated on an arbitrary Banach lattice $E$.

Definition I.6. An operator $A$ on $E$ satisfies the positive minimum principle if for all $f \in D(A)_{+}, \phi \in E_{+}^{\prime}$,
(P) $\langle f, \phi\rangle=0$ implies $\langle A f, \phi\rangle \geq 0$.

Remark. It is easy to see that this definition coincides with that given in $B-I I$ sec.l in the case when $E=C(K)$ ( $K$ compact). [In fact, suppose that for all $f \in D(A)+$ and $x \in K, f(x)=0$ implies (Af) ( $x$ ) $\geqslant 0$, Let $g \in D(A)_{+}, \mu \in M(K)+$ such that $\langle g, \mu>=0$. Then $g(x)=0$ for all $x \in \operatorname{supp} \mu$. Thus by hypothesis, (Ag) (x) $\geqq 0$ for all $x \in \operatorname{supp} \mu$. Consequently $\langle A g, \mu>\geqq 0$. This proves one direction. The other is obvious by considering point measures.]

Proposition 1.7. The generator of a strongly continuous positive semigroup satisfies the positive minimum principle (P).

Proof. Let $(T(t))_{t \geqslant 0}$ be a strongly continuous positive semigroup with generator $A$ and $0 \leqq f \in D(A), \phi \in E_{+}^{\prime} \operatorname{such}$ that $\langle f, \phi\rangle=0$. Then $\left.\langle A f, \phi\rangle=\lim _{t \rightarrow 0} I / t<T(t) f \rightarrow f, \phi\right\rangle=\lim _{t \rightarrow 0} 1 / t\langle T(t) f, \phi\rangle \geqq 0$.

We will see that the positive minimum principle is not sufficient for the positivity of the semigroup, in general (Remark 3.16). However, the following special case is of interest.

Theorem 1.8. Let $A$ be the generator of a strongly continuous semigroup ( $T(t))_{t \geq 0}$ on a Banach lattice $E$. Assume that
a) there exists $w \in \mathbb{R}$ such that $\|T(t)\| \leqq e^{w t}$ for all $t$ a ;
b) there exists a core $D_{o}$ of $A$ such that $f \in D_{o}$ implies $|f| \in D_{o}$.
If the restriction of $A$ to $D_{o}$ satisfies the positive minimum principle, then the semigroup is positive.

Remark. Elementary examples show that neither a) nor b) hold for generators of positive semigroups, in general.

The proof of Theorem 1.8 is based on the following proposition.

Proposition 1.9. Let $A$ be a densely defined dissipative operator which possesses a core $D_{o}$ such that $f \in D_{o}$ implies $|f| \in D_{o}$. \#f the restriction of $A$ to $D_{o}$ satisfies the positive mindmum principle ( $P$ ), then $A$ is dispersive.

Proof. By A-II, Prop.2.9, it is enough to show that $A_{o}: A_{0} \|_{0}$ is dispersive.
Let $f \in D_{o}$ and $\phi \in \mathrm{CN}^{+}(f)$. Then $\phi \in E_{+}^{\prime},\|\phi\|_{\|} \leq 1$ and $\langle f, \phi\rangle=$ $\left\|\mathrm{f}^{+}\right\|$, Hence, $\left\langle\mathrm{f}^{-}, \phi\right\rangle=\left\langle\mathrm{f}^{-}, \phi\right\rangle+\left\langle\mathrm{f}_{\mathrm{t}} \phi\right\rangle-\left\|\mathrm{f}^{+}\right\|=\left\langle\mathrm{f}^{+}, \phi\right\rangle-\left\|_{i} \mathrm{f}^{+}\right\|_{\|} \leqq 0$. Thus $\left\langle f^{-}, \phi\right\rangle=0$. Consequently, $\left\langle\hat{f}^{+}, \phi\right\rangle=\langle f, \phi\rangle=\left\|_{\|}^{+}\right\|_{i} ;$ and so $\phi \in \mathbb{d}\left(\mathrm{f}^{+}\right)$. Since A is dissipative it follows that $\left\langle\mathrm{A} \mathrm{f}^{+}, \phi\right\rangle \leq 0$. Moreover, since $A$ satisfies (P) we have $\left\langle A f^{-}, \phi\right\rangle \leqslant 0$. So we finally obtain, $\langle A f, \phi\rangle=\left\langle A f^{+} \phi\right\rangle-\left\langle A f^{-}, \phi\right\rangle \leqslant 0$.

Proof of Theorem I.8. The operator A - w satisfies (P) as well. So it follows from Proposition 1.9 that $A-w$ is dispersive. Consequently, the semigroup $\left(e^{-w t} T(t)\right) t \geqq 0$, which is generated by $A-W$, is positive. Thus $(T(t)) t \geqslant 0$ is positive as well.

Next we give a reformulation of the positive minimum principle. For $0<u \in E_{+}$we denote by $E_{u}$ the principal ideal generated by $u$. If $g \ell E_{+}$, then $g \in \bar{E}_{u}$ if and only if lim ${ }_{n+\infty}\left\|_{\|} u-n u \wedge g\right\|=0$.

Lemua 1.10. An operator $A$ on $E$ satisfies (P) if and only if
(1.8) (Au) ${ }^{-} \in \bar{E}_{u}$ for all $u \in D(A)+:=D(A) \cap E_{+}$.

Proof. Let $u \in D(A)+, g=A u$. Assume that $(A u)^{-} \epsilon \bar{E}_{u}$.
Then, if $0 \& \phi \in E_{+}^{\prime}$ such that $\langle u, \phi\rangle=0$ one has $\left\langle f_{r} \phi\right\rangle=0$ for all $f \in \bar{E}_{U^{\prime}}^{-}$hence $\left\langle(A u)^{-}, \phi\right\rangle=0$ and consequently $\langle A u, \phi\rangle \geqslant 0$. This proves one direction. To prove the other assume that $g^{-} \mathcal{F}_{u^{-}}^{-}$ Then there exists $\phi \in\left(E_{u}\right)^{\circ}$ such that $\left\langle g^{-}, \phi\right\rangle \neq 0$. Since ( $\left.E_{u}\right)^{\circ}$ has a generating cone (by [Schaefer (1974), II, 4.77), we can assurne that $\phi>0$.
Define $\psi_{o}(f)=\sup \phi\left([0, f] \quad \cap E\left(g^{-}\right)\right.$for $f \in E_{+}$. Then $\psi_{o}$ is positive homogeneous on $E_{+}$. Thus the linear extension of $\psi_{o}$ defines a positive linear form $\psi$ on $E$. We have $\left\langle g^{-}, \psi\right\rangle=\left\langle g^{-}\right.$, 中> $\rangle 0$ and $\left.<g^{+}, \psi\right\rangle=0$. Thus $\langle A u, \psi\rangle=-\left\langle g^{-}, \psi\right\rangle\langle 0$. But $\langle u, \psi\rangle \leqq$ $\langle u, \phi\rangle=0$. Thus (P) does not hold.

Bounced generators of positive semigroups can now be characterized as follows.

Theorem I.1I. Let $A$ be a bounded operator on a Banach lattice E. The following assertions are equivalent:
(i) $e^{t A} \geq 0(t \geq 0)$.
(ii) $f \in E_{+}, \phi \in E_{+}^{\prime},\langle f, \phi\rangle=0$ implies $\langle A f, \phi\rangle \geq 0$.
(iii) (Af) ${ }^{-} \overline{E_{f}}$ for all $f \in D(A)+$.
(iv) $A+\|A\|-I d \geq 0$.

Proof. It follows by Proposition 1.7 that (i) implies (ii). Since $\left\|e^{t A}\right\| e^{t\|A\|} \quad(t \geq 0)$, (ii) implies (i) by Theorem 1.8. The equivaJ.ence of (ii) and (iii) is established by Lemma l.lo. If (iv) holds, then $e^{t(A+\|A\|)} \geq 0 \quad(t \geqslant 0)$. Thus $e^{t A}=e^{-t\|A\|} e^{t(A+\|A\|)} \geqq 0 \quad$ (t?0). We have shown that (i), (ii) and (iii) are equivalent and (iv) implies (i).
It remains to show that (i) implies (iv). Since assertions (i) and (iv) are satisfied for $A$ if and only if they are satisfied for $A^{\prime}$, we can assume that $F$ is order complete (considering $A$ instead of A if necessary). Assume that (i) holds. Then by what we have proved above (iii) holds as well. In particular
(1.9) $(A u)^{-} \epsilon\{u\}^{d d}$ for all $u \in E_{+}$.

Let $\lambda E 0$ and $f \in E_{+}$such that $g=(A+\lambda) f \neq 0$. We have to show that $\lambda \&\|A\|$. Denote by $P$ the band projection onto the band generated by $g^{*}$. Then PAf $+\lambda P f=P g=g^{-}<0$. Since by (1.9), $[A(I d-P) f]^{*} \in\left(I A^{-} P\right) E$, it follows $0>\lambda P f+P A f=\lambda P f+P A P f+$ $\operatorname{PA}(I d-P) f=\lambda P f+P A P f+P(A(I d-P) f)^{+} Z \lambda P f+P A P f$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-272.jpg?height=50&width=1611&top_left_y=272&top_left_x=231) $\leq\|A\| \cdot\|P f\|$. Consequently $\lambda \leqq\|A\|$.

Remark 1.12. It follows from the proof of Theorem 1.11 that on a o -order complete Banach lattice condition (l.9) is equivalent to the positivity of the semigroup ( $\left.e^{t A}\right)$ $\geq 0$.

Examples I.13. Let $E=\ell^{\mathrm{P}} \quad\left(1 \leqq p \leqq \infty\right.$ or $E=c_{0}$.
a) An operator $A \in \mathbb{L}(E)$ can be canonically represented by a matrix ( $a_{i j}$ ) . It follows from Thm. 1.11 that $e^{t A} \geqq 0$ for all $t \geqslant 0$ if and only if $a_{i j} \geq 0$ whenever $i \neq j$.
b) Let $A$ be the generator of a strongly continuous contraction semigroup $(T(t))_{t \geq 0}$ on $E$. Suppose that the space $c_{o o}$ of all sequences which vanish off a finite set is a core of $A$. Let $\left(a_{n m}\right)_{m \in \mathbb{N}}=\left(A_{n}\right)$ where $e_{n}=\left(\delta_{n m}\right)_{m \in \mathbb{N}}$ denotes the $n^{t h}$ unit vector. Then it follows from Thm. 1.8 that the semigroup is positive if and only if $a_{n m} \geqq 0$ whenever $n \neq m$.

\section*{2. KATO's INEQUALITY}

A strongly continuous semigroup on $C(K)$ ( $K$ compact) or a norm continuous semigroup on an arbitrary Banach lattice is positive if and only if its generator $A$ satisfies the positive minimum principle (P). However, we will see that in general (P) is not sufficient for the positivity of the semigroup. One reason seems to be that (P) involves merely positive elements in $D(A)$ but $D(A)+$ can be small if the semigroup is not positive (cf. Remark 3.16). Our aim in this section is to find a different condition on the generator which is necessary for the positivity of the semigroup.

We recall from chapter c-I,sec.s definition and properties of the signum operator.

Proposition 2.1. Let $E$ be a omorder complete (real or complex) Banach lattice. For every $f \in E$ there exists a unique linear operator (sign f) on $E$ which satisfies
\begin{tabular}{lll} 
(2.1) & $|(s i g n f) g| \leqq|g|$ & $(g \in E)$ \\
$(2.2)$ & $(s i g n f) g=0$ & if inf $\{|f|,|g|\}=0$ \\
(2.3) & $(s i g n \bar{f}) f=|f|$ & (where $\bar{f}:=$ Ref - iImf).
\end{tabular}

The operator (siĝn f) (which is non-linear in general) is defined by (2.4) (sign f) $g=(\operatorname{sign} f) g+\left(I d-P_{|f|}\right)|g|$
where for $h \in E_{+}$we denote by $P_{h}$ the band projection onto the band $\{h\} d g^{+}$generated by $h$.

If $E$ is a real g-order complete Banach lattice, then
(2.5) $\operatorname{sign} f=P_{\left(f^{+}\right)}-P_{\left(f^{-}\right)}$.

Example 2.2. Let $f \in E:=L^{P}(X, \Sigma, \mu)$ (real or complex) where $(X, \Sigma, \mu)$ is a ofinite measure space and $I \leqslant p \leqslant \infty$. Define
$$
\operatorname{mi}(x)= \begin{cases}f(x) /|f(x)| & \text { if } f(x) \neq 0 \\ 0 & \text { if } f(x)=0 .\end{cases}
$$

Then sign f is the multiplication operator defined by m ; i.e.r

Moreover,
$$
\begin{array}{ll}
(\operatorname{sign} f) g=m \cdot g & (g \in E) \\
(\operatorname{sig} n f) g=m \cdot g+1_{[f(x)=0]}|g| & (g \in E)
\end{array}
$$

The operator sign $f$ is related to the Gateaux-derivative (B-II, Definition 3.2$)$ of the modulus. We explain this by an example.

Example 2.3. Let $E$ be the real or complex space $L^{P}(X, \Sigma, \mu)$ where $(X, E, \mu)$ is a definite measure space and $I \leqslant p<\infty$. Let $f, g \in E$ and $x \in X$. Then by B-II, Lenma 2.4
$\lim _{t+0} l / t(|f(x)+\operatorname{tg}(x)|-|f(x)|)= \begin{cases}\operatorname{Re}(\operatorname{sign} \overline{f(x)}) g(x) & \text { if } f(x) \neq 0 \\ \lg (x) \mid & \text { if } f(x)=0 .\end{cases}$
If $\quad \in E \rightarrow E_{+}$denotes the modulus function given by $\theta(h)=|h|$, then it follows from the dominated convergence theorem that $\theta$ is right-sided Gateaux-differentiable and
$$
\begin{equation*}
D_{g} \theta(f)=\operatorname{Re}(\operatorname{sign} \bar{f}) g \tag{2.6}
\end{equation*}
$$

Later we will see that (2.6) holds in every Banach lattice with order continuous norm.

Now let $A$ be the generator of a strongly continuous positive semigroup ( $T(t))_{t \geqslant 0}$. The positivity of the semigroup is equivalent to (2.7) $|T(t) f| \leq T(t)|f| \quad(t \geqslant 0, f \in E)$.

In order to deduce from (2.7) a property for the generator $A$ it is natural trying to differentiate (2.7) in $t=0$. Let us assume for a moment that $E=L^{P}(X, \Sigma, \mu)$ (as in Ex. 2.3).
Let $f \in D(A)$ and $0 \leq \phi \in D\left(A^{\prime}\right)$. Then by (2.7),
$(2.8)\langle | T(t) f|, \phi\rangle \leqslant T(t)|f|, \phi\rangle \quad(t \geqslant 0)$
where the equality holds for $t=0$. Hence the inequality remains valid if we differentiate in 0 on both sides of (2.8).
Since $\phi \in D\left(A^{\prime}\right)$ we obtain $d / d t|t=0<T(t)| f|, \phi\rangle=\langle | f\left|, A^{\prime} \phi\right\rangle$ on the right side. By (2.6) and the chain rule $B-I P_{p}$ prop. 2.3 one obtains $d / d t|t=0| T(t) f \mid=\operatorname{Re}((s i g n \operatorname{f}) A f) \quad$ on the left side.
Since $\operatorname{Re}((\operatorname{sign} \underset{f}{f}) A f) \leqslant \operatorname{Re}((s i \hat{g} n \bar{f}) A f)$, this finally gives
(K) $\left.\left.\quad \operatorname{Re}^{<}(\operatorname{sign} \bar{f}) A f, \phi\right\rangle \leqq<|f|, A^{\prime} \phi\right\rangle \quad\left(f \in D(A), 0 \leqq \phi \in D\left(A^{\prime}\right)\right.$.

We refer to this as Kato's ineguality , since it represents an abstract version of the classical incquality proved by kato for the Laplacian (see Erample 2.5).
We will see in the next Section that, together with an additional condition, this inequality is characteristic for the positivity of the semigroup.

By a different proof, we now show that Kato's inequality holds for generators of positive semigroups in general.

Theorem 2.4. The generator $A$ of a strongly continuous positive semigroup ( $\mathrm{T}(\mathrm{t}))_{\mathrm{t}}^{\mathrm{Z}} 0$ on a o-order complete (real or complex) Banach Iattice $E$ satisfies Kato's inequality; i.e.,
(K) $\left.\quad \operatorname{Re}\langle(\operatorname{sign} \bar{f}) A f, \phi\rangle \leqq<|f|, A^{\prime} \phi\right\rangle \quad\left(f \in D(A), 0 \leqq \phi \in D\left(A^{\prime}\right)\right)$.

Proof. Let $f \in D(A), 0 \leqq \phi \in D\left(A^{\prime}\right)$. Then
$$
\begin{aligned}
\langle(\operatorname{sign} \overline{\mathrm{f}}) \mathrm{Af}, \phi\rangle & \left.=\lim _{t \rightarrow 0} I / t<(\operatorname{sign} \overline{\mathrm{f}})(\mathrm{T}(\mathrm{t}) \mathrm{f}-\mathrm{f}), \phi\right\rangle \\
& =\underset{\substack{ \\
\lim _{t \rightarrow 0}}}{ } 1 / t<(\operatorname{sign} \overline{\mathrm{f}}) \mathrm{T}(\mathrm{t}) \mathrm{f}-|\mathrm{f}|, \phi> \\
& \left.\leq \lim _{t \rightarrow 0} I / t<|T(t) f|-|f|, \phi\right\rangle
\end{aligned}
$$
$$
\begin{aligned}
& \left.\leqq \lim _{t \rightarrow 0} 1 / t<T(t)|f|-|f|, \phi\right\rangle \\
& =\lim _{t \rightarrow 0}\langle | f\left|, 1 / t\left(T(t)^{\prime} \phi-\phi\right)\right\rangle \\
& =\langle | f\left|, A^{\prime} \phi\right\rangle
\end{aligned}
$$

Let $D\left(A^{\prime}\right)_{+}{ }^{+} E_{+}^{\prime} \cap D\left(A^{\prime}\right)$. Consicer the condition
$(2.9) \quad{\overline{D\left(A^{\prime}\right)}}_{+}^{\sigma}\left(E^{\prime}, E\right)=E_{+}^{\prime}$
(which is satisfied if the semigroup is positive). If (K) and (2.9) hold, then Kato's inequality holds in the strong form as well, whenever it makes sense; i.e.,
(2.10) Re((sign fif) $\leqslant A|f| \quad$ (whenever $f,|f| \in D(A))$.

Example 2.5. Kato's inequality in its classical form says the following (see Kato (1973) or [Reed-Simon (1975); X.27]).
Let $f \in \mathbb{L}_{l_{g C}}\left(\mathbb{R}^{n}\right)$ be such that the distributional Laplacian satisfies Af $\in L_{\text {loc }}^{I}\left(R^{\mathrm{K}}\right)$. Then the inequality
$$
\operatorname{Re}((\operatorname{sign} \bar{f}) \Delta f) \leqq \Delta|f|
$$
holds in the sense of distributions; i.e.,
$<\phi, \operatorname{Re}((s i g n \bar{f}) \Delta f)\rangle \leqslant<\phi, \Delta|f|>\quad(=<\Delta \phi,|f|>)$ holds for all
$0 \leqslant \phi \in C_{C}^{\infty}\left(\mathbb{R}^{n}\right)$. Note that the closure of $\Delta$ defined on $C_{C}^{\infty}\left(\mathbb{R}^{n}\right)$ generates a strongly continuous positive semigroup on $L^{p}\left(\mathbb{R}^{n}\right)$ $(1 \leq p<\infty)(s e e$ Example I.5.d and Example 4.7)).

We want to discuss the relation between the classical (distributional) inequality and our version given in Theorem 2.4.

Let
$$
A=\Gamma \quad|a| \leq m a_{a} D^{\alpha}
$$
be a differential operator, where $a_{d} \in C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$. Here we let
$D^{\alpha}=\left(\partial / \partial x_{1}\right)^{\alpha} 1 \ldots\left(\partial / \partial x_{n}\right)^{\alpha} n$ for all multi-indices $a=\left(\alpha_{1}, \ldots, \alpha_{n}\right)$
$\epsilon \mathbb{N}_{0}^{n} \quad\left(\mathbb{N}_{0}:=\mathbb{N u}\{0\}\right)$ of order $|a| t=\alpha_{1}+\ldots+a_{n}$
We say that $A$ satisfies Kato's inequality in the sense of distrim butions if
$\left(K_{d}\right) \quad \operatorname{Re}<((\operatorname{sign} \bar{f}) A f, \phi\rangle \leq<|f|, A^{*} \phi$
for all $f \in C_{C}^{\infty}\left(\mathbb{R}^{n}\right), 0 \leq \phi \in C_{C}^{\infty}\left(\mathbb{R}^{n}\right)$, where $A^{*}$ denotes the formal adjoint of $A$.
Let now $A$ be the generator of a positive semigroup ( $T(t)$ ) $t$ en on $E:=L^{P}\left(i R^{n}\right) \quad(1 \leq p<\infty)$ or $C_{o}\left(\mathbb{R}^{n}\right)$. Assume that there enists a core
$D_{o}$ of $A$ such that $C_{C}^{\infty} \subset D_{0}$ and $A f=A f$ in the sense of distributions for all f $\in \mathrm{D}_{\mathrm{O}}$. Then $A$ satisfies Kato's inequality in the sense of distributions.
In fact, let $0 \leqslant \phi \in C_{C}^{\infty}\left(\mathbb{R}^{n}\right)$. Then $\langle A f, \phi\rangle=\langle A f, \phi\rangle=\left\langle f, A^{*} \phi\right\rangle$ for all $f \in D_{0}$. Since $D_{o}$ is a core of $A$, this implies that
$\phi \in D\left(A^{\prime}\right)$ and $A^{\prime} \phi=A^{*} \phi$. Thus (K) gives Re< (sign fif $\left.A f\right\rangle=$ $\operatorname{Re}\langle($ (sígn $\bar{f}) \mathrm{Af}), \phi\rangle \leqq\langle | f\left|, A^{\prime} \phi\right\rangle=\langle | f\left|, A^{*} \phi\right\rangle=\langle A| f|, \phi\rangle$ for a11
$f \in C_{C}^{\infty}\left(\mathbb{R}^{n}\right), 0 \leq \phi \in C_{C}^{\infty}\left(R^{n}\right)$. This is Kato's inequality in the distributional sense.

Remark. It has been proved by Miyajima and okasawa (1984) that (K $\mathcal{C}_{0}$ ) implies that $m \leqq 2$ and that the principal part $A_{0}=\sum_{a \mid=2} a_{a} D_{a}$ of $A$ is elliptic: i.e., if we write the operator $A_{o}$ in the form $A_{o}=\sum_{i, j=1}^{2} b_{i j} \partial^{2} / \partial x_{i} \partial x_{i}$, then the matrix $\quad\left(b_{i j}(x)\right)$ is positive semidefinite for all $x \in \mathbb{R}^{n}$.

Finally we formulate Theorem 2.4 for the space $E:=C_{o}(X)$ ( $X$ local$1 y$ compact) (which is not o-order complete unless $x$ is o-stonian). Recall, for $f \in C_{o}(x)$, sign $f$ is defined as a Borel function and for any bounded Borel function $g$ on $X$ and any $\phi \in M(X)=C_{o}(X)$ ' we let $\left\langle g, \phi>=\int g(x) d \phi(x) \quad\right.$ (see B-II,sec. 2 ).

Theorem 2.6. Let $X$ be a locally compact space and $A$ be the generator of a strongly continuous positive semigroup on $\mathcal{C}_{\mathrm{o}}(\mathrm{X})$. Then
(K)
Re< (sign
気) $A \neq \phi\rangle \leqq\langle | f\left|, A^{\prime} \phi\right\rangle$
$\left(f \in D(A), \phi \in D\left(A^{\prime}\right)+1\right.$.

The proof of Theorem 2.4 can be taken over literally. Also the analogue of the proof given for $\mathrm{L}^{\text {P. }}$-spaces (preceding Theorem 2.4) is valid if one uses B-II،Lema 2.6.

\section*{3. A CHARACTERIZATION OF GENERATORS OF POSITIVE SEMIGROUPS}

In this section we confine ourselves to real Banach lattices. This coes not mean a restriction since every positive semigroup on a complex Banach lattice leaves the real part of the space invariant.

Remark 3.1. Let (S(t)) tep be a semigroup on a comples Banach lattice $E$ with generator $A$. Then $S(t) E_{\mathbb{R}} \subset E_{R}$ for all $t \geqq 0$ if and only if
(3.1) $f \in D(A)$ implies $\bar{f} \in D(A)$ and $A \bar{f}=(A f)^{-}$.

In that case the generator $A_{R}$ of the restriction semigroup on $E_{R}$ is given by $A_{R} f=A f$ on $D\left(A_{\mathbb{R}}\right)=D(A) \cap E_{\mathbb{R}}$.

We will see below that for generators of a strongly continuous semigroup Kato's inequality alone is not sufficient to ensure the positi* vity of the semigroup. So we introduce another condition.

Definition 3.2 . A subset $M^{\prime \prime}$ of $E^{\prime \prime}$ is called strictly positive if for every $f \in E_{+},\langle f, \phi\rangle=0$ for all $\phi \in M^{\prime}$ implies $f=0$. Accordingly, an element $\phi$ of $E_{+}^{\prime}$ is called strictly positive if the set $\{\phi\}$ is strictly positive.

Example 3.3. Let $E=L^{P}(X, \mu) \quad(1 \leqq p<\infty)$, where ( $\left.X, \mu\right)$ is a ofinite measure space. Then $\phi \in E^{+}=L^{q}(X, \mu) \quad$ (where $1 / p+1 / q=1$ ) is strictly positive if and only if $\phi(x)>0$ $\mu=a . e$. Note that strictly positive elements of $E^{\prime}$ always exist in this case.

Definition 3.4. Let $B$ be an operator on a Banach lattice $F$ and let $u \in F$. Then $u$ is called a positive subeigenvector of $B$ if
a) $0<u \in D(B)$ and
b) $B u \leq \lambda u$ for some $\lambda \in \mathbb{R}$.

Proposition 3.5. Let (T(t)) teo be a positive semigroup on a real Banach Iattice with generator $A$. Then there exists a strictly positive set $M^{\prime}$ of subeigenvectors of $A^{\prime}$ (the adjoint of the generator A ) . Moreover, if there exist strictly positive linear forms on $E$, then there exists a strictly positive subeigenvector of $A^{\prime}$.

Proof. Let $\lambda>0$ be such that $R(\lambda, A)=(\lambda-A)^{-1}$ exists and such that $R(\lambda, A) \geq 0$. Let $N^{\prime} C^{\prime} E_{+}^{\prime}$ be strictly positive. Then $M^{\prime}:=\left\{R(\lambda, A)^{\prime} \psi: \psi \in N^{\prime}\right\}\left[D\left(A^{\prime}\right\}+\right.$. We show that $M^{\prime}$ is strictly positive. Indeed, let $f \in E_{+}$such that $\langle f, \phi\rangle=0$ for all $\phi \in M^{\prime}$. Then $\langle R(\lambda, A) f, \psi\rangle=0$ for all $\psi \in N^{\prime}$. Hence $R(\lambda, A) f=0$ since $N^{\prime}$ is strictly positive. Consequently, $f=0$. The set $M^{\prime}$ consists of
subeigenvectors of $A^{\prime}$. In fact, let $\psi \in N^{\prime}, \phi=R(\lambda, A)^{\prime} \psi$. Then $A^{\prime} \phi=\lambda \phi-\psi \leqq \lambda \phi$.

The fact that $\phi \in D\left(A^{\prime \prime}\right)+$ is a subeigenvector can be expressed by the semigroup (if it is positive).

Proposition 3.6. Assume that $A$ is the generator of a positive semigroup (T(t)) $t \geq 0$ on a real Banach lattice $E$. Let $\phi \in D\left(A^{\prime}\right)_{+}$and $\lambda \in R$. Then
$$
A^{\prime} \phi \leq \lambda \phi \text { if and only if } T(t)^{\prime} \phi \leqslant e^{\lambda t} \quad(t \leq 0)
$$

Proof. If $T(t)$ '中 $\leqslant e^{\lambda t} \phi$ for all $t \geqq 0$, then $A^{\prime} \phi=\sigma\left(E^{\prime}, E\right)-1 m_{t * 0} 1 / t\left(T(t)^{\prime} \phi-\phi\right) \leq \lim _{t+0} 1 / t\left(e^{\lambda t} \phi-\phi\right)=\lambda \phi$. For the converse let $f \in E_{+}$. Then
$$
\begin{aligned}
\left\langle f_{r} T(t)^{\prime} \phi\right\rangle & =\left\langle f_{r} \phi\right\rangle+\int_{0}^{t}\left\langle f_{f} T(s)^{\prime} A{ }^{\prime} \phi\right\rangle \mathrm{ds} \\
& \left\langle\left\langle f_{f} \phi\right\rangle+\lambda \int_{0}^{t}\left\langle f_{,} T(s)^{\prime} \phi\right\rangle \mathrm{ds} .\right.
\end{aligned}
$$

It follows from Gronwall's lemma that $\left\langle f, T(t)^{\prime} \phi\right\rangle \leq e^{\lambda t}\langle f, \phi\rangle$.

Remark 3.7. a) Using Prop. 3.6 it is immediately clear that (T(t)) $\mathrm{t} \geqq 0$ is irreducible if and only if every positive subeigenvector of $A^{\prime}$ is strictly positive (cf. C-III, Def.3.I).
b) In the proof of the "only if" - part of Prop. 3.6 we needed the positivity of the semigroup in order to be able to apply Gronwall's lemma. Fowever, if instead of assuming that the semigroup is positive we suppose that $A$ satisfies Kato's inequality and A'd s $\lambda \phi$ for some strictly positive $\phi \in D\left(A^{\prime}\right)$ then we will show that $T(t){ }^{\prime} \phi$ $e^{\lambda t} \phi$ and that the semigroup $1 s$ positive (see cor.3.9).

The following is our characterization.

Theorem 3. 8 . Let $(T(t))_{t \geqslant 0}$ be a semigroup on a ororder complete real Banach lattice $E$. The semigroup is positive if and only if its generator $A$ satisfies the following condition. There exists a core $D_{0}$ of $A$ and a strictly positive set $M$ of subeigenvectors of $A^{*}$ such that
$$
\begin{equation*}
\langle(s i g n f) A f, \phi\rangle \leqq\langle | f\left|, A^{\prime} \phi\right\rangle \quad \text { for all } f \in D_{o}, \phi \in M^{\prime} \tag{K}
\end{equation*}
$$

Corollary 3.9. Assume in addition that $E^{\prime}$ contains a strictly positive functional. Then the semigroup is positive if and only if there exists a core $D_{o}$ of $A$ and a strictly positive subeigenvector $\phi$ of $A^{\prime}$ such that
$$
\begin{equation*}
\langle\langle\operatorname{sign} f) A f, \phi\rangle \leqslant\langle | f\left|, A^{\prime} \phi\right\rangle \quad \text { for all } f \in D_{o} . \tag{K}
\end{equation*}
$$

From the proof of Theorem 3.8 we isolate the following

Proposition 3.10. Let $B$ be a densely defined operator on $E$ and $D_{o}$ be a core of $B$. Suppose that $\phi \in D\left(B^{\prime}\right)_{+}$is such that $B^{\prime} \phi \leqq 0$. Denote by $P$ the sublinear functional given by $p(f)=\left\langle f^{+}, \phi\right\rangle$. If (K) $\langle(s i g n f) \quad B f, \phi\rangle \leq\left\langle f \mid, B^{\prime} \phi\right\rangle \quad\left(f \in D_{o}\right)$. then $B$ is p-dissipative.

Proof Let $f \in D_{o}$. Set $P_{+}:=P_{f}{ }^{+}, P_{f}:=P_{f}-$ and let $P:=I C^{-P} P_{+} P_{-}, Q=P_{+}+1 / 2 P$ and $\psi=Q^{\prime} \phi$. we show that (3.2) $\psi \in \operatorname{dp}(f)$.

Let $g \in E$. Since $0 \leq Q \leq I d$ we have $\langle g, \psi\rangle=\langle Q g, \phi\rangle \leq\left\langle Q g^{+}, \phi\right\rangle \leq$ $\left\langle g^{+}, \phi\right\rangle=p(g)$. Moreover, $\langle f, \psi\rangle=\langle Q f, \phi\rangle=\left\langle P_{+} f+1 / 2 P f, \phi\right\rangle=\left\langle f^{+}, \phi\right\rangle$ $=p\left(f^{+}\right)$. So (3.2) follows by the definition of $d p(f)$. We show that (3.3) <Bf. $\psi>0 \leq$.

One has trivially
(3.4) $\left\langle\left(P_{+}+P_{-}+P\right) B f, \phi\right\rangle=\left\langle f, B^{\prime} \phi\right\rangle$.

Addition of (3.4) and (K) gives
$\left\langle\left(2 P_{+}+P\right) B f, \phi\right\rangle \leqslant\left\langle 2 f^{+}, B^{\prime} \phi\right\rangle \leqq 0$. Hence $\langle B f, \psi\rangle=\langle Q B f, \phi\rangle \leqslant 0$.
Thus we have proved that $B_{\|} D_{o}$ is p-dissipative. Hence $B$ is p-dis* sipative as well (by A-II, Cor.2.5).

Proof of Theorem 3.8. Proposition 3.5 and Theorem 2.4 yield one implication. In order to show the other assume that the condition in Theorem 3.8 is satisfied. We have to show that $T(t) \geqq 0$ for all $t \geqq 0$.
Let $\phi \in M^{\prime}$. Consider the half-norm $p(f)=\left\langle f^{+}\right.$, $\phi^{\prime}$ and the operator $B=A-\lambda$, where $\lambda \in \mathbb{R}$ is such that $A^{*} \phi \leqslant \lambda \phi$. Then $B$ satism fies $B^{\prime} \phi \in 0$ and $(K)$ as well 0 so it follows from Proposition 3.10 that $B$ is p-dissipative.
Since $B$ generates the semigroup $\left(e^{-\lambda t} T(t)\right)_{t \geq 0}$ we obtain from

A-II, Thm. 2. 6 that $p\left(e^{-\lambda t} T(t) f\right) \leqslant p(f) \quad(f \in E, t \geqslant 0)$. Hence,
(3.5) < (T(t)f) ${ }^{+}, \phi>\leqq e^{\lambda t}\left\langle f^{+}, \phi\right\rangle \quad(f \in E, t \geqslant 0)$.

Now let $t>0$ and $f \leqq 0$; then $f^{+}=0$. It follows from (3.5) that $<(T(t) f)^{+}, \phi>0$. Since $\phi \in M^{*}$ is arbitrary and $M^{\prime}$ is strictly positive, it follows that $(T(t) f)^{+}=0 ; i . e ., T(t) f \leqq 0$. This implies that $T(t) \geq 0$.

Remark 3.11. a) The proof of Theorem 3.8 shows the following. If A is the generator of a positive semigroup and $E^{\prime}$ contains strictly positive linear forms, then there exist a continuous half-norm $p$ on $E$ and $w \in \mathcal{B}$ such that $A-w$ is p-dissipative. We stress that $P$ cannot be replaced by the norm (or by $N^{+}$), since in general none of the semigroups $\left(e^{-w t} T(t)\right) t \geqslant 0 \quad(w \in \mathbb{R})$ is contractive for the norm (cf. Derndinger (1984) and Batty-Davies (1982)).
b) Using Proposition 3.10 one can show with the help of the proof of A-II, Prop.2.9 that a densely defined operator is closable whenever there exists a strictly positive set $M^{\prime}$ of subeigenvectors of $A^{\prime}$ such that (K) holds for all $f \in D(A)$ and $\phi \in M^{\top}$.

Remark 3.12 In Theorem 3.8 and Corollary 3.9 one can replace inequality ( $k$ ) by the inequality
$$
\begin{equation*}
\left\langle\mathrm{P}_{\left(\mathrm{f}^{+}\right)} A f, \phi\right\rangle \leqq\left\langle\mathrm{f}^{+}, A^{\prime} \phi\right\rangle \tag{3.6}
\end{equation*}
$$
(with the notation of Prop. 3.10).
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-280.jpg?height=70&width=1620&top_left_y=1801&top_left_x=227)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-280.jpg?height=55&width=1360&top_left_y=1863&top_left_x=228) On the other hand, if A generates a positive semigroup, one sees by the obvious alterations in the proof of Theorem 2.4 that (3.6) holds for all $f \in D(A)$ and $\phi \in D\left(A^{\prime}\right)_{+}-$
Next we formulate the result for the space $C_{o}(x)$, where $X$ is a locally compact space (concerning the notation cf. Thm. 2.6 and sec. 2 of $B-I I$ ).

Theorem 3.13 Let $A$ be the generator of a semigroup on $C_{0}(X)$ The semigroup is positive if and only if there exists a core $D_{0}$ of $A$ and a strictly positive set $M^{\prime}$ of subeigenvectors of $A^{\prime}$ such that
(K)
$$
\left\langle(s i g n \text { f) } A f, \phi\rangle \leq\langle | f \mid A^{\prime} \phi\right\rangle \text { for allf } f D_{O}, \phi \in M^{\prime} .
$$

This theorem can be proved in the same way as Theorem 3.8.

Remark. If $X$ is separable, then there exist strictly positive measures on $C_{o}(X)$. In that case the analogue of Corollary 3.9 holds as well.

Now we want to discuss the results obtalned so far.

As a first example we consider the first derivative with boundary conditions on $E=L^{P}[0,1, \quad(1 \leqq p<\infty)$, By $A C[0,1]$ we denote the space of all absolutely continuous functions on [0,1]. Let $A_{\text {mas }}$ be given by
$$
\begin{aligned}
D\left(A_{\text {max }}\right) & \left.=\left\{f \in A C[0,1]: f^{*} \in L^{P_{[0, ~}}, 1\right]\right\} \\
A_{\text {max }} f & =f^{\prime} \quad\left(f \in D\left(A_{\text {max }}\right)\right)
\end{aligned}
$$

The following lemma is easy to prove.

Lemma 3.14. Let $f \in A C[0,1]$. Then $|f| \in A C[0,1]$ and $|f|^{\prime \prime}=(\operatorname{signf} f)^{\prime} \quad(a . e).$.

As a consequence of the lemma, $D\left(A_{\text {max }}\right)$ is a sublattice of $E$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-281.jpg?height=58&width=1212&top_left_y=1684&top_left_x=219)

For $\lambda>0$ one has
(3.8) $\quad$ ker $\left(\lambda-A_{\max }\right)=\mathbb{R} \cdot e_{\lambda} \quad$ where $e_{\lambda}(x)=e^{\lambda x}$.

Hence $A_{\text {max }}$ is not a generator. We impose the following boundary conditions.

Let $d \in \mathbb{R}$. Consider the restriction $A_{d}$ of $A_{\text {max }}$ to the domain
$$
D\left(A_{d}\right)=\left\{\ddagger \in D\left(A_{\max }\right): f(1)=d f(0)\right\}
$$

Then $A_{d}$ is the generator of the semigroup $\left(T_{d}(t)\right)$ teo given by
(3.9) $\quad T_{d}(t) f(x)=d^{n}, f(x+t-n) \quad i \pm \quad x+t \in[n, n+1) \quad(n \in \mathbb{N})$.

This is not difficult to prove. Actually (3.9) defines a group if
$d \neq 0$ and if we let $t \in \mathbb{R}, n \in \mathbb{Z}$. For $d=0$ one obtains the nilpotent shift semigroup on $E$. It follows from (3.9) that the semigroup $\left(T_{d}(t)\right)_{t}=0$ is positive if and only if $d \geq 0$.

Let usfix $d<0$. Let $A=A$ and $T(t)=T_{d}(t)$ for $t \geqslant 0$. Then
(T(t)) ta0 is a semigroup which is not positive . Nevertheless its generator $A$ satisfies Kato's inequality. Even the equality is valid; i.e.,
( 3.10 ) $\langle$ (sign f) $A f, \phi\rangle=\langle | f\left|, A^{\prime} \phi\right\rangle$ for all $f \in D(A), 0 \leqq \phi \in D\left(A^{\prime}\right)$.

Proof. It is not difficult to see that
$$
\begin{equation*}
D\left(A^{\prime}\right)=\left\{\phi \in A C[0,1]: \phi^{\prime} \in L^{q}[0,1], \phi(0)=d \phi(1)\right\} \tag{3.11}
\end{equation*}
$$
```
    A'\phi = - 中' for all \phi & D(A') .
```
where $1 / \mathrm{p}+1 / \mathrm{q}=1$. Tet $\phi \in \mathrm{D}\left(\mathrm{A}^{r}\right)+$. since $\mathrm{d}<0$, it follows that $\phi(0)=\phi(1)=0$. Hence for $f \in D(A)$, $\left.\langle\langle\operatorname{sign} \mathrm{f}) \mathrm{Af}, \phi\rangle=\left\langle(\operatorname{sign} \mathrm{f}) \mathrm{f}^{\prime}, \phi\right\rangle=\left.\langle | f\right|^{\prime}, \phi\right\rangle$
$=\int_{0}^{1}|f|^{\prime}(x) \phi(x) d x$
$=|f(1)| \phi(1)-|f(0)| \phi(0)-\int_{0}^{1}|f(x)| \phi^{\prime}(x) d x$
$=|f(1)| \phi(1)-|f(0)| \phi(0)+\langle | f\left|, A^{\prime} \phi\right\rangle$
$=\langle | f\left|, A^{\prime} \phi\right\rangle$

Remark 3.15. The equality (3.10) does not hold for all $\phi \in \mathrm{D}_{\mathrm{A}}(\mathrm{A})$. In fact, this would imply that $|f| \in D(A)$ and (sign flaf $=A|f|$ for all $f \in D(A)$. Thus by Cor. 5.8 below the semigroup would be positive. The reason why in this example the equality holds will be explained from a more general point of view in Section 5 (see Rem-5.12) .

Relation (3.10) shows that $A$ also satisfies Kato's inequality formally in the strong sense. In order to formulate this more precisely, observe that it follows from (3.8) that $D\left(A_{\max }\right)=$
$D(A)+\pi \cdot e_{\lambda}$ (for any fised $\left.0<\lambda \in p(A)\right) \quad$ - Thus the extension $A_{\text {max }}$ of $A$ satisfies the following.
(3.12) $A_{\max }$ is closed.
(3.13) $D\left(A_{\text {max }}\right)$ is a sublattice of $E$.
(3.14) $D(A)$ has codimension one in $D\left(A_{\text {max }}\right)$.
(3.15) (sign f) $A f=A_{\text {max }}|f|$ for all $f \in D(A)$.

It is also remarkable that there exists a dense sublattice
$D_{O}:=\{f \in D(A): f(0)=f(1)=0\} \quad o f \quad E$ which is incluced in $D(A)$. Eut $D_{o}$ is not a core of $A$ (this would imply the positivity of the semigroup by $T h m .1 .8$ if $|d| \leq 1$ ).

Since（T（t））$t \geq 0$ is not positive but Kato＇s inequality holds，it follows from Theorem 3.8 that there does not exist a strictly posi－ tive subeigenvector of $A^{\prime}$ ．In fact，even the following is true．
（3．16） $0 \leqq \phi \in D\left(A^{\prime}\right), A^{\prime} \phi \leqq 山 \phi$ for some $\mu \in \mathbb{R}$ implies $\phi=0$ ．

Proof．Suppose that $0 \leqq \phi \in D\left(A^{\prime}\right)$ such that $-\phi^{\prime}=A^{\prime} \phi \leqq \mu_{\phi}$ ．We can assume that $\mu \geq 0$ ．Let $\psi(x)=\phi(1-x)$ ．Then $\psi^{\prime}(x)=-{ }^{\prime}(1-x) \leqq$上中 $(1-x)=\mu \psi(x)$－Since $\psi(0)=0$ ，we obtain
$\psi(x)=\int_{0}^{x} \psi^{*}(y) d y \leqslant \mu \int_{0}^{x} \psi(y) d y \quad(x \in[0,1 \eta)$.
It follows from Gronwall＇s lemma that $\psi s 0$ ．Hence $\phi=\psi=0$ ．

Remark 3．16．Let $B$ be the generator of a strongly continuous semi－ group on a real Banach lattice with order continuous norm．Assume that the following two conditions hold．
$$
\begin{equation*}
\langle(s i g n f) B f, \phi\rangle \leqslant\langle | f\left|, B^{\prime} \phi\right\rangle \quad\left(f \in D(B), \phi \in D\left(B^{\prime}\right){ }_{+}\right) . \tag{K}
\end{equation*}
$$
$$
\begin{equation*}
\left(\mathrm{D}\left(\mathrm{~B}^{\prime}\right)_{+}\right)^{-\sigma\left(\mathrm{E}^{\prime}, \mathrm{E}\right)}=\mathrm{E}_{+}^{\prime} . \tag{3.17}
\end{equation*}
$$

Because of（3．17）condition（K）implies that $P_{f} B f(s i g n$ f）Bf $\leqq B f$ whenever $f \in D(B)+$ ．
This is Kato＇s inequality in the strong form for positive $f \in D(B)$ and is equivalent to $(B f)^{-} \epsilon\{f\}^{d d}=\overline{E_{f}} \quad$（f $\left.\in D(A)_{+}\right)$（recall that $E$ has order continuous norm）．By Lemma 1.5 this again is equivalent to （P） $0 \leq f \in D(B), \phi \in E_{+}^{\prime},\langle f, \phi\rangle=0$ implies $\langle B f, \phi\rangle \geqq 0$.

It is easy to see that the operator $A$ in the example satisfies conditions（K）and（3．17）．Thus the positive minimum principle（ $P$ ）is not sufficient for the positivity of the semigroup．

In view of the preceding example and remarks one might presume that the existence of a strictly positive set of subeigenvectors of the adjoint of the generator actually implies the positivity of the semigroup．This is not the case．

To give an example consider $E=L^{2}(\mathbb{R})$ and the operator $B$ given by
$$
\begin{aligned}
& B f=f^{(3)} \text { with domain } \\
& D(B)=\left\{f \in L^{2}(\mathbb{R}): f \in C^{2}(\mathbb{R}) ; f^{\prime \prime} \in A C(\mathbb{R}) ; f_{r} f^{\prime}, f^{\prime \prime}, f^{(3)} \in L^{2}(\mathbb{R})\right\}
\end{aligned}
$$

Then $B$ is the generator of a unitary group $(0(t)) t \in \mathbb{R}$ - In particular, B is skew-adjoint, i.e. $\mathrm{B}^{\prime}=-\mathrm{B}$.

Moreover, we claim that
(3.18) $B^{\prime}$ has a strictly positive subeigenvector $\$$.

Proof - Let $\lambda>0$ and $\phi \in C^{3}(R)$ such that $\phi(x)=e^{-|x|}$ for $|x| \geq 1, \phi(x)>0$ for all $x \in R, \phi(0)=1$ and $\phi^{\prime}(0)=\phi^{n}(0)=0$. Then $\phi \in D\left(B^{\prime}\right)$. Moreover, $-\phi^{(3)}(x) \leq \phi(x)$ for $|x|$ a 1 . Hence there exists $\mu \geq 1$ such that $B^{\prime} \phi=-\phi^{(3)} \leq \mu \phi$.

But the semigroup $(U(t))_{t \geqq 0}$ is not positive. In fact, we show that there exists $f \in D(B)$ such that
```
<(sign f) Bf,\phi>><<|f|,B'\phi>.
```

Proof. Let $f \in D(B)$ be such that $f(x)=e^{-x} \sin x$ in a neighborhood of 0 , while $f(x)>0$ for $\Rightarrow>0$ and $f(x)<0$ for $x<0$. Then
$\left\langle\left(\operatorname{sign}\right.\right.$ f) $\mathrm{Bf}, \phi>=-\int_{-\infty}^{0} \mathrm{f}^{(3)}(x) \phi(x) \mathrm{d} x+\int_{0}^{\infty} f(3)(x) \phi(x) \mathrm{d}_{\mathrm{x}}$.
Hence, $\langle | f\left|, B^{\top} \phi\right\rangle=\int_{-\infty}^{0}(-f(x))\left(-\phi^{(3)}(x)\right) d x+\int_{0}^{\infty} f(x)(-\phi(3)(x)) d x$ $=-\int_{-\infty}^{0} f^{(3)}(x) \phi(x) d x+\int_{0}^{\infty} f(3)(x) \phi(x) d x$ $+\left[\left.f^{\prime \prime} \phi\right|_{-\infty} ^{0}-\left.\left[f^{n} \phi\right]\right|_{0} ^{\infty} \quad\left(\right.\right.$ since $\left.\phi^{\prime \prime}(0)=\phi^{\prime}(0)=0\right)$ $=\langle(s i g n f) B f, \phi\rangle+2 f "(0) \phi(0)$ $\ll(s i g n f)$ Bf. $\phi>\quad\left(\operatorname{since} f^{\prime \prime}(0) \phi(0)=f^{\prime \prime}(0)=-2\right)$.

We now show that $B$ satisfies Kato's inequality for positive elements, though; i.e.,
```
Pf
```

In fact, more is true, $B$ is local, i.e.
(3.21) f $\perp \mathrm{g}$ implies $B f \perp g$ for all $f \in \operatorname{D}(B), g \in L^{2}(\mathbb{R})$.

Proof. Let $A$ be the generator of the translation group which, in particular, is a lattice semigroup (see Section 5). We obtain from Proposition 5.4 below that $A$ is local. Hence $B=A^{3}$ is local as well.

This example shows that even if there exists a strictly positive subeigenvector of the adjoint of the generator, Kato's inequality for positive elements alone does not suffice for the positivity of the semigroup. Note also that (because of the order continuous norm) Kato's inequality holds for positive elements if and only if the positive minimum princlple is satisfied (see Remark 3.14).

\section*{4. DOMINATION OF SEMIGROUPS}

Frequently it is useful to be able to compare two semigroups on a Banach lattice with respect to the ordering (for example, in order to decide whether a semigroup is stable (see Chapter $A-I V$ and Example 4.14).

In this section we assume that $E$ is a o-order complete complex Banach lattice. Let (T(t)) $t \geq 0$ be a positive semigroup with generator $A$ and $(S(t))_{t \geqq 0}$ a semigroup with generator $B$. We say, $(T(t)){ }_{t \geq 0}$ dominates $(s(t))_{t \geq 0}$ if
$$
\begin{equation*}
|S(t) f| \leqq T(t)|f| \quad \text { for all } f \in E, t>0 \text {. } \tag{4.1}
\end{equation*}
$$

We first observe that domination of the semigroup is equivalent to domination of the resolvents.

Proposition 4.1. The semigroup (T(t)) t¥o dominates (S(t)) $t \geq 0$ if and only if
(4.2) $|R(\lambda, B) f| \leqq R(\lambda, A)|f| \quad(f \in E)$ for large real $\lambda$.

Proof. (4.2) follows from (4.1) since the resolvent 15 given by the Laplace transform of the semigroup. Conversely, if (4.2) holds, then
$$
\begin{aligned}
|S(t) f| & =\lim _{n \rightarrow \infty}\left|((n / t) R(n / t, B))^{n} f\right| \\
& \leq \lim _{n \rightarrow \infty}((n / t) R(n / t, A))^{n}|f| \\
& =T(t)|f| \quad(t \geqslant 0, f \in E) .
\end{aligned}
$$

One can describe domination by an inequality for the generators in a manner analoguous to the characterization of positive semigroups in Section I; however, no positive subeígenvectors are needed here.

Theorem 4.2. Let (T(t)) ${ }_{t \geq 0}$ be a positive semigroup with generator $A$ and $(s(t))$ tzo a semigroup with generator $B$. The following assertions are equivalent.
(i) $|S(t) f| \leqq T(t) \mid f(f o r a l l f \in E, t \geqq 0$.
(ii) $\operatorname{Re}<(\operatorname{sign} \bar{f}) B f, \phi\rangle \leqslant\langle | f\left|, A^{\top} \phi\right\rangle$ for all $f \in D(B), \phi \in D\left(A^{\prime}\right)+$.

Proof. (i) implies (ii). Let $f \in D(B), \phi \in D\left(A^{\prime}\right)+$. Then
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-286.jpg?height=70&width=1269&top_left_y=936&top_left_x=222)
$$
\begin{aligned}
& \left.=<1 i_{t+0} 1 / t(\operatorname{Re}((\operatorname{sign} \bar{f}) S(t) f)-\mid f!), \phi\right\rangle \\
& \left.\leq \lim _{t+0}<1 / t(|S(t) f|-|E|), \phi\right\rangle \\
& \left.\leq \operatorname{Iim}_{t+0}<1 / t(T(t)|f|-|f|), \phi\right\rangle=\langle | f\left|, A^{\prime} \phi\right\rangle .
\end{aligned}
$$
(ii) implies (i). Let $\lambda>\max \{\omega(A), \omega(B)\}$ and $g \in E$. We show that (4.3) $|R(\lambda, B) g| \leqq R(\lambda, A)|g|$.

Let $\psi \in E_{+}^{\prime}$. Then $\phi ;=R(\lambda, A)^{\prime} \psi \in D\left(A^{\prime}\right)_{+}-$
Setting $f:=R(\lambda, B) g \in D(B)$ we obtain by (ii)
$\langle | R(\lambda, B) g|, \psi\rangle=\langle | f\left|,\left(\lambda-A^{\prime}\right) \phi\right\rangle \leqq\langle\lambda| f|, \phi\rangle-\operatorname{Re}\langle(\operatorname{sign} \bar{f}) \mathrm{Bf}, \phi\rangle=$ $\operatorname{Re}\langle(\operatorname{sign} \bar{f})(\lambda f-B f), \phi\rangle=\operatorname{Re}\langle(\operatorname{sign} \bar{f}) g, \phi\rangle \leqq\langle | g|, \phi\rangle=\langle R(\lambda, A)| g|, \psi\rangle$. Since $\psi \in E_{+}^{\prime}$ is arbitrary (4.3) follows.

In order to deduce that (ii) implies (i) in Theorem 4.2, it is not necessary to assume that $B$ is a generator. Merely a range condition is sufficient. The precise formulation is the following.

Theorem 4.3. Let $(T(t)) t \geqslant 0$ be a positive semigroup with generator $A$. Let $B$ be a densely defined operator such that
```
Re<(sign \overline{f}})\textrm{Bf},\phi>\<<|||,A'\phi
for all f G D(B), , & D(A')}+
```

Then $B$ is closable. Moreover, if $(\lambda-B) D(B)$ is dense in $E$ for some $\lambda>\max \{0, s(A)\}$, then $\vec{B}$ (the closure of $B$ ) generates a semigroup which is cominated by $\{T(t))_{t \geq 0}$.

Proof. 1. We show that $B$ is closable.
Let $u_{n} \in D(B)$ satisfy $u_{n} \rightarrow 0$ and $B u_{n}+v(n+\infty)$. We have to
show that $v=0$. Considering $A-\mu$ and $B-\mu$ for some $\mu>s(A)$ instead of $A$ and $B$ we may assume that $s(A)<0$. Then there exists a strictly positive set $M^{\prime} \subset E^{\prime}$ such that
(4.5) $\phi \in D\left(A^{\prime}\right)$ and $A^{\prime} \phi \leq 0$ for all $\phi \in M^{*}$
(see the proof of Proposition 3.5).
Let $\phi \in M^{+}$and $p$ be the seminorm given by $p(f)=\langle!f|$, $\phi$. We show that $B$ is p-dissipative (see end of $A-I I$ sec. 2).
Let $f \in D(B), \psi=(s i g n \mathcal{f}){ }^{\prime} \phi$. Then it is easy to see that
$\psi \in \operatorname{dp}(f)$. Moreover, by (4.4) and (4.5) one obtains that Re<Bf. $\psi>=$ Re< (sign $\bar{f}) B f, \phi\rangle \leqq\langle | f\left|, A^{\prime} \phi\right\rangle \leqq 0$. Thus $B$ is p-dissipative. By the proof of $A$-II, Prop. 2.9 one sees that $p(v)=0 ; i . e .,\langle i v i, \phi\rangle=0$. since $\phi \in M^{\prime}$ was arbitrary we conclude that $v=0$.
2. Let $\lambda>\lambda_{0}:=\max \{s(A), 0\}$. We show that for $f \in D(B)$,
(4.6)
$$
g=(\lambda-B) f \text { implies }|f: \leqslant R(\lambda, A)| g \mid .
$$

Let $\psi \in E_{+}^{\prime}$. We have to show that $\langle\dot{i} \mid, \psi\rangle \leq\left\langle R(\lambda, A) \mid g_{i}^{\prime}, \psi\right\rangle$.
Let $\phi=R(\lambda, A)^{\prime} \psi \varepsilon D\left(A^{\prime}\right)_{+}$. Then by (4.4)
$\langle | f|, \psi\rangle=\left\langle i f_{i}^{\prime},\left(\lambda-A^{\prime}\right) \phi\right\rangle=\operatorname{Re}\langle(\operatorname{sign} \bar{f})(\lambda f), \phi\rangle-\langle | f \mid, A_{\phi}^{\prime} \phi$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-287.jpg?height=49&width=975&top_left_y=1392&top_left_x=392)
$\leqq\langle i g \mid, \phi\rangle=\left\langle R(\lambda, A) \mid g_{i}^{\prime} \psi\right\rangle$.
It follows from (4.6) that for $\lambda>\lambda_{o}$ and $f \in D(\bar{B})$
$$
\begin{equation*}
g=\left(\lambda-\frac{5}{B}\right) \Sigma \quad \text { implies } \quad\left|f_{i}^{\prime} \leq R(\lambda, A)\right| g_{i}^{\prime} \tag{4.7}
\end{equation*}
$$

In particular, $(\lambda-\bar{B})$ is injective for $\lambda>\lambda_{0}$. Moreover,
$$
\begin{align*}
& |\mathrm{R}(\lambda, \overline{\mathrm{~B}}) \mathrm{g}| \leqq \mathrm{R}(\lambda, \mathrm{~A}) \mathrm{g} \mid \text { for all } \mathrm{g} \in \mathrm{E}  \tag{4.8}\\
& \text { whenever } \lambda_{0}<\lambda \in \rho(\overline{\mathrm{B}}) \text {. }
\end{align*}
$$

Assume now that $\mu>\lambda_{0}$ such that $(\mu-B) D(B)$ is dense in $E$. Then ( $\mu-\bar{B}$ ) $D(\bar{B})=E$. (Indeed, let $h \in E$. There exists $f_{n} \in D(B)$ such that $g_{n}:=(\mu-B) f_{n} \rightarrow h(n \rightarrow \infty)$. By (4.6) it follows that $\left|f_{n}-f_{m}^{\prime} \leqq R\left(\lambda_{r} A\right)\right| g_{n}-g_{m}^{i} \dot{\prime}$. Thus $\left(f_{n}\right)$ is a cauchy sequence. Let $f=\lim _{n \rightarrow \infty} f_{n}$. Then $f \in D(\bar{B})$ and $(\mu-\bar{B}) f=h, \quad$, Thus $\mu \in \rho(\bar{B})$. It follows from the hypothesis that there esists $\lambda_{1} \in \rho(\bar{B})$ such that $\lambda_{0}<\lambda_{1}$. Since $R(\lambda, A) \leq R\left(\lambda_{1}, A\right)$ (by $\left.B-I I, L e m m a 1.9\right)$, it follows from (4.8) that $\|R(\lambda, \vec{B})\| \leq\left\|_{1} R(\lambda, A)\right\| \equiv\left\|R\left(\lambda_{1}, A\right)\right\|:=c$; hence dist $(\lambda, \sigma(\bar{B}))=r(R(\lambda, \vec{B}))^{-1} \geqq\|R(\lambda, \bar{B})\|^{-1} \geqq 1 / \mathrm{c}$ for all $\lambda \in \rho(\bar{B}) \cap\left[\lambda_{I}, \infty\right]$. This implies that $\left[\lambda_{1}, \infty\right)=\rho(\vec{B})$. Moreover, it follows from (4.8) that
$$
\begin{equation*}
\left|R(\lambda, \bar{B})^{n} f_{i}^{\prime} \leqq R(\lambda, A)^{n}\right| f\left(\quad\left(f \in E, n \in \mathbb{N}, \lambda_{I}<\lambda\right)-\right. \tag{4.9}
\end{equation*}
$$

Let $w>w(A),{ }^{\lambda} 1$. Then it follows from (4.9) that
$\left\|(\lambda-w)^{n} R(\lambda, \bar{B})^{n}\right\| \leqq\left\|(\lambda-w)^{n} R(\lambda, A)^{n}\right\|$ for all $\lambda>w, n \in \mathbb{N}$. So by the Hille-Yosida theorem, $\bar{B} \quad 1 s$ the generator of a semigroup
$(S(t))_{t \geqslant 0}$. Finally, the domination of $(S(t))_{t \geqslant 0}$ by $(T(t)){ }_{t \geqslant 0}$ follows from (4.8) and Prop.4.1.

Example 4.4. a) Let $E$ be a o-order complete complex Banach lattice and $(T(t))_{t \geqslant 0}$ be a positive semigroup with generator $A$. Let
$M \in Z(E) \quad$ (the center of $E$ (see C-I,Sec.9). For example, if $E=$
$L^{P}(X, \mu)$ (where ( $X, \mu$ ) is a $\sigma$-finite measure space and $I \leqslant p \leqslant \infty$ ) then $M$ is the multiplication operator defined by a function in $L^{\infty}(X, H)$.
Let $B=A+M$. Then $B$ generates a semígroup ( $S(t))_{t \geq 0}$.
Assume that ReM $\leq 0$. Let $f \in D(B)$ and $\phi \in D\left(A^{\prime}\right)_{+}$. Then
$\operatorname{Re}\langle(\operatorname{sign} \bar{f}) B f, \phi\rangle=\operatorname{Re}\langle(\operatorname{sign} \bar{f}) A f, \phi\rangle+\operatorname{Re}\langle(\operatorname{sign} \bar{f}) M f, \phi\rangle$
$=\operatorname{Rec}(s i g n \mathrm{f}) \mathrm{Af}, \phi\rangle+\operatorname{Re}\langle\mathrm{M}| \mathrm{f}|, \phi\rangle$
$\leq\left\langle\mid f, A^{\prime} \phi\right\rangle$.
Thus, by Theorem $4.2,(S(t))_{t \geqslant 0}$ is dominated by (T(t)) t¥0.
b) Let $E$ be an order complete complex Banach lattice and $B$ be a regular bounded operator on $E$. Then $B$ can be written as $B=B_{0}+$ $M$ where $M \in Z(E) \quad$ and $B_{O} \in L^{r}(E)$ such that inf $\left\{\left|B_{0}\right|, I d\right\}=0$. Let $A=\left|B_{o}\right|+\operatorname{Re} M$. Then the semigroup $\left(e^{t B}\right){ }_{t \geqq 0}$ is dominated by $\left(e^{t A}\right) t \geqq 0$.
In fact, let $f \in E$. Then $\operatorname{Re}\left[(\operatorname{sign} \bar{f}) B f i=\operatorname{Re}(\operatorname{sign} \bar{f}) B_{o f} f+\operatorname{ReM} \cdot|f|\right.$ $\leq\left|B_{0}\right||f|+\operatorname{Rem}|f|=A|f|$. This implies condition (ii) in Thm. 4.2 .

Domination and positivity are characterized simultaneously as follows.

Proposition 4.5. Let $E$ be a ororder complete real Banach lattice.
Let $(T(t)) t \geqslant 0$ be a positive semigroup with generator $A$ and let (S (t)) $t \geqslant 0$ be a semigroup with generator $B$. The following are equivalent.
(i) $0 \leqq s(t) \leqq T(t) \quad$ for all $t \geqq 0$.
(ii) $\left\langle P_{\left(f^{+}\right)} \mathrm{Bf}_{\mathrm{r}} \phi\right\rangle \leq\left\langle\mathrm{F}^{+}, \mathrm{A}^{\prime} \phi\right\rangle \quad$ for $\mathrm{all} \dot{\mathrm{I}} \in \mathrm{D}(\mathrm{B}), \phi \in \mathrm{D}\left(\mathrm{A}^{\prime}\right)+\cdot$
(iii) $\left\langle P_{\left(f^{+}\right)}\right.$Bf, $\left.\phi\right\rangle \leqq\left\langle f^{+}, A^{\prime} \phi\right\rangle$ for all $f \in D_{O}, \phi \in D\left(A^{\prime}\right)+$, where $D_{o}$ is a core of $B$.

Remark 4.6. Condition (ii) implies (4.4) (cf. Remark 3.12).

Proof. One proves as in Theorem 4.2 that (i) implies (ii).
It is trivial that (ii) 1mplies (iii). Assume that (iii) holds. Let $\lambda>\lambda_{0}=\max \{s(A), s(B), 0\}$. In a similar way as (4.6) one shows that for all $f \in D_{o}$
(4.10) $\lambda f-B f=g$ implies $f^{+} \leqq R(\lambda, A) g^{+}$.

Since $D_{o}$ is a core of $B$ it follows that (4.10) also holds for all $f \in D(B)$. This implies that $(R(\lambda, B) g)^{+} \leqq R(\lambda, A) g^{+}$for all $g \in E$, $\lambda>\lambda_{o}$ Consequently, $0 \leq R(\lambda, B) \leqq R(\lambda, A)$ for all $\lambda>\lambda_{o}$. Hence (i) holds.

In the following example we apply Theorem 4.3 to Schrodinger operators. Here the range condition is proved by an elegant argument due to Kato (1986) with the help of Kato's classical inequality.

Example 4.7 (schrodinger operators on $L^{P}$ ).
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-289.jpg?height=81&width=1615&top_left_y=1290&top_left_x=209) Define $B$ on $E$ by $B f=\Delta f-V f$ with domain $D(B)=C_{C}^{\infty}\left(\mathbb{R}^{n}\right)$. Then $B$ ís closable and $\bar{B}$ is the generator of a semigroup ( $S(t)$ ) $t \geqslant 0$ which is dominated by the diffusion semigroup (Example $1.5 d$ and $A-I$, 2.8). If $V \geq 0$, then $(S(t)) t \geq 0$ is positive.

Proof. Denote by $A$ the generator of the diffusion semigroup. Then $C_{c}^{\infty}:=C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ is a core of $A$ and $A f=\Delta \underline{f o r} f \in C_{C}^{\infty}$ (see Example I. $5 d^{\prime}$. Let $0 \leqslant \phi \in D\left(A^{\prime}\right)$. Then
$\operatorname{Re}\langle(\operatorname{signf}) B f, \phi\rangle=\operatorname{Re}\langle(\operatorname{signf}) A f, \phi\rangle-\langle(\operatorname{ReV})| f|, \phi\rangle \leqslant \operatorname{Re}\langle(\operatorname{sign} \bar{f}) A f, \phi\rangle \leqq$ $\langle | f\left|, A^{\prime} \phi\right\rangle$ for all $f \in C_{c}^{\infty}$ by Theorem 2.4. Thus (4.4) holds.
We show that ( $\lambda-B$ ) has dense range for $\lambda>0$. If not, then there exists $0 \neq \phi \in E^{\prime}=L^{q}\left(\mathbb{R}^{n}\right)$ such that $\langle(\lambda-A+V) f, \phi\rangle=0$ for all $f \in C_{c}^{\infty}$; i.e., $(\lambda-A+V) \phi=0$ in the sense of distributions. By Kato's classical inequality (see Example 2.5) this implies that $(\lambda-\Delta+\operatorname{Rev})|\phi| \leqq \lambda|\phi|-\operatorname{Re}[(\operatorname{sign} \phi)(\lambda \phi-\Delta \phi+V \phi)]=0$ (here we use that $\left.\Delta \phi=\lambda \phi+V \phi \in L_{l o c}^{l}\right)$. Hence $(\lambda-\Delta)|\phi| \leqq-($ ReV $)|\phi| \leq 0$. Since $(\lambda-A)^{-1}$ is a positive linear mapping from $S\left(\mathbb{R}^{n}\right)^{\prime}$ onto $S\left(\mathbb{R}^{n}\right)^{\prime}$. this implies that $\phi=0$. It follows from Thm, 4.3 that $\bar{B}$ is the generator of a semigroup $(S(t))$ to 0 which $1 s$ dominated by the semigroup generated by A.
If $V=R e V \geqq 0$, we may consider the real space $L^{P}\left(\mathbb{R}^{n}\right)$. Then for every $f \in C_{C}^{\infty}, 0 \leqq \phi \in D\left(A^{\prime}\right)$ we have
$\left\langle P_{\left(f^{+}\right)} B f, \phi\right\rangle=\left\langle P_{\left(f^{+}\right)} A f, \phi\right\rangle-\left\langle V f^{+}, \phi\right\rangle$
$$
\begin{aligned}
& \leq\left\langle P f^{+}, A f, \phi>\right. \\
& \leq\left\langle f^{+A}, \phi\right\rangle
\end{aligned}
$$
$$
\leqq\left\langle f^{f^{+}}, A^{\prime} \phi\right\rangle
$$
by (3.6). It follows from Prop. 4.5 that $(S(t))$ t 20 is positive.

Finally, if it is known that the semigroup ( $S$ (t)) $t \geq 0$ is positive, domination can be characterized as follows.

Proposition 4.8 . Let $E$ be a real Banach lattice, (T(t)) tミ0 a positive semigroup with generator $A$ and (S(t)) tき0 a positive semigroup with generator $B$. Consider the following conditions.
(i) $S(t) \leqq T(t) \quad(t \geqq 0)$.
(ii) $\langle B f, \phi\rangle \leqq\left\langle f, A^{\prime} \phi\right\rangle$ for all $f \in D(B)_{+} \in \phi \in D\left(A^{\prime}\right)_{+}$.
(iii) $B f$ ́Af for $0 \leq f \in D(A) \cap D(B)$.

Then (i) and (ii) are equivalent and imply (iii).
Moreover, if $D(A) G D(B) \quad o r \quad D(B) \quad C D(A)$, then (iii) implies (i).

Proof. Assume that (i) holds. Then for $f \in D(B)+, \phi \in D(A)_{+}^{\prime}$, $\left.\left.\langle B f, \phi\rangle=\lim _{t \rightarrow 0} l / t<S(t) f-f, \phi\right\rangle \leqq \lim _{t \rightarrow 0} l / t<T(t) f=f, \phi\right\rangle$ $=\left\langle\mathrm{f}, \mathrm{A} \mathrm{A}^{\prime} \phi\right\rangle$.
So (ii) holds. (iii) is proved similarly.
Now assume (ii) , Let $\lambda>\max \{s(A), s(B)\}$, Let $g \in E_{+} \psi^{*} \in E_{+}^{\prime}$. Then $<\mathrm{R}(\lambda, B) \mathrm{g}-\mathrm{R}(\lambda, A) \mathrm{g}, \psi>$
$=\langle R(\lambda, A) g r \lambda R(\lambda, B) \quad \psi-\psi\rangle=\langle\lambda R(\lambda, A) g=g r R(\lambda, B) \quad \psi\rangle$
$=\left\langle f, B^{\prime \prime} \phi\right\rangle-\langle A f, \phi\rangle \leqslant 0$,
where $f=R(\lambda, A) g \in D(A)+$ and $\phi=R(\lambda, B)^{\prime} \psi \in D\left(B^{\prime}\right)_{+}$. Hence $R(\lambda, B)$ $\leqq R(\lambda, A)$ and (i) follows.

Finally, we prove that (iii) implies (i) if $D(B) \in D(A)$, say.
Let $\lambda>\max \{s(A), s(B)\}$. Then $(A-B) R(\lambda, B)$ is a positive operator. Hence $R(\lambda, A)-R(\lambda, B)=R(\lambda, A)(A-B) R(\lambda, B) \geqq 0$. This implies (i).

The preceding results can be applied to the perturbation by multiplication operators. Let $(X, \mu)$ be a $\sigma$ finite measure space and $E=$ $L^{P}(X, \mu) \quad(1 \leqslant p<\infty)$. Consider a positive semigroup (T(t)) $t \geq 0$ with generator $A$, Let $m: X \rightarrow R$ be a measurable function such that $m(x) \leqq 0$ for all $x \in X$. Let $D(m)=\{f \in E: f \cdot m \in E\}$. Define the operator $B$ with domain $D(B)=D(A) \quad \cap D(m) \quad b y \quad B f=A f+m \cdot f$ (f $\in D(B)$ ).

Theorem 4.9. If there exists a quasi-interior subeigenvector u of $A$ such that $u \in D(m)$, then $B$ is closable and the closure $\bar{B}$ of $B$ is the generator of a positive semigroup ( $(\mathrm{t}))_{\mathrm{t} \geqslant 0}$ which is dominated by $(T(t)) t \geq 0$.

For the proof of the theorem we need the following leman.

Lemma 4.10. Let $A$ and $B$ be generators of positive semigroups ( $T(t)$ ) $t \geq 0$ and $S(t) t \geq 0$, respectively. If $(T(t)) t \geq 0$ dominates ( $s(\mathrm{t}))_{\mathrm{tzo}}$, then $s(\mathrm{~B}) \mathrm{s} s(\mathrm{~A})$.

Proof of Lemma 4. 10. Let $\lambda>s(A)$. Then for all $\mu>\max \{\lambda, s(B)\}$ one has $0 \leqq R(\mu, A) \subseteq R(\lambda, A)$ (by B-II,Lemma 1.9), and so $\|R(\mu, B)\| \leqq$ $\|R(\mu, A)\| \leq\|R(\lambda, A)\|_{1}$. Thus dist $(\mu, \sigma(B)) \geq\left\|_{\|} R(\mu, B)\right\|^{-1} \geqq\|R(\lambda, A)\|^{-1}$. This implies that $[\lambda, \infty) \subset \rho(B)$. Hence $s(B) \leqq \lambda$.

Proof of Theorem 4.9. There exists $\mu>0$ such that $A u \leqq \mu u$.
Let $\lambda>\max \{s(A), \mu\}$. Then $\lambda R(\lambda, A) u=A R(\lambda, A) u+u \leqq \mu R(\lambda, A) u+u$. Hence $R(\lambda, A) u \leqq c \cdot u$ where $c>0$. It follows that $R(\lambda, A) E_{u}=$ $E_{u} \cap D(A) \subset D(B)$. Hence $D(B)$ is dense.
Let $f \in D(B), \phi \in D\left(A^{\prime}\right){ }_{+}$and set $P_{+}:=P_{f^{+}}, P_{-}:=P_{f}{ }^{-}$. Then
$$
\begin{equation*}
\left\langle P_{+} B f, \phi\right\rangle \leq\left\langle f^{+}, A^{\prime} \phi\right\rangle . \tag{4.11}
\end{equation*}
$$

In fact, $\left\langle P_{+} B f, \phi\right\rangle=\left\langle P_{+} A f, \phi\right\rangle+\left\langle P_{+} M \cdot f, \phi\right\rangle$
$$
\begin{aligned}
& =\left\langle P_{+} A f, \phi\right\rangle+\left\langle m \cdot f^{+}, \phi\right\rangle \\
& \leqq\left\langle P_{+} A f, \phi\right\rangle \\
& \leqq\left\langle f^{+}, A^{\prime} \phi\right\rangle \quad(b y(3.6)) .
\end{aligned}
$$

But (4.ll) implies (4.4). So it follows from Theorem 4.3 that $B$ is closable. Moreover, if we can show that $(\lambda-\bar{B}) D(\bar{B})$ is dense in $E$, it follows that $\bar{B}$ is the generator of a semigroup ( $S(t)$ ) $t \geqq 0^{\circ}$ In that case (4.Il) implies that $(s(t))_{t \geqslant 0}$ is dominated by ( $\left.T(t)\right)_{t \geq 0}$ (by Proposition 4.5).
Now we show that $(\lambda-\bar{B}) D(\bar{B})$ is dense in $E$.
Let $m_{n}=\sup \left\{m,-n 1_{Y}\right\} \quad(n \in \mathbb{N}) \quad \operatorname{and} B_{n}=A+m_{n}$. Then $B_{n}$ is the generator of a positive semigroup and it follows from Proposition 4.8 that $0 \leq R\left(\lambda, B_{n+1}\right) \leq R\left(\lambda, B_{n}\right) \leq R(\lambda, A)$ for all $n \in \mathbb{N}, \lambda>s(A)$. (Note that $s\left(B_{n}\right) \leqq s(A)$ by Lemma 4.10$)$. Let $0 \leqq f \in E_{u}$ and $g_{n}=$ $R\left(\lambda, B_{n}\right) f$. Then $g=\inf { }_{n \in \mathbb{N}} g_{n}=\lim { }_{n \rightarrow \infty} g_{n}$ exists. Moreover $g_{n} \in D(B)$ and $\quad \lim _{n \rightarrow \infty}(\lambda-B) g_{n}=f+\lim _{n+\infty}\left(B_{n}-B\right) g_{n}=f$, since $\left|\left(B_{n}-B\right) g_{n}\right| \leq\left(m_{n}-m\right)\left|g_{n}\right|=\left(m_{n}-m\right)\left|R\left(\lambda, B_{n}\right) f\right| \leq\left(m_{n}-m\right) R(\lambda, A)|f| \leqslant$ $c^{\prime}\left(m_{n}-m\right) u$ for some positive constant $c^{\prime}$.

But $I_{i m \rightarrow \infty}\left(m_{n}-m\right) u=0$ since $u \in D(m)$. Thus $g \in D(\bar{B})$ and $(\lambda-\vec{B}) g=f$. We have shown that $E_{u} \subset(\lambda-\vec{B}) D(\bar{B})$. Hence $(\lambda-\vec{B}) D(\bar{B})$ is dense in $E$.

Example 4.II. If in the situation explained before Theorem 4.9 $D(A) \subset L^{\infty}(X, \mu)$ and $m \in L^{P}(X, \mu)$, then the hypotheses of Theorem 4.9 are satisfied.

Now we want to indlcate how the results of this section look like for $C_{o}(X)$. In fact, most of them carry over with a different interpretation of "sign" but the same proofs. We want to state the analogs of Theorem 4.2 and Theorem 4.3 explicitly. Here we use the notation of $\mathrm{B}=\mathrm{II}, \mathrm{Sec} .2$.

Theorem 4.12. Let $E=C_{0}(X)$ where $Y$ is locally compact.
Let ( ${ }^{(T)}(t) t_{30}$ be a strongly continuous positive semigroup with generator $A$ and $(S(t))_{t \geqq 0}$ a semigroup with generator $B$. The following assertions are equivalent.
```
|S(t)f| {T(t)|f: for allfeEE,t>0.
Re<<(sign \overline{E})Bf,\phi>\leqq<|||,A'\phi>
for allf\inD(B), &\inD(A')}+\mathrm{ .
```

Recall that by defindtion
$\operatorname{Re}\langle(\operatorname{sign} \overline{\mathrm{f}}) \mathrm{Bf}, \phi\rangle=\int\left[(\operatorname{sign} \overline{\mathrm{f}(\mathrm{x})}) \cdot(\mathrm{Bf})(\mathrm{x}) \mathrm{l} \mathrm{d}_{\phi}(\mathrm{x})\right.$ where sign $\mathrm{f}(\mathrm{x})=$ $f(x) /|f(x)|$ if $f(x) \neq 0$ and $\operatorname{sign} 0=0$.

Theorem 4.13. Let $E=C_{o}(X)$ ( $X$ locally compact) and let (T(t)) $t \geqq 0$ be a positive semigroup on $E$ with generator $A$. Let $B$ be a densely defined operator such that
$$
\begin{align*}
& \text { Re }\langle(\operatorname{sign} \bar{f}) \mathrm{Bf}, \phi\rangle \leqq\langle | \mathrm{f}\left|, \mathrm{~A}^{\prime} \phi\right\rangle  \tag{4.12}\\
& \text { for all f } \in \mathrm{D}(\mathrm{~B}), \phi \in \mathrm{D}\left(\mathrm{~A}^{\prime}\right)_{+} .
\end{align*}
$$

Then $B$ is closable. Moreover, if ( $\lambda$ - B)D(B) is dense in $E$ for some $\lambda>\max \{0, s(A)\}$, then $\vec{A}$ (the closure of $B$ ) generates a semígroup which is doninated by (T(t)) t?0.

Example 4.14. Let $E:=C([-1,0], C), \alpha \in \mathbb{R}, \beta \in \mathbb{C}, \mu \in M[-1,0]_{+}$ and $v \in M[-1,0]$ such that $\mu(\{0\})=v(\{0\})=0$. Then the operator $A$ given by $A f=f^{\prime}$ on $D(A)=\left\{f \in C^{l}([-1,0], C): f^{\prime}(0)=a f(0)+\right.$ <f, $上$ >) generates a strongly continuous positive semigroup (T(t)) $t \geqq 0$ (see B-II, Example 1.22).

Consider the operator $B$ given by $B f=f^{\prime}$ with domain $D(B)=\{f \in$ $\left.C^{1}([-1,0], C): f^{\prime}(0)=B f(0)+\langle f, v\rangle\right\}$. We claim that

B is the generator of a strongly continuous semigroup
(4.13) (S(t)) $t \geq 0$. Moreover, ( $s(t))_{t \geq 0}$ is dominated by ( $\left.T(t)\right)_{t \geq 0}$ if and only if Res $\leqq a$ and $!v \mid \leq \mu$.

Remark. It is of interest to find a condution on $B$ which implies that the semigroup ( $S(t)$ ) $t \geqq 0$ is stable (see $A-I V, S e c . I$ ).
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-293.jpg?height=61&width=1623&top_left_y=792&top_left_x=205) (T(t)) tzo is stable if and only if $\|\mu\|+\alpha<0$. Since a semigroup which is dominated by a stable semigroup is itself stable we obtain from (4.13) that $(S(t))_{t \geq 0}$ is stable if $\|v\|+R e \beta<0$.

Proof of (4.13). We first assume that $a ;=\operatorname{Re} \beta$ and $\mu=1 v \mid$. We show that (4.12) is satisfied. Consider the operator $A_{\max }$ on $C[-1,0]$ given by $A_{\max } f=f^{\prime}$ with domain $D\left(A_{\text {max }}\right)=C^{1}[-1,0]$. We know by B-II, Example 2.12 that $\operatorname{Re}^{<}(\operatorname{sign} \bar{f}) A f, \phi>\leqq \operatorname{Re}\langle(s i g n \bar{f})(A f), \phi>=$ $\langle | f \mid,\left(A_{\max }\right)^{\prime} \phi^{>}$for all $\left.f \in D\left(A_{\max }\right), 0 \leqq \phi \in D\left(A_{\max }\right)^{\prime}\right)$. In particular
(4.14) $\quad \operatorname{Re}\langle(s 1 g n \bar{f}) B f, \phi\rangle \leqslant\langle | f\left|, A^{\prime} \phi\right\rangle$
holds for allf $\left.f \in D(B), 0 \leqq \Phi \in D\left(A_{\text {max }}\right)^{\prime}\right)$. It is not difficult to see that $D\left(A^{1}\right)=D\left(\left(A_{\max }\right)^{\prime}\right)+\varepsilon_{0}$, and since $\left.D\left(A_{\text {max }}\right)^{\prime}\right)=B V[-1,0$. (see B-II, Example 2.12 ) this is an order direct sum.
Thus, in view of (4.14), it remains to show that
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-293.jpg?height=64&width=929&top_left_y=1770&top_left_x=209)
for all $f \in D(B)$. By the definition of $A, \delta_{o} \in D\left(A^{\prime}\right)$ and $A^{\prime} \delta_{0}=$ $\alpha_{0}+\mu$. Hence for $f \in D(B)$,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-293.jpg?height=70&width=1623&top_left_y=1961&top_left_x=205) $\langle f, v\rangle)\rangle \leq \operatorname{ReB}|f(0)|+|\langle f, v\rangle| \leqq a|f(0)|+\langle | f\left|, \mu^{\prime}\right\rangle=\langle | f\left|, A^{\prime} \delta_{0}\right\rangle$.
Thus (4.15) and so also (4.12) are proved.
As in the proof in Example 2.14 one shows that $\lambda \rightarrow B$ is surjective for large real $\lambda$. Hence by Theorem 4.14 , $B$ is the generator of a strongly continuous semigroup $(S(t))_{t \geq 0}$ which is dominated by ( $T(t))_{t \geq 0}$. This proves the first assertion of (4.13) and the sufficiency of the second.
Now we assume that the semlgroup ( $5(t))_{t \geqslant 0}$ is dominated by $(T(t))_{t \geqq 0}$. We have to show that $R e e \leqq a$ and $|v| \leqq \mu$. Since $\delta_{o} \in D\left(A^{1}\right) \cap D\left(B^{1}\right)$ we have for all f. $\in C[-I, 0]_{+}$satisfying
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-293.jpg?height=72&width=1522&top_left_y=2597&top_left_x=207) $=\lim _{t \rightarrow 0+} 1 / t|(s(t) f)(0)|$
```
\leqq lim
= lim
= <|f|,A'\mp@subsup{\delta}{0}{\prime}
Since }\mu({0})=v[0})=0, this implies that |v|\leq\mu
Moreover, for arbitrary f & C[-1,0]+ we have
<f, Reß \delta
    s lim}\mp@subsup{t}{->0+}{}1/t\operatorname{Re}<(T(t)f-f),\mp@subsup{\delta}{0}{\prime
Consequently, (Rep)\delta
\mu({0)})=v{0})=0
```

We conclude this section discussing the following question. Let ( $S(t))_{t \geqslant 0}$ be a semigroup which is dominated by some positive semigroup. Does there exist a smallest semigroup ( $T(t)$ ) $t_{2} 0$ which dominates $(S(t)) t \geq 0$ ? More precisely, we look for a positive semigroup $(T(t))_{t \geq 0}$ dominating $(s(t))_{t \geq 0}$ such that $(T(t))_{t_{3} 0}$ is dominated by any other positive semigroup which dominates $(S(t))_{t \geqslant 0}$. If such a minimal dominating semigroup exists, it is unique and we call it the modulus semigroup of $(S(t))_{t \geq 0}$ *

Example 4.15 (the modulus semigroup associated with $A-V$ ), Let $E$ be the complex space $L^{P}\left(\mathbb{R}^{n}\right) \quad(1 \leqq p<\infty)$ and $V \in \operatorname{L}_{10 c}^{p}\left(\mathbb{R}^{n}\right)$ satisfying ReV $\geq 0$. Denote by $B$ the closure of $A-V$ on $C_{c}^{\infty}$ (cf. Example 4.7). The modulus semigroup of the semigroup ( $\mathrm{S}(\mathrm{t})$ ) t t 0 generated by $B$ exists and its generator $A$ is given by $A f=A f-(R e V) f$ for all $f \in \mathcal{C}_{C}^{\infty}$ (and $\mathcal{C}_{C}^{\infty}$ is a core of $A$, see Example 4.7).

Proof. The operator A defined above generates a positive semigroup (see Example 4.7). For $f \in C_{C}^{\infty}, \phi \in D\left(A^{\prime}\right)_{+}$one has $\operatorname{Re}<(s i g n \mathrm{f}) \mathrm{Bf}, \phi\rangle=\operatorname{Re}<(\operatorname{sign} \mathrm{f})(\Delta f-V f), \phi>=$
$\operatorname{Re}\langle(\operatorname{sign} \overline{\mathrm{f}}) \Delta \mathrm{f}, \phi\rangle \rightarrow\langle(\operatorname{ReV})| \mathrm{f}|, \phi\rangle=\operatorname{Re}\left\langle(\operatorname{sign}\right.$ f)Af, $\left.\phi\rangle \leq\langle | f \mid, A^{\prime} \phi\right\rangle$ by Thm.2.4. Since $C_{c}^{\infty}$ is a core of $B$, it follows from Thm. 4.3 that the semigroup generated by $A$ dominates $(s(t)) t_{t \geqslant 0}$. Let $C$ be the generator of a semigroup $f(t) t^{2}{ }_{20}$ dominating ( $\left.S(t)\right)_{t \geq 0}$. Then
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-294.jpg?height=61&width=1617&top_left_y=2357&top_left_x=231) $\leqslant\langle | f\left|, C^{1} \phi\right\rangle$ for all $f \in C_{c}^{\infty}, \phi \in D\left(C^{1}\right)+b y T h m .4 .2$. It follows from Thm. 4.3 that $(\mathbb{O}(t))_{t \geqq 0}$ dominates the semigroup generated by $A$.

Example 4.16. Let $A_{o}$ be the generator of a positive semigroup on an order complete Banach lattice $E$ and $M \in Z(E)$. The semigroup generated by $A_{o}+M$ possesses a modulus semigroup. Its generator is $A_{o}+$ ReM . (This can be proved as the assertion in Example 4.15.)

If a semigroup has a bounded regular generator then it possesses a modulus semigroup. Its generator is bounded too (see C-I,Sec. 6 for the notion of regular operators).

Theorem 4.17. Let $B$ be a regular, bounded operator on an order complete complex Banach lattice $E$. The semigroup (e ${ }^{t B}$ ) $t \geqslant 0$ possesses a modulus semigroup. Its generator is $A=\left|B_{o}\right|+R e M$, where $B=B_{o}+M$ is the unique decomposition of $B$ in $L^{r}(E)$ satisfying $M \in Z(E), B_{o} \in Z(E)^{d}$.

For the proof we need the following result which is of independent interest.

Leman 4.I8. Let $A$ be the generator of a positive semigroup on a Banach lattice $E$. If $A f \geqslant 0$ for all $\underset{\sim}{f} \in D(A){ }_{+}$, then $A$ is bounded.

Proof. There exists $M \geqq I$ such that $\|R(\lambda, A)\| \leq M / \lambda$ for all $\lambda \geq$ $\omega(A)+1$. Fix $\mu \geqslant \omega(A)+1$ - Then $A R(\mu, A) A f=\mu R(\mu, A) A f-A f=$ $\mu^{2} R(\mu, A) f-\mu f-A f ;$ hence $0 \leq A f \leq \mu^{2} R(\mu, A) f$ whenever $f \in D(A)+$. Thus $\left\|_{1} A f\right\| \leqq C\|f\|_{i}$ for all $f \in D(A)+\left(w h e r e \quad c:=\mu^{2}\|R(\mu, A)\|\right.$ ). Consequent1y.
$\|(\lambda R(\lambda, A)-I d) f\|=\|A R(\lambda, A) f\| \leqq c\|R(\lambda, A) f\| \leqq(M C / \lambda)\|f\|$ for $a I l$
$f \in E_{+}$and all $\lambda \geqq \operatorname{m}(A)+1$. Hence
$\|(\lambda R(\lambda, A)-I d) g\|_{j}^{\prime} \leqq \operatorname{Mc} / \lambda\left(\left\|g^{+}\right\|+\left\|_{i}^{-}\right\|_{i}\right) \leqq(2 M c / \lambda)\|g\|$ for all $g \in E$.
Thus $\lambda R(\lambda, A)$ is invertible if $\lambda$ is large enough and
$D(A)=\operatorname{im}(\lambda R(\lambda, A))=E$.

Proof of Thm. 4. 17 . Let $A=\left|B_{0}\right|+$ ReM . It has been shown in Example $4.4 b$ that $\left(e^{t A}\right){ }_{t \geqq 0}$ dominates $\left(e^{t B}\right)_{t \geqq 0}$. Let ( $\left.u(t)\right)_{t \geqq 0}$ be a positive semigroup dominating $\left(e^{t B}\right)$ tæ0 and $c$ its generator. We first show that $C$ is bounded.
Let $f \in D(C)+$ Then $\operatorname{Re}(B f)=1 i m t \geqslant 01 / t\left(\operatorname{Re}\left(e^{t B} f\right)-f\right) \leqq$ $\lim _{t \downarrow 0} 1 / t(U(t) f-f)=C f$. Hence $(C+|B|) f \geqslant(C-R e B) f \geqq 0$ for all $f \in D(C)+$. By Lemma 4.18 this implies that $C+|B| \quad i s$ bounded. Hence $C$ is bounded as well.

Since $C+\|C\| \cdot I d \geqq 0 \quad b y$ Thm. I. $11, \quad C$ is regular. Let $C=C \quad+N$ where $C_{o} \epsilon Z(E)$ and $N \in Z(E)$, Since $C \geqslant$ ReB by what we just proved, it follows that $N \geq$ ReM.
Let $f \in E_{+}, \phi \in E_{+}^{\prime}$ satisfy $\langle f, \phi\rangle=0$. Then for all $\alpha \in R$,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-296.jpg?height=78&width=1609&top_left_y=492&top_left_x=229) Thus $C-\operatorname{Re}\left(e^{i \alpha_{B}}\right)$ satisfies the positive minimum principle (P) for all $\alpha \in \mathbb{R}$. It follows from Thm. 1.11 that $c-\operatorname{Re}\left(e^{i a_{B}}\right)+$
$(\|C\|+\|B\|) I d \geq 0$ for all a $\in \mathbb{R}$. Applying the band projection onto $Z(E)^{d}$ on both sides of this inequality one obtains that
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-296.jpg?height=87&width=1500&top_left_y=776&top_left_x=229)
$T \in L^{r}(E)$, see $\left.C-I, S e c .7\right)$.
We have proved that $R e M \leq N$ and $\left|B_{0}\right| \leq C_{o}$. This implies that
$\operatorname{Re}((\operatorname{sign} \bar{f}) B f)=\operatorname{Re}\left((\operatorname{sign} \bar{f}) B_{o f} f\right)+(\operatorname{ReM})|f| \leqq C_{O}|f|+N|f|=C|f| \quad$ for allf $f \in E$. It follows from Thm. 4.2 that $\left(e^{t s}\right)$ ta 0 is dominated by $\left(e^{t C}\right)_{t \geq 0}$.

Remark. The proof of Thm. 4.17 shows that any semigroup dominating a semigroup whose generator is bounded and regular has a bounded generator as well.

Example 4.19. Let $E=e^{P}(I \leqq p<\infty)$ or $c_{o}$ and $B \in L^{r}(E)$ be given by the matrix ( $b_{i j}$ ) . The generator $A$ of the modulus semigroup of $\left(e^{t B}\right)$ ta0 is given by the matrix ( $a_{i j}$ ) where $a_{i j}=\left|b_{i j}\right|$ when $i \neq j$ and $a_{i i}=\operatorname{Re} b_{i j}$.

A related question is under which condition a semigroup ( $S$ ( $t$ ) ${ }_{t \geqslant 0}$ is dominated by some positive semigroup. of course, a necessary condition is that every $s(t)$ is a regular operator. on an AL-space this condition is automatically satisfied. But Kipnis (1974) gives an example of a strongly continuous semigroup on $\ell^{1}$ which is not dominated. On the other hand, it has been findependently shown by Kipnis (1974) and Kubokawe (1975) that every contraction semigroup on an $L^{\text {l }}$ space possesses a modulus semigroup (which is contractive as well).

In this section wo consider a special case of domination. Recall from C-I.Sec. 6 that a Iinear operator $S$ on $E$ is called lattice homomorphism if
(5.1) $|S f|=S|f| \quad$ for all $f \in E$.

An operator $S \in L(E)$ is called disjointness preserving if
(5.2) f $\ddagger \perp g$ implies $S f \perp S g$ for all f.g $\in E$.

Note that an operator $s$ is a lattice homomorphism if and only if $s$ is positive and disjointness preserving.

In the following we will consider disjointness preserving semigroups (by this we mean semigroups of disjointness preserving operators) and lattice semigroups (i.e., semigroups of lattice homomorphisms). For example, the semigroup $\left(T_{d}(t)\right)_{t \geq 0}$ defined in section 3 is disjointness preserving for all $d \in \mathbb{R}$ and a lattice semigroup if $d \geqslant 0$.

Proposition 5.1. A bounded operator $S$ on a complex Banach lattice E is disjointness preserving if and only if there exists a linear operator $|s|$ on $E$ such that
$$
\begin{equation*}
|S \underline{f}|=|S||f| \quad(f \in E) \tag{5+3}
\end{equation*}
$$

In that case the operator $|S|$ is uniquely determined by (5.3). $|\xi|$ is a lattice homomorphism and the modulus of $S$ (i.e., one has $|\xi| \leq T$ for all $T \in L(E)$ such that $|S f| \leq T \mid f(\quad(f(E))$.

For the proof of the proposition we refer to Arendt (1983) and de Pagter (1985).

Proposition 5.2 . Let $(S(t))$ t 30 be a disjointness preserving semigroup Let $T(t)=|S(t)|(t \geq 0)$. Then $(T(t)) t \geq 0$ is a strongly continuous semigroup.

Proof. Let $0 \leq s, t$ and $f \in E_{f^{*}}$ Then by (5.1), $T(s) T(t) f=T(s)|S(t) f|$ $=|S(s) S(t) f|=|S(s+t) f|=T(s+t) f$. Since $\operatorname{span} E_{+}=E$, it follows that $(T(t)) t \geqslant 0$ is a semigroup. Moreover, for $f \in E_{+}, \lim _{t \rightarrow 0} T(t) f$ $=\lim _{t \rightarrow 0}|s(t) f|=|f|=f$. This implies that $(T(t)) t \geqslant 0$ is strongly continuous.

Example 5.3. Let $d \in \mathbb{C}$ and $S(t)=T_{d}(t)$ be given by (3.9). Then $\left|T_{d}(t)\right|=\left.T\right|_{d}(t) \quad(t \geq 0)$.

Proposition 5.4. Let B be the generator of a disjointness preserving semigroup $(S(t))_{t \geqq 0}$ on a Banach lattice $E$. Then $B$ is locali i.e. (5.4) $f \pm g$ implies $B f \pm g$ for all $f \in D(B), g \in E$. Proof Let $f \in D(B)$ and $g \in E$ such that infi|f|, $|g| f=0$. Then $|1 / t(S(t) f-f)| \wedge|g| \leq|1 / t S(t) f| \wedge|g|+I / t|f| \wedge|g|$ $=1 / t|S(t) f|$ a $|g|$ $\leq 1 / t|s(t) f| \wedge|S(t) g-g|+(1 / t|S(t) f|)$ ค $|S(t) g|$ $=1 / t|S(t) f| A|S(t) g-g|$ $\leqq|S(t) g-g|$.

Letting $t \rightarrow \infty$ one obtains $|B f| \wedge|g|=0$.

We now describe the relation between the generator of a disjointness preserving semigroup and the generator of the modulus semigroup.

Theorem 5.5. Assume that $E$ is a complex Banach lattice with order continuous norm. Let (s(t)) $\downarrow \geq 0$ be a semigroup with generator $B$. The following assertions are equivalent.
(i) (S(t)) ${ }_{t \geqq 0} 1 s$ disjointness preserving.
(ii) There exists a semigroup (T(t)) tき0 with generator A such that
(5.5) f $f \in D(B)$ implies $|f| \in D(A)$ and $\operatorname{Re}((\operatorname{sign} \mathrm{f} \mid \mathrm{ff})=A|f|$.

Moreover, if these equivalent conditions are satisfied, then $T(t)=|S(t)| \quad(t \geqslant 0)$.

Remark. By B-II, Lemma 2.9 the relation (5,5) is equivalent to $\langle\operatorname{Re}((\operatorname{sign} \bar{f}) \mathrm{Bf}), \phi\rangle=\langle | f\left|, A^{\prime} \phi\right\rangle \quad\left(f \in \mathrm{D}(\mathrm{B}), \phi \in \mathrm{D}\left(\mathrm{A}^{\prime}\right)\right)$.
b) It is remarkable that, in contrast with the situation considered in Theorem 3.8, here condition (ii) implies the positivity of (T(t) tao without further assumptions.

The basic idea of the proof of Theorem 5.5 is to differentiate the equation $|S(t) f|=T(t)|f| \quad($ where $T(t)=|S(t)|$, cf. (5.3)). For
that we need that the modulus function is differentiable. If $E=L^{P}(X, \Gamma, \mu)(1 \leq P<\infty)$ this had been proved in section 2 (Ex. 2,3 ). We extend this result to Banach lattices with order continuous norm.

Proposition 5.6. Let $E$ be a real or complex Banach lattice with order continuous norm. Then the modulus function $\theta: E \rightarrow E$ igiven by $0(h)=|h|)$ is right-sided Gateaux differerentiable and
$$
\begin{equation*}
D_{g} \rho(f)=\operatorname{Re}((s i \hat{g} n \bar{f}) g) \quad(f, g \in E) \tag{5.6}
\end{equation*}
$$

Proof. Let $f, g \in E$. Define $k: \mathbb{R} \rightarrow E \quad b y \quad k(t)=|f+t g|-|f|$. Then $k(0)=0$ and $k$ is convex (i.e., $k(\lambda s+(I-\lambda) t) \leqslant \lambda k(s)+$ (I- 1 ) k(t) Eor all $5, t \in \mathbb{R}, \lambda \in[0,1]$ ).
We show that
$$
\begin{equation*}
k(s) / s \leqq k(t) / t \tag{5.7}
\end{equation*}
$$
whenever $s<t, s, t \neq 0$.
First case: $s<t<0$.
Choose $\lambda=t / s \in(0,1)$. Then $t=(I-\lambda) 0+\lambda s$. Consequently,
$k(t) \subseteq(I-\lambda) k(0)+\lambda k(s)=t / s k(s)$.
Second case; $s<0<t$.
Let $0<\lambda:=t /(t-s)<I$. Then $0=\lambda s+(1-\lambda) t$. Hence $0=k(0)$, $\lambda k(s)+(l-\lambda) k(t)=t /(t-s) k(s)-s /(t-s) k(t)$, which implies (5.7). Third case: $0<s<t$.
Let $\lambda=s / t \in(0,1)$. Then $s=(1-\lambda) 0+\lambda t$. Consequently, $k(s) \leq$ $(1-\lambda) k(0)+\lambda k(t)=s / t k(t)$, which implies (5.7).

It follows from (5.7) that the net $(k(t) / t) t>0$ is decreasing and bounded below (by $-k(-1)$, for instance). since $E$ has order continuous norm, it follows that $D_{g}(f)=l_{i m} t \rightarrow 0+k(t) / t$ exists.
It remains to show that $D_{g}(f) \neq \operatorname{Re}\left(\operatorname{sig} \hat{g}^{\prime} \bar{f}\right) g$.
First of all denote by $P^{g}$ the band projection onto $\{f\}^{d d}$. Then it follows from the definition of $D_{g}{ }^{\theta}(f)$ that $D_{g}{ }^{e(f)}=P D_{g}{ }^{\theta(f)}$ + $(I d-P) D_{g} G(f)=D_{P g}{ }^{\theta(f)}+|(I d-P) g|$. Thus it remains to show that
(5.8) $\quad D_{h}(f)=\operatorname{Re}((\operatorname{sign} f) h) \quad$ whenever $h \in\{f\}^{d d}$.

According to the Kakutani-Krein theorem there exists a compact space $K$ such that $E|f|$ can be identified with $C(K)$. Then by $B-I I$. Lemma 2.4
(5.9) $\quad \lim _{t \rightarrow 0+} 1 / t(|f+t h|-|f|)(x)=\operatorname{Re}(\operatorname{sign}(\overline{f(x)}) h(x)) \quad(x \in K)$.

Let $\phi \in \mathrm{E}_{+}^{\prime}$. Then $\phi$ restricted to $\mathrm{E}_{|\mathrm{f}|}$ can be identified with a regular Borel measure $\mu$ on $C(K)$ +

So it follows from (5.9) and the dominated convergence theorem that $\left\langle D_{h} \rho(f), \phi\right\rangle=1 i m t \rightarrow 0+1 / t<(|f+t h|-|f l|, \phi\rangle$
$$
=\int_{K} \operatorname{Re}(\operatorname{sign}(\bar{f}(x)) h(x)) d \mu(x)=\langle\operatorname{Re}((\operatorname{sign} \bar{f}) h) ; \phi\rangle
$$
(the last identity holds since by the definition of sign $\underset{f}{\in} \in(E)$, we have (sign $\bar{f}) h \in E_{|f|}=C(K)$ whenever $h \in C(K)$ and $((\operatorname{sign} \overline{\mathrm{f}}) \mathrm{h})(\mathrm{x})=(\mathrm{sign} \overline{\mathrm{f}}(\overline{\mathrm{x}} \overline{\mathrm{J}}) \mathrm{h}(\mathrm{x}) \quad($ see C-I, sec. B$)$ ). Consequently, $D_{h}(f)=\operatorname{Re}(\operatorname{sign} \bar{f}) h$ whenever $h \in E|f|$. Since $D_{h}$ (f) is continuous in $h$ (in fact, $!D_{h} \in(f)-D_{k}(f)!\leqq|h-k|$ for all $h, k \in E)$ and $E|f|$ is dense in $\{f\}^{d d}$, it follows that (5.8) holds for all $h \in\{f\}^{d d}$.

Remark 5.7. a) By the same argument as given in the proof one sees that $\theta$ is left-sided Gateaux differentiable and
$$
\mathrm{D}_{\mathrm{g}}^{-} \mathrm{e}(\mathrm{f})=\operatorname{Re}((\operatorname{sign} \overline{\mathrm{f}}) \mathrm{g})-\mathrm{P}_{\mathrm{f}}^{\mathrm{d}}|\mathrm{~g}|
$$
for all $f, g \in E$, where $D_{g}^{-\theta(f)=} \lim _{t_{f} 0} l / t(\theta(f+t g)=\theta(f))$ and $\mathrm{P}_{\mathrm{f}}^{\mathrm{d}}$ denotes the band projection onto $\{\mathrm{f}\}^{\circ}$. In particular, (5.10) $\quad D_{g}^{+} \rho(f)=D_{g}^{-} \rho(f) \quad$ whenever $g \in\{f)^{d d}$.
b) The proof of Prop. 5.6 shows that every convex function $\theta: E \rightarrow E_{R}$ (where $E$ is a Banach lattice with order continuous norm) is right(and left-) sided Gateaux differentiable (cf. Arendt (1982)).

Proof of Theorem 5.5. Assume that (i) holds, Let $f \in D(B)$, Then $S(t) f$ is differentiable in $t$. By the chain rule B-II, Prop. 2.3 . $T(t)|f|=|S(t) f| \quad$ is also differentiable and $d / d t|t=0 \quad T(t)| f \mid=$ $d / d t|t=0| S(t) f \mid=\operatorname{Re}(s i g n \quad \bar{f}) B f \quad(b y \operatorname{Prop} .5 .6)$. Hence $|f| \in D(A)$ and $A|f|=\operatorname{Re}(\operatorname{sign} \bar{f}) B f$.
Conversely, assume that (ii) holds. Let $s>0, f \in E$. We show that $|S(s) f|=T(s)|f|$. This implies that $S(s)$ is disjointness preserving and $|S(s)|=T(s)$ (by Proposition 5.1)). Since $D(B)$ 1s dense we can assume that $f \in D(B)$. Let $\xi(t)=T(s-t)|S(t) f|(t \in[0, s])$. Since by assumption $|S(t) f| \in D(A)$ one obtains $d / d t E(t)=-A T(s-t)|s(t) f|+T(s-t) d / d r|r=t| S(r) f \mid$ $=-A T(s-t)|S(t) f|+T(s-t)(R e(s i g n ~ S(t) f) B S(t) f)$ (by Prop.5.6 and the chain rule B-II, Prop. 2. 3) $=0$ by the assumption (ii).
Hence $\xi(0)=\xi(s) ;$ i.e. $\quad|S(s) f|=T(s)|f|$.

The case when $S(t)=T(t)(t \geq 0)$ is of special interest: it yields a characterization of generators of lattice semigroups.
Recall that if a semigroup (T(t)) $t \geqslant 0$ is positive, i.e., if (5.13) $|T(t) f| \leqq T(t)|f| \quad(f \in E)$,
then its generator $A$ satisfies Kato's inequality. We now obtain from Theorem 5.5: the semigroup consists of lattice homomorphisms (i.e., the equality holds in (5.13)) if and only if A satisfies Kato's equality. The precise statement is the following.

Corollary 5.8. Let $A$ be the generator of a strongly continuous semigroup ( $T(t))_{t \geq 0}$ on a Banach lattice $E$ with order continuous norm. The following assertions are equivalent.
(i) (T(t)) ${ }_{t \geq 0}$ is a lattice semigroup.
(ii) $f \in D(A)$ implies $|f| \in D(A)$ and $\operatorname{Re}((s i g ̂ n$ fiff $=A|f|$. (iii) f $\in D(A)$ implies $|f|, \bar{f} \in D(A)$ and $\operatorname{Re}((\operatorname{sign} \bar{f}) A f)=A|f|$ (Kato's equality).

Proof. The equivalence of (i) and (ii) follows directly from Thm. 5.5. If (i) holds, then $A$ is local by Prop. 5.4.

Thus (sign $\underset{f}{f}) A f=$ (siĝn fiAf for all f $\in D(A)$ and so (iii) holds since (ii) is valid.
Assume now that (iii) holds. Then Kato's equality implies that $A f \in\{f\}^{d a}$ whenever $f \in D(A)+$. Since $D(A)$ is a sublattice of $E$ by hypothesis, this implies that $A$ is local. Thus (ii) follows from (iii).

In the case when $E$ is real this result can be reformulated.

Corollary 5.9. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t z 0}$ on a real Banach lattice $E$ with order continuous norm. The following assertions are equivalent.
(i) $\quad(T(t))_{t \geq 0}$ is a lattice semigroup.
(ii) $D(A)$ is a sublattice and $A$ is jocal.

Proof. Assume that (ii) holds. Let $f \in D(A)$, and set $P_{+}:=P_{f^{+}}$ and $P_{-}:=P_{f^{*}}$.
Then $\left(P_{+}\right) A f^{-}=\left(P_{-}\right) A f^{+}=0$ since $A$ is local. Hence
$(\operatorname{sign} f) A f=\left(P_{+}-P_{-}\right) A f=\left(P_{+}-P_{-}\right)\left(A f^{+}-A f^{*}\right)=\left(P_{+}\right) A f^{+}+\left(P_{-}\right) A f^{-}=$ $A f^{+}+A f^{-}=A|f|$.

Thus Kato's equality holds and it follows from corollary 5.8 that (T(t)) $t \geq 0$ is a lattice semigroup. The other implication follows directly from Corollary 5.8.

Example 5.10. Let $E=L^{P}(X, \mu)$ (where $(X, \mu)$ is a ofinite measure space and $1 \leqslant P<\infty$ and let $A_{o}$ be the generator of a semigroup of lattice homomorphisms. Let $h \in L^{\infty}$ and $B=A_{o}+h$ i.e.. $B$ is given by $B f=A_{o} f+h \times f$ for $f \in D(B)=D\left(A_{o}\right)$. Let $A=A_{o}+\operatorname{Re} h$. Since $A_{o}$ generates a semigroup of lattice homomorphisms, we have $|f| \in D\left(A_{o}\right)$ whenever $f \in D\left(A_{o}\right)$ and $\operatorname{Re}\left((\operatorname{sign} \bar{f}) A_{o} f\right)=A_{o}|f|$. Hence $\left.\operatorname{Re}((\operatorname{sig} n \vec{f}) \mathrm{Bf})=\operatorname{Re}\left((\operatorname{sig} n \bar{f}) A_{o} f\right)+(\operatorname{Re} h)+|f|\right)=$ $A_{o}|f|+(\operatorname{Re~h}) \cdot|f|=A|f|$ for all $f \in D(B)$. Thus it follows from Theorem 5.5 that $B$ generates a disjointness preserving semigroup whose modulus semigroup is generated by $A$.

Next we describe when a disjointness preserving semigroup is positive.

Proposition 5.11. Let $E$ be a complex Banach lattice with order continuous norm and $B$ be the generator of a disjointness preserving semigroup $(S(t))_{t \geqq 0}$. The semigroup is positive if and only if $B$ is real and $\operatorname{span} D(B)_{+}=D(B)$.

Proof. The conditions are clearly necessary. In order to prove sufficiency, we can assume that $E$ is real. Denote by $A$ the generator of $(T(t))_{t \geqslant 0}$, where $T(t)=|S(t)|$. Let $f \in D(B)_{+}$. Since $B$ is local we have $B f=P_{f} B f=(s i g n f l B f=A|f|=A f$. By assumption. span $D(B)_{+}=D(B)$. Thus it follows that $B G A$. This implies that $B=A$ since $\rho(B) \cap \rho(A) \neq \emptyset$.

Remark 5.12. If $B$ is the generator of a disjointness preserving semigroup (s ( $t$ ) $)_{t \geq 0}$ on a real Banach lattice $E$ with order continuous norm then Kato's inequality holds in the reverse sense; i.e.,
$<(s i g n f) \mathrm{Bf}, \phi\rangle \geq\langle | \mathrm{f}\left|, \mathrm{B}^{1} \phi\right\rangle$ for all $\mathrm{f} \in \mathrm{D}(\mathrm{B}), \phi \in \mathrm{D}\left(\mathrm{B}^{\prime}\right)_{+} \cdot$
(cf. (3.9) for a concrete example). In fact. let $T(t)=|S(t)|$ and denote by $A$ the generator of $(T(t))_{t \geq 0}$. Let $f \in D(B), \phi \in D\left(B^{\prime}\right)+{ }^{\prime}$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-302.jpg?height=52&width=1529&top_left_y=2441&top_left_x=229) $\left.\lim _{t \rightarrow 0} 1 / t<S(t)|f|-|f|, \phi\right\rangle=\langle | f\left|, B^{\prime \prime} \phi\right\rangle$.

Finally, we come back to Corollary 5.9. If in condition (ii) we demand that $D(A)$ is not only a sublattice but an ideal of $E$ we obtain a characterization of multiplication semigroups.

Here we call a semigroup (T(t)) $t \geqslant 0$ mutiplication semigroup if $T(t)$ is a multiplication operator (i.e.. an element of the center) for every $t>0$.

Theorem 5.13. Let A be the generator of a strongly continuous semigroup $(T(t))$ t $\geq 0$ on a ororder complete real or complex Banach lattice $E$. The following assertions are equivalent.
(i) (T(t)) ${ }_{t \geq 0}$ is a mutiplication semigroup.
(ii) There exists $\lambda \in \rho(A)$ such that $R(\lambda, A)$ is a multiplication operator.
(iii) $R(\lambda, A)$ is a multiplication operator for all $\lambda \in \rho(A)$.
(iv) $A$ is local and $D(A)$ is an ideal in $E$.
(v) If $f \in D(A)$ then $P f \in D(A)$ for every band projection $P$ on E and APf= PAf.

Proof. Assume that (i) holds and let $\lambda>m(A)$. Since $R(\lambda, A)$ is the Laplace transform of the semigroup, it follows that $R(\lambda, A)$ is local since $T(t)$ is local for all $t \geqslant 0$. This implies $R(\lambda, A) \in Z(E) \quad$ (see $C-I$, Sec. 9 ).
We show that (ii) implies (v). Assume that $\lambda \in \rho(A)$ such that $R(\lambda, A)$ is a multiplication operator. Let $P$ be a band projection. Then $P R(\lambda, A)=R(\lambda, A) P$. Let $f \in D(A), g:=(\lambda-A) f$. Then $P f=$ $P R(\lambda, A) g \neq R(\lambda, A) P g$. Hence $P f \in D(A)$ and $(\lambda-A) P f=P g$. Thus $\mathrm{APf}=\lambda \mathrm{Pf}-\mathrm{Pg}=\mathrm{P}(\lambda \mathrm{f}-\mathrm{g})=\mathrm{PAf}$.

We show that (v) implies (iii). Let $\lambda \in \rho(A)$ and $P$ be a band projection. We have to show that $\operatorname{PR}(\lambda, A)=R(\lambda, A) P$. Let $g \in E$, $f:=R(\lambda, A) g$. Then $P f \in D(A)$ and $A P f=P A f$. Hence $P R(\lambda, A) g=P f$ $=R(\lambda, A)(\lambda-A) P f=R(\lambda, A) P(\lambda-A) f=R(\lambda, A) P g$. It follows from $C-I$, Sec. $g$ that $R(\lambda, A) \in Z(E)$.
(iii) implies (i) since $T(t)=\lim _{n \rightarrow \infty}\left[n / t R(n / t, A) l^{n}\right.$ strongly for a11 t > 0 .
It remains to show the equivalence of (iv) and (v). Assume that (iv) holds, let $f \in D(A)$ and $P$ be a band projection. Then $P f \in D(A)$ and $(I d-P) f \in D(A)$ by the assumption. Since $A$ is local we have APf $=$ PAPf $+(I d-P) A P f=P A P f=P A P f+P A(I d-P) f=P A f . C o n v e r s e l y$, assume (v). Let $f \in D(A)$ and $|g| \leqslant|f|$. Then there exists a band projection $P$ such that $p f=g$. Hence $g \in D(A)$. We have shown
that $D(A)$ is an ideal. Assume that inf $\{|h| f|f|\}=0$. Denote by $P$ the band projection onto $\{i h \mid\} d$. Then $P A f=A P f=A 0=0$. Thus Af $\in\{|h|\}^{d}$. We have proved that $A$ is local.

Corollary 5.I4. A multiplication semigroup (T(t)) $t \geq 0$ on a complex Banach lattice $E$ with order continuous norm is positive if and only if its generator $A$ is real; i.e.r f $\in D(A)$ implies $F \in D(A)$ and $\bar{A}=\overline{(n f)}$.

Proof. The condition is equivalent to $T(t) E_{\mathbb{R}} \subset E_{\mathbb{R}} \quad(t \geqslant 0)$ (cf. Rem. 3.1), so it is clearly necessary. Conversely, if A is real, then denote by $\left(T_{\mathbb{E}}(t){ }_{t}{ }^{2} 0\right.$ the restriction semigroup on $E_{\mathbb{R}}$ and by $A_{\mathbb{R}}$ its generator. Then $A_{\mathbb{R}}$ is local (since $A$ is loca1) and $D\left(A_{p}\right)$ is a sublattice of $E_{\mathbb{R}}$. Thus $\left(T_{\mathbb{R}}(t)\right)_{t \geqslant 0}$ is a lattice semigroup (and so positive) by Cor. 5.9.

The class of bounded operators which generate a lattice semigroup is very restricted.

Proposition 5.15. Let $E$ be a real or complex Banach lattice and $A \in L(E)$. The following assertions are equivalent.
(i) $A \in Z(E)$.
(ii) $e^{t A}$ is disjointness preserving for all $t \geqq 0$.
(iii) $e^{t A} \in 2(E)$ for all $t \in \mathbb{R}$.

Moreover, if $A \in Z(E)$ is real, then $e^{t A} \mathcal{B}$ for all $t \in \mathbb{R}$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-304.jpg?height=56&width=1614&top_left_y=1908&top_left_x=221) it is clear that (i) implies (iii). Assertion (ii) follows trivially from (iii). If (ii) holds, then $A$ is local by Prop.5.4. Hence $A \in Z(E)$.
The last assertion follows from the fact that $2(E)$ is isomorphic to a space $C(K)$ as a Banach Iattice and a Banach algebra.

Proposition. 5.16. Let $E$ be a complex Banach lattice.
Every strongly continuous group (T(t)) t>0 of real operators contained in $Z(E)$ has a bounded generator.

Proof. Let $(T(t))_{t \geq 0}$ be a strongly continuous multiplication
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-305.jpg?height=72&width=1503&top_left_y=321&top_left_x=205) $(t \geqslant 0)$. Then $\|f\|_{1}:=s u p_{t \geq 0}\left\|e^{-w t} T(t)\right\| f \|$ defines an equivalent lattice norm on $E$ for which $\|T(t)\|_{1} s e^{w t}$ ( $t \geqq 0$ ). since $2(E)$ is isometrically isomorphic to a space $C(K)$ (as a Banach lattice), for an operator $s \in Z(E)$ one has $\|S\|=\inf \{c>0:|S| \leq c \cdot I d\}$. Hence the operator norm of $S$ is independent of which lattice noxm equivalent to the given one is considered on $E$. Consequently, $\|T(t)\|=\|T(t)\|_{1} \leq e^{w t} \quad(t \geq 0)$.

If (T(t)) $t \geqq 0$ is a strongly continuous group contained in $Z(E)$, then it follows that $\|T(t)\| \leq e^{w / t \mid}$ ( $t \in \mathbb{R}$ ) for some $w \geq 0$. If in addition the operators $T(t)$ are real one obtains from the above expression for the operator norm that
$$
e^{-w t} \cdot I d \leq T(t) \leq e^{w t} \cdot I d \quad(t \geq 0)
$$

Consequent Iy, $\quad \lim t+0\|T(t)-I d\|=0$.

The assumption that the group consists of real operators is essential in Proposition 5.16. In fact, many differential operators on $L^{2}\left(\mathbb{R}^{n}\right)$ generate a strongly continuous group which (via Fourier transforma* tion) is similar to a multiplication group. A concrete example is the Laplacian (A-I, Example 2.8).
On the other hand, if $E=C(K)(K$ compact), then every strongly continous multiplication semigroup (T(t)) tきo has a bounded gener= ator.
In fact, let $m=T(t) 1 \quad(t \geqslant 0)$. Then $1 i m t \neq 0\|T(t)-I d\|=$ $\lim _{t+0}\left\|_{t}-1\right\|_{m}=0 \quad .1$

Lemma 5.17. Let $E$ be a real Banach lattice with order continuous norm. Let $A \in L(E)$. Assume that there exists a dense sublattice $D$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-305.jpg?height=50&width=1611&top_left_y=2071&top_left_x=208) Then $A \in Z(E)$.

Proof. Let $0 \leqq f \in D$, $\dagger \in E_{t}^{\prime}$ such that $\langle f, \phi\rangle=0$. Since Af $\in\{f\}^{d d}$ by assumption, it follows that $\langle A f, \phi\rangle=0$, Thus $A_{\mid D}$ and $\left.{ }^{-A}\right|_{D}$ satisfy ( $P$ ). It follows from Thm. 1.8 that $\left(e^{t A}\right)$ t $\in R$ is a positive group. Thus $A \in 2(E)$ by Prop.5.15.

Let $A$ be the generator of a positive semigroup and $B \in L(E)$. The semigroup generated by $A+B$ is positive whenever $\left(e^{t B}\right)$ tzo is positive (this follows from (1.8)). However this condition is not
necessary. [For example. Iet $A \in L(E)$ such that $\left(e^{t A}\right) t \geqslant 0$ is positive and let $B=-A$. Then $A+B$ generates a positive semigroup. but ( $\left.e^{t B}\right)_{t \leq 0}$ is positive only if $A \in Z(E)$. The situation is different when $A$ generates a lattice semigroup.

Theorem 5,18. Let $E$ be a real Banach lattice with order continuous norm and $A$ be the generator of a lattice semigroup. Let $B \in L(E)$. The semigroup generated by $A+B$ is positive if and only if $\left(e^{t B}\right)_{t \geqslant 0}$ is positive. The semigroup generated by $A+B$ is a lattice semigroup if and only if $B \in Z(E)$.

Proof. Assume that $A+B$ generates a positive semigroup. Let $f \in D(A)+\quad \phi \in E_{+}^{r}$ such that $\left\langle f_{,} \phi\right\rangle=0$. Since $A$ is local, it follows that $\langle A f, \phi\rangle=0$. But $\langle(A+B) f, \phi\rangle=0$ by Prop. 1.7 . Hence $\langle B f, \phi\rangle \geqslant 0$. We have shown that $B_{\text {( }}(A)$ satisfies the positive minimum principle (Def.1.6), Since $D(A)$ is a sublattice of E (by Cor.5.9), it follows from Thm.l.8 that ( $e^{t B}$, $\geqq 0$ is positive. By Cor.5.9 the operator $A+B$ generates a lattice semigroup if and only if $A+B$ is local. Since $A$ is local, this is equivalent to $\left.{ }^{B}\right|_{D}(A)$ being local. By Lemma 5.17 this is true if and only if $B \in Z(E)$.

\section*{NOTES.}

Section 1. The notion of dispersiveness is due to Phillips (1962) who uses a semiscalar product instead of the subdifferential of the canonical half-norm. Our approach follows Arendt-Chernoff-Kato (1982). Bounded generators of positive semigroups on a special class of ordered Banach spaces (which includes Banach lattices and C*-algebras) were characterized by the positive minfmum principle by Evans and Hanche-olsen (1979). The equivalence of (i) and (iv) in Theorem 1.10 19 due to NagelUhlig (1981). Theoren l. 8 has been obtained independently by Arendt (1984a) and van Casteren (1984).

Section 2. The classical distributional Kato's Inequality for the Laplacian is due to Kato (1973). It is a most elegant tool to prove egsential selfadjointness of Schrödinger operators with domain $\mathrm{C}_{\mathrm{C}}^{\infty}(\mathrm{R}$ ) (cf. Example 4.7).
The relation between Kato's inequality and positivity of $e^{t A}$ was firgt pointed out by sitnon (1977). A criterion for a formnegative operator on a space $L^{2}$ to generate a positive semigroup is given by Beurling-Deny (1958), see also Reed-Simon (1978), Vol. IV, Sec.XIII.12. It was a conjecture of Nagel that some abstract version of

Kato's inequality characterizes the positivity of the semigroup (cf. Nagel-Uhlig (1981)). The necessity of Kato's inequality in the form given in Thm. 2.4 was first proved in [Arendt (1982), Remark 3.10] with a different proof. The proof we give here appeared in Arendt (1984). Miyajima-Okazawa (1984) use this inequality to show that a differential operator on $\mathrm{L}^{\mathrm{P}}\left(\mathrm{R}^{\mathrm{n}}\right)$ which generates a positive semigroup is necessarily of order $\leqslant 2$ and has an elliptic principal part. This result is generalized to the spaces $\mathbb{N}^{P}(\Omega), a \in \mathbb{R}^{\Pi}$ suitable, by Miyajima (1986).

Section 3. In this section we closely follow Arendt (1984). Theorem 3. B, in a sitmilar form but with different proof, has been obtained independently by schep (1985).

Section 4. The characterization of domination by Kato's inequality on a Hilbert space is due to Simon (1977). Further contributions are due to Hess-Schrader-价lenbrock (1977) and Kishimoto-Robinson (1980). Theorem 4.3 is due to Arendt (1984b). The result on Schrodinger operators on $\mathbb{E}^{\mathrm{P}}\left(\mathbb{R}^{\mathrm{n}}\right)$ stated in Exataple 4.7 is due to Kato (1986). The case $p \neq 2$ was proved in Kato (1973), where the classical Kato's inequality was established. Extensive information on Schrödinger semigroups on $I_{i}{ }^{\mathbb{P}}\left(\mathbb{R}^{\mathrm{n}}\right)$ is given in Simon (1982). Other recent results on the $L^{\text {P }}$-theory of Schrodlnger operators are obtained by Davies (1986), Okazawa (1984) and Voigt (1984).
The existence of the modulus semigroup of semigroups with bounded, regular generator (Theorem 4.17) is due to Derndinger (1984) (in the real case).
Proposition 5.15 had been proved in Schaefer-holff-Arendt (1978) by a completely different method.

Section 5. The characterization of generators of lattice semigroups on a Banach lattice with order continuous norm (Cor. 5.8) is due to Nagel-jhlig (1981). An extension of this result to arbitrary Banach lattices is given by Arendt (1982) frofu which the proof of Prop. 5.6 is taken as well.
Local closed operators having an ideal as domain (i,e, operators satisfying condition (iv) of Thm. 5.13) are investigated in detail by Nakano (1950) who calls them dilatators. Peetre (1959) characterizes differential operators by locality (see also Luxemburg (1979)). In the context of $\mathrm{C}^{*}-a 1 \mathrm{gebras}$ local operators are investigated by Batty (1985) and Batty-Robinson (1985).

\title{
SPECTRALTHEORY OFP P O S I T I V E S E M I G R O U P ON BANACH LATTICES \\ by \\ Günther Greiner
}

In Chapter $B-I I I$ we have shown that positive semigroups on spaces $C_{o}(X)$ possess several interesting spectral properties. Now we are going to extend many of the results obtained there to the more general setting of Banach lattices. We will improve some of the results of B-III considerably and give the complete proof of B-III.Thm. 4.1 . Throughout this chapter we will assume that $E \neq\{0\}$ is a complex Banach Iattice.

\section*{1. THE SPECTRAL BOUND}

The fact that the spectral bound of a positive semigroup is always contained in the spectrum (provided that the spectrum is non-empty) is also true in the general setting of Banach lattices. The proof given in B-III, Thm, 1,1 for spaces $C_{o}(X)$ works in the general case too. Another proof is given below (cf. Cor.1.4). Furthermore, Cor, I. 3 and Prop.I. 5 of $B-I I I$ are true in the setting of Banach lattices and their proofs can be carried over to the general case. For the sake of completeness we sumarize these results in the following theorem.

Theorem 1.I. Let $A$ be the generator of a positive semigroup $(T(t))_{t \geq 0}$ on a Banach lattice $E$.
(a) $s(A) \in \sigma(A)$ unless $\sigma(A)=\varnothing$.
(b) For $\lambda_{o} \in \rho(A)$ we have:
$\mathrm{R}\left(\lambda_{\mathrm{O}^{\prime}} \mathrm{A}\right)$ is positive if and only if $\lambda_{\mathrm{O}_{1}}>\mathrm{s}(\mathrm{A})$.
In this case $r\left(R\left(A_{0}, A\right)\right)=\left(\lambda_{0}-s(A)\right)^{O_{1}}$.
(c) If $T(I)$ has a positive fixed vector $h_{o}$, then ker $A$ contains a positive element $h$ such that $h_{o} \in \overline{E_{|h|}}$.
(d) If $T(1)^{\prime} \phi_{o}=\phi_{O}$ for some $\phi_{o} \in E_{+}^{*}$ then there exists $\phi \in D\left(A^{*}\right)+w i t h \quad\{f \in E=\langle | f|, \phi\rangle=0\} \subseteq\left\{f \in E:\langle | f\left|, \phi_{0}\right\rangle=0\right\}$ such that $\mathrm{A}^{*} \boldsymbol{\phi}=0$.

The fact that $s(A)$ is always an eigenvalue of the adjoint (cf. B-III Thm. 1.6 ) is characteristic for spaces $C(K), K$ compact, as can be seen considering the Iraplacian on $L^{P}\left(\mathbb{R}^{n}\right)$ where $I < p <\infty$ or on $C_{o}\left(\mathbb{R}^{n}\right)$ (see B-III, Ex.I.7). Another result which cannot be extended to arbitrary Banach lattices is that spectral bound and growth bound coincide (cf. B-IV, Thm.l.4); an example is given in A-III, Ex.l.3. Despite of this the resolvent $R(\lambda, A)$ of a positive semigroup is given as the Laplace transform of the semigroup in the half-plane $\{z \in \mathbb{C}: \operatorname{Re} z>s(A)\}$ (even in case that $\omega(A)>s(A)$ ). Note however that the integral exists only as an improper Riemann integral. By Datko's Theorem (A-IV,Thm. 1.11) the function $t+e^{-\lambda t} \cdot T(t) f$ cannot be Bochner integrable for all $f \in E$ in case Re $\lambda \leqq \omega(A)$.

Theorem 1.2. Suppose $A$ is the generator of a positive semigroup (T (t) ) $t \geq 0$. For $\operatorname{Re} \lambda>s(A)$ we have:
(1.1) $R(\lambda, A) f=\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s) f d s$ for all $f \in E$.

Moreover, the operators $\int_{0}^{t} e^{-\lambda s} T(s) d s$ tend to $R(\lambda, A)$ with respect to the operator norm as $t \rightarrow \infty$.

Proof. We fix $\lambda_{o}>w(A)$. Then by $A-I, P r o p .1 .11$
$$
\begin{equation*}
R\left(\lambda_{o}, A\right)^{n+1} f=\frac{1}{n!} \int_{0}^{\infty} s^{n} \exp \left(-\lambda_{o} s\right) T(s) f d s \quad\left(n \in \mathbb{N}_{o}, f \in E\right) \tag{1.2}
\end{equation*}
$$

Given $\mu$ such that $s(A)<\mu<\lambda_{o}, f \in E_{+}, \phi \in E_{+}^{\prime}$ then
$(1.3)\langle R(\mu, A) f, \phi\rangle=\sum_{n=0}^{\infty}\left(\lambda_{o}-\mu\right)^{n}\left\langle R\left(\lambda_{o}, A\right)^{n+1} f, \phi\right\rangle=$
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

Given $0 \leq t < r $ and setting $E:=$ Re $\lambda-\mu$ we have:
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

\section*{2. THE BOUNDARY SPECTRUM}

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

Definition 2.4. Let $D$ be an open (non-empty) subset of $\mathbb{C}$ and let $G$ be a Banach space. A mapping $R: D+L(G)$ which satisfies
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

To do this we fix $\lambda \in \Delta$. Then there exists $r_{0}>0$ such that $|r-\lambda| < r $ whenever $r>r_{o}$. Therefore $R(\lambda)=\sum_{n=0}^{\infty}(r-\lambda)^{n}{ }_{R(r)}^{n+1}$ for $r>r_{o}$, which implies for $f \in E$
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
$\phi_{1} \in \cap_{e>0}\left\{r_{1}(r) \cdot|\phi|: 0 < r <\varepsilon\right\}^{-\sigma}$.
Using the resolvent equation (2.8) we get for $r>0, \varepsilon>0$ :
$\left(1-r R_{1}(r)^{\prime}\right) \varepsilon R_{1}(\varepsilon)^{\prime}|\phi|=\varepsilon(r-\varepsilon)^{-1}\left(r R_{1}(r)^{\prime}|\phi|-\left.\varepsilon R_{1}(\varepsilon)^{\prime}\right|_{\phi} \mid\right)$.
since the right hand side tends to 0 as $\varepsilon \rightarrow 0$, we have (1-rR $\left.R_{1}(r)^{\prime}\right) \phi_{1}=0$ or
(2.18) $\quad \lambda R_{I}(\lambda)^{\prime} \phi_{1}=\phi_{1} \quad(\operatorname{Re\lambda }>0)$.

Moreover, from $0<\left|\left\langle h_{1}, \phi\right\rangle\right| \leqq\langle | h_{1}|,|\phi|\rangle \leqslant\left\langle r R_{1}(r)\right| h_{I}|,|\phi|\rangle=$ $<\left|h_{1}\right|, r R_{1}(r)^{+}|\phi|>\quad$ it follows that
(2.19) $\langle | h_{1}\left|, \phi_{1}\right\rangle>0$.

For arbitrary $f_{1} \in E_{1}$, Re $\lambda>0$ we have $<\left|R_{1}(\lambda) f_{1}\right|, \phi_{1}>$ $\left. < r _{1}(\operatorname{Re} \lambda)\left|f_{1}\right|, \phi_{1}\right\rangle^{\prime}=\langle | f_{1}\left|, R_{1}(\operatorname{Re} \lambda)^{\prime} \phi_{1}\right\rangle=(\operatorname{Re} \lambda)^{-1}\langle | f_{1}\left|, \phi_{1}\right\rangle$.
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

\footnotetext{
(2.23) Does every positive semigroup have cyclic boundary spectrum?
}

\section*{3. IRREDUCIBLE SEMIGROUPS}

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-325.jpg?height=64&width=1615&top_left_y=502&top_left_x=232) with domain $D(A \mid I)=D(A) \| I=D(B) \cap I$ is the generator of a semigroup on I . It follows that $I$ is invariant for the semigroup generated by B.
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
Since we assumed that $k$ is strictly positive, $I_{Y}$ is K-invariant if and only if $Y=X \times[-1,1]$ for some measurable set $X \subset[0,1.1$. If we assume that $X$ has positive measure and define $\alpha:=\sup \{x \in[0,1]$ : $\left.\int_{0}^{x} 1_{X}(s) d s=0\right\}$ and $\beta:=\inf \left\{x \in[0,1]: \int_{X}^{1} l_{X}(s) d s=0\right\}$ then we have $\alpha<\beta$ and the support of the function $h:=R(\lambda, A) 1_{Y}$
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

Proof. By Thm. 3.8 and $A-I I I, T h m .5 .4$ we have $\operatorname{Ro}(A)=P_{0}(A)=\sigma(A)=$ ioZ with $\alpha:=\frac{2 \pi}{n \tau}$ for suitable $n \in \mathbb{N}$. We fix $h \in k e r(i a-A)$, $h \neq 0$. Then $|h| \in \operatorname{ker} A$ and there exists $\phi \in$ ker $A^{\prime}$ such that $\langle | h \mid, \phi=1$. According to the Kakutani-Krein Theorem we identify $E|h|$ with $C(K)$. Then $h$ is a unimodular function onto $r$ (use the argument given in the proof of B-III, Thm. 3.6(c)).
We define $i=C(\Gamma) \rightarrow E$ by $i(f):=f o h \in C(K) \cong E_{h} \subset E$, then $i$ is injective. For the monomials $e_{n}(z):=z^{n}$ ( $n \in \mathbb{Z}$ ) we have $i\left(e_{n}\right)=h^{[n]}$ thus $i$ has dense image in $E$ (by AuIII,Thm.5.4). Moreover, $2 \pi \cdot \delta_{n 0}=\left\langle h^{[n]}, \phi\right\rangle=\left\langle i\left(e_{n}\right), \phi\right\rangle=\int_{0}^{2 \pi} e_{n}\left(e^{i t}\right) d t$ for all $n \in T$, hence $\int_{0}^{2 \pi} f\left(e^{i t}\right) d t=\langle i(f), \phi\rangle$ for all $f \in C(f)$. It follows that $(E, \phi) \approx L^{1}(\Gamma)$ and we dofine $j$ to be the canonical mapping from $E$ into $(E, \phi)=L^{1}(F)$ (see $\left.C-I, S e c .4\right)$. Then $j$ has dense image and is injective since $\phi$ is strictly positive (cf. Prop. $3.5(b)$ ) One easily verifies that the diagramm commutes.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-332.jpg?height=89&width=1386&top_left_y=2537&top_left_x=209)
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-333.jpg?height=64&width=1617&top_left_y=2515&top_left_x=214) $J$ is closed (see [Schaefer (1974), III.Thm. 1.2]). T-invariant and we have $P E=$ ker $A \subset J$. Then $P / J=0$ hence the spectral bound $s(A / J)$
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-336.jpg?height=46&width=1617&top_left_y=1025&top_left_x=205) first claim. In order to prove the second, we denote the semigroup corresponding to $A$ and $B$ by ( $T(t)$ ) and (S(t)) respectively. It follows from Prop. 3.3 that (S(t)) is irreducible and we have $S(t)=T(t)+\int_{0}^{t} T(t-s) K S(s) d s \quad$ (see A-II, (1.9)). Iterating this identity we obtain for every $m \in \mathbb{N}, t \geqq 0:$
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

\section*{4. SEMIGROUPS OF LATTICE HOMOMORPHISMS}

In Section 2 we proved that the boundary spectrum of certain positive semigroups is a cyclic set. For semigroups of lattice homomorphisms much more can be said: The whole spectrum is an imaginary additively cyclic subset of $\mathbb{C}$ (cf. Thm. 4.2 ). This result can be used to derive cyclicity results for the eigenvalues in the boundary spectrum of positive semigroups (cf. Cor. 4.3). In the last part of this section we discuss a spectral decomposition of positive groups (cf. Thm.4.10).

Lemma 4.I. Suppose that $(T(t)) t \geq 0$ is a semigroup of lattice homorphisms on a Banach lattice $E$ with generator A.
In case $i \alpha \in \operatorname{Ro}(A), \alpha \in \mathbb{R}$, then one of the following assertions is true:
(a) $i a \mathbb{Z} r^{-} R(A)$;
(b) $\quad\{\lambda \in \mathbf{C}: \operatorname{Re} \lambda<0\}=\operatorname{Ro}(\mathrm{A})$.

Proof. There exists $\phi \in E^{\prime}, \phi \neq 0$ such that $T(t)^{\prime} \phi=e^{i \alpha t} \phi$ ( $t \geq 0$ ). Then we have $|\phi|=\left|T(t)^{\prime} \phi\right| \leqq T(t)^{\prime}|\phi|(t \geqslant 0)$. If we fix $r>w(T)$ and define $\psi:=r R(r, A) \quad|\phi|$, we have
$(4.1) \quad T(t) * \psi \leqq e^{r t_{\psi}}, T(t)^{T} \psi \geqq \psi(t \geqq 0)$ and $|\phi| \leqslant \psi$.

In fact, $A-I,(3.1)$ implies $\left(e^{r t}-T(r)\right) R(r, A) \geqslant 0$ hence $T(t)^{r} \psi=r R(r, A)^{\prime} T(t)^{\prime}|\phi| \leqq r+e^{r t} R(r, A)^{\prime}|\phi|=e^{r t} \psi$.
Moreover, the inequality $T(t)^{\prime}|\phi| \geqq|\phi|$ ( t \& 0 ) implies $T(t)^{\prime} \psi=r R(r, A)^{7} T(t)^{\prime}|\phi| \geqslant r R(r, A)^{r}|\phi|=\psi \quad$ and
$\psi=\operatorname{rR}(r, A)^{\prime}|\phi|=r \int_{0}^{\infty} e^{-r t_{T}(t)^{\prime}|\phi| d t \geqslant r \int_{0}^{\infty} e^{-r t}|\phi| d t=|\phi| .}$
Considering the $A L-s p a c e(E, \psi)$ (see $C-I$, sec. 4 ) the first inequality of $(4,1)$ implies that $(T(t)) t \geqslant 0$ induces a strongly continuous semigroup $\left(T_{1}(t)\right)_{t \geq 0}$ on $(E, \psi)$.
That is we have
$$
\begin{equation*}
T_{1}(t) \circ q_{\psi 1}=q_{\psi} \circ T(t) \quad(t \geq 0) \tag{4.2}
\end{equation*}
$$

Denoting by $A_{1}$ the generator of $\left(T_{1}(t)\right)$ we have $\operatorname{Ro}\left(A_{1}\right) \subset \operatorname{Ro}(A)$.
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-338.jpg?height=358&width=412&top_left_y=746&top_left_x=1256)

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-338.jpg?height=61&width=1620&top_left_y=1951&top_left_x=207) and $A \sigma\left(A_{1}\right) \cap\{\lambda \in \mathbb{C}$ : Re $\lambda<0\}=\phi$. Since the toplogical boundary of the spectrum is always contained in the approximate point spectrum (see $A$-III, Prop.2.2) and $\operatorname{Ro}(T(t)) \backslash(0)=\exp (t R o(A))$ (see $A-I I I$, Thm.6.3), precisely one of the following two cases occurs :
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-338.jpg?height=61&width=1583&top_left_y=2260&top_left_x=219)
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-338.jpg?height=58&width=1605&top_left_y=2318&top_left_x=217)

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-340.jpg?height=75&width=1615&top_left_y=1639&top_left_x=209) exists and we have $T|f|_{o}=\lim _{n \rightarrow \infty} T^{n+1} ;\left.f\left|=|f|_{o}\right.$, i.e. $| f\right|_{O} \in F_{\mathbb{R}}$. For $g \in F_{\mathbb{R}}$ satisfying $4 f \leqslant g$ we have $|f|_{0} \leq g$ thus $|f|_{O}=\sup _{F}\{f,-f\}$. Moreover, $\|f\|_{O}:=\left\||f|_{o}\right\| \quad(f \in f)$ is an equivalent norm on $F$ such that $(F,\|\cdot\|)$ is a Banach lattice.
(b) If $T(s)$ is mean-ergodic then we have ker (1-T(s)) $=P E$ where $P$ is the mean-ergodic projection, i.e. Pf $\left.=\lim _{n \rightarrow \infty} \sum_{k=0}^{n-1} T^{T}\right)^{k} f$. Obviously $P$ is positive, hence II.l1.5 of schaefer (1974) implies that $P E$ is a Banach lattice (for the induced order and an equivalent norm).

The assumptions made in Cor. 4.3 can be weakened slightly (cf. Greiner (1982)). However, one cannot prove cyclicity of $P_{\sigma_{b}}$ (A) for arbitrary positive semigroups.

Example 4.4. At first we recall Ex. 2.13 of Chapter B-III. There we constructed a bounded semigroup on the space $C(\Gamma) \times C_{0}(\mathbb{R})$ such that $\mathrm{Po}_{\mathrm{b}}(\mathrm{A})=\{\mathbf{i k}: k \in \mathbb{Z}, k \neq 0\}$.

Let us perform the same construction on the Hilbert space $H:=L^{2}(\Gamma) \times L^{2}(R)$. For a fixed positive, nonzero function $k \in C_{c}(\mathbb{R})$ we define $T(t)$ on $H$ as follows:
$$
T(t)(f, g)=\left(f_{t}, g_{t}\right) \quad \text { with }
$$
$$
\begin{align*}
& f_{t}(z):=f\left(z \cdot e^{i t}\right) \quad(z \in \Gamma) \text { and }  \tag{4,6}\\
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
Fix $t>0$ and assume $r \in \sigma(T(t)), r>0$ and let $\alpha:=\frac{1}{t} \log r-$ At first we assume $r \in R(\sigma(T(t))$. Then by A-III, Tho. 6.3 there exists $B \in \mathbb{R}$ such that $\alpha+i \beta \in \operatorname{Ro}(A)$. By Lemma 4.1 either $\alpha+i \beta \mathbb{Z} \in \operatorname{Ro}(A)$ or $\{\lambda \in \mathcal{C}: \operatorname{Re} \lambda<\alpha\}=\operatorname{Rg}_{\mathrm{g}}(\mathrm{A})$. In both cases we have a $\in(\mathrm{A})$.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-342.jpg?height=47&width=1323&top_left_y=1530&top_left_x=224)
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
$\int_{0}^{t} e^{-\mu s} T(s) h d s=R(\mu, A) h-e^{-\mu t} T(t) R(\mu, A) h \leq R(\mu, A) h \quad$ which implies assertion (ii).
(ii) $+(i):$ The assumption implies that $\int_{0}^{\infty} e^{-v s} T(s) h \mathrm{ds}:=$ $\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-v s^{\prime}} \mathbf{T}(s) h$ ds exists for $v>\mu$. Using that $A$ is a closed operator it follows that $(v-A)\left(\int_{0}^{\infty} e^{-v S} T(s) h \quad d s\right)=h$. For $v$ sufficiently close to $\mu$ such that $v \in \rho(A) \cap R$ we have $R(v, A) h x$ $\int_{0}^{\infty} e^{-v s} T(s) h d s \geq 0$. By continuity we conclude $R(\mu, A) h \geqq 0$.

By now we are prepared to prove the spectral decomposition for positive groups. Before we formulate the theorem we recall the following consequence of Thm. 4.2 : For any $\mu \in \rho(A)$ IR the line $\mu+i f i$ is a subset of the resolvent set and divides o(A) into disjoint sets. Both sets will be unbounded in general.

Theorem 4.8. Let $\{T(t))_{t \in \mathbb{R}}$ be strongly continuous group of positive operators on a Banach lattice $E$ with order continuous norm.

If $A$ is the generator and $\mu \in p(A) \cap f \quad$ then
$I_{\mu}:=\{f \in E: R(\mu, A)|f| \geq 0\}$ and $J_{\mu}:=\{f \in E: R(\mu, A)|f| \leq 0\}$
are $(T(t))_{t \in \mathbb{R}^{-i n v a r i a n t ~}}$ projection bands, the direct sum of them
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-347.jpg?height=72&width=969&top_left_y=1623&top_left_x=227)
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

\section*{A S Y MPTOTICS}
OF POSITIVE SEMIGROUPS

ON BANACH UATTICES

In this chapter we describe the long term behavior of positive semigroups and discuss some concrete examples in more detail.

The first section is devoted to the stability of positive semigroups, and we give sufficient and necessary conditions which ensure that the semigroup (and the solution of the abstract Cauchy problem, respectively) converges to zero as $t \rightarrow \infty$. It is shown that for positive semigroups stability is determined fairly well by spectral properties of the generator.

In the second section we describe conditions ensuring convergence of the sertigroup (as $t \rightarrow \infty$ ) to an equilibrium point or to a periodic solution. Again we are interested in spectral conditions ensuring such a behavior.

In the final section a series of examples is discussed in more detail. In particular we consider semigroups related to retarded equations and discuss existence of solutions, spectral properties and asymptotic behavior. Most of the examples are motivated by biological models.

\title{
1. STABILITY OF POSITIVE SEMIGROUPS ON BANACH LATTICES
}

\author{
by \\ Ginther Greiner and Frank Neubrander
}

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-352.jpg?height=58&width=1358&top_left_y=2041&top_left_x=229)
(b) We identify $E_{h}$ according to the Kakutani-Krein Theorem with a space $C(K), K$ compact. Considering $T(t)$ as operator from $E$ into $c(K)$, we denote it by $T_{o}$. Then $T_{o}$ is positive hence continuous (see Schaefer (1974), II.Thm.5.3). Let $j: C(K) \cong E_{h} \rightarrow E$ be the canonical inclusion. The spectral radii of $T(T)=j \circ T_{o}$ and $T_{o}{ }^{\circ} j$ coincide and are given by $\rho:=\exp (\tau+4(A))$ - By the Krein-Rutman Theorem (cf. the Corollary to Thm. 2.6 in the Appendix of schaefer (I966) there exists $0<\mu \in C(K)^{r}$ such that ( $\left.\mathcal{P}_{\circ}{ }^{\circ}\right)^{*} \mu=\rho \cdot \mu$. Then $\phi:=T_{\circ}^{\prime} \mu$ is an eigenvector of $\left(j_{>} T_{\rho}\right)^{\prime}$ with eigenvalue $p$. Thus $p \in \operatorname{Ro}(T(T))$ and hence $s(A) \geqq \omega(A)$ by A-III,Thm,6,2.
(c) For $a>s(A), r>\tau, f \in E_{+}$we have
$\int_{0}^{r} e^{-\alpha s}\|T(s) f\| d s=\int_{0}^{\tau} e^{-\alpha s}\|T(s) f\|_{i}^{d} d x+e^{-\alpha \tau} \int_{0}^{r-\tau} e^{-\alpha s}\|T(\tau) T(s) f\| d s \leq$ $\leq \int_{0}^{T} e^{-\alpha s}\|T(s) f\| d s+e^{-a \tau} \int_{0}^{r-\tau} e^{-\alpha s}\langle T(s) f, \phi\rangle d s \leq$ $\leq \int_{0}^{T} e^{-\alpha S}\|T(s) f\| d s+\|R(a, A) f\|$
(the last inequality follows from C-riI, Thm.l.2). Now Datko ${ }^{\text { }} 5$ Theorem (A-IV,Thm.1.11) implies $\omega(A)<\alpha$

For $L^{P}$-spaces, $p \neq 1,2$, $\quad$, it is not known whether spectral- and growth bound of an arbitrary positive semigroup coincide. Using interpolation techniques and Thm.l.1 one can treat some special cases. Before doing this we have to recall some facts on interpolation. For details we refer to [Dunford-Schwartz (1958), VI.10] or [Reed-Simon (1975) , IK.4.3.

Let $(\mathrm{X}, \mathrm{\Sigma}, \mu)$ be a $\sigma$ finite measure space, $1 \leqq p<q<a$ and suppose that $T_{0}: L^{P(\mu)} \cap L^{q}(\mu)+L^{P}(\mu) \cap L^{q}(\mu) \quad$ is a Iinear operator which
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-353.jpg?height=75&width=1617&top_left_y=1270&top_left_x=205) $r \in[P, q], T_{0}$ has a (unique) continuous extension $T_{r}: L^{r}(\mu) \rightarrow L^{r}(\mu)$. Moreover ,
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-354.jpg?height=70&width=1620&top_left_y=616&top_left_x=229) with Re $\lambda$ large enough. Hence by (I. 2 ) $u \rightarrow \log \left[r\left(R\left(k, A_{1 / u}\right)\right)\right.$ is a convex function for large $k \in \mathbb{N}$. We have $\log \left[\left(1-\frac{1}{k} s(1 / u)\right)^{-k} \underset{\sim}{f}=k \cdot \log k+k \cdot \log [k-s(1 / u)]^{-1}=\right.$ $=k \cdot \log k+k \cdot \log \left[r\left(R\left(k, A_{I} / u_{0}\right)\right]^{-1}\right.$,
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

As an application of Thm. 1.5 we consider the Japlacian as generator on $L^{p}\left(R^{n}\right), 1 \leqq p<\infty,($ see $A-I, 2.8)$. For $P=I$ the constant functions are eigenvectors of the adjoint operator, hence $0 \in R G(\Delta)$. Thus the semigroup is not stable on $L^{1}\left(\mathbb{R}^{n}\right)$. On the other hand, for $1 \leqq p<\infty$ there does not exist a non-zero function $h \in L^{P}\left(\mathbb{R}^{n}\right)$ with $\Delta h=0$. Hence $A$ generates a stable semigroup on $L^{p}\left(\mathbb{R}^{n}\right)$ for $1 < p <\infty$.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-358.jpg?height=61&width=992&top_left_y=449&top_left_x=229)
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
where the forcing term $F(t)$ converges to some $f_{0} \in F$ as $t+\infty$. In case that $A$ generates a positive semigroup the assumption $r^{4}(A)<0^{\prime}$, which is needed to prove the next proposition for arbitrary generators (see [pazy (1983), Thm.4.4.4]), can be replaced by the 'stability' of the semigroup. We recall that some important generators as, for example, the Laplacian on $L^{P}\left(\mathbb{R}^{n}\right), 1 < p <\infty$, generate positive, stable semigroups which are not uniformly exponentially stable. Therefore, the weakening of the assumptions on $A$ mentioned above $*$ i.e., replacing $\quad$ w $(A)<0^{\prime}$ by ${ }^{\prime}$ positive and stable' widens the class of equations (1.6) for which the following stability result is applicable. For additional results of this kind see Neubrander (1985b).

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-360.jpg?height=67&width=1478&top_left_y=1029&top_left_x=229)
It follows that the third term in (I. 8 ) tencs to zero.

\section*{2. CONVERGENCE OF POSITIVE SEMIGROUPS \\ by \\ Günther Greiner and Rainer Nagel}

The considerations in this section are motivated by the following guideline:

The asymptotic behavior of a strongly continuous semigroup (T(t)) $t \geqslant 0$ is determined by the (structure, location of the) spectrum $\sigma(A)$ of the generator $A$.

Unfortunately this principle does not hold in general, e.g., there are semigroups with spectral bound less than zero and growth bound greater than zero (see A-III, Ex. $1.3 \& 1.4$ ). In order to prove results in the above direction we have to assume additional hypotheses on the senigroup. Positivity may serve to this purpose. For example, the norm convergence to zero, i.e. $\lim _{t \rightarrow \infty}\|T(t)\|=0$, for a positive semigroup on certain Banach lattices is characterized by the condition $s(A)<0$ (see Thm. I. I). Thus in this case the location of the spectrum determines the norm convergence of the semigroup.
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

Clearly, quasi-compactness was essential in the above example as well as in Thm.2.l. For spaces $C_{o}(X)$ we proved in B-IV,Thm. 2.12 that Doeblin's condition is sufficient for quasi-compactness. Actually this is true in $L^{P}$-spaces with $1 < p <\infty$ as well. We quote the result from Lotz (1986).

Proposition 2.4. Let ( $T(t))_{t}$ ( 0 be a bounded positive semigroup on $E=L^{P}(\mu), 1 < p <\infty$.
Assume that there exist $t_{0} \neq 0, \phi \in E_{+}^{1}, b<1$ such that
(2.4) $\left\|T\left(t_{0}\right) f\right\| \leqq\langle f, \phi\rangle+b\left\|_{i} f\right\|$ for all $f \geqq 0$.

Then $(T(t))_{t \geqslant 0}$ is quasi-compact.

In the following result we replace quasi-compactness by eventual norm-continuity of the semigroup.

Theorem 2.5. Let $T=(T(t))_{t \geq 0}$ be a bounded, eventually normcontinuous positive semigroup with gererator $A$ on a reflexive Banach Iattice $E$. Then $P f:=\lim _{t \rightarrow \infty} T(t) f$ exists for every $f \in \mathbb{E}$. $P$ is a positive projection onto the fixed space Fix (T) $=$ ker $A$.

Proof. In view of Thm. 1.5 it suffices to consider the case
$s(A)=0 \in \operatorname{PG}(A)$, We define $F:=\left\{f \in E: \lim _{t \rightarrow \infty} T(t) f\right.$ exists $\}$. $F$ is closed since $(T(t))_{t \geqslant 0}$ is bounded and obviously ker $A \subset F$. Since $G(A)$ AiR is cyclic and bounded (see C-III,Thm. 2.10 and $A-I I, T h m .1 .20$ resp. $)$ we have $G(A)$ iin $=\{0\}$. Since the spectral mapping theorem holds (cf. A-III,Thm.6.6) we conclude $\sigma(T(t)) \cap \Gamma=\{1\}$ for all $t \geqslant 0$. Then (1.4) implies $\operatorname{Iim}_{n \rightarrow \infty}\|T(n)-T(n+1)\|=0$ hence $\lim _{t \rightarrow \infty}\|T(t)-T(t+1)\|=0$. Take $f=g-T(1) g$. Then $\|T(t) f\|=$
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-363.jpg?height=70&width=1615&top_left_y=2555&top_left_x=206) Thus
(2.5) $\quad \lim _{t \rightarrow \infty} T(t) f=0$ for every $f \in \operatorname{im}(I d-T(I))$.

That is, im(Id $-T(1))=F$. Since ker $A=f_{t \geqslant 0} \operatorname{ker}(I d-T(t))=$ ker(Id - T(1)) (cf. A-III, Cor. 6.4 ) we have
im(Id - T(1)) $+\operatorname{ker}(I d-T(1)) \subset F$.
since power bounded operators on a reflexive Banach space are mean ergodic (e.g., see Krenge1 (1985), Chap. 2,Thm. I. 2) we obtain that im (Id - $T(1)$ ) + ker (Id $-T(1)$ is dense in $E$, hence $F=E$.

Strong convergence of the semigroup $T=(T(t))_{t \geqslant 0}$ implies strong convergence of the Césaromeans $C(t) f:=\frac{1}{t} \cdot \int_{0}^{t} T(s) f d s, f \in E$ which (by definition) is mean ergodicity of the semigroup $T$ (see Davies (1980), Chap.5.1). On the other hand an inspection of the proof of Thm. 2.5 shows that reflexivity of the underlying space can be replaced by the assumption that $T$ is a mean ergodic semigroup.
This remark also shows where to look for examples of semigroups not converging as $t \rightarrow \infty$ : Consider the positive contraction $R$ defined by (Rf)(x) $:=f(x+I)$ on $\left.E=L^{l}(f)\right)$. Then $T(t):=e^{t(R-I d)}$ defines a positive norm-continuous semigroup on $F$. Since $\operatorname{ker}(R-I d)=F i x R=\{0\}$ but $\|T(t) f\|=e^{-t} \sum_{n=0}^{\infty}\left\|R^{n} f\right\| t^{n} / n!=\|f\|>0$ for every $0<f \in E$ we see that $\lim _{t \rightarrow \infty} T(t)$ does not exist for the strong operator topology.
Finally we remark that in Thm.2.5 'eventual norm-continuity' is crucial as well. This can be seen by considering the translation (semi-) groups on $L^{P}(R)$.

In the next few results we study semigroups which are not necessarily eventually normmontinuous, but restrict our attention to positive
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-364.jpg?height=52&width=1620&top_left_y=1916&top_left_x=224) following '0-2 law' which we quote from Greiner (1982), Thm. 3.7.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-365.jpg?height=58&width=1612&top_left_y=1756&top_left_x=202) A-III, Cor. 6.4), hence we have convergence on ker (Id -T(t)). Since $T(\tau)$ is a contraction on a reflexive Banach space we have
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-365.jpg?height=64&width=1600&top_left_y=1921&top_left_x=202) finally proves the convergence on the whole space.

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

It is not difficult to see that $T(t)$ is a positive linear contraction on $L^{1}(\mu)$. We have $T(t), l_{X}=I_{X}$ and $T(t) 1_{X}=l_{X}$ for all $t \geqq 0$ and $T(t) T(s)=T(t+s)$ for $t, s \geqq 0$. This follows from (2.7a), (2.7d) and (2.7c) respectively. Moreover (2.7e) implies strong continuity of the semigroup $(T(t))_{t \geq 0}$. In fact by Prop.1.23 of Davies (1980) we only have to show weak continuity at $t=0$. Since the characteristic functions are total in $L^{\circ "}(\mu)$ this is true provided that $\lim _{t \rightarrow 0}\left\langle T(t) h, l_{C}=\left\langle h, l_{C}\right\rangle\right.$ for $h \in L^{I}(\mu), C \in E$. Given $h\left(L^{1}(\mu)\right.$, then by (2.7e) $\lim _{t \rightarrow 0} P_{t}(x, C) h(x)=l_{C}(x) h(x)$ $\mu$-a.e. By Lebesgue's Theorem $\left\langle T(t) h, l_{C}\right\rangle=\int P_{t}(x, C) h(x) d \mu(x)$ tends to $\int l_{C}(x) h(x) d_{\mu}(x)=\left\langle h_{r} 1_{C}\right\rangle a s \quad t \rightarrow 0$ and we have weak hence strong continuity.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-368.jpg?height=70&width=1623&top_left_y=1330&top_left_x=219) operator hence by (2.9) all the assumptions of Cor.2.Io are satisfied. Thus we have convergence on the the principal ideal $E_{j}$. Since the semigroup is bounded and the union of these ideals is total in $L^{P}(\mu)$ we have convergence on the whole space.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-371.jpg?height=93&width=1617&top_left_y=1184&top_left_x=205) $t \geqq 0, q \geqq p$.
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

\title{
3. A SEMIGROUP APPROACH TO RETARDED ECUATIONS
}
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-375.jpg?height=58&width=1617&top_left_y=1159&top_left_x=205) $\varepsilon_{\lambda}$ denotes the function $s \rightarrow e^{\lambda s}$ as an element of $L^{1}[-1,0]$ and
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-375.jpg?height=64&width=1620&top_left_y=1259&top_left_x=207) and $s \in[-1,0]$. clearly $\left\|_{E_{\lambda}}\right\|_{i}^{i}=1 / \lambda \cdot\left(1-e^{-\lambda}\right) \rightarrow 0$ as $\lambda \rightarrow \infty$ and we have $\left\|S_{\lambda}\right\|=\|E\|_{\lambda}\|\cdot\| \Phi\left\|_{i}=1 / \lambda \cdot\left(1-e^{-\lambda}\right) \cdot\right\| \Phi\|\leq 1 / \lambda \cdot\| \Phi \|_{\|}^{\|}$.
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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-381.jpg?height=78&width=1600&top_left_y=2108&top_left_x=205) since $K(s)$ are positive and irreducible operators.
Especially, $\Phi_{\mu} x_{\lambda}>\Phi_{\lambda} x_{\lambda}=r\left(\Phi_{\lambda}\right) x_{\lambda} \quad$ and by evaluation
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-381.jpg?height=58&width=1611&top_left_y=2318&top_left_x=208) Since the operators $\Phi_{\lambda}$ are irreducible for each $\lambda$ (due to the irreducibility of $K(s)$ ) $x_{\mu}$ ' is a strictly positive functional on $F$. Hence $\left\langle x_{\lambda}, X_{\mu}{ }^{\prime}\right\rangle \neq 0$ and thus $\left.r\left(\Phi_{\mu}\right)\right\rangle r\left(\Phi_{\lambda}\right)$.

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-382.jpg?height=92&width=1623&top_left_y=1687&top_left_x=225) and, moreover, $\left(\Phi_{\mu}\right)^{n} f \geqq e^{n(\mu-\lambda) E}\left(\Phi_{\lambda}\right)^{n} f \quad$ for every $n \in$ 前. Hence ${ }_{i 1}\left(\Phi_{\mu}\right)^{n}\left\|>e^{n(\mu-\lambda) \varepsilon_{i}}\right\|\left(\Phi_{\lambda}\right)^{n H}$ and consequently $\quad r\left(\Phi_{\mu}\right) \leq e^{(\mu-\lambda) \varepsilon_{i}} r\left(\Phi_{\lambda}\right)$.
Now $(\mu-\lambda) \varepsilon>0$ implies $r\left(\Phi_{\mu}\right)>r\left(\Phi_{\lambda}\right)$.

The theory developed so far can also be applied to certain population equations. We first notice that (ACP) is isomorphic (in an obvious manner) to the following Cauchy problem.
For some $r \in R_{+}$take $E:=L^{l}([0, r], F)$ and let $A:=-\frac{d}{d x}$ on the domain $D(A):=\left\{f \in A C([0, r], F): f^{\prime} \in E\right.$ and $\left.f(0)=\Phi(f)\right\}$ for some $\Phi \in L(E, F)$.
We adopt this setting and transform the above results; e.g., en has to be defined as $\varepsilon_{\lambda}(s): \# e^{-\lambda_{s}}$ instead of $e^{\lambda s}$. As a concrete example we consider the following.

Example 3.12. Let $F:=\mathbb{K}^{n}, E:=L^{1}([0, r], F)=\Pi_{k=1}^{n} F_{k}, F_{k}=L^{1}[0, r]$. and defíne $\Phi: E \rightarrow c^{n}$ by $\Phi=\left\langle v_{i j} j_{n \times n}\right.$ where
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-383.jpg?height=78&width=1589&top_left_y=378&top_left_x=205) As $\Phi_{\lambda}$ we obtain the scalar matrix,
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-383.jpg?height=318&width=1523&top_left_y=543&top_left_x=204)

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
![](https://cdn.mathpix.com/cropped/2025_01_13_f0e65ab81a0d812d779fg-383.jpg?height=547&width=1620&top_left_y=1988&top_left_x=201)
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

