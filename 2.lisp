(defun print-hash-table-entry (key value)
(if (or (eq value 3) (eq value 2)) (return-from print-hash-table-entry value) (return-from print-hash-table-entry NIL))))

(defun iter-hash-map (hashmap func)
  (maphash func hashmap))

(defun letter-count (word)
(let ((count (make-hash-table)))
  (loop for ch across word do
       (if (eq (gethash ch count) NIL) (setf (gethash ch count) 1)
	     (setf (gethash ch count) (incf (gethash ch count)))))
  (iter-hash-map count #'print-hash-table-entry)))

(let ((data (uiop:read-file-lines "C:/Users/HARIKRISHNAN/experimental/aoc 18/2.input")))
  (dolist (word '("hello" "world"))
    (format t "~a~%" (letter-count word))))

