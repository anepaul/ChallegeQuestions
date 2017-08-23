import Control.Applicative
import Control.Monad
import System.IO


-- main :: IO ()
main = do
    n_temp <- getLine
    let n_t = words n_temp
    let n = read $ n_t!!0 :: Int
    let k = read $ n_t!!1 :: Int
    a_temp <- getLine
    let a = map read $ words a_temp :: [Int]
    let ret = recRepeat rotateLeft k a
    -- print ret
    -- prettyPrint ret
    mapM_ print ret

-- prettyPrint arr = 
--     case arr of
--         []      -> putStr ""
--         (x:xs)  -> do 
--             putStr x
--             prettyPrint xs

rotateLeft :: [Int] -> [Int]

rotateLeft arr =
    case arr of 
        []  -> []
        h:t -> t ++ [h]

recRepeat func times param =
    if times <= 0 then param
    else recRepeat func (times - 1) (func param)


getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = x:xs
        return ret