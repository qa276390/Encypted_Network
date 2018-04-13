mkdir -p ../SallJSON
for i in ../allJSON/*
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
	jsonpath=../SallJSON/$filename.json

	echo $2
	../sleuth $i > $jsonpath
	

	#python3 read_json.py $jsonpath ../distJSON/png/dist_$filename.png
done
