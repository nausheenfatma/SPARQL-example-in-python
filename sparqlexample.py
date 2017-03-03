# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:58:34 2015

@author: nausheenfatma
"""

#code to check if SPARQL endpoint is working

from SPARQLWrapper import SPARQLWrapper,JSON
import re

sparql=SPARQLWrapper("http://dbpedia.org/sparql") #query the online DBpedia RDF database

def run_query(query):                #query returns triples #json
           # print "query:"+query
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            triple_list={}
            try :            
                results = sparql.query().convert()
                print "len--",len(results["results"]["bindings"])
                #print "not here"
                i=0
                for result in results["results"]["bindings"]:
                    s=""
                    p=""
                    o=""
                    #print result
                    if "s" in result:
                        s=(result["s"]["value"])
                        s="<"+s+">"
                    if "p" in result:
                        p=(result["p"]["value"])
                        p="<"+p+">"
                        
                    if "o" in result :
                        o=(result["o"]["value"])
                    
                        if (re.match("http",o)):
                        #print "match"
                            o="<"+o+">"
                    triple_list[i]={"s":s,"p":p,"o":o}
                    i=i+1
            except :
                print "x"
                pass
            #print "---"
            return triple_list  



query="select ?s ?p ?o where {?s ?p ?o .} limit 20"
list_one=run_query(query)
print len(list_one)
print list_one

query="select  ?p ?o where {<http://dbpedia.org/resource/Priyanka_Chopra> ?p ?o .}"
list_one=run_query(query)
print len(list_one)
print list_one
