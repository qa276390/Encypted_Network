mkdir -p ../SallJSON

for i in ../SallJSON/*
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
	#../sleuth $i > $jsonpath
	

	python3 Faster_Generator.py $jsonpath
done
