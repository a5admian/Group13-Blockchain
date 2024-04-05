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

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain)

@app.route('/add_block', methods=["POST"])
def add_block();
  customer_data = {
      "name": request.form['name'],
      "policy_number": request.form['policy_number'],
      "dob": request.form['dob'],
      "address": request.form['address']
  }
  block = Block(customer_data, blockchain.get_latest_block().hash)
  blockchain.add_block(block)
  return redirect(url_for('index'))
