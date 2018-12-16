# Another approach for part B

One possible approach would be to start from 'e' and advance in the progression saving how many steps it took to reach that *intermediate molecule*.

And also have a *similarity* function that measures how close we are to the final molecule.
That way we can apply transformations to that molecule; and, if we get on a *branch* that gets further from the final 'e' we can continue with another.