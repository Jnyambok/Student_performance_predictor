
<!-- ABOUT THE PROJECT -->
# CI/CD Pipeline for Student Performance Prediction on Microsoft Azure using Github Actions


![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/ba795455-bc59-4d1c-89fd-b5a035618c58)


This Machine Learning project seeks to predict the math scores of students by assessing various dependent factors and has been deployed through:

* Microsoft Azure Cloud Platform
* Running Locally through Flask

## Disclaimer : Please note that this error arises because I have deleted the resources on Azure to save on costs
![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/a12f6a2a-501c-42aa-8aac-ff59b6f7e968)

Refer to this screenshot for the last successful deployment
![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/67745091-721b-464b-b98c-9ef4a8efbc45)




To understand the business case of this project, navigate to the <a href="https://github.com/Jnyambok/end_to_end_azure_ml_project/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb">EDA notebook</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With
[![My Skills](https://skillicons.dev/icons?i=flask,html,python,css,azure,githubactions,vscode)](https://skillicons.dev)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## 1. Local Deployment
Clone this repo and open the project via your preferred IDE.
* Clone this repo :
  ```sh
  https://github.com/Jnyambok/end_to_end_azure_ml_project.git
  ```
* Install Flask through pip:
  ```sh
  pip install flask
  ```
 * Then navigate to the "app.py" file in the directory and run:
  ```sh
  python app.py
  ```
  * Open your preferred browser and run paste :
  ```sh
  http://127.0.0.1:5000/predictdata
  ```

## 2. Deployment through Microsoft Azure Cloud Platform
* Fork this repo and proceed to https://azure.microsoft.com/en-in/free/ to sign up for a free Microsoft Azure account
  
* Navigate to the resource page and search for "Web App". This should take you to the navigation page. Your free subscription will be pre-filled. Select "create new" at the resource group level and provide your preferred name. Provide a web app name that will appear on the search bar name.
  
  ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/331f34e6-47b5-4b60-a560-da0b05b32462)

* Select **python 3.8** as the runtime stack and select the region **closest to your physical location**
  
 ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/0e62d117-5fb3-40cf-bed7-6419ba34d10c)

* Navigate to the **Deployment** section and select **enable**. You will be prompted to link your GitHub account and your forked repo. A workflow configurations file will be added to your repo which will be used to initiate your CI/CD pipeline. To the bottom, ensure basic authentication is off 
  
 ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/473a782e-0588-4857-af4f-3f5fe78ef957)

* You should get the following success message. On your repo, you will find a **.yml** file created for you. This file contains all the necessary metadata for configuring a CI/CD pipeline in Azure through GitHub actions
  
![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/ad3d29cc-e2b6-4310-8ddc-fbb9fd6dd628)

* Navigate to your GitHub repo and go to the **Actions** tab. Your CI/CD pipeline has been set up for you.

  ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/71d18825-a297-4f9c-8507-6d36d25d692d)

* Click the link provided on the **deployment** action and voila:

  ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/9290ecc2-6c65-4a42-8af8-4b5cf0f11f41)

* **Do not forget to delete your Azure resource after you're done. Cloud resources are not cheap!**. Navigate to your resource group on the Azure homepage and delete it.

  ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/42f81626-50cd-4227-9cb5-0bce3881dfc7)


  

<!-- ROADMAP -->
## Future Works and Considerations

- [ ] "Beautify" the home page
- [ ]  Deploy through AWS 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

