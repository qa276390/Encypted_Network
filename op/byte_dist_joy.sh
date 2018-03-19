
item=byte_dist


dir="../${item}_JSON"
pngdir="../${item}_JSON/png"

mkdir $dir
mkdir $pngdir

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
	jsonpath="$dir/${item}_$filename.json"
	pngpath="$dir/png/${item}_$filename.png"
	#echo $filename
	../bin/joy dist=1 $i | gunzip > $jsonpath
	echo $filename
	python3 ${item}_read_json.py $jsonpath $pngpath
done
