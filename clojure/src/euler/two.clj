(ns euler.core)

; generator for fib numbers
; sum under 4,000,000
(def fib-seq (lazy-cat [0 1]
 (map + fib-seq (rest fib-seq))))
(apply +' (filter (fn [x] (and (even? x )(< x 4000000))) fib-seq)) ; filter can be used to control output from lazy-cat
