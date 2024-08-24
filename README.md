ML Model Info: Acheived a jacard index of 0.801 for segmentation , finetuned SAM which is a VIT based model on the skin data for segmentation.<br>
Hugging Face Repo Link: https://huggingface.co/Virendrasinh10/Fine_tuned_SAM_for_skin_disearse_segmentation/tree/main.<br>
Used DCNNs for skin disease classification(used transfer learning based approach utilising DenseNet121 ResNET and VGGnet in different iterations of the process for feature extraction, the DenseNet approach gave the best results in this case).<br><br>
Can utilise the weights of the trained model for any further tasks. 
About the Platform:<br>
<li>A comprehensive tele-medicine platform for early detection of fatal skin diseases. Using powerful CNN models to diagnose possibility of fatal diseases and generate doctor recommendations.</li><br>
<li>Implemented the backend using Flask, Geolocation based doctor recommendation feature by integrating OpenStreet Map and added feature of getting diagnostic information over email. </li>


Homepage:
![image](https://github.com/user-attachments/assets/a04b21c5-2640-4bb6-aa2f-869cf7e7b88a)

Doctor Recommendation based on Location: 
![image](https://github.com/user-attachments/assets/ddafda3a-b217-4fde-a827-b38ed10ceef9)

Report Generated and sent via email:
![image](https://github.com/user-attachments/assets/e2295ee5-b0c2-4f95-ab93-15843d41fbb4)

<br>
Steps to run the project locally:
<li>Clone this repo</li>
<li>Install the required libraries mentioned in requirements.txt <br>
pip install -r -requirements.txt</li>
<li>Move to the directory containing the app.py file</li>
<li>Execute python app.py, the Flask server will be running at localhost:5000 by default</li>
<br>
