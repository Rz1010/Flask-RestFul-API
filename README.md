This is a wiki on how to use my REST API , you should POST files to the API and recieve the output

Information : 

This RESTApi consumes a POST request with a file in the body.
The API is deployed through a docker container , having a gunicorn production server 
and a nginx reverse proxy server.

Installation :

Please use the compose module of docker in the main directory : 

docker compose up



There are 3 modes :

*Face Detection* : 

Will return a dictionary with the coordinates of the rectangle surrounding the face in an image 
Also Supports pdf

Usage : 

curl 0.0.0.0/photo -F "photo=@local/dir/of/image"


*Text Named Entity Detection*

Will return a dictionary with the named entity in a file of text

Usage : 

curl 0.0.0.0/text -F "text=@local/dir/of/text_file"


*Un-Silent Audio Deteciton*

Will return a zip file with the chunks of unsilent audio given a mixed audio file
where the name of chunks is as numberofchunk_[start_time end_time].mp3

Usage :

curl 0.0.0.0/audio -F "audio=@/local/dir/of/audio_file" --output unsilent.zip

 
