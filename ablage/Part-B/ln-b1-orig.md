## PART B

## POSITIVE SEMIGROUPS ON $C_{0}(X)$

CHAPTER B-I

## BASIC RESULTS ON SPACES C C (X)

by
Rainer Nagel and Ulf Schlotterbeck

This part, of the book is devoted to a study of one-parameter semigroups of operators on spaces of continuous functions of type $C_{0}(X)$, spaces which are Banach lattices of a very special kind. We treat this case separately since we feel that an intermingling with the abstract Banach lattice situation considered in Part $C$ would have made it difficult to appreciate the easy accessibility and the pilot function of methods and results available here. In this chapter we want to fix the notation we are going to use and to collect some basic facts about the spaces we are considering.

If $X$ is a locally compact topological space, then $C_{0}(x)$ denotes the space of all continuous complex-valued functions on $x$ which vanish at infinity, endowed with the supremum-norm. If $X$ is compact, then any continuous function on $x$ "vanishes at infinity" and $C_{0}(X)$ is the space of all continuous functions on $X$. We often write $C(X)$ instead of $C_{0}(X)$ in this situation. We sometimes study real-valued functions and write the corresponding real spaces as $C_{o}(X, \mathbb{R})$ and $C(X, \mathbb{R})$, and the notations $C_{o}(X, C)$ and $C(X, C)$ are used if there is the possibility of confusion between both cases.

## 1. ALGEBRAIC AND ORDER-STRUCTURE: IDEALS AND QUOTIENTS

Any space $C_{0}(X)$ is a commutative $C^{*}$-algebra under the sup-norm and the pointwise multiplication, and by the Gelfand Representation Theorem any commutative $c^{\star}-a l g e b r a ~ c a n, ~ o n ~ t h e ~ o t h e r ~ h a n d, ~ b e ~ c a n o n i-~$ cally represented as an algebra $C_{o}(x)$ on a suitable locally compact space $X$. The algebraic notions of ideal, quotient, homomorphism are
well known and need not be explained further. Another natural and important structure of $C_{o}(X)$ is the pointwise ordering, under which $C_{o}(X, \mathbb{F})$ is a (real) Banach lattice and $C_{o}(X, C)$ a complex Banach lattice in the sense explained in Chapter C-I. Concerning the order structure of $C_{o}(x)$ we use the following notations: For a function $f$ in $C_{0}(\mathrm{X}, \mathbb{R})$

```
f\geqq0 means f(t) }\geq0\mathrm{ for all t & X (f is then called
positive),
f > 0 means that f is positive but does not vanish iden*
    tically,
f >> means that f(t) >0 for all t in X (f is then
called strictly positive).
```

The notion of an order ideal explained in Chapter $C-I$ applies of course to the Banach lattices $C_{o}(X)$ and might give rise to confusion with the corresponding algebraic notion. However, since we are mainly considering closed ideals and since a closed linear subspace I of $C_{o}(\mathrm{X})$ is a lattice ideal if and only if $I$ is an algebraic ideal, we may and will simply speak of closed ideals without specifying whether we think of the algebraic or the order theoretic meaning of this word. An important and frequently used characterization of these objects is the following: $A$ subspace $I$ of $C_{o}(X)$ is a closed ideal if and only if there exists a closed subset $A$ of $X$ such that a function $f$ belongs to $I$ if and only if $f$ vanishes on $A$. $A$ is of course uniquely determined by $I$ and is called the support of $I$. If $I=I_{A}$ is a closed ideal with support $A$ then $I_{A}$ is naturally isomorphic to $C_{0}(X, A)$ and the quotient $C_{0}^{(X)} / I^{(X)}$ is (under the natural quotient structure) again a Banach algebra and a Banach lattice that can be identified canonically (via the map $f+I+f_{A}$ ) with $C_{0}(A)$.

## 2. LINERR FORMS AND DUALITY

The Riesz Representation Theorem asserts that the dual of $C_{0}(x)$ can be identified in a natural way with the space of bounded regular Borel measures on $X$. While there is no natural algebra structure on this dual, the dual ordering (see $C-I$ ) makes $C_{o}(X)$ ' into a Banach lattice. We will occasionally make use of the order structure of $C_{o}(X)$ ' but since at least its measure theoretic interpretation is supposed to be well-known, it may suffice here to refer to Chapter c-I, Sections 3
and 7 , for a more detailed discussion and to recall some basic notations here: If $H$ is a linear form on $C_{0}(X, B)$ then

```
# > means u(f) \geqq 0 for all f \geqq 0 ; th is then called
    positive (positivity automatically implies continuity),
~ > means that }\mu\geqq0\mathrm{ , but }\mu\mathrm{ does not vanish identically,
|>>0 meang that }\mu(f)>0\mathrm{ for any f > O; u is then called
strictly positive.
```

