# Abstract
The textile sector in Pakistan is a very significant and vital part of the economy a contribution to GDP that amounts to 8.5 percent approximately US$1.2 trillion. In this modern age of fast-changing emerging technologies. The second factor is increasing demand for textile products, coupled with reduced time-to-market, to produce this diverse range of textiles on customer demand. Fashion and textile firms face dynamic challenges from the marketplace, where consumer behavior and global connections change fast.
Mechanization of the production process is one of the significant challenges these industries face. The textile fabrics industry requires, at preset, the detection of defects like holes, stains, and objects by visual means, which is time-consuming, error-prone, and less efficient. Also, continuous monitoring is required to ensure the quality of the products.
This is where industries are turning to automation. Powered by artificial intelligence and machine learning, we have devised a solution to automate this task. For object detection, we have used the state-of-the-art YOLOv8 model, which provides a very robust foundation for defect detection due to its complex, densely built architecture.

<div align="center">
  <img src="https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/a329e5fe-0bbf-4834-8305-9e2116c3d5cf" alt="image" width="500"/>
</div>
<br>
Our model achieved an overall precision of 85%. One of the most used benchmarking datasets for defect detection in fabrics is ZJU-Leaper; it has a dataset size of 98,000 images, wherein 23,000 are defective, and 75,000 are suitable images.
After developing our model, we created a web application with HTML and CSS at the front end and Flask at the back end to support our application. The application prompts two modes: users can provide a live stream camera for real-time detection of defects or an MP4 video and run inference to detect defects in their fabrics. This is thus a centralized application wherein users can link to any device's camera and use it for detection.  


# PROBLEM STATEMENTS

- Manual inspection does not provide immediate feedback, delaying corrective actions and reducing overall efficiency.
- Employing a large workforce for manual inspection is expensive and often unsustainable.
- Manual inspection is prone to human error and inconsistency due to fatigue and subjective judgment.
- Manual inspection is time-consuming, slowing down the production process.

# PROPOSED SOLUTION
<div align="center">
<img src= "https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/5aacb1c3-6ba7-4a48-893d-466d0e6cc3e8">
</div>

We have opted for the YOLOv8 for Object detection of the fabrics defects in Textile Industry. The architecture of this model is really complex and has alot of layers in it.
The yolov8x.pt is the used model for object detection.</br>
# Methodology
<div align = "center">
  <img src = "https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/8b5eb4ff-9c10-45dd-8843-dc9c6906d68c" alt="image" width="500"/>
</div>

# DATA SET
We have used the ZJU Leaper dataset that is the benchmark for fabric defect detection in the textile industry.
<div align="center">
  <img src="https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/420aea9a-636f-445c-a10f-093ca2c181e8" alt="image" width="500"/>
</div>

# Statistics of Dataset
<img src = "https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/207451c0-1631-4539-a4b7-820f75e570b4"/>

# Web Interface
![image](https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/0afba4c3-5312-41f4-beb1-55c368d98457)
</br>

![image](https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/52938d7b-cb84-4d6e-a1ea-d9ed7bc35077)
</br>

# Live Webcam Inference
![image](https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/78eecc92-fe71-49d9-9c77-6323de996fc9)
</br>

# Results
![image](https://github.com/Zeeshanx186/Automated-Vision-System-for-Fabric-Defect-Inspection-/assets/101282364/3f174ee3-f55d-4b76-9afd-6fb37cb1da4a)
<div align="center">
  <img src="https://github.com/user-attachments/assets/3d023574-8596-4c60-9493-487f403f1f54" alt="image" width="500"/>
</div>
<div align="center">
  <img src="https://www.kaggleusercontent.com/kf/123747350/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..eliFjwccjFuwzw96YTWtkA.LD2rOprkNqobLnIV520ayaeT6Gxi8nBV1Fbb_51lO9SsrdpajQ4eR8SI2AAqrKr7_15mUoJooAS78L7p0c8NU1IgQbyU_q0dCKxGCokZ1WNif_OcdyoAwygOz6VyMH2Loo210JSTQgD2kfUX4mfecWBNjCIepJzB2VQslUAeIirAtzJGw6VHWJuZHJ2y1BVAdIhV4_ilYfcJRjTfTou_dnwOFMIqjQ9WLxFpJqoWdhPqDT732tn1QEc1U-CR7zp_WOhxdhY7Zft-R7ExxifPeu_HkeF9iHuvCQKg780k630uV1I1xZjA2LgPsiGNz3flCgWs_C-CUHWWoBMfhGqCMKQxAvUkfQ2qf1d9ay1LjMpaqfQQwuI9-8O9q3YgW-11aV0qvvxeIbj09nDhDcMNT9Y7vJBLyu6Uqdlx-EtN2FqyWwMyb808WAYCQ5dZsB_zJ02nFBlkshFN2larhPBL1LeVBAV1QbG1_d4x_CzXhgc9GXrYJqlri_9P4C8DpX8Vt36zcWJJcoCliEn5EH1OqtuAVWrgXRTpE0I6Z8QsfCz17GF3F2qrIuRU8MXVc1T9dil02PiIC0TiQ4G_c6Ae5Z-zTJ0TD-mga5flAjUwESZsNJwS3n69I270dvxo_Ere.Xadcw3isw_4q9t0edtOwSg/__results___files/__results___35_0.png" alt="image" width="500"/>
</div>
<div align="center">
  <img src="https://www.kaggleusercontent.com/kf/123747350/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..eliFjwccjFuwzw96YTWtkA.LD2rOprkNqobLnIV520ayaeT6Gxi8nBV1Fbb_51lO9SsrdpajQ4eR8SI2AAqrKr7_15mUoJooAS78L7p0c8NU1IgQbyU_q0dCKxGCokZ1WNif_OcdyoAwygOz6VyMH2Loo210JSTQgD2kfUX4mfecWBNjCIepJzB2VQslUAeIirAtzJGw6VHWJuZHJ2y1BVAdIhV4_ilYfcJRjTfTou_dnwOFMIqjQ9WLxFpJqoWdhPqDT732tn1QEc1U-CR7zp_WOhxdhY7Zft-R7ExxifPeu_HkeF9iHuvCQKg780k630uV1I1xZjA2LgPsiGNz3flCgWs_C-CUHWWoBMfhGqCMKQxAvUkfQ2qf1d9ay1LjMpaqfQQwuI9-8O9q3YgW-11aV0qvvxeIbj09nDhDcMNT9Y7vJBLyu6Uqdlx-EtN2FqyWwMyb808WAYCQ5dZsB_zJ02nFBlkshFN2larhPBL1LeVBAV1QbG1_d4x_CzXhgc9GXrYJqlri_9P4C8DpX8Vt36zcWJJcoCliEn5EH1OqtuAVWrgXRTpE0I6Z8QsfCz17GF3F2qrIuRU8MXVc1T9dil02PiIC0TiQ4G_c6Ae5Z-zTJ0TD-mga5flAjUwESZsNJwS3n69I270dvxo_Ere.Xadcw3isw_4q9t0edtOwSg/__results___files/__results___35_1.png" alt="image" width="500"/>
</div>

