import Control.Applicative
import Control.Monad
import System.IO

-- Print "Hello World" N  amount of times. The input portion will be handled automatically.
-- You need to write a function with the recommended method signature.
-- Source https://www.hackerrank.com/challenges/fp-hello-world-n-times
hello_worlds n =
    if n <= 0 then putStr ""
    else do
        putStrLn "Hello World"
        hello_worlds (n-1)


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    hello_worlds n
    --  Print "Hello World" on a new line 'n' times.

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret