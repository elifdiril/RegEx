Sample input (file.txt):

06/03/17 12:34:45 user:  ilknur a36-12.2344 status:  success
06/03/17 18:14:42 error on purchase process
07/03/17 08:23:21 user:  bayram zxg6546-374.08 isbn:12345678987 status:  success
35/13/17 09:34:38 user:  asdf bgcg567-3457.3 isbn:11223344556 status:  failed

Sample output (datesoutput.txt):

06-03-2017
06-03-2017
07-03-2017
35-13-2017

Sample input (file.txt):

06/03/17 12:34:45 user:  ilknur abetgg34456-124455.2334 status:  success
06/03/17 18:14:42 user:  bayram error on purchase process no pr001.23
07/03/17 08:23:21 user:  bayram z646-357.8 isbn:12345678987 status:  success
07/03/17 09:34:38 user:  asdf bg567-34.33 isbn:11223344556 status:  failed
08/03/17 11:19:12 user:  ilknur error on purchase process
08/03/17 14:45:04 user:  ilknur bq9530-2452.0335 isbn:98765432123 status:  success
09/03/17 19:34:35 user:  asdf az326-12.99 status:  waiting

Sample output (codeoutput.txt):

06-03-2017 Abetgg34456-124455.2334 ilknur
07-03-2017 12345678987 Z646-357.8 bayram
08-03-2017 98765432123 Bq9530-2452.0335 ilknur
