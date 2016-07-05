#!/bin/bash
# This is a comment

hdfs dfs -rm -r /user/hadoop/HW7Output/EDADirectedGraph
nohup python EDADirectedGraph.py -r hadoop hdfs:///user/hadoop/HW7data/all-pages-indexed-out.txt --output-dir=HW7Output/EDADirectedGraph --no-output > nohup/EDADirectedGraph.out &

