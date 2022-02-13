import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","project.settings")
django.setup()

from .models import PubmedDatabase
from Bio import Entrez
from Bio import Medline

def ToDatabase(): 
    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term="asthma", retmax = "40000")
    records = Entrez.read(handle)
    records["IdList"]
    idlist = records["IdList"]

    #def split_list(lst,n):
    #    for i in range(0, len(lst), n):
    #        yield idlist[i:i + n]


    #final_list = list(split_list(idlist,10000))
    #for i in range(0,5):

    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records =  Medline.parse(handle)

    title_list = []
    author_list = []
    pmid_list = []
    abstract_list = []
    keywords_list = []

    for record in records:
        try:
            title = record.get("TI")
            #title_list.append(title)
        except:
            title = "-"
            #title_list.append(title)
        try:
            author = record.get("AU")
            #author_list.append(author)
        except:
            author = "-"
            #author_list.append(author)
        try:
            pmid = record.get("PMID")
            #pmid_list.append(pmid)
        except:
            pmid = "-"
            #pmid_list.append(pmid)
        try:
            abstract = record.get("AB")
            #abstract_list.append(abstract)
        except:
            abstract = "-"
            #abstract_list.append(abstract)
        try:
            keywords = record.get("OT")
            #keywords_list.append(keywords)
        except:
            keywords = "-"
            #keywords_list.append(keywords)

        a = PubmedDatabase(id_name = pmid, author = author, title = title, abstracts = abstract, keywords=keywords )
        a.save()


