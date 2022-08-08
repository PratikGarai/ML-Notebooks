# Distributions

## Gaussian / Normal / Laplace - Gauss 

![Normal Distribution](./img/NormalDistribution.png)

1. Symmetric about the mean. 
2. Lower variation = Steeper Curve.
3. Formula : 
$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2} $$
4. Default assumption of natural data when we have no idea about the data distribution.
5. The area between $\mu \pm nx ; (n \in Natural Number)$ follow a particular breakdown.
![Normal Distribution Breakdown](./img/NormalDistributionBreakdown.png)

### Central Limit Theorem

A sample size increases, the data distribution of the sample usually converges (or becomes similar) to the normal distribution.Therefore, physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have distributions that are nearly normal.