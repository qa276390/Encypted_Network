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
	jsonpath=../distJSON/dist_$filename.json
	#echo $filename
	../bin/joy dist=1 $i | gunzip > $jsonpath
	echo $filename
	python3 read_json.py $jsonpath ../distJSON/png/dist_$filename.png
done