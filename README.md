Naive Bayesian
=============

In this question, i implemented the Naive Bayes document classiﬁer and apply it to the classic 20 newsgroups [dataset]
(http://qwone.com/~jason/20Newsgroups/) In this dataset, each document is a posting that was made to one of 20 diﬀerent usenet newsgroups.

The goal was to write a program which can predict which newsgroup a given document was posted to.

1. vocabulary.txt is a list of the words that may appear in documents. The line number is word’s id in other ﬁles. That is, the ﬁrst word (’archive’) has wordId 1, the second (’name’) has wordId 2, etc. 

2. newsgrouplabels.txt is a list of newsgroups from which a docment may have come. Again, the line number corresponds to the label’s id, which is used in the .label ﬁles. The ﬁrst line (’alt.atheism’) has id 1, etc. 

3. train.label Each line corresponds to the label for one document from the training set. Again, the document’s id (docId) is the line number. 

4. test.label The same as train.label, except that the labels are for the test documents. 

5. train.data Speciﬁes the counts for each of the words used in each of the documents. Each line is of the form “docId wordId count”, where count speciﬁes the number of times the word with id wordId in the training document with id docId. All word/document pairs that do not appear in the ﬁle have count 0.

6. test.data Same as train.data, except that it speciﬁed counts for test documents. 



##how to run:
    
    python nb.py vocabulary.txt train.label train.data test.label test.data


**- Khabbab Saleem**
