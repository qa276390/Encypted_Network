
mkdir ../spltJSON
mkdir ../spltJSON/png

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
	jsonpath=../spltJSON/splt_$filename.json
	pngpath=../spltJSON/png/splt_$filename.png
	#echo $filename
	../bin/joy bidir=1 $i | gunzip > $jsonpath
	echo $filename
	python3 read_json.py $jsonpath $pngpath
done
