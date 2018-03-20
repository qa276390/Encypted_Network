
item=pk_splt


dir="../${item}_JSON"
pngdir="../${item}_JSON/png"

mkdir $dir
mkdir $pngdir

for i in ../spltJSON/*
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
	jsonpath=$i
	pngpath="$dir/png/${item}_$filename.png"
	#echo $filename
	#../bin/joy bidir=1 $i | gunzip > $jsonpath
	echo $filename
	python3 ${item}_read_json.py $jsonpath $pngpath
done
