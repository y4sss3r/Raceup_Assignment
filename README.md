# Raceup_Assignment
Driverless Electric Division
# Coordinate System

$$
\text{Let } H, K \in \mathbb{N}
$$

Let $N$ be the set of nodes of the system (with polar coordinates).

I find it convenient to change the coordinate system and switch from the polar one to a “customized” one:

Let $P$ be a point belonging to $N$.
Let $h$ be the index of the circumference starting from the innermost one.
Let $k$ be the number of inclinations of the line containing point $P$ with angular coefficient $\tan\left( \frac{y_{p}}{x_{p}} \right)$
$$
\text{In the new system, the point is defined as } P(h, k)
$$
$$
\text{with } h\in[0, H-1], ~k\in[0, K-1]
$$
Therefore, the initial point $P_{0}$, in the new system, has coordinates $(H-1, 0)$

Now I will illustrate how to move from the customized coordinates to the polar ones:
$\text{Point P belongs to the semicircle of radius:}$
$$
r= r_\text{inner}+h\cdot \frac{r_{\text{outer}}-r_{\text{inner}}}{H-1}
$$
$\text{Point P belongs to the line forming with the x-axis an angle of: }$
$$
\alpha=k\cdot \frac{\pi}{K-1}
$$
If in Cartesian coordinates a point could be written as:
$$
P\left(r\cos(\alpha), r\sin(\alpha)\right)
$$
we can conclude by showing the relationship between the Cartesian and the customized coordinates.
$$
\begin{cases}

x_{p}=\left(r_\text{inner}+h\cdot \frac{r_{\text{outer}}-r_{\text{inner}}}{H-1}\right)\cos\left(k\cdot \frac{\pi}{K-1}\right) \
y_{p}=\left(r_\text{inner}+h\cdot \frac{r_{\text{outer}}-r_{\text{inner}}}{H-1}\right)\sin\left(k\cdot \frac{\pi}{K-1}\right)
\end{cases}
$$

# Distance Between Two Points

Let $P_{1}(h_{1}, k_{1})$ and $P_{2}(h_{2}, k_{2})$

$$
\overline{P_{1}P_{2}}=\sqrt{ (x_1 -x_{2})^2 + (y_{1}-y_{2})^2 }
$$
where $x, y$ are values as functions of $h$ and $k$, easily derived using the relation illustrated in the previous paragraph.

