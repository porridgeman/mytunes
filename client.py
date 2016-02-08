#!/usr/bin/env python

import rethinkdb as r

conn = r.connect( "rolandmechler.com", 28015, db="rmechler")

for change in r.table('controllers').changes().run(conn):
  print change['new_val']['time']

