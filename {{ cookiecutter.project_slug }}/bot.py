"""Top-level file for {{ cookiecutter.project_name }}.
"""
__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"

import os
import sys

from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
from cards import make_card_payload, ResponseCard

api = WebexTeamsAPI()
app = Flask(__name__)

def send_card(personEmail, card):
    """This is a sample function to show how you can send a adaptive card 
    using pyadaptivecard and the webexteamssdk
    """
    attachment = make_card_payload(card)
    
    api.messages.create(toPersonEmail=personEmail, markdown="fallback text", attachments=[attachment,])

@app.route('/alive')
def alive():
    return "I am up!"

@app.route('/webhook/memberships/created', methods=['POST'])
def webhook_memberships_created():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/memberships/updated', methods=['POST'])
def webhook_memberships_updated():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/memberships/deleted', methods=['POST'])
def webhook_memberships_deleted():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/messages/created', methods=['POST'])
def webhook_messages_created():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/messages/deleted', methods=['POST'])
def webhook_messages_deleted():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/rooms/created', methods=['POST'])
def webhook_rooms_created():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/rooms/updated', methods=['POST'])
def webhook_rooms_updated():
    raw_json = request.get_json()

    return jsonify({'success': True})


@app.route('/webhook/attachmentActions/created', methods=['POST'])
def webhook_attachmentActions_created():
    raw_json = request.get_json()

    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010, debug=True)