# Distributions - (Gaussian / Normal / Laplace - Gauss)

![Normal Distribution](./img/NormalDistribution.png)

1. Symmetric about the mean. 
2. Lower variation = Steeper Curve.
3. Formula : 
$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2} $$
4. Default assumption of natural data when we have no idea about the data distribution.
5. The area between $\mu \pm nx ; (n \in Natural Number)$ follow a particular breakdown.
![Normal Distribution Breakdown](./img/NormalDistributionBreakdown.png)

## Central Limit Theorem

A sample size increases, the data distribution of the sample usually converges (or becomes similar) to the normal distribution.Therefore, physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have distributions that are nearly normal.


## Z Score

Given a value ($x$), how many standard deviations away from the mean of the distribution$(\mu)$ it is. 

$$ Z-Score = \frac{x_i-\mu}{\sigma}$$ 

Example 1:- <br />
Distribution with : Mean = 4 ; Standard Deviation = 1. Find the Z-Score for 4.75. <br />
Sol. $$Z-Score = \frac{4.75-4}{1} = 0.75 \sigma$$

**Note:** The value (4.75) is on the right of the mean, since the Z-Score is positive. If the Z-Score was negative, the value would be on the left side of the mean.

Example 2:- <br />
Distribution with : Mean = 4 ; Standard Deviation = 1. Find the Z-Score for 3.75. <br />
Sol. $$Z-Score = \frac{3.75-4}{1} = -0.25 \sigma$$

## Standard Normal Distribution

Normal Distribution where mean $(\mu) = 0$ and standard deviation $(\sigma) = 1$.

### Standardinzing a Normal Distribution

Take every value in a distribution and find its Z-Score. This new array of outputs is the standard normal distribution.

![Standardizing Normal Distribution](./img/StandardizingNormalDistribution.svg)

### Appications in ML

**Standardization** is used to scale down all features (column wise data) into a smaller range in a propotional manner so that the decisions are not skewed due to numerical scales. For example : If the dataset has income in 1000s range and age in 10s range, the decision making will be affected highly due to income, as compared to age. However, if we standardize both all the features, both will be reduced to a common numerical scale. This will make both income and age to have similar weightage in the decision making process.