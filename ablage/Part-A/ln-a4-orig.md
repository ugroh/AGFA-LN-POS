by
Frank Neubrander

In this chapter we study the asymptotic behavior of the solutions of the initial value problem

$$
\begin{equation*}
\dot{u}(t)=A u(t)+F(t), u(0)=f \tag{*}
\end{equation*}
$$

with respect to time $t \geqslant 0$. Here $A$ will be a generator of a strongly continuous semigroup $(T(t)) t \geq 0$ on a Banach space $E$ and $F(\cdot)$ is a function from $\mathbb{R}_{+}$with values in $E$.
In Section 1 we investigate whether and how fast a solution $T(\cdot) f$ of the homogeneous problem tends to the zero solution as $t \rightarrow \infty$; in Section 2 we consider the long term behavior of the solutions of (*) for different classes of forcing terms $F$.

1. STABILITY : HOMOGENEOUS CASE

Let $(T(t)) t \geqslant 0$ be a semigroup on $E$ with generator $A$ An initial value $f \in D(A)$ ig called stable if the solution $t \rightarrow T(t) f$ of
$(\mathrm{ACP}) \quad \dot{u}(\mathrm{t})=\mathrm{Au}(\mathrm{t}), \mathrm{u}(0)=\mathrm{f}$
converges to zero as t tends to infinity. The semigroup is called stable if every solution converges to zero; i.e., if every initial value $f \in D(A)$ is stable.

If the space $E$ is finite dimensional, then the stability of the semigroup implies that the decay is exponential. More precisely, the statements
(a)
(b)

$$
\begin{aligned}
& \|T(t) f\| \rightarrow 0 \text { for every } f \in \mathbb{C}^{n}, \\
& \|T(t)\| \leq M e^{-\omega t} \text { for some } \omega>0
\end{aligned}
$$

are equivalent. Moreover, these statements hold if and only if

$$
s(A)=\sup \{\operatorname{Re} h: h \in \sigma(A)\}<0,
$$

see $A-I I I, C o r .1 .2$.

As already discussed in Chapter $A \rightarrow I I I$ the situation is far more difficult in the infinite dimensional case. Here, and for unbounded generators, we have to distinguish between strong and generalized (mild) solutions of $u(t)=A u(t)$ and between various notions of stability. Recall that for $f \in D(A)$ the function $T(\cdot) f$ is a strong solution of (ACP) (see A-II, Cor.l.2.); for arbitrary $f \in E$ the function $T(\cdot) f$ is called a generalized or mild solution of (ACP). Next we introduce several constants characterizing the growth of the solutions of (ACP).

Definition 1.1 ( $1^{s t}$ part). Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$. Then
(i) $\quad \omega(f):=\inf \left\{w: \| T(t) f \mid \leq M e^{W t}\right.$ for some $M$ and every $\left.t z 0\right\}$ is called the (exponential) growth bound of T(:)f.
(iii) $\omega_{1}(\vec{R}):=\sup \{\omega(f): f \in D(\vec{R})\}$ is called the (exponential) growth bound of the solutions of the cauchy problem $u(t)=A u(t)$.
$i(A)=\sup \{u(f): f \in E\}$ is called the (exponential) growth
bound of the mild solutions of the cauchy problem
$\dot{u}(\mathrm{t})=\mathrm{Au}(\mathrm{t})$.

Note that, by the Principle of Uniform Boundedness, sup(w(f): $f \in E\}$ $=\inf \left\{\omega: \mid f(t) \| \sum M e^{\mu t}\right.$ for some $M$ and every $\left.t \geqq 0\right\}$. Hence $\omega(A)$ coincides with the growth bound of the semigroup (T(t)) teo as defined in $A-T, 1.3$. With the constants defined above we obtain the following stability concepts.

