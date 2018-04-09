mkdir -p ../allJSON
for i in ../LinktoPCAPS/*
#do
#	set - $(IFS="."; echo $i)
#	tmp=$1
#	echo $tmp
#done
do
	set - $(IFS="."; echo $i)
	tmp=$1
	set - $(IFS="/"; echo $tmp)
	filename=$2
	jsonpath=../allJSON/$filename.json

	../bin/joy tls=1 dns=1 http=1 bidir=1 idp=16 dist=1 entropy=1 $i | gunzip > $jsonpath
	

	#python3 read_json.py $jsonpath ../distJSON/png/dist_$filename.png
done
