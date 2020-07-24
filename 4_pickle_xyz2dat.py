import pickle
import os
import io
import numpy as np
if __name__ == '__main__':

  obj_path = '03642806.txt'
    
  with open(obj_path, 'r') as f:
      while (True):
          line = f.readline()
          if not line:
              break
          line = line.replace('\n', '')
          print(line)
          rendering_path = line.replace("model.obj","rendering")
          for i in range(8):
              xyz_path=os.path.join(rendering_path ,'%.2d.xyz'% i)
              dat_path=os.path.join(rendering_path ,'%.2d.dat'% i)
              #print(dat_path)
              
              #with io.open(xyz_path,'r',encoding='utf-8') as src, io.open(dat_path,'wb') as dest:
              #src=io.open(xyz_path,'r',encoding='utf-8')
              src=open(xyz_path,'r')
              dest=open(dat_path,'wb')
              lines=src.readlines()
              #pickle.dump(len(lines),dest)
              dat_array = np.zeros((len(lines), 6), np.float32)
              #y = [[np.float32(i) for i in s.split()] for s in x]
              for i in range(len(lines)):
                  line=lines[i].split()
                  # line= line.split()
                  # line_float = []
                  for j in range(len(line)):
                      dat_array[i, j] = np.float32(line[j])
                      #line_float.append(np.float32(num))
              #print(type(dat_array))
              #print(dat_array.shape)
              #print(type(dat_array[0,0]))
              pickle.dump(dat_array, dest)
              #print(dat_array)
              dest.close()
              '''
              label1 = pickle.load(io.open(dat_path, 'rb',))
              print(type(label1))
              print(label1)w
              
              label2 = pickle.load(io.open('./00_P2M.dat', 'rb'))
              print(label2)
              print(type(label2))
              #print(label2.shape)
              
              with open('./00_P2M_new.dat', 'wb') as new_p2m:
                  pickle.dump(label2, new_p2m)
              new_p2m.close()
              
              label3 = pickle.load(io.open('./00_P2M_new.dat', 'rb'))
              print(type(label3))
              '''
        
        
  
        
      