Definition 1.1 ( $2^{\text {nd }}$ part). The semigroup $(T(t))$ t $\geq 0$ is called
(iv) uniformly exponentially stable if $w(A)<0$;
(v) exponentially stable if $\omega_{1}(A)<0$;
(vi) uniformly stable if $\|T(t) f\|_{i} \rightarrow 0$ (as $t \rightarrow \infty$ for every $f \in E$;

```
    stable if |T(t)f|->0 (as t t m) for every f f D(B).
```

The interrelation between these stability concepts is given by
<img class="imgSvg" id = "m5y4xow14cjpiaec47k" src="data:image/svg+xml;base64,PHN2ZyBpZD0ic21pbGVzLW01eTR4b3cxNGNqcGlhZWM0N2siIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDE2NiA1Ny43NTAwNTUwOTQ2OTg2NSIgc3R5bGU9IndpZHRoOiAxNjUuODM5MzkwMDU0NjMwNTRweDsgaGVpZ2h0OiA1Ny43NTAwNTUwOTQ2OTg2NXB4OyBvdmVyZmxvdzogdmlzaWJsZTsiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1tNXk0eG93MTRjanBpYWVjNDdrLTEiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iOTYuNTU5NjAwNDM4NDA3MjciIHkxPSIyMS4wMDAwMzY3Mjk4MDE0OCIgeDI9IjEyMy44MzkzOTAwNTQ2MzA1NCIgeTI9IjM2Ljc1MDA1NTA5NDY5ODY1Ij48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1tNXk0eG93MTRjanBpYWVjNDdrLTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iNjkuMjc5Nzg5NjE2MjIzMjUiIHkxPSIzNi43NTAwMTgzNjQ4OTcxNyIgeDI9Ijk2LjU1OTYwMDQzODQwNzI3IiB5Mj0iMjEuMDAwMDM2NzI5ODAxNDgiPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIyMCUiPjwvc3RvcD48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMTAwJSI+PC9zdG9wPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lLW01eTR4b3cxNGNqcGlhZWM0N2stNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSI0MiIgeTE9IjIxIiB4Mj0iNjkuMjc5Nzg5NjE2MjIzMjUiIHkyPSIzNi43NTAwMTgzNjQ4OTcxNyI+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjIwJSI+PC9zdG9wPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PG1hc2sgaWQ9InRleHQtbWFzay1tNXk0eG93MTRjanBpYWVjNDdrIj48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ3aGl0ZSI+PC9yZWN0PjxjaXJjbGUgY3g9IjEyMy44MzkzOTAwNTQ2MzA1NCIgY3k9IjM2Ljc1MDA1NTA5NDY5ODY1IiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjY5LjI3OTc4OTYxNjIyMzI1IiBjeT0iMzYuNzUwMDE4MzY0ODk3MTciIHI9IjcuODc1IiBmaWxsPSJibGFjayI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDIiIGN5PSIyMSIgcj0iNy44NzUiIGZpbGw9ImJsYWNrIj48L2NpcmNsZT48L21hc2s+PHN0eWxlPgogICAgICAgICAgICAgICAgLmVsZW1lbnQtbTV5NHhvdzE0Y2pwaWFlYzQ3ayB7CiAgICAgICAgICAgICAgICAgICAgZm9udDogMTRweCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAgICAgICAgIGFsaWdubWVudC1iYXNlbGluZTogJ21pZGRsZSc7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAuc3ViLW01eTR4b3cxNGNqcGlhZWM0N2sgewogICAgICAgICAgICAgICAgICAgIGZvbnQ6IDguNHB4IEhlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+PGcgbWFzaz0idXJsKCN0ZXh0LW1hc2stbTV5NHhvdzE0Y2pwaWFlYzQ3aykiPjxsaW5lIHgxPSI5Ni41NTk2MDA0Mzg0MDcyNyIgeTE9IjIxLjAwMDAzNjcyOTgwMTQ4IiB4Mj0iMTIzLjgzOTM5MDA1NDYzMDU0IiB5Mj0iMzYuNzUwMDU1MDk0Njk4NjUiIHN0eWxlPSJzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLXdpZHRoOjEuMjYiIHN0cm9rZT0idXJsKCcjbGluZS1tNXk0eG93MTRjanBpYWVjNDdrLTEnKSI+PC9saW5lPjxsaW5lIHgxPSI2OS4yNzk3ODk2MTYyMjMyNSIgeTE9IjM2Ljc1MDAxODM2NDg5NzE3IiB4Mj0iOTYuNTU5NjAwNDM4NDA3MjciIHkyPSIyMS4wMDAwMzY3Mjk4MDE0OCIgc3R5bGU9InN0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utd2lkdGg6MS4yNiIgc3Ryb2tlPSJ1cmwoJyNsaW5lLW01eTR4b3cxNGNqcGlhZWM0N2stMycpIj48L2xpbmU+PGxpbmUgeDE9IjQyIiB5MT0iMjEiIHgyPSI2OS4yNzk3ODk2MTYyMjMyNSIgeTI9IjM2Ljc1MDAxODM2NDg5NzE3IiBzdHlsZT0ic3Ryb2tlLWxpbmVjYXA6cm91bmQ7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS13aWR0aDoxLjI2IiBzdHJva2U9InVybCgnI2xpbmUtbTV5NHhvdzE0Y2pwaWFlYzQ3ay01JykiPjwvbGluZT48L2c+PGc+PHRleHQgeD0iMTE5LjkwMTg5MDA1NDYzMDU0IiB5PSI0Mi4wMDAwNTUwOTQ2OTg2NSIgY2xhc3M9ImVsZW1lbnQtbTV5NHhvdzE0Y2pwaWFlYzQ3ayIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iCiAgICAgICAgICAgICAgICB0ZXh0LWFuY2hvcjogc3RhcnQ7CiAgICAgICAgICAgICAgICB3cml0aW5nLW1vZGU6IGhvcml6b250YWwtdGI7CiAgICAgICAgICAgICAgICB0ZXh0LW9yaWVudGF0aW9uOiBtaXhlZDsKICAgICAgICAgICAgICAgIGxldHRlci1zcGFjaW5nOiBub3JtYWw7CiAgICAgICAgICAgICAgICBkaXJlY3Rpb246IGx0cjsKICAgICAgICAgICAgIj48dHNwYW4+TjwvdHNwYW4+PHRzcGFuIHN0eWxlPSJ1bmljb2RlLWJpZGk6IHBsYWludGV4dDsiPkg8dHNwYW4gYmFzZWxpbmUtc2hpZnQ9InN1YiIgY2xhc3M9InN1Yi1tNXk0eG93MTRjanBpYWVjNDdrIj4yPC90c3Bhbj48L3RzcGFuPjwvdGV4dD48dGV4dCB4PSIxMjMuODM5MzkwMDU0NjMwNTQiIHk9IjM2Ljc1MDA1NTA5NDY5ODY1IiBjbGFzcz0iZGVidWciIGZpbGw9IiNmZjAwMDAiIHN0eWxlPSIKICAgICAgICAgICAgICAgIGZvbnQ6IDVweCBEcm9pZCBTYW5zLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAiPjwvdGV4dD48dGV4dCB4PSI5Ni41NTk2MDA0Mzg0MDcyNyIgeT0iMjEuMDAwMDM2NzI5ODAxNDgiIGNsYXNzPSJkZWJ1ZyIgZmlsbD0iI2ZmMDAwMCIgc3R5bGU9IgogICAgICAgICAgICAgICAgZm9udDogNXB4IERyb2lkIFNhbnMsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICI+PC90ZXh0Pjx0ZXh0IHg9IjY5LjI3OTc4OTYxNjIyMzI1IiB5PSIyOC44NzUwMTgzNjQ4OTcxNzMiIGNsYXNzPSJlbGVtZW50LW01eTR4b3cxNGNqcGlhZWM0N2siIGZpbGw9ImN1cnJlbnRDb2xvciIgc3R5bGU9IgogICAgICAgICAgICAgICAgdGV4dC1hbmNob3I6IHN0YXJ0OwogICAgICAgICAgICAgICAgd3JpdGluZy1tb2RlOiB2ZXJ0aWNhbC1ybDsKICAgICAgICAgICAgICAgIHRleHQtb3JpZW50YXRpb246IHVwcmlnaHQ7CiAgICAgICAgICAgICAgICBsZXR0ZXItc3BhY2luZzogLTFweDsKICAgICAgICAgICAgICAgIGRpcmVjdGlvbjogbHRyOwogICAgICAgICAgICAiPjx0c3Bhbj5OPC90c3Bhbj48dHNwYW4gc3R5bGU9InVuaWNvZGUtYmlkaTogcGxhaW50ZXh0OyI+SDwvdHNwYW4+PC90ZXh0Pjx0ZXh0IHg9IjY5LjI3OTc4OTYxNjIyMzI1IiB5PSIzNi43NTAwMTgzNjQ4OTcxNyIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iNDcuMjUiIHk9IjI2LjI1IiBjbGFzcz0iZWxlbWVudC1tNXk0eG93MTRjanBpYWVjNDdrIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSIKICAgICAgICAgICAgICAgIHRleHQtYW5jaG9yOiBzdGFydDsKICAgICAgICAgICAgICAgIHdyaXRpbmctbW9kZTogaG9yaXpvbnRhbC10YjsKICAgICAgICAgICAgICAgIHRleHQtb3JpZW50YXRpb246IG1peGVkOwogICAgICAgICAgICAgICAgbGV0dGVyLXNwYWNpbmc6IG5vcm1hbDsKICAgICAgICAgICAgICAgIGRpcmVjdGlvbjogcnRsOyB1bmljb2RlLWJpZGk6IGJpZGktb3ZlcnJpZGU7CiAgICAgICAgICAgICI+PHRzcGFuIHN0eWxlPSIKICAgICAgICAgICAgICAgIHVuaWNvZGUtYmlkaTogcGxhaW50ZXh0OwogICAgICAgICAgICAgICAgd3JpdGluZy1tb2RlOiBsci10YjsKICAgICAgICAgICAgICAgIGxldHRlci1zcGFjaW5nOiBub3JtYWw7CiAgICAgICAgICAgICAgICB0ZXh0LWFuY2hvcjogc3RhcnQ7CiAgICAgICAgICAgICI+QWw8L3RzcGFuPjx0c3BhbiBzdHlsZT0idW5pY29kZS1iaWRpOiBwbGFpbnRleHQ7Ij5IPHRzcGFuIGJhc2VsaW5lLXNoaWZ0PSJzdWIiIGNsYXNzPSJzdWItbTV5NHhvdzE0Y2pwaWFlYzQ3ayI+MjwvdHNwYW4+PC90c3Bhbj48L3RleHQ+PHRleHQgeD0iNDIiIHk9IjIxIiBjbGFzcz0iZGVidWciIGZpbGw9IiNmZjAwMDAiIHN0eWxlPSIKICAgICAgICAgICAgICAgIGZvbnQ6IDVweCBEcm9pZCBTYW5zLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAiPjwvdGV4dD48L2c+PC9zdmc+"/>

If $A$ is a bounded operator, i.e., if $D(A)=E$, then (iv) 《w> (v) and (vi) as $^{\prime}$ (vii). J.f A is unbounded then the stability notions may differ as we will see in the following examples.

Examples 1.2 . (a) Let $E=C_{0}$. Then $A$ : $\left(x_{n}\right)_{n \in \mathbb{N}} \rightarrow\left(-1 / n \cdot x_{n}\right)_{n \in \mathbb{N}}$ generates the semigroup $T(t)\left(x_{n}\right)=\left(e^{\left.-t / n_{x_{n}}\right)}{ }_{n} \in \mathbb{N}\right.$. It is easy to see that $\|T(t)\|=i$ and $\|T(t) f\|_{i} \rightarrow 0$ for every $f \in c_{0}$. Moreover, $A$ is a bounded operator, hence $D(A)=E$. This gives an example for a (uniformly) stable but not exponentially stable semigroup. The translation semigroups generated by the first derivative on $\mathrm{C}_{0}\left(\mathbb{R}_{t}\right)$ or $L^{P}\left(\mathbb{R}_{+}\right)$for $1<p<\infty$ give further examples for (uniformly) stable but not exponentially stable semjoroups. Moreover, as seen in $A_{i} \bar{i}$, Ex.1.l4, the foplacian $\Delta$ on $C_{o}\left(\mathbb{R}^{n}\right)$ generates a bounded holomorphic semigroup given by

$$
T(t) E(x)=(4 \pi t)^{-n / 2} \cdot \int_{R^{n}} e^{-(x-y)^{2} / 4 t} f(y) d y
$$

which cannot be exponentially stable because $0 \in \sigma(A)\left(i m A \nmid C_{0}\left(\mathbb{R}^{n}\right)\right)$, see Cor.l.5 below. By a straightforward (2-e)-argument using $(4 \pi t)^{-n / 2} \int_{R^{n}} \exp \left(-y^{2} / 4 t\right) d y=1$ one can easily show that $\|T(t) f\|+0$ for all $f \in C_{0}\left(\mathbb{R}^{n}\right)$ (see also BuIII,Ex,1.7). Therefore, the Laplacian on $C_{o}^{\left(R^{n}\right)}$ (and also on $L^{P}\left(\mathbb{R}^{n}\right)$ for $1<p<\infty$, see Ex. 1.15 below) generates a (uniformly) stable but not exponentially stable semigroup.
(b) Note that the condition $0 \leqq \omega(A)=\inf \left[\omega:\|T(t)\| \leqq M e^{\omega t}\right.$ for all $t \geq 0\}$ does not exclude that the semigroup ( $T(t)$ ) $t \geq 0$ is expou nentially stable. In fact, as shown in $A-I I I, 1.3$ the translation semigroup $(T(t)) t \geqq 0$ on $E:=C_{0}\left(\mathbb{R}_{+}\right) \cap L^{1}\left(\mathbb{R}_{+}, e^{x} d x\right)$ satisfies $\|T(t)\|$ $=1$, hence $\omega(A)=0$, and for every $\lambda \in \mathbb{C}$ with Re $\lambda>-1$ the resolvent of the generator ig given $a g$ R(h, $A) f=\int_{0}^{\infty} e^{h t} T(t) f d t$ for every $\ddagger \in E$. From the equation $A-I, 3.2$

$$
T(t) f=e^{\lambda t}\left(f-\int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f(s)\right.
$$

and the existence of $\lim _{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f$ ds it follows that $\|T(t) f\| \leqq M-e^{\lambda t}$ for every $f \in D(A)$ and some constant $M$ depending
on $f$. This yields ${ }^{\mu}(A) \leqq \sim l<0=\omega(A)$. Thus we have a semigroup which is exponentially, but not uniformly exponentially stable.
(c) Rescaling this semigroup (see Aw, 3.1) we obtain a semigroup with $-1 / 2={ }^{w}(A)$ and $1 / 2=w(A)$. Therefore there are exponentially stable and hence stable semigroups which are not bounded and hence not uniformly stable. We conclude from this example that there may be an essential difference between the long term behavior of the semigroup (T(t)) ${ }_{\text {t }} \geq 0$ (i.e. of the set of all mild solutions) and the long term behavior of the strong solutions $\{T(\cdot] f: f \in D(A)\}$ of (ACP).

In the following we characterize the exponential growth bounds $w(f)$, ${ }_{1}(A)$ and ${ }^{\omega}(A)$ by certain abscissas of simple or absolute conw vergence of the Laplace transform of $T(\cdot) f$. These characterizations will be the basic tool in showing that for certain semigroups the growth bounds $w(A)$ and/or ${ }^{11}$ (A) coincide with the spectral bound $\Sigma(\bar{B})=\sup \{\operatorname{Re\lambda }: \lambda \in \sigma(A)\}$.

We remark first that $s(A)$ can be regarded as the abscissa of holomorphy of the Laplace transform $\lambda \rightarrow \int_{0}^{\infty} e^{\lambda t} T(t) d t$ of the semigroup $(T(t))_{t \geq 0}$.
Next we recall that the Laplace transform exists for every $\lambda \in \mathbb{C}$ with Re $\lambda>\operatorname{Re} \sharp$ as soon as it exists for $k$. This follows from the equation

$$
\begin{align*}
\int_{0}^{t} e^{-\lambda s} f(s) d s= & e^{-(\lambda-\mu) t} \cdot \int_{0}^{t} e^{-\mu s} f(s) d s  \tag{1.1}\\
& +(\lambda-\mu) \int_{0}^{t} e^{-(\lambda-\mu) s} \int_{0}^{s} e^{-\mu r} f(r) d r d s
\end{align*}
$$

Note that even boundedness of $\int_{0}^{t} e^{-\mu s} f(s) d s$ implies the existence of the Laplace transform for ke $\lambda>$ Re $\mu$. Therefore the gubset of $\mathbb{C}$ for which the Laplace transform exists ig always a halfuplane $\{\lambda \in \mathbb{C}$ : $\operatorname{Re} \lambda>y\} \cup H$, where $H$ is a subset of the line $\{\lambda \in \mathbb{C}: \operatorname{Re} \lambda=\gamma\}$.

In the subsequent theorem we show that the bound of the half-plane for which the Laplace transform of $T(*) f$ (f $\in E$ ) exists absolutely and the bound of the half-plane for which the Laplace trangform of $T \|^{*}$ )Af (f $\in D(A))$ exists strongly coincide with the growth bound w(f) $=$ $\inf \left(\omega:\|T(t) f\| \leqq M e^{\omega t}\right.$ for all $\left.t \geqq 0\right\}$.

Theorem 1.3. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geqslant 0}$ on a Banach space $E$. Then, for every $f \in E$, (1.2) $\quad \omega(f)=1 i m s u_{t \rightarrow \infty} 1 / t \cdot \log \| T(t) f$,
and
(i) $\quad \omega(f)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t\right.$ exists $\}$.

