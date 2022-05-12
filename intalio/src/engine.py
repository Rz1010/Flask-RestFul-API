def process_audio(file):
    from pydub import AudioSegment
    from pydub.silence import split_on_silence,detect_nonsilent
    import os
    from io import BytesIO
    from zipfile import ZipFile
    
    sound = AudioSegment.from_mp3(file)
    timings=detect_nonsilent(sound, min_silence_len=500, silence_thresh=-40 )
    audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )
    #zipfolder = zipfile.ZipFile('Audiofiles.zip','w', compression = zipfile.ZIP_STORED)
    stream = BytesIO()
    with ZipFile(stream, 'w') as zipfolder:
        for i, chunk in enumerate(audio_chunks):
            output_file = str(i)+"_"+str(timings[i])+".mp3"
            chunk.export(output_file, format="mp3")
            zipfolder.write(output_file)
            os.remove(output_file)
    #zipfolder.close()
    stream.seek(0)
    return stream
       
      # chunk.export(output_file, format="mp3")
    
process_audio('test_audio.mp3')

def process_photo(file):
	from PIL import Image
	if file.endswith('pdf') :
	    get={}
	    from pdf2image import convert_from_path
	    pages = convert_from_path(file, 500)
	    for i,page in enumerate(pages):
	       get[i]=process_photo_helper(page) #recursive
	    return get
	img = Image.open(file)
	return process_photo_helper(img)

def process_photo_helper(img) : #gets only images
	import cv2
	import numpy as np
	img = np.array(img)
	img = cv2.resize(img,(300,300))
	img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
	modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
	configFile = "deploy.prototxt.txt"
	net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
	h, w = img.shape[:2]
	blob = cv2.dnn.blobFromImage(img, 1.0,
	(300, 300), (104.0, 117.0, 123.0))
	net.setInput(blob)
	faces = net.forward()
	get={}
	count=0
	for i in range(faces.shape[2]):
		    confidence = faces[0, 0, i, 2]
		    if confidence > 0.5:
		        count=count+1
		        box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
		        (x, y, x1, y1) = box.astype("int")
		        cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
		        get[str(count)]=["X1" , str(x),"Y1" , str(y), "X2", str(x1),"Y2", str(y1)]
	return get
	
def process_text(file):
    import spacy
    lang='en'
    if(lang=='en'):
        nlp = spacy.load('en_core_web_sm')
        article = nlp(file)
        gets={}
        for X in article.ents :
            gets[X.text]=X.label_
        return gets
        
    elif(lang=='ar') :
        import pickle
        car_pickle = open ("/home/fireflood/Desktop/intalio/fun folder/textdet/Arabic-NER-master/ar_test_output/model-final.pickle", "rb")
        car_contents = pickle.load(car_pickle)
        print(car_contents)
        #output_dir='/home/fireflood/Desktop/intalio/fun folder/textdet/Arabic-NER-master/ar_test_output/model-final'
        #print("Loading from", output_dir)
        #nlp = spacy.load(output_dir)
        #nlp
        #data1="و نشر العدل من خلال قضاء مستقل"
        #doc1=nlp(data1)
        #print('Entities', [(ent.text, ent.label_) for ent in doc1.ents])
        