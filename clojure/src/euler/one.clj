(ns euler.core)

(defn mod3or5 [x] 
  (or 
    (= 
      (mod x 5) 
      0) 
    (= 
      (mod x 3) 
      0)
    )
  )
(apply + (filter mod3or5 (range 1000)))