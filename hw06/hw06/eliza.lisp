;;; -*- Mode: Lisp; Syntax: Common-Lisp; -*-

#|
=========================================================
Module: eliza.lisp: 
Description: A version of ELIZA that takes inputs without 
paretheses around them unlike eliza1.lisp.
Bugs to vladimir kulyukin in canvas
=========================================================
|#

;;; ==============================

(defun rule-pattern (rule) (first rule))
(defun rule-responses (rule) (rest rule))

(defun read-line-no-punct ()
  "Read an input line, ignoring punctuation."
  (read-from-string
    (concatenate 'string "(" (substitute-if #\space #'punctuation-p
                                            (read-line))
                 ")")))

(defun punctuation-p (char) (find char ".,;:`!?#-()\\\""))

;;; ==============================

(defun use-eliza-rules (input)
  "Find some rule with which to transform the input."
  (some #'(lambda (rule)
            (let ((result (pat-match (rule-pattern rule) input)))
              (if (not (eq result fail))
                  (sublis (switch-viewpoint result)
                          (random-elt (rule-responses rule))))))
        *eliza-rules*))

(defun switch-viewpoint (words)
  "Change I to you and vice versa, and so on."
  (sublis '((i . you) (you . i) (me . you) (am . are) (my . your) (your . my))
          words))

(defparameter *good-byes* '((good bye) (see you) (see you later) (so long)))

(defun eliza ()
  "Respond to user input using pattern matching rules."
  (loop
    (print 'eliza>)
    (let* ((input (read-line-no-punct))
           (response (flatten (use-eliza-rules input))))
      (print-with-spaces response)
      (if (member response *good-byes* :test #'equal)
	  (RETURN))))
  (values))

(defun print-with-spaces (list)
  (mapc #'(lambda (x) (prin1 x) (princ " ")) list))

(defun print-with-spaces (list)
  (format t "~{~a ~}" list))

;;; ==============================

(defparameter *eliza-rules*
  '(
    ;;; rule 1
    (((?* ?x) hello (?* ?y))      
    (How do you do.  Please state your problem.))

    ;;; rule 2
    (((?* ?x) computer (?* ?y))
     (Do computers worry you?)
     (What do you think about machines?)
     (Why do you mention computers?)
     (What do you think machines have to do with your problem?))

    ;;; rule 3
    (((?* ?x) name (?* ?y))
     (I am not interested in names))

    ;;; rule 4
    (((?* ?x) sorry (?* ?y))
     (Please don't apologize)
     (Apologies are not necessary)
     (What feelings do you have when you apologize))

    ;;; rule 5
    (((?* ?x) remember (?* ?y)) 
     (Do you often think of ?y)
     (Does thinking of ?y bring anything else to mind?)
     (What else do you remember)
     (Why do you recall ?y right now?)
     (What in the present situation reminds you of ?y)
     (What is the connection between me and ?y))

    ;;; rule 6
    (((?* x) good bye (?* y))
     (good bye))

	;;; rule 7
	(((?* x) so long (?* y))
	(good bye)
	(bye)
	(see you)
	(see you later))
	

    ;;; ========== your rules begin
    ;;; add your rules here
	; r1
	(((?* ?x) what are you (?* ?y))
	(I am Eliza)
	(A therapist of sorts)
	(Shouldnt you know that by now))
	
	; r2
	(((?* ?x) what time (?* ?y))
	(I dont have a watch.)
	(Time to for you to get a watch)
	(Dont you have a phone that tells time))
	
	; r3
	(((?* ?x) sleep (?* ?y))
	(Do you often feel tired)
	(What about ?y affected your sleep))
	
	; r4
	(((?* ?x) hate (?* ?y))
	(Why do you hate ?y)
	(How would you feel if ?y hates ?x)
	(Hate leads to suffering))
	
	; r5
	(((?* ?x) hi (?* ?y))
	(How do you do.  Please state your problem))
	
	; r6
	(()
	(If you dont talk to me I cant help you)
	(Dont ignore me))
	
	; r7
	(((?* ?x) dont like (?* ?y))
	(Why dont you like about ?y)
	(What makes you say that?)
	(I dont like ?y either!))
	
	; r9
	(((?* ?x) help me (?* ?y))
	(Lets talk about ?y and i will try to help))
	
	; r10
	(((?* ?x) time (?* ?y))
	(Why ?x time?)
	(That is too long)
	(That is not enough time))
	
	; r11
	(((?* ?x) do i do (?* ?y))
	(Do ?x you would in a normal situation.)
	(Do ?x you want with ?y))
	
	; r12
	(((?* ?x) too many (?* ?y))
	(Start at the begining.)
	(Take your ?y one step at a time.))
	
	; r13
	(((?* ?x) dont want (?* ?y))
	(Why dont you want ?y))
	
	; r14
	(((?* ?x) should I (?* ?y))
	(What do you think?)
	(What do you think would happen if you did ?y))
	
	; r15
	(((?* ?x) because (?* ?y))
	(What makes you say that?)
	(How does ?y affect the situation?))
	
	; r16
	(((?* ?x) dont know (?* ?y))
	(Was my question too complicated?)
	(Did my question make you uncomfortable?)
	(Then it must not be too important.))
	
	; r17
	(((?* ?x) yes (?* ?y))
	(Why is that?)
	(What conclusions can you draw from that?)
	(Are you sure?)
	(That is good.)
	(That works.))
	
	; r18
	(((?* ?x) having (?* ?y))
	(Did you come to me because you are having ?y))
	
	; r19
	(((?* ?x) cant remember (?* ?y))
	(Then it must not be too important.)
	(What can you remember that is related to ?y))
	
	; r20
	(((?* ?x) what if (?* ?y))
	(How would ?y affect you?)
	(Do you wish that it does?))
	
	; r21
	(((?* ?x))
	(Im not sure I understand what you mean.)
	(Could you please go into more detail?)
	(That statement seems vague could you explain it better?)
	(Go on.))
	
	; r22
	(((?* ?x) thank you (?* ?y))
	(Im happy to help)
	(Do you this meeting was helpful?))
	
    ;;; ========== your rules end

   ))

;;; ==============================


