from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify({"notes": notes, "total": len(notes)})

@app.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"error": "Title and content are required"}), 400
    note = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "content": data['content'],
        "category": data.get('category', 'General'),
        "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }
    notes.append(note)
    return jsonify({"message": "Note created", "note": note}), 201

@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n['id'] != note_id]
    return jsonify({"message": "Note deleted"}), 200

@app.route('/api/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = data.get('title', note['title'])
            note['content'] = data.get('content', note['content'])
            note['category'] = data.get('category', note['category'])
            return jsonify({"message": "Note updated", "note": note}), 200
    return jsonify({"error": "Note not found"}), 404

@app.route('/health')
def health():
    return jsonify({"status": "OK", "total_notes": len(notes)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
