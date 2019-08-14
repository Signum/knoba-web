#!/usr/bin/env python3

from flask import Flask, escape, request, render_template
#import sys
import sqlite3
import os.path

BASEDIR='/home/knoba/bot/data'

app = Flask(__name__,
        static_url_path='/static')

@app.route('/<channel>')
def facts(channel):
  #print(channel)
  #channel = request.args.get("channel", "#postfix")
  #return f'Hello, {escape(name)}!'
  #return f'juchu'
  #return sys.version
  #return escape(channel)
  dbfile = os.path.join(BASEDIR, ('#'+channel), 'Factoids.db')
  if not os.path.isfile(dbfile):
      return "Meh..."

  conn = sqlite3.connect(dbfile)
  curs = conn.cursor()
  curs.execute("select keys.key as key,factoids.fact as fact from keys,factoids,relations where keys.id=relations.key_id and factoids.id=relations.fact_id order by key")
  facts = curs.fetchall()
  return render_template('facts.html', channel=channel, facts=facts)

#@app.errorhandler(404)
#def page_not_found(error):
#  return str(error), 404
#  #return render_template('page_not_found.html'), 404

if __name__ == "__main__":
  app.run()
else:
  application = app