If ker $A=\{0\}$, then for every $f \in D(A)$ we have
(ii) $\quad$ (f) $=\inf \left(\mathrm{Re} \lambda: \int_{0}^{\infty} e^{-h t} T(t) A f\right.$ dt exists as an improper Riemann integral\} .

Proof. The proof of (1.2) is omitted (see Hille-Philitips (1957), p.306). In order to prove (i) and (ii) we need the following lemma.

Lemma. Let $F \in C\left(\mathbb{R}^{+}, \mathbb{R}^{+}\right)$be such that $\int_{0}^{\infty} F(t)$ dt exists. If there is a positive number m and an interval [0, $n]$ such that $F(t+s) \leqq$ $m$.F(s) for all $s \geq 0$ and $t \in[0, n]$, then $\lim _{s \rightarrow \infty} F(s)=0$.

Proof of the lemma. For all $s>0$ there exists a>0 such that $A(a):=\int_{a}^{\infty} F(s) d s, \frac{n}{m} \cdot \varepsilon$. For all $t>a+n$ there exists $r \in[t-n, t]$ such that $F(r) \leq{\underset{\sim}{n}}_{1}^{1} \cdot A(a)$.
Therefore, $F(t)=F(t-r+r) \leqq m \cdot F(r) \leqq \frac{m}{n} \cdot A(a) \leqq \varepsilon$.

In order to prove (i) we define $b ;=\operatorname{inf(Re\lambda }: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\|^{\prime} d t$ exists). A straightforward application of the lemma shows that $\mu(f) \leqslant b$. The definition of $u(f)$ gives the reverse inequality. It remains to prove statement (ii) of Thm. 1.3 .
Assume that ker $A=\{0\}$ and let $f \in D(A), \lambda \in \mathbb{C}$ with $\operatorname{Re} \lambda>$ (f). From the equation

$$
\int_{0}^{t} e^{-\lambda s} T(s) \lambda f d s=e^{-\lambda t} T(t) f-f+\lambda \int_{0}^{t} e^{-\lambda s} T(s) f d s
$$

it follows that $\int_{0}^{\infty} e^{-\lambda s} T(s) A f d s$ exists,
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-05.jpg?height=64&width=1431&top_left_y=2147&top_left_x=221)

Next we show that $b<0$ implies $b \leqq m(f)$. Suppose $b<0$, Then, $b y(1,1), \int_{0}^{\infty} T(s) A f d s$ exists, By $\int_{0}^{T} T(s) A f d s=T(r) f-f$ we see that $l_{i m} r_{\rightarrow \infty} T(r) f=: g$ exists. But, for every $t \geqq 0, T(t) g=g$ and therefore $g \in \operatorname{Ker} A$ or $g=0$, Hence $\int_{t}^{\infty} T(s) A f d s=-T(t) f$. Then choosing $r, b<r<0$, and integrating by parts we obtain
$-T(t) f=\operatorname{Lim}{ }_{u \rightarrow \infty} \int_{t}^{u} e^{r s} e^{-r s} T(s) A f d s$
$=\lim u_{\rightarrow \infty}\left(e^{r u} \int_{0}^{u} e^{-r g} T(s) A f d s-e^{r t} \int_{0}^{t} e^{-r s} T(s) A f d s\right.$ $\left.-I \int_{t}^{u} e^{r s} \int_{0}^{s} e^{-r v} T(v) A f d v d s\right)$
$=-e^{r t} \int_{0}^{t} e^{-r s} T(s) A f d s-r \int_{t}^{\infty} e^{r s} \int_{0}^{s} e^{\sim r v} T(v) A f d v d s$.
From $\left\|\int_{0}^{t} e^{-r s} T(s) A f d s\right\| \leq M$ for some $M$ and every $t \geqq 0$ we con clude that $\|T(t) f\| \leqq \vec{A} e^{r t}$ for all $t \geqq 0$ and some constant $\vec{M}$.
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-06.jpg?height=52&width=1300&top_left_y=708&top_left_x=207)
If $b \geqq 0$ and $w>b$, then $\left[\int_{0}^{t} e^{-w s} T(s) A f d s \| \leqq M\right.$ for $a l l$ $t \geqslant 0$. By $T(t) f-f=\int_{0}^{t} e^{W G} e^{-w s} T(s) A f d s$

$$
=e^{w t} \int_{0}^{t} e^{-w s} T(s) \hat{A} f d s-W \int_{0}^{t} e^{w s} \int_{0}^{s} e^{-W I} T(r) A f d r d s
$$

we obtain $\|T(t) f \sim E\|\left\{M e^{w t}+M\left(e^{w t} \sim 1\right) \leqq 2 M e^{w t}\right.$. Hence w(f) $\leq w$ for every $w>b$, i.e., $\quad(f) \leqq b$.

From (1.2) and the Uniform Boundedness Principle it follows that the growth bound ${ }^{\omega}(A)=\sup (\dot{A}(f): f \in D(A)\}$ satisfies
(1.3) $w_{1}(A)=\operatorname{inf(w:for}$ every $f \in D(A)$ there exists a constant $M$ such that $\|T(t) f\| \leqq M e^{w t}$ for every $\left.t \geq 0\right\}$

$$
=1 i m \sup _{t \rightarrow \infty} 1 / t+\log \|T(t) R(\lambda, A)\| \quad(\lambda \in \rho(A))
$$

The subsequent theorem will be of particular importance in the stability theory of positive semigroups. We show that the constant ${ }^{4}$ (A) coincides with the abscissa of simple convergence of the Laplace transform of the semigroup and with the abscissa of absolute convergence of the Laplace transform of the strong solutions of (ACP).

Theorem 1.4. Let $A$ be the generator of a strongly continuous semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$. Then
(1.4) $\quad \omega_{1}(A)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t\right.$ exists as an improper Riemann integral for every $f \in E\}$

$$
=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} \text { lie }-\lambda t \mathrm{~T}(\mathrm{t}) \mathrm{fl} \mathrm{l} \mathrm{dt}\right. \text { exists for every }
$$

