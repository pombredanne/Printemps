Printemps
=========

Printemps is my attempt at creating a GraphDB stack for Python. It's inspired
from `Tinkerpop <https://github.com/tinkerpop/>`_ stack and make a heavy use
of it.

Here is a description of all the component:

- ``printemps.core``: core API, based on `jnius <https://github.com/kivy/pyjnius/>`_ 
  bindings of `Blueprints <https://github.com/tinkerpop/blueprints>`_. You can 
  use the API depending of the underlying backend for embedded or remote 
  graphdb work.

- ``printemps.server``: It's similar in purpose to Tinkerpop's 
  `Rexster <https://github.com/tinkerpop/rexster/>`_ but doesn't make use of it.
  You can use it for your remote graphdb work.

- ``printemps.client``: It's a Python ORM for graphdb, it's similar in purpose 
  to `bulbflow <http://bulbflow.com/>`_ an can be used with a Printemps server.
  Flask and Django client integration are planned.

- ``printemps.query``: It's similar in purpose and spirit to Tinkerpop's
  `Gremlin <https://github.com/tinkerpop/gremlin/>`_ but doesn't make use of it.
  You can use it with embedded databases built with the core API or with the 
  client library.

- Planned: ``printemps.pygq``: It allows to query a remote graphdb using pure 
  python functions and methods defined in a custom graph database class or 
  vanilla ``printemps.core.Graph``


The reason of the existence of this project are multiple:

- There is no way to access graph databases from Python as an embedded database,
  except for `neo4j <https://github.com/neo4j/python-embedded/>`_, Printemps
  fixes that.
- Sometime you need more than what Gremlin has to offer, Printemps offers 
  through ``printemps.query`` all is needed to experiment new languages construct 
  against a graph database in a similar architecture as the one used in Gremlin 
  which can be later ported to Gremlin if you really need it.
- Gremlin/Groovy is a nice language but doesn't have the same expresiveness and
  smooth learning curve Python can have, expectially Java doesn't have 
  generators which even if not a beginner language construct can be quiet 
  useful to do 
  `complex and efficiant lookups <http://protractileaigu.blogspot.fr/2012/09/full-text-multi-terms-search-in.html>`. 
  ``printemps.pygq`` fixes one of the reasons why graphdb are not popular, 
  their query langugages; ``pygq`` queries are plain old Python functions, 
  which can be run against a remote ``printemps`` database.
