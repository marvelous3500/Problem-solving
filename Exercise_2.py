*Exercise 2*
Create a functions that takes two arguments: an `Array` and a `Number`.
This is a kind of Markov chain. The _function_ should return the number of `Number` chain that can be created from the `Array`

For Example
Array =  [A, B, C, D, E, F, G, H]`
Number = 4`

We can create `5` chains : `[A,B,C,D]`, `[B,C,D,E]`,  `[C,D,E,F]`,  `[D,E,F, G]`, `[E,F, G,H]`
The _function_ should return `5` since we can only create `5` changes of  `Number 4

```
def chain_counter(array, chain_length):
    chain = []
    chain_holder = []
    if len(array) < chain_length:
        return 0
    for item in array:
        chain.append(item)
        if len(chain) == chain_length:
            print(chain)
            chain_holder.append(chain)
            array.pop(0)
            chain_counter(array, chain_length)

    return len(chain_holder)
```