$$
f \in D(A)\} .
$$

Remarks. (a) One can show that the abscissas of uniform, strong and weak convergence of the Laplace transform coincide isee C-IIT, Thm. 1.2 , last part of the proof). Therefore, by Thm.1.4,

$$
\begin{align*}
& \left.{ }^{\omega}\right]_{1}(A)=\inf \left(\mathrm{ke} \lambda: \text { weakwlim} t \rightarrow \infty \quad \int_{0}^{t} e^{-\lambda s} T(s) \text { ds exists }\right\}  \tag{1.5}\\
& =\inf \left\{\operatorname{Re} \lambda: \text { uniform-1im}{ }_{t \rightarrow \infty} \int_{0}^{t} e^{-\lambda s} T(s)\right. \text { ds exists\}. }
\end{align*}
$$

(b) In the equations (1.4) and (1.5) the term "Re $\lambda$ " may be replaced by ${ }^{n \lambda} \in \mathbb{R}^{\prime \prime}$ (use (1.1)).

Proof of Thm.l.4. The equality ${ }^{\omega} l^{(A)}=\operatorname{inf(Re} \lambda=\int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t$ exists for all $f \in D(A)\}$ follows from the definition of ${ }_{\mathrm{H}}(\mathrm{A})$ and the lemma used in the proof of Thm. 1,3 .
We prove $\omega_{1}(A)=\operatorname{inf(Re} \lambda: \int_{0}^{\infty} e^{-\lambda s_{T}}(s) f d s$ exists for every $\left.f \in E\right\}$. The identity

$$
T(t) f=e^{\lambda t}\left(f-\int_{0}^{t} e^{-\lambda s} T(s)(\lambda-A) f d s\right)
$$

yields
${ }^{\mu} l^{(A)} \leqq \inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t\right.$ exists for every f $f$ im $\left.(\lambda-\lambda)\right\}$. Therefore
${ }_{\omega}(A) \leqq \inf \left\{\right.$ Re $\lambda: \int_{0}^{\infty} e^{-\lambda t} T(t) f d t$ exists for every $\left.f \in E\right\}=: b$. Take $\lambda \in \mathbb{C}$ with Re $\lambda>{ }^{\prime}{ }_{1}(A)$. Then $\int_{0}^{\infty} e^{-\lambda t} T(t) f$ dt exists for every $f \in D(A)$. Define $g:=\int_{0}^{1} e^{-\lambda t} T(t) f d t$. Then $g \in D(A)$ and $\int_{0}^{n} e^{-\lambda t} T(t) f d t=\sum_{k=0}^{n-1} e^{-\lambda k} T(k) g$. Since $\operatorname{Re} \lambda>\omega_{1}(A)$ it follows that the sum converges for every $g \in D(A)$. Therefore the integral converges as $n \rightarrow \infty \quad\left(n \in N\right.$ for every $f \in E$. For every $t \in \mathbb{R}_{+}$ define a bounded operator $T_{t}$ by $f * \int_{0}^{t} e^{-h s} T(s) f d s$. As seen above, $T_{n}{ }^{f}$ converges as $n \rightarrow m(n \in N i$ for every $f \in E$. It follows from the Uniform Boundedness Principle that the family ( $\mathrm{T}_{\mathrm{n}}$ ) $\mathrm{n} \in \mathrm{d}$ is uniformly bounded.
For every $t \in \mathbb{R}+$ there exist $n \in \mathbb{N}$ and $t^{\prime} \in[0,1)$ such that $T_{t}=T_{t}+e^{-\lambda t^{\prime}} T^{\prime}\left(t^{\prime}\right) T_{n}$. Since the operator families on the right side of the equation are uniformly bounded the same is true for $\left(T_{t}\right)_{t a 0}$. Since ( $\left.T_{t}{ }^{f}\right){ }_{t} \geqslant 0$ converges for every $f \in D(A)$ it follows that $\left(T_{t}{ }^{f}\right) t \geqq 0$ converges for every $f \in E$. Thus $b \leqslant w^{(A)}$.

The inequality
$\mathbb{M}(A) \geqq \inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t\right.$ exists for every $\left.f \in E\right\}$ in combination with the lemma of Thm.l. 3 implies that the growth bound w(A) coincides with the abscissa of absolute convergence of the Laplace transform of $(T(t))_{t \geq 0}$; i.e..
$(1,6) \quad \mu(A)=\inf \left\{\operatorname{Re} \lambda: \int_{0}^{\infty}\left\|_{0} e^{-\lambda t} T(t) f\right\| d t\right.$ existsfor every $\left.f \in E\right\}$.
$A s$ seen in A-I, Prop.1.11, if $\quad \int_{0}^{\infty} e^{-\lambda t} T(t) f$ dt exists for every $f \in E$, then $\lambda \in f(A)$ and $R(h, A) f=\int_{0}^{\infty} e^{-\lambda t} T(t) f d t$. This and Thm.l. 4 yield the following corollary.

Corollary $1.5 . \quad$ Let $\boldsymbol{R}^{\prime}$ be the generator of a strongly continuous semigroup (T(t)) $\quad(\xi 0$ on a Banach space E Then

$$
s(A) \leftrightarrows \omega^{\circ}(A) \leftrightarrows
$$

Example 1.2.(2) shows that the uniform exponential stability of the
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-08.jpg?height=49&width=1611&top_left_y=638&top_left_x=214) following example we will see that not only the semigroup ii.e.r all generalized solutions of (ACP)), but also the strong solutiong can be ungtable even when $g(A)<0$. In fact, we will give an example of a semigroup with $s(A)<\omega_{1}(A)<\Leftrightarrow\left(A_{1}\right)$.

Example $1.6, ~ 5 n A-I I I, E x .1 .4$ it was shown that the semigroup (T(t)) $t \leq 0$ on the Hilbert space $E=\left\{1 x^{1}, x^{2}, \ldots, x^{n} \in \mathbb{E}^{n}: \sum_{i=1}^{\infty}\left\|x^{i}\right\| \in \infty\right\}$ given by $T(t):=\left(e^{2 \pi i n t} \exp \left(\tan _{n}\right)\right)_{n \in \mathbb{N}}$ with

$$
A_{n}=\left\{\begin{array}{ccccc}
0 & 1 & 0 & \ldots & 0 \\
\cdot & . & & & 0 \\
\cdots & & \cdots & & 0 \\
\cdots & & & . & 1
\end{array}\right]_{n \times n}
$$

has growth $e^{t}\left(\|T(t)\|=e^{t}\right)$. Thus $\quad\left(\mathcal{R}_{2}\right)=1$ whereas the generator $A:\left(2 \pi i n+\beta_{n}\right){ }_{n} \in \mathbb{N}$ has spectral bound 0 . We will show first that for this semigroup $\psi_{1}(A)=$ (A) holds (we will uge thig to construct a
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-08.jpg?height=61&width=852&top_left_y=1663&top_left_x=214)
Let $e_{n}=n^{-1 / 2},(1, \ldots, 1) \in c^{n}$, Then we have
$\left\|\exp \left(\tan _{n}\right) \cdot e_{n}\right\|^{2}=$

$$
=\frac{1}{n} \cdot\left\|\left(1+t+\ldots+\frac{t^{n-1}}{(n-1)!}, 1+t+\ldots+\frac{t^{n-2}}{(n-2)!} \ldots, 1+t, 1\right)\right\|^{2}=
$$

$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1}\left(\sum_{j=0}^{r} \frac{1}{j!} \cdot t^{j}\right)^{2}=
$$

$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1}\left(\sum_{j, s, 0}^{I}, \frac{1}{j!s+} \cdot t^{j+s}\right)=
$$

$$
=\frac{1}{n} \cdot \sum_{\mathrm{r}=0}^{\mathrm{n}-1} \sum_{i=0}^{2 r} t^{i} \sum_{j+s=i} \frac{1}{j!5!}=
$$

$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1} \sum_{i=0}^{2 r} \frac{t^{i}}{i!} \sum_{j=0}^{i}\binom{i}{j}=
$$

$$
=\frac{1}{n} \cdot \sum_{r=0}^{n-1} \sum_{i=0}^{2 r} \frac{1}{i!}(2 t)^{i}
$$

$$
\equiv \frac{1}{\Omega^{2}} \cdot \sum_{j=0}^{n+1} \frac{1}{i!}(2 t)^{i}
$$

For $0<G<1$ we consider $x_{G} \in$ fit defined as follows

$$
x_{q}:=\left(q * e_{1}, 2 q^{2} e_{2}, \ldots+q^{n} e_{n}, \ldots\right)
$$

Then $X_{q} \in D(A)$ and

