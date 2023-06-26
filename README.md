# Object_detection
Using yolov8 we are detecting medical images

We are using yolov8 model this is the updated model,which doesnot required to clone project locally
We are detecing object that are mentioned in the class list writen inside the code
We are uploading images and lables in crome driver and import it in colab and map it to train the model 

In yolov8 dataset should be in this format,\n
1.Create folder ex:- first_data_set,\n
2.Create folder as test,val,train
3.With in each folder create image and lable folder 
4.Using makesence.Ai create lables by uploading images and write labels and mape every images to proper labels.
5.At the end export zip file to local folder and paste it in label folder and paste images to image folder 
6.Create data.yaml folder ex:- 
      train: /content/drive/MyDrive/saridon_dolo_data_set/train
      val: /content/drive/MyDrive/saridon_dolo_data_set/val
      test: /content/drive/MyDrive/saridon_dolo_data_set/test
      
      nc: 2
      name: ['Dolo 650', 'Saridon']