If $\mu$ is a linear form on $C_{0}(X, C)$, then $H$ can be written uniquely as $\mu_{1}=H_{1}+H_{2}$ where $H_{1}$ and $H_{2}$ map $C_{o}(X, R)$ into $\mathbb{F}$ (decomposition into real and imaginary parts). We call 4 positive (strictly positive) and use the above notations if $\|_{2} * 0$ and $\mu_{1}$ is positive (strictly positive). We point out that strictly positive linear forms need not exist on $C_{o}(X)$, but if $X$ is separable then a strictly positive linear form is obtained by suming a suitable sequence of point measures.

The coincidence of the notions of a closed algebraic and a closed lattice ideal in $C_{0}(X)$ has of course its effect on the algebraic and the lattice theoretic notions of a homomorphism. The case of a homomorphism into another space $C_{0}(Y)$ will be discussed below. As for homomorphisms into the scalar field, we have essentially coincidence between the algebraic and the order theoretic meaning of this word, more exactly: A linear form $\mu \neq 0$ on $C_{0}(X)$ is a lattice homomorphism if and only if $\&$ is, up to normalization, an algebra homonorphism (algebra homomorphisms $\neq 0$ must necessarily have norm 1 ). since the algebra homomorphisms $\neq 0$ on $C_{0}(x)$ are known to be the point measures (denoted by $\delta_{t}$ ) on $X$ and since on the other hand iu is a lattice homomorphism if and only if $|\mu(f)|$ equals $f(|f|)$ for all f , it follows that this latter condition on $w$ is equivalent to bs aby for a suitable $t$ in $x$ and a positive roal number a . This can be summarized by saying that $X$ can be canonically identified, via the map $t \rightarrow \delta_{t}$, with the gubset of the dual $C_{o}(X)$ ' consisting of the non-zero algebra homomorphisms, which is also the set of all normalized lattice homomorphisms. This identification is a topological isomorphism with respect to the weak*-topology of $\mathrm{C}_{\mathrm{O}}(\mathrm{X})^{\prime}$.

## 3. LINEAR OPERATORS

A linear mapping $T$ from $C_{D}(X, \mathbb{R})$ into $C_{O}(Y, \mathbb{R})$ is called
positive (notation: $T \geqq 0$ ), if $T f$ ig a positive function whenever $f$ is positive,
a lattice homomorphism if $|T f|=T|f|$ for all $f$.
a Markov-operator if $X$ and $Y$ are compact and $T$ is a positive operator mapping $1_{X}$ to $1_{Y}$.

In the case of complex scalars $T$ can be decomposed into real and imaginary parts. We call $T$ positive in this situation if the imaginary part of $T$ is $=0$ and the real part is positive. The terms "Markov operator" and "lattice homomorphism" are defined formally in the same way as above. Note that a complex lattice homomorphism is necessarily positive, and that the complexification of a real lattice homomorphism is a complex lattice homomorphism. Positive Operators are always continuous.

Since the adjoint of a Markov operator $T$ maps positive normalized measures into positive normalized measures while the adjoint of an algebra homomorphism (lattice homomorphism) maps point measures into (multiples of) point measures, the adjoint of a Markov lattice homomorphism as well as the adjoint of an algebra homomorphism induces a continuous map $\phi$ from $Y$ (viewed as a subset of the weak dual $C(Y)$ ' $\quad$ into $X$ (viewed as a subset of $C(X)$ ' . This mapping $\phi$ determines $T$ in a natural and unique way, so that the following are equivalent assertions on a linear mapping $T$ from a space $C(X)$ into a space $C(Y)$ :
(a) $T$ is a Markov lattice homomorphism
(b) $T$ is a Markov algebra homomorphism
(c) There exists a continuous map $\phi$ from $Y$ into $X$ such $T f *$ fod for all $f \in C(X)$.

If $T$ is in addition bijective, then the mapping $\phi$ in (c) is a homeomorhism from $Y$ onto $X$. This characterization of homomorphisms carries over mutatis mutandis to situations where the conditions on $\mathrm{X}, \mathrm{Y}$ or $T$ are less restrictive. For later reference we explicitly state:
(i) Let $K$ be compact. Then $T \in L(C(K))$ is a lattice homomorphism if and only if there is a mapping $\phi$ from $K$ into $K$ and a function
$h \in C(K)$ such that $T f(s)=h(s) f(\phi(s))$ holds for all $s \in K$. $\quad$ ( $\quad$ is continuous in every point $t$ with $h(t) \neq 0$.
(ii) Let $X$ be locally compact, $T \in\left(C_{o}(X)\right)$. $T$ is a lattice isomorphism if and only if there is a homeomorhism $\phi$ from $x$ onto $X$ and a bounded continuous function $h$ on $x$ such that $h(s) \geqq \delta>0$ for all $s$ and Tf(s) $\quad$ h(s)f(申(s)) ( $s \in X)$. T is an algebraic *-isomorphism if and only if $T$ is a lattice isomorphism and the function $h$ above is $\equiv 1$.

