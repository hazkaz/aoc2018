;; function to check if a given value exists in a list
(defun in (val list)
  (if (eq (car list) val) T (if (eq (cdr list) NIL) NIL (in val (cdr list)))))

;; loop through the list in a wraparound fashion until a frequency repeats itself
(let (
      (total 0)
      (data (mapcar #'parse-integer (uiop:read-file-lines "1.input")))
      (n 0)
      (existing NIL)
      ) (loop for num = (nth n data)
	     while (not (in total existing)) do (progn
						  ;; add the current frequency to the list 'existing'
						  (setf existing (cons total existing))
						  (setf total (+ total num))
						  (setf n (+ 1 n))	
						  (setf n (mod n (list-length data)))))
	;; print the total once done
	(format t "~A~%" total))
