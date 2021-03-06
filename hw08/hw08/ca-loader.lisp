#|
===========================================================
-*- Mode: Lisp; Syntax: Common-Lisp -*-

File: ca-loader.lisp
Author: Vladimir Kulyukin

Bugs to vladimir kulyukin in canvas
===========================================================
|#

(in-package :user)

;;; change this to the directory where the ca files are.
(defparameter *ca-dir* "/mnt/c/Users/Sanko/Documents/School/IntelligentSystems/hw08/hw08/")

(defparameter *files* '("ca-utilities" "cd" "ca" "ca-functions" "ca-lexicon"))

(defun ca-loader (files &key (mode :lisp))
  (dolist (a-file files t)
    (load (concatenate 'string
            *ca-dir*
            a-file
            (ecase mode
              (:lisp ".lisp")
              (:cl  ".cl")
              (:fasl ".fasl"))))))
