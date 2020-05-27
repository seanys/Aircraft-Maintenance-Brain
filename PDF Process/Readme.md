## Navigate To Target Page In One Step

### Abstract

The high standards of the aviation industry are reflected in the huge number of manuals. Usually, engineers have to check terms in different manuals. However, there are about 1000 pages in a single manual on average,  so lots of time is wasted on turning pages.

With the help of our PDF Process technology, this job will become easier. We have built a PDF Process system and it works well. We have extracted key information from manuals and have established databases. For example, we have extracted texts and images in the IPCs (Illustrated Part Catalogs) and used this data in our Component Recognition. In addition, we have extracted tables in the AMMs (Aircraft Maintenance Manuals) and also analyzed the structure of these PDF documents. Therefore, when an engineer looks for a component information or a task, our intelligent brain will know which page he or she should turn to.  As a result, once click an item, engineers can navigate to target page in one step.

### Structure

In manuals, the information we need is presented in different forms, such as texts, images and tables etc. However, they are all objects in PDF files. After deconstruction a file, we can extract objects in it and then turn these objects to data we want. What's more, we can analyze the outline to get the relationship between chapters' title (such as tasks and components) and page numbers, so as to achieve a quick navigation among pages.


### Explanation

#### AMM Process

We process PDF files of AMM using Python with the help of [Camelot](https://camelot-py.readthedocs.io/en/master/index.html) and [PDFMiner](https://github.com/euske/pdfminer).

**Demo:**  `737NG-AMM-directory.pdf` and manuals in `\73NG-AMM_9309` have been processed to `AMMdirectory.csv` and `AMMchapters.csv` 

#### IPC Process

We process PDF files of IPC using Python with the help of [Camelot](https://camelot-py.readthedocs.io/en/master/index.html), [PDFMiner](https://github.com/euske/pdfminer) and [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

**Demo:** `\pic` and `IPCtext.csv` shows the text and image data of each part in `Illustrated-Parts-Catalog.pdf.`



**Contact:** wangzilu@tongji.edu.cn

**Author:** Prinway