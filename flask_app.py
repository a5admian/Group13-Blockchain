#Group 13

from flask import Flask, render_template, request, redirect, url_for
import hashlib
import datetime

class Block:
  def __init__(self, data, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calculate_hash

  def calculate_hash(self):
    hash_data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
    return hashlib.sha256(hash_data.encode()).hexidigest()
