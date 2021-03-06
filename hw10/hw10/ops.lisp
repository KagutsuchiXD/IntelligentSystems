;;; -*- Mode: Lisp; Syntax: Common-Lisp; -*-
;;; Module: ops.lisp
;;; different worlds and operators for the GPS planner.
;;; bugs to vladimir kulyukin in canvas

;;;Plan for Problem 2 A:
;;;((START) (EXECUTE PUT-C-FROM-A-ON-T) (EXECUTE PUT-B-FROM-T-ON-C) (EXECUTE PUT-A-FROM-T-ON-B))
;;;Plan for Problem 2 B:
;;;((START) (EXECUTE PUT-C-FROM-A-ON-T) (EXECUTE PUT-B-FROM-T-ON-C) (EXECUTE PUT-A-FROM-T-ON-B))
;;;Plan for Problem 3:
;;;((START) (EXECUTE DROP-BALL) (EXECUTE PUSH-CHAIR-FROM-DOOR-TO-MIDDLE-ROOM) (EXECUTE CLIMB-ON-CHAIR)
;;; (EXECUTE GRASP-BANANAS) (EXECUTE EAT-BANANAS))
;;; =========================================

(in-package :user)

(defstruct op "An operation"
  (action nil) 
  (preconds nil) 
  (add-list nil) 
  (del-list nil))

(defun executing-p (x)
  "Is x of the form: (execute ...) ?"
  (starts-with x 'execute))

(defun convert-op (op)
  "Make op conform to the (EXECUTING op) convention."
  (unless (some #'executing-p (op-add-list op))
    (push (list 'execute (op-action op)) (op-add-list op)))
  op)

(defun op (action &key preconds add-list del-list)
  "Make a new operator that obeys the (EXECUTING op) convention."
  (convert-op
    (make-op :action action :preconds preconds
             :add-list add-list :del-list del-list)))

;;; ================= Son At School ====================

(defparameter *school-world* '(son-at-home car-needs-battery
					   have-money have-phone-book))

(defparameter *school-ops*
  (list
    ;;; operator 1
   (make-op :action 'drive-son-to-school
	    :preconds '(son-at-home car-works)
	    :add-list '(son-at-school)
	    :del-list '(son-at-home))
   ;;; operator 2
   (make-op :action 'shop-installs-battery
	    :preconds '(car-needs-battery shop-knows-problem shop-has-money)
	    :add-list '(car-works))
   ;;; operator 3
   (make-op :action 'tell-shop-problem
	    :preconds '(in-communication-with-shop)
	    :add-list '(shop-knows-problem))
   ;;; operator 4
   (make-op :action 'telephone-shop
	    :preconds '(know-phone-number)
	    :add-list '(in-communication-with-shop))
   ;;; operator 5
   (make-op :action 'look-up-number
	    :preconds '(have-phone-book)
	    :add-list '(know-phone-number))
   ;;; operator 6
   (make-op :action 'give-shop-money
	    :preconds '(have-money)
	    :add-list '(shop-has-money)
	    :del-list '(have-money))))

;;; ================= Sussman's Anomaly ====================

(defparameter *block-world* '(a-on-t b-on-t c-on-a clear-c clear-b))

(defparameter *block-ops*
  (list
   ;;; your block world operators to avoid the Sussman Anomaly.
   ; operator 1
    (make-op :action 'put-a-from-t-on-b
		:preconds '(a-on-t clear-a clear-b b-on-c)
		:add-list '(a-on-b)
		:del-list '(a-on-t clear-b))
	; operator 2
	(make-op :action 'put-c-from-a-on-t
		:preconds '(c-on-a clear-c a-on-t)
		:add-list '(c-on-t clear-a)
		:del-list '(c-on-a))
	;operator 3
	(make-op :action 'put-b-from-t-on-c
		:preconds '(b-on-t clear-b clear-c c-on-t)
		:add-list '(b-on-c)
		:del-list '(c-clear b-on-t))
   )
  )
	    
;;; ================= Monkey and Bananas ====================

(defparameter *banana-world* '(at-door on-floor has-ball hungry chair-at-door))

(defparameter *banana-ops*
  (list
    ;;; your banana world operators to help the hungry monkey not to starve.
	; op 1
	(make-op :action 'push-chair-from-door-to-middle-room
		:preconds '(at-door chair-at-door)
		:add-list '(at-middle-room chair-at-middle-room)
		:del-list '(at-door chair-at-door))
	; op2
	(make-op :action 'climb-on-chair  
		:preconds '(at-middle-room on-floor chair-at-middle-room)
		:add-list '(at-bananas)
		:del-list '(on-floor))
	; op 3
	(make-op :action 'drop-ball
		:preconds '(has-ball)
		:add-list '(empty-handed)
		:del-list '(has-ball))
	; op 4
	(make-op :action 'grasp-bananas
		:preconds '(empty-handed at-bananas)
		:add-list '(has-bananas)
		:del-list '(empty-handed))
	; op 5
	(make-op :action 'eat-bananas
		:preconds '(hungry has-bananas)
		:add-list '(not-hungry empty-handed)
		:del-list '(hungry has-bananas))
	;op 6
	(make-op :action 'grasp-ball
		:preconds '(empty-handed)
		:add-list '(has-ball)
		:del-list '(empty-handed))
    )
  )
  
(mapc #'convert-op *school-ops*)
(mapc #'convert-op *block-ops*)
(mapc #'convert-op *banana-ops*)

(provide :ops)
