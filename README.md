# Blender_Shapenet_model


First:

use blender --version blender-2.76b-windows64 to generate the different views images of model.

            --get .png image & corresponding metadata including (azimuth,altitude,yaw,distance_ratio,fov=25) 
            
                                                                azimuth (0-360), elevation around 30, tilt 0, camera distance to the zero of an object around 0.8m.
                                                                
Second:

Follow the order to run scripts in ubuntu   
    bash 1_sample_pc.sh
    
    python 2_generate_normal.py
    
    python 3_camera_transform.py
