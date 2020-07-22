#!/bin/bash

mlx_script=upsample.mlx
path=/media/data2/zhangyuqi/Pixel2Mesh/GenerateData/path_path_train_all.txt

#meshlabserver -i 02876657/114509277e76e413c8724d5673a063a6/model.obj -o 02876657/114509277e76e413c8724d5673a063a6/model.xyz -s upsample.mlx
#meshlabserver -i model1.obj -o model1.xyz -s upsample.mlx

cat path | tr "\n" " "

cat $path | while read line;
do
    
    #line=line.strip('\r')
    #echo "meshlabserver ${line}" > tmp.txt
    #echo
    meshlabserver -i $line -o ${line/.obj/.xyz}  -s $mlx_script
done