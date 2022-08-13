# Probability

Likelihood of occurence of an event.

$$ P(Event) = \frac{No.\ of\ ways\ the\ event\ can\ occur}{Total\ possible\ outcomes} $$

## Mutual Exclusive Events
Two events are mutually exclusive if they cannot occur at the same time. Example : <br />
1. When we are rolling a dice, we can only get one number at a time. So, the event of getting 2 is mutually exclusive from the event of getting 5. 
2. When we toss a coin, event of getting head is mutually exclusive from event of getting a tail. 

## Non-Mutual Exclusive Events
Multiple events can occur at the same time. Example : 
1. Probability of turning left using and having the radio turned on.
2. Probability of eating a green vegetabe with a red cereal. 
3. Probability of getting a queen or a heart from a deck (both can together in case of Queen of hearts). 

## Independent Events
When the occurence of one event is completely unaffected by the other. Example : <br />
1. One dice roll is independent of the previous dice roll.
2. Probability of getting rain is independent on the traffic of city.

## Dependent Events
Occurence of one event is affected by the other. Example : <br />
1. Probability of tournament depends on the probability of rain.
2. If a bag has 3 red and 3 green balls. We take out one of them. Let the event of that ball being Red be (A). Now, if we take out another ball, the probability of this being red as well depends on A.  

## Additional Rule (Probability OR)

If Event A and B are mutually exclusive, 

$$P(A \cup B) = P(A) + P(B)$$

For non-exclusive case,

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

### Questions

1. What is the probability of getting head or tail? <br />
This is a case of mutually exclusive events because coin toss can either give Head or Tail at a time. So, 
$$P(H \cup T) = P(H) + P(T) = \frac{1}{2} + \frac{1}{2} = 1$$

2. What is the probability of getting a Queen or Heart? <br />
This is a case of non mutually exclusive events because both can occur simultaneouly if the card is a Queen of Hearts. So,
$$P(Q \cup H) = P(Q) + P(H) - P(Q \cap H) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52}  = \frac{4}{13}$$

## Multiplication Rule (Probability AND)

If Event A and B are independent, 

$$P(A \cap B) = P(A) * P(B)$$


If event A is dependent on B,

$$P(A \cap B) = P(B) * P (A / B)$$
P(A/B)  = Probability of A occuring given B has already occured.

### Questions

1. What is the probability of getting a 5 after getting a 4 in dice? (Independent) <br />
$$P(5 \cap 4) = P(5) * P(4) = \frac{1}{6} * \frac{1}{6} = \frac{1}{36}$$

2. What is the probability of drawing a queen and then an ace from a deck of cards?
$$P(A \cap Q) = P(Q) * P(A / Q) = \frac{4}{52} * \frac{4}{51} = \frac{4}{663}$$