$$
\begin{aligned}
\left\|T(t) x_{q}\right\|^{2} & =\sum_{n=1}^{\infty} n^{2} q^{2 n}\left\|\exp \left(t A_{n}\right) e_{n}\right\|^{2} \geqq \\
& \geqq \sum_{n=1}^{\infty} n^{2} q^{2 n}\left(\frac{1}{n^{2}} \cdot \sum_{i=0}^{n=1} \frac{1}{i!}(2 t)^{i}\right) \\
& =\sum_{i=0}^{\infty} \sum_{n=i+1}^{\infty}\left(q^{2 n} \cdot \frac{1}{i!}(2 t)^{i}\right) \\
& =\sum_{i=0}^{\infty} q^{2 i+2} \cdot\left(1-q^{2}\right)^{-1} \cdot \frac{1}{i!}(2 t)^{i}= \\
& =\frac{q^{2}}{1-q^{2}} \cdot \sum_{i=0}^{\infty} \frac{1}{i!}\left(2 t q^{2}\right)^{i}=\frac{q^{2}}{1-q^{2}} \cdot e^{2 t q^{2}} .
\end{aligned}
$$

It follows that $\left(x_{q}\right) \geqq q^{2}$. Thus

$$
1=\sup \left\{\omega\left(x_{q}\right): 0<q<1\right\} \leqq \omega_{1}(A) \leq \mu(A)=1 .
$$

Rescaling the semigroup (i.e. looking at $e^{-3 / 2 \cdot t} T(t)$ ) we obtain a semigroup generator $\vec{A}$ on the Hilbert space $E$ with $-3 / 2=5(\bar{A})$ and $\omega_{1}(A)=\omega(A)=-1 / 2$. On the other hand, Example 1.2. (2) yields a semigroup on a Banach space $F$ with generator $B$ such that $-1=s(B)=\omega_{1}(B)$ while $\omega(B)=0$. Now the operator $C:=A \oplus B$ on the Banach space $E \Phi F$ is a semigroup generator for which
$s(C)=\max \{s(A), s(B)\}=-1,{ }^{\omega} 1(C)=\max \left\{\omega_{1}(A){ }_{f} \omega_{1}(B)\right\}=-1 / 2$ and
$\omega(C)=\max \{\omega(A), \omega(B)\}=0$.
(1.7) Important remark: For eventually nom continuous semigroups, in particular for compact, differentiable, holomorphic or nilpotent semigroups the spectral mapping theorem o(T(t)) $\{0\}=\mathrm{e}^{\mathrm{to}(\mathrm{A})}$ holds, and therefore

$$
\begin{equation*}
\Sigma(A)=\omega_{1}(\bar{A})=\omega(A) \tag{1,8}
\end{equation*}
$$

is valid (Cor.1.5 and AmIII, Cor.6.7).
Hence, if $A$ is the generator of an eventually norm continuous semigroup, then the exponential growth bounds of the strong and the mild solutions of $\dot{u}(t)=A u(t)$ are determined by the spectral bound $s(A)=\sup \{\operatorname{Re} \lambda: \lambda \in o(A)\}$.

In general, the growth bound w(A) can be obtained through the Hille-Yosida theorem (see $\mathrm{A}-\mathrm{II}, \mathrm{Thm}, 1,7$ ) as
(1.9) $\quad \omega(A)=\inf \left\{w:\left\|R(\lambda, A)^{n}\right\| \leq M \cdot(\operatorname{Re} \lambda-w)^{-n}\right.$ for some $M$ and every $n \in A$ and $\lambda \in \mathbb{C}$ with $k e \lambda>w)$.

In view of the difficulties in estimating all powers of the resolvent this equation is of little practical interest. If $A$ is the generator
of a semigroup on a Hilbert space $H$, then it is shown in $\bar{A} w I I$, Cor.7.ll that
(1.10) $\quad 山(A)=\inf \left(w:\|R(\lambda, A)\|_{i} \leq M_{W}\right.$ for Re $\left.\lambda>w\right\}$.

Unfortunately, the identity (1.10) does not hold on arbitrary Banach spaces, but we will see in section 1 of $C=I v$ that for every positive semigroup on a Banach lattice the identity
(1.11) $s(A)={ }_{\omega} 1(A)=\inf \left\{w:\|R(\lambda, A)\| \leq M_{w}\right.$ for $\left.\operatorname{Re} \lambda>w\right\}$
is valid. Therefore, for positive semigroups with $s(A)={ }_{\omega}(A)<(A)$ (see Ex.1.2.(2)) the equation (1.10) is not true. However, we can prove the following theorem.

Theorem 1.9. Let $A$ be the generator of a strongly continuous semiw group ( $T(t))_{t \geq 0}$ on a Banach space $E$. If there are constants $a \geqq 0$ and $q \geqslant s(A)$ and if there are $C \in \mathbb{H}_{+}, n \in \mathbb{N}$ such that, for every $\lambda \in \mathbb{C}$ with $\operatorname{Re} \lambda>g$ and $\left|I_{m} \lambda\right|>a$ we have $\|R(\lambda, A)\| \leqq C|\lambda|^{n-2}$, then $\sup \left\{u(f), f \in D\left(A^{n}\right)\right\} \geqq G$.

Proof. The hypothesis $\|R(\lambda, A)\| \leqq C|\lambda|^{n-2}$ is invariant under rescaling; i.e., the resolvent $R(\lambda,-b+A)$ of the generator $-b+A$ of the rescaled semigroup $e^{-b t} T(t)$ satisfies $\|R(\lambda,-b+A)\| \cong \tilde{C}|\lambda|^{n-2}$ for every $\lambda \in \mathbb{C}$ with Re $\lambda>q m b$ and $\mid$ Im $\lambda \mid>a+2 b$ and a suitable constant $\bar{C}$. Therefore we may assume that $b:=\max (\omega(A), q)<0$, Let $\omega(A)<p<0$. Then, by the inversion formula for the Laplace transform for every $f \in D(A)$ and $p^{\prime}=\max \{p, q\}<0$,

$$
\begin{equation*}
T(t) f=\frac{1}{2 \pi i} \cdot \int_{P^{\prime} \sim i \infty}^{P^{\prime}+i \infty} e^{\lambda t} R(\lambda, \bar{A}) f d \lambda . \tag{1.12}
\end{equation*}
$$

(For a proof of the vector valued version of the inverrion formula one may follow [widder (1946), p. 66?; also see the notes to this section.)
By the resolvent equation we obtain

$$
R(\lambda, A) R(0, A)^{n}=\sum_{k=1}^{n}(-1)^{k+1} \cdot \lambda^{-k} R(0, A)^{n+1-k}+(-1)^{n} \cdot \lambda^{-n} R(\lambda, A) .
$$

Using that $\frac{1}{2 \pi i^{\prime}} \cdot \int_{\mathrm{P}^{\prime}-\mathrm{im}}^{\mathrm{P}^{\prime}+\mathrm{im}} \mathrm{e}^{\lambda t} \cdot \lambda^{-k} \mathrm{~d}_{\lambda}=0$ for $\mathrm{k} \geqq 1, \mathrm{p}^{\prime}<0$ and $\mathrm{t}>0$ we obtain
(1.13) $T(t) R(0, A)^{n_{f}}=(\sim 1)^{n} \cdot \frac{1}{2 \pi i} \cdot \int_{P^{\prime}-i=1 \infty}^{P^{\prime}+i=} e^{\lambda t} \cdot \lambda^{-n} R(\lambda, A) f(\lambda$
for every $f \in E$ and $t>0$.
If $G \in P^{\prime}$, then, by Cauchy's Integral Theorem and since $\|R(\lambda, A)\|$ $c \cdot|\lambda|^{n-2}$ we see that the path of integration can be shifted to Reג = q ;
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-10.jpg?height=86&width=1338&top_left_y=2567&top_left_x=219)

Therefore $\left\|T(t) R(0, A)^{n} f\right\| \leqq c^{\prime} e^{q t}\|f\| \int_{-m}^{m}\left(q^{2}+s^{2}\right)^{-l} d s=M^{2} e^{q t} \cdot\|f\|^{\prime}$ or $\|T(t) f\| \leqq M \cdot e^{q t}\left\|_{R^{n}} f\right\|$ for $f \in D\left(A^{n}\right)$.

In view of the characterizations given in section 1 of $A-I I$, the semigroups occuring in the theorem are holomorphic if $n=1$. In this case one may apply (1.7) to obtain the stronger statement (1.8).

Instead of making assumptions on the resolvent of $A$ we now take a different view and characterize the property ${ }^{n} \omega(A)<0 "$ in terms of the semigroup $(T(t))_{t \geqslant 0}$ directly.

Proposition 1.10 . Let $A$ be the generator of the strongly continuous semigroup ( $T(t))_{t \geqq 0}$. Then the following statements are equivalent:
(a) $\omega(A)<0$
(b) $\quad \lim _{t \rightarrow \infty}\left\|_{i} T(t)\right\|=0$
(c) $\left\|T\left(t^{\prime}\right)\right\|<1$ for some $t^{\prime}>0$.

Proof. The only nontrivial implication (c) $\rightarrow(a)$ follows from
$\omega(A)=\lim _{t+\infty} \frac{1}{t} \log \|T(t)\| \quad(\operatorname{see} A-I,(1.1))$ and $\frac{\log \|T(t)\|}{t} \leqslant \frac{\log \left\|T\left(t^{*}\right)\right\|^{i}}{t^{\prime}}+\frac{\log \|T(t)\|_{i}}{n t^{t}+s}$ for $t=n t^{\prime}+s, s \in\left[0, t^{\prime}\right)$.

Other less obvious characterizations of the property "w( A$)<0$ " are given in the next theorem. The equivalence of (a) and (c) is known as Datko's Theorem.

Theorem 1.11 . Let $A$ be the generator of a strongly continuous semigroup ( $T(t)$ ) $t \geqq 0$ on a Banach space $E$. Then the following statements are equivalent:
(a) $\quad \infty(A)<0$.
(b) $s(A)<0$ and there is $t_{0}>0$ such that

$$
|\lambda|<1 \text { for every } \lambda \in \operatorname{Ao}\left(T\left(t_{0}\right)\right)
$$

(c) For every (some) psl exists $\int_{0}^{\infty}\|T(t) f\|^{P} d t$ for every $f \in E$.

Proof. The implication ${ }^{\prime \prime}(a) \rightarrow(b)$ follows from $r(T(t))=e^{a(A) t} \varepsilon I$ and $s(A) \leqq w(A)<0$. For the point and residual spectrum the spectral mapping theorem is valid (see $A-I I I, T h m .6 .3$ ). The approximate point spectrum is closed, hence the additional information in (ii)
implies $|\lambda| \leq r<1$ for some $r$ and each $\left.\lambda \in \operatorname{Aof}\left(t_{o}\right)\right)$ - Conseu quently, $\exp \left(\omega(A) \cdot t_{0}=I\left(T\left(t_{O}\right)\right) \leqq \max \left(\exp \left(t_{0} \cdot s(A)\right), r\right)\right\} \ll \quad$ or $\omega(A)<0$. This proves $"(b) \rightarrow(a) "$. For a proof of the equivalence of (a) and (c) we refer to Datko (1972) or Pazy (1983), Thm.4.4.1.

