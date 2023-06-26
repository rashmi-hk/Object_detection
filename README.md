# Object_detection
Using yolov8 we are detecting medical images

We are using yolov8 model this is the updated model,which doesnot required to clone project locally
We are detecing object that are mentioned in the class list writen inside the code
We are uploading images and lables in crome driver and import it in colab and map it to train the model 

In yolov8 dataset should be in this format,<br>
1.Create folder ex:- first_data_set,<br>
2.Create folder as test,val,train <br>
3.With in each folder create image and lable folder <br>
4.Using makesence.Ai create lables by uploading images and write labels and mape every images to proper labels. <br>
5.At the end export zip file to local folder and paste it in label folder and paste images to image folder <br>
6.Create data.yaml folder ex:- <br>
      train: /content/drive/MyDrive/saridon_dolo_data_set/train <br>
      val: /content/drive/MyDrive/saridon_dolo_data_set/val <br>
      test: /content/drive/MyDrive/saridon_dolo_data_set/test <br>  
      nc: 2  <br>
      name: ['Dolo 650', 'Saridon']

