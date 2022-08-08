# Percentiles and Quartiles

## Percentile 

A value below which a certain percentage ob observations lie.

## Five Number Summary 

1. Minimum
2. First Quartile ( $Q_1$ )
3. Median
4. Third Quartile ( $Q_3$ )
5. Maximum

$$ Inter Quartile Range (IQR) = Q_3 - Q_1 $$

## Removing Outliers using Five Number Summary

$$ Outlier < Lower Fence < Non Outlier < Higher Fence < Outlier $$ 
$$ Lower Fence = Q_1 - 1.5*IQR$$
$$ Higher Fence = Q_3 + 1.5*IQR$$

## Example 

Let dataset $D = \{ 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 27\}$<br />

$ Q_1 = D[\lfloor(0.25 * 19)\rfloor] = 3 $ <br />
$ Q_3 = D[\lfloor(0.75 * 19)\rfloor] = 7 $ <br />
$ IQR = 7-3 = 4 $ <br />
$ Lower Fence = 3-(1.5*4) = -3 $ <br />
$ Higher Fence = 7+(1.5*4) = 13 $ <br />

So, Outlier = 27