Rescaling a given semigroup (T(t)) $t \geq 0$ one obtains the following corollary from (1.1) and statement (c) of the above theorem.

Corollary 1.12 . Let $(T(t)) t \geq 0$ be a strongly continuous semigroup on a Banach space $E$. Then the set of complex numbers $\lambda$ for which $\int_{0}^{\infty}\left\|e^{-\lambda t} T(t) f\right\| d t$ exists for every $f \in E$ is an open right halfplane.

In the next theorem we give two necessary conditions for stability of (T(t)) $t \geq 0$ in terms of the generator $A$. We will see in Chapter $C-I V$ that for positive semigroups a condition similar to statement (ii) below is even sufficient for stability of the semigroup. We emphasize that stable semigroups need not be uniformly bounded (see Ex. $1.2(3)$ ) and that $s(A)=\omega(A)=0$ does not imply boundedness or even stabil~ ity of the semigroup (see also $A-I$, Ex.1.4.(i)).

Theorem 1.13. Let $A$ be the generator of a stable semigroup (T(t)) $t \supseteq 0$ on a Banach space $E$. Then the following asgertions hold:
(i) $\quad g(A) \equiv 0$ and $\operatorname{Re} \lambda \in 0$ for every $\lambda \in \operatorname{Po}(A) \cup R o(A)$.
(ii) $\lim _{\lambda \rightarrow 0+} h_{R}(\lambda, A) f$ exists for every $f \in D(A)$.

Proof. (i) If (T(t)) $t \geqslant 0$ is stable, then $\|T(t) f\| \leqq M_{f}$ Eor every $\mathrm{f} \in \mathrm{D}(\mathrm{A})$. Therefore $\mathrm{s}(\mathrm{A}) \subseteq \omega_{1}(\mathrm{~A}) \leqq 0$.
Assume there is $\lambda \in \operatorname{Po}(A)$ with Re $\lambda=0$. Then by $A w I I, C o r .6 .4$ there is $g \neq 0$ such that $T(t) g=e^{h t} g$ for all $t$ a . Since $\left|e^{\lambda t}\right|=1$ this contradicts the stability of the semigroup. Assume there is $\lambda \in \operatorname{Ro}(A)=P \sigma\left(A^{\prime}\right)$ with Re $\lambda=0$. Then there is $0 \neq \Phi \in E^{\prime}$ with $T(t)^{*} \Phi=\exp (\lambda t) \cdot \Phi$ for all $t \geqq 0$. Choose $f \in D(\bar{A})$ such that $\langle f, \phi\rangle \neq 0$. Then $|\langle T(t) f, \Phi\rangle|=|\langle f, \Phi\rangle|>0$ for every $t \geqq 0$ which contradicts the stability of the semigroup.
(ii) From the stability of the semigroup and the identity
$\int_{0}^{t} T(s) A f d s=T(t) f-f$ we see that $\int_{0}^{\infty} T(s) A f$ ds exists for every $f \in D(A)$. But ${ }^{\mu} 1(A) \leqq 0$ and hence $R(\lambda, A) A f=\int_{0}^{\infty} e^{-\lambda s} T(s) A f d s$ for every $\lambda>0$ (see Thm.1.4). By a classical theorem of Laplace transform theory (for a proof of the vector valued version one may
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-13.jpg?height=67&width=1620&top_left_y=275&top_left_x=224) and is equal to $\int_{0}^{m} T(s) A f d a$. The identity $R(\lambda, A) A f=\lambda R(h, A) f-f$ yields the existence of $1 \mathrm{im}_{\lambda \rightarrow 0+} \lambda \mathrm{R}(\lambda, A) \mathrm{f}$ for every $\mathrm{f} \in \mathrm{D}(\mathrm{A})$.

