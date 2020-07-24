# Blender_Shapenet_model


First:

use blender --version blender-2.76b-windows64 to generate the different views images(.png) of model & corresponding metadata including (azimuth,altitude,yaw,distance_ratio,fov=25) 
           
           azimuth (0-360), elevation around 30, tilt 0, camera distance to the zero of an object around 0.8m.
            
           remember setting the RGBA to get the background white. 
                                                                
Second:

Follow the order to run scripts in ubuntu   

    bash 1_sample_pc.sh  # upsampling model.obj to model.xyz  
           
           #the key is meshlabserver -i $line -o ${line/.obj/.xyz}  -s $mlx_script
           
           the mlx_script can get by Meshlab - Filters - Sampling - Poisson-dist Sampling. And then Filters - Show current filter script - save scripts. 
    
    python 2_generate_normal.py # calculate normal of model.xyz
           
    python 3_camera_transform.py # transform point cloud according to the PNG image(00.png). Get the point cloud of this view(00.xyz).
    
    python 4_pickle_xyz2dat  #use the standard library pickle in Python to serialize data to .dat files.
