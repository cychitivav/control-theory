# Control theory repository

<!-- ## Table of contents
1. [Signals and systems I](#signals-and-systems-i)
1. [Signals and systems II](#signals-and-systems-ii)
1. [Control systems](#control-systems) -->

#### Requirements

- Python 3.6+.
- Python Control Systems Library `pip install control`.
  - Documentation: [Python Control Systems Library](https://python-control.readthedocs.io/en/0.9.2/index.html).
  - Functions: [functions reference](https://python-control.readthedocs.io/en/0.9.2/control.html#function-ref)
- NumPy `pip install numpy`.
- SciPy `pip install scipy`.
- Matplotlib `pip install matplotlib`.

## Fundamentals

### Modeling

In physics and engineering, mathematical models are used to abstract the real world. This abstraction is done through first-principles equations such as:

- Kirchhoff's circuit laws
  1. Current law: $\sum_{k=1}^n I_k = 0$
  1. Voltage law: $\sum_{k=1}^n V_k = 0$
- Newton's laws of motion
  - $\vec{F} = m \vec{a}$
- Maxwell's equations
  1. $\nabla\cdot E=\frac{\rho}{\epsilon_0}$
  1. $\nabla\cdot B=0$
  1. $\nabla\times E=-\frac{\partial B}{\partial t}$
  1. $\nabla\times B=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right)$
- etc.

All these formulas describe systems, a collection of interconnected parts that form a larger more complex whole and also receive and yield signals, which are also mathematically modeled. The **usefulness** of the models depends on the accuracy, i.e., how close it is to the real system and signals.

#### Signals

A signal is a measurable (physical) function whose values describe a physical quantity. The **mathematical model** of a signal is a _function_ (mapping from a domain $\mathcal{D}$ to a range $\mathcal{R}$, i.e. $f(\cdot):\mathcal{D}\to\mathcal{R}$ ) or formula that describes the physical quantity of interest.

Generally the domain is the one-dimensional space of the positive reals (time $t\in\mathbb{R}^+$), although there are multidimensional signals (more than one independent variable).

##### Classification of signals

The signals can be classified into several types, but the main ones are:

```mermaid
graph LR;
    P[Classification of signals]:::green;

    P --> N[Nature of independent variable]:::purple;
    P --> S[Symmetry]:::purple;
    P --> Pe[Periodicity]:::purple;
    P --> R[Range of the function]:::purple;
    P --> I[Number of independent variable]:::purple;
    P --> F[Functional definition]:::purple;
    P --> E[Energy and power]:::purple;

    N --> C[Continuous-time signals]:::blue;
    N --> D[Discrete-time signals]:::blue;
    C --> A[Analog signals]:::yellow;
    D --> Di[Digital signals]:::yellow;

    S --> Ev[Even signals]:::blue;
    S --> O[Odd signals]:::blue;
    S --> As[Asymmetric signals]:::blue;

    Pe --> Per[Periodic signals]:::blue;
    Pe --> No[Non-periodic signals]:::blue;

    R --> Re[Real valued signals]:::blue;
    R --> Im[Complex valued signals]:::blue;

    I --> M[Multidimensional signals]:::blue;
    I --> On[One-dimensional signals]:::blue;

    F --> St[Stochastic signals]:::blue;
    F --> De[Deterministic signals]:::blue;

    E --> En[Energy signals]:::blue;
    E --> Po[Power signals]:::blue;

	%% Colors
	classDef green  fill:#58fc71, stroke:#000;
	classDef yellow  fill:#fcd158, stroke:#000;
	classDef purple  fill:#c668fc, stroke:#000;
    classDef blue  fill:#68d2fc, stroke:#000;
```

- **Nature of independent variable**:

  - **Continuous-time (CT) signals**: are defined at every time
    instant in a time interval of interest, and its amplitude can assume any value in a continuous range.
  - **Discrete-Time (DT) Signals**: are defined only at discrete time instants, and its amplitude can assume any value in a
    continuous range.
	- **Digital Signals**: its amplitude can assume a value only from a finite given set.

- **Symmetry**:

  - **Even signals**: are symmetric around the origin, i.e. $f(x) = f(-x)$

- **Periodicity**:

  - **Periodic**: the signal is periodic, i.e. it repeats itself periodically.
    - $x(t)=x(nT)$ where $n$ is an integer and $T$ is the period of the signal.
    - $x[n]=x[n+N]$ where $N$ is the number of samples.
  - **Non-periodic**: if doesn't satisfy the periodicity condition, the signal is non-periodic.

  > **Note**: All CT sinusoidal signals are periodic, but not all DT sinusoidal signals are periodic. See [signals notebook](scripts/signals.ipynb).

##### Transformations
There are 3 basic transformations of signals:
* **Shift**
* **Scale**
* **Reversal**


## Resources and references

- [**Awesome control theory repo**](https://github.com/A-make/awesome-control-theory): Very useful to find resources (e.g., books, videos, lectures, etc.) about control theory.
- [**Control theory slides**](https://github.com/SergeiSa/Control-Theory-Slides-Spring-2022): Slides about control theory made by Sergei Savin.
- [**Engineering media**](https://engineeringmedia.com/): A website with a lot of resources about control theory made by Brian Douglas.
