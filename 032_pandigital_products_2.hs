-- Partially edited (cleaned up) by Arthur Lee.

-- My first attempt at Haskell. 11 Jan 2021
-- Took a while to figure out what merge did (looked at stack overflow), but managed to modify it to suit my purpose.
-- All code parsed on https://coderpad.io/sandbox. Go to hell, ghci.
-- Still not really sure how to set all the headers and proper containers.

{-
Project Euler Problem 32: Pandigital products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
-}

module Main where
import qualified Data.List as List

digits :: String
digits = concat . map show $ [1..9]

-- me: what's the diff between $ and .?

-- "." is function composition (forgot the word). So (.) :: (b -> c) -> (a -> b) -> (a -> c)
-- "$" is function application. So ($) :: (a -> b) -> a -> b
--     same as space, except that it has the lowest priority in binding. So in the above example:
-- concat . map show $ [1..9]
-- = (concat . map show) [1..9]

perm :: [String]
perm = List.permutations digits

eqn :: String -> [(Integer, Integer, Integer)]
eqn numStr = do  -- look up "list monad". This is exactly what the list comprehension expands into (by the compiler. It's cleaner when you start to have complicated list comprehensions.
  start <- [1..4]
  let end = 5
  pure ( read (take start numStr)
       , read (drop start $ take end numStr)
       , read (drop end numStr)
       )
  
eqns :: String -> [Integer]
eqns numStr = [c | (a,b,c) <- (eqn numStr), a * b == c]



merge :: Ord a => [[a]] -> [a]
merge = List.foldl1' (\x y -> List.nub $ x ++ y)

fx :: Integer
fx = sum . merge . map eqns $ perm


main :: IO ()
main = print fx
