from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from search import search, load_embeddings
from flask_caching import Cache

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

embeddings_dict = load_embeddings('embeddings.json')

@app.route('/search', methods=['POST'])
def search_endpoint():
    data = request.json
    query = data['query']
    results = search(query, embeddings_dict)
    return jsonify(results)

# Serve static files from the text_files directory
@app.route('/text_files/<path:filename>')
def serve_text_file(filename):
    return send_from_directory('text_files', filename)

# Serve static PDF files from the moodle_files directory
@app.route('/moodle_files/<path:filename>')
def serve_pdf_file(filename):
    return send_from_directory('moodle_files', filename)

if __name__ == '__main__':
    app.run(debug=True)
    

cache = Cache(app)

@app.route('/clear_cache')
def clear_cache():
    cache.clear()
    return "Cache cleared!"