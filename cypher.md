Docker
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# Commands

## get count
> MATCH (n) OPTIONAL MATCH (n)-[r]-() return count(n)

## get some data
> MATCH (n) OPTIONAL MATCH (n)-[r]-() RETURN n,r LIMIT 1000

## delete all
> MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r

## more samples

> CREATE (ee:Person { name: "Emil", from: "Sweden", klout: 99 }) return ee

> MATCH (ee:Person) WHERE ee.name = "Emil" RETURN ee;

> MATCH   (ee:Person) WHERE ee.name = "Emil"

> CREATE  (js:Person  { name: "Johan", from: "Sweden", learn: "surfing" }),
        (ir:Person  { name: "Ian", from: "England", title: "author" }),
        (rvb:Person { name: "Rik", from: "Belgium", pet: "Orval" }),
        (ally:Person{ name: "Allison", from: "California", hobby: "surfing" }),
        (ee)-[:KNOWS {since: 2001}]->(js),
        (ee)-[:KNOWS {rating: 5}]->(ir),
        (js)-[:KNOWS]->(ir),
        (js)-[:KNOWS]->(rvb),
        (ir)-[:KNOWS]->(js),
        (ir)-[:KNOWS]->(ally),
        (rvb)-[:KNOWS]->(ally)

> MATCH (p:Person) WHERE p.name = "Emil"

> MATCH (p2:Person) WHERE p2.name = "Emil2"

> CREATE (p)-[:KNOWS]->(p2)

> MATCH (ee:Person)-[:KNOWS]-(friends)
> WHERE ee.name = "Emil"
> RETURN ee, friends

> MATCH (js:Person)-[:KNOWS]-()-[:KNOWS]-(surfer)
> WHERE js.name = "Johan" AND surfer.hobby = "surfing"
> RETURN DISTINCT surfer
- ()empty parenthesis to ignore these nodes
- DISTINCTbecause more than one path will match the pattern
- surfer will contain Allison, a friend of a friend who surfs


> CREATE (t:Person { name: "Tom", age: "50" }) return t


-------------------------------------------------------------------------------
# Neo4j

## start db
> ./neo4j-community-3.0.4/bin/neo4j console			

## clean db completly
> data/databases/graph.db                           


-------------------------------------------------------------------------------
_The end._