Bounded holomorphic semigroups (see AwI, Def.l.ll) satisfy $\| A T(t) \mid E m \cdot t^{-1}$ [Goldstein (1985a), p.33], hence $T(t) f \rightarrow 0$ as $t \rightarrow \infty$ whenever $£ \in$ im $A$. If im $A$ is dense (i.e., 0 ( $R_{g}(A)$ ) we obtain uniform atability and the following corollary.

Corollary 1.14. Let $A$ be the generator of a bounded holomorphic semigroup $(T(t)) t \geqslant 0$ on a Banach space $E$. Then the following statements are equivalent.
(a) $0 \leqslant P_{\sigma}(\bar{A}) \cup R_{\sigma}(A)$.
(b) $(T(t))_{t \geq 0}$ is uniformly stable.

Example 1.15 The Laplacian $A$ generates a bounded holomorphic semi* groups on $L^{\mathrm{P}}\left(\mathbb{R}^{n}\right)$ for $\pm \leq p<\infty$ (see the example proceeding Cor.l. 13 of Chap. $A-I I)$. All solutions of $\Delta f=0$ are either constant or unbounded, therefore $0 \underset{f}{f} \quad \mathrm{O}(\Delta)$. If $1<p<\infty$, then the adjoint of the Laplacian on $L^{P}\left(\mathbb{R}^{n}\right)$ is the Laplacian on $L^{q}\left(\mathbb{R}^{n}\right)$ where $\frac{1}{\mathrm{p}}+\frac{1}{\mathrm{q}}=1$. Therefore $0 \not \equiv \operatorname{Ro}(\Delta) \cup \operatorname{Po}\left(\Delta^{\prime}\right)$ and we obtain by Cor.1.14 that $\Delta$ generates uniformly atable semigroups on the space $L^{P}\left(\mathbb{R}^{n}\right)$ for $1<p<\infty$ which are, by ims $\neq L^{P}\left(\mathbb{R}^{n}\right)$ and cor.l.5, not exponenw tially stable.

As seen in Thm. 1.4, exponential stability can be defined by saying that the abscissa of convergence of the Laplace transform of (T (t)) $t \geqq 0$ is less than zero. This should be compared to the assertion of our final theorem.

Theorem l. L6. Let $A$ be the generator of a strongly continuous semigroup (T(t)) te0 on a Banach space $E$. The following assertions are equivalent:
(a) (T(t)) $t \geq 0$ is stable.
(b) ker $A=\{0\}$ and $\int_{0}^{\infty} T(t) \neq d t$ exists for allfimin.

Furthermore the following statements are equivalent:
(a') (T(t)) $t \geqslant 0$ is stable and bounded.
(b') (T(t)) $t \geq 0$ is uniformly stable.
(c') (T(t)) $t$ ( ${ }^{\prime} 0$ is bounded and there is a dense subspace $D$ such that $\quad \int_{0}^{\infty} T(t) f d t$ exists for every $f \in D$.
![](https://cdn.mathpix.com/cropped/2025_01_15_1ca88247a1734ca9eee6g-14.jpg?height=79&width=1615&top_left_y=563&top_left_x=209) $\int_{0}^{t} T(s) A f d s=T(t) f-f, \quad-f$ as $t \rightarrow$. . Therefore (al implies (b). On the other hand, if $\int_{0}^{t} T(s) h f d s$ converges as $t * \infty$, then, by the equation above, $g:=1 i m l_{t \rightarrow \infty} T(t) f$ exists. But ker $A=\{0\}$ and therefore $g=0$. This proves " $(b) \rightarrow(a)^{\prime \prime}$.
The implication " $\left(a^{\prime}\right) \rightarrow\left(b^{\prime}\right) "$ is obvious. If $T(t) f \rightarrow 0$ for every $f \in E$, then $\|T(t)\| \leq M$ and $0 \notin \operatorname{Ro}(A) \quad$ (Thm.1.12). Therefore $D:=\operatorname{im} A$ is dense and $\int_{0}^{\infty} T(t) f d t$ exists for every $f \in D$. This proves " (b') $\rightarrow\left(c^{\prime}\right)^{\prime \prime}$. We have to show that (c') implies (a'). Define $G:=\left\{h \in E: h=\int_{0}^{\infty} T(t) g d t\right.$ for some $\left.g \in D\right\}$. We will show that $G$ is dense in $E$. First we notice that $g \sim T(s) g \in D$ when ever $g \in D$ and $s \in \mathbb{R}_{+}$.
Define $h_{s}=\frac{1}{s} \cdot \int_{0}^{\infty} T(t)(g-T(s) g) d t=\frac{1}{s} \cdot \int_{O}^{s} T(t) g$ dt. Then $h_{s} \in G$ and $h_{s}+g$ as $s * 0$. Therefore $D \subset \bar{G}$ or $\bar{G}=E$. Now let $h \in G$. Then $T(t) h=T(t) \int_{0}^{\infty} T(s) g d s=\int_{t}^{\infty} T(s) g d s \rightarrow 0$ as $t \rightarrow \infty$. But $\|T(t)\| \in M$ and therefore $T(t) f * 0$ for every $f \in E$.

Remarks 1.17. (a) If $B$ is the generator of a stable semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$, then, by the previous theorem, im $A=\left\{f \in E: \int_{0}^{\infty} T(t) f\right.$ dt exists $\}=H$.
If $g \in H$, then $\int_{0}^{\infty} T(t) g d t \in D(A)$ and $A \int_{0}^{\infty} T(t) g d t=-g$. Therew fore $g \in i m h$ and we obtain that the dense subspace im $A$ is given by
(1.14) $\quad$ im $A=\left\{f \in E: \int_{0}^{\infty} T(t) f d t\right.$ exists $\}$
in case that $A$ is the generator of a stable semigroup ( $T(t)$ ) $t \geqq 0$.
(b) If $u(f)<0$ for every $f \in D(A)$, then (T(t)) is stable (but might not be exponentially stable if
$0=H_{1}(A)=\sup (u(f): f \in D(A)\}$. In this case it can be seen by a proof similar to the one of Thm. 1.4, that o(A) has to be contained in the open left half-plane; i.e. Fe $\lambda<0$ for $\lambda \in \sigma(A)$.
(c) If one defines a semigroup (T(t)) tap to be weakly stable if $<T(t) f, \Phi>0$ as $t \rightarrow \infty$ for every $f \in D(A)$ and $\Phi \in E \prime$ or as weakly uniformly stable if $\langle T(t) f, \Phi\rangle \rightarrow 0$ as $t * \infty$ for every $f \in E$ and $\phi \in E$, then Theorem 1.13 and 1.16 can be reformulated in a
weak form (i.e.; we replace stable by weakly stable and 'lim' by 'weak-lim'). The proofs require only some obvious modifications.
If $A$ has a compact resolvent or $i$ : $A$ is the generator of a bounded holomorphic semigroup, then weak stability implies stability. In general, this is no longer true; e.g., the translation semigroup on $L^{2}(\mathbb{R})$ is weakly uniformly stable but not stable (see also BuTV,Ex.1.2).

## 2. STABIJITY: INHOMOGENEOUS CASE

Wring the results of the first section, we now investigate the long term behavior of the solutions of the inhomogeneous initial value problem

$$
\begin{equation*}
\dot{u}(t) \Rightarrow A u(t)+F(t) \quad, \quad u(0)=f \tag{2.1}
\end{equation*}
$$

where $A$ is the generator of a strongly continuous semigroup on a Banach space $E$ and $F(\cdot)$ is a locally integrable function from $\mathbb{R}+$ into $E$ called forcing_term. A function $u(*)$ is called a (strong) solution of (2.1) if $u\left({ }^{\circ}\right): \mathbb{R}_{+}+D(A), u\left({ }^{*}\right) \in C^{1}\left(R_{+}, E\right)$ and (2.1) is satisfied for $t \geqslant 0$,
The assumption that $A$ is the generator of a semigroup (T(t)) $t \geqq 0$ yields the uniqueness of the solution of (2.1). If u(.) is a solution of (2.1), then the function $v(s):=T(t-s) u(s), 0 \leqq s \leqq t$, is differentiable and $V^{*}(s)=T(t-s) F(s)$. But $F(*)$ is locally integrable, and by $\int_{0}^{t} T(t-s) F(s) d s=v(t)-v(0)=u(t)-T(t) f$ we see that the solution $u(t)$ of (2.1) is given by

$$
\begin{equation*}
u(t)=T(t) f+\int_{0}^{t} T(t-s) F(s) d s \tag{2.2}
\end{equation*}
$$

Example. Let $(T(t)) t \geqq 0$ be not eventually differentiable. Then there exists $g \in E$ such that $t \rightarrow T(t) g$ is not differentiable on ( $0, \infty$ ). The initial value problem $u(t)=A u(t)+T(t) g, u(0)=0$ has no (strong) solution $u(\cdot)$ because otherwise

$$
u(t)=\int_{0}^{t} T(t-s) T(s) g d s=t T(t) g
$$

has to be differentiable on $\mathbb{R}_{+}$.
Whenever the expression (2.2) makes sense we call it a generalized (or mild) solution of (2.1). If $F(*)$ is continuous and $f \in D(A)$, then the generalized solution of (2.1) is a strong solution if and only if $v(t): \int_{0}^{t} T(t-s) F(s) d s$ is differentiable (see Pazy (1983) Chap. 4 ,

Thm, 2.4). There are several sufficient conditions on the generator $A$, the forcing term $F(\cdot)$ or the space $E$ such that everymild solution is a strong solution of (2.1) (see Travis (1979) or Pazy (1983) Sec.4.2).

It is our aim in this section to study the asymptotic behavior of the solutions of (2.1) as $t \rightarrow$. To that purpose we consider absolutely integrable or periodic forcing terms $F(*)$, and assume the semigroup to be uniformly stable.

Similar results for integrable and convergent forcing terms $F(\cdot)$ can be obtained if the semigroup is supposed to be uniformly exponentially stable (see Pazy (1983), p.119 or Neubrander (1985b)). However, if the semigroup is positive, these results even hold for stable semigroups (see Section C-IV). From Theorem 1.13.(i) we recall that for stable semigroups im A is dense in $E$.

Theorem 2, 1. Let $A$ be the generator of a uniformly stable semigroup $(T(t))_{t \geq 0}$ on a Banach space $E$. If there is $g \in i m \mathcal{B}^{\prime}$ such that $\int_{0}^{m}\|F(s)-g\|_{i}^{d s}$ exists, then every generalized solution $u(\cdot)$ of (2,1) converges as $t \rightarrow \infty$ and $\lim _{t \rightarrow \infty} u(t)=$ h where $h \in D(A)$ with $A_{h}=g$.

Proof. If $u(\cdot)$ is a generalized solution of (2,1), then, by (2.2), $u(t)=T(t) f+\int_{0}^{t} T(s) g d s+\int_{0}^{t} T(t-s)(F(s)-g) d s$. By the uniform stability and Thm.l.l4 we see that the first term converges to zero and that the second one converges to h . We have to show that the third term oonverges to zero. Take $g>0$ and $G(s):=F(s)-g$. Then

$$
\begin{aligned}
\left\|\int_{0}^{t} T(t-s) G(s) d s\right\| & \leqq\left\|\int_{0}^{t^{\prime}} T\left(t-t^{\prime}+t^{\prime}-s\right) G(s) d s\right\|+\left\|\int_{t^{\prime}}^{t} T(t-s) G(s) d s\right\| \\
& \leqq\left\|^{\prime} T\left(t-t^{\prime}\right) \int_{0}^{t^{\prime}} T\left(t^{\prime}-s\right) G(s) d s\right\|+M \int_{t^{\prime}}^{*}\|C(s)\| d s .
\end{aligned}
$$

Since the semigroup is uniformly stable we obtain
$T\left(t \sim t^{\prime}\right) \int_{0}^{t^{\prime}} T\left(t^{\prime}-s\right) G(s) d s \quad 0 \quad a s \quad t * 0$ for every $t^{\prime} \geqq 0$. Therefore $\left\|\int_{0}^{t} T(t-s) G(s) d s\right\|_{i} \leqslant E$ for all sufficiently large $t$.

In the subsequent theorem we see that if $A$ is the generator of a uniformly stable semigroup, if the forcing term $F(\cdot)$ is puperiodic and if $\int_{0}^{P} T(p-s) F(s) d s \quad \in \quad i m(I d-T(p))$ (notice that, by Thm.1.13. (i) and A-III, Lemma 5.3, $\overline{\text { im (Id }-T(P))}=E$ ), then (2.1) admits a unique p-periodic, asymptotically stable mild solution.

Lemma 2.2. Let $A$ be the generator of a strongly continuous semigroup (T(t)) $t \geq 0$ on a Banach space $E$ and let $F(\cdot)$ be a p-peri* odic, locally integrable function, $p>0$. Then the following statements are equivalent;
(a) $\dot{u}(t)=\bar{R} u(t)+F(t)$ admits a (unique) generalized p-periodic solution.
(b) There exists a (unique) $f \in E$ such that (Id $-T(p)) f=$ $\int_{o}^{P} T(p-s) F(s) d s$.

Proof. " (a) $\rightarrow(b) "$ Let $f:=u(0)$ be the initial value for which (2.1) has the p-periodic solution. Then we have

$$
\begin{aligned}
u(t)=u(t+p) & =T(t) T(p) f+\int_{0}^{P} T(t+p-s) F(s) d s+\int_{p}^{t+p} T(t+p-s) F(s) d s \\
& =T(t)\left[T(p) f+\int_{0}^{P} T(p-s) F(s) d s\right]+\int_{0}^{t} T(t-s) F(s) d s
\end{aligned}
$$

for every $t \geqq 0$. Therefore $f=u(0)=T(p) f+\int_{0}^{p} T(p-s) F(s) d s$. clearly, if u(.) is a unique periodic solution with u(0) $=\mathrm{E}$, then $f$ is the unique element for which $f=T(p) f+\int_{0}^{P} T(p-s) F(s) d s$ holds.
" (b) $\rightarrow$ (a)". Define u(.) as in (2.2). Then
$u(t+p)=T(t)\left[T(p) E+\int_{0}^{P} T(p-s) F(s) d s\right]+\int_{0}^{t} T(t-s) F(s) d s=u(t)$.

If $f$ is unique, then, by the considerations above, the solution is unique.

Remark 2.3. Let $A$ be the generator of a strongly continuous semigroup ( $T(t)$ ) $t \geqslant 0$ for which the spectral mapping theorem (see $A m I I$, Sec. 6 ) is valid and let $F$ be a puperiodic forcing term. If $\frac{2 \pi i n}{P} \in \rho(A)$ for every $n \in Z$, then, by Lemma 2.2,
$\dot{u}(t)=A u(t)+F(t)$ has a unique puperiodic solution with initial value $(I d-T(p))^{-l}\left(\int_{0}^{P} T(p-s) F(s) d s\right)$.

As a consequence of Thm. 1.13 and $A \sim I I I, C o r .6 .4$, for a uniformly stable semigroup there exists at most one $f \in E$ such that $(I d-T(p)) f=\int_{0}^{p} T(p-s) F(s) d s$. This and Lemma 2.2 is used to prove the following theorem.

Theorem 2.4. Let $A$ be the generator of a uniformly stable semigroup $(T(t))_{t \geqslant 0}$ and let $F(\cdot)$ be a puperiodic locally integrable function such that $(I d-T(p)) f=\int_{o}^{P} T(p-s) F(s) d s$ for some $f \in E$. Then the
unique p-periodic generalized solution

$$
u(t)=T(t) f+\int_{0}^{p} T(p-s) F(s) d s
$$

is asymptotically stable; i.e., for every generalized solution $v(\cdot)$ of (2.1) we have $\mathrm{lim}_{\mathrm{t} \rightarrow+}\|v(\mathrm{t})-\mathrm{u}(\mathrm{t})\|=0$.

Example 2.5. Let $E$ be the Banach space $C_{0}\left(\mathbb{R}_{+}\right) ; A=\frac{d}{d x}$ with $\bar{D}(A)=\left\{f \in E: f^{\prime} \in C^{1}\right.$ and $\left.f^{\prime} \in E\right\}$ is the generator of the uniformly stable translation semigroup $T(t) f(x):=f(t+x)$. Applying (1.14) we obtain that $i m A=\left\{f: \int_{0}^{\infty} f(x) d x\right.$ exists\} is dense in $C_{o}\left(\mathbb{R}_{+}\right)$. Let $r \in \operatorname{im} A_{1}$ and let $F(\cdot)$ be a p-periodic real-valued function.

We apply Theorem 2.4 to the initial value problem

$$
\begin{equation*}
\frac{d}{d t} u(t, x)=\frac{d}{d x} u(t, x)+r(x) F(x+t) \quad, u(0, \cdot) \in D(A) . \tag{*}
\end{equation*}
$$

We may rewrite (*) as

$$
\begin{equation*}
\dot{v}(t)=A v(t)+G(t) \tag{**}
\end{equation*}
$$

where $v(t)=u(t,-)$ and $G: \mathbb{R}_{+} \rightarrow E$ is defined by

$$
G(t)(x)=r(x) F(x+t)
$$

$G \quad i s \quad p$-periodic with values in $E$ and $h_{o}=\int_{o}^{p} T(p-t) G(t)$ dt is the function $x \rightarrow\left[\int_{0}^{P} T(p-t) G(t) d t .7(x)=F(x) \int_{x}^{x+p} r(s) d s\right.$. For the function $f=\int_{k=0}^{\infty} T(k p) h_{0}$, which is given by $x \rightarrow F(x) \int_{x}^{\infty} r(s) d s$, we clearly have (Id - T(p))f $=h_{o}$. Therefore (**) has a unique p-periodic generalized solution (Thm.2.4) although iR $\in$ o( $\mathcal{A}$ ) (compare with Remark 2.3).
The unique p-periodic generalized solution u(t, *) is given by $u(t, x)=F(x+t) \int_{x+t}^{\infty} r(s) d s+F(x+t) \int_{X}^{x+t} I(s) d g=F(x+t) \int_{X}^{\infty} r(s) d s$. For every solution $v(t, \cdot)$ of (*) we have, by Thm. 2.4:
$\sup \left(\left|v(t, x)-F(x+t) \int_{x}^{+} r(s) d s\right|: x \in \mathbb{R}_{+}\right\} \rightarrow 0$ as $t \rightarrow 0$.

WOTES.
Section 1. The exponential growth bounds w(f) and w(A) as well as the characterizations (1.2), (1.6) and Theorem 1.3 (i) can be found in Hille-Phillips (1957). Growth bounds similar to $\omega_{1}$ (A) were considered first in [D'Jacenko (1976) ] and in [Zabczyk (19793, Prop.2]. Example 1.2.(2) is taken Erom wolff (1981); other 'counterexamples' can be Found in Hillemphilltps (1957), Folas (1973), Triggiani (1975), Zabczyk (1975) and Grefner-Vofgt-Nolff (1981). The statements (1.2), (1.6) and Theorem l.3.(1) are semigroup versions of results of classical Laplace transform
theory, see Hille-Phillips (1957) and widder (1946). Theorem 1.3. (f. () is a semigroup version of Theorem 1.2 .7 and 1.2 .8 fn Doetsch (1950). The lemata in the proof of Thm. 1.3 is taken from Mil'stein (1975). Theorem 1.4 and Corollary 1.5 can be found in Neubrander (1985a). Example 1.6 follows Remark 2 in Zabczyk (1975). Statement ( 1.8 ) is sometimes called the 'spectrum determined growth assumption', see, for example, Triggianf. (1975b). Theorem 1.9 is due to Slemrod (1976). The proor given here is based on a much sharper version of the inversion formula for the Laplace transform, than the one given by HillewFhillips (1957), p.349. Visin Widder (1946), p. 66 or Doetsch (1950), p. 212 one can show the followtng theorem (see Neubrander (1984b)).

Theorem. Let $A$ be the generator of a strongly continuous semigroup (T(t)) t ( on a Eanach space $E$. For every $f \in D(A)$ and $P^{>} \omega_{1}(A)$ we have

$$
T(t) f=\frac{1}{2 \pi i} \int_{P+i^{\infty}}^{p+i^{\infty}} e^{\mu t} R(\mu, A) f d \mu .
$$

The equivalence of the statements (1.12). (1.13) and 'u(A) \& 0 , were observed by many authors, see for example, Balakrishnan (1976), p.178 or Benchimol (1978). Theorem 1.11 is due to Jatko (1970) and Delfour (1974); for a proof see Pazy (1983), p. 116. Theorems 1.13 and 1.16 can be found in Neubrander (1985b) and Corollary l. 14 is due to Komatsu (1969). An example of an unstable semigroup generator a with Re $\mu<0$ for all $\mu \in \sigma(A)$ is given in Datko (1983).

Section 2. For a discusston of well-posedness of lnhonogeneous Cauchy problems we refer to Goldstein (1985a), p. 83 and Pazy (1983), p. 105. Further results on the asymptotic behavtor of the solutions of the inthomogeneous problem can be found in Reo-Hengartner (1974), Zaidnan (1979), Pazy (1983), and Neubrander (1985b). Results simillar to Lemma 2.2 and Theorem 2.4 are due to Prub (1984). For a djscussion of the asyaptotic behtvior of the solutions of $\mathrm{a}^{\prime}(\mathrm{t})=\mathrm{A}(\mathrm{t}) \mathrm{u}(\mathrm{t})+\mathrm{F}(\mathrm{t})$ see Datko (1972) and pazy (1983)sp.172.

