(defun day-1-part-2 (changes)
  ;; problem 1 was just summing the list of changes
  ;; problem 2 was finding the first frequency that repeated
  (let ((freq 0)
        (seen (make-hash-table :test 'equal)))
    (loop do
	 (dolist (f changes)
	   (incf freq f)
	   (cond ((gethash freq seen nil)
		  (return-from day-1-part-2 freq))
		 (t (setf (gethash freq seen) t)))))))

(let ((data (mapcar #'parse-integer (uiop:read-file-lines "1.input"))))
  (format t "~a~%" (day-1-part-2 data))
)
