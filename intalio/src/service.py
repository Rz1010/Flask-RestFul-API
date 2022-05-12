from flask import Flask,request,jsonify,send_file


app = Flask(__name__)


@app.route('/audio', methods=['POST'])
def do_process_audio(): 
    from engine import process_audio
    file=request.files['audio']
    audio_chunks_stream=process_audio(file)
    return send_file(
        audio_chunks_stream,
        as_attachment=True,
        attachment_filename='archive.zip'
    )

@app.route('/photo', methods=['POST'])
def do_process_photo(): 
    from engine import process_photo
    file=request.files['photo']
    filex=file.filename
    get=process_photo(filex)
    return jsonify(get)


@app.route('/text', methods=['POST'])
def do_process_text(): 
    from engine import process_text
    file=request.files['text']
    data=file.read().decode("UTF_8")
    get=process_text(data)
    return jsonify(get)


if __name__ == '__main__':
    app.run(debug=True, port=7000)
    
    #app.run(host='0.0.0.0', port=7000)
