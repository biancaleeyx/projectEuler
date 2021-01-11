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
import Data.List

digits :: String
digits = concat [show n|n<-[1..9]]

perm :: [String]
perm = permutations digits

eqn :: String -> [(Integer, Integer, Integer)]
eqn numStr = [(read (take start numStr) :: Integer, read (drop start $ take end numStr) :: Integer, read (drop end numStr) :: Integer)|start<-[1..4],end<-[5]]

eqns :: String -> [Integer]
eqns numStr = [c|(a,b,c)<-(eqn numStr), a*b==c]

merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] [] = []
merge2 [] x = x
merge2 x [] = x
merge2 xs (y:ys) = if y `elem` xs
                    then merge2 xs ys
                    else y:(merge2 xs ys)
                    
mergePairs :: Ord a => [[a]] -> [[a]]
mergePairs [] = []
mergePairs (x:[]) = [x]
mergePairs (x:y:end) = mergePairs ((merge2 x y):(mergePairs end))

merge :: Ord a => [[a]] -> [a]
merge [] = []
merge x = head $ mergePairs x

-- given permuted list 123456789
fx :: Integer
fx = sum $ merge [eqns numStr|numStr<-perm]

main :: IO ()
main = do print (